# RepoLens — GitHub Architecture Explorer

Paste a public GitHub repository URL → get a high-level **Mermaid block diagram** and a
readable, evidence-backed **Markdown architecture report**. Python repositories first
(spec: `Project_updated.md`); JavaScript/React is a later phase.

Existing reports are served free from cache; a **Fresh analysis** (paid action, mock
checkout in this MVP) re-analyses the current commit and stores a new report version.

## Architecture

```
User → Next.js frontend → FastAPI API → report cache (SQLite/Postgres)
                              └─(miss / paid fresh)→ analysis job
                                   ├─ GitHub: metadata API + one codeload tarball download
                                   ├─ Static analysis: inventory → Python AST → framework detection
                                   ├─ Structured architecture model (components, relationships, evidence)
                                   ├─ Optional OpenRouter summary polish (off unless key set)
                                   └─ Mermaid diagram + 12-section Markdown report → stored, versioned
```

Repository code is **never executed, installed, or imported**. Repo text is treated as
untrusted input; likely secrets are redacted and excluded from reports/prompts.

## Run locally

Backend (Python 3.11+):

```powershell
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --port 8000   # http://localhost:8000/docs
```

Frontend (Node 20+):

```powershell
cd frontend
npm install
npm run dev                                   # http://localhost:3000
```

Then paste e.g. `https://github.com/pallets/click` on the landing page, or open
`/sample` for a built-in example report that needs no backend.

## Configuration (all optional)

| Variable | Default | Purpose |
|---|---|---|
| `GITHUB_TOKEN` | — | Raises GitHub API limits. Without it, metadata may fall back to minimal data (analysis still runs via the archive download) and the report says so. |
| `OPENROUTER_API_KEY` / `OPENROUTER_MODEL` | — / `openrouter/free` | Polish the one-paragraph summary only; evidence model stays deterministic. |
| `DATABASE_URL` | `sqlite:///./repolens.db` | Use PostgreSQL in production, e.g. `postgresql+psycopg://…` (add a driver). |
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | Frontend → backend base URL. |
| `MAX_FILES` / `MAX_FILE_BYTES` / `MAX_TOTAL_BYTES` | 800 / 200000 / 8000000 | Repository size limits (§12). |

See `.env.example`.

## API summary

- `POST /api/analyze {url, fresh}` — cached report if present, else queues analysis
- `GET /api/analyses/{id}` — job status
- `GET /api/reports/{owner}/{repo}` — latest report (model + Mermaid + Markdown)
- `GET /api/reports/{owner}/{repo}/versions`, `GET …/markdown` — versions / download
- `GET /api/reports`, `GET /api/examples`, `GET /api/repositories/{owner}/{repo}`
- `POST /api/payments/fresh {url}` — **mock** payment (no provider integrated yet); authorises and queues a fresh analysis

## Tests

```powershell
python -m pytest backend/tests -q   # 15 tests: analyzer (synthetic repo, secret-redaction) + API (offline, fake GitHub)
cd frontend; npm run build
```

## MVP status vs spec milestones

- ✅ M2 Working analysis engine (URL → metadata/inventory → AST → model → Mermaid + Markdown → stored)
- ✅ M3 Public web experience (landing, examples, sample report, report viewer, copy/download, responsive)
- 🟡 M4 Cache + payments: cache/versioning done; payment is a clearly-labelled mock — integrate a real provider (e.g. Stripe/Paystack) and set pricing before charging anyone
- ⬜ M1/M5: curate the 10–20 repo evaluation set and run a private beta; JS/React (M6) not started
