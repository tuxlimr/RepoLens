# Project structure: firebase/functions-samples

**Analysed commit:** `5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32`

**Commit reference:** [5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32](https://github.com/firebase/functions-samples/commit/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32)

**Tree at this commit:** [firebase/functions-samples@5c5ef9a5ad4f](https://github.com/firebase/functions-samples/tree/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | firebase/functions-samples |
| Description | Collection of sample apps showcasing popular use cases using Cloud Functions for Firebase |
| Stars | 12212 |
| Forks | 3814 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32` |
| Retrieved at | 2026-11-14T19:12:08.215126+00:00 |
| Files in this snapshot | 540 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    docs.md
  workflows/  (6 files)
    stale.yml
    targeted-dependency-update.yml
    test_dart.yml
    test_node.yml
    test_node_1st_gen.yml
    test_python.yml
.opensource/  (1 files)
  project.json
Dart/  (38 files)
  codelab-dart-functions/  (19 files)
    functions/  (4 files)
      … 4 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    packages/  (8 files)
      … 8 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    analysis_options.yaml
    firebase.json
    pubspec.yaml
  quickstarts/  (19 files)
    callable-functions/  (5 files)
      … 5 files under this directory
    callable-functions-streaming/  (5 files)
      … 5 files under this directory
    https-time-server/  (5 files)
      … 5 files under this directory
    resize-image/  (4 files)
      … 4 files under this directory
Node/  (144 files)
  alerts-to-discord/  (6 files)
    functions/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    firebase.json
  app-distribution-feedback-to-jira/  (7 files)
    functions/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    firebase.json
  call-vertex-remote-config-server/  (11 files)
    client/  (7 files)
      … 7 files under this directory
    functions/  (2 files)
      … 2 files under this directory
    README.md
    firebase.json
  delete-unused-accounts-cron/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  fcm-notifications/  (12 files)
    functions/  (4 files)
      … 4 files under this directory
    public/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    database.rules.json
    firebase.json
  instrument-with-opentelemetry/  (7 files)
    functions/  (5 files)
      … 5 files under this directory
    README.md
    firebase.json
  quickstarts/  (91 files)
    auth-blocking-functions/  (7 files)
      … 7 files under this directory
    callable-functions/  (8 files)
      … 8 files under this directory
    callable-functions-streaming/  (8 files)
      … 8 files under this directory
    custom-events/  (5 files)
      … 5 files under this directory
    email-users/  (10 files)
      … 10 files under this directory
    firestore-sync-auth/  (9 files)
      … 9 files under this directory
    genkit-helloworld/  (7 files)
      … 7 files under this directory
    https-time-server/  (5 files)
      … 5 files under this directory
    monitor-cloud-logging/  (5 files)
      … 5 files under this directory
    pubsub-helloworld/  (7 files)
      … 7 files under this directory
    testlab-matrix-completed/  (5 files)
      … 5 files under this directory
    thumbnails/  (5 files)
      … 5 files under this directory
    uppercase-firestore/  (7 files)
      … 7 files under this directory
    uppercase-rtdb/  (3 files)
      … 3 files under this directory
  remote-config-diff/  (1 files)
    README.md
  test-functions-jest/  (1 files)
    functions/  (1 files)
      … 1 files under this directory
  test-functions-jest-ts/  (1 files)
    functions/  (1 files)
      … 1 files under this directory
  README.md
  pnpm-workspace.yaml
Node-1st-gen/  (345 files)
  authenticated-json-api/  (9 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (3 files)
      … 3 files under this directory
    README.md
    database.rules.json
    firebase.json
  authorized-https-endpoint/  (8 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  bigquery-import/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  child-count/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  convert-images/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  coupon-on-purchase/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  delete-old-child-nodes/  (4 files)
    functions/  (2 files)
      … 2 files under this directory
    README.md
    firebase.json
  delete-unused-accounts-cron/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  developer-motivator/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  email-confirmation/  (9 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (3 files)
      … 3 files under this directory
    README.md
    database.rules.json
    firebase.json
  exif-images/  (9 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (3 files)
      … 3 files under this directory
    README.md
    database.rules.json
    firebase.json
  fcm-notifications/  (10 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (4 files)
      … 4 files under this directory
    README.md
    database.rules.json
    firebase.json
  ffmpeg-convert-audio/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  fulltext-search/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  fulltext-search-firestore/  (10 files)
    functions/  (6 files)
      … 6 files under this directory
    public/  (2 files)
      … 2 files under this directory
    README.md
    firebase.json
  github-to-slack/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  google-sheet-sync/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  image-maker/  (10 files)
    functions/  (6 files)
      … 6 files under this directory
    public/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    firebase.json
  lastmodified-tracking/  (6 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    database.rules.json
    firebase.json
  limit-children/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  linkedin-auth/  (12 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    database.rules.json
    firebase.json
    main.css
  message-translation/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  minimal-webhook/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  moderate-images/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  okta-auth/  (8 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    firebase.json
    setup.js
  presence-firestore/  (7 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (2 files)
      … 2 files under this directory
    README.md
    firebase.json
  publish-model/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  quickstarts/  (83 files)
    auth-blocking-functions/  (7 files)
      … 7 files under this directory
    big-ben/  (7 files)
      … 7 files under this directory
    email-users/  (8 files)
      … 8 files under this directory
    https-time-server/  (5 files)
      … 5 files under this directory
    multicodebase-hellos/  (13 files)
      … 13 files under this directory
    pubsub-helloworld/  (5 files)
      … 5 files under this directory
    runtime-options/  (6 files)
      … 6 files under this directory
    taskqueues-backup-images/  (5 files)
      … 5 files under this directory
    testlab-matrix-completed/  (6 files)
      … 6 files under this directory
    thumbnails/  (5 files)
      … 5 files under this directory
    uppercase-firestore/  (9 files)
      … 9 files under this directory
    uppercase-rtdb/  (7 files)
      … 7 files under this directory
  remote-config-diff/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  spotify-auth/  (11 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (4 files)
      … 4 files under this directory
    README.md
    database.rules.json
    firebase.json
    main.css
  stripe/  (8 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (2 files)
      … 2 files under this directory
    README.md
    firebase.json
    firestore.rules
  survey-app-update/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  template-handlebars/  (9 files)
    functions/  (6 files)
      … 6 files under this directory
    public/  (1 files)
      … 1 files under this directory
    README.md
    firebase.json
  testlab-to-slack/  (6 files)
    functions/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    firebase.json
  text-moderation/  (9 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
    security.rules.json
  url-shortener/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  user-data-cleanup/  (3 files)
    doc/  (2 files)
      … 2 files under this directory
    README.md
  username-password-auth/  (9 files)
    functions/  (3 files)
      … 3 files under this directory
    public/  (3 files)
      … 3 files under this directory
    README.md
    database.rules.json
    firebase.json
  vision-annotate-images/  (8 files)
    functions/  (6 files)
      … 6 files under this directory
    README.md
    firebase.json
  youtube/  (5 files)
    functions/  (3 files)
      … 3 files under this directory
    README.md
    firebase.json
  README.md
  pnpm-workspace.yaml
.gitignore
CONTRIBUTING.md
LICENSE
```

## Entry points

- [Node-1st-gen/quickstarts/auth-blocking-functions/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node-1st-gen/quickstarts/auth-blocking-functions/functions/index.js)
- [Node-1st-gen/quickstarts/multicodebase-hellos/js/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node-1st-gen/quickstarts/multicodebase-hellos/js/index.js)
- [Node-1st-gen/quickstarts/runtime-options/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node-1st-gen/quickstarts/runtime-options/functions/index.js)
- [Node-1st-gen/quickstarts/taskqueues-backup-images/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node-1st-gen/quickstarts/taskqueues-backup-images/functions/index.js)
- [Node-1st-gen/youtube/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node-1st-gen/youtube/functions/index.js)
- [Node/alerts-to-discord/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node/alerts-to-discord/functions/index.js)
- [Node/app-distribution-feedback-to-jira/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node/app-distribution-feedback-to-jira/functions/index.js)
- [Node/call-vertex-remote-config-server/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node/call-vertex-remote-config-server/functions/index.js)
- [Node/fcm-notifications/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node/fcm-notifications/functions/index.js)
- [Node/quickstarts/auth-blocking-functions/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node/quickstarts/auth-blocking-functions/functions/index.js)
- [Node/quickstarts/callable-functions-streaming/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node/quickstarts/callable-functions-streaming/functions/index.js)
- [Node/quickstarts/callable-functions/functions/index.js](https://github.com/firebase/functions-samples/blob/5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32/Node/quickstarts/callable-functions/functions/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 178 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 4 file(s) under external integrations (observed from repository paths and static analysis). |
| Node package | library | Observed | Groups 46 file(s) under node package (observed from repository paths and static analysis). |
| Node-1st-gen package | library | Observed | Groups 121 file(s) under node-1st-gen package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/targeted-dependency-update.yml` (ci)
- `.github/workflows/test_dart.yml` (ci)
- `.github/workflows/test_node.yml` (ci)
- `.github/workflows/test_node_1st_gen.yml` (ci)
- `.github/workflows/test_python.yml` (ci)
- `.opensource/project.json` (config)
- `Dart/codelab-dart-functions/analysis_options.yaml` (config)
- `Dart/codelab-dart-functions/firebase.json` (config)
- `Dart/codelab-dart-functions/functions/analysis_options.yaml` (config)
- `Dart/codelab-dart-functions/functions/build.yaml` (config)
- `Dart/codelab-dart-functions/functions/pubspec.yaml` (config)
- `Dart/codelab-dart-functions/packages/shared/analysis_options.yaml` (config)
- `Dart/codelab-dart-functions/packages/shared/pubspec.yaml` (config)
- `Dart/codelab-dart-functions/pubspec.yaml` (config)
- `Dart/quickstarts/callable-functions-streaming/firebase.json` (config)
- `Dart/quickstarts/callable-functions-streaming/pubspec.yaml` (config)
- `Dart/quickstarts/callable-functions/firebase.json` (config)
- `Dart/quickstarts/callable-functions/pubspec.yaml` (config)
- `Dart/quickstarts/https-time-server/firebase.json` (config)
- `Dart/quickstarts/https-time-server/pubspec.yaml` (config)
- `Dart/quickstarts/resize-image/firebase.json` (config)
- `Dart/quickstarts/resize-image/pubspec.yaml` (config)
- `Node-1st-gen/authenticated-json-api/database.rules.json` (config)
- `Node-1st-gen/authenticated-json-api/firebase.json` (config)
- `Node-1st-gen/authenticated-json-api/functions/package.json` (manifest)
- `Node-1st-gen/authorized-https-endpoint/firebase.json` (config)
- `Node-1st-gen/authorized-https-endpoint/functions/package.json` (manifest)
- `Node-1st-gen/bigquery-import/firebase.json` (config)
- `Node-1st-gen/bigquery-import/functions/package.json` (manifest)
- `Node-1st-gen/child-count/firebase.json` (config)
- `Node-1st-gen/child-count/functions/package.json` (manifest)
- `Node-1st-gen/convert-images/firebase.json` (config)
- `Node-1st-gen/convert-images/functions/package.json` (manifest)
- `Node-1st-gen/coupon-on-purchase/firebase.json` (config)
- `Node-1st-gen/coupon-on-purchase/functions/package.json` (manifest)
- `Node-1st-gen/delete-old-child-nodes/firebase.json` (config)
- `Node-1st-gen/delete-old-child-nodes/functions/package.json` (manifest)
- `Node-1st-gen/delete-unused-accounts-cron/firebase.json` (config)
- `Node-1st-gen/delete-unused-accounts-cron/functions/package.json` (manifest)
- `Node-1st-gen/developer-motivator/firebase.json` (config)
- `Node-1st-gen/developer-motivator/functions/package.json` (manifest)
- `Node-1st-gen/email-confirmation/database.rules.json` (config)
- `Node-1st-gen/email-confirmation/firebase.json` (config)
- `Node-1st-gen/email-confirmation/functions/package.json` (manifest)
- `Node-1st-gen/exif-images/database.rules.json` (config)
- `Node-1st-gen/exif-images/firebase.json` (config)
- `Node-1st-gen/exif-images/functions/package.json` (manifest)
- `Node-1st-gen/fcm-notifications/database.rules.json` (config)
- `Node-1st-gen/fcm-notifications/firebase.json` (config)
- `Node-1st-gen/fcm-notifications/functions/package.json` (manifest)
- `Node-1st-gen/ffmpeg-convert-audio/firebase.json` (config)
- `Node-1st-gen/ffmpeg-convert-audio/functions/package.json` (manifest)
- `Node-1st-gen/fulltext-search-firestore/firebase.json` (config)
- `Node-1st-gen/fulltext-search-firestore/functions/package.json` (manifest)
- `Node-1st-gen/fulltext-search/firebase.json` (config)
- `Node-1st-gen/fulltext-search/functions/package.json` (manifest)
- `Node-1st-gen/github-to-slack/firebase.json` (config)
- `Node-1st-gen/github-to-slack/functions/package.json` (manifest)
- `Node-1st-gen/google-sheet-sync/firebase.json` (config)
- `Node-1st-gen/google-sheet-sync/functions/package.json` (manifest)
- `Node-1st-gen/image-maker/firebase.json` (config)
- `Node-1st-gen/image-maker/functions/package.json` (manifest)
- `Node-1st-gen/lastmodified-tracking/database.rules.json` (config)
- `Node-1st-gen/lastmodified-tracking/firebase.json` (config)
- `Node-1st-gen/lastmodified-tracking/functions/package.json` (manifest)
- `Node-1st-gen/limit-children/firebase.json` (config)
- `Node-1st-gen/limit-children/functions/package.json` (manifest)
- `Node-1st-gen/linkedin-auth/database.rules.json` (config)
- `Node-1st-gen/linkedin-auth/firebase.json` (config)
- `Node-1st-gen/linkedin-auth/functions/package.json` (manifest)
- `Node-1st-gen/message-translation/firebase.json` (config)
- `Node-1st-gen/message-translation/functions/package.json` (manifest)
- `Node-1st-gen/minimal-webhook/firebase.json` (config)
- `Node-1st-gen/minimal-webhook/functions/package.json` (manifest)
- `Node-1st-gen/moderate-images/firebase.json` (config)
- `Node-1st-gen/moderate-images/functions/package.json` (manifest)
- `Node-1st-gen/okta-auth/firebase.json` (config)
- `Node-1st-gen/okta-auth/functions/package.json` (manifest)
- `Node-1st-gen/pnpm-workspace.yaml` (config)
- `Node-1st-gen/presence-firestore/firebase.json` (config)
- `Node-1st-gen/presence-firestore/functions/package.json` (manifest)
- `Node-1st-gen/publish-model/firebase.json` (config)
- `Node-1st-gen/publish-model/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/auth-blocking-functions/firebase.json` (config)
- `Node-1st-gen/quickstarts/auth-blocking-functions/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/big-ben/firebase.json` (config)
- `Node-1st-gen/quickstarts/big-ben/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/email-users/firebase.json` (config)
- `Node-1st-gen/quickstarts/email-users/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/https-time-server/firebase.json` (config)
- `Node-1st-gen/quickstarts/https-time-server/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/multicodebase-hellos/firebase.json` (config)
- `Node-1st-gen/quickstarts/multicodebase-hellos/js/package.json` (manifest)
- `Node-1st-gen/quickstarts/multicodebase-hellos/ts/package.json` (manifest)
- `Node-1st-gen/quickstarts/multicodebase-hellos/ts/tsconfig.dev.json` (config)
- `Node-1st-gen/quickstarts/multicodebase-hellos/ts/tsconfig.json` (config)
- `Node-1st-gen/quickstarts/pubsub-helloworld/firebase.json` (config)
- `Node-1st-gen/quickstarts/pubsub-helloworld/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/runtime-options/firebase.json` (config)
- `Node-1st-gen/quickstarts/runtime-options/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/taskqueues-backup-images/firebase.json` (config)
- `Node-1st-gen/quickstarts/taskqueues-backup-images/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/testlab-matrix-completed/firebase.json` (config)
- `Node-1st-gen/quickstarts/testlab-matrix-completed/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/thumbnails/firebase.json` (config)
- `Node-1st-gen/quickstarts/thumbnails/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/uppercase-firestore/firebase.json` (config)
- `Node-1st-gen/quickstarts/uppercase-firestore/firestore.indexes.json` (config)
- `Node-1st-gen/quickstarts/uppercase-firestore/functions/package.json` (manifest)
- `Node-1st-gen/quickstarts/uppercase-rtdb/database.rules.json` (config)
- `Node-1st-gen/quickstarts/uppercase-rtdb/firebase.json` (config)
- `Node-1st-gen/quickstarts/uppercase-rtdb/functions/package.json` (manifest)
- `Node-1st-gen/remote-config-diff/firebase.json` (config)
- `Node-1st-gen/remote-config-diff/functions/package.json` (manifest)
- `Node-1st-gen/spotify-auth/database.rules.json` (config)
- `Node-1st-gen/spotify-auth/firebase.json` (config)
- `Node-1st-gen/spotify-auth/functions/package.json` (manifest)
- `Node-1st-gen/stripe/firebase.json` (config)
- `Node-1st-gen/stripe/functions/package.json` (manifest)
- `Node-1st-gen/survey-app-update/firebase.json` (config)
- `Node-1st-gen/survey-app-update/functions/package.json` (manifest)
- `Node-1st-gen/template-handlebars/firebase.json` (config)
- `Node-1st-gen/template-handlebars/functions/package.json` (manifest)
- `Node-1st-gen/testlab-to-slack/firebase.json` (config)
- `Node-1st-gen/testlab-to-slack/functions/package.json` (manifest)
- `Node-1st-gen/text-moderation/firebase.json` (config)
- `Node-1st-gen/text-moderation/functions/package.json` (manifest)
- `Node-1st-gen/text-moderation/security.rules.json` (config)
- `Node-1st-gen/url-shortener/firebase.json` (config)
- `Node-1st-gen/url-shortener/functions/package.json` (manifest)
- `Node-1st-gen/username-password-auth/database.rules.json` (config)
- `Node-1st-gen/username-password-auth/firebase.json` (config)
- `Node-1st-gen/username-password-auth/functions/package.json` (manifest)
- `Node-1st-gen/vision-annotate-images/firebase.json` (config)
- `Node-1st-gen/vision-annotate-images/functions/package.json` (manifest)
- `Node-1st-gen/vision-annotate-images/functions/tsconfig.json` (config)
- `Node-1st-gen/youtube/firebase.json` (config)
- `Node-1st-gen/youtube/functions/package.json` (manifest)
- `Node/alerts-to-discord/firebase.json` (config)
- `Node/alerts-to-discord/functions/package.json` (manifest)
- `Node/app-distribution-feedback-to-jira/firebase.json` (config)
- `Node/app-distribution-feedback-to-jira/functions/package.json` (manifest)
- `Node/call-vertex-remote-config-server/client/package.json` (manifest)
- `Node/call-vertex-remote-config-server/firebase.json` (config)
- `Node/call-vertex-remote-config-server/functions/package.json` (manifest)
- `Node/delete-unused-accounts-cron/firebase.json` (config)
- `Node/delete-unused-accounts-cron/functions/package.json` (manifest)
- `Node/fcm-notifications/database.rules.json` (config)
- `Node/fcm-notifications/firebase.json` (config)
- `Node/fcm-notifications/functions/package.json` (manifest)
- `Node/instrument-with-opentelemetry/firebase.json` (config)
- `Node/instrument-with-opentelemetry/functions/package.json` (manifest)
- `Node/pnpm-workspace.yaml` (config)
- `Node/quickstarts/auth-blocking-functions/firebase.json` (config)
- `Node/quickstarts/auth-blocking-functions/functions/package.json` (manifest)
- `Node/quickstarts/callable-functions-streaming/firebase.json` (config)
- `Node/quickstarts/callable-functions-streaming/functions/package.json` (manifest)
- `Node/quickstarts/callable-functions/firebase.json` (config)
- `Node/quickstarts/callable-functions/functions/package.json` (manifest)
- `Node/quickstarts/custom-events/firebase.json` (config)
- `Node/quickstarts/custom-events/functions/package.json` (manifest)
- `Node/quickstarts/email-users/firebase.json` (config)
- `Node/quickstarts/email-users/functions/package.json` (manifest)
- `Node/quickstarts/firestore-sync-auth/firebase.json` (config)
- `Node/quickstarts/firestore-sync-auth/firestore.indexes.json` (config)
- `Node/quickstarts/firestore-sync-auth/functions/package.json` (manifest)
- `Node/quickstarts/genkit-helloworld/firebase.json` (config)
- `Node/quickstarts/genkit-helloworld/functions/package.json` (manifest)
- `Node/quickstarts/https-time-server/firebase.json` (config)
- `Node/quickstarts/https-time-server/functions/package.json` (manifest)
- `Node/quickstarts/monitor-cloud-logging/firebase.json` (config)
- `Node/quickstarts/monitor-cloud-logging/functions/package.json` (manifest)
- `Node/quickstarts/pubsub-helloworld/firebase.json` (config)
- `Node/quickstarts/pubsub-helloworld/functions/package.json` (manifest)
- `Node/quickstarts/testlab-matrix-completed/firebase.json` (config)
- `Node/quickstarts/testlab-matrix-completed/functions/package.json` (manifest)
- `Node/quickstarts/thumbnails/firebase.json` (config)
- `Node/quickstarts/thumbnails/functions/package.json` (manifest)
- `Node/quickstarts/uppercase-firestore/firebase.json` (config)
- `Node/quickstarts/uppercase-firestore/firestore.indexes.json` (config)
- `Node/quickstarts/uppercase-firestore/functions/package.json` (manifest)
- `Node/quickstarts/uppercase-rtdb/database.rules.json` (config)
- `Node/quickstarts/uppercase-rtdb/firebase.json` (config)
- `Node/test-functions-jest-ts/functions/tsconfig.dev.json` (config)

## Top-level layout

- `Node-1st-gen` — 345 analysed file(s)
- `Node` — 144 analysed file(s)
- `Dart` — 38 analysed file(s)
- `.github` — 9 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.opensource` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 68 file(s) were skipped during inventory (2 x likely secret file excluded; 66 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5c5ef9a5ad4faa16215c7a406d1afe3f8c3b9c32` is the revision these paths and observations refer to.
