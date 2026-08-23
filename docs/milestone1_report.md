# Milestone 1 — Project Progress Report

**Project:** GovAssist RAG — An evaluated RAG-based assistant for improving access to
Australian Government service information
**Unit/Subject:** Case Studies in Data Science
**Group ID:** 49
**Date:** 23 August 2026

---

## 1. Group Details & Links

- **Group ID:** 49 (as listed on Canvas)
- **Trello board:** https://trello.com/b/obfnzOND/govassist-rag-assistant

The repository README contains the Group ID and full list of team members, and the assigned
mentor will be given access.

---

## 2. Project Aim Statement

GovAssist RAG is a retrieval-augmented assistant that helps Australians quickly find accurate,
source-verified information about JobSeeker Payment eligibility, payments, and application
steps — reducing the confusion and misinformation risk of navigating scattered government
websites.

### User Stories

- As a **recently unemployed person**, I want to ask a simple question about payment
  eligibility, so that I don't have to manually search through multiple government pages to
  understand if I qualify.
- As a **recently retrenched tech worker**, I want to ask about redundancy pay, tax treatment,
  and Centrelink waiting periods in one place, so that I can plan my finances without
  misreading a scattered set of official pages.
- As a **sponsored visa holder who has lost their job**, I want a clear, sourced answer about
  my visa cessation window, so that I don't rely on outdated or incorrect information found
  online.

---

## 3. Progress So Far

The team has set up a Trello board to organise tasks, assign clear responsibilities, and
monitor daily progress. For software development and version control, we configured a private
GitHub repository to ensure secure code sharing, accurate tracking, and seamless collaboration.
Supported by these defined roles and consistent team communication, we adopted an incremental
development strategy — prioritising a stable, fully functional core system before building out
secondary features.

We also scoped the target knowledge base for our use case: a 15-subtopic taxonomy covering
redundancy entitlements, JobSeeker eligibility and waiting periods, superannuation, visa
implications, and related domains, each traceable to a named official publisher (Fair Work
Ombudsman, Services Australia, ATO, Home Affairs, DEWR, ASIC Moneysmart, and Jobs and Skills
Australia). This plan is documented in full in `docs/knowledge_base_plan.md` in the repository.

**Preliminary Walert reproduction results:**

> TODO — this section is required by the brief and not yet complete. Once the BM25 index is
> built over the 120-passage `chiir24_data` collection and evaluated with `trec_eval` against
> `qrels.txt`, report at minimum: NDCG@5/@10 against the published Walert BM25 numbers, and a
> breakdown by question type (known / inferred / out-of-KB) as described in `DATA_GUIDE.md`.
> Insert those figures here before submission.

---

## 4. Planned Tasks for the Next Three Weeks

**Week 1 — Dataset Preparation and Baseline Setup**
We will collect relevant information from official Australian Government websites, focusing on
services, payments, concessions, eligibility requirements, and application processes. The
collected information will be cleaned and organised into a manageable knowledge base. We will
then adapt the Walert RAG baseline to our Australian Government services use case and prepare a
set of questions for initial testing.

**Week 2 — RAG Development and Testing**
Using the prepared knowledge base, we will develop and improve the RAG pipeline, testing how
well the system retrieves relevant information and generates useful, well-supported answers. We
will identify issues such as incorrect retrieval or unsupported answers and iterate accordingly.

**Week 3 — Evaluation and Final Analysis**
In the final week, we will evaluate the improved RAG system using measures such as answer
correctness, faithfulness, and citation accuracy, and check whether the system correctly
abstains when there is not enough supporting information. We will compare results against the
Walert baseline, discuss strengths and limitations, and summarise key findings.

---

## 5. Expected Outcome

By the end of the next three weeks, the team aims to have a functional early prototype of the
Government Services RAG Assistant focused on Employment Assistance. The prototype should accept
a user's natural language question, retrieve relevant chunks from the corpus via a vector store,
and generate a grounded response using only retrieved content, with supporting source(s)
displayed alongside the answer.

Alongside the prototype, the team will run an initial evaluation pass using a small set of test
questions with known answers, to verify whether responses are accurately grounded in source
material or include hallucinated content. The project scope and technical implementation will
continue to be refined based on these results.

The overall development strategy is to first establish a reliable minimum viable RAG system for
the chosen category, then progressively improve retrieval quality, response accuracy, usability,
and evaluation coverage in subsequent phases — expanding to additional service categories only
if time and technical capacity allow.

---

## 6. Bottlenecks & Risks

- **Preliminary Walert reproduction is not yet complete** — the pinned 2023 dependency versions
  (`faiss==1.7.4`, `huggingface-hub==0.16.4`) may require version bumps on a modern machine; any
  deviation will be recorded.
- **Time-sensitive government content** (e.g. tax-free thresholds, visa cessation window
  lengths) requires careful date-stamping to avoid the system confidently quoting outdated
  figures.

---

## 7. Group Members and Roles

| Student ID | Full Name | Roles / Skills / Strengths | % Contribution |
|---|---|---|---|
| 4175665 | Diya Jindal | Project Coordinator | 20% |
| 4232687 | Divyanshu | Data & Ingestion + RAG | 20% |
| 4192016 | Priya Prashantha | Report writing + Trello board | 20% |
| 4187984 | Salman Beg | Documentation | 20% |
| 4216778 | Sucheta Mohanty | Report writing | 20% |
| **Total** | | | **100%** |

All group members have been assigned to the corresponding group on Canvas.

---

## References

- Es, S., James, J., Espinosa Anke, L., & Schockaert, S. (2024). RAGAs: Automated Evaluation of
  Retrieval Augmented Generation. *Proceedings of EACL 2024*, 150–158.
- Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., &
  Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing
  Surveys, 55*(12), Article 248. https://doi.org/10.1145/3571730
- Karpukhin, V., Oğuz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W. (2020).
  Dense passage retrieval for open-domain question answering. *Proceedings of the 2020
  Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 6769–6781.
  https://doi.org/10.48550/arXiv.2004.04906
- Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
  *Advances in Neural Information Processing Systems*, 33.
