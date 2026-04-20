# DataFabric Python Engineer — Technical Interview

Welcome. This session is about 75 minutes across three exercises. No need to prepare anything in advance — we'll work through each part together.

## Setup

Start the mock server before we begin:

```bash
cd mock_server
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The server exposes a small pipeline API at `http://localhost:8000`. You can browse the auto-generated docs at `http://localhost:8000/docs`.

## Structure

```
python-interview/
├── mock_server/          # FastAPI mock server
├── candidate_snippets/   # One file per exercise
│   ├── part_a_review.py
│   ├── part_b_design.py
│   └── part_c_debug.py
└── README.md
```

## Exercises

| Part | Duration | File |
|------|----------|------|
| A — Code Review | 20 min | `candidate_snippets/part_a_review.py` |
| B — System Design | 20 min | `candidate_snippets/part_b_design.py` |
| C — Debugging | 20 min | `candidate_snippets/part_c_debug.py` |
| Wrap-up / Q&A | 10–15 min | — |

We'll go through each file together. Think out loud as much as you can — reasoning matters more than arriving at the answer immediately.
