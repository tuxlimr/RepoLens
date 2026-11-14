# Project structure: serverless/examples

**Analysed commit:** `424fe6f7737bd45aeea4e5b40d7beda3422ffa54`

**Commit reference:** [424fe6f7737bd45aeea4e5b40d7beda3422ffa54](https://github.com/serverless/examples/commit/424fe6f7737bd45aeea4e5b40d7beda3422ffa54)

**Tree at this commit:** [serverless/examples@424fe6f7737b](https://github.com/serverless/examples/tree/424fe6f7737bd45aeea4e5b40d7beda3422ffa54)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | serverless/examples |
| Description | Serverless Examples – A collection of boilerplates and examples of serverless architectures built with the Serverless Framework on AWS Lambda, Microsoft Azure, Google Cloud Functions, and more. |
| Stars | 11517 |
| Forks | 4347 |
| Licence | Other |
| Language | JavaScript |
| Default branch | v4 |
| Analysed commit | `424fe6f7737bd45aeea4e5b40d7beda3422ffa54` |
| Retrieved at | 2026-11-14T19:12:17.045411+00:00 |
| Files in this snapshot | 760 |

## Directory tree

```text
.github/  (1 files)
  pull_request_template.md
aws-bedrock-agentcore/  (154 files)
  javascript/  (79 files)
    langgraph-basic/  (5 files)
      … 5 files under this directory
    langgraph-basic-dockerfile/  (6 files)
      … 6 files under this directory
    langgraph-browser/  (5 files)
      … 5 files under this directory
    langgraph-browser-custom/  (5 files)
      … 5 files under this directory
    langgraph-code-interpreter/  (5 files)
      … 5 files under this directory
    langgraph-code-interpreter-custom/  (5 files)
      … 5 files under this directory
    langgraph-comprehensive/  (6 files)
      … 6 files under this directory
    langgraph-gateway/  (6 files)
      … 6 files under this directory
    langgraph-memory/  (5 files)
      … 5 files under this directory
    langgraph-multi-gateway/  (10 files)
      … 10 files under this directory
    langgraph-streaming/  (5 files)
      … 5 files under this directory
    mcp-server/  (6 files)
      … 6 files under this directory
    mcp-server-lambda-tools/  (5 files)
      … 5 files under this directory
    strands-browser/  (5 files)
      … 5 files under this directory
  python/  (74 files)
    langgraph-basic-code/  (6 files)
      … 6 files under this directory
    langgraph-basic-docker/  (7 files)
      … 7 files under this directory
    langgraph-browser/  (7 files)
      … 7 files under this directory
    langgraph-browser-custom/  (7 files)
      … 7 files under this directory
    langgraph-code-interpreter/  (7 files)
      … 7 files under this directory
    langgraph-code-interpreter-custom/  (7 files)
      … 7 files under this directory
    langgraph-gateway/  (8 files)
      … 8 files under this directory
    langgraph-memory/  (7 files)
      … 7 files under this directory
    langgraph-multi-gateway/  (11 files)
      … 11 files under this directory
    strands-browser/  (7 files)
      … 7 files under this directory
  README.md
aws-dev-mode/  (6 files)
  src/  (1 files)
    api.ts
  worker/  (1 files)
    handler.py
  .gitignore
  README.md
  package.json
  serverless.yml
aws-dotnet-rest-api-with-dynamodb/  (33 files)
  src/  (26 files)
    DotNetServerless.Application/  (14 files)
      … 14 files under this directory
    DotNetServerless.Lambda/  (12 files)
      … 12 files under this directory
  tests/  (4 files)
    DotNetServerless.Tests/  (4 files)
      … 4 files under this directory
  .gitignore
  DotNetServerless.sln
  README.md
aws-ffmpeg-layer/  (6 files)
  .gitignore
  README.md
  build.sh
  handler.js
  package.json
  serverless.yml
aws-golang-auth-examples/  (19 files)
  functions/  (12 files)
    auth/  (3 files)
      … 3 files under this directory
    auth2/  (3 files)
      … 3 files under this directory
    hello-world/  (3 files)
      … 3 files under this directory
    hello-world2/  (3 files)
      … 3 files under this directory
  .gitignore
  Makefile
  README.md
  go.mod
  go.sum
  package.json
  serverless.yml
aws-golang-googlemap/  (11 files)
  geomap/  (1 files)
    geomap.go
  getgeodetail/  (1 files)
    main.go
  getgeolocation/  (1 files)
    main.go
  getnearbylocation/  (1 files)
    main.go
  getsearchlocation/  (1 files)
    main.go
  .gitignore
  Makefile
  README.md
  go.mod
  go.sum
  serverless.yml
aws-golang-http-get-post/  (10 files)
  get/  (1 files)
    main.go
  getquery/  (1 files)
    main.go
  post/  (1 files)
    main.go
  .gitignore
  Makefile
  README.md
  go.mod
  go.sum
  package.json
  serverless.yml
aws-golang-rest-api-with-dynamodb/  (12 files)
  todos/  (5 files)
    create/  (1 files)
      … 1 files under this directory
    delete/  (1 files)
      … 1 files under this directory
    get/  (1 files)
      … 1 files under this directory
    list/  (1 files)
      … 1 files under this directory
    update/  (1 files)
      … 1 files under this directory
  .gitignore
  Makefile
  README.md
  go.mod
  go.sum
  package.json
  serverless.yml
aws-golang-s3-file-replicator/  (7 files)
  src/  (1 files)
    main.go
  .gitignore
  Makefile
  README.md
  go.mod
  go.sum
  serverless.yml
aws-golang-simple-http-endpoint/  (9 files)
  hello/  (1 files)
    main.go
  world/  (1 files)
    main.go
  .gitignore
  Makefile
  README.md
  go.mod
  go.sum
  package.json
  serverless.yml
aws-java-simple-http-endpoint/  (11 files)
  gradle/  (1 files)
    wrapper/  (1 files)
      … 1 files under this directory
  src/  (3 files)
    main/  (3 files)
      … 3 files under this directory
  .gitignore
  README.md
  build.gradle
  gradlew
  gradlew.bat
  pom.xml
  serverless.yml
aws-multiple-runtime/  (6 files)
  api/  (2 files)
    .gitignore
    handler.js
  web/  (1 files)
    handler.py
  README.md
  package.json
  serverless.yml
aws-node/  (4 files)
  .gitignore
  README.md
  handler.js
  serverless.yml
aws-node-alexa-skill/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-auth0-cognito-custom-authorizers-api/  (6 files)
  .gitignore
  README.md
  auth.js
  handler.js
  package.json
  serverless.yml
aws-node-auth0-custom-authorizers-api/  (9 files)
  frontend/  (3 files)
    app.css
    app.js
    index.html
  .gitignore
  README.md
  handler.js
  package.json
  public_key-example
  serverless.yml
aws-node-container-snapstart/  (4 files)
  Dockerfile
  README.md
  handler.mjs
  serverless.yml
aws-node-durable-function/  (4 files)
  README.md
  handler.mjs
  package.json
  serverless.yml
aws-node-dynamic-image-resizer/  (7 files)
  src/  (4 files)
    handlers/  (3 files)
      … 3 files under this directory
    lib/  (1 files)
      … 1 files under this directory
  README.md
  package.json
  serverless.yml
aws-node-dynamodb-stream-processing/  (4 files)
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-env-variables/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-env-variables-encrypted-in-a-file/  (9 files)
  scripts/  (2 files)
    decrypt.mjs
    encrypt.mjs
  .gitignore
  README.md
  handler.js
  package.json
  secrets.dev.yml.encrypted
  secrets.prod.yml.encrypted
  serverless.yml
aws-node-esm-esbuild/  (3 files)
  src/  (1 files)
    handler.ts
  README.md
  serverless.yml
aws-node-express-api/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-express-dynamodb-api/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-express-web-app/  (4 files)
  src/  (1 files)
    server.js
  README.md
  package.json
  serverless.yml
aws-node-fetch-file-and-store-in-s3/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-github-check/  (8 files)
  libs/  (2 files)
    github-service.js
    response-lib.js
  .babelrc
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yaml
aws-node-github-webhook-listener/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-graphql-api-with-dynamodb/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-http-api/  (4 files)
  .gitignore
  README.md
  handler.js
  serverless.yml
aws-node-http-api-dynamodb/  (9 files)
  todos/  (5 files)
    create.js
    delete.js
    get.js
    list.js
    update.js
  .gitignore
  README.md
  package.json
  serverless.yml
aws-node-http-api-dynamodb-local/  (13 files)
  dynamodb/  (2 files)
    Dockerfile
    docker-compose.yml
  offline/  (1 files)
    migrations/  (1 files)
      … 1 files under this directory
  todos/  (6 files)
    create.js
    delete.js
    dynamodb.js
    get.js
    list.js
    update.js
  .gitignore
  README.md
  package.json
  serverless.yml
aws-node-http-api-mongodb/  (6 files)
  model/  (1 files)
    User.js
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-http-api-typescript/  (6 files)
  .gitignore
  README.md
  handler.ts
  package.json
  serverless.yml
  tsconfig.json
aws-node-http-api-typescript-dynamodb/  (9 files)
  todos/  (4 files)
    create.ts
    get.ts
    list.ts
    update.ts
  .gitignore
  README.md
  package.json
  serverless.yml
  tsconfig.json
aws-node-iot-event/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-mongodb-atlas/  (6 files)
  .gitignore
  README.md
  handler.js
  index.js
  package.json
  serverless.yml
aws-node-nextjs-web-app/  (10 files)
  app/  (4 files)
    api/  (1 files)
      … 1 files under this directory
    layout.js
    page.js
    page.module.css
  public/  (1 files)
    lambda.svg
  .gitignore
  README.md
  next.config.mjs
  package.json
  serverless.yml
aws-node-puppeteer/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-recursive-function/  (6 files)
  .gitignore
  README.md
  event.json
  handler.js
  package.json
  serverless.yml
aws-node-rekognition-analysis-s3-image/  (7 files)
  lib/  (1 files)
    imageAnalyser.js
  .gitignore
  README.md
  handler.js
  package.json
  post.json
  serverless.yml
aws-node-rest-api/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-rest-api-mongodb/  (6 files)
  model/  (1 files)
    User.js
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-rest-api-typescript/  (18 files)
  app/  (9 files)
    controller/  (1 files)
      … 1 files under this directory
    model/  (5 files)
      … 5 files under this directory
    service/  (1 files)
      … 1 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    handler.ts
  tests/  (2 files)
    books.mock.ts
    books.test.ts
  .editorconfig
  .gitignore
  .nycrc.json
  README.md
  package.json
  serverless.yml
  tsconfig.json
aws-node-rest-api-typescript-simple/  (6 files)
  .gitignore
  README.md
  handler.ts
  package.json
  serverless.yml
  tsconfig.json
aws-node-rest-api-with-dynamodb/  (9 files)
  todos/  (5 files)
    create.js
    delete.js
    get.js
    list.js
    update.js
  .gitignore
  README.md
  package.json
  serverless.yml
aws-node-rest-api-with-dynamodb-and-offline/  (13 files)
  dynamodb/  (2 files)
    Dockerfile
    docker-compose.yml
  offline/  (1 files)
    migrations/  (1 files)
      … 1 files under this directory
  todos/  (6 files)
    create.js
    delete.js
    dynamodb.js
    get.js
    list.js
    update.js
  .gitignore
  README.md
  package.json
  serverless.yml
aws-node-s3-file-replicator/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-scheduled-cron/  (4 files)
  .gitignore
  README.md
  handler.js
  serverless.yml
aws-node-self-managed-code-storage/  (4 files)
  layer/  (1 files)
    nodejs/  (1 files)
      … 1 files under this directory
  README.md
  handler.mjs
  serverless.yml
aws-node-serve-dynamic-html-via-http-endpoint/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-serverless-gong/  (4 files)
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-ses-receive-email-body/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-ses-receive-email-header/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-shared-gateway/  (22 files)
  gateway/  (3 files)
    .gitignore
    README.md
    serverless.yml
  products/  (5 files)
    .gitignore
    README.md
    handler.js
    package.json
    serverless.yml
  transactions/  (5 files)
    .gitignore
    README.md
    handler.js
    package.json
    serverless.yml
  users/  (5 files)
    .gitignore
    README.md
    handler.js
    package.json
    serverless.yml
  README.md
  ci-decomission.sh
  ci-deploy.sh
  package.json
aws-node-signed-uploads/  (5 files)
  src/  (1 files)
    upload.js
  .gitignore
  README.md
  package.json
  serverless.yml
aws-node-simple-http-endpoint/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-simple-transcribe-s3/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-single-page-app-via-cloudfront/  (8 files)
  app/  (2 files)
    app.js
    index.html
  serverless-single-page-app-plugin/  (2 files)
    index.js
    package.json
  .gitignore
  README.md
  package.json
  serverless.yml
aws-node-sqs-worker/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-stripe-integration/  (5 files)
  .gitignore
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-telegram-echo-bot/  (4 files)
  README.md
  handler.js
  package.json
  serverless.yml
aws-node-text-analysis-via-sns-post-processing/  (6 files)
  .gitignore
  README.md
  addNote.js
  analyzeNote.js
  package.json
  serverless.yml
aws-node-twilio-send-text-message/  (11 files)
  frontend/  (2 files)
    app.css
    index.html
  .gitignore
  .npmignore
  README.md
  event.json
  handler.js
  messenger.js
  messenger.test.js
  package.json
  serverless.yml
aws-node-typescript-apollo-lambda/  (18 files)
  src/  (12 files)
    graphql/  (11 files)
      … 11 files under this directory
    handler.ts
  .gitignore
  README.md
  esbuild.config.js
  package.json
  serverless.yml
  tsconfig.json
aws-node-typescript-kinesis/  (8 files)
  kinesis/  (2 files)
    consumer.ts
    producer.ts
  .gitignore
  README.md
  handler.ts
  package.json
  serverless.yml
  tsconfig.json
aws-node-typescript-nest/  (18 files)
  src/  (5 files)
    app.controller.spec.ts
    app.controller.ts
    app.module.ts
    app.service.ts
    main.ts
  test/  (2 files)
    app.e2e-spec.ts
    jest-e2e.json
  .gitignore
  .prettierrc
  README.md
  bench.js
  esbuild.config.js
  nest-cli.json
  package.json
  serverless.yml
  tsconfig.build.json
  tsconfig.json
  tsconfig.spec.json
aws-node-typescript-rest-api-with-dynamodb/  (9 files)
  todos/  (4 files)
    create.ts
    get.ts
    list.ts
    update.ts
  .gitignore
  README.md
  package.json
  serverless.yml
  tsconfig.json
aws-node-typescript-sqs-standard/  (8 files)
  sqs/  (2 files)
    receiver.ts
    sender.ts
  .gitignore
  README.md
  handler.ts
  package.json
  serverless.yml
  tsconfig.json
aws-node-upload-to-s3-and-postprocess/  (7 files)
  frontend/  (1 files)
    index.template.html
  .gitignore
  README.md
  generate-form.js
  handler.js
  package.json
  serverless.yml
aws-node-web-app-custom-domain/  (12 files)
  api/  (2 files)
    package.json
    server.js
  web/  (7 files)
    app/  (4 files)
      … 4 files under this directory
    public/  (1 files)
      … 1 files under this directory
    next.config.mjs
    package.json
  .gitignore
  README.md
  serverless.yml
aws-node-websockets-authorizers/  (4 files)
  README.md
  handler.js
  package.json
  serverless.yml
aws-python-alexa-skill/  (5 files)
  .gitignore
  README.md
  handler.py
  package.json
  serverless.yml
aws-python-auth0-custom-authorizers-api/  (11 files)
  frontend/  (3 files)
    app.css
    app.js
    index.html
  .gitignore
  Makefile
  README.md
  lambda_handlers.py
  package.json
  public_key-example
  requirements.txt
  serverless.yml
aws-python-flask-api/  (5 files)
  README.md
  app.py
  package.json
  requirements.txt
  serverless.yml
aws-python-flask-dynamodb-api/  (5 files)
  README.md
  app.py
  package.json
  requirements.txt
  serverless.yml
aws-python-http-api-with-dynamodb/  (11 files)
  todos/  (7 files)
    __init__.py
    create.py
    decimalencoder.py
    delete.py
    get.py
    list.py
    update.py
  .gitignore
  README.md
  package.json
  serverless.yml
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
LICENSE.txt
README.md
```

## Entry points

- [aws-bedrock-agentcore/python/langgraph-basic-code/agent.py:122](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-basic-code/agent.py#L122)
- [aws-bedrock-agentcore/python/langgraph-basic-code/test-invoke.py:78](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-basic-code/test-invoke.py#L78)
- [aws-bedrock-agentcore/python/langgraph-basic-docker/agent.py:122](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-basic-docker/agent.py#L122)
- [aws-bedrock-agentcore/python/langgraph-basic-docker/test-invoke.py:75](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-basic-docker/test-invoke.py#L75)
- [aws-bedrock-agentcore/python/langgraph-browser-custom/agent.py:178](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-browser-custom/agent.py#L178)
- [aws-bedrock-agentcore/python/langgraph-browser-custom/test-invoke.py:218](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-browser-custom/test-invoke.py#L218)
- [aws-bedrock-agentcore/python/langgraph-browser/agent.py:94](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-browser/agent.py#L94)
- [aws-bedrock-agentcore/python/langgraph-browser/test-invoke.py:107](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-browser/test-invoke.py#L107)
- [aws-bedrock-agentcore/python/langgraph-code-interpreter-custom/agent.py:168](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-code-interpreter-custom/agent.py#L168)
- [aws-bedrock-agentcore/python/langgraph-code-interpreter-custom/test-invoke.py:162](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-code-interpreter-custom/test-invoke.py#L162)
- [aws-bedrock-agentcore/python/langgraph-code-interpreter/agent.py:107](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-code-interpreter/agent.py#L107)
- [aws-bedrock-agentcore/python/langgraph-code-interpreter/test-invoke.py:146](https://github.com/serverless/examples/blob/424fe6f7737bd45aeea4e5b40d7beda3422ffa54/aws-bedrock-agentcore/python/langgraph-code-interpreter/test-invoke.py#L146)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 17 file(s) under api layer (observed from repository paths and static analysis). Observed top-level functions: _evaluate_node, handler, safe_calculate. |
| aws-bedrock-agentcore package | library | Observed | Groups 29 file(s) under aws-bedrock-agentcore package (observed from repository paths and static analysis). |
| aws-dev-mode package | library | Observed | Groups 2 file(s) under aws-dev-mode package (observed from repository paths and static analysis). Observed top-level functions: process. |
| aws-dotnet-rest-api-with-dynamodb package | library | Observed | Groups 12 file(s) under aws-dotnet-rest-api-with-dynamodb package (observed from repository paths and static analysis). |
| aws-ffmpeg-layer package | library | Observed | Groups 2 file(s) under aws-ffmpeg-layer package (observed from repository paths and static analysis). |
| aws-golang-auth-examples package | library | Observed | Groups 12 file(s) under aws-golang-auth-examples package (observed from repository paths and static analysis). |
| aws-golang-googlemap package | library | Observed | Groups 5 file(s) under aws-golang-googlemap package (observed from repository paths and static analysis). |
| aws-golang-http-get-post package | library | Observed | Groups 3 file(s) under aws-golang-http-get-post package (observed from repository paths and static analysis). |
| aws-golang-rest-api-with-dynamodb package | library | Observed | Groups 5 file(s) under aws-golang-rest-api-with-dynamodb package (observed from repository paths and static analysis). |
| aws-golang-s3-file-replicator package | library | Observed | Groups 1 file(s) under aws-golang-s3-file-replicator package (observed from repository paths and static analysis). |
| aws-golang-simple-http-endpoint package | library | Observed | Groups 2 file(s) under aws-golang-simple-http-endpoint package (observed from repository paths and static analysis). |
| aws-java-simple-http-endpoint package | library | Observed | Groups 3 file(s) under aws-java-simple-http-endpoint package (observed from repository paths and static analysis). |
| aws-multiple-runtime package | library | Observed | Groups 1 file(s) under aws-multiple-runtime package (observed from repository paths and static analysis). Observed top-level functions: hello. |
| aws-node package | library | Observed | Groups 1 file(s) under aws-node package (observed from repository paths and static analysis). |
| aws-node-alexa-skill package | library | Observed | Groups 1 file(s) under aws-node-alexa-skill package (observed from repository paths and static analysis). |
| aws-node-auth0-cognito-custom-authorize… package | library | Observed | Groups 2 file(s) under aws-node-auth0-cognito-custom-authorize… package (observed from repository paths and static analysis). |
| aws-node-auth0-custom-authorizers-api package | library | Observed | Groups 2 file(s) under aws-node-auth0-custom-authorizers-api package (observed from repository paths and static analysis). |
| aws-node-container-snapstart package | library | Observed | Groups 1 file(s) under aws-node-container-snapstart package (observed from repository paths and static analysis). |
| aws-node-durable-function package | library | Observed | Groups 1 file(s) under aws-node-durable-function package (observed from repository paths and static analysis). |
| aws-node-dynamic-image-resizer package | library | Observed | Groups 1 file(s) under aws-node-dynamic-image-resizer package (observed from repository paths and static analysis). |
| aws-node-dynamodb-stream-processing package | library | Observed | Groups 1 file(s) under aws-node-dynamodb-stream-processing package (observed from repository paths and static analysis). |
| aws-node-env-variables package | library | Observed | Groups 1 file(s) under aws-node-env-variables package (observed from repository paths and static analysis). |
| aws-node-env-variables-encrypted-in-a-f… package | library | Observed | Groups 3 file(s) under aws-node-env-variables-encrypted-in-a-f… package (observed from repository paths and static analysis). |
| aws-node-esm-esbuild package | library | Observed | Groups 1 file(s) under aws-node-esm-esbuild package (observed from repository paths and static analysis). |
| aws-node-express-api package | library | Observed | Groups 1 file(s) under aws-node-express-api package (observed from repository paths and static analysis). |
| aws-node-express-dynamodb-api package | library | Observed | Groups 1 file(s) under aws-node-express-dynamodb-api package (observed from repository paths and static analysis). |
| aws-node-express-web-app package | library | Observed | Groups 1 file(s) under aws-node-express-web-app package (observed from repository paths and static analysis). |
| aws-node-fetch-file-and-store-in-s3 package | library | Observed | Groups 1 file(s) under aws-node-fetch-file-and-store-in-s3 package (observed from repository paths and static analysis). |
| aws-node-github-check package | library | Observed | Groups 3 file(s) under aws-node-github-check package (observed from repository paths and static analysis). |
| aws-node-github-webhook-listener package | library | Observed | Groups 1 file(s) under aws-node-github-webhook-listener package (observed from repository paths and static analysis). |
| aws-node-graphql-api-with-dynamodb package | library | Observed | Groups 1 file(s) under aws-node-graphql-api-with-dynamodb package (observed from repository paths and static analysis). |
| aws-node-http-api package | library | Observed | Groups 1 file(s) under aws-node-http-api package (observed from repository paths and static analysis). |
| aws-node-http-api-dynamodb package | library | Observed | Groups 5 file(s) under aws-node-http-api-dynamodb package (observed from repository paths and static analysis). |
| aws-node-http-api-dynamodb-local package | library | Observed | Groups 6 file(s) under aws-node-http-api-dynamodb-local package (observed from repository paths and static analysis). |
| aws-node-http-api-mongodb package | library | Observed | Groups 2 file(s) under aws-node-http-api-mongodb package (observed from repository paths and static analysis). |
| aws-node-http-api-typescript package | library | Observed | Groups 1 file(s) under aws-node-http-api-typescript package (observed from repository paths and static analysis). |
| aws-node-http-api-typescript-dynamodb package | library | Observed | Groups 4 file(s) under aws-node-http-api-typescript-dynamodb package (observed from repository paths and static analysis). |
| aws-node-iot-event package | library | Observed | Groups 1 file(s) under aws-node-iot-event package (observed from repository paths and static analysis). |
| aws-node-mongodb-atlas package | library | Observed | Groups 2 file(s) under aws-node-mongodb-atlas package (observed from repository paths and static analysis). |
| aws-node-nextjs-web-app package | library | Observed | Groups 3 file(s) under aws-node-nextjs-web-app package (observed from repository paths and static analysis). |
| aws-node-puppeteer package | library | Observed | Groups 1 file(s) under aws-node-puppeteer package (observed from repository paths and static analysis). |
| aws-node-recursive-function package | library | Observed | Groups 1 file(s) under aws-node-recursive-function package (observed from repository paths and static analysis). |
| aws-node-rekognition-analysis-s3-image package | library | Observed | Groups 2 file(s) under aws-node-rekognition-analysis-s3-image package (observed from repository paths and static analysis). |
| aws-node-rest-api package | library | Observed | Groups 1 file(s) under aws-node-rest-api package (observed from repository paths and static analysis). |
| aws-node-rest-api-mongodb package | library | Observed | Groups 2 file(s) under aws-node-rest-api-mongodb package (observed from repository paths and static analysis). |
| aws-node-rest-api-typescript package | library | Observed | Groups 8 file(s) under aws-node-rest-api-typescript package (observed from repository paths and static analysis). |
| aws-node-rest-api-typescript-simple package | library | Observed | Groups 1 file(s) under aws-node-rest-api-typescript-simple package (observed from repository paths and static analysis). |
| aws-node-rest-api-with-dynamodb package | library | Observed | Groups 5 file(s) under aws-node-rest-api-with-dynamodb package (observed from repository paths and static analysis). |
| aws-node-rest-api-with-dynamodb-and-off… package | library | Observed | Groups 6 file(s) under aws-node-rest-api-with-dynamodb-and-off… package (observed from repository paths and static analysis). |
| aws-node-s3-file-replicator package | library | Observed | Groups 1 file(s) under aws-node-s3-file-replicator package (observed from repository paths and static analysis). |
| aws-node-scheduled-cron package | library | Observed | Groups 1 file(s) under aws-node-scheduled-cron package (observed from repository paths and static analysis). |
| aws-node-self-managed-code-storage package | library | Observed | Groups 2 file(s) under aws-node-self-managed-code-storage package (observed from repository paths and static analysis). |
| aws-node-serve-dynamic-html-via-http-en… package | library | Observed | Groups 1 file(s) under aws-node-serve-dynamic-html-via-http-en… package (observed from repository paths and static analysis). |
| aws-node-serverless-gong package | library | Observed | Groups 1 file(s) under aws-node-serverless-gong package (observed from repository paths and static analysis). |
| aws-node-ses-receive-email-body package | library | Observed | Groups 1 file(s) under aws-node-ses-receive-email-body package (observed from repository paths and static analysis). |
| aws-node-ses-receive-email-header package | library | Observed | Groups 1 file(s) under aws-node-ses-receive-email-header package (observed from repository paths and static analysis). |
| aws-node-shared-gateway package | library | Observed | Groups 5 file(s) under aws-node-shared-gateway package (observed from repository paths and static analysis). |
| aws-node-signed-uploads package | library | Observed | Groups 1 file(s) under aws-node-signed-uploads package (observed from repository paths and static analysis). |
| aws-node-simple-http-endpoint package | library | Observed | Groups 1 file(s) under aws-node-simple-http-endpoint package (observed from repository paths and static analysis). |
| aws-node-simple-transcribe-s3 package | library | Observed | Groups 1 file(s) under aws-node-simple-transcribe-s3 package (observed from repository paths and static analysis). |
| aws-node-single-page-app-via-cloudfront package | library | Observed | Groups 2 file(s) under aws-node-single-page-app-via-cloudfront package (observed from repository paths and static analysis). |
| aws-node-sqs-worker package | library | Observed | Groups 1 file(s) under aws-node-sqs-worker package (observed from repository paths and static analysis). |
| aws-node-stripe-integration package | library | Observed | Groups 1 file(s) under aws-node-stripe-integration package (observed from repository paths and static analysis). |
| aws-node-telegram-echo-bot package | library | Observed | Groups 1 file(s) under aws-node-telegram-echo-bot package (observed from repository paths and static analysis). |
| aws-node-text-analysis-via-sns-post-pro… package | library | Observed | Groups 2 file(s) under aws-node-text-analysis-via-sns-post-pro… package (observed from repository paths and static analysis). |
| aws-node-twilio-send-text-message package | library | Observed | Groups 3 file(s) under aws-node-twilio-send-text-message package (observed from repository paths and static analysis). |
| aws-node-typescript-apollo-lambda package | library | Observed | Groups 13 file(s) under aws-node-typescript-apollo-lambda package (observed from repository paths and static analysis). |
| aws-node-typescript-kinesis package | library | Observed | Groups 3 file(s) under aws-node-typescript-kinesis package (observed from repository paths and static analysis). |
| aws-node-typescript-nest package | library | Observed | Groups 7 file(s) under aws-node-typescript-nest package (observed from repository paths and static analysis). |
| aws-node-typescript-rest-api-with-dynam… package | library | Observed | Groups 4 file(s) under aws-node-typescript-rest-api-with-dynam… package (observed from repository paths and static analysis). |
| aws-node-typescript-sqs-standard package | library | Observed | Groups 3 file(s) under aws-node-typescript-sqs-standard package (observed from repository paths and static analysis). |
| aws-node-upload-to-s3-and-postprocess package | library | Observed | Groups 2 file(s) under aws-node-upload-to-s3-and-postprocess package (observed from repository paths and static analysis). |
| aws-node-web-app-custom-domain package | library | Observed | Groups 4 file(s) under aws-node-web-app-custom-domain package (observed from repository paths and static analysis). |
| aws-node-websockets-authorizers package | library | Observed | Groups 1 file(s) under aws-node-websockets-authorizers package (observed from repository paths and static analysis). |
| aws-python-alexa-skill package | library | Observed | Groups 1 file(s) under aws-python-alexa-skill package (observed from repository paths and static analysis). Observed top-level functions: lucky_number, parseInt. |
| aws-python-auth0-custom-authorizers-api package | library | Observed | Groups 2 file(s) under aws-python-auth0-custom-authorizers-api package (observed from repository paths and static analysis). Observed top-level functions: auth, convert_certificate_to_pem, create_200_response, create_aw… |
| aws-python-http-api-with-dynamodb package | library | Observed | Groups 7 file(s) under aws-python-http-api-with-dynamodb package (observed from repository paths and static analysis). Observed top-level classes: DecimalEncoder. Observed top-level functions: create, delete, get, list,… |
| Configuration and deployment | config | Observed | Groups 253 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 23 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /hello, ROUTE /users/<string:user_id>,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `aws-bedrock-agentcore/javascript/langgraph-basic-dockerfile/Dockerfile` (container)
- `aws-bedrock-agentcore/javascript/langgraph-basic-dockerfile/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-basic-dockerfile/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-basic/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-basic/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-browser-custom/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-browser-custom/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-browser/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-browser/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-code-interpreter-custom/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-code-interpreter-custom/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-code-interpreter/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-code-interpreter/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-comprehensive/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-comprehensive/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-gateway/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-gateway/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-memory/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-memory/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-multi-gateway/Dockerfile.private` (container)
- `aws-bedrock-agentcore/javascript/langgraph-multi-gateway/Dockerfile.public` (container)
- `aws-bedrock-agentcore/javascript/langgraph-multi-gateway/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-multi-gateway/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/langgraph-streaming/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/langgraph-streaming/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/mcp-server-lambda-tools/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/mcp-server-lambda-tools/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/mcp-server/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/mcp-server/serverless.yml` (config)
- `aws-bedrock-agentcore/javascript/strands-browser/package.json` (manifest)
- `aws-bedrock-agentcore/javascript/strands-browser/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-basic-code/requirements.txt` (manifest)
- `aws-bedrock-agentcore/python/langgraph-basic-code/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-basic-docker/Dockerfile` (container)
- `aws-bedrock-agentcore/python/langgraph-basic-docker/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-basic-docker/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-browser-custom/Dockerfile` (container)
- `aws-bedrock-agentcore/python/langgraph-browser-custom/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-browser-custom/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-browser/Dockerfile` (container)
- `aws-bedrock-agentcore/python/langgraph-browser/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-browser/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-code-interpreter-custom/Dockerfile` (container)
- `aws-bedrock-agentcore/python/langgraph-code-interpreter-custom/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-code-interpreter-custom/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-code-interpreter/Dockerfile` (container)
- `aws-bedrock-agentcore/python/langgraph-code-interpreter/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-code-interpreter/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-gateway/Dockerfile` (container)
- `aws-bedrock-agentcore/python/langgraph-gateway/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-gateway/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-memory/Dockerfile` (container)
- `aws-bedrock-agentcore/python/langgraph-memory/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-memory/serverless.yml` (config)
- `aws-bedrock-agentcore/python/langgraph-multi-gateway/Dockerfile.private` (container)
- `aws-bedrock-agentcore/python/langgraph-multi-gateway/Dockerfile.public` (container)
- `aws-bedrock-agentcore/python/langgraph-multi-gateway/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/langgraph-multi-gateway/serverless.yml` (config)
- `aws-bedrock-agentcore/python/strands-browser/Dockerfile` (container)
- `aws-bedrock-agentcore/python/strands-browser/pyproject.toml` (manifest)
- `aws-bedrock-agentcore/python/strands-browser/serverless.yml` (config)
- `aws-dev-mode/package.json` (manifest)
- `aws-dev-mode/serverless.yml` (config)
- `aws-dotnet-rest-api-with-dynamodb/src/DotNetServerless.Lambda/.config/dotnet-tools.json` (config)
- `aws-dotnet-rest-api-with-dynamodb/src/DotNetServerless.Lambda/env.configs.example.yml` (config)
- `aws-dotnet-rest-api-with-dynamodb/src/DotNetServerless.Lambda/package.json` (manifest)
- `aws-dotnet-rest-api-with-dynamodb/src/DotNetServerless.Lambda/serverless.yml` (config)
- `aws-ffmpeg-layer/package.json` (manifest)
- `aws-ffmpeg-layer/serverless.yml` (config)
- `aws-golang-auth-examples/go.mod` (manifest)
- `aws-golang-auth-examples/package.json` (manifest)
- `aws-golang-auth-examples/serverless.yml` (config)
- `aws-golang-googlemap/go.mod` (manifest)
- `aws-golang-googlemap/serverless.yml` (config)
- `aws-golang-http-get-post/go.mod` (manifest)
- `aws-golang-http-get-post/package.json` (manifest)
- `aws-golang-http-get-post/serverless.yml` (config)
- `aws-golang-rest-api-with-dynamodb/go.mod` (manifest)
- `aws-golang-rest-api-with-dynamodb/package.json` (manifest)
- `aws-golang-rest-api-with-dynamodb/serverless.yml` (config)
- `aws-golang-s3-file-replicator/go.mod` (manifest)
- `aws-golang-s3-file-replicator/serverless.yml` (config)
- `aws-golang-simple-http-endpoint/go.mod` (manifest)
- `aws-golang-simple-http-endpoint/package.json` (manifest)
- `aws-golang-simple-http-endpoint/serverless.yml` (config)
- `aws-java-simple-http-endpoint/build.gradle` (manifest)
- `aws-java-simple-http-endpoint/pom.xml` (manifest)
- `aws-java-simple-http-endpoint/serverless.yml` (config)
- `aws-multiple-runtime/package.json` (manifest)
- `aws-multiple-runtime/serverless.yml` (config)
- `aws-node-alexa-skill/package.json` (manifest)
- `aws-node-alexa-skill/serverless.yml` (config)
- `aws-node-auth0-cognito-custom-authorizers-api/package.json` (manifest)
- `aws-node-auth0-cognito-custom-authorizers-api/serverless.yml` (config)
- `aws-node-auth0-custom-authorizers-api/package.json` (manifest)
- `aws-node-auth0-custom-authorizers-api/serverless.yml` (config)
- `aws-node-container-snapstart/Dockerfile` (container)
- `aws-node-container-snapstart/serverless.yml` (config)
- `aws-node-durable-function/package.json` (manifest)
- `aws-node-durable-function/serverless.yml` (config)
- `aws-node-dynamic-image-resizer/package.json` (manifest)
- `aws-node-dynamic-image-resizer/serverless.yml` (config)
- `aws-node-dynamodb-stream-processing/package.json` (manifest)
- `aws-node-dynamodb-stream-processing/serverless.yml` (config)
- `aws-node-env-variables-encrypted-in-a-file/package.json` (manifest)
- `aws-node-env-variables-encrypted-in-a-file/serverless.yml` (config)
- `aws-node-env-variables/package.json` (manifest)
- `aws-node-env-variables/serverless.yml` (config)
- `aws-node-esm-esbuild/serverless.yml` (config)
- `aws-node-express-api/package.json` (manifest)
- `aws-node-express-api/serverless.yml` (config)
- `aws-node-express-dynamodb-api/package.json` (manifest)
- `aws-node-express-dynamodb-api/serverless.yml` (config)
- `aws-node-express-web-app/package.json` (manifest)
- `aws-node-express-web-app/serverless.yml` (config)
- `aws-node-fetch-file-and-store-in-s3/package.json` (manifest)
- `aws-node-fetch-file-and-store-in-s3/serverless.yml` (config)
- `aws-node-github-check/package.json` (manifest)
- `aws-node-github-check/serverless.yaml` (config)
- `aws-node-github-webhook-listener/package.json` (manifest)
- `aws-node-github-webhook-listener/serverless.yml` (config)
- `aws-node-graphql-api-with-dynamodb/package.json` (manifest)
- `aws-node-graphql-api-with-dynamodb/serverless.yml` (config)
- `aws-node-http-api-dynamodb-local/dynamodb/Dockerfile` (container)
- `aws-node-http-api-dynamodb-local/dynamodb/docker-compose.yml` (container)
- `aws-node-http-api-dynamodb-local/offline/migrations/todos.json` (config)
- `aws-node-http-api-dynamodb-local/package.json` (manifest)
- `aws-node-http-api-dynamodb-local/serverless.yml` (config)
- `aws-node-http-api-dynamodb/package.json` (manifest)
- `aws-node-http-api-dynamodb/serverless.yml` (config)
- `aws-node-http-api-mongodb/package.json` (manifest)
- `aws-node-http-api-mongodb/serverless.yml` (config)
- `aws-node-http-api-typescript-dynamodb/package.json` (manifest)
- `aws-node-http-api-typescript-dynamodb/serverless.yml` (config)
- `aws-node-http-api-typescript-dynamodb/tsconfig.json` (config)
- `aws-node-http-api-typescript/package.json` (manifest)
- `aws-node-http-api-typescript/serverless.yml` (config)
- `aws-node-http-api-typescript/tsconfig.json` (config)
- `aws-node-http-api/serverless.yml` (config)
- `aws-node-iot-event/package.json` (manifest)
- `aws-node-iot-event/serverless.yml` (config)
- `aws-node-mongodb-atlas/package.json` (manifest)
- `aws-node-mongodb-atlas/serverless.yml` (config)
- `aws-node-nextjs-web-app/package.json` (manifest)
- `aws-node-nextjs-web-app/serverless.yml` (config)
- `aws-node-puppeteer/package.json` (manifest)
- `aws-node-puppeteer/serverless.yml` (config)
- `aws-node-recursive-function/event.json` (config)
- `aws-node-recursive-function/package.json` (manifest)
- `aws-node-recursive-function/serverless.yml` (config)
- `aws-node-rekognition-analysis-s3-image/package.json` (manifest)
- `aws-node-rekognition-analysis-s3-image/post.json` (config)
- `aws-node-rekognition-analysis-s3-image/serverless.yml` (config)
- `aws-node-rest-api-mongodb/package.json` (manifest)
- `aws-node-rest-api-mongodb/serverless.yml` (config)
- `aws-node-rest-api-typescript-simple/package.json` (manifest)
- `aws-node-rest-api-typescript-simple/serverless.yml` (config)
- `aws-node-rest-api-typescript-simple/tsconfig.json` (config)
- `aws-node-rest-api-typescript/.editorconfig` (config)
- `aws-node-rest-api-typescript/.nycrc.json` (config)
- `aws-node-rest-api-typescript/package.json` (manifest)
- `aws-node-rest-api-typescript/serverless.yml` (config)
- `aws-node-rest-api-typescript/tsconfig.json` (config)
- `aws-node-rest-api-with-dynamodb-and-offline/dynamodb/Dockerfile` (container)
- `aws-node-rest-api-with-dynamodb-and-offline/dynamodb/docker-compose.yml` (container)
- `aws-node-rest-api-with-dynamodb-and-offline/offline/migrations/todos.json` (config)
- `aws-node-rest-api-with-dynamodb-and-offline/package.json` (manifest)
- `aws-node-rest-api-with-dynamodb-and-offline/serverless.yml` (config)
- `aws-node-rest-api-with-dynamodb/package.json` (manifest)
- `aws-node-rest-api-with-dynamodb/serverless.yml` (config)
- `aws-node-rest-api/package.json` (manifest)
- `aws-node-rest-api/serverless.yml` (config)
- `aws-node-s3-file-replicator/package.json` (manifest)
- `aws-node-s3-file-replicator/serverless.yml` (config)
- `aws-node-scheduled-cron/serverless.yml` (config)
- `aws-node-self-managed-code-storage/serverless.yml` (config)
- `aws-node-serve-dynamic-html-via-http-endpoint/package.json` (manifest)
- `aws-node-serve-dynamic-html-via-http-endpoint/serverless.yml` (config)
- `aws-node-serverless-gong/package.json` (manifest)
- `aws-node-serverless-gong/serverless.yml` (config)
- `aws-node-ses-receive-email-body/package.json` (manifest)
- `aws-node-ses-receive-email-body/serverless.yml` (config)
- `aws-node-ses-receive-email-header/package.json` (manifest)
- `aws-node-ses-receive-email-header/serverless.yml` (config)
- `aws-node-shared-gateway/gateway/serverless.yml` (config)
- `aws-node-shared-gateway/package.json` (manifest)
- `aws-node-shared-gateway/products/package.json` (manifest)
- `aws-node-shared-gateway/products/serverless.yml` (config)
- `aws-node-shared-gateway/transactions/package.json` (manifest)
- `aws-node-shared-gateway/transactions/serverless.yml` (config)
- `aws-node-shared-gateway/users/package.json` (manifest)
- `aws-node-shared-gateway/users/serverless.yml` (config)
- `aws-node-signed-uploads/package.json` (manifest)
- `aws-node-signed-uploads/serverless.yml` (config)
- `aws-node-simple-http-endpoint/package.json` (manifest)
- `aws-node-simple-http-endpoint/serverless.yml` (config)
- `aws-node-simple-transcribe-s3/package.json` (manifest)
- `aws-node-simple-transcribe-s3/serverless.yml` (config)
- `aws-node-single-page-app-via-cloudfront/package.json` (manifest)
- `aws-node-single-page-app-via-cloudfront/serverless-single-page-app-plugin/package.json` (manifest)
- `aws-node-single-page-app-via-cloudfront/serverless.yml` (config)
- `aws-node-sqs-worker/package.json` (manifest)
- `aws-node-sqs-worker/serverless.yml` (config)
- `aws-node-stripe-integration/package.json` (manifest)
- `aws-node-stripe-integration/serverless.yml` (config)
- `aws-node-telegram-echo-bot/package.json` (manifest)
- `aws-node-telegram-echo-bot/serverless.yml` (config)
- `aws-node-text-analysis-via-sns-post-processing/package.json` (manifest)
- `aws-node-text-analysis-via-sns-post-processing/serverless.yml` (config)
- `aws-node-twilio-send-text-message/event.json` (config)
- `aws-node-twilio-send-text-message/package.json` (manifest)
- `aws-node-twilio-send-text-message/serverless.yml` (config)
- `aws-node-typescript-apollo-lambda/package.json` (manifest)
- `aws-node-typescript-apollo-lambda/serverless.yml` (config)
- `aws-node-typescript-apollo-lambda/tsconfig.json` (config)
- `aws-node-typescript-kinesis/package.json` (manifest)
- `aws-node-typescript-kinesis/serverless.yml` (config)
- `aws-node-typescript-kinesis/tsconfig.json` (config)
- `aws-node-typescript-nest/nest-cli.json` (config)
- `aws-node-typescript-nest/package.json` (manifest)
- `aws-node-typescript-nest/serverless.yml` (config)
- `aws-node-typescript-nest/tsconfig.build.json` (config)
- `aws-node-typescript-nest/tsconfig.json` (config)
- `aws-node-typescript-nest/tsconfig.spec.json` (config)
- `aws-node-typescript-rest-api-with-dynamodb/package.json` (manifest)
- `aws-node-typescript-rest-api-with-dynamodb/serverless.yml` (config)
- `aws-node-typescript-rest-api-with-dynamodb/tsconfig.json` (config)
- `aws-node-typescript-sqs-standard/package.json` (manifest)
- `aws-node-typescript-sqs-standard/serverless.yml` (config)
- `aws-node-typescript-sqs-standard/tsconfig.json` (config)
- `aws-node-upload-to-s3-and-postprocess/package.json` (manifest)
- `aws-node-upload-to-s3-and-postprocess/serverless.yml` (config)
- `aws-node-web-app-custom-domain/api/package.json` (manifest)
- `aws-node-web-app-custom-domain/serverless.yml` (config)
- `aws-node-web-app-custom-domain/web/package.json` (manifest)
- `aws-node-websockets-authorizers/package.json` (manifest)
- `aws-node-websockets-authorizers/serverless.yml` (config)
- `aws-node/serverless.yml` (config)
- `aws-python-alexa-skill/package.json` (manifest)
- `aws-python-alexa-skill/serverless.yml` (config)
- `aws-python-auth0-custom-authorizers-api/package.json` (manifest)
- `aws-python-auth0-custom-authorizers-api/requirements.txt` (manifest)
- `aws-python-auth0-custom-authorizers-api/serverless.yml` (config)
- `aws-python-flask-api/package.json` (manifest)
- `aws-python-flask-api/requirements.txt` (manifest)
- `aws-python-flask-api/serverless.yml` (config)
- `aws-python-flask-dynamodb-api/package.json` (manifest)
- `aws-python-flask-dynamodb-api/requirements.txt` (manifest)
- `aws-python-flask-dynamodb-api/serverless.yml` (config)
- `aws-python-http-api-with-dynamodb/package.json` (manifest)
- `aws-python-http-api-with-dynamodb/serverless.yml` (config)

## Top-level layout

- `aws-bedrock-agentcore` — 154 analysed file(s)
- `aws-dotnet-rest-api-with-dynamodb` — 33 analysed file(s)
- `aws-node-shared-gateway` — 22 analysed file(s)
- `aws-golang-auth-examples` — 19 analysed file(s)
- `aws-node-rest-api-typescript` — 18 analysed file(s)
- `aws-node-typescript-apollo-lambda` — 18 analysed file(s)
- `aws-node-typescript-nest` — 18 analysed file(s)
- `aws-node-http-api-dynamodb-local` — 13 analysed file(s)
- `aws-node-rest-api-with-dynamodb-and-offline` — 13 analysed file(s)
- `aws-golang-rest-api-with-dynamodb` — 12 analysed file(s)
- `aws-node-web-app-custom-domain` — 12 analysed file(s)
- `aws-golang-googlemap` — 11 analysed file(s)
- `aws-java-simple-http-endpoint` — 11 analysed file(s)
- `aws-node-twilio-send-text-message` — 11 analysed file(s)
- `aws-python-auth0-custom-authorizers-api` — 11 analysed file(s)
- `aws-python-http-api-with-dynamodb` — 11 analysed file(s)
- `aws-golang-http-get-post` — 10 analysed file(s)
- `aws-node-nextjs-web-app` — 10 analysed file(s)
- `aws-golang-simple-http-endpoint` — 9 analysed file(s)
- `aws-node-auth0-custom-authorizers-api` — 9 analysed file(s)
- `aws-node-env-variables-encrypted-in-a-file` — 9 analysed file(s)
- `aws-node-http-api-dynamodb` — 9 analysed file(s)
- `aws-node-http-api-typescript-dynamodb` — 9 analysed file(s)
- `aws-node-rest-api-with-dynamodb` — 9 analysed file(s)
- `aws-node-typescript-rest-api-with-dynamodb` — 9 analysed file(s)
- `aws-node-github-check` — 8 analysed file(s)
- `aws-node-single-page-app-via-cloudfront` — 8 analysed file(s)
- `aws-node-typescript-kinesis` — 8 analysed file(s)
- `aws-node-typescript-sqs-standard` — 8 analysed file(s)
- `aws-golang-s3-file-replicator` — 7 analysed file(s)
- `aws-node-dynamic-image-resizer` — 7 analysed file(s)
- `aws-node-rekognition-analysis-s3-image` — 7 analysed file(s)
- `aws-node-upload-to-s3-and-postprocess` — 7 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `aws-dev-mode` — 6 analysed file(s)
- `aws-ffmpeg-layer` — 6 analysed file(s)
- `aws-multiple-runtime` — 6 analysed file(s)
- `aws-node-auth0-cognito-custom-authorizers-api` — 6 analysed file(s)
- `aws-node-http-api-mongodb` — 6 analysed file(s)
- `aws-node-http-api-typescript` — 6 analysed file(s)
- `aws-node-mongodb-atlas` — 6 analysed file(s)
- `aws-node-recursive-function` — 6 analysed file(s)
- `aws-node-rest-api-mongodb` — 6 analysed file(s)
- `aws-node-rest-api-typescript-simple` — 6 analysed file(s)
- `aws-node-text-analysis-via-sns-post-processing` — 6 analysed file(s)
- `aws-node-alexa-skill` — 5 analysed file(s)
- `aws-node-env-variables` — 5 analysed file(s)
- `aws-node-express-api` — 5 analysed file(s)
- `aws-node-express-dynamodb-api` — 5 analysed file(s)
- `aws-node-fetch-file-and-store-in-s3` — 5 analysed file(s)
- `aws-node-github-webhook-listener` — 5 analysed file(s)
- `aws-node-graphql-api-with-dynamodb` — 5 analysed file(s)
- `aws-node-iot-event` — 5 analysed file(s)
- `aws-node-puppeteer` — 5 analysed file(s)
- `aws-node-rest-api` — 5 analysed file(s)
- `aws-node-s3-file-replicator` — 5 analysed file(s)
- `aws-node-serve-dynamic-html-via-http-endpoint` — 5 analysed file(s)
- `aws-node-ses-receive-email-body` — 5 analysed file(s)
- `aws-node-ses-receive-email-header` — 5 analysed file(s)
- `aws-node-signed-uploads` — 5 analysed file(s)
- `aws-node-simple-http-endpoint` — 5 analysed file(s)
- `aws-node-simple-transcribe-s3` — 5 analysed file(s)
- `aws-node-sqs-worker` — 5 analysed file(s)
- `aws-node-stripe-integration` — 5 analysed file(s)
- `aws-python-alexa-skill` — 5 analysed file(s)
- `aws-python-flask-api` — 5 analysed file(s)
- `aws-python-flask-dynamodb-api` — 5 analysed file(s)
- `aws-node` — 4 analysed file(s)
- `aws-node-container-snapstart` — 4 analysed file(s)
- `aws-node-durable-function` — 4 analysed file(s)
- `aws-node-dynamodb-stream-processing` — 4 analysed file(s)
- `aws-node-express-web-app` — 4 analysed file(s)
- `aws-node-http-api` — 4 analysed file(s)
- `aws-node-scheduled-cron` — 4 analysed file(s)
- `aws-node-self-managed-code-storage` — 4 analysed file(s)
- `aws-node-serverless-gong` — 4 analysed file(s)
- `aws-node-telegram-echo-bot` — 4 analysed file(s)
- `aws-node-websockets-authorizers` — 4 analysed file(s)
- `aws-node-esm-esbuild` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 40 file(s) were skipped during inventory (6 x likely secret file excluded; 34 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `424fe6f7737bd45aeea4e5b40d7beda3422ffa54` is the revision these paths and observations refer to.
