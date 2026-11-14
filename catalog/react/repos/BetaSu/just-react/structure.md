# Project structure: BetaSu/just-react

**Analysed commit:** `45a85e238fa07050d5c6fb672d60aeced7f6b77f`

**Commit reference:** [45a85e238fa07050d5c6fb672d60aeced7f6b77f](https://github.com/BetaSu/just-react/commit/45a85e238fa07050d5c6fb672d60aeced7f6b77f)

**Tree at this commit:** [BetaSu/just-react@45a85e238fa0](https://github.com/BetaSu/just-react/tree/45a85e238fa07050d5c6fb672d60aeced7f6b77f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BetaSu/just-react |
| Description | 「React技术揭秘」  一本自顶向下的React源码分析书 |
| Stars | 6380 |
| Forks | 552 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `45a85e238fa07050d5c6fb672d60aeced7f6b77f` |
| Retrieved at | 2026-11-14T19:14:06.896598+00:00 |
| Files in this snapshot | 52 |

## Directory tree

```text
.bin/  (1 files)
  create_tongji.js
docs/  (44 files)
  .vuepress/  (4 files)
    styles/  (1 files)
      … 1 files under this directory
    theme/  (2 files)
      … 2 files under this directory
    config.js
  concurrent/  (4 files)
    disrupt.md
    lane.md
    prepare.md
    scheduler.md
  diff/  (3 files)
    multi.md
    one.md
    prepare.md
  hooks/  (7 files)
    create.md
    prepare.md
    structure.md
    useeffect.md
    usememo.md
    useref.md
    usestate.md
  preparation/  (7 files)
    file.md
    idea.md
    jsx.md
    newConstructure.md
    oldConstructure.md
    source.md
    summary.md
  process/  (6 files)
    beginWork.md
    completeWork.md
    doubleBuffer.md
    fiber-mental.md
    fiber.md
    reconciler.md
  renderer/  (4 files)
    beforeMutation.md
    layout.md
    mutation.md
    prepare.md
  state/  (6 files)
    mental.md
    prepare.md
    priority.md
    reactdom.md
    setstate.md
    update.md
  course.md
  index.md
  me.md
.drone.yml
.gitignore
LICENSE
README.md
deploy.sh
dockerfile
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.drone.yml` (config)
- `dockerfile` (container)
- `package.json` (manifest)

## Top-level layout

- `docs` — 44 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `45a85e238fa07050d5c6fb672d60aeced7f6b77f` is the revision these paths and observations refer to.
