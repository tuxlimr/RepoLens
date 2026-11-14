# Project structure: awesome-opencode/awesome-opencode

**Analysed commit:** `c125252fe11f2021c58545e705d4f69d5c6092f0`

**Commit reference:** [c125252fe11f2021c58545e705d4f69d5c6092f0](https://github.com/awesome-opencode/awesome-opencode/commit/c125252fe11f2021c58545e705d4f69d5c6092f0)

**Tree at this commit:** [awesome-opencode/awesome-opencode@c125252fe11f](https://github.com/awesome-opencode/awesome-opencode/tree/c125252fe11f2021c58545e705d4f69d5c6092f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | awesome-opencode/awesome-opencode |
| Description | A curated list of awesome plugins, themes, agents, projects, and resources for https://opencode.ai |
| Stars | 10991 |
| Forks | 1130 |
| Licence | CC0-1.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `c125252fe11f2021c58545e705d4f69d5c6092f0` |
| Retrieved at | 2026-11-14T19:12:27.048604+00:00 |
| Files in this snapshot | 224 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    generate-readme.yml
    validate-pr.yml
  PULL_REQUEST_TEMPLATE.md
data/  (207 files)
  agents/  (7 files)
    claude-subagents.yaml
    deliberation.yaml
    gem-team.yaml
    nerv.yaml
    opencode-agent-orchestration-kit.yaml
    opencode-agents.yaml
    opencode-auto-resume.yaml
  examples/  (7 files)
    README.md
    agent.yaml
    fork.yaml
    plugin.yaml
    project.yaml
    resource.yaml
    theme.yaml
  plugins/  (96 files)
    aerovato-operator-memory.yaml
    agent-memory.yaml
    agent-notifications.yaml
    agent-skills-jdt.yaml
    agy-auth.yaml
    aidevops.yaml
    antigravity-auth.yaml
    basemind.yaml
    beads-plugin.yaml
    brhp.yaml
    bro.yaml
    cache-stats.yaml
    caspian-opencode-plugin.yaml
    cc-safety-net.yaml
    chisle.yaml
    cli-subagent-output.yaml
    codemem.yaml
    command-inject.yaml
    contextstream.yaml
    deja.yaml
    ditto.yaml
    dodo-payments.yaml
    dynamic-context-pruning.yaml
    envsitter-guard.yaml
    … 72 more files
  projects/  (86 files)
    ag-local-bridge.yaml
    agent-harness.yaml
    agent-manager.yaml
    agent-of-empires.yaml
    agent-sessions.yaml
    agent-teams.yaml
    agentbox.yaml
    agentdeals.yaml
    agentglass.yaml
    agenttrace.yaml
    aionui.yaml
    assay.yaml
    ax.yaml
    beads.yaml
    bifrost.yaml
    brood-box.yaml
    bx.yaml
    call-me.yaml
    calyx.yaml
    caprock.yaml
    claudexor.yaml
    clawmetry.yaml
    cli-proxy-api.yaml
    codenomad.yaml
    … 62 more files
  resources/  (9 files)
    coding-agent-orchestration.yaml
    debug-log-to-text-file.yaml
    gotty.yaml
    jev-social.yaml
    lwc.yaml
    my-opencode-deepseek-config.yaml
    qmenpowers.yaml
    runapi-mcp.yaml
    tapetide-mcp.yaml
  themes/  (1 files)
    opencode-light-themes.yaml
  schema.json
docs/  (1 files)
  schema-design.md
scripts/  (6 files)
  utils/  (3 files)
    template.js
    validation.js
    yaml.js
  export-json.js
  generate-readme.js
  validate.js
templates/  (1 files)
  README.template.md
.gitignore
LICENSE
README.md
code-of-conduct.md
contributing.md
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 207 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/generate-readme.yml` (ci)
- `.github/workflows/validate-pr.yml` (ci)
- `data/agents/claude-subagents.yaml` (config)
- `data/agents/deliberation.yaml` (config)
- `data/agents/gem-team.yaml` (config)
- `data/agents/nerv.yaml` (config)
- `data/agents/opencode-agent-orchestration-kit.yaml` (config)
- `data/agents/opencode-agents.yaml` (config)
- `data/agents/opencode-auto-resume.yaml` (config)
- `data/examples/agent.yaml` (config)
- `data/examples/fork.yaml` (config)
- `data/examples/plugin.yaml` (config)
- `data/examples/project.yaml` (config)
- `data/examples/resource.yaml` (config)
- `data/examples/theme.yaml` (config)
- `data/plugins/aerovato-operator-memory.yaml` (config)
- `data/plugins/agent-memory.yaml` (config)
- `data/plugins/agent-notifications.yaml` (config)
- `data/plugins/agent-skills-jdt.yaml` (config)
- `data/plugins/agy-auth.yaml` (config)
- `data/plugins/aidevops.yaml` (config)
- `data/plugins/antigravity-auth.yaml` (config)
- `data/plugins/basemind.yaml` (config)
- `data/plugins/beads-plugin.yaml` (config)
- `data/plugins/brhp.yaml` (config)
- `data/plugins/bro.yaml` (config)
- `data/plugins/cache-stats.yaml` (config)
- `data/plugins/caspian-opencode-plugin.yaml` (config)
- `data/plugins/cc-safety-net.yaml` (config)
- `data/plugins/chisle.yaml` (config)
- `data/plugins/cli-subagent-output.yaml` (config)
- `data/plugins/codemem.yaml` (config)
- `data/plugins/command-inject.yaml` (config)
- `data/plugins/contextstream.yaml` (config)
- `data/plugins/deja.yaml` (config)
- `data/plugins/ditto.yaml` (config)
- `data/plugins/dodo-payments.yaml` (config)
- `data/plugins/dynamic-context-pruning.yaml` (config)
- `data/plugins/envsitter-guard.yaml` (config)
- `data/plugins/flowdeck.yaml` (config)
- `data/plugins/forloop-planner.yaml` (config)
- `data/plugins/froggy.yaml` (config)
- `data/plugins/gemini-auth.yaml` (config)
- `data/plugins/godmode.yaml` (config)
- `data/plugins/handoff.yaml` (config)
- `data/plugins/honcho.yaml` (config)
- `data/plugins/internet-court.yaml` (config)
- `data/plugins/kibi-opencode.yaml` (config)
- `data/plugins/kilo-auth.yaml` (config)
- `data/plugins/lemma.yaml` (config)
- `data/plugins/llm-proxy.yaml` (config)
- `data/plugins/magic-context.yaml` (config)
- `data/plugins/mem0.yaml` (config)
- `data/plugins/micode.yaml` (config)
- `data/plugins/morph-fast-apply.yaml` (config)
- `data/plugins/neuralyzer.yaml` (config)
- `data/plugins/oh-my-cassette.yaml` (config)
- `data/plugins/oh-my-opencode-slim.yaml` (config)
- `data/plugins/oh-my-opencode.yaml` (config)
- `data/plugins/open-plan-annotator.yaml` (config)
- `data/plugins/opencode-agents-sidebar.yaml` (config)
- `data/plugins/opencode-boffin.yaml` (config)
- `data/plugins/opencode-claude-code-plugin.yaml` (config)
- `data/plugins/opencode-claude-memory.yaml` (config)
- `data/plugins/opencode-cmd-provider.yaml` (config)
- `data/plugins/opencode-cursor.yaml` (config)
- `data/plugins/opencode-dir-tree-tui.yaml` (config)
- `data/plugins/opencode-ensemble.yaml` (config)
- `data/plugins/opencode-failover.yaml` (config)
- `data/plugins/opencode-github-release.yaml` (config)
- `data/plugins/opencode-goopspec.yaml` (config)
- `data/plugins/opencode-gpt-imagegen.yaml` (config)
- `data/plugins/opencode-litellm.yaml` (config)
- `data/plugins/opencode-mem.yaml` (config)
- `data/plugins/opencode-mission-control.yaml` (config)
- `data/plugins/opencode-models-discovery.yaml` (config)
- `data/plugins/opencode-ntfy.sh.yaml` (config)
- `data/plugins/opencode-openai-compact.yaml` (config)
- `data/plugins/opencode-openwork.yaml` (config)
- `data/plugins/opencode-plugin-otel.yaml` (config)
- `data/plugins/opencode-pollinations-plugin.yaml` (config)
- `data/plugins/opencode-pr-signature.yaml` (config)
- `data/plugins/opencode-quota.yaml` (config)
- `data/plugins/opencode-rag.yaml` (config)
- `data/plugins/opencode-review.yaml` (config)
- `data/plugins/opencode-short-term-memory.yaml` (config)
- `data/plugins/opencode-skills-tui.yaml` (config)
- `data/plugins/opencode-snip.yaml` (config)
- `data/plugins/opencode-snippets.yaml` (config)
- `data/plugins/opencode-swarm.yaml` (config)
- `data/plugins/opencode-synced.yaml` (config)
- `data/plugins/opencode-system-prompt-logger.yaml` (config)
- `data/plugins/opencode-telemetry.yaml` (config)
- `data/plugins/opencode-update-notifier.yaml` (config)
- `data/plugins/opencode-usage-monitor.yaml` (config)
- `data/plugins/opencode-visualizer.yaml` (config)
- `data/plugins/orgx-opencode-plugin.yaml` (config)
- `data/plugins/plannotator.yaml` (config)
- `data/plugins/rehydra.yaml` (config)
- `data/plugins/ring-a-bell-example.yaml` (config)
- `data/plugins/simple-memory.yaml` (config)
- `data/plugins/sonarqube.yaml` (config)
- `data/plugins/superpowers.yaml` (config)
- `data/plugins/systematic.yaml` (config)
- `data/plugins/telemetry-dev-opencode.yaml` (config)
- `data/plugins/toon-config.yaml` (config)
- `data/plugins/typeui.yaml` (config)
- `data/plugins/ul-opencode-event.yaml` (config)
- `data/plugins/unmoji.yaml` (config)
- `data/plugins/wakatime.yaml` (config)
- `data/plugins/xquik.yaml` (config)
- `data/projects/ag-local-bridge.yaml` (config)
- `data/projects/agent-harness.yaml` (config)
- `data/projects/agent-manager.yaml` (config)
- `data/projects/agent-of-empires.yaml` (config)
- `data/projects/agent-sessions.yaml` (config)
- `data/projects/agent-teams.yaml` (config)
- `data/projects/agentbox.yaml` (config)
- `data/projects/agentdeals.yaml` (config)
- `data/projects/agentglass.yaml` (config)
- `data/projects/agenttrace.yaml` (config)
- `data/projects/aionui.yaml` (config)
- `data/projects/assay.yaml` (config)
- `data/projects/ax.yaml` (config)
- `data/projects/beads.yaml` (config)
- `data/projects/bifrost.yaml` (config)
- `data/projects/brood-box.yaml` (config)
- `data/projects/bx.yaml` (config)
- `data/projects/call-me.yaml` (config)
- `data/projects/calyx.yaml` (config)
- `data/projects/caprock.yaml` (config)
- `data/projects/claudexor.yaml` (config)
- `data/projects/clawmetry.yaml` (config)
- `data/projects/cli-proxy-api.yaml` (config)
- `data/projects/codenomad.yaml` (config)
- `data/projects/codewalk.yaml` (config)
- `data/projects/crit.yaml` (config)
- `data/projects/dotpals.yaml` (config)
- `data/projects/eval-harness.yaml` (config)
- `data/projects/foreman.yaml` (config)
- `data/projects/forgeo.yaml` (config)
- `data/projects/golembot.yaml` (config)
- `data/projects/handy.yaml` (config)
- `data/projects/happier.yaml` (config)
- `data/projects/hcom.yaml` (config)
- `data/projects/herdr-reviewr.yaml` (config)
- `data/projects/hexis.yaml` (config)
- `data/projects/heym.yaml` (config)
- `data/projects/hipocampo.yaml` (config)
- `data/projects/intentic.yaml` (config)
- `data/projects/ivy-tendril.yaml` (config)
- `data/projects/jailoc.yaml` (config)
- `data/projects/kimaki.yaml` (config)
- `data/projects/kranz.yaml` (config)
- `data/projects/looptroop.yaml` (config)
- `data/projects/nextprob.yaml` (config)
- `data/projects/oc-monitor-share.yaml` (config)
- `data/projects/ocp.yaml` (config)
- `data/projects/octto.yaml` (config)
- `data/projects/ocx.yaml` (config)
- `data/projects/open-agent.yaml` (config)
- `data/projects/open-walnut.yaml` (config)
- `data/projects/openchamber.yaml` (config)
- `data/projects/openclient.yaml` (config)
- `data/projects/opencode-a2a.yaml` (config)
- `data/projects/opencode-handoff-p2p.yaml` (config)
- `data/projects/opencode-kanban.yaml` (config)
- `data/projects/opencode-mobile.yaml` (config)
- `data/projects/opencode-neovim.yaml` (config)
- `data/projects/opencode-profile-router.yaml` (config)
- `data/projects/opencode-sidebar.yaml` (config)
- `data/projects/opencode-telegram-bot.yaml` (config)
- `data/projects/opencode-vim.yaml` (config)
- `data/projects/openspec.yaml` (config)
- `data/projects/opentab.yaml` (config)
- `data/projects/orcareplay.yaml` (config)
- `data/projects/orkas.yaml` (config)
- `data/projects/p4oc.yaml` (config)
- `data/projects/parallel-code.yaml` (config)
- `data/projects/ppt-design-skill.yaml` (config)
- `data/projects/qualitylayer.yaml` (config)
- `data/projects/qwen-audio-agent.yaml` (config)
- `data/projects/redcode.yaml` (config)
- `data/projects/rolecraft.yaml` (config)
- `data/projects/sandbase-cli.yaml` (config)
- `data/projects/self-host.yaml` (config)
- `data/projects/showagent.yaml` (config)
- `data/projects/squirrelscan.yaml` (config)
- `data/projects/supamem.yaml` (config)
- `data/projects/superlocalmemory.yaml` (config)
- `data/projects/swe-mux.yaml` (config)
- `data/projects/tokscale.yaml` (config)
- `data/projects/uizze.yaml` (config)
- `data/projects/universal-llm-proxy.yaml` (config)
- `data/projects/unship.yaml` (config)
- `data/projects/vestige.yaml` (config)
- `data/projects/vibe-kanban.yaml` (config)
- `data/resources/coding-agent-orchestration.yaml` (config)
- `data/resources/debug-log-to-text-file.yaml` (config)
- `data/resources/gotty.yaml` (config)
- `data/resources/jev-social.yaml` (config)
- `data/resources/lwc.yaml` (config)
- `data/resources/my-opencode-deepseek-config.yaml` (config)
- `data/resources/qmenpowers.yaml` (config)
- `data/resources/runapi-mcp.yaml` (config)
- `data/resources/tapetide-mcp.yaml` (config)
- `data/schema.json` (config)
- `data/themes/opencode-light-themes.yaml` (config)
- `package.json` (manifest)

## Top-level layout

- `data` — 207 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 3 analysed file(s)
- `docs` — 1 analysed file(s)
- `templates` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x lockfile excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c125252fe11f2021c58545e705d4f69d5c6092f0` is the revision these paths and observations refer to.
