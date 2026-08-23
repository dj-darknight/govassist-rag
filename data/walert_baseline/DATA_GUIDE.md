# Walert Raw Data — What's In Here and How To Use It

Source: `https://github.com/rmit-ir/walert` (RMIT IR Group). Released with the CHIIR '24 paper.
Citation file: `CITATION.bib`. Cite it in your report — this is someone else's dataset.

## Important framing point

**You do not "train" on this data.** RAG has no training step. The FAQ passages are the
knowledge base you index and retrieve from; the questions + qrels + gold answers are the
**test collection** you evaluate against. Nothing here is a training split. If your report
says "training data", a marker who knows this paper will notice.

The only thing that was ever *trained* in the original work is the intent-based Alexa model
(`intent_mapping.csv`), which is the non-RAG baseline. The data README says explicitly that
this file is not used to build RAG.

---

## Folder: `chiir24_data/` — the collection used in the paper

This is the version whose numbers appear in the published results table. Use this one for
your reproduction.

| File | Rows | What it is |
|---|---|---|
| `collection.csv` | 120 passages | The knowledge base. Columns: `passage_id` (P01…), `passage` (raw FAQ text). |
| `collection.jsonl` | 120 | Same corpus in Pyserini/Anserini index format: `{"id": "P01", "contents": "..."}`. **Index this file.** |
| `collection/collection.jsonl` | 120 | Identical copy in a subfolder — Pyserini's indexer takes a *directory*, so point `--input` at `collection/`. |
| `topics.csv` | 106 questions | The queries. Columns: `topic_id` (W01…), `topic` (original FAQ question), `question_id` (W01Q01…), `question` (paraphrase variant). 43 unique topics, 1–4 paraphrases each. |
| `qrels.txt` | 500 judgements | TREC qrels format, tab-separated: `question_id  0  passage_id  relevance`. Relevance 2 = fully relevant, 1 = partially relevant. Feed straight to `trec_eval`. |
| `groundtruth.csv` | 140 | Topic→passage mapping with the passage text inline and the relevance judgement. Human-readable version of qrels. |
| `gold_summaries.csv` | 114 | Reference answers for generation scoring. Columns: `question_id`, `summary_id`, `summary`, `passage_id`. This is what you compare generated answers against with BERTScore / ROUGE-1. |
| `intent_mapping.csv` | 346 | Intent-based baseline only. **Not for RAG.** |
| `walert_intent_results.csv` | 106 | Outputs of the deployed Alexa intent system, for baseline comparison. |
| `Walert_NLU_Testing_Results.json` | — | Raw Alexa NLU evaluation dump (in the 2024 folder). |

### The three question types — derive them yourself from qrels

The paper reports results broken down by question type, but there is no `type` column.
You compute it:

| Type | Rule | Count |
|---|---|---|
| **Known** | question has at least one qrel with relevance **2** | 84 |
| **Inferred** | question's maximum qrel relevance is **1** (only partial passages) | 12 |
| **Out-of-KB** | question ID appears in `topics.csv` but **not at all** in `qrels.txt` | 10 |

```python
import pandas as pd
topics = pd.read_csv("topics.csv")
qrels = pd.read_csv("qrels.txt", sep="\t", header=None,
                    names=["question_id", "iteration", "passage_id", "relevance"])
max_rel = qrels.groupby("question_id").relevance.max()

def qtype(qid):
    if qid not in max_rel.index:
        return "out_of_kb"
    return "known" if max_rel[qid] == 2 else "inferred"

topics["qtype"] = topics.question_id.map(qtype)
print(topics.qtype.value_counts())   # known 84, inferred 12, out_of_kb 10
```

The 10 out-of-KB question IDs are: `W33Q01, W34Q01, W35Q01, W36Q01, W37Q01, W38Q01,
W40Q1, W41Q1, W42Q1, W43Q1`. Note the inconsistent ID format (`W40Q1`, not `W40Q01`) —
string-matching on a `QQ\d\d` pattern will silently drop four of them. The 12 inferred
questions are `W21Q01` through `W32Q01`.

For out-of-KB questions the correct behaviour is refusal, so score them on **% unanswered**,
not NDCG. This is where RAG performs worst in the paper (0–20% correct refusal versus 80%
for the intent baseline) and is the most defensible thing for your project to improve.

---

## Folder: `updated_2024_data/` — later revision

Same file names, revised content (`collection.csv`, `topics.csv` and `qrels.txt` all differ
from the CHIIR version). Also contains `chunking_gen/` — retrieval outputs from a chunking
experiment (`Chunking_OkapiBM25_sentence_k{1,3,5}.csv`, columns include `retrieved_list`,
`top_k`, `Chunking_Type`, `split_length`, `split_overlap`).

**Reproduce against `chiir24_data/` first.** If you mix versions, your numbers won't match
the published table and you won't be able to tell whether the gap is your pipeline or the
data. Once the baseline is locked, the 2024 version is a reasonable extension target.

---

## Folder: `reference_runs/` — the authors' own outputs

| Path | Contents |
|---|---|
| `runs/rag-bm25.txt`, `runs/rag-dense-faiss.txt`, `runs/walert-intent.txt` | TREC run files from the paper's three systems |
| `trec_eval_results/` | Their `trec_eval` output (`.txt`) and LaTeX tables (`.tex`) |
| `summaries/falcon_bm25_eval.csv`, `falcon_dense_eval.csv`, `walert_eval.csv` | Per-question generated answers with BERTScore/ROUGE |

Use these as a correctness check: if your BM25 run file doesn't closely match theirs on the
same collection, your indexing or query handling is off, and there's no point moving on to
generation until it does.

---

## Folder: `pipeline_code/`

- `retrieval/` — `index-bm25.sh`, `encode.sh`, `index.sh`, `search.py`, `search.sh`,
  `eval.py`, `data.py`, `main.sh`, plus `RAG_SYSTEM.py` and `RAG_Voice_Demo.py`
- `nlg/` — `falcon_gen.py` (generation), `eval.py`, `end2end_eval.R`, `falcon_details.txt`
- `requirements.txt` — the original pinned environment (2023 versions; `faiss==1.7.4`,
  `huggingface-hub==0.16.4`, etc.)

Expect the pinned environment to fight you on a modern machine. Install into a fresh venv,
and if you have to bump versions or swap the generator, record it — that's a legitimate
deviation to report, not a failure.

---

## Minimal reproduction path

```bash
# 1. Sparse index over the 120 passages
python -m pyserini.index.lucene \
  --collection JsonCollection --input chiir24_data/collection/ \
  --index indexes/bm25 --generator DefaultLuceneDocumentGenerator \
  --threads 1 --storePositions --storeDocvectors --storeRaw

# 2. Retrieve (queries = the `question` column, ids = `question_id`)
#    write TREC format: qid Q0 docid rank score runtag

# 3. Score retrieval
trec_eval -m ndcg -m ndcg_cut.1,3,5 chiir24_data/qrels.txt runs/your-run.txt

# 4. Generate answers from top-k passages, then score against gold_summaries.csv
#    with BERTScore and ROUGE-1, broken down by question type
```

Two gotchas that cost people a day each: the CSVs are CRLF-terminated with quoted multi-line
fields, so parse with `pandas.read_csv`, never `split(",")`; and evaluate at
`question_id` level (106 queries), not `topic_id` level (43) — mixing these up changes
every number you report.
