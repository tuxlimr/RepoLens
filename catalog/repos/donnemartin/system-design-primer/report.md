# Architecture report: donnemartin/system-design-primer

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | donnemartin/system-design-primer |
| Description | Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards. |
| Language | Python |
| Stars | 377864 |
| Licence | Other |
| Analysed commit / branch | ae9bbd7b02d90b9866215de185217d33f39ab733 / master |
| Framework(s) | None detected |
| Files analysed | 60 |
| Components | 4 |

## 2. Architecture in one minute

donnemartin/system-design-primer - Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.. This repository was analysed statically from 60 file(s) (26 Python). Detected technologies (observed from imports/manifests): no known frameworks/libraries. Files are grouped into 4 component(s): Configuration and deployment, Core modules, Application entry point, solutions package. Observed entry point(s): solutions/system_design/mint/mint_mapreduce.py, solutions/system_design/pastebin/pastebin.py, solutions/system_design/sales_rank/sales_rank_mapreduce.py. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph config_group
        config["Configuration and deployment"]
    end
    subgraph core_group
        core["Core modules"]
    end
    subgraph entrypoint_group
        entrypoint["Application entry point"]
    end
    subgraph library_group
        solutions["solutions package"]
    end
```

## 4. Main components

### Configuration and deployment (`config`)

- **Kind:** config
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `epub-metadata.yaml`
- **Evidence:** [epub-metadata.yaml](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/epub-metadata.yaml)

### Core modules (`core`)

- **Kind:** core
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under core modules (observed from repository paths and static analysis).
- **Paths:** `generate-epub.sh`
- **Evidence:** [generate-epub.sh](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/generate-epub.sh)

### Application entry point (`entrypoint`)

- **Kind:** entrypoint
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: HitCounts, RemoveDuplicateUrls, SalesRanker, SpendingByCategory.
- **Paths:** `solutions/system_design/mint/mint_mapreduce.py`, `solutions/system_design/pastebin/pastebin.py`, `solutions/system_design/sales_rank/sales_rank_mapreduce.py`, `solutions/system_design/web_crawler/web_crawler_mapreduce.py`
- **Evidence:** [solutions/system_design/mint/mint_mapreduce.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/mint/mint_mapreduce.py#L6); [solutions/system_design/pastebin/pastebin.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/pastebin/pastebin.py#L6); [solutions/system_design/sales_rank/sales_rank_mapreduce.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/sales_rank/sales_rank_mapreduce.py#L6); [solutions/system_design/web_crawler/web_crawler_mapreduce.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/web_crawler/web_crawler_mapreduce.py#L6)

### solutions package (`solutions`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 22 file(s) under solutions package (observed from repository paths and static analysis). Observed top-level classes: AddRequest, BlackJackCard, BlackJackHand, Budget, Bus, Cache.
- **Paths:** `solutions/object_oriented_design/call_center/__init__.py`, `solutions/object_oriented_design/call_center/call_center.py`, `solutions/object_oriented_design/deck_of_cards/__init__.py`, `solutions/object_oriented_design/deck_of_cards/deck_of_cards.py`, `solutions/object_oriented_design/hash_table/__init__.py`, `solutions/object_oriented_design/hash_table/hash_map.py`, `solutions/object_oriented_design/lru_cache/__init__.py`, `solutions/object_oriented_design/lru_cache/lru_cache.py`, `solutions/object_oriented_design/online_chat/__init__.py`, `solutions/object_oriented_design/online_chat/online_chat.py`, `solutions/object_oriented_design/parking_lot/__init__.py`, `solutions/object_oriented_design/parking_lot/parking_lot.py`, `solutions/system_design/mint/__init__.py`, `solutions/system_design/mint/mint_snippets.py`, `solutions/system_design/pastebin/__init__.py`, `solutions/system_design/query_cache/__init__.py`, `solutions/system_design/query_cache/query_cache_snippets.py`, `solutions/system_design/sales_rank/__init__.py`, `solutions/system_design/social_graph/__init__.py`, `solutions/system_design/social_graph/social_graph_snippets.py`, `solutions/system_design/web_crawler/__init__.py`, `solutions/system_design/web_crawler/web_crawler_snippets.py`
- **Evidence:** [solutions/object_oriented_design/call_center/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/call_center/__init__.py); [solutions/object_oriented_design/call_center/call_center.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/call_center/call_center.py#L6); [solutions/object_oriented_design/deck_of_cards/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/deck_of_cards/__init__.py); [solutions/object_oriented_design/deck_of_cards/deck_of_cards.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/deck_of_cards/deck_of_cards.py#L6); [solutions/object_oriented_design/hash_table/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/hash_table/__init__.py); [solutions/object_oriented_design/hash_table/hash_map.py:1](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/hash_table/hash_map.py#L1); [solutions/object_oriented_design/lru_cache/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/lru_cache/__init__.py); [solutions/object_oriented_design/lru_cache/lru_cache.py:1](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/lru_cache/lru_cache.py#L1)

## 5. Execution flow

**Observed** entry point(s):

- [solutions/system_design/mint/mint_mapreduce.py:56](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/mint/mint_mapreduce.py#L56)
- [solutions/system_design/pastebin/pastebin.py:45](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/pastebin/pastebin.py#L45)
- [solutions/system_design/sales_rank/sales_rank_mapreduce.py:76](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/sales_rank/sales_rank_mapreduce.py#L76)
- [solutions/system_design/web_crawler/web_crawler_mapreduce.py:24](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/web_crawler/web_crawler_mapreduce.py#L24)

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `.gitattributes` - other (33 bytes)
- `.gitignore` - other (800 bytes)
- `CONTRIBUTING.md` - docs (5377 bytes)
- `LICENSE.txt` - docs (365 bytes)
- `README-ja.md` - docs (137561 bytes)
- `README-zh-Hans.md` - docs (101490 bytes)
- `README-zh-TW.md` - docs (126363 bytes)
- `README.md` - docs (109830 bytes)
- `TRANSLATIONS.md` - docs (6700 bytes)
- `epub-metadata.yaml` - config (60 bytes)
- `generate-epub.sh` - source, Shell (1192 bytes)

### `.github`

- `.github/PULL_REQUEST_TEMPLATE.md` - docs (560 bytes)

### `solutions`

- `solutions/object_oriented_design/call_center/__init__.py` - source, Python (0 bytes)
- `solutions/object_oriented_design/call_center/call_center.ipynb` - other (6474 bytes)
- `solutions/object_oriented_design/call_center/call_center.py` - source, Python (3263 bytes)
- `solutions/object_oriented_design/deck_of_cards/__init__.py` - source, Python (0 bytes)
- `solutions/object_oriented_design/deck_of_cards/deck_of_cards.ipynb` - other (5247 bytes)
- `solutions/object_oriented_design/deck_of_cards/deck_of_cards.py` - source, Python (2547 bytes)
- `solutions/object_oriented_design/hash_table/__init__.py` - source, Python (0 bytes)
- `solutions/object_oriented_design/hash_table/hash_map.ipynb` - other (3123 bytes)
- `solutions/object_oriented_design/hash_table/hash_map.py` - source, Python (1079 bytes)
- `solutions/object_oriented_design/lru_cache/__init__.py` - source, Python (0 bytes)
- `solutions/object_oriented_design/lru_cache/lru_cache.ipynb` - other (4096 bytes)
- `solutions/object_oriented_design/lru_cache/lru_cache.py` - source, Python (1931 bytes)
- `solutions/object_oriented_design/online_chat/__init__.py` - source, Python (0 bytes)
- `solutions/object_oriented_design/online_chat/online_chat.ipynb` - other (5154 bytes)
- `solutions/object_oriented_design/online_chat/online_chat.py` - source, Python (2443 bytes)
- `solutions/object_oriented_design/parking_lot/__init__.py` - source, Python (0 bytes)
- `solutions/object_oriented_design/parking_lot/parking_lot.ipynb` - other (5913 bytes)
- `solutions/object_oriented_design/parking_lot/parking_lot.py` - source, Python (3070 bytes)
- `solutions/system_design/mint/README-zh-Hans.md` - docs (20225 bytes)
- `solutions/system_design/mint/README.md` - docs (20615 bytes)
- `solutions/system_design/mint/__init__.py` - source, Python (0 bytes)
- `solutions/system_design/mint/mint_mapreduce.py` - source, Python (1475 bytes)
- `solutions/system_design/mint/mint_snippets.py` - source, Python (1413 bytes)
- `solutions/system_design/pastebin/README-zh-Hans.md` - docs (16490 bytes)
- `solutions/system_design/pastebin/README.md` - docs (15782 bytes)
- `solutions/system_design/pastebin/__init__.py` - source, Python (0 bytes)
- `solutions/system_design/pastebin/pastebin.py` - source, Python (1055 bytes)
- `solutions/system_design/query_cache/README-zh-Hans.md` - docs (15060 bytes)
- `solutions/system_design/query_cache/README.md` - docs (14053 bytes)
- `solutions/system_design/query_cache/__init__.py` - source, Python (0 bytes)
- `solutions/system_design/query_cache/query_cache_snippets.py` - source, Python (2610 bytes)
- `solutions/system_design/sales_rank/README-zh-Hans.md` - docs (15832 bytes)
- `solutions/system_design/sales_rank/README.md` - docs (14885 bytes)
- `solutions/system_design/sales_rank/__init__.py` - source, Python (0 bytes)
- `solutions/system_design/sales_rank/sales_rank_mapreduce.py` - source, Python (1921 bytes)
- `solutions/system_design/scaling_aws/README-zh-Hans.md` - docs (18248 bytes)
- `solutions/system_design/scaling_aws/README.md` - docs (19841 bytes)
- `solutions/system_design/social_graph/README-zh-Hans.md` - docs (14639 bytes)
- `solutions/system_design/social_graph/README.md` - docs (15894 bytes)
- `solutions/system_design/social_graph/__init__.py` - source, Python (0 bytes)
- `solutions/system_design/social_graph/social_graph_snippets.py` - source, Python (1750 bytes)
- `solutions/system_design/twitter/README-zh-Hans.md` - docs (17135 bytes)
- `solutions/system_design/twitter/README.md` - docs (16643 bytes)
- `solutions/system_design/web_crawler/README-zh-Hans.md` - docs (18077 bytes)
- `solutions/system_design/web_crawler/README.md` - docs (17048 bytes)
- `solutions/system_design/web_crawler/__init__.py` - source, Python (0 bytes)
- `solutions/system_design/web_crawler/web_crawler_mapreduce.py` - source, Python (494 bytes)
- `solutions/system_design/web_crawler/web_crawler_snippets.py` - source, Python (2202 bytes)

## 7. Key dependencies and integrations

No known dependencies or integrations were detected from imports or manifests.

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `epub-metadata.yaml` (config)

## 10. Design observations

- An entry/API layer is separated from other code (Inferred from paths and decorators).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

## 12. Source references

- [epub-metadata.yaml](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/epub-metadata.yaml)
- [generate-epub.sh](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/generate-epub.sh)
- [solutions/object_oriented_design/call_center/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/call_center/__init__.py)
- [solutions/object_oriented_design/call_center/call_center.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/call_center/call_center.py#L6)
- [solutions/object_oriented_design/deck_of_cards/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/deck_of_cards/__init__.py)
- [solutions/object_oriented_design/deck_of_cards/deck_of_cards.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/deck_of_cards/deck_of_cards.py#L6)
- [solutions/object_oriented_design/hash_table/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/hash_table/__init__.py)
- [solutions/object_oriented_design/hash_table/hash_map.py:1](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/hash_table/hash_map.py#L1)
- [solutions/object_oriented_design/lru_cache/__init__.py](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/lru_cache/__init__.py)
- [solutions/object_oriented_design/lru_cache/lru_cache.py:1](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/object_oriented_design/lru_cache/lru_cache.py#L1)
- [solutions/system_design/mint/mint_mapreduce.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/mint/mint_mapreduce.py#L6)
- [solutions/system_design/mint/mint_mapreduce.py:56](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/mint/mint_mapreduce.py#L56)
- [solutions/system_design/pastebin/pastebin.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/pastebin/pastebin.py#L6)
- [solutions/system_design/pastebin/pastebin.py:45](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/pastebin/pastebin.py#L45)
- [solutions/system_design/sales_rank/sales_rank_mapreduce.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/sales_rank/sales_rank_mapreduce.py#L6)
- [solutions/system_design/sales_rank/sales_rank_mapreduce.py:76](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/sales_rank/sales_rank_mapreduce.py#L76)
- [solutions/system_design/web_crawler/web_crawler_mapreduce.py:6](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/web_crawler/web_crawler_mapreduce.py#L6)
- [solutions/system_design/web_crawler/web_crawler_mapreduce.py:24](https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/solutions/system_design/web_crawler/web_crawler_mapreduce.py#L24)
