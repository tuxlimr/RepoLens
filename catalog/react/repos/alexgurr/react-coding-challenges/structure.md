# Project structure: alexgurr/react-coding-challenges

**Analysed commit:** `fc446a3dadc2aca69b7e55fc72ed62b413d382b4`

**Commit reference:** [fc446a3dadc2aca69b7e55fc72ed62b413d382b4](https://github.com/alexgurr/react-coding-challenges/commit/fc446a3dadc2aca69b7e55fc72ed62b413d382b4)

**Tree at this commit:** [alexgurr/react-coding-challenges@fc446a3dadc2](https://github.com/alexgurr/react-coding-challenges/tree/fc446a3dadc2aca69b7e55fc72ed62b413d382b4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alexgurr/react-coding-challenges |
| Description | A series of ReactJS coding challenges with a variety of difficulties.  |
| Stars | 3425 |
| Forks | 1108 |
| Licence | Not detected |
| Language | SCSS |
| Default branch | master |
| Analysed commit | `fc446a3dadc2aca69b7e55fc72ed62b413d382b4` |
| Retrieved at | 2026-11-14T19:15:19.340418+00:00 |
| Files in this snapshot | 100 |

## Directory tree

```text
chatter/  (37 files)
  public/  (3 files)
    index.html
    manifest.json
    robots.txt
  src/  (32 files)
    common/  (4 files)
      … 4 files under this directory
    components/  (14 files)
      … 14 files under this directory
    contexts/  (3 files)
      … 3 files under this directory
    layouts/  (6 files)
      … 6 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    App.js
    _index.scss
    config.js
    index.js
  README.md
  package.json
dark-mode/  (13 files)
  public/  (3 files)
    index.html
    manifest.json
    robots.txt
  src/  (8 files)
    common/  (1 files)
      … 1 files under this directory
    routes/  (4 files)
      … 4 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    index.js
  README.md
  package.json
rocket-ship/  (15 files)
  public/  (3 files)
    index.html
    manifest.json
    robots.txt
  src/  (10 files)
    routes/  (8 files)
      … 8 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    index.js
  README.md
  package.json
spootify/  (30 files)
  public/  (3 files)
    index.html
    manifest.json
    robots.txt
  src/  (25 files)
    assets/  (2 files)
      … 2 files under this directory
    common/  (10 files)
      … 10 files under this directory
    routes/  (9 files)
      … 9 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    config.js
    index.js
  README.md
  package.json
.gitignore
README.md
issue_template.md
new_challenge_template.md
pull_request_template.md
```

## Entry points

- [chatter/src/App.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/chatter/src/App.js)
- [chatter/src/index.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/chatter/src/index.js)
- [dark-mode/src/index.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/dark-mode/src/index.js)
- [dark-mode/src/routes/index.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/dark-mode/src/routes/index.js)
- [rocket-ship/src/index.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/rocket-ship/src/index.js)
- [rocket-ship/src/routes/index.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/rocket-ship/src/routes/index.js)
- [spootify/src/index.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/spootify/src/index.js)
- [spootify/src/routes/index.js](https://github.com/alexgurr/react-coding-challenges/blob/fc446a3dadc2aca69b7e55fc72ed62b413d382b4/spootify/src/routes/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 15 file(s) under api layer (observed from repository paths and static analysis). |
| chatter package | library | Observed | Groups 24 file(s) under chatter package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dark-mode package | library | Observed | Groups 2 file(s) under dark-mode package (observed from repository paths and static analysis). |
| rocket-ship package | library | Observed | Groups 1 file(s) under rocket-ship package (observed from repository paths and static analysis). |
| spootify package | library | Observed | Groups 9 file(s) under spootify package (observed from repository paths and static analysis). |

## Important files

- `chatter/package.json` (manifest)
- `chatter/public/manifest.json` (config)
- `dark-mode/package.json` (manifest)
- `dark-mode/public/manifest.json` (config)
- `rocket-ship/package.json` (manifest)
- `rocket-ship/public/manifest.json` (config)
- `spootify/package.json` (manifest)
- `spootify/public/manifest.json` (config)

## Top-level layout

- `chatter` — 37 analysed file(s)
- `spootify` — 30 analysed file(s)
- `rocket-ship` — 15 analysed file(s)
- `dark-mode` — 13 analysed file(s)
- `(root files)` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `fc446a3dadc2aca69b7e55fc72ed62b413d382b4` is the revision these paths and observations refer to.
