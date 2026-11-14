# Project structure: pterodactyl/panel

**Analysed commit:** `90b2aa87469da4fffd941b3c99f3c1ca48a01b78`

**Commit reference:** [90b2aa87469da4fffd941b3c99f3c1ca48a01b78](https://github.com/pterodactyl/panel/commit/90b2aa87469da4fffd941b3c99f3c1ca48a01b78)

**Tree at this commit:** [pterodactyl/panel@90b2aa87469d](https://github.com/pterodactyl/panel/tree/90b2aa87469da4fffd941b3c99f3c1ca48a01b78)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pterodactyl/panel |
| Description | Pterodactyl® is a free, open-source game server management panel built with PHP, React, and Go. Designed with security in mind, Pterodactyl runs all game servers in isolated Docker containers while exposing a beautiful and intuitive UI to end users. |
| Stars | 9512 |
| Forks | 2750 |
| Licence | Other |
| Language | PHP |
| Default branch | 1.0-develop |
| Analysed commit | `90b2aa87469da4fffd941b3c99f3c1ca48a01b78` |
| Retrieved at | 2026-11-14T19:13:33.917142+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (16 files)
  ISSUE_TEMPLATE/  (3 files)
    1-bug-report.yml
    2-approved.yml
    config.yml
  assets/  (2 files)
    logo-dark.svg
    logo-light.svg
  docker/  (6 files)
    README.md
    default.conf
    default_ssl.conf
    entrypoint.sh
    supervisord.conf
    www.conf
  workflows/  (4 files)
    build.yaml
    ci.yaml
    docker.yaml
    release.yaml
  FUNDING.yml
app/  (566 files)
  Console/  (24 files)
    Commands/  (22 files)
      … 22 files under this directory
    Kernel.php
    RequiresDatabaseMigrations.php
  Contracts/  (25 files)
    Core/  (1 files)
      … 1 files under this directory
    Criteria/  (1 files)
      … 1 files under this directory
    Extensions/  (1 files)
      … 1 files under this directory
    Http/  (1 files)
      … 1 files under this directory
    Models/  (1 files)
      … 1 files under this directory
    Repository/  (20 files)
      … 20 files under this directory
  Enum/  (2 files)
    JwtScope.php
    ResourceLimit.php
  Events/  (24 files)
    Auth/  (4 files)
      … 4 files under this directory
    Server/  (9 files)
      … 9 files under this directory
    Subuser/  (4 files)
      … 4 files under this directory
    User/  (5 files)
      … 5 files under this directory
    ActivityLogged.php
    Event.php
  Exceptions/  (52 files)
    Http/  (7 files)
      … 7 files under this directory
    Model/  (1 files)
      … 1 files under this directory
    Repository/  (4 files)
      … 4 files under this directory
    Service/  (32 files)
      … 32 files under this directory
    Solutions/  (1 files)
      … 1 files under this directory
    Transformer/  (1 files)
      … 1 files under this directory
    AccountNotFoundException.php
    AutoDeploymentException.php
    DisplayException.php
    Handler.php
    ManifestDoesNotExistException.php
    PterodactylException.php
  Extensions/  (12 files)
    Backups/  (1 files)
      … 1 files under this directory
    Facades/  (1 files)
      … 1 files under this directory
    Filesystem/  (1 files)
      … 1 files under this directory
    Illuminate/  (2 files)
      … 2 files under this directory
    Laravel/  (1 files)
      … 1 files under this directory
    Lcobucci/  (1 files)
      … 1 files under this directory
    League/  (1 files)
      … 1 files under this directory
    Spatie/  (1 files)
      … 1 files under this directory
    Themes/  (1 files)
      … 1 files under this directory
    DynamicDatabaseConnection.php
    Hashids.php
  Facades/  (3 files)
    Activity.php
    LogBatch.php
    LogTarget.php
  Helpers/  (2 files)
    Time.php
    Utilities.php
  Http/  (222 files)
    Controllers/  (79 files)
      … 79 files under this directory
    Middleware/  (23 files)
      … 23 files under this directory
    Requests/  (117 files)
      … 117 files under this directory
    Resources/  (1 files)
      … 1 files under this directory
    ViewComposers/  (1 files)
      … 1 files under this directory
    Kernel.php
  Jobs/  (2 files)
    Schedule/  (1 files)
      … 1 files under this directory
    RevokeSftpAccessJob.php
  Listeners/  (3 files)
    AuthenticationListener.php
    RevocationListener.php
    TwoFactorListener.php
  Models/  (38 files)
    Attributes/  (1 files)
      … 1 files under this directory
    Filters/  (2 files)
      … 2 files under this directory
    Objects/  (1 files)
      … 1 files under this directory
    Traits/  (2 files)
      … 2 files under this directory
    APILog.php
    ActivityLog.php
    ActivityLogSubject.php
    Allocation.php
    ApiKey.php
    AuditLog.php
    Backup.php
    Database.php
    DatabaseHost.php
    Egg.php
    EggMount.php
    EggVariable.php
    Location.php
    Model.php
    Mount.php
    MountNode.php
    MountServer.php
    Nest.php
    Node.php
    Permission.php
    RecoveryToken.php
    Schedule.php
    Server.php
    ServerTransfer.php
    … 8 more files
  Notifications/  (6 files)
    AccountCreated.php
    AddedToServer.php
    MailTested.php
    RemovedFromServer.php
    SendPasswordReset.php
    ServerInstalled.php
  Observers/  (4 files)
    EggVariableObserver.php
    ServerObserver.php
    SubuserObserver.php
    UserObserver.php
  Policies/  (2 files)
    .gitkeep
    ServerPolicy.php
  Providers/  (12 files)
    ActivityLogServiceProvider.php
    AppServiceProvider.php
    AuthServiceProvider.php
    BackupsServiceProvider.php
    BladeServiceProvider.php
    BroadcastServiceProvider.php
    EventServiceProvider.php
    HashidsServiceProvider.php
    RepositoryServiceProvider.php
    RouteServiceProvider.php
    SettingsServiceProvider.php
    ViewComposerServiceProvider.php
  Repositories/  (32 files)
    Eloquent/  (22 files)
      … 22 files under this directory
    Wings/  (9 files)
      … 9 files under this directory
    Repository.php
  Rules/  (2 files)
    Fqdn.php
    Username.php
  Services/  (62 files)
    Acl/  (1 files)
      … 1 files under this directory
    Activity/  (3 files)
      … 3 files under this directory
    Allocations/  (3 files)
      … 3 files under this directory
    Api/  (1 files)
      … 1 files under this directory
    Backups/  (3 files)
      … 3 files under this directory
    Databases/  (6 files)
      … 6 files under this directory
    Deployment/  (2 files)
      … 2 files under this directory
    Eggs/  (11 files)
      … 11 files under this directory
    Helpers/  (2 files)
      … 2 files under this directory
    Locations/  (3 files)
      … 3 files under this directory
    Nests/  (3 files)
      … 3 files under this directory
    Nodes/  (4 files)
      … 4 files under this directory
    Schedules/  (1 files)
      … 1 files under this directory
    Servers/  (12 files)
      … 12 files under this directory
    Subusers/  (1 files)
      … 1 files under this directory
    Telemetry/  (1 files)
      … 1 files under this directory
    Users/  (5 files)
      … 5 files under this directory
  Traits/  (6 files)
    Commands/  (1 files)
      … 1 files under this directory
    Controllers/  (1 files)
      … 1 files under this directory
    Helpers/  (1 files)
      … 1 files under this directory
    Services/  (3 files)
      … 3 files under this directory
  Transformers/  (30 files)
    Api/  (30 files)
      … 30 files under this directory
  helpers.php
bootstrap/  (3 files)
  cache/  (1 files)
    .gitignore
  app.php
  tests.php
config/  (29 files)
  egg_features/  (1 files)
    eula.php
  prologue/  (1 files)
    alerts.php
  activity.php
  addons.php
  app.php
  auth.php
  backups.php
  broadcasting.php
  cache.php
  compile.php
  cors.php
  database.php
  filesystems.php
  fractal.php
  hashids.php
  hashing.php
  http.php
  ide-helper.php
  javascript.php
  logging.php
  mail.php
  pterodactyl.php
  queue.php
  recaptcha.php
  sanctum.php
  services.php
  … 3 more files
database/  (168 files)
  Factories/  (17 files)
    AllocationFactory.php
    ApiKeyFactory.php
    BackupFactory.php
    DatabaseFactory.php
    DatabaseHostFactory.php
    EggFactory.php
    EggVariableFactory.php
    LocationFactory.php
    NestFactory.php
    NodeFactory.php
    ScheduleFactory.php
    ServerFactory.php
    ServerTransferFactory.php
    SubuserFactory.php
    TaskFactory.php
    UserFactory.php
    UserSSHKeyFactory.php
  Seeders/  (18 files)
    eggs/  (14 files)
      … 14 files under this directory
    .gitkeep
    DatabaseSeeder.php
    EggSeeder.php
    NestSeeder.php
  migrations/  (132 files)
    2016_01_23_195641_add_allocations_table.php
    2016_01_23_195851_add_api_keys.php
    2016_01_23_200044_add_api_permissions.php
    2016_01_23_200159_add_downloads.php
    2016_01_23_200421_create_failed_jobs_table.php
    2016_01_23_200440_create_jobs_table.php
    2016_01_23_200528_add_locations.php
    2016_01_23_200648_add_nodes.php
    2016_01_23_201433_add_password_resets.php
    2016_01_23_201531_add_permissions.php
    2016_01_23_201649_add_server_variables.php
    2016_01_23_201748_add_servers.php
    2016_01_23_202544_add_service_options.php
    2016_01_23_202731_add_service_varibles.php
    2016_01_23_202943_add_services.php
    2016_01_23_203119_create_settings_table.php
    2016_01_23_203150_add_subusers.php
    2016_01_23_203159_add_users.php
    2016_01_23_203947_create_sessions_table.php
    2016_01_25_234418_rename_permissions_column.php
    2016_02_07_172148_add_databases_tables.php
    2016_02_07_181319_add_database_servers_table.php
    2016_02_13_154306_add_service_option_default_startup.php
    2016_02_20_155318_add_unique_service_field.php
    … 108 more files
  .gitignore
.editorconfig
.env.example
.eslintignore
.eslintrc.js
.gitignore
.php-cs-fixer.dist.php
.prettierrc.json
BUILDING.md
CHANGELOG.md
CONTRIBUTING.md
Dockerfile
LICENSE.md
README.md
SECURITY.md
artisan
babel.config.js
composer.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 211 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 159 file(s) under app package (observed from repository paths and static analysis). |
| bootstrap package | library | Observed | Groups 2 file(s) under bootstrap package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 48 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 251 file(s) under data layer (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 93 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/1-bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/2-approved.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/build.yaml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/docker.yaml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.prettierrc.json` (config)
- `Dockerfile` (container)
- `composer.json` (config)
- `database/Seeders/eggs/minecraft/egg-bungeecord.json` (config)
- `database/Seeders/eggs/minecraft/egg-forge-minecraft.json` (config)
- `database/Seeders/eggs/minecraft/egg-paper.json` (config)
- `database/Seeders/eggs/minecraft/egg-sponge--sponge-vanilla.json` (config)
- `database/Seeders/eggs/minecraft/egg-vanilla-minecraft.json` (config)
- `database/Seeders/eggs/rust/egg-rust.json` (config)
- `database/Seeders/eggs/source-engine/egg-ark--survival-evolved.json` (config)
- `database/Seeders/eggs/source-engine/egg-counter--strike--global-offensive.json` (config)
- `database/Seeders/eggs/source-engine/egg-custom-source-engine-game.json` (config)
- `database/Seeders/eggs/source-engine/egg-garrys-mod.json` (config)
- `database/Seeders/eggs/source-engine/egg-insurgency.json` (config)
- `database/Seeders/eggs/source-engine/egg-team-fortress2.json` (config)
- `database/Seeders/eggs/voice-servers/egg-mumble-server.json` (config)
- `database/Seeders/eggs/voice-servers/egg-teamspeak3-server.json` (config)

## Top-level layout

- `app` — 566 analysed file(s)
- `database` — 168 analysed file(s)
- `config` — 29 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 16 analysed file(s)
- `bootstrap` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `90b2aa87469da4fffd941b3c99f3c1ca48a01b78` is the revision these paths and observations refer to.
