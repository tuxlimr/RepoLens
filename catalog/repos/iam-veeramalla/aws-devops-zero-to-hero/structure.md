# Project structure: iam-veeramalla/aws-devops-zero-to-hero

**Analysed commit:** `f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4`

**Commit reference:** [f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4](https://github.com/iam-veeramalla/aws-devops-zero-to-hero/commit/f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4)

**Tree at this commit:** [iam-veeramalla/aws-devops-zero-to-hero@f4aa48e41941](https://github.com/iam-veeramalla/aws-devops-zero-to-hero/tree/f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | iam-veeramalla/aws-devops-zero-to-hero |
| Description | AWS zero to hero repo for devops engineers to learn AWS in 30 Days. This repo includes projects, presentations, interview questions and real time examples. |
| Stars | 11714 |
| Forks | 15840 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4` |
| Retrieved at | 2026-11-14T19:10:25.770693+00:00 |
| Files in this snapshot | 79 |

## Directory tree

```text
day-14/  (8 files)
  simple-python-app/  (7 files)
    Dockerfile
    app.py
    appspec.yml
    buildspec.yml
    requirements.txt
    start_container.sh
    stop_container.sh
  README.md
day-16/  (4 files)
  custom_metrics_demo/  (2 files)
    cloudwatch_metrics.py
    requirements.txt
  default_metrics_demo/  (1 files)
    cpu_spike.py
  README.md
day-17/  (1 files)
  README.md
day-18/  (2 files)
  README.md
  ebs_stale_snapshosts.py
day-19/  (1 files)
  README.md
day-2/  (2 files)
  README.md
  interview-questions
day-20/  (1 files)
  README.md
day-21/  (5 files)
  Dockerfile
  README.md
  app.py
  commands.md
  requirements.txt
day-22/  (7 files)
  2048-app-deploy-ingress.md
  README.md
  alb-controller-add-on.md
  configure-oidc-connector.md
  installing-eks.md
  prerequisites.md
  sample-app.md
day-24/  (5 files)
  main.tf
  provider.tf
  userdata.sh
  userdata1.sh
  variables.tf
day-25/  (3 files)
  README.md
  lambda_function.py
  lambda_function_permissions.md
day-3/  (1 files)
  README.md
day-4/  (1 files)
  README.md
day-5/  (1 files)
  README.md
day-6/  (1 files)
  README.md
day-7/  (1 files)
  vpc-demo-2-tier-app
day-8/  (1 files)
  Interview_q&a
day-9/  (3 files)
  demos/  (2 files)
    bucket-policies/  (2 files)
      … 2 files under this directory
  README.md
interview-questions/  (26 files)
  01-ADVANCED.md
  01-SCENARIO-BASED.md
  aws-cli.md
  aws-terraform.md
  cloud-migration.md
  cloudformation.md
  cloudfront.md
  cloudtrail.md
  cloudwatch.md
  code-build.md
  code-deploy.md
  code-pipeline.md
  dynamodb.md
  ecr.md
  ecs.md
  eks.md
  elastic-bean-stalk.md
  elastic-cloud-compute.md
  elb.md
  iam.md
  lambda-functions.md
  rds.md
  route53.md
  s3.md
  … 2 more files
scripts/  (2 files)
  start_container.sh
  stop_container.sh
LICENSE
README.md
appspec.yml
```

## Entry points

- [day-14/simple-python-app/app.py:3](https://github.com/iam-veeramalla/aws-devops-zero-to-hero/blob/f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4/day-14/simple-python-app/app.py#L3)
- [day-16/custom_metrics_demo/cloudwatch_metrics.py:7](https://github.com/iam-veeramalla/aws-devops-zero-to-hero/blob/f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4/day-16/custom_metrics_demo/cloudwatch_metrics.py#L7)
- [day-16/default_metrics_demo/cpu_spike.py:24](https://github.com/iam-veeramalla/aws-devops-zero-to-hero/blob/f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4/day-16/default_metrics_demo/cpu_spike.py#L24)
- [day-21/app.py:5](https://github.com/iam-veeramalla/aws-devops-zero-to-hero/blob/f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4/day-21/app.py#L5)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| day-14 package | library | Observed | Groups 2 file(s) under day-14 package (observed from repository paths and static analysis). |
| day-18 package | library | Observed | Groups 1 file(s) under day-18 package (observed from repository paths and static analysis). Observed top-level functions: lambda_handler. |
| day-24 package | library | Observed | Groups 2 file(s) under day-24 package (observed from repository paths and static analysis). |
| day-25 package | library | Observed | Groups 1 file(s) under day-25 package (observed from repository paths and static analysis). Observed top-level functions: lambda_handler. |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /, ROUTE /product/<product_id>, ROUTE /… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `appspec.yml` (config)
- `day-14/simple-python-app/Dockerfile` (container)
- `day-14/simple-python-app/appspec.yml` (config)
- `day-14/simple-python-app/buildspec.yml` (config)
- `day-14/simple-python-app/requirements.txt` (manifest)
- `day-16/custom_metrics_demo/requirements.txt` (manifest)
- `day-21/Dockerfile` (container)
- `day-21/requirements.txt` (manifest)
- `day-9/demos/bucket-policies/restrict-access-to-owner.json` (config)
- `day-9/demos/bucket-policies/static-website-basic.json` (config)

## Top-level layout

- `interview-questions` — 26 analysed file(s)
- `day-14` — 8 analysed file(s)
- `day-22` — 7 analysed file(s)
- `day-21` — 5 analysed file(s)
- `day-24` — 5 analysed file(s)
- `day-16` — 4 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `day-25` — 3 analysed file(s)
- `day-9` — 3 analysed file(s)
- `day-18` — 2 analysed file(s)
- `day-2` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `day-17` — 1 analysed file(s)
- `day-19` — 1 analysed file(s)
- `day-20` — 1 analysed file(s)
- `day-3` — 1 analysed file(s)
- `day-4` — 1 analysed file(s)
- `day-5` — 1 analysed file(s)
- `day-6` — 1 analysed file(s)
- `day-7` — 1 analysed file(s)
- `day-8` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f4aa48e41941d2eedbd0f57684ccfb3c77fc52a4` is the revision these paths and observations refer to.
