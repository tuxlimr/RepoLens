# Project structure: sebastianruder/NLP-progress

**Analysed commit:** `379f03ff7568b18bd9843490b84c94679f880a79`

**Commit reference:** [379f03ff7568b18bd9843490b84c94679f880a79](https://github.com/sebastianruder/NLP-progress/commit/379f03ff7568b18bd9843490b84c94679f880a79)

**Tree at this commit:** [sebastianruder/NLP-progress@379f03ff7568](https://github.com/sebastianruder/NLP-progress/tree/379f03ff7568b18bd9843490b84c94679f880a79)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sebastianruder/NLP-progress |
| Description | Repository to track the progress in Natural Language Processing (NLP), including the datasets and the current state-of-the-art for the most common NLP tasks. |
| Stars | 22954 |
| Forks | 3587 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `379f03ff7568b18bd9843490b84c94679f880a79` |
| Retrieved at | 2026-11-14T19:07:51.344378+00:00 |
| Files in this snapshot | 79 |

## Directory tree

```text
_includes/  (2 files)
  chart.html
  table.html
arabic/  (1 files)
  language_modeling.md
bengali/  (4 files)
  emotion_detection.md
  part_of_speech_tagging.md
  question_answering.md
  sentiment_analysis.md
chinese/  (3 files)
  chinese.md
  chinese_word_segmentation.md
  question_answering.md
english/  (39 files)
  automatic_speech_recognition.md
  ccg.md
  common_sense.md
  constituency_parsing.md
  coreference_resolution.md
  data_to_text_generation.md
  dependency_parsing.md
  dialogue.md
  domain_adaptation.md
  entity_linking.md
  grammatical_error_correction.md
  information_extraction.md
  intent_detection_slot_filling.md
  keyphrase_extraction_generation.md
  language_modeling.md
  lexical_normalization.md
  machine_translation.md
  missing_elements.md
  multi-task_learning.md
  multimodal.md
  named_entity_recognition.md
  natural_language_inference.md
  paraphrase-generation.md
  part-of-speech_tagging.md
  … 15 more files
french/  (2 files)
  question_answering.md
  summarization.md
german/  (2 files)
  question_answering.md
  summarization.md
hindi/  (1 files)
  hindi.md
korean/  (1 files)
  question_answering.md
nepali/  (1 files)
  nepali.md
persian/  (3 files)
  named_entity_recognition.md
  natural_language_inference.md
  summarization.md
portuguese/  (1 files)
  question_answering.md
russian/  (3 files)
  question_answering.md
  sentiment-analysis.md
  summarization.md
spanish/  (3 files)
  entity_linking.md
  named_entity_recognition.md
  summarization.md
structured/  (3 files)
  README.md
  export.py
  requirements.txt
turkish/  (1 files)
  summarization.md
vietnamese/  (1 files)
  vietnamese.md
.gitignore
CITATION.cff
CNAME
Gemfile
LICENSE
README.md
_config.yml
jekyll_instructions.md
```

## Entry points

- [structured/export.py:465](https://github.com/sebastianruder/NLP-progress/blob/379f03ff7568b18bd9843490b84c94679f880a79/structured/export.py#L465)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: extract_code_links, extract_dataset_desc_and_sota_table, extract_dataset_desc_links, ext… |

## Important files

- `_config.yml` (config)
- `structured/requirements.txt` (manifest)

## Top-level layout

- `english` — 39 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `bengali` — 4 analysed file(s)
- `chinese` — 3 analysed file(s)
- `persian` — 3 analysed file(s)
- `russian` — 3 analysed file(s)
- `spanish` — 3 analysed file(s)
- `structured` — 3 analysed file(s)
- `_includes` — 2 analysed file(s)
- `french` — 2 analysed file(s)
- `german` — 2 analysed file(s)
- `arabic` — 1 analysed file(s)
- `hindi` — 1 analysed file(s)
- `korean` — 1 analysed file(s)
- `nepali` — 1 analysed file(s)
- `portuguese` — 1 analysed file(s)
- `turkish` — 1 analysed file(s)
- `vietnamese` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `379f03ff7568b18bd9843490b84c94679f880a79` is the revision these paths and observations refer to.
