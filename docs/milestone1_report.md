# WIL Project — Milestone 1 Report

**Group ID:** `<GROUP-ID>` *(must match the Canvas group)*
**Project name (optional):** `<PROJECT NAME>`
**Date:** `<DD Month YYYY>`

---

## 1. Group and Project Links

| Item | Link / Value |
|---|---|
| Group ID (Canvas) | `<GROUP-ID>` |
| Trello board (teaching team has view access) | `<https://trello.com/b/XXXXXXXX/...>` |
| GitHub repository (private) | `<https://github.com/<org-or-user>/<repo>>` |
| README contains | Group ID, full member list, project aim, setup instructions |
| Access | Mentor `<mentor name / GitHub handle>` to be added as collaborator on request |

---

## 2. Project Aim Statement

> **Aim (one sentence):** We aim to build and rigorously evaluate a retrieval-augmented conversational agent that answers `<TARGET USER>`'s frequently asked questions about `<DOMAIN / KNOWLEDGE BASE>`, extending the Walert approach with `<YOUR EXTENSION — e.g. a larger document collection, a modern open-weight LLM, hallucination-aware answer abstention>`.

### 2.1 User Stories (Connextra format)

| ID | User Story | Acceptance criteria |
|---|---|---|
| US-01 | As a **prospective student**, I want to **ask a natural-language question about program structure**, so that **I get an accurate answer without reading the entire FAQ document**. | Answer is grounded in a retrieved passage; response < 5 s. |
| US-02 | As a **prospective student**, I want the agent to **tell me when it does not know**, so that **I am not misled by a fabricated answer**. | Out-of-KB questions return an explicit "I don't have an answer" ≥ `<X>`% of the time. |
| US-03 | As a **prospective student**, I want to **phrase my question in my own words**, so that **I don't have to guess the exact wording used in the FAQ**. | Paraphrased query variants retrieve the same gold passage. |
| US-04 | As a **course coordinator**, I want to **update the knowledge base without retraining the model**, so that **answers stay current at low maintenance cost**. | New document indexed and retrievable within one pipeline run. |
| US-05 | As a **developer on the team**, I want **a reproducible evaluation harness**, so that **I can compare retrievers and generators on the same test collection**. | Single command reproduces NDCG / BERTScore / ROUGE-1 tables. |
| US-06 | As a **teaching-team assessor**, I want **every claim in the demo traceable to a source passage**, so that **I can verify the system is not hallucinating**. | Each answer displays its supporting passage IDs. |

*(Trim to 3–4 stories if page budget is tight.)*

---

## 3. Team Members

| Student ID | Full Name | Proposed Role | Relevant Skills |
|---|---|---|---|
| `sXXXXXXX` | `<Name>` | Team Lead / Scrum Master | Agile facilitation, stakeholder comms, Trello/Jira |
| `sXXXXXXX` | `<Name>` | Retrieval Engineer | Python, Pyserini/Elasticsearch, BM25, dense retrieval |
| `sXXXXXXX` | `<Name>` | LLM / Generation Engineer | HuggingFace, prompt engineering, quantised inference |
| `sXXXXXXX` | `<Name>` | Data & Knowledge Base Lead | Data cleaning, passage chunking, annotation, qrels |
| `sXXXXXXX` | `<Name>` | Evaluation Lead | IR metrics (NDCG, MAP), BERTScore/ROUGE, statistics |
| `sXXXXXXX` | `<Name>` | Frontend / Integration | React or Streamlit, REST APIs, deployment, Docker |

*Roles are indicative; all members contribute to code review and documentation.*

---

## 4. Progress to Date

### 4.1 Team setup
- Canvas group formed, roles assigned, weekly meeting cadence agreed (`<day/time>`), stand-up notes in Trello.
- Private GitHub repo created with `README.md` (Group ID + members), branch protection on `main`, PR-based workflow.
- Trello board configured with Backlog / Sprint / In Progress / Review / Done columns; Milestone 1 tasks tracked as cards.

### 4.2 Reproducing the Walert RAG approach
We cloned `https://github.com/rmit-ir/walert` and ran the pipeline in `quantitative_eval/` against the released test collection.

**Testbed as released (Pathiyan Cherumanal et al., CHIIR 2024):** 120 passages and 106 questions (including paraphrase variants) split into 84 *Known* (direct answer in the FAQ), 12 *Inferred* (answer must be composed from multiple partially relevant passages), and 10 *Out-of-KB* questions (no supporting passage; the gold answer is an explicit refusal).

**Pipeline reproduced:** sparse retrieval with BM25 (`k1 = 1.2`, `b = 0.75`) and dense retrieval with DPR via Pyserini, feeding the top-*k* passages (*k* ∈ {1, 3, 5}) into an instruction-tuned generator with the paper's answer-synthesis prompt (answer from retrieved documents, else return NA). Evaluation covers the retrieval stage (NDCG) and the end-to-end answer (BERTScore, ROUGE-1), reported separately per question type.

**Reference (published) figures we are reproducing against:**

| Approach | Cutoff *k* | Known NDCG | Known BERTScore | Known ROUGE-1 | Inferred NDCG | Inferred BERTScore | Out-of-KB % unanswered |
|---|---|---|---|---|---|---|---|
| Intent-Based (baseline) | – | 0.6429 | 0.771 | 0.671 | 0.0833 | 0.332 | 80 |
| RAG (BM25 + Falcon-7B-instruct) | 1 | 0.5119 | 0.536 | 0.179 | 0.1667 | 0.493 | 0 |
| RAG (BM25 + Falcon-7B-instruct) | 3 | 0.4912 | 0.543 | 0.209 | 0.2556 | 0.447 | 10 |
| RAG (BM25 + Falcon-7B-instruct) | 5 | 0.4733 | 0.543 | 0.209 | 0.3291 | 0.447 | 10 |
| RAG (DPR + Falcon-7B-instruct) | 1 | 0.6905 | 0.545 | 0.193 | 0.2500 | 0.513 | 10 |
| RAG (DPR + Falcon-7B-instruct) | 3 | 0.6119 | 0.564 | 0.244 | 0.2350 | 0.476 | 20 |
| RAG (DPR + Falcon-7B-instruct) | 5 | 0.5812 | 0.564 | 0.244 | 0.2350 | 0.476 | 20 |

**Our reproduction (fill with your own run — do not submit the table above as your result):**

| Run | Retriever | Generator | *k* | NDCG (Known) | NDCG (Inferred) | BERTScore | ROUGE-1 | % Unanswered (Out-of-KB) |
|---|---|---|---|---|---|---|---|---|
| R1 | BM25 | `<model>` | 1 | `<>` | `<>` | `<>` | `<>` | `<>` |
| R2 | BM25 | `<model>` | 3 | `<>` | `<>` | `<>` | `<>` | `<>` |
| R3 | DPR | `<model>` | 1 | `<>` | `<>` | `<>` | `<>` | `<>` |
| R4 | DPR | `<model>` | 3 | `<>` | `<>` | `<>` | `<>` | `<>` |

**Observations so far (edit to match your numbers):**
1. Retrieval quality dominates end-to-end quality — dense retrieval gives the strongest NDCG on *Known* questions at `k = 1`.
2. Aggressive truncation helps generation: fewer passages in the prompt yielded higher BERTScore/ROUGE-1, so more context is not automatically better.
3. RAG clearly beats the intent-based baseline on *Inferred* questions, which require combining multiple partially relevant passages.
4. The main weakness is abstention: the RAG configurations answer nearly every out-of-KB question instead of refusing, which is exactly the hallucination risk our project targets.
5. `<Any deviation you observed from published numbers, e.g. different generator checkpoint, tokenizer version, or BERTScore model — state it explicitly.>`

**Environment:** `<Python 3.x, Pyserini x.y, transformers x.y, GPU/CPU, seed>` — pinned in `requirements.txt`; run scripts under `/experiments`.

---

## 5. Plan for the Next Three Weeks

| Week | Sprint goal | Key tasks | Owner | Deliverable |
|---|---|---|---|---|
| Week 1 | Lock the baseline | Finish full reproduction across all *k*; pin dependencies; write `run_all.sh`; document metric definitions | Retrieval + Evaluation leads | Reproducible baseline table committed to repo |
| Week 2 | Extend the pipeline | Swap in `<modern open-weight LLM>`; add `<hybrid / re-ranking>` retrieval; expand KB with `<additional documents>`; add abstention prompt + threshold | LLM + Data leads | New runs benchmarked against baseline |
| Week 3 | Evaluate and demo | Ablation on *k* and abstention threshold; significance testing; error analysis on out-of-KB failures; minimal demo UI; draft Milestone 2 report | Whole team | Results tables, working demo, report draft |

Working method: one-week sprints, Trello cards mapped to the user stories above, Monday planning and Friday review, all code merged via pull request with at least one reviewer.

---

## 6. Risks and Bottlenecks (optional section)

| # | Risk / bottleneck | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| R1 | Compute access for LLM inference (GPU quota / cost) | High | Medium | Use quantised 7B models; batch offline; fall back to CPU-friendly or hosted API |
| R2 | Exact reproduction blocked by deprecated model checkpoints or library versions | Medium | Medium | Pin versions; document substitutions and report both configurations |
| R3 | Small test collection (106 questions) limits statistical power | Medium | High | Report significance tests; extend the question set with new annotated items |
| R4 | Hallucination on out-of-KB questions | High | High | Explicit abstention prompt, retrieval-score threshold, human spot-check |
| R5 | Uneven workload / member availability across assessment periods | Medium | Medium | Rotate roles, pair programming, buffer in sprint plan |
| R6 | Data sensitivity if the KB includes internal documents | Medium | Low | Keep repo private; self-host the model; no third-party API calls on sensitive text |

---

## References

- Pathiyan Cherumanal, S., Tian, L., Abushaqra, F. M., Magnossão de Paula, A. F., Ji, K., Ali, H., Hettiachchi, D., Trippas, J. R., Scholer, F., & Spina, D. (2024). *Walert: Putting Conversational Information Seeking Knowledge into Action by Building and Evaluating a Large Language Model-Powered Chatbot.* CHIIR '24. https://doi.org/10.1145/3627508.3638309 (preprint: arXiv:2401.07216)
- Walert code and data: https://github.com/rmit-ir/walert
- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS.
- Karpukhin, V. et al. (2020). *Dense Passage Retrieval for Open-Domain Question Answering.* EMNLP.
- Robertson, S. E. et al. (1995). *Okapi at TREC-3.*
- Lin, J. et al. (2021). *Pyserini: A Python Toolkit for Reproducible Information Retrieval Research.* SIGIR.
- Zhang, T. et al. (2020). *BERTScore: Evaluating Text Generation with BERT.* ICLR.
- Lin, C.-Y. (2004). *ROUGE: A Package for Automatic Evaluation of Summaries.* ACL Workshop.
- Järvelin, K., & Kekäläinen, J. (2002). *Cumulated Gain-Based Evaluation of IR Techniques.* ACM TOIS.

---

## Appendix A — README template for the GitHub repo

```markdown
# <Project Name> — WIL Project
**Group ID:** <GROUP-ID>

## Team
| Student ID | Name | Role |
|---|---|---|
| sXXXXXXX | <Name> | Team Lead |
| ... | ... | ... |

## Aim
<One-sentence aim statement>

## Repository structure
- `data/`        knowledge base passages, questions, qrels
- `src/`         retrieval and generation pipeline
- `experiments/` run scripts and configs
- `results/`     metric outputs

## Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash experiments/run_all.sh

## Links
- Trello: <link>
- Milestone reports: `docs/`
```
