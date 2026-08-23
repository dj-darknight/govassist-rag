import json, re, pandas as pd
from rank_bm25 import BM25Okapi
from ranx import Qrels, Run, evaluate

DATA = "/home/claude/check/extracted"

# --- Load collection ---
docs = []
with open(f"{DATA}/collection.jsonl") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        docs.append((d["id"], d["contents"]))

doc_ids = [d[0] for d in docs]

def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())

tokenized_corpus = [tokenize(t) for _, t in docs]
bm25 = BM25Okapi(tokenized_corpus)

# --- Load topics (queries) ---
topics = pd.read_csv(f"{DATA}/topics_clean.csv")

# --- Run BM25 retrieval, top 100 per question ---
run_dict = {}
for qid, question in topics[["question_id", "question"]].values:
    scores = bm25.get_scores(tokenize(str(question)))
    ranked = sorted(zip(doc_ids, scores), key=lambda x: -x[1])[:100]
    run_dict[qid] = {docid: float(score) for docid, score in ranked if score > 0}

run = Run(run_dict, name="bm25-reproduction")

# --- Load qrels ---
qrels_df = pd.read_csv(f"{DATA}/qrels_clean.txt", sep="\t", header=None,
                        names=["q_id", "iter", "doc_id", "score"],
                        dtype={"q_id": str, "doc_id": str})
qrels_df["q_id"] = qrels_df["q_id"].astype(object)
qrels_df["doc_id"] = qrels_df["doc_id"].astype(object)
qrels_full = Qrels.from_df(qrels_df, q_id_col="q_id", doc_id_col="doc_id", score_col="score")

# --- Derive question types (per DATA_GUIDE.md) ---
max_rel = qrels_df.groupby("q_id").score.max()
all_qids = set(topics["question_id"])
qrel_qids = set(qrels_df["q_id"])

known_ids = [q for q in all_qids if q in max_rel.index and max_rel[q] == 2]
inferred_ids = [q for q in all_qids if q in max_rel.index and max_rel[q] == 1]
out_of_kb_ids = [q for q in all_qids if q not in qrel_qids]

print(f"Known: {len(known_ids)}  Inferred: {len(inferred_ids)}  Out-of-KB: {len(out_of_kb_ids)}")
print(f"(paper reference: known 84, inferred 12, out_of_kb 10)\n")

def eval_subset(name, qids):
    qids = [q for q in qids if q in qrels_df["q_id"].values]
    if not qids:
        print(f"{name}: no qrels available")
        return
    sub_qrels_df = qrels_df[qrels_df["q_id"].isin(qids)]
    sub_qrels = Qrels.from_df(sub_qrels_df, q_id_col="q_id", doc_id_col="doc_id", score_col="score")
    sub_run_dict = {q: run_dict[q] for q in qids if q in run_dict}
    sub_run = Run(sub_run_dict, name="bm25-reproduction")
    results = evaluate(sub_qrels, sub_run, ["ndcg@1", "ndcg@3", "ndcg@5"])
    print(f"{name} (n={len(qids)}): {results}")

eval_subset("Known", known_ids)
eval_subset("Inferred", inferred_ids)

# Out-of-KB: correct behaviour is to return nothing / abstain.
# Since this naive BM25 always returns top matches (no abstention mechanism),
# report how often it returns *any* result for out-of-KB queries as a proxy
# for the "should have abstained but didn't" failure mode.
answered_out_of_kb = sum(1 for q in out_of_kb_ids if run_dict.get(q))
print(f"\nOut-of-KB (n={len(out_of_kb_ids)}): naive BM25 returned a result (i.e. failed to "
      f"abstain) for {answered_out_of_kb}/{len(out_of_kb_ids)} "
      f"({100*answered_out_of_kb/len(out_of_kb_ids):.0f}%)")
