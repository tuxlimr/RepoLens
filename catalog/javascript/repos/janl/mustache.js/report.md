# Architecture report: janl/mustache.js

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | janl/mustache.js |
| Description | Minimal templating with {{mustaches}} in JavaScript |
| Language | JavaScript |
| Stars | 16723 |
| Licence | MIT |
| Analysed commit / branch | 972fd2b27a036888acfcb60d6119317744fac7ee / master |
| Framework(s) | None detected |
| Files analysed | 249 |
| Components | 4 |

## 2. Architecture in one minute

janl/mustache.js - Minimal templating with {{mustaches}} in JavaScript. This repository was analysed statically from 249 file(s) (0 Python). Detected technologies (observed from imports/manifests): GitHub Actions. Files are grouped into 4 component(s): Configuration and deployment, Core modules, spec package, Tests. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph config_group
        config["Configuration and deployment"]
    end
    subgraph core_group
        core["Core modules"]
    end
    subgraph library_group
        spec["spec package"]
    end
    subgraph test_group
        tests["Tests"]
    end
```

## 4. Main components

### Configuration and deployment (`config`)

- **Kind:** config
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `package.json`
- **Evidence:** [package.json](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/package.json)

### Core modules (`core`)

- **Kind:** core
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under core modules (observed from repository paths and static analysis).
- **Paths:** `mustache.js`
- **Evidence:** [mustache.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/mustache.js)

### spec package (`spec`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under spec package (observed from repository paths and static analysis).
- **Paths:** `spec/_files/bom_as_whitespace.js`
- **Evidence:** [spec/_files/bom_as_whitespace.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/spec/_files/bom_as_whitespace.js)

### Tests (`tests`)

- **Kind:** test
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 219 file(s) under tests (observed from repository paths and static analysis).
- **Paths:** `test/.eslintrc`, `test/_files/ampersand_escape.js`, `test/_files/ampersand_escape.mustache`, `test/_files/ampersand_escape.txt`, `test/_files/apostrophe.js`, `test/_files/apostrophe.mustache`, `test/_files/apostrophe.txt`, `test/_files/array_of_strings.js`, `test/_files/array_of_strings.mustache`, `test/_files/array_of_strings.txt`, `test/_files/avoids_obj_prototype_in_view_cache.js`, `test/_files/avoids_obj_prototype_in_view_cache.mustache`, `test/_files/avoids_obj_prototype_in_view_cache.txt`, `test/_files/backslashes.js`, `test/_files/backslashes.mustache`, `test/_files/backslashes.txt`, `test/_files/bug_11_eating_whitespace.js`, `test/_files/bug_11_eating_whitespace.mustache`, `test/_files/bug_11_eating_whitespace.txt`, `test/_files/bug_length_property.js`, `test/_files/bug_length_property.mustache`, `test/_files/bug_length_property.txt`, `test/_files/changing_delimiters.js`, `test/_files/changing_delimiters.mustache`, `test/_files/changing_delimiters.txt`, `test/_files/check_falsy.js`, `test/_files/check_falsy.mustache`, `test/_files/check_falsy.txt`, `test/_files/cli.cjs`, `test/_files/cli.js`, `test/_files/cli.json`, `test/_files/cli.mustache`, `test/_files/cli.txt`, `test/_files/cli_js_view_with_function.js`, `test/_files/cli_js_view_with_function.mustache`, `test/_files/cli_js_view_with_function.txt`, `test/_files/cli_with_partials.json`, `test/_files/cli_with_partials.mustache`, `test/_files/cli_with_partials.txt`, `test/_files/comments.js`, `test/_files/comments.mustache`, `test/_files/comments.txt`, `test/_files/complex.js`, `test/_files/complex.mustache`, `test/_files/complex.txt`, `test/_files/context_lookup.js`, `test/_files/context_lookup.mustache`, `test/_files/context_lookup.txt`, `test/_files/delimiters.js`, `test/_files/delimiters.mustache`, `test/_files/delimiters.txt`, `test/_files/disappearing_whitespace.js`, `test/_files/disappearing_whitespace.mustache`, `test/_files/disappearing_whitespace.txt`, `test/_files/dot_notation.js`, `test/_files/dot_notation.mustache`, `test/_files/dot_notation.txt`, `test/_files/double_render.js`, `test/_files/double_render.mustache`, `test/_files/double_render.txt`, `test/_files/empty_list.js`, `test/_files/empty_list.mustache`, `test/_files/empty_list.txt`, `test/_files/empty_sections.js`, `test/_files/empty_sections.mustache`, `test/_files/empty_sections.txt`, `test/_files/empty_string.js`, `test/_files/empty_string.mustache`, `test/_files/empty_string.txt`, `test/_files/empty_template.js`, `test/_files/empty_template.mustache`, `test/_files/empty_template.txt`, `test/_files/error_not_found.js`, `test/_files/error_not_found.mustache`, `test/_files/error_not_found.txt`, `test/_files/escaped.js`, `test/_files/escaped.mustache`, `test/_files/escaped.txt`, `test/_files/falsy.js`, `test/_files/falsy.mustache`, `test/_files/falsy.txt`, `test/_files/falsy_array.js`, `test/_files/falsy_array.mustache`, `test/_files/falsy_array.txt`, `test/_files/grandparent_context.js`, `test/_files/grandparent_context.mustache`, `test/_files/grandparent_context.txt`, `test/_files/higher_order_sections.js`, `test/_files/higher_order_sections.mustache`, `test/_files/higher_order_sections.txt`, `test/_files/implicit_iterator.js`, `test/_files/implicit_iterator.mustache`, `test/_files/implicit_iterator.txt`, `test/_files/included_tag.js`, `test/_files/included_tag.mustache`, `test/_files/included_tag.txt`, `test/_files/inverted_section.js`, `test/_files/inverted_section.mustache`, `test/_files/inverted_section.txt`, `test/_files/keys_with_questionmarks.js`, `test/_files/keys_with_questionmarks.mustache`, `test/_files/keys_with_questionmarks.txt`, `test/_files/malicious_template.js`, `test/_files/malicious_template.mustache`, `test/_files/malicious_template.txt`, `test/_files/multiline_comment.js`, `test/_files/multiline_comment.mustache`, `test/_files/multiline_comment.txt`, `test/_files/nested_dot.js`, `test/_files/nested_dot.mustache`, `test/_files/nested_dot.txt`, `test/_files/nested_higher_order_sections.js`, `test/_files/nested_higher_order_sections.mustache`, `test/_files/nested_higher_order_sections.txt`, `test/_files/nested_iterating.js`, `test/_files/nested_iterating.mustache`, `test/_files/nested_iterating.txt`, `test/_files/nesting.js`, `test/_files/nesting.mustache`, `test/_files/nesting.txt`, `test/_files/nesting_same_name.js`, `test/_files/nesting_same_name.mustache`, `test/_files/nesting_same_name.txt`, `test/_files/null_lookup_array.js`, `test/_files/null_lookup_array.mustache`, `test/_files/null_lookup_array.txt`, `test/_files/null_lookup_object.js`, `test/_files/null_lookup_object.mustache`, `test/_files/null_lookup_object.txt`, `test/_files/null_string.js`, `test/_files/null_string.mustache`, `test/_files/null_string.txt`, `test/_files/null_view.js`, `test/_files/null_view.mustache`, `test/_files/null_view.txt`, `test/_files/partial_array.js`, `test/_files/partial_array.mustache`, `test/_files/partial_array.partial`, `test/_files/partial_array.txt`, `test/_files/partial_array_of_partials.js`, `test/_files/partial_array_of_partials.mustache`, `test/_files/partial_array_of_partials.partial`, `test/_files/partial_array_of_partials.txt`, `test/_files/partial_array_of_partials_implicit.js`, `test/_files/partial_array_of_partials_implicit.mustache`, `test/_files/partial_array_of_partials_implicit.partial`, `test/_files/partial_array_of_partials_implicit.txt`, `test/_files/partial_empty.js`, `test/_files/partial_empty.mustache`, `test/_files/partial_empty.partial`, `test/_files/partial_empty.txt`, `test/_files/partial_template.js`, `test/_files/partial_template.mustache`, `test/_files/partial_template.partial`, `test/_files/partial_template.txt`, `test/_files/partial_view.js`, `test/_files/partial_view.mustache`, `test/_files/partial_view.partial`, `test/_files/partial_view.txt`, `test/_files/partial_whitespace.js`, `test/_files/partial_whitespace.mustache`, `test/_files/partial_whitespace.partial`, `test/_files/partial_whitespace.txt`, `test/_files/recursion_with_same_names.js`, `test/_files/recursion_with_same_names.mustache`, `test/_files/recursion_with_same_names.txt`, `test/_files/reuse_of_enumerables.js`, `test/_files/reuse_of_enumerables.mustache`, `test/_files/reuse_of_enumerables.txt`, `test/_files/section_as_context.js`, `test/_files/section_as_context.mustache`, `test/_files/section_as_context.txt`, `test/_files/section_functions_in_partials.js`, `test/_files/section_functions_in_partials.mustache`, `test/_files/section_functions_in_partials.partial`, `test/_files/section_functions_in_partials.txt`, `test/_files/simple.js`, `test/_files/simple.mustache`, `test/_files/simple.txt`, `test/_files/string_as_context.js`, `test/_files/string_as_context.mustache`, `test/_files/string_as_context.txt`, `test/_files/two_in_a_row.js`, `test/_files/two_in_a_row.mustache`, `test/_files/two_in_a_row.txt`, `test/_files/two_sections.js`, `test/_files/two_sections.mustache`, `test/_files/two_sections.txt`, `test/_files/unescaped.js`, `test/_files/unescaped.mustache`, `test/_files/unescaped.txt`, `test/_files/uses_props_from_view_prototype.js`, `test/_files/uses_props_from_view_prototype.mustache`, `test/_files/uses_props_from_view_prototype.txt`, `test/_files/whitespace.js`, `test/_files/whitespace.mustache`, `test/_files/whitespace.txt`, `test/_files/zero_view.js`, `test/_files/zero_view.mustache`, `test/_files/zero_view.txt`, `test/cli-test.js`, `test/context-test.js`, `test/create-browser-suite.js`, `test/helper.js`, `test/module-systems/.eslintrc`, `test/module-systems/_fixtures/amd.html`, `test/module-systems/_fixtures/global-scope.html`, `test/module-systems/browser-test.js`, `test/module-systems/commonjs-test.js`, `test/module-systems/deno-test.ts`, `test/module-systems/esm-test-exports.mjs`, `test/module-systems/esm-test.mjs`, `test/mustache-spec-test.js`, `test/parse-test.js`, `test/partial-test.js`, `test/render-helper.js`, `test/render-test-browser-tmpl.mustache`, `test/render-test.js`, `test/scanner-test.js`
- **Evidence:** [test/.eslintrc](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/.eslintrc); [test/_files/ampersand_escape.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/ampersand_escape.js); [test/_files/ampersand_escape.mustache](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/ampersand_escape.mustache); [test/_files/ampersand_escape.txt](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/ampersand_escape.txt); [test/_files/apostrophe.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/apostrophe.js); [test/_files/apostrophe.mustache](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/apostrophe.mustache); [test/_files/apostrophe.txt](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/apostrophe.txt); [test/_files/array_of_strings.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/array_of_strings.js)

## 5. Execution flow

**Observed** entry point(s):

- [bin/mustache](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/bin/mustache)
- [mustache.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/mustache.js)

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `.eslintrc` - other (531 bytes)
- `.esmrc` - other (288 bytes)
- `.gitignore` - other (200 bytes)
- `.gitmodules` - other (82 bytes)
- `.travis.yml` - ci, YAML (547 bytes)
- `.zuul.yml` - config (191 bytes)
- `CHANGELOG.md` - docs (22306 bytes)
- `LICENSE` - docs (1183 bytes)
- `MIGRATING.md` - docs (1339 bytes)
- `README.md` - docs (16852 bytes)
- `Rakefile` - other (1387 bytes)
- `mustache.js` - source, JavaScript (23522 bytes)
- `package.json` - manifest (2063 bytes)

### `.github`

- `.github/workflows/usage.yml` - ci, YAML (3726 bytes)
- `.github/workflows/verify.yml` - ci, YAML (1829 bytes)

### `bin`

- `bin/mustache` - other (3468 bytes)

### `scripts`

- `scripts/bump-version-in-source` - other (1417 bytes)

### `spec`

- `spec/_files/bom_as_whitespace.js` - source, JavaScript (86 bytes)
- `spec/_files/bom_as_whitespace.mustache` - other (10 bytes)
- `spec/_files/bom_as_whitespace.txt` - docs (16 bytes)

### `test`

- `test/.eslintrc` - test (70 bytes)
- `test/_files/ampersand_escape.js` - test, JavaScript (32 bytes)
- `test/_files/ampersand_escape.mustache` - test (13 bytes)
- `test/_files/ampersand_escape.txt` - test (12 bytes)
- `test/_files/apostrophe.js` - test, JavaScript (39 bytes)
- `test/_files/apostrophe.mustache` - test (20 bytes)
- `test/_files/apostrophe.txt` - test (7 bytes)
- `test/_files/array_of_strings.js` - test, JavaScript (46 bytes)
- `test/_files/array_of_strings.mustache` - test (49 bytes)
- `test/_files/array_of_strings.txt` - test (13 bytes)
- `test/_files/avoids_obj_prototype_in_view_cache.js` - test, JavaScript (67 bytes)
- `test/_files/avoids_obj_prototype_in_view_cache.mustache` - test (21 bytes)
- `test/_files/avoids_obj_prototype_in_view_cache.txt` - test (34 bytes)
- `test/_files/backslashes.js` - test, JavaScript (24 bytes)
- `test/_files/backslashes.mustache` - test (110 bytes)
- `test/_files/backslashes.txt` - test (92 bytes)
- `test/_files/bug_11_eating_whitespace.js` - test, JavaScript (19 bytes)
- `test/_files/bug_11_eating_whitespace.mustache` - test (12 bytes)
- `test/_files/bug_11_eating_whitespace.txt` - test (7 bytes)
- `test/_files/bug_length_property.js` - test, JavaScript (27 bytes)
- `test/_files/bug_length_property.mustache` - test (57 bytes)
- `test/_files/bug_length_property.txt` - test (30 bytes)
- `test/_files/changing_delimiters.js` - test, JavaScript (58 bytes)
- `test/_files/changing_delimiters.mustache` - test (49 bytes)
- `test/_files/changing_delimiters.txt` - test (46 bytes)
- `test/_files/check_falsy.js` - test, JavaScript (119 bytes)
- `test/_files/check_falsy.mustache` - test (31 bytes)
- `test/_files/check_falsy.txt` - test (9 bytes)
- `test/_files/cli.cjs` - test, JavaScript (39 bytes)
- `test/_files/cli.js` - test, JavaScript (39 bytes)
- `test/_files/cli.json` - test (23 bytes)
- `test/_files/cli.mustache` - test (23 bytes)
- `test/_files/cli.txt` - test (21 bytes)
- `test/_files/cli_js_view_with_function.js` - test, JavaScript (156 bytes)
- `test/_files/cli_js_view_with_function.mustache` - test (30 bytes)
- `test/_files/cli_js_view_with_function.txt` - test (16 bytes)
- `test/_files/cli_with_partials.json` - test (160 bytes)
- `test/_files/cli_with_partials.mustache` - test (73 bytes)
- `test/_files/cli_with_partials.txt` - test (73 bytes)
- `test/_files/comments.js` - test, JavaScript (67 bytes)
- `test/_files/comments.mustache` - test (65 bytes)
- `test/_files/comments.txt` - test (28 bytes)
- `test/_files/complex.js` - test, JavaScript (414 bytes)
- `test/_files/complex.mustache` - test (262 bytes)
- `test/_files/complex.txt` - test (137 bytes)
- `test/_files/context_lookup.js` - test, JavaScript (78 bytes)
- `test/_files/context_lookup.mustache` - test (49 bytes)
- `test/_files/context_lookup.txt` - test (2 bytes)
- `test/_files/delimiters.js` - test, JavaScript (183 bytes)
- `test/_files/delimiters.mustache` - test (87 bytes)
- `test/_files/delimiters.txt` - test (135 bytes)
- `test/_files/disappearing_whitespace.js` - test, JavaScript (36 bytes)
- `test/_files/disappearing_whitespace.mustache` - test (40 bytes)
- `test/_files/disappearing_whitespace.txt` - test (6 bytes)
- `test/_files/dot_notation.js` - test, JavaScript (422 bytes)
- `test/_files/dot_notation.mustache` - test (678 bytes)
- `test/_files/dot_notation.txt` - test (401 bytes)
- `test/_files/double_render.js` - test, JavaScript (52 bytes)
- `test/_files/double_render.mustache` - test (24 bytes)
- `test/_files/double_render.txt` - test (8 bytes)
- `test/_files/empty_list.js` - test, JavaScript (18 bytes)
- `test/_files/empty_list.mustache` - test (46 bytes)
- `test/_files/empty_list.txt` - test (20 bytes)
- `test/_files/empty_sections.js` - test, JavaScript (6 bytes)
- `test/_files/empty_sections.mustache` - test (36 bytes)
- `test/_files/empty_sections.txt` - test (4 bytes)
- `test/_files/empty_string.js` - test, JavaScript (73 bytes)
- `test/_files/empty_string.mustache` - test (51 bytes)
- `test/_files/empty_string.txt` - test (13 bytes)
- `test/_files/empty_template.js` - test, JavaScript (6 bytes)
- `test/_files/empty_template.mustache` - test (52 bytes)
- `test/_files/empty_template.txt` - test (52 bytes)
- `test/_files/error_not_found.js` - test, JavaScript (16 bytes)
- `test/_files/error_not_found.mustache` - test (7 bytes)
- `test/_files/error_not_found.txt` - test (0 bytes)
- `test/_files/escaped.js` - test, JavaScript (108 bytes)
- `test/_files/escaped.mustache` - test (76 bytes)
- `test/_files/escaped.txt` - test (108 bytes)
- `test/_files/falsy.js` - test, JavaScript (115 bytes)
- `test/_files/falsy.mustache` - test (436 bytes)
- `test/_files/falsy.txt` - test (109 bytes)
- `test/_files/falsy_array.js` - test, JavaScript (143 bytes)
- `test/_files/falsy_array.mustache` - test (70 bytes)
- `test/_files/falsy_array.txt` - test (101 bytes)
- `test/_files/grandparent_context.js` - test, JavaScript (371 bytes)
- `test/_files/grandparent_context.mustache` - test (183 bytes)
- `test/_files/grandparent_context.txt` - test (206 bytes)
- `test/_files/higher_order_sections.js` - test, JavaScript (190 bytes)
- `test/_files/higher_order_sections.mustache` - test (35 bytes)
- `test/_files/higher_order_sections.txt` - test (44 bytes)
- `test/_files/implicit_iterator.js` - test, JavaScript (86 bytes)
- `test/_files/implicit_iterator.mustache` - test (198 bytes)
- `test/_files/implicit_iterator.txt` - test (90 bytes)
- `test/_files/included_tag.js` - test, JavaScript (37 bytes)
- `test/_files/included_tag.mustache` - test (28 bytes)
- `test/_files/included_tag.txt` - test (37 bytes)
- `test/_files/inverted_section.js` - test, JavaScript (21 bytes)
- `test/_files/inverted_section.mustache` - test (97 bytes)
- `test/_files/inverted_section.txt` - test (20 bytes)
- `test/_files/keys_with_questionmarks.js` - test, JavaScript (42 bytes)
- `test/_files/keys_with_questionmarks.mustache` - test (41 bytes)
- `test/_files/keys_with_questionmarks.txt` - test (10 bytes)
- `test/_files/malicious_template.js` - test, JavaScript (6 bytes)
- `test/_files/malicious_template.mustache` - test (203 bytes)
- `test/_files/malicious_template.txt` - test (2 bytes)
- `test/_files/multiline_comment.js` - test, JavaScript (6 bytes)
- `test/_files/multiline_comment.mustache` - test (52 bytes)
- `test/_files/multiline_comment.txt` - test (13 bytes)
- `test/_files/nested_dot.js` - test, JavaScript (21 bytes)
- `test/_files/nested_dot.mustache` - test (29 bytes)
- `test/_files/nested_dot.txt` - test (11 bytes)
- `test/_files/nested_higher_order_sections.js` - test, JavaScript (150 bytes)
- `test/_files/nested_higher_order_sections.mustache` - test (61 bytes)
- `test/_files/nested_higher_order_sections.txt` - test (25 bytes)
- `test/_files/nested_iterating.js` - test, JavaScript (78 bytes)
- `test/_files/nested_iterating.mustache` - test (55 bytes)
- `test/_files/nested_iterating.txt` - test (7 bytes)
- `test/_files/nesting.js` - test, JavaScript (70 bytes)
- `test/_files/nesting.mustache` - test (46 bytes)
- `test/_files/nesting.txt` - test (18 bytes)
- `test/_files/nesting_same_name.js` - test, JavaScript (80 bytes)
- `test/_files/nesting_same_name.mustache` - test (54 bytes)
- `test/_files/nesting_same_name.txt` - test (9 bytes)
- `test/_files/null_lookup_array.js` - test, JavaScript (148 bytes)
- `test/_files/null_lookup_array.mustache` - test (77 bytes)
- `test/_files/null_lookup_array.txt` - test (50 bytes)
- `test/_files/null_lookup_object.js` - test, JavaScript (480 bytes)
- `test/_files/null_lookup_object.mustache` - test (506 bytes)
- `test/_files/null_lookup_object.txt` - test (177 bytes)
- `test/_files/null_string.js` - test, JavaScript (137 bytes)
- `test/_files/null_string.mustache` - test (103 bytes)
- `test/_files/null_string.txt` - test (63 bytes)
- `test/_files/null_view.js` - test, JavaScript (38 bytes)
- `test/_files/null_view.mustache` - test (54 bytes)
- `test/_files/null_view.txt` - test (15 bytes)
- `test/_files/partial_array.js` - test, JavaScript (37 bytes)
- `test/_files/partial_array.mustache` - test (12 bytes)
- `test/_files/partial_array.partial` - test (65 bytes)
- `test/_files/partial_array.txt` - test (51 bytes)
- `test/_files/partial_array_of_partials.js` - test, JavaScript (79 bytes)
- `test/_files/partial_array_of_partials.mustache` - test (59 bytes)
- `test/_files/partial_array_of_partials.partial` - test (6 bytes)
- `test/_files/partial_array_of_partials.txt` - test (28 bytes)
- `test/_files/partial_array_of_partials_implicit.js` - test, JavaScript (39 bytes)
- `test/_files/partial_array_of_partials_implicit.mustache` - test (59 bytes)
- `test/_files/partial_array_of_partials_implicit.partial` - test (6 bytes)
- `test/_files/partial_array_of_partials_implicit.txt` - test (28 bytes)
- `test/_files/partial_empty.js` - test, JavaScript (16 bytes)
- `test/_files/partial_empty.mustache` - test (25 bytes)
- `test/_files/partial_empty.partial` - test (0 bytes)
- `test/_files/partial_empty.txt` - test (6 bytes)
- `test/_files/partial_template.js` - test, JavaScript (76 bytes)
- `test/_files/partial_template.mustache` - test (32 bytes)
- `test/_files/partial_template.partial` - test (18 bytes)
- `test/_files/partial_template.txt` - test (33 bytes)
- `test/_files/partial_view.js` - test, JavaScript (250 bytes)
- `test/_files/partial_view.mustache` - test (57 bytes)
- `test/_files/partial_view.partial` - test (105 bytes)
- `test/_files/partial_view.txt` - test (110 bytes)
- `test/_files/partial_whitespace.js` - test, JavaScript (250 bytes)
- `test/_files/partial_whitespace.mustache` - test (65 bytes)
- `test/_files/partial_whitespace.partial` - test (113 bytes)
- `test/_files/partial_whitespace.txt` - test (110 bytes)
- `test/_files/recursion_with_same_names.js` - test, JavaScript (116 bytes)
- `test/_files/recursion_with_same_names.mustache` - test (75 bytes)
- `test/_files/recursion_with_same_names.txt` - test (29 bytes)
- `test/_files/reuse_of_enumerables.js` - test, JavaScript (77 bytes)
- `test/_files/reuse_of_enumerables.mustache` - test (90 bytes)
- `test/_files/reuse_of_enumerables.txt` - test (36 bytes)
- `test/_files/section_as_context.js` - test, JavaScript (184 bytes)
- `test/_files/section_as_context.mustache` - test (144 bytes)
- `test/_files/section_as_context.txt` - test (131 bytes)
- `test/_files/section_functions_in_partials.js` - test, JavaScript (120 bytes)
- `test/_files/section_functions_in_partials.mustache` - test (37 bytes)
- `test/_files/section_functions_in_partials.partial` - test (30 bytes)
- `test/_files/section_functions_in_partials.txt` - test (42 bytes)
- `test/_files/simple.js` - test, JavaScript (132 bytes)
- `test/_files/simple.mustache` - test (106 bytes)
- `test/_files/simple.txt` - test (64 bytes)
- `test/_files/string_as_context.js` - test, JavaScript (49 bytes)
- `test/_files/string_as_context.mustache` - test (64 bytes)
- `test/_files/string_as_context.txt` - test (58 bytes)
- `test/_files/two_in_a_row.js` - test, JavaScript (44 bytes)
- `test/_files/two_in_a_row.mustache` - test (24 bytes)
- `test/_files/two_in_a_row.txt` - test (14 bytes)
- `test/_files/two_sections.js` - test, JavaScript (6 bytes)
- `test/_files/two_sections.mustache` - test (36 bytes)
- `test/_files/two_sections.txt` - test (0 bytes)
- `test/_files/unescaped.js` - test, JavaScript (77 bytes)
- `test/_files/unescaped.mustache` - test (33 bytes)
- `test/_files/unescaped.txt` - test (22 bytes)
- `test/_files/uses_props_from_view_prototype.js` - test, JavaScript (531 bytes)
- `test/_files/uses_props_from_view_prototype.mustache` - test (88 bytes)
- `test/_files/uses_props_from_view_prototype.txt` - test (22 bytes)
- `test/_files/whitespace.js` - test, JavaScript (40 bytes)
- `test/_files/whitespace.mustache` - test (21 bytes)
- `test/_files/whitespace.txt` - test (15 bytes)
- `test/_files/zero_view.js` - test, JavaScript (23 bytes)
- `test/_files/zero_view.mustache` - test (24 bytes)
- `test/_files/zero_view.txt` - test (6 bytes)
- `test/cli-test.js` - test, JavaScript (5852 bytes)
- `test/context-test.js` - test, JavaScript (1748 bytes)
- `test/create-browser-suite.js` - test, JavaScript (455 bytes)
- `test/helper.js` - test, JavaScript (753 bytes)
- `test/module-systems/.eslintrc` - test (82 bytes)
- `test/module-systems/_fixtures/amd.html` - test (726 bytes)
- `test/module-systems/_fixtures/global-scope.html` - test (293 bytes)
- `test/module-systems/browser-test.js` - test, JavaScript (1690 bytes)
- `test/module-systems/commonjs-test.js` - test, JavaScript (222 bytes)
- `test/module-systems/deno-test.ts` - test, TypeScript (340 bytes)
- `test/module-systems/esm-test-exports.mjs` - test, JavaScript (212 bytes)
- `test/module-systems/esm-test.mjs` - test, JavaScript (225 bytes)
- `test/mustache-spec-test.js` - test, JavaScript (2465 bytes)
- `test/parse-test.js` - test, JavaScript (10694 bytes)
- `test/partial-test.js` - test, JavaScript (6554 bytes)
- `test/render-helper.js` - test, JavaScript (1395 bytes)
- `test/render-test-browser-tmpl.mustache` - test (1024 bytes)
- `test/render-test.js` - test, JavaScript (9221 bytes)
- `test/scanner-test.js` - test, JavaScript (2472 bytes)

### `wrappers`

- `wrappers/dojo/mustache.js.post` - other (58 bytes)
- `wrappers/dojo/mustache.js.pre` - other (192 bytes)
- `wrappers/jquery/mustache.js.post` - other (359 bytes)
- `wrappers/jquery/mustache.js.pre` - other (141 bytes)
- `wrappers/mootools/mustache.js.post` - other (128 bytes)
- `wrappers/mootools/mustache.js.pre` - other (14 bytes)
- `wrappers/qooxdoo/mustache.js.post` - other (184 bytes)
- `wrappers/qooxdoo/mustache.js.pre` - other (6376 bytes)
- `wrappers/yui3/mustache.js.post` - other (45 bytes)
- `wrappers/yui3/mustache.js.pre` - other (34 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| GitHub Actions | ci | Observed | 0.90 | [.github/workflows/usage.yml](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/.github/workflows/usage.yml); [.github/workflows/verify.yml](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/.github/workflows/verify.yml) |

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `.github/workflows/usage.yml` (ci)
- `.github/workflows/verify.yml` (ci)
- `.travis.yml` (ci)
- `.zuul.yml` (config)
- `package.json` (manifest)

## 10. Design observations

- Tests are present alongside source code (Observed from test file paths).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

## 12. Source references

- [.github/workflows/usage.yml](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/.github/workflows/usage.yml)
- [.github/workflows/verify.yml](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/.github/workflows/verify.yml)
- [bin/mustache](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/bin/mustache)
- [mustache.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/mustache.js)
- [package.json](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/package.json)
- [spec/_files/bom_as_whitespace.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/spec/_files/bom_as_whitespace.js)
- [test/.eslintrc](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/.eslintrc)
- [test/_files/ampersand_escape.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/ampersand_escape.js)
- [test/_files/ampersand_escape.mustache](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/ampersand_escape.mustache)
- [test/_files/ampersand_escape.txt](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/ampersand_escape.txt)
- [test/_files/apostrophe.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/apostrophe.js)
- [test/_files/apostrophe.mustache](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/apostrophe.mustache)
- [test/_files/apostrophe.txt](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/apostrophe.txt)
- [test/_files/array_of_strings.js](https://github.com/janl/mustache.js/blob/972fd2b27a036888acfcb60d6119317744fac7ee/test/_files/array_of_strings.js)
