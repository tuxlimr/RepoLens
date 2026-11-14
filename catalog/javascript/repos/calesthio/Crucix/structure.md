# Project structure: calesthio/Crucix

**Analysed commit:** `3db7068817e0c815df353fa0f19657c85142789d`

**Commit reference:** [3db7068817e0c815df353fa0f19657c85142789d](https://github.com/calesthio/Crucix/commit/3db7068817e0c815df353fa0f19657c85142789d)

**Tree at this commit:** [calesthio/Crucix@3db7068817e0](https://github.com/calesthio/Crucix/tree/3db7068817e0c815df353fa0f19657c85142789d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | calesthio/Crucix |
| Description | Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes. |
| Stars | 12224 |
| Forks | 1861 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `3db7068817e0c815df353fa0f19657c85142789d` |
| Retrieved at | 2026-11-14T19:12:07.798059+00:00 |
| Files in this snapshot | 88 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (1 files)
    docker-publish.yml
  CODEOWNERS
  pull_request_template.md
apis/  (35 files)
  sources/  (29 files)
    acled.mjs
    adsb.mjs
    bls.mjs
    bluesky.mjs
    cisa-kev.mjs
    cloudflare-radar.mjs
    comtrade.mjs
    eia.mjs
    epa.mjs
    firms.mjs
    fred.mjs
    gdelt.mjs
    gscpi.mjs
    kiwisdr.mjs
    noaa.mjs
    ofac.mjs
    opensanctions.mjs
    opensky.mjs
    patents.mjs
    reddit.mjs
    reliefweb.mjs
    safecast.mjs
    ships.mjs
    space.mjs
    … 5 more files
  utils/  (2 files)
    env.mjs
    fetch.mjs
  BRIEFING_PROMPT.md
  BRIEFING_TEMPLATE.md
  briefing.mjs
  save-briefing.mjs
dashboard/  (3 files)
  public/  (2 files)
    jarvis.html
    loading.html
  inject.mjs
lib/  (18 files)
  alerts/  (2 files)
    discord.mjs
    telegram.mjs
  delta/  (3 files)
    engine.mjs
    index.mjs
    memory.mjs
  llm/  (12 files)
    anthropic.mjs
    codex.mjs
    gemini.mjs
    grok.mjs
    ideas.mjs
    index.mjs
    minimax.mjs
    mistral.mjs
    ollama.mjs
    openai.mjs
    openrouter.mjs
    provider.mjs
  i18n.mjs
locales/  (2 files)
  en.json
  fr.json
scripts/  (1 files)
  clean.mjs
test/  (9 files)
  llm-grok.test.mjs
  llm-minimax-integration.test.mjs
  llm-minimax.test.mjs
  llm-mistral-integration.test.mjs
  llm-mistral.test.mjs
  llm-ollama-integration.test.mjs
  llm-ollama.test.mjs
  llm-openrouter-integration.test.mjs
  llm-openrouter.test.mjs
.dockerignore
.env.example
.gitignore
.nvmrc
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
SECURITY.md
crucix.config.mjs
diag.mjs
docker-compose.yml
package.json
server.mjs
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apis package | library | Observed | Groups 33 file(s) under apis package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| dashboard package | library | Observed | Groups 1 file(s) under dashboard package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 18 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/docker-publish.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `locales/en.json` (config)
- `locales/fr.json` (config)
- `package.json` (manifest)

## Top-level layout

- `apis` — 35 analysed file(s)
- `lib` — 18 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `test` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `dashboard` — 3 analysed file(s)
- `locales` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3db7068817e0c815df353fa0f19657c85142789d` is the revision these paths and observations refer to.
