# Project structure: apache/answer

**Analysed commit:** `6744295fa888e0621fc9f9a8ace04f1a4daf8554`

**Commit reference:** [6744295fa888e0621fc9f9a8ace04f1a4daf8554](https://github.com/apache/answer/commit/6744295fa888e0621fc9f9a8ace04f1a4daf8554)

**Tree at this commit:** [apache/answer@6744295fa888](https://github.com/apache/answer/tree/6744295fa888e0621fc9f9a8ace04f1a4daf8554)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | apache/answer |
| Description | A Q&A platform software for teams at any scales. Whether it's a community forum, help center, or knowledge management platform, you can always count on Apache Answer. |
| Stars | 15712 |
| Forks | 1387 |
| Licence | Apache-2.0 |
| Language | Go |
| Default branch | main |
| Analysed commit | `6744295fa888e0621fc9f9a8ace04f1a4daf8554` |
| Retrieved at | 2026-11-14T19:13:16.237774+00:00 |
| Files in this snapshot | 796 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    config.yml
    enhancement_request.md
    feature_request.md
  PULL_REQUEST_TEMPLATE/  (1 files)
    pull_request_template.md
  workflows/  (7 files)
    build-binary-for-release.yml
    build-image-for-latest-release.yml
    build-image-for-manual.yml
    build-image-for-release.yml
    build-image-for-test.yml
    check-asf-header.yml
    lint.yml
.vaunt/  (1 files)
  config.yaml
.vscode/  (1 files)
  settings.json
charts/  (11 files)
  templates/  (7 files)
    _helpers.tpl
    deployment.yaml
    hpa.yaml
    ingress.yaml
    pvc.yaml
    service.yaml
    serviceaccount.yaml
  .helmignore
  Chart.yaml
  README.md
  values.yaml
cmd/  (5 files)
  answer/  (1 files)
    main.go
  command.go
  main.go
  wire.go
  wire_gen.go
configs/  (4 files)
  config.go
  config.yaml
  path_ignore.yaml
  reserved-usernames.json
docs/  (78 files)
  img/  (1 files)
    logo.svg
  release/  (77 files)
    licenses/  (75 files)
      … 75 files under this directory
    LICENSE
    NOTICE
i18n/  (46 files)
  af_ZA.yaml
  ar_SA.yaml
  az_AZ.yaml
  bal_BA.yaml
  ban_ID.yaml
  bn_BD.yaml
  bs_BA.yaml
  ca_ES.yaml
  cs_CZ.yaml
  cy_GB.yaml
  da_DK.yaml
  de_DE.yaml
  el_GR.yaml
  en_US.yaml
  es_ES.yaml
  fa_IR.yaml
  fi_FI.yaml
  fr_FR.yaml
  he_IL.yaml
  hi_IN.yaml
  hu_HU.yaml
  hy_AM.yaml
  i18n.go
  i18n.yaml
  … 22 more files
internal/  (436 files)
  base/  (58 files)
    conf/  (1 files)
      … 1 files under this directory
    constant/  (20 files)
      … 20 files under this directory
    cron/  (2 files)
      … 2 files under this directory
    data/  (2 files)
      … 2 files under this directory
    handler/  (4 files)
      … 4 files under this directory
    middleware/  (15 files)
      … 15 files under this directory
    pager/  (2 files)
      … 2 files under this directory
    path/  (1 files)
      … 1 files under this directory
    queue/  (2 files)
      … 2 files under this directory
    reason/  (2 files)
      … 2 files under this directory
    server/  (4 files)
      … 4 files under this directory
    translator/  (2 files)
      … 2 files under this directory
    validator/  (1 files)
      … 1 files under this directory
  cli/  (7 files)
    build.go
    config.go
    dump.go
    i18n.go
    install.go
    install_check.go
    reset_password.go
  controller/  (45 files)
    template_render/  (6 files)
      … 6 files under this directory
    activity_controller.go
    ai_controller.go
    ai_conversation_controller.go
    ai_tools_test.go
    answer_controller.go
    badge_controller.go
    collection_controller.go
    comment_controller.go
    connector_controller.go
    controller.go
    dashboard_controller.go
    embed_controller.go
    follow_controller.go
    lang_controller.go
    mcp_controller.go
    mcp_controller_test.go
    meta_controller.go
    notification_controller.go
    permission_controller.go
    plugin_captcha_controller.go
    plugin_sidebar_controller.go
    plugin_user_center_controller.go
    question_controller.go
    question_controller_test.go
    … 15 more files
  controller_admin/  (9 files)
    ai_conversation_admin_controller.go
    badge_controller.go
    controller.go
    e_api_key_controller.go
    plugin_controller.go
    role_controller.go
    siteinfo_controller.go
    theme_controller.go
    user_backyard_controller.go
  entity/  (37 files)
    activity_entity.go
    ai_conversation.go
    ai_conversation_record.go
    answer_entity.go
    api_key_entity.go
    auth_user_entity.go
    badge_award_entity.go
    badge_entity.go
    badge_group_entity.go
    captcha_entity.go
    collection_entity.go
    collection_group_entity.go
    comment_entity.go
    config_entity.go
    file_record_entity.go
    meta_entity.go
    notification_entity.go
    plugin_config_entity.go
    plugin_kv_storage_entity.go
    plugin_user_config_entity.go
    power_entity.go
    question_entity.go
    question_link_entity.go
    report_entity.go
    … 13 more files
  install/  (5 files)
    install_controller.go
    install_from_env.go
    install_main.go
    install_req.go
    install_server.go
  migrations/  (40 files)
    init.go
    init_data.go
    migrations.go
    v1.go
    v10.go
    v11.go
    v12.go
    v13.go
    v14.go
    v15.go
    v16.go
    v17.go
    v18.go
    v19.go
    v2.go
    v20.go
    v21.go
    v22.go
    v23.go
    v24.go
    v25.go
    v26.go
    v27.go
    v28.go
    … 16 more files
  repo/  (70 files)
    activity/  (6 files)
      … 6 files under this directory
    activity_common/  (3 files)
      … 3 files under this directory
    ai_conversation/  (1 files)
      … 1 files under this directory
    answer/  (1 files)
      … 1 files under this directory
    api_key/  (1 files)
      … 1 files under this directory
    auth/  (1 files)
      … 1 files under this directory
    badge/  (2 files)
      … 2 files under this directory
    badge_award/  (1 files)
      … 1 files under this directory
    badge_group/  (1 files)
      … 1 files under this directory
    captcha/  (1 files)
      … 1 files under this directory
    collection/  (2 files)
      … 2 files under this directory
    comment/  (1 files)
      … 1 files under this directory
    config/  (1 files)
      … 1 files under this directory
    export/  (1 files)
      … 1 files under this directory
    file_record/  (1 files)
      … 1 files under this directory
    limit/  (1 files)
      … 1 files under this directory
    meta/  (1 files)
      … 1 files under this directory
    notification/  (1 files)
      … 1 files under this directory
    plugin_config/  (2 files)
      … 2 files under this directory
    question/  (1 files)
      … 1 files under this directory
    rank/  (1 files)
      … 1 files under this directory
    reason/  (1 files)
      … 1 files under this directory
    repo_test/  (17 files)
      … 17 files under this directory
    report/  (1 files)
      … 1 files under this directory
    review/  (1 files)
      … 1 files under this directory
    revision/  (1 files)
      … 1 files under this directory
    role/  (4 files)
      … 4 files under this directory
    search_common/  (1 files)
      … 1 files under this directory
    search_sync/  (1 files)
      … 1 files under this directory
    site_info/  (1 files)
      … 1 files under this directory
    tag/  (2 files)
      … 2 files under this directory
    tag_common/  (2 files)
      … 2 files under this directory
    unique/  (1 files)
      … 1 files under this directory
    user/  (2 files)
      … 2 files under this directory
    user_external_login/  (1 files)
      … 1 files under this directory
    user_notification_config/  (1 files)
      … 1 files under this directory
    vector_search_sync/  (1 files)
      … 1 files under this directory
    provider.go
  router/  (11 files)
    answer_api_router.go
    config.go
    mcp_router.go
    plugin_api_router.go
    provider.go
    static_router.go
    static_router_test.go
    swagger_router.go
    template_router.go
    ui.go
    ui_test.go
  schema/  (50 files)
    mcp_tools/  (1 files)
      … 1 files under this directory
    activity.go
    ai_config_schema.go
    ai_conversation_schema.go
    answer_activity_schema.go
    answer_schema.go
    api_key_schema.go
    backyard_user_schema.go
    badge_schema.go
    collection_group_schema.go
    comment_schema.go
    config_schema.go
    connector_schema.go
    dashboard_schema.go
    email_template.go
    email_template_test.go
    err_schema.go
    event_schema.go
    follow_schema.go
    forbidden_schema.go
    mcp_schema.go
    meta_schema.go
    new_question_queue_schema.go
    notification_schema.go
    permission.go
    … 25 more files
  service/  (104 files)
    action/  (2 files)
      … 2 files under this directory
    activity/  (4 files)
      … 4 files under this directory
    activity_common/  (3 files)
      … 3 files under this directory
    activity_type/  (1 files)
      … 1 files under this directory
    activityqueue/  (1 files)
      … 1 files under this directory
    ai_conversation/  (1 files)
      … 1 files under this directory
    answer_common/  (1 files)
      … 1 files under this directory
    apikey/  (1 files)
      … 1 files under this directory
    auth/  (3 files)
      … 3 files under this directory
    badge/  (4 files)
      … 4 files under this directory
    collection/  (2 files)
      … 2 files under this directory
    collection_common/  (1 files)
      … 1 files under this directory
    comment/  (2 files)
      … 2 files under this directory
    comment_common/  (1 files)
      … 1 files under this directory
    config/  (1 files)
      … 1 files under this directory
    content/  (10 files)
      … 10 files under this directory
    dashboard/  (2 files)
      … 2 files under this directory
    embedding/  (1 files)
      … 1 files under this directory
    eventqueue/  (1 files)
      … 1 files under this directory
    export/  (1 files)
      … 1 files under this directory
    feature_toggle/  (1 files)
      … 1 files under this directory
    file_record/  (1 files)
      … 1 files under this directory
    follow/  (1 files)
      … 1 files under this directory
    importer/  (2 files)
      … 2 files under this directory
    meta/  (2 files)
      … 2 files under this directory
    meta_common/  (1 files)
      … 1 files under this directory
    mock/  (1 files)
      … 1 files under this directory
    noticequeue/  (1 files)
      … 1 files under this directory
    notification/  (10 files)
      … 10 files under this directory
    notification_common/  (1 files)
      … 1 files under this directory
    object_info/  (1 files)
      … 1 files under this directory
    permission/  (5 files)
      … 5 files under this directory
    plugin_common/  (1 files)
      … 1 files under this directory
    question_common/  (1 files)
      … 1 files under this directory
    rank/  (1 files)
      … 1 files under this directory
    reason/  (1 files)
      … 1 files under this directory
    reason_common/  (1 files)
      … 1 files under this directory
    report/  (1 files)
      … 1 files under this directory
    report_common/  (1 files)
      … 1 files under this directory
    report_handle/  (1 files)
      … 1 files under this directory
    review/  (1 files)
      … 1 files under this directory
    revision/  (1 files)
      … 1 files under this directory
    revision_common/  (1 files)
      … 1 files under this directory
    role/  (4 files)
      … 4 files under this directory
    search_common/  (1 files)
      … 1 files under this directory
    search_parser/  (1 files)
      … 1 files under this directory
    service_config/  (1 files)
      … 1 files under this directory
    siteinfo/  (2 files)
      … 2 files under this directory
    siteinfo_common/  (2 files)
      … 2 files under this directory
    tag/  (1 files)
      … 1 files under this directory
    tag_common/  (1 files)
      … 1 files under this directory
    unique/  (1 files)
      … 1 files under this directory
    uploader/  (1 files)
      … 1 files under this directory
    user_admin/  (1 files)
      … 1 files under this directory
    user_common/  (1 files)
      … 1 files under this directory
    user_external_login/  (3 files)
      … 3 files under this directory
    user_notification_config/  (1 files)
      … 1 files under this directory
    vector_sync/  (1 files)
      … 1 files under this directory
    provider.go
pkg/  (34 files)
  checker/  (13 files)
    chinese.go
    email.go
    email_test.go
    file_type.go
    file_type_test.go
    password.go
    path_ignore.go
    question_link.go
    question_link_test.go
    reserved_username.go
    url.go
    username.go
    zero_string.go
  converter/  (5 files)
    array.go
    markdown.go
    markdown_test.go
    str.go
    user.go
  day/  (2 files)
    day.go
    day_test.go
  dir/  (1 files)
    dir.go
  display/  (2 files)
    url.go
    url_test.go
  encryption/  (1 files)
    md5.go
  gravatar/  (2 files)
    gravatar.go
    gravatar_test.go
  htmltext/  (2 files)
    htmltext.go
    htmltext_test.go
  obj/  (1 files)
    obj.go
  random/  (1 files)
    random_username.go
  token/  (1 files)
    token.go
  uid/  (2 files)
    id.go
    sid.go
  writer/  (1 files)
    writer.go
plugin/  (24 files)
  plugin_test/  (2 files)
    kv_storage_test.go
    plugin_main_test.go
  agent.go
  base.go
  cache.go
  captcha.go
  cdn.go
  config.go
  connector.go
  embed.go
  filter.go
  importer.go
  kv_storage.go
  notification.go
  parser.go
  plugin.go
  render.go
  reviewer.go
  search.go
  sidebar.go
  storage.go
  user_center.go
  user_config.go
  vector_search.go
script/  (5 files)
  build_plugin.sh
  check-asf-header.sh
  entrypoint.sh
  gen-api.sh
  plugin_list
ui/  (122 files)
  public/  (2 files)
    manifest.json
    robots.txt
  scripts/  (5 files)
    env.js
    importPlugins.js
    loadPlugins.js
    preinstall.js
    setup-eslint.js
  src/  (104 files)
    assets/  (1 files)
      … 1 files under this directory
    behaviour/  (1 files)
      … 1 files under this directory
    common/  (6 files)
      … 6 files under this directory
    components/  (95 files)
      … 95 files under this directory
    App.tsx
  .browserslistrc
  .editorconfig
  .eslintignore
  .eslintrc.js
  .gitignore
  .lintstagedrc.json
  .prettierrc.json
  commitlint.config.js
  index.html
  package.json
  pnpm-workspace.yaml
.asf.yaml
.editorconfig
.env.example
.gitignore
.gitlab-ci.yml
.golangci.yaml
.goreleaser.yaml
Dockerfile
LICENSE
Makefile
NOTICE
README.md
crowdin.yml
docker-compose.yaml
go.mod
go.sum
licenserc.toml
```

## Entry points

- [ui/src/App.tsx](https://github.com/apache/answer/blob/6744295fa888e0621fc9f9a8ace04f1a4daf8554/ui/src/App.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cmd package | library | Observed | Groups 5 file(s) under cmd package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 71 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 1 file(s) under i18n package (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 328 file(s) under internal package (observed from repository paths and static analysis). |
| pkg package | library | Observed | Groups 34 file(s) under pkg package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 24 file(s) under plugin package (observed from repository paths and static analysis). |
| script package | library | Observed | Groups 4 file(s) under script package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 103 file(s) under service / domain layer (observed from repository paths and static analysis). |
| ui package | library | Observed | Groups 93 file(s) under ui package (observed from repository paths and static analysis). |

## Important files

- `.asf.yaml` (config)
- `.editorconfig` (config)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/build-binary-for-release.yml` (ci)
- `.github/workflows/build-image-for-latest-release.yml` (ci)
- `.github/workflows/build-image-for-manual.yml` (ci)
- `.github/workflows/build-image-for-release.yml` (ci)
- `.github/workflows/build-image-for-test.yml` (ci)
- `.github/workflows/check-asf-header.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.gitlab-ci.yml` (ci)
- `.golangci.yaml` (config)
- `.goreleaser.yaml` (config)
- `.vaunt/config.yaml` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `charts/Chart.yaml` (config)
- `charts/templates/deployment.yaml` (config)
- `charts/templates/hpa.yaml` (config)
- `charts/templates/ingress.yaml` (config)
- `charts/templates/pvc.yaml` (config)
- `charts/templates/service.yaml` (config)
- `charts/templates/serviceaccount.yaml` (config)
- `charts/values.yaml` (config)
- `configs/config.yaml` (config)
- `configs/path_ignore.yaml` (config)
- `configs/reserved-usernames.json` (config)
- `crowdin.yml` (config)
- `docker-compose.yaml` (container)
- `go.mod` (manifest)
- `i18n/af_ZA.yaml` (config)
- `i18n/ar_SA.yaml` (config)
- `i18n/az_AZ.yaml` (config)
- `i18n/bal_BA.yaml` (config)
- `i18n/ban_ID.yaml` (config)
- `i18n/bn_BD.yaml` (config)
- `i18n/bs_BA.yaml` (config)
- `i18n/ca_ES.yaml` (config)
- `i18n/cs_CZ.yaml` (config)
- `i18n/cy_GB.yaml` (config)
- `i18n/da_DK.yaml` (config)
- `i18n/de_DE.yaml` (config)
- `i18n/el_GR.yaml` (config)
- `i18n/en_US.yaml` (config)
- `i18n/es_ES.yaml` (config)
- `i18n/fa_IR.yaml` (config)
- `i18n/fi_FI.yaml` (config)
- `i18n/fr_FR.yaml` (config)
- `i18n/he_IL.yaml` (config)
- `i18n/hi_IN.yaml` (config)
- `i18n/hu_HU.yaml` (config)
- `i18n/hy_AM.yaml` (config)
- `i18n/i18n.yaml` (config)
- `i18n/id_ID.yaml` (config)
- `i18n/it_IT.yaml` (config)
- `i18n/ja_JP.yaml` (config)
- `i18n/ko_KR.yaml` (config)
- `i18n/ml_IN.yaml` (config)
- `i18n/nl_NL.yaml` (config)
- `i18n/no_NO.yaml` (config)
- `i18n/pl_PL.yaml` (config)
- `i18n/pt_BR.yaml` (config)
- `i18n/pt_PT.yaml` (config)
- `i18n/ro_RO.yaml` (config)
- `i18n/ru_RU.yaml` (config)
- `i18n/sk_SK.yaml` (config)
- `i18n/sq_AL.yaml` (config)
- `i18n/sr_SP.yaml` (config)
- `i18n/sv_SE.yaml` (config)
- `i18n/te_IN.yaml` (config)
- `i18n/tr_TR.yaml` (config)
- `i18n/uk_UA.yaml` (config)
- `i18n/vi_VN.yaml` (config)
- `i18n/zh_CN.yaml` (config)
- `i18n/zh_TW.yaml` (config)
- `licenserc.toml` (config)
- `ui/.editorconfig` (config)
- `ui/.lintstagedrc.json` (config)
- `ui/.prettierrc.json` (config)
- `ui/package.json` (manifest)
- `ui/pnpm-workspace.yaml` (config)
- `ui/public/manifest.json` (config)

## Top-level layout

- `internal` — 436 analysed file(s)
- `ui` — 122 analysed file(s)
- `docs` — 78 analysed file(s)
- `i18n` — 46 analysed file(s)
- `pkg` — 34 analysed file(s)
- `plugin` — 24 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 12 analysed file(s)
- `charts` — 11 analysed file(s)
- `cmd` — 5 analysed file(s)
- `script` — 5 analysed file(s)
- `configs` — 4 analysed file(s)
- `.vaunt` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (3 x likely secret file excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6744295fa888e0621fc9f9a8ace04f1a4daf8554` is the revision these paths and observations refer to.
