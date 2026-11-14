# Project structure: wanshuiyin/Auto-claude-code-research-in-sleep

**Analysed commit:** `9f30e834d24a337dbdd06fb20a1150d4376dfa59`

**Commit reference:** [9f30e834d24a337dbdd06fb20a1150d4376dfa59](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/commit/9f30e834d24a337dbdd06fb20a1150d4376dfa59)

**Tree at this commit:** [wanshuiyin/Auto-claude-code-research-in-sleep@9f30e834d24a](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/9f30e834d24a337dbdd06fb20a1150d4376dfa59)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wanshuiyin/Auto-claude-code-research-in-sleep |
| Description | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent. |
| Stars | 19197 |
| Forks | 1548 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `9f30e834d24a337dbdd06fb20a1150d4376dfa59` |
| Retrieved at | 2026-11-14T19:08:16.785737+00:00 |
| Files in this snapshot | 202 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.codex-plugin/  (1 files)
  plugin.json
.github/  (7 files)
  agents/  (2 files)
    aris-reviewer-claude.agent.md
    aris-reviewer-openai.agent.md
  workflows/  (5 files)
    check-skills-inventory.yml
    lint-skills-helpers.yml
    test-install-aris-ps1.yml
    test-suite.yml
    verify-codex-policy-audit.yml
agents/  (1 files)
  aris-fanout-leaf.md
aris-monitor/  (7 files)
  README.md
  focus-tty.sh
  focus.py
  run.sh
  scanner.py
  ticker.py
  widget.py
commands/  (1 files)
  setup.md
docs/  (164 files)
  integrations/  (8 files)
    FEISHU.md
    FEISHU_CN.md
    OBSIDIAN.md
    OBSIDIAN_CN.md
    VAST_GPU_GUIDE.md
    VAST_GPU_GUIDE_CN.md
    ZOTERO.md
    ZOTERO_CN.md
  tutorials/  (108 files)
    3d_generation_tutorial.html
    3d_generation_tutorial.md
    3d_generation_tutorial.review.json
    3d_generation_tutorial_en.html
    3d_generation_tutorial_en.md
    README.md
    agent_foundations_tutorial.html
    agent_foundations_tutorial.md
    agent_foundations_tutorial.review.json
    agent_foundations_tutorial_en.html
    agent_foundations_tutorial_en.md
    agentic_rl_tutorial.html
    agentic_rl_tutorial.md
    agentic_rl_tutorial.review.json
    agentic_rl_tutorial_en.html
    agentic_rl_tutorial_en.md
    attention_tutorial.html
    attention_tutorial.md
    attention_tutorial.review.json
    attention_tutorial_en.html
    attention_tutorial_en.md
    diffusion_distillation_tutorial.html
    diffusion_distillation_tutorial.md
    diffusion_distillation_tutorial.review.json
    … 84 more files
  ALI_CODING_PLAN_GUIDE.md
  ANTIGRAVITY_ADAPTATION.md
  ANTIGRAVITY_ADAPTATION_CN.md
  ARIS-Code-README_CN.md
  ARIS-Code-README_EN.md
  ARIS_INTRO.html
  ARIS_INTRO.md
  ARIS_INTRO.review.json
  CODEX_CLAUDE_REVIEW_GUIDE.md
  CODEX_CLAUDE_REVIEW_GUIDE_CN.md
  CODEX_GEMINI_REVIEW_GUIDE.md
  CODEX_GEMINI_REVIEW_GUIDE_CN.md
  CODEX_POLICY_AUDIT.md
  COPILOT_CLI_ADAPTATION.md
  CURSOR_ADAPTATION.md
  CUSTOMIZATION.md
  CUSTOMIZATION_CN.md
  GPU_SETUP.md
  GPU_SETUP_CN.md
  LLM_API_MIX_MATCH_GUIDE.md
  MANUAL_REVIEW_GUIDE.md
  MANUAL_REVIEW_GUIDE_CN.md
  MINIMAX_MCP_GUIDE.md
  MODELSCOPE_GUIDE.md
  … 24 more files
mcp-servers/  (6 files)
  antigravity-exec/  (2 files)
    README.md
    aris-antigravity-review.md
  claude-review/  (1 files)
    run_with_claude_aws.sh
  feishu-bridge/  (1 files)
    requirements.txt
  llm-chat/  (1 files)
    requirements.txt
  minimax-chat/  (1 files)
    requirements.txt
skills/  (2 files)
  paper-poster-html/  (2 files)
    scripts/  (2 files)
      … 2 files under this directory
tests/  (1 files)
  __init__.py
tools/  (1 files)
  requirements-codex-policy-audit.txt
.env.example
.gitattributes
.gitignore
AGENT_GUIDE.md
CONTRIBUTING.md
CONTRIBUTING_CN.md
LICENSE
SETUP_GUIDE.md
SETUP_GUIDE_CN.md
```

## Entry points

- [aris-monitor/scanner.py:444](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9f30e834d24a337dbdd06fb20a1150d4376dfa59/aris-monitor/scanner.py#L444)
- [aris-monitor/ticker.py:80](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9f30e834d24a337dbdd06fb20a1150d4376dfa59/aris-monitor/ticker.py#L80)
- [aris-monitor/widget.py:371](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/9f30e834d24a337dbdd06fb20a1150d4376dfa59/aris-monitor/widget.py#L371)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| aris-monitor package | library | Observed | Groups 3 file(s) under aris-monitor package (observed from repository paths and static analysis). Observed top-level functions: _pid_tty, focus. |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: FloatWidget, Info, Session. Observed top-level functions: _as_int, _cwd_to_project_slug, _… |
| mcp-servers package | library | Observed | Groups 1 file(s) under mcp-servers package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 2 file(s) under skills package (observed from repository paths and static analysis). Observed top-level functions: ascii_safe. |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.env.example` (config)
- `.github/workflows/check-skills-inventory.yml` (ci)
- `.github/workflows/lint-skills-helpers.yml` (ci)
- `.github/workflows/test-install-aris-ps1.yml` (ci)
- `.github/workflows/test-suite.yml` (ci)
- `.github/workflows/verify-codex-policy-audit.yml` (ci)
- `docs/ARIS_INTRO.review.json` (config)
- `docs/tutorials/3d_generation_tutorial.review.json` (config)
- `docs/tutorials/agent_foundations_tutorial.review.json` (config)
- `docs/tutorials/agentic_rl_tutorial.review.json` (config)
- `docs/tutorials/attention_tutorial.review.json` (config)
- `docs/tutorials/diffusion_distillation_tutorial.review.json` (config)
- `docs/tutorials/diffusion_foundations_tutorial.review.json` (config)
- `docs/tutorials/diffusion_post_training_tutorial.review.json` (config)
- `docs/tutorials/distributed_training_tutorial.review.json` (config)
- `docs/tutorials/flow_matching_tutorial.review.json` (config)
- `docs/tutorials/image_generation_systems_tutorial.review.json` (config)
- `docs/tutorials/kl_divergence_rlhf_tutorial.review.json` (config)
- `docs/tutorials/kv_cache_speculative_decoding_tutorial.review.json` (config)
- `docs/tutorials/llm_opd_tutorial.review.json` (config)
- `docs/tutorials/long_context_rope_yarn_mla_tutorial.review.json` (config)
- `docs/tutorials/moe_tutorial.review.json` (config)
- `docs/tutorials/multi_agent_long_horizon_tutorial.review.json` (config)
- `docs/tutorials/quantization_tutorial.review.json` (config)
- `docs/tutorials/reasoning_models_tutorial.review.json` (config)
- `docs/tutorials/rlhf_dpo_grpo_ppo_tutorial.review.json` (config)
- `docs/tutorials/self_evolving_agents_tutorial.review.json` (config)
- `docs/tutorials/vae_vqvae_vqgan_tutorial.review.json` (config)
- `docs/tutorials/video_generation_tutorial.review.json` (config)
- `docs/tutorials/vlm_multimodal_tutorial.review.json` (config)
- `mcp-servers/feishu-bridge/requirements.txt` (manifest)
- `mcp-servers/llm-chat/requirements.txt` (manifest)
- `mcp-servers/minimax-chat/requirements.txt` (manifest)
- `tools/requirements-codex-policy-audit.txt` (manifest)

## Top-level layout

- `docs` — 164 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 7 analysed file(s)
- `aris-monitor` — 7 analysed file(s)
- `mcp-servers` — 6 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `skills` — 2 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `agents` — 1 analysed file(s)
- `commands` — 1 analysed file(s)
- `tests` — 1 analysed file(s)
- `tools` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `9f30e834d24a337dbdd06fb20a1150d4376dfa59` is the revision these paths and observations refer to.
