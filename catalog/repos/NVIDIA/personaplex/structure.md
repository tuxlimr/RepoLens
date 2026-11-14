# Project structure: NVIDIA/personaplex

**Analysed commit:** `16419a2ef7b98611f58c9df07477d00e5ad61d5f`

**Commit reference:** [16419a2ef7b98611f58c9df07477d00e5ad61d5f](https://github.com/NVIDIA/personaplex/commit/16419a2ef7b98611f58c9df07477d00e5ad61d5f)

**Tree at this commit:** [NVIDIA/personaplex@16419a2ef7b9](https://github.com/NVIDIA/personaplex/tree/16419a2ef7b98611f58c9df07477d00e5ad61d5f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NVIDIA/personaplex |
| Description | PersonaPlex code. |
| Stars | 12130 |
| Forks | 1636 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `16419a2ef7b98611f58c9df07477d00e5ad61d5f` |
| Retrieved at | 2026-11-14T19:10:14.962299+00:00 |
| Files in this snapshot | 96 |

## Directory tree

```text
.github/  (2 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.yml
    question.yml
assets/  (1 files)
  test/  (1 files)
    prompt_service.txt
client/  (55 files)
  src/  (42 files)
    components/  (2 files)
      … 2 files under this directory
    decoder/  (1 files)
      … 1 files under this directory
    pages/  (31 files)
      … 31 files under this directory
    protocol/  (3 files)
      … 3 files under this directory
    app.tsx
    audio-processor.ts
    env.ts
    index.css
    modules.d.ts
  .eslinrc.json
  .nvmrc
  .prettierignore
  .prettierrc.json
  Dockerfile
  LICENSE
  README.md
  index.html
  package.json
  postcss.config.js
  tailwind.config.js
  tsconfig.json
  vite.config.ts
moshi/  (32 files)
  moshi/  (26 files)
    models/  (4 files)
      … 4 files under this directory
    modules/  (8 files)
      … 8 files under this directory
    quantization/  (4 files)
      … 4 files under this directory
    utils/  (6 files)
      … 6 files under this directory
    __init__.py
    client_utils.py
    offline.py
    server.py
  LICENSE.audiocraft
  LICENSE.moshi
  MANIFEST.in
  pyproject.toml
  requirements.txt
  setup.cfg
.dockerignore
.gitignore
Dockerfile
LICENSE-MIT
README.md
docker-compose.yaml
```

## Entry points

- [moshi/moshi/modules/streaming.py:628](https://github.com/NVIDIA/personaplex/blob/16419a2ef7b98611f58c9df07477d00e5ad61d5f/moshi/moshi/modules/streaming.py#L628)
- [moshi/moshi/offline.py:451](https://github.com/NVIDIA/personaplex/blob/16419a2ef7b98611f58c9df07477d00e5ad61d5f/moshi/moshi/offline.py#L451)
- [moshi/moshi/utils/sampling.py:129](https://github.com/NVIDIA/personaplex/blob/16419a2ef7b98611f58c9df07477d00e5ad61d5f/moshi/moshi/utils/sampling.py#L129)
- [client/src/app.tsx](https://github.com/NVIDIA/personaplex/blob/16419a2ef7b98611f58c9df07477d00e5ad61d5f/client/src/app.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: CompressionModel, LMGen, LMModel, LMOutput, MimiModel, ScaledEmbedding. Observed top-level functions: _… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: RawStreamingConv1d, RawStreamingConvTranspose1d, Resetable, ServerState, StreamingAdd, Str… |
| External integrations | external | Observed | Groups 40 file(s) under external integrations (observed from repository paths and static analysis). |
| moshi package | library | Observed | Groups 18 file(s) under moshi package (observed from repository paths and static analysis). Observed top-level classes: ActivationGating, BaseQuantizer, CUDAGraphed, Checkpoint, ColorizedLog, ConvDownsample1d. Observed… |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `Dockerfile` (container)
- `client/.eslinrc.json` (config)
- `client/.prettierrc.json` (config)
- `client/Dockerfile` (container)
- `client/package.json` (manifest)
- `client/tsconfig.json` (config)
- `docker-compose.yaml` (container)
- `moshi/MANIFEST.in` (manifest)
- `moshi/pyproject.toml` (manifest)
- `moshi/requirements.txt` (manifest)
- `moshi/setup.cfg` (manifest)

## Top-level layout

- `client` — 55 analysed file(s)
- `moshi` — 32 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `16419a2ef7b98611f58c9df07477d00e5ad61d5f` is the revision these paths and observations refer to.
