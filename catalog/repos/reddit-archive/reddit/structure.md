# Project structure: reddit-archive/reddit

**Analysed commit:** `753b17407e9a9dca09558526805922de24133d53`

**Commit reference:** [753b17407e9a9dca09558526805922de24133d53](https://github.com/reddit-archive/reddit/commit/753b17407e9a9dca09558526805922de24133d53)

**Tree at this commit:** [reddit-archive/reddit@753b17407e9a](https://github.com/reddit-archive/reddit/tree/753b17407e9a9dca09558526805922de24133d53)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reddit-archive/reddit |
| Description | historical code from reddit.com |
| Stars | 16949 |
| Forks | 2842 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `753b17407e9a9dca09558526805922de24133d53` |
| Retrieved at | 2026-11-14T19:08:39.997456+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
install/  (14 files)
  README.md
  done.sh
  drone.sh
  install.cfg
  install_apt.sh
  install_cassandra.sh
  install_services.sh
  install_zookeeper.sh
  reddit.sh
  setup_cassandra.sh
  setup_mcrouter.sh
  setup_postgres.sh
  setup_rabbitmq.sh
  travis.sh
r2/  (778 files)
  r2/  (771 files)
    config/  (14 files)
      … 14 files under this directory
    controllers/  (35 files)
      … 35 files under this directory
    data/  (1 files)
      … 1 files under this directory
    lib/  (163 files)
      … 163 files under this directory
    models/  (33 files)
      … 33 files under this directory
    public/  (168 files)
      … 168 files under this directory
    templates/  (315 files)
      … 315 files under this directory
    tests/  (40 files)
      … 40 files under this directory
    __init__.py
    commands.py
  Makefile
  Makefile.py
  babel.cfg
  check-code
  coverage.sh
  example.ini
  pylintrc
.drone.yml
.gitignore
.travis.yml
LICENSE
README.md
SECURITY.md
Vagrantfile
install-reddit.sh
```

## Entry points

- [r2/r2/lib/contrib/rcssmin.py:344](https://github.com/reddit-archive/reddit/blob/753b17407e9a9dca09558526805922de24133d53/r2/r2/lib/contrib/rcssmin.py#L344)
- [r2/r2/lib/einhorn.py:95](https://github.com/reddit-archive/reddit/blob/753b17407e9a9dca09558526805922de24133d53/r2/r2/lib/einhorn.py#L95)
- [r2/r2/lib/static.py:96](https://github.com/reddit-archive/reddit/blob/753b17407e9a9dca09558526805922de24133d53/r2/r2/lib/static.py#L96)
- [r2/r2/lib/totp.py:68](https://github.com/reddit-archive/reddit/blob/753b17407e9a9dca09558526805922de24133d53/r2/r2/lib/totp.py#L68)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 35 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: APIv1GoldController, APIv1LoginController, APIv1ScopesController, APIv1UserController, AdController, Ad… |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: CleanupMiddleware, DomainListingMiddleware, DomainMiddleware, ExtensionMiddleware, F… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 45 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AccountSRFeedback, AccountSRPrefs, AccountsByIP, AdImpressionsByCodename, AdminNotesBySystem, AdminToo… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: EinhornSyncWorker. Observed top-level functions: _make_cssmin, generate_secret, generate_s… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| install package | library | Observed | Groups 12 file(s) under install package (observed from repository paths and static analysis). |
| r2 package | library | Observed | Groups 263 file(s) under r2 package (observed from repository paths and static analysis). Observed top-level classes: AbortWikiError, AccountJsonTemplate, Address, AddressValueError, AdminDetailsBar, AdminKindMenu. Obse… |
| Tests | test | Observed | Groups 40 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH r2.lib.authorize.api.CreateCustomerProfileRequest, PATCH r2.lib.authorize.api.Profile, PATCH r2.lib.authorize.ap… |

## Important files

- `.drone.yml` (config)
- `.travis.yml` (ci)
- `install/install.cfg` (config)
- `r2/babel.cfg` (config)
- `r2/example.ini` (config)
- `r2/r2/data/locations.json` (config)

## Top-level layout

- `r2` — 778 analysed file(s)
- `install` — 14 analysed file(s)
- `(root files)` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File r2/Makefile.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/commands.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/controllers/embed.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/controllers/error.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/amqp.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/automoderator.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/cache.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/cookies.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/db/alter_db.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/db/queries.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/db/tdb_cassandra.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/db/tdb_sql.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/db/thing.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/emailer.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/emr_helpers.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/generate_strings.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/js.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/media.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/memoize.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/merge.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/migrate/campaigns_to_things.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/migrate/migrate.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/migrate/vote_details_ip_backfill.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/mr_tools/mr_tools.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/nymph.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/promote.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/providers/search/cloudsearch.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/providers/search/solr.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/s3_helpers.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/souptest.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/template_helpers.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/traffic/emr_traffic.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/traffic/traffic.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/translation.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/utils/utils.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/validator/validator.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/lib/voting.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/models/account.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/models/award.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/models/bidding.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/models/builder.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/models/mail_queue.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File r2/r2/models/subreddit.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `753b17407e9a9dca09558526805922de24133d53` is the revision these paths and observations refer to.
