# Project structure: RUCAIBox/LLMSurvey

**Analysed commit:** `4a468e40e417fd3541d190c056e260da322ef4de`

**Commit reference:** [4a468e40e417fd3541d190c056e260da322ef4de](https://github.com/RUCAIBox/LLMSurvey/commit/4a468e40e417fd3541d190c056e260da322ef4de)

**Tree at this commit:** [RUCAIBox/LLMSurvey@4a468e40e417](https://github.com/RUCAIBox/LLMSurvey/tree/4a468e40e417fd3541d190c056e260da322ef4de)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | RUCAIBox/LLMSurvey |
| Description | The official GitHub page for the survey paper "A Survey of Large Language Models". |
| Stars | 12229 |
| Forks | 929 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `4a468e40e417fd3541d190c056e260da322ef4de` |
| Retrieved at | 2026-11-14T19:10:15.875662+00:00 |
| Files in this snapshot | 243 |

## Directory tree

```text
Experiments/  (241 files)
  HumanAlignment/  (31 files)
    HaluEval/  (6 files)
      … 6 files under this directory
    metric/  (8 files)
      … 8 files under this directory
    model/  (11 files)
      … 11 files under this directory
    README.md
    eval_Crows_Pairs.sh
    eval_RealToxityPrompts.sh
    eval_TruthfulQA.sh
    eval_WinoGender.sh
    requirements.txt
  InstructTuning/  (37 files)
    auto_eval/  (2 files)
      … 2 files under this directory
    bbh/  (21 files)
      … 21 files under this directory
    mmlu/  (9 files)
      … 9 files under this directory
    README.md
    requirements.txt
    test.sh
    train.py
    train.sh
  KnowledgeReasoning/  (7 files)
    data/  (1 files)
      … 1 files under this directory
    ChatGPT.py
    Claude.py
    davinci-002.py
    davinci-003.py
    get_response.py
    run_all_models.sh
  KnowledgeUtilization/  (9 files)
    WikiFact/  (6 files)
      … 6 files under this directory
    README.md
    requirements.txt
    test_wikifact.sh
  LanguageGeneration/  (25 files)
    HumanEval/  (3 files)
      … 3 files under this directory
    LAMBADA/  (4 files)
      … 4 files under this directory
    WMT22/  (6 files)
      … 6 files under this directory
    XSum/  (6 files)
      … 6 files under this directory
    README.md
    requirements.txt
    test_humaneval.sh
    test_lambada.sh
    test_wmt.sh
    test_xsum.sh
  MathematicalReasoning/  (19 files)
    demo/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    claude.py
    data_process.py
    do_gsm8k.py
    do_math.py
    evaluate.py
    evaluate_falcon.py
    prompt_pattern.py
    readme.md
    solve_claude.py
    solve_text_002.py
    solve_text_003.py
    solve_turbo.py
    test_falcon_gsm8k.py
    test_falcon_math.py
  SymbolicReasoning/  (20 files)
    dataset/  (4 files)
      … 4 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    claude.py
    data_process.py
    do_color.py
    do_penguins.py
    evaluate_color.py
    evaluate_penguins.py
    prompt_pattern.py
    readme.md
    solve_claude.py
    solve_text_002.py
    solve_text_003.py
    solve_turbo.py
    test_falcon_color.py
    test_falcon_penguins.py
  ToolManipulation/  (92 files)
    Gorilla/  (80 files)
      … 80 files under this directory
    HotPotQA/  (11 files)
      … 11 files under this directory
    README.md
  README.md
Prompts/  (1 files)
  README.md
README.md
```

## Entry points

- [Experiments/InstructTuning/bbh/src/main.py:107](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/InstructTuning/bbh/src/main.py#L107)
- [Experiments/HumanAlignment/HaluEval/claude_halu.py:9](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/HaluEval/claude_halu.py#L9)
- [Experiments/HumanAlignment/HaluEval/open-source_model.py:106](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/HaluEval/open-source_model.py#L106)
- [Experiments/HumanAlignment/HaluEval/openai_gpt.py:123](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/HaluEval/openai_gpt.py#L123)
- [Experiments/HumanAlignment/metric/Winogender.py:89](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/Winogender.py#L89)
- [Experiments/HumanAlignment/metric/cal_crows_res.py:43](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/cal_crows_res.py#L43)
- [Experiments/HumanAlignment/metric/cal_toxicity_score.py:24](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/cal_toxicity_score.py#L24)
- [Experiments/HumanAlignment/metric/cal_truth_res.py:35](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/cal_truth_res.py#L35)
- [Experiments/HumanAlignment/metric/cal_wino_res.py:24](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/cal_wino_res.py#L24)
- [Experiments/HumanAlignment/metric/crows_pairs.py:42](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/crows_pairs.py#L42)
- [Experiments/HumanAlignment/metric/eval_truthfulqa.py:109](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/eval_truthfulqa.py#L109)
- [Experiments/HumanAlignment/metric/real-toxicity-prompts.py:51](https://github.com/RUCAIBox/LLMSurvey/blob/4a468e40e417fd3541d190c056e260da322ef4de/Experiments/HumanAlignment/metric/real-toxicity-prompts.py#L51)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 29 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Model. |
| Application entry point | entrypoint | Observed | Groups 87 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: CausalModel, ChatGLMModel, ChatGPTDecoder,… |
| Experiments package | library | Observed | Groups 67 file(s) under experiments package (observed from repository paths and static analysis). Observed top-level classes: Autotuner, BBH3kBenchmark, ChatGPTModel, DataArguments, DummyModel, FeverWrapper. Observed to… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 19 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: clean, g, get_answer_boxed, load_from_json, load_multi_line_json, make_query. |

## Important files

- `Experiments/HumanAlignment/HaluEval/requirements.txt` (manifest)
- `Experiments/HumanAlignment/requirements.txt` (manifest)
- `Experiments/InstructTuning/bbh/config/benchmark/bbh10k.yaml` (config)
- `Experiments/InstructTuning/bbh/config/model/chatgpt.yaml` (config)
- `Experiments/InstructTuning/bbh/config/model/dummy.yaml` (config)
- `Experiments/InstructTuning/bbh/config/model/llama.yaml` (config)
- `Experiments/InstructTuning/bbh/config/model/local.yaml` (config)
- `Experiments/InstructTuning/bbh/config/model/openai.yaml` (config)
- `Experiments/InstructTuning/bbh/output/bbh10kbenchmark/llama-model_english.json` (config)
- `Experiments/InstructTuning/requirements.txt` (manifest)
- `Experiments/KnowledgeUtilization/requirements.txt` (manifest)
- `Experiments/LanguageGeneration/requirements.txt` (manifest)
- `Experiments/MathematicalReasoning/demo/aqua.json` (config)
- `Experiments/MathematicalReasoning/demo/gsm8k.json` (config)
- `Experiments/MathematicalReasoning/demo/math.json` (config)
- `Experiments/SymbolicReasoning/dataset/penguins/test.json` (config)
- `Experiments/ToolManipulation/Gorilla/data/apizoo/shawnharmsen1.json` (config)
- `Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/.github/workflows/ci.yml` (ci)
- `Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/Cargo.toml` (manifest)
- `Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/package.json` (manifest)
- `Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/src/grammar.json` (config)
- `Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/src/node-types.json` (config)
- `Experiments/ToolManipulation/Gorilla/inference/requirements.txt` (manifest)
- `Experiments/ToolManipulation/Gorilla/requirements.txt` (manifest)
- `Experiments/ToolManipulation/HotPotQA/base_config.yaml` (config)
- `Experiments/ToolManipulation/HotPotQA/prompts/alfworld.json` (config)
- `Experiments/ToolManipulation/HotPotQA/prompts/alfworld_3prompts.json` (config)
- `Experiments/ToolManipulation/HotPotQA/prompts/fever.json` (config)
- `Experiments/ToolManipulation/HotPotQA/prompts/prompts_naive.json` (config)

## Top-level layout

- `Experiments` — 241 analysed file(s)
- `(root files)` — 1 analysed file(s)
- `Prompts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x vendored/generated directory excluded).
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/compound-statement-without-trailing-newline.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/crlf-line-endings.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/mixed-spaces-tabs.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/multiple-newlines.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/python2-grammar-crlf.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/python2-grammar.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/python3.8_grammar.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/simple-statements-without-trailing-newline.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/examples/trailing-whitespace.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File Experiments/ToolManipulation/Gorilla/eval/eval-scripts/codebleu/parser/tree-sitter-python/test/highlight/pattern_matching.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4a468e40e417fd3541d190c056e260da322ef4de` is the revision these paths and observations refer to.
