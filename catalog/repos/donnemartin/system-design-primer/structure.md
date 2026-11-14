# Project structure: donnemartin/system-design-primer

**Analysed commit:** `ae9bbd7b02d90b9866215de185217d33f39ab733`

**Commit reference:** [ae9bbd7b02d90b9866215de185217d33f39ab733](https://github.com/donnemartin/system-design-primer/commit/ae9bbd7b02d90b9866215de185217d33f39ab733)

**Tree at this commit:** [donnemartin/system-design-primer@ae9bbd7b02d9](https://github.com/donnemartin/system-design-primer/tree/ae9bbd7b02d90b9866215de185217d33f39ab733)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | donnemartin/system-design-primer |
| Description | Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards. |
| Stars | 377864 |
| Forks | 59283 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `ae9bbd7b02d90b9866215de185217d33f39ab733` |
| Retrieved at | 2026-11-14T19:05:59.634380+00:00 |
| Files in this snapshot | 60 |

## Directory tree

```text
.github/  (1 files)
  PULL_REQUEST_TEMPLATE.md
solutions/  (48 files)
  object_oriented_design/  (18 files)
    call_center/  (3 files)
      … 3 files under this directory
    deck_of_cards/  (3 files)
      … 3 files under this directory
    hash_table/  (3 files)
      … 3 files under this directory
    lru_cache/  (3 files)
      … 3 files under this directory
    online_chat/  (3 files)
      … 3 files under this directory
    parking_lot/  (3 files)
      … 3 files under this directory
  system_design/  (30 files)
    mint/  (5 files)
      … 5 files under this directory
    pastebin/  (4 files)
      … 4 files under this directory
    query_cache/  (4 files)
      … 4 files under this directory
    sales_rank/  (4 files)
      … 4 files under this directory
    scaling_aws/  (2 files)
      … 2 files under this directory
    social_graph/  (4 files)
      … 4 files under this directory
    twitter/  (2 files)
      … 2 files under this directory
    web_crawler/  (5 files)
      … 5 files under this directory
.gitattributes
.gitignore
CONTRIBUTING.md
LICENSE.txt
README-ja.md
README-zh-Hans.md
README-zh-TW.md
README.md
TRANSLATIONS.md
epub-metadata.yaml
generate-epub.sh
```

## Entry points

- [solutions/system_design/mint/mint_mapreduce.py:56](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/mint/mint_mapreduce.py#L56)
- [solutions/system_design/pastebin/pastebin.py:45](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/pastebin/pastebin.py#L45)
- [solutions/system_design/sales_rank/sales_rank_mapreduce.py:76](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/sales_rank/sales_rank_mapreduce.py#L76)
- [solutions/system_design/web_crawler/web_crawler_mapreduce.py:24](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/web_crawler/web_crawler_mapreduce.py#L24)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: HitCounts, RemoveDuplicateUrls, SalesRanker, SpendingByCategory. |
| solutions package | library | Observed | Groups 22 file(s) under solutions package (observed from repository paths and static analysis). Observed top-level classes: AddRequest, BlackJackCard, BlackJackHand, Budget, Bus, Cache. |

## Important files

- `epub-metadata.yaml` (config)

## Top-level layout

- `solutions` — 48 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ae9bbd7b02d90b9866215de185217d33f39ab733` is the revision these paths and observations refer to.
