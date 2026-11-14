# Project structure: bailicangdu/node-elm

**Analysed commit:** `32ea999c63f59db4f6fb05e3227bc305663782f0`

**Commit reference:** [32ea999c63f59db4f6fb05e3227bc305663782f0](https://github.com/bailicangdu/node-elm/commit/32ea999c63f59db4f6fb05e3227bc305663782f0)

**Tree at this commit:** [bailicangdu/node-elm@32ea999c63f5](https://github.com/bailicangdu/node-elm/tree/32ea999c63f59db4f6fb05e3227bc305663782f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bailicangdu/node-elm |
| Description | Backend system based on node.js + Mongodb.  基于 node.js + Mongodb 构建的后台系统 |
| Stars | 12318 |
| Forks | 3659 |
| Licence | GPL-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `32ea999c63f59db4f6fb05e3227bc305663782f0` |
| Retrieved at | 2026-11-14T19:12:06.267468+00:00 |
| Files in this snapshot | 90 |

## Directory tree

```text
InitData/  (9 files)
  activity.js
  category.js
  delivery.js
  entry.js
  explain.js
  hongbao.js
  payments.js
  rate.js
  remark.js
config/  (3 files)
  .gitignore
  default.js
  development.js
controller/  (18 files)
  admin/  (1 files)
    admin.js
  member/  (1 files)
    vipcart.js
  promotion/  (1 files)
    hongbao.js
  shopping/  (3 files)
    category.js
    food.js
    shop.js
  statis/  (1 files)
    statis.js
  ugc/  (1 files)
    rating.js
  v1/  (7 files)
    address.js
    captchas.js
    carts.js
    cities.js
    order.js
    remark.js
    search.js
  v2/  (2 files)
    entry.js
    user.js
  v3/  (1 files)
    explain.js
logs/  (1 files)
  .gitignore
middlewares/  (4 files)
  check.js
  history.js
  statistic.js
  w2-proxy
models/  (20 files)
  admin/  (1 files)
    admin.js
  bos/  (1 files)
    order.js
  promotion/  (1 files)
    hongbao.js
  shopping/  (5 files)
    activity.js
    category.js
    delivery.js
    food.js
    shop.js
  statis/  (1 files)
    statis.js
  ugc/  (1 files)
    rating.js
  v1/  (5 files)
    address.js
    cart.js
    cities.js
    payments.js
    remark.js
  v2/  (3 files)
    entry.js
    user.js
    userInfo.js
  v3/  (1 files)
    explain.js
  ids.js
mongodb/  (1 files)
  db.js
prototype/  (2 files)
  addressComponent.js
  baseComponent.js
public/  (6 files)
  elm/  (4 files)
    static/  (4 files)
      … 4 files under this directory
  img/  (1 files)
    .gitignore
  index.html
routes/  (14 files)
  admin.js
  bos.js
  eus.js
  index.js
  member.js
  payapi.js
  promotion.js
  shopping.js
  statis.js
  ugc.js
  v1.js
  v2.js
  v3.js
  v4.js
views/  (2 files)
  home.ejs
  index.html
.babelrc
.gitignore
API.md
COPYING
README.md
app.js
ecosystem.config.js
index.js
package.json
todo.txt
```

## Entry points

- [index.js](https://github.com/bailicangdu/node-elm/blob/32ea999c63f59db4f6fb05e3227bc305663782f0/index.js)
- [app.js](https://github.com/bailicangdu/node-elm/blob/32ea999c63f59db4f6fb05e3227bc305663782f0/app.js)
- [routes/index.js](https://github.com/bailicangdu/node-elm/blob/32ea999c63f59db4f6fb05e3227bc305663782f0/routes/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 14 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| controller package | library | Observed | Groups 18 file(s) under controller package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 20 file(s) under data layer (observed from repository paths and static analysis). |
| InitData package | library | Observed | Groups 9 file(s) under initdata package (observed from repository paths and static analysis). |
| middlewares package | library | Observed | Groups 3 file(s) under middlewares package (observed from repository paths and static analysis). |
| mongodb package | library | Observed | Groups 1 file(s) under mongodb package (observed from repository paths and static analysis). |
| prototype package | library | Observed | Groups 2 file(s) under prototype package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 3 file(s) under public package (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)

## Top-level layout

- `models` — 20 analysed file(s)
- `controller` — 18 analysed file(s)
- `routes` — 14 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `InitData` — 9 analysed file(s)
- `public` — 6 analysed file(s)
- `middlewares` — 4 analysed file(s)
- `config` — 3 analysed file(s)
- `prototype` — 2 analysed file(s)
- `views` — 2 analysed file(s)
- `logs` — 1 analysed file(s)
- `mongodb` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `32ea999c63f59db4f6fb05e3227bc305663782f0` is the revision these paths and observations refer to.
