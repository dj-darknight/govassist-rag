### An evaluated RAG-based assistant for improving access to Australian Government service information — WIL Project

## Group ID: 49

## Aim

A retrieval-augmented assistant that helps recently retrenched Australian tech workers find accurate, source-grounded information on redundancy entitlements, JobSeeker eligibility, visa implications, and reskilling pathways — extending the Walert (Pathiyan Cherumanal et al., 2024) approach with a larger, higher-stakes domain and explicit hallucination-aware abstention.

## Repository structure
data/walert_baseline/ — Walert reproduction dataset, used to baseline our pipeline
data/knowledge_base/ — our own ~150–200 passage corpus across 15 subtopics (not yet built — see docs/knowledge_base_plan.md for the taxonomy and sourcing plan)
src/ — retrieval, generation, and evaluation pipeline (not yet started)
experiments/ — run scripts and configs (currently: run_bm25_eval.py, a preliminary BM25 reproduction over the Walert baseline collection, with methodology notes in experiments/README.md)
results/ — metric outputs
docs/ — milestone reports and the knowledge base plan (milestone1_report.md, knowledge_base_plan.md)
Setup

## Preliminary Walert BM25 reproduction (what's runnable today):

bash
pip install rank_bm25 ranx pandas
python experiments/run_bm25_eval.py

See experiments/README.md for what this script does, why it substitutes for the original pyserini-based pipeline, and how to run the official pipeline instead if you have unrestricted network access.

Full project pipeline (src/, data/knowledge_base/) is still in development — setup instructions will be added here once those components exist.

## Team

See docs/milestone1_report.md for full team member list, roles, and project progress.

## Links
Trello board: https://trello.com/b/obfnzOND/govassist-rag-assistant
Knowledge base plan: docs/knowledge_base_plan.md
Milestone 1 report: docs/milestone1_report.md
## Reference

Pathiyan Cherumanal, S., et al. (2024). Walert: Putting Conversational Information Seeking Knowledge into Action by Building and Evaluating a Large Language Model-Powered Chatbot. Proceedings of CHIIR '24.
