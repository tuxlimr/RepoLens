# Project structure: emmabostian/developer-portfolios

**Analysed commit:** `cecf27d06a4cdb391ad4a031afc0d510ef71a0a2`

**Commit reference:** [cecf27d06a4cdb391ad4a031afc0d510ef71a0a2](https://github.com/emmabostian/developer-portfolios/commit/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2)

**Tree at this commit:** [emmabostian/developer-portfolios@cecf27d06a4c](https://github.com/emmabostian/developer-portfolios/tree/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | emmabostian/developer-portfolios |
| Description | A list of developer portfolios for your inspiration |
| Stars | 27698 |
| Forks | 5431 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `cecf27d06a4cdb391ad4a031afc0d510ef71a0a2` |
| Retrieved at | 2026-11-14T19:07:18.867453+00:00 |
| Files in this snapshot | 23 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    link-checker.yml
    parking-redirect-checker.yml
  pull_request_template.md
src/  (6 files)
  alphabetical.py
  check_parking_redirects.py
  generate_feed.py
  remove_emoji_in_readme.py
  run_dup_report.py
  run_tests.py
tests/  (7 files)
  test_alphabetical.py
  test_emoji_detection.py
  test_feed_json.py
  test_fullstack_variants.py
  test_main_e2e.py
  test_remove_emoji.py
  test_url_format.py
.gitignore
.lycheeignore
.lycherc.toml
CONTRIBUTING.md
FEED_JSON.md
README.md
run_tests.py
```

## Entry points

- [src/alphabetical.py:802](https://github.com/emmabostian/developer-portfolios/blob/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2/src/alphabetical.py#L802)
- [src/check_parking_redirects.py:354](https://github.com/emmabostian/developer-portfolios/blob/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2/src/check_parking_redirects.py#L354)
- [src/generate_feed.py:85](https://github.com/emmabostian/developer-portfolios/blob/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2/src/generate_feed.py#L85)
- [src/remove_emoji_in_readme.py:57](https://github.com/emmabostian/developer-portfolios/blob/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2/src/remove_emoji_in_readme.py#L57)
- [src/run_dup_report.py:91](https://github.com/emmabostian/developer-portfolios/blob/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2/src/run_dup_report.py#L91)
- [src/run_tests.py:44](https://github.com/emmabostian/developer-portfolios/blob/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2/src/run_tests.py#L44)
- [run_tests.py:25](https://github.com/emmabostian/developer-portfolios/blob/cecf27d06a4cdb391ad4a031afc0d510ef71a0a2/run_tests.py#L25)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _follow, _has_gambling_title, _has_parking_content, _is_emoji_codepoint, _is_parking_dom… |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestAlphabetical, TestEmojiDetection, TestFindMalformedUrls, TestFixEscapedUrlScheme, TestFullStackVariants,… |

## Important files

- `.github/workflows/link-checker.yml` (ci)
- `.github/workflows/parking-redirect-checker.yml` (ci)
- `.lycherc.toml` (config)

## Top-level layout

- `(root files)` — 7 analysed file(s)
- `tests` — 7 analysed file(s)
- `src` — 6 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cecf27d06a4cdb391ad4a031afc0d510ef71a0a2` is the revision these paths and observations refer to.
