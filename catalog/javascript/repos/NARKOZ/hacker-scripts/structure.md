# Project structure: NARKOZ/hacker-scripts

**Analysed commit:** `b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0`

**Commit reference:** [b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0](https://github.com/NARKOZ/hacker-scripts/commit/b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0)

**Tree at this commit:** [NARKOZ/hacker-scripts@b14a0a89bdf7](https://github.com/NARKOZ/hacker-scripts/tree/b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NARKOZ/hacker-scripts |
| Description | Based on a true story |
| Stars | 49871 |
| Forks | 6621 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0` |
| Retrieved at | 2026-11-14T19:10:37.134799+00:00 |
| Files in this snapshot | 59 |

## Directory tree

```text
CSharp/  (2 files)
  Hangover.cs
  SmackMyBitch.cs
R/  (2 files)
  hangover.R
  smack_my_bitch_up.R
clojure/  (4 files)
  coffee.clj
  hangover.clj
  kumar.clj
  smack.clj
coffee/  (1 files)
  fucking.coffee
go/  (3 files)
  fucking-coffee.go
  hangover.go
  smack_my_bitch_up.go
groovy/  (1 files)
  fucking_coffee.groovy
java/  (4 files)
  FuckingCoffee.java
  Hangover.java
  KumarAsshole.java
  SmackMyBitch.java
kotlin/  (4 files)
  FuckingCoffee.kt
  Hangover.kt
  KumarAsshole.kt
  SmackMyBitch.kt
nodejs/  (5 files)
  fucking_coffee.js
  fucking_coffee_yo_server.js
  hangover.js
  kumar_asshole.js
  smack_my_bitch_up.js
perl/  (4 files)
  fucking-coffee.pl
  hangover.pl
  kumar-asshole.pl
  smack-my-bitch-up.pl
php/  (4 files)
  composer.json
  fucking_coffee.php
  hangover.php
  smack_my_bitch_up.php
powershell/  (3 files)
  fucking_coffee.psm1
  hangover.psm1
  smack_my_bitch_up.ps1
python/  (4 files)
  fucking_coffee.py
  hangover.py
  kumar_asshole.py
  smack_my_bitch_up.py
python3/  (6 files)
  fucking_coffee.py
  hackerutils.py
  hangover.py
  kumar_asshole.py
  requirements.txt
  smack_my_bitch_up.py
scala/  (1 files)
  fucking-coffee.scala
.env.example
README.md
README.zh-CN.md
fucking-coffee.sh
fucking_coffee.rb
hangover.rb
hangover.sh
kumar-asshole.sh
kumar_asshole.rb
smack-my-bitch-up.sh
smack_my_bitch_up.rb
```

## Entry points

- [python3/fucking_coffee.py:33](https://github.com/NARKOZ/hacker-scripts/blob/b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0/python3/fucking_coffee.py#L33)
- [python3/hangover.py:51](https://github.com/NARKOZ/hacker-scripts/blob/b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0/python3/hangover.py#L51)
- [python3/kumar_asshole.py:43](https://github.com/NARKOZ/hacker-scripts/blob/b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0/python3/kumar_asshole.py#L43)
- [python3/smack_my_bitch_up.py:50](https://github.com/NARKOZ/hacker-scripts/blob/b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0/python3/smack_my_bitch_up.py#L50)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| CSharp package | library | Observed | Groups 2 file(s) under csharp package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: main, send_reply. |
| go package | library | Observed | Groups 3 file(s) under go package (observed from repository paths and static analysis). |
| java package | library | Observed | Groups 4 file(s) under java package (observed from repository paths and static analysis). |
| nodejs package | library | Observed | Groups 5 file(s) under nodejs package (observed from repository paths and static analysis). |
| php package | library | Observed | Groups 3 file(s) under php package (observed from repository paths and static analysis). |
| python package | library | Observed | Groups 4 file(s) under python package (observed from repository paths and static analysis). |
| python3 package | library | Observed | Groups 1 file(s) under python3 package (observed from repository paths and static analysis). Observed top-level functions: get_dotenv, get_log_path, sh. |

## Important files

- `.env.example` (config)
- `php/composer.json` (config)
- `python3/requirements.txt` (manifest)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `python3` — 6 analysed file(s)
- `nodejs` — 5 analysed file(s)
- `clojure` — 4 analysed file(s)
- `java` — 4 analysed file(s)
- `kotlin` — 4 analysed file(s)
- `perl` — 4 analysed file(s)
- `php` — 4 analysed file(s)
- `python` — 4 analysed file(s)
- `go` — 3 analysed file(s)
- `powershell` — 3 analysed file(s)
- `CSharp` — 2 analysed file(s)
- `R` — 2 analysed file(s)
- `coffee` — 1 analysed file(s)
- `groovy` — 1 analysed file(s)
- `scala` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File python/hangover.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File python/smack_my_bitch_up.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b14a0a89bdf743c63ca4cc9cbcd866e050d7b3b0` is the revision these paths and observations refer to.
