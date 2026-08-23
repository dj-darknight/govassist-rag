# Retrenched Tech Worker Assistant — WIL Project
**Group ID:** <49>

## Aim
A retrieval-augmented assistant that helps recently retrenched Australian tech
workers find accurate, source-grounded information on redundancy entitlements,
JobSeeker eligibility, visa implications, and reskilling pathways — extending
the Walert (Pathiyan Cherumanal et al., 2024) approach with a larger, higher-stakes
domain and explicit hallucination-aware abstention.

## Repository structure
- `data/walert_baseline/`   reproduction dataset for baselining our pipeline
- `data/knowledge_base/`    our own ~150-200 passage corpus (15 subtopics)
- `src/`                    retrieval, generation, evaluation pipeline
- `experiments/`            run scripts and configs
- `results/`                metric outputs
- `docs/`                   milestone reports and the knowledge base plan

## Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash experiments/run_all.sh
