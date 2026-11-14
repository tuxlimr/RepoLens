# Project structure: timqian/chinese-independent-blogs

**Analysed commit:** `6efc52fec8a2dc34650ba126ecd7b366d9ec109b`

**Commit reference:** [6efc52fec8a2dc34650ba126ecd7b366d9ec109b](https://github.com/timqian/chinese-independent-blogs/commit/6efc52fec8a2dc34650ba126ecd7b366d9ec109b)

**Tree at this commit:** [timqian/chinese-independent-blogs@6efc52fec8a2](https://github.com/timqian/chinese-independent-blogs/tree/6efc52fec8a2dc34650ba126ecd7b366d9ec109b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | timqian/chinese-independent-blogs |
| Description | 中文独立博客列表 |
| Stars | 24470 |
| Forks | 2777 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6efc52fec8a2dc34650ba126ecd7b366d9ec109b` |
| Retrieved at | 2026-11-14T19:11:02.356552+00:00 |
| Files in this snapshot | 37 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    pr_lint.yml
    updateInfo.yml
  FUNDING.yml
frontend/  (25 files)
  migrations/  (10 files)
    0001_init.sql
    0002_blog_num.sql
    0003_users.sql
    0004_notifications.sql
    0005_follows.sql
    0006_avatars.sql
    0007_next_check.sql
    0008_conditional_get.sql
    0009_dead_since.sql
    0010_blocked_blogs.sql
  public/  (3 files)
    app.js
    favicon.svg
    style.css
  scripts/  (1 files)
    seed-dev.sql
  worker/  (8 files)
    auth.js
    categories.js
    crawl.js
    discuss.js
    favicon.js
    index.js
    telegram.js
    views.js
  README.md
  package.json
  wrangler.jsonc
scripts/  (4 files)
  lib/  (1 files)
    feed.mjs
  generate-opml.mjs
  lint.mjs
  render-readme.mjs
.gitignore
LICENSE
README.md
blogs-original.csv
package.json
```

## Entry points

- [frontend/public/app.js](https://github.com/timqian/chinese-independent-blogs/blob/6efc52fec8a2dc34650ba126ecd7b366d9ec109b/frontend/public/app.js)
- [frontend/worker/index.js](https://github.com/timqian/chinese-independent-blogs/blob/6efc52fec8a2dc34650ba126ecd7b366d9ec109b/frontend/worker/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 9 file(s) under frontend package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/pr_lint.yml` (ci)
- `.github/workflows/updateInfo.yml` (ci)
- `frontend/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `frontend` — 25 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6efc52fec8a2dc34650ba126ecd7b366d9ec109b` is the revision these paths and observations refer to.
