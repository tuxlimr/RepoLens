# Project structure: twintproject/twint

**Analysed commit:** `e7c8a0c764f6879188e5c21e25fb6f1f856a7221`

**Commit reference:** [e7c8a0c764f6879188e5c21e25fb6f1f856a7221](https://github.com/twintproject/twint/commit/e7c8a0c764f6879188e5c21e25fb6f1f856a7221)

**Tree at this commit:** [twintproject/twint@e7c8a0c764f6](https://github.com/twintproject/twint/tree/e7c8a0c764f6879188e5c21e25fb6f1f856a7221)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | twintproject/twint |
| Description | An advanced Twitter scraping & OSINT tool written in Python that doesn't use Twitter's API, allowing you to scrape a user's followers, following, Tweets and more while evading most API limitations. |
| Stars | 16410 |
| Forks | 2722 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `e7c8a0c764f6879188e5c21e25fb6f1f856a7221` |
| Retrieved at | 2026-11-14T19:08:48.170305+00:00 |
| Files in this snapshot | 40 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (1 files)
    ISSUE_TEMPLATE.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
elasticsearch/  (6 files)
  README.md
  dashboard.json
  index-follow.json
  index-tweets.json
  index-user.json
  visualizations.json
twint/  (21 files)
  storage/  (6 files)
    __init__.py
    db.py
    elasticsearch.py
    panda.py
    write.py
    write_meta.py
  __init__.py
  __version__.py
  cli.py
  config.py
  datelock.py
  feed.py
  format.py
  get.py
  output.py
  run.py
  token.py
  tweet.py
  url.py
  user.py
  verbose.py
.gitignore
.travis.yml
Dockerfile
LICENSE
MANIFEST.in
README.md
automate.py
requirements.txt
setup.py
test.py
```

## Entry points

- [test.py:91](https://github.com/twintproject/twint/blob/e7c8a0c764f6879188e5c21e25fb6f1f856a7221/test.py#L91)
- [twint/cli.py](https://github.com/twintproject/twint/blob/e7c8a0c764f6879188e5c21e25fb6f1f856a7221/twint/cli.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Config. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: jobone, jobtwo. |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: RecycleObject. Observed top-level functions: Conn, Csv, Data, Fieldnames, Follow, Json. |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Twint. Observed top-level functions: Favorites, Followers, Following, Lookup, Profile, Sea… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| twint package | library | Observed | Groups 12 file(s) under twint package (observed from repository paths and static analysis). Observed top-level classes: Datelock, NoMoreTweetsException, RefreshTokenException, Token, TokenExpiryException, tweet. Observe… |

## Important files

- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `elasticsearch/dashboard.json` (config)
- `elasticsearch/index-follow.json` (config)
- `elasticsearch/index-tweets.json` (config)
- `elasticsearch/index-user.json` (config)
- `elasticsearch/visualizations.json` (config)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `twint` — 21 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `elasticsearch` — 6 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `e7c8a0c764f6879188e5c21e25fb6f1f856a7221` is the revision these paths and observations refer to.
