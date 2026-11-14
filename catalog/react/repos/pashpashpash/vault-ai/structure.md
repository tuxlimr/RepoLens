# Project structure: pashpashpash/vault-ai

**Analysed commit:** `60ec5f21f8222e942f266971b630b9f0f4575693`

**Commit reference:** [60ec5f21f8222e942f266971b630b9f0f4575693](https://github.com/pashpashpash/vault-ai/commit/60ec5f21f8222e942f266971b630b9f0f4575693)

**Tree at this commit:** [pashpashpash/vault-ai@60ec5f21f822](https://github.com/pashpashpash/vault-ai/tree/60ec5f21f8222e942f266971b630b9f0f4575693)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pashpashpash/vault-ai |
| Description | OP Vault ChatGPT: Give ChatGPT long-term memory using the OP Stack (OpenAI + Pinecone Vector Database). Upload your own custom knowledge base files (PDF, txt, epub, etc) using a simple React frontend. |
| Stars | 3385 |
| Forks | 291 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `60ec5f21f8222e942f266971b630b9f0f4575693` |
| Retrieved at | 2026-11-14T19:15:21.412377+00:00 |
| Files in this snapshot | 54 |

## Directory tree

```text
chunk/  (1 files)
  fileprocessing.go
components/  (22 files)
  Footer/  (2 files)
    index.jsx
    index.less
  Go/  (1 files)
    index.jsx
  Header/  (3 files)
    beta.jsx
    index.jsx
    index.less
  Page/  (2 files)
    index.jsx
    index.less
  Pages/  (2 files)
    LandingPage/  (2 files)
      … 2 files under this directory
  Util/  (6 files)
    Cookies.jsx
    PostAPI.jsx
    Promises.jsx
    Text.jsx
    TimedLocalStorage.jsx
    index.jsx
  common.less
  defaults.less
  fonts.less
  index.jsx
  routes.jsx
  routes.less
config/  (1 files)
  websites.json
errorlist/  (1 files)
  errorlist.go
form/  (2 files)
  callquestions.go
  form.go
scripts/  (2 files)
  go-compile.sh
  source-me.sh
secret/  (1 files)
  .gitignore
serverutil/  (2 files)
  config.go
  util.go
static/  (1 files)
  index.html
validator/  (2 files)
  email.go
  validator.go
vault-web-server/  (7 files)
  getapi/  (1 files)
    getapi.go
  postapi/  (5 files)
    fileupload.go
    formparseverify.go
    handlercontext.go
    openai.go
    questions.go
  main.go
vectordb/  (3 files)
  pinecone/  (1 files)
    pinecone.go
  qdrant/  (1 files)
    qdrant.go
  vectordb.go
.eslintrc.js
.gitignore
.prettierrc
LICENSE
README.md
go.mod
go.sum
package.json
webpack.config.js
```

## Entry points

- [components/Footer/index.jsx](https://github.com/pashpashpash/vault-ai/blob/60ec5f21f8222e942f266971b630b9f0f4575693/components/Footer/index.jsx)
- [components/Go/index.jsx](https://github.com/pashpashpash/vault-ai/blob/60ec5f21f8222e942f266971b630b9f0f4575693/components/Go/index.jsx)
- [components/Header/index.jsx](https://github.com/pashpashpash/vault-ai/blob/60ec5f21f8222e942f266971b630b9f0f4575693/components/Header/index.jsx)
- [components/Page/index.jsx](https://github.com/pashpashpash/vault-ai/blob/60ec5f21f8222e942f266971b630b9f0f4575693/components/Page/index.jsx)
- [components/Pages/LandingPage/index.jsx](https://github.com/pashpashpash/vault-ai/blob/60ec5f21f8222e942f266971b630b9f0f4575693/components/Pages/LandingPage/index.jsx)
- [components/Util/index.jsx](https://github.com/pashpashpash/vault-ai/blob/60ec5f21f8222e942f266971b630b9f0f4575693/components/Util/index.jsx)
- [components/index.jsx](https://github.com/pashpashpash/vault-ai/blob/60ec5f21f8222e942f266971b630b9f0f4575693/components/index.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chunk package | library | Observed | Groups 1 file(s) under chunk package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 14 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| errorlist package | library | Observed | Groups 1 file(s) under errorlist package (observed from repository paths and static analysis). |
| form package | library | Observed | Groups 2 file(s) under form package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| serverutil package | library | Observed | Groups 2 file(s) under serverutil package (observed from repository paths and static analysis). |
| validator package | library | Observed | Groups 2 file(s) under validator package (observed from repository paths and static analysis). |
| vault-web-server package | library | Observed | Groups 7 file(s) under vault-web-server package (observed from repository paths and static analysis). |
| vectordb package | library | Observed | Groups 3 file(s) under vectordb package (observed from repository paths and static analysis). |

## Important files

- `config/websites.json` (config)
- `go.mod` (manifest)
- `package.json` (manifest)

## Top-level layout

- `components` — 22 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `vault-web-server` — 7 analysed file(s)
- `vectordb` — 3 analysed file(s)
- `form` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `serverutil` — 2 analysed file(s)
- `validator` — 2 analysed file(s)
- `chunk` — 1 analysed file(s)
- `config` — 1 analysed file(s)
- `errorlist` — 1 analysed file(s)
- `secret` — 1 analysed file(s)
- `static` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `60ec5f21f8222e942f266971b630b9f0f4575693` is the revision these paths and observations refer to.
