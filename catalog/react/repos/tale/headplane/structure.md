# Project structure: tale/headplane

**Analysed commit:** `c8c192dbf0ade31f5947777fa4f46e45885edb49`

**Commit reference:** [c8c192dbf0ade31f5947777fa4f46e45885edb49](https://github.com/tale/headplane/commit/c8c192dbf0ade31f5947777fa4f46e45885edb49)

**Tree at this commit:** [tale/headplane@c8c192dbf0ad](https://github.com/tale/headplane/tree/c8c192dbf0ade31f5947777fa4f46e45885edb49)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tale/headplane |
| Description | A feature-complete Web UI for Headscale |
| Stars | 3304 |
| Forks | 269 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `c8c192dbf0ade31f5947777fa4f46e45885edb49` |
| Retrieved at | 2026-11-14T19:15:25.889189+00:00 |
| Files in this snapshot | 434 |

## Directory tree

```text
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (19 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yaml
    config.yml
    feature-request.yaml
  workflows/  (11 files)
    automated.yaml
    build.yaml
    docs-beta.yaml
    docs-build.yaml
    docs-publish.yaml
    labeler.yaml
    lifecycle.yaml
    pullfrog.yml
    release.yaml
    stale.yaml
    triage.yaml
  CODEOWNERS
  CONTRIBUTING.md
  FUNDING.yml
  SECURITY.md
  labeler.yml
app/  (213 files)
  assets/  (4 files)
    android.svg
    ios.svg
    macos.svg
    windows.svg
  components/  (34 files)
    tags/  (5 files)
      … 5 files under this directory
    action-dialog.tsx
    attribute.tsx
    avatar.tsx
    button.tsx
    callout.tsx
    card.tsx
    chip.tsx
    code-block.tsx
    code.tsx
    dialog.tsx
    field.tsx
    filter-dropdown.tsx
    input.tsx
    link.tsx
    list.tsx
    logo-mark.tsx
    menu.tsx
    number-input.tsx
    page-error.tsx
    page-header.tsx
    radio-group.tsx
    section.tsx
    select.tsx
    status-circle.tsx
    … 5 more files
  layout/  (5 files)
    app.tsx
    error-page.tsx
    footer.tsx
    header.tsx
    scrollbar.tsx
  routes/  (96 files)
    acls/  (16 files)
      … 16 files under this directory
    auth/  (11 files)
      … 11 files under this directory
    dns/  (13 files)
      … 13 files under this directory
    machines/  (16 files)
      … 16 files under this directory
    settings/  (13 files)
      … 13 files under this directory
    ssh/  (6 files)
      … 6 files under this directory
    users/  (15 files)
      … 15 files under this directory
    util/  (5 files)
      … 5 files under this directory
    home.tsx
  server/  (43 files)
    config/  (10 files)
      … 10 files under this directory
    db/  (2 files)
      … 2 files under this directory
    headscale/  (15 files)
      … 15 files under this directory
    oidc/  (1 files)
      … 1 files under this directory
    web/  (5 files)
      … 5 files under this directory
    ARCHITECTURE.md
    README.md
    app.ts
    assets.ts
    context.ts
    feature.ts
    hp-agent.ts
    main.ts
    result.ts
    tailscale-release.ts
  types/  (7 files)
    HostInfo.ts
    Key.ts
    Machine.ts
    PreAuthKey.ts
    Route.ts
    User.ts
    index.ts
  utils/  (17 files)
    acl-policy.ts
    cn.ts
    color-scheme.ts
    copy.ts
    describe-error.ts
    form.ts
    host-info.ts
    live-data.tsx
    log.ts
    node-info.ts
    oidc-state.ts
    register-key.ts
    res.ts
    time.ts
    toast-provider.tsx
    toast.ts
    user.ts
  entry.client.tsx
  entry.server.tsx
  globals.d.ts
  root.tsx
  routes.ts
  tailwind.css
  tokens.css
cmd/  (5 files)
  fake_sh/  (1 files)
    fake_sh.go
  hp_agent/  (1 files)
    hp_agent.go
  hp_healthcheck/  (1 files)
    hp_healthcheck.go
  hp_ssh/  (2 files)
    build-tags.txt
    wasm_js.go
docs/  (60 files)
  app/  (26 files)
    components/  (13 files)
      … 13 files under this directory
    lib/  (5 files)
      … 5 files under this directory
    routes/  (4 files)
      … 4 files under this directory
    app.css
    env.d.ts
    root.tsx
    routes.ts
  configuration/  (8 files)
    api-keys.md
    compose-examples.ts
    index.md
    integrations.mdx
    meta.json
    reverse-proxy.mdx
    sensitive-values.md
    tls.md
  features/  (7 files)
    acls.mdx
    agent.mdx
    meta.json
    proxy-auth.md
    ssh.mdx
    sso.mdx
    users-roles.mdx
  install/  (5 files)
    docker.mdx
    index.mdx
    meta.json
    native-mode.mdx
    nix.md
  public/  (2 files)
    _redirects
    favicon.svg
  reference/  (2 files)
    meta.json
    nixos-options.md
  scripts/  (1 files)
    finish-build.ts
  introduction.mdx
  meta.json
  quickstart-examples.ts
  quickstart.mdx
  react-router.config.ts
  troubleshooting.mdx
  tsconfig.json
  upgrading.mdx
  vite.config.ts
drizzle/  (16 files)
  20250619175127_spicy_bloodscream/  (2 files)
    migration.sql
    snapshot.json
  20250818220542_naive_lilith/  (2 files)
    migration.sql
    snapshot.json
  20250819153327_square_bloodstorm/  (2 files)
    migration.sql
    snapshot.json
  20260307210718_thick_otto_octavius/  (2 files)
    migration.sql
    snapshot.json
  20260314162950_nappy_praxagora/  (2 files)
    migration.sql
    snapshot.json
  20260330175441_add_user_picture/  (2 files)
    migration.sql
    snapshot.json
  20260408181638_parallel_synch/  (2 files)
    migration.sql
    snapshot.json
  20260426221245_add_oidc_id_token/  (2 files)
    migration.sql
    snapshot.json
internal/  (6 files)
  config/  (3 files)
    config.go
    config_test.go
    preflight.go
  tsnet/  (2 files)
    peers.go
    server.go
  util/  (1 files)
    logger.go
nix/  (7 files)
  agent.nix
  docs.js
  docs.nix
  module.nix
  options.nix
  package.nix
  ssh-wasm.nix
patches/  (5 files)
  tailscale-netcheck-derp-port.patch
  tsconnect-ssh-banner.patch
  tsconnect-term-type.patch
  tsconnect-types.patch
  tsconnect-utf8-chunks.patch
public/  (1 files)
  favicon.svg
runtime/  (2 files)
  http.ts
  vite-plugin.ts
scripts/  (3 files)
  release.ts
  sync-tsconnect.sh
  wasm-tags.go
tests/  (69 files)
  harness/  (18 files)
    scenarios/  (3 files)
      … 3 files under this directory
    agent-hostinfo.ts
    browser-ssh-client.ts
    browser-ssh.ts
    cli.ts
    dex.ts
    headplane.ts
    headscale.ts
    launch.ts
    loadgen.go
    node.ts
    scenario.ts
    screenshots.ts
    tailnet.ts
    versions.ts
    wait.ts
  integration/  (27 files)
    agent/  (6 files)
      … 6 files under this directory
    harness/  (2 files)
      … 2 files under this directory
    headplane/  (12 files)
      … 12 files under this directory
    headscale/  (1 files)
      … 1 files under this directory
    oidc/  (1 files)
      … 1 files under this directory
    platform/  (3 files)
      … 3 files under this directory
    ssh/  (2 files)
      … 2 files under this directory
  support/  (2 files)
    app.ts
    temp.ts
  unit/  (21 files)
    auth/  (3 files)
      … 3 files under this directory
    config/  (5 files)
      … 5 files under this directory
    headscale/  (6 files)
      … 6 files under this directory
    oidc/  (1 files)
      … 1 files under this directory
    runtime/  (1 files)
      … 1 files under this directory
    utils/  (5 files)
      … 5 files under this directory
  README.md
.dockerignore
.gitattributes
.gitignore
.oxfmtrc.json
.oxlintrc.json
AGENTS.md
CHANGELOG.md
Caddyfile
Dockerfile
LICENSE
README.md
build.sh
compose.yaml
config.example.yaml
drizzle.config.ts
flake.lock
flake.nix
go.mod
go.sum
lefthook.yml
mise.toml
package.json
react-router.config.ts
tsconfig.json
… 2 more files
```

## Entry points

- [app/layout/app.tsx](https://github.com/tale/headplane/blob/c8c192dbf0ade31f5947777fa4f46e45885edb49/app/layout/app.tsx)
- [app/routes/ssh/page.tsx](https://github.com/tale/headplane/blob/c8c192dbf0ade31f5947777fa4f46e45885edb49/app/routes/ssh/page.tsx)
- [app/server/app.ts](https://github.com/tale/headplane/blob/c8c192dbf0ade31f5947777fa4f46e45885edb49/app/server/app.ts)
- [app/server/main.ts](https://github.com/tale/headplane/blob/c8c192dbf0ade31f5947777fa4f46e45885edb49/app/server/main.ts)
- [app/types/index.ts](https://github.com/tale/headplane/blob/c8c192dbf0ade31f5947777fa4f46e45885edb49/app/types/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 108 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 85 file(s) under app package (observed from repository paths and static analysis). |
| cmd package | library | Observed | Groups 4 file(s) under cmd package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 3 file(s) under internal package (observed from repository paths and static analysis). |
| nix package | library | Observed | Groups 1 file(s) under nix package (observed from repository paths and static analysis). |
| runtime package | library | Observed | Groups 2 file(s) under runtime package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 69 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yaml` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/automated.yaml` (ci)
- `.github/workflows/build.yaml` (ci)
- `.github/workflows/docs-beta.yaml` (ci)
- `.github/workflows/docs-build.yaml` (ci)
- `.github/workflows/docs-publish.yaml` (ci)
- `.github/workflows/labeler.yaml` (ci)
- `.github/workflows/lifecycle.yaml` (ci)
- `.github/workflows/pullfrog.yml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/stale.yaml` (ci)
- `.github/workflows/triage.yaml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `Dockerfile` (container)
- `compose.yaml` (container)
- `config.example.yaml` (config)
- `docs/configuration/meta.json` (config)
- `docs/features/meta.json` (config)
- `docs/install/meta.json` (config)
- `docs/meta.json` (config)
- `docs/reference/meta.json` (config)
- `docs/tsconfig.json` (config)
- `drizzle/20250619175127_spicy_bloodscream/snapshot.json` (config)
- `drizzle/20250818220542_naive_lilith/snapshot.json` (config)
- `drizzle/20250819153327_square_bloodstorm/snapshot.json` (config)
- `drizzle/20260307210718_thick_otto_octavius/snapshot.json` (config)
- `drizzle/20260314162950_nappy_praxagora/snapshot.json` (config)
- `drizzle/20260330175441_add_user_picture/snapshot.json` (config)
- `drizzle/20260408181638_parallel_synch/snapshot.json` (config)
- `drizzle/20260426221245_add_oidc_id_token/snapshot.json` (config)
- `go.mod` (manifest)
- `lefthook.yml` (config)
- `mise.toml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `app` — 213 analysed file(s)
- `tests` — 69 analysed file(s)
- `docs` — 60 analysed file(s)
- `(root files)` — 26 analysed file(s)
- `.github` — 19 analysed file(s)
- `drizzle` — 16 analysed file(s)
- `nix` — 7 analysed file(s)
- `internal` — 6 analysed file(s)
- `cmd` — 5 analysed file(s)
- `patches` — 5 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `runtime` — 2 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c8c192dbf0ade31f5947777fa4f46e45885edb49` is the revision these paths and observations refer to.
