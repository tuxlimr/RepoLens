# Project structure: jasontaylordev/CleanArchitecture

**Analysed commit:** `e1ab4cc4d5d7b4e25e57bd8b0514b766573b8c04`

**Commit reference:** [e1ab4cc4d5d7b4e25e57bd8b0514b766573b8c04](https://github.com/jasontaylordev/CleanArchitecture/commit/e1ab4cc4d5d7b4e25e57bd8b0514b766573b8c04)

**Tree at this commit:** [jasontaylordev/CleanArchitecture@e1ab4cc4d5d7](https://github.com/jasontaylordev/CleanArchitecture/tree/e1ab4cc4d5d7b4e25e57bd8b0514b766573b8c04)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jasontaylordev/CleanArchitecture |
| Description | Clean Architecture Solution Template for ASP.NET Core |
| Stars | 20719 |
| Forks | 4305 |
| Licence | MIT |
| Language | C# |
| Default branch | main |
| Analysed commit | `e1ab4cc4d5d7b4e25e57bd8b0514b766573b8c04` |
| Retrieved at | 2026-11-14T19:13:10.711108+00:00 |
| Files in this snapshot | 244 |

## Directory tree

```text
.devcontainer/  (2 files)
  README.md
  devcontainer.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (4 files)
    build.yml
    codeql.yml
    release.yml
    test-templates.yml
  FUNDING.yml
.template.config/  (3 files)
  dotnetcli.host.json
  ide.host.json
  template.json
docs/  (5 files)
  decisions/  (5 files)
    ADR-000-template.md
    ADR-001-Use-EFCore-In-Application-Layer.md
    ADR-002-Aspire-For-Orchestration-And-Testing.md
    ADR-003-MediatR-Contracts-In-Domain.md
    README.md
src/  (166 files)
  AppHost/  (6 files)
    Properties/  (1 files)
      … 1 files under this directory
    AppHost.csproj
    Extensions.cs
    Program.cs
    appsettings.Development.json
    appsettings.json
  Application/  (34 files)
    Common/  (13 files)
      … 13 files under this directory
    TodoItems/  (7 files)
      … 7 files under this directory
    TodoLists/  (9 files)
      … 9 files under this directory
    WeatherForecasts/  (2 files)
      … 2 files under this directory
    Application.csproj
    DependencyInjection.cs
    GlobalUsings.cs
  Domain/  (13 files)
    Common/  (4 files)
      … 4 files under this directory
    Constants/  (1 files)
      … 1 files under this directory
    Entities/  (2 files)
      … 2 files under this directory
    Enums/  (1 files)
      … 1 files under this directory
    Events/  (1 files)
      … 1 files under this directory
    Exceptions/  (1 files)
      … 1 files under this directory
    ValueObjects/  (1 files)
      … 1 files under this directory
    Domain.csproj
    GlobalUsings.cs
  Infrastructure/  (12 files)
    Data/  (6 files)
      … 6 files under this directory
    Identity/  (3 files)
      … 3 files under this directory
    DependencyInjection.cs
    GlobalUsings.cs
    Infrastructure.csproj
  ServiceDefaults/  (2 files)
    Extensions.cs
    ServiceDefaults.csproj
  Shared/  (2 files)
    Services.cs
    Shared.csproj
  Web/  (97 files)
    ClientApp/  (47 files)
      … 47 files under this directory
    ClientApp-React/  (26 files)
      … 26 files under this directory
    Endpoints/  (4 files)
      … 4 files under this directory
    Infrastructure/  (8 files)
      … 8 files under this directory
    Properties/  (1 files)
      … 1 files under this directory
    Services/  (1 files)
      … 1 files under this directory
    DependencyInjection.cs
    GlobalUsings.cs
    Program.cs
    Web-webapi.http
    Web.csproj
    Web.http
    appsettings.PostgreSQL.json
    appsettings.SQLServer.json
    appsettings.SQLite.json
    appsettings.json
templates/  (4 files)
  ca-use-case/  (4 files)
    .template.config/  (2 files)
      … 2 files under this directory
    FeatureName/  (2 files)
      … 2 files under this directory
tests/  (42 files)
  Application.FunctionalTests/  (15 files)
    Infrastructure/  (4 files)
      … 4 files under this directory
    TodoItems/  (4 files)
      … 4 files under this directory
    TodoLists/  (4 files)
      … 4 files under this directory
    Application.FunctionalTests.csproj
    FunctionalTestSetup.cs
    GlobalUsings.cs
  Application.UnitTests/  (4 files)
    Common/  (3 files)
      … 3 files under this directory
    Application.UnitTests.csproj
  Domain.UnitTests/  (2 files)
    ValueObjects/  (1 files)
      … 1 files under this directory
    Domain.UnitTests.csproj
  Infrastructure.IntegrationTests/  (2 files)
    GlobalUsings.cs
    Infrastructure.IntegrationTests.csproj
  TestAppHost/  (2 files)
    Program.cs
    TestAppHost.csproj
  Web.AcceptanceTests/  (17 files)
    Features/  (4 files)
      … 4 files under this directory
    Pages/  (5 files)
      … 5 files under this directory
    StepDefinitions/  (4 files)
      … 4 files under this directory
    AspireSetup.cs
    GlobalUsings.cs
    PlaywrightSetup.cs
    Web.AcceptanceTests.csproj
.editorconfig
.gitattributes
.gitignore
CODE_OF_CONDUCT.md
CleanArchitecture.nuspec
CleanArchitecture.slnx
Directory.Build.props
Directory.Packages.props
LICENSE
README-template.md
README.md
aspire.config.json
global.json
renovate.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| AppHost package | library | Observed | Groups 2 file(s) under apphost package (observed from repository paths and static analysis). |
| Application package | library | Observed | Groups 31 file(s) under application package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 8 file(s) under data layer (observed from repository paths and static analysis). |
| Infrastructure package | library | Observed | Groups 5 file(s) under infrastructure package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 13 file(s) under service / domain layer (observed from repository paths and static analysis). |
| ServiceDefaults package | library | Observed | Groups 1 file(s) under servicedefaults package (observed from repository paths and static analysis). |
| Shared package | library | Observed | Groups 1 file(s) under shared package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 2 file(s) under templates package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 42 file(s) under tests (observed from repository paths and static analysis). |
| Web package | library | Observed | Groups 52 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test-templates.yml` (ci)
- `.template.config/dotnetcli.host.json` (config)
- `.template.config/ide.host.json` (config)
- `.template.config/template.json` (config)
- `aspire.config.json` (config)
- `global.json` (config)
- `renovate.json` (config)
- `src/AppHost/Properties/launchSettings.json` (config)
- `src/AppHost/appsettings.Development.json` (config)
- `src/AppHost/appsettings.json` (config)
- `src/Web/ClientApp-React/nswag.json` (config)
- `src/Web/ClientApp-React/package.json` (manifest)
- `src/Web/ClientApp-React/tsconfig.json` (config)
- `src/Web/ClientApp/.editorconfig` (config)
- `src/Web/ClientApp/angular.json` (config)
- `src/Web/ClientApp/nswag.json` (config)
- `src/Web/ClientApp/package.json` (manifest)
- `src/Web/ClientApp/tsconfig.app.json` (config)
- `src/Web/ClientApp/tsconfig.json` (config)
- `src/Web/ClientApp/tsconfig.spec.json` (config)
- `src/Web/Properties/launchSettings.json` (config)
- `src/Web/appsettings.PostgreSQL.json` (config)
- `src/Web/appsettings.SQLServer.json` (config)
- `src/Web/appsettings.SQLite.json` (config)
- `src/Web/appsettings.json` (config)
- `templates/ca-use-case/.template.config/dotnetcli.host.json` (config)
- `templates/ca-use-case/.template.config/template.json` (config)

## Top-level layout

- `src` — 166 analysed file(s)
- `tests` — 42 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 8 analysed file(s)
- `docs` — 5 analysed file(s)
- `templates` — 4 analysed file(s)
- `.template.config` — 3 analysed file(s)
- `.devcontainer` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e1ab4cc4d5d7b4e25e57bd8b0514b766573b8c04` is the revision these paths and observations refer to.
