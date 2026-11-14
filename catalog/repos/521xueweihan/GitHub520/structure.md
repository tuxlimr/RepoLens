# Project structure: 521xueweihan/GitHub520

**Analysed commit:** `617d378e97c54362c44d27a502611a8df72d1a0c`

**Commit reference:** [617d378e97c54362c44d27a502611a8df72d1a0c](https://github.com/521xueweihan/GitHub520/commit/617d378e97c54362c44d27a502611a8df72d1a0c)

**Tree at this commit:** [521xueweihan/GitHub520@617d378e97c5](https://github.com/521xueweihan/GitHub520/tree/617d378e97c54362c44d27a502611a8df72d1a0c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 521xueweihan/GitHub520 |
| Description | :kissing_heart: 让你“爱”上 GitHub，解决访问时图裂、加载慢的问题。（无需安装） |
| Stars | 30309 |
| Forks | 2773 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `617d378e97c54362c44d27a502611a8df72d1a0c` |
| Retrieved at | 2026-11-14T19:07:10.182638+00:00 |
| Files in this snapshot | 12 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    GitHub520.yml
  FUNDING.yml
.gitignore
README.md
README_template.md
actions_requirements.txt
common.py
fetch_ips.py
hosts
hosts.json
requirements.txt
update_ips.py
```

## Entry points

- [fetch_ips.py:179](https://github.com/521xueweihan/GitHub520/blob/617d378e97c54362c44d27a502611a8df72d1a0c/fetch_ips.py#L179)
- [update_ips.py:41](https://github.com/521xueweihan/GitHub520/blob/617d378e97c54362c44d27a502611a8df72d1a0c/update_ips.py#L41)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: get_json, write_file, write_host_file, write_hosts_content, write_json_file. |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: get_ip, get_ip_list_from_dns, get_ip_list_from_doh, get_json, main, ping_cached. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/GitHub520.yml` (ci)
- `hosts.json` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 10 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `617d378e97c54362c44d27a502611a8df72d1a0c` is the revision these paths and observations refer to.
