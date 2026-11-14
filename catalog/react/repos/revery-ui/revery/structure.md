# Project structure: revery-ui/revery

**Analysed commit:** `141f70f69d6abd69674b46d805a783411b38cd79`

**Commit reference:** [141f70f69d6abd69674b46d805a783411b38cd79](https://github.com/revery-ui/revery/commit/141f70f69d6abd69674b46d805a783411b38cd79)

**Tree at this commit:** [revery-ui/revery@141f70f69d6a](https://github.com/revery-ui/revery/tree/141f70f69d6abd69674b46d805a783411b38cd79)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | revery-ui/revery |
| Description | :zap: Native, high-performance, cross-platform desktop apps - built with Reason! |
| Stars | 8030 |
| Forks | 194 |
| Licence | MIT |
| Language | Reason |
| Default branch | master |
| Analysed commit | `141f70f69d6abd69674b46d805a783411b38cd79` |
| Retrieved at | 2026-11-14T19:13:43.045946+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.ci/  (10 files)
  .gitattributes
  create-docs.yml
  esy-bench.yml
  esy-build-steps.yml
  esy-check-hygiene.yml
  format.sh
  publish-build-cache.yml
  publish-release.yml
  restore-build-cache.yml
  use-node.yml
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
assets/  (1 files)
  revery.svg
bench/  (11 files)
  exe/  (2 files)
    Bench.re
    dune
  lib/  (9 files)
    BenchFramework.re
    DrawBench.re
    LayoutBench.re
    NodeUtility.re
    PaintBench.re
    RecalculateBench.re
    SurfaceUtility.re
    ViewNodeBench.re
    dune
bench.esy.lock/  (76 files)
  opam/  (67 files)
    astring.0.8.5/  (1 files)
      … 1 files under this directory
    base-bigarray.base/  (1 files)
      … 1 files under this directory
    base-bytes.base/  (1 files)
      … 1 files under this directory
    base-threads.base/  (1 files)
      … 1 files under this directory
    base-unix.base/  (1 files)
      … 1 files under this directory
    base.v0.14.1/  (1 files)
      … 1 files under this directory
    biniou.1.2.1/  (1 files)
      … 1 files under this directory
    bos.0.2.0/  (1 files)
      … 1 files under this directory
    camomile.1.0.2/  (1 files)
      … 1 files under this directory
    charInfo_width.1.1.0/  (1 files)
      … 1 files under this directory
    conf-pkg-config.2/  (1 files)
      … 1 files under this directory
    cppo.1.6.7/  (1 files)
      … 1 files under this directory
    csexp.1.5.1/  (1 files)
      … 1 files under this directory
    ctypes.0.15.1/  (1 files)
      … 1 files under this directory
    dot-merlin-reader.4.1/  (1 files)
      … 1 files under this directory
    dune-build-info.2.8.5/  (1 files)
      … 1 files under this directory
    dune-configurator.2.8.5/  (1 files)
      … 1 files under this directory
    dune.2.8.5/  (1 files)
      … 1 files under this directory
    easy-format.1.3.2/  (1 files)
      … 1 files under this directory
    fix.20201120/  (1 files)
      … 1 files under this directory
    fmt.0.8.9/  (1 files)
      … 1 files under this directory
    fpath.0.7.3/  (1 files)
      … 1 files under this directory
    integers.0.4.0/  (1 files)
      … 1 files under this directory
    junit.2.0.2/  (1 files)
      … 1 files under this directory
    logs.0.7.0/  (1 files)
      … 1 files under this directory
    lwt.5.4.1/  (1 files)
      … 1 files under this directory
    lwt_ppx.2.0.1/  (1 files)
      … 1 files under this directory
    markup.0.8.2/  (1 files)
      … 1 files under this directory
    menhir.20210419/  (1 files)
      … 1 files under this directory
    menhirLib.20210419/  (1 files)
      … 1 files under this directory
    menhirSdk.20210419/  (1 files)
      … 1 files under this directory
    merlin-extend.0.6/  (1 files)
      … 1 files under this directory
    mmap.1.1.0/  (1 files)
      … 1 files under this directory
    ocaml-compiler-libs.v0.12.3/  (1 files)
      … 1 files under this directory
    ocaml-lsp-server.1.6.1/  (1 files)
      … 1 files under this directory
    ocaml-migrate-parsetree.1.8.0/  (1 files)
      … 1 files under this directory
    ocamlbuild.0.14.0/  (1 files)
      … 1 files under this directory
    ocamlfind.1.9.1/  (1 files)
      … 1 files under this directory
    ocplib-endian.1.1/  (1 files)
      … 1 files under this directory
    pp.1.1.2/  (1 files)
      … 1 files under this directory
    ppx_derivers.1.2.1/  (1 files)
      … 1 files under this directory
    ppx_deriving.4.5/  (1 files)
      … 1 files under this directory
    ppx_optcomp.v0.14.0/  (1 files)
      … 1 files under this directory
    ppx_tools.6.3/  (1 files)
      … 1 files under this directory
    ppx_tools_versioned.5.4.0/  (1 files)
      … 1 files under this directory
    ppx_yojson_conv_lib.v0.14.0/  (1 files)
      … 1 files under this directory
    ppxfind.1.4/  (1 files)
      … 1 files under this directory
    ppxlib.0.15.0/  (1 files)
      … 1 files under this directory
    printbox.0.5/  (1 files)
      … 1 files under this directory
    psq.0.2.0/  (1 files)
      … 1 files under this directory
    ptime.0.8.5/  (1 files)
      … 1 files under this directory
    re.1.9.0/  (1 files)
      … 1 files under this directory
    reason.3.7.0/  (1 files)
      … 1 files under this directory
    result.1.5/  (1 files)
      … 1 files under this directory
    rresult.0.6.0/  (1 files)
      … 1 files under this directory
    seq.base/  (3 files)
      … 3 files under this directory
    sexplib0.v0.14.0/  (1 files)
      … 1 files under this directory
    stdio.v0.14.0/  (1 files)
      … 1 files under this directory
    stdlib-shims.0.3.0/  (1 files)
      … 1 files under this directory
    topkg.1.0.3/  (1 files)
      … 1 files under this directory
    tyxml.4.5.0/  (1 files)
      … 1 files under this directory
    uchar.0.0.2/  (1 files)
      … 1 files under this directory
    uucp.13.0.0/  (1 files)
      … 1 files under this directory
    uutf.1.0.2/  (1 files)
      … 1 files under this directory
    yojson.1.7.0/  (1 files)
      … 1 files under this directory
  overrides/  (6 files)
    opam__s__conf_pkg_config_opam__c__2_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ctypes_opam__c__0.15.1_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ocamlbuild_opam__c__0.14.0_opam_override/  (2 files)
      … 2 files under this directory
    opam__s__ocamlfind_opam__c__1.9.1_opam_override/  (2 files)
      … 2 files under this directory
  .gitattributes
  .gitignore
  index.json
doc.esy.lock/  (78 files)
  opam/  (69 files)
    astring.0.8.5/  (1 files)
      … 1 files under this directory
    base-bigarray.base/  (1 files)
      … 1 files under this directory
    base-bytes.base/  (1 files)
      … 1 files under this directory
    base-threads.base/  (1 files)
      … 1 files under this directory
    base-unix.base/  (1 files)
      … 1 files under this directory
    base.v0.14.1/  (1 files)
      … 1 files under this directory
    biniou.1.2.1/  (1 files)
      … 1 files under this directory
    bos.0.2.0/  (1 files)
      … 1 files under this directory
    camomile.1.0.2/  (1 files)
      … 1 files under this directory
    charInfo_width.1.1.0/  (1 files)
      … 1 files under this directory
    cmdliner.1.0.4/  (1 files)
      … 1 files under this directory
    conf-pkg-config.2/  (1 files)
      … 1 files under this directory
    cppo.1.6.7/  (1 files)
      … 1 files under this directory
    csexp.1.5.1/  (1 files)
      … 1 files under this directory
    ctypes.0.15.1/  (1 files)
      … 1 files under this directory
    dot-merlin-reader.4.1/  (1 files)
      … 1 files under this directory
    dune-build-info.2.8.5/  (1 files)
      … 1 files under this directory
    dune-configurator.2.8.5/  (1 files)
      … 1 files under this directory
    dune.2.8.5/  (1 files)
      … 1 files under this directory
    easy-format.1.3.2/  (1 files)
      … 1 files under this directory
    fix.20201120/  (1 files)
      … 1 files under this directory
    fmt.0.8.9/  (1 files)
      … 1 files under this directory
    fpath.0.7.3/  (1 files)
      … 1 files under this directory
    integers.0.4.0/  (1 files)
      … 1 files under this directory
    junit.2.0.2/  (1 files)
      … 1 files under this directory
    logs.0.7.0/  (1 files)
      … 1 files under this directory
    lwt.5.4.1/  (1 files)
      … 1 files under this directory
    lwt_ppx.2.0.1/  (1 files)
      … 1 files under this directory
    markup.0.8.2/  (1 files)
      … 1 files under this directory
    menhir.20210419/  (1 files)
      … 1 files under this directory
    menhirLib.20210419/  (1 files)
      … 1 files under this directory
    menhirSdk.20210419/  (1 files)
      … 1 files under this directory
    merlin-extend.0.6/  (1 files)
      … 1 files under this directory
    mmap.1.1.0/  (1 files)
      … 1 files under this directory
    ocaml-compiler-libs.v0.12.3/  (1 files)
      … 1 files under this directory
    ocaml-lsp-server.1.6.1/  (1 files)
      … 1 files under this directory
    ocaml-migrate-parsetree.1.8.0/  (1 files)
      … 1 files under this directory
    ocamlbuild.0.14.0/  (1 files)
      … 1 files under this directory
    ocamlfind.1.9.1/  (1 files)
      … 1 files under this directory
    ocplib-endian.1.1/  (1 files)
      … 1 files under this directory
    odoc.1.5.2/  (1 files)
      … 1 files under this directory
    pp.1.1.2/  (1 files)
      … 1 files under this directory
    ppx_derivers.1.2.1/  (1 files)
      … 1 files under this directory
    ppx_deriving.4.5/  (1 files)
      … 1 files under this directory
    ppx_optcomp.v0.14.0/  (1 files)
      … 1 files under this directory
    ppx_tools.6.3/  (1 files)
      … 1 files under this directory
    ppx_tools_versioned.5.4.0/  (1 files)
      … 1 files under this directory
    ppx_yojson_conv_lib.v0.14.0/  (1 files)
      … 1 files under this directory
    ppxfind.1.4/  (1 files)
      … 1 files under this directory
    ppxlib.0.15.0/  (1 files)
      … 1 files under this directory
    printbox.0.5/  (1 files)
      … 1 files under this directory
    psq.0.2.0/  (1 files)
      … 1 files under this directory
    ptime.0.8.5/  (1 files)
      … 1 files under this directory
    re.1.9.0/  (1 files)
      … 1 files under this directory
    reason.3.7.0/  (1 files)
      … 1 files under this directory
    result.1.5/  (1 files)
      … 1 files under this directory
    rresult.0.6.0/  (1 files)
      … 1 files under this directory
    seq.base/  (3 files)
      … 3 files under this directory
    sexplib0.v0.14.0/  (1 files)
      … 1 files under this directory
    stdio.v0.14.0/  (1 files)
      … 1 files under this directory
    stdlib-shims.0.3.0/  (1 files)
      … 1 files under this directory
    topkg.1.0.3/  (1 files)
      … 1 files under this directory
    tyxml.4.5.0/  (1 files)
      … 1 files under this directory
    uchar.0.0.2/  (1 files)
      … 1 files under this directory
    uucp.13.0.0/  (1 files)
      … 1 files under this directory
    uutf.1.0.2/  (1 files)
      … 1 files under this directory
    yojson.1.7.0/  (1 files)
      … 1 files under this directory
  overrides/  (6 files)
    opam__s__conf_pkg_config_opam__c__2_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ctypes_opam__c__0.15.1_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ocamlbuild_opam__c__0.14.0_opam_override/  (2 files)
      … 2 files under this directory
    opam__s__ocamlfind_opam__c__1.9.1_opam_override/  (2 files)
      … 2 files under this directory
  .gitattributes
  .gitignore
  index.json
esy.lock/  (76 files)
  opam/  (67 files)
    astring.0.8.5/  (1 files)
      … 1 files under this directory
    base-bigarray.base/  (1 files)
      … 1 files under this directory
    base-bytes.base/  (1 files)
      … 1 files under this directory
    base-threads.base/  (1 files)
      … 1 files under this directory
    base-unix.base/  (1 files)
      … 1 files under this directory
    base.v0.14.1/  (1 files)
      … 1 files under this directory
    biniou.1.2.1/  (1 files)
      … 1 files under this directory
    bos.0.2.0/  (1 files)
      … 1 files under this directory
    camomile.1.0.2/  (1 files)
      … 1 files under this directory
    charInfo_width.1.1.0/  (1 files)
      … 1 files under this directory
    conf-pkg-config.2/  (1 files)
      … 1 files under this directory
    cppo.1.6.7/  (1 files)
      … 1 files under this directory
    csexp.1.5.1/  (1 files)
      … 1 files under this directory
    ctypes.0.15.1/  (1 files)
      … 1 files under this directory
    dot-merlin-reader.4.1/  (1 files)
      … 1 files under this directory
    dune-build-info.2.8.5/  (1 files)
      … 1 files under this directory
    dune-configurator.2.8.5/  (1 files)
      … 1 files under this directory
    dune.2.8.5/  (1 files)
      … 1 files under this directory
    easy-format.1.3.2/  (1 files)
      … 1 files under this directory
    fix.20201120/  (1 files)
      … 1 files under this directory
    fmt.0.8.9/  (1 files)
      … 1 files under this directory
    fpath.0.7.3/  (1 files)
      … 1 files under this directory
    integers.0.4.0/  (1 files)
      … 1 files under this directory
    junit.2.0.2/  (1 files)
      … 1 files under this directory
    logs.0.7.0/  (1 files)
      … 1 files under this directory
    lwt.5.4.1/  (1 files)
      … 1 files under this directory
    lwt_ppx.2.0.1/  (1 files)
      … 1 files under this directory
    markup.0.8.2/  (1 files)
      … 1 files under this directory
    menhir.20210419/  (1 files)
      … 1 files under this directory
    menhirLib.20210419/  (1 files)
      … 1 files under this directory
    menhirSdk.20210419/  (1 files)
      … 1 files under this directory
    merlin-extend.0.6/  (1 files)
      … 1 files under this directory
    mmap.1.1.0/  (1 files)
      … 1 files under this directory
    ocaml-compiler-libs.v0.12.3/  (1 files)
      … 1 files under this directory
    ocaml-lsp-server.1.6.1/  (1 files)
      … 1 files under this directory
    ocaml-migrate-parsetree.1.8.0/  (1 files)
      … 1 files under this directory
    ocamlbuild.0.14.0/  (1 files)
      … 1 files under this directory
    ocamlfind.1.9.1/  (1 files)
      … 1 files under this directory
    ocplib-endian.1.1/  (1 files)
      … 1 files under this directory
    pp.1.1.2/  (1 files)
      … 1 files under this directory
    ppx_derivers.1.2.1/  (1 files)
      … 1 files under this directory
    ppx_deriving.4.5/  (1 files)
      … 1 files under this directory
    ppx_optcomp.v0.14.0/  (1 files)
      … 1 files under this directory
    ppx_tools.6.3/  (1 files)
      … 1 files under this directory
    ppx_tools_versioned.5.4.0/  (1 files)
      … 1 files under this directory
    ppx_yojson_conv_lib.v0.14.0/  (1 files)
      … 1 files under this directory
    ppxfind.1.4/  (1 files)
      … 1 files under this directory
    ppxlib.0.15.0/  (1 files)
      … 1 files under this directory
    printbox.0.5/  (1 files)
      … 1 files under this directory
    psq.0.2.0/  (1 files)
      … 1 files under this directory
    ptime.0.8.5/  (1 files)
      … 1 files under this directory
    re.1.9.0/  (1 files)
      … 1 files under this directory
    reason.3.7.0/  (1 files)
      … 1 files under this directory
    result.1.5/  (1 files)
      … 1 files under this directory
    rresult.0.6.0/  (1 files)
      … 1 files under this directory
    seq.base/  (3 files)
      … 3 files under this directory
    sexplib0.v0.14.0/  (1 files)
      … 1 files under this directory
    stdio.v0.14.0/  (1 files)
      … 1 files under this directory
    stdlib-shims.0.3.0/  (1 files)
      … 1 files under this directory
    topkg.1.0.3/  (1 files)
      … 1 files under this directory
    tyxml.4.5.0/  (1 files)
      … 1 files under this directory
    uchar.0.0.2/  (1 files)
      … 1 files under this directory
    uucp.13.0.0/  (1 files)
      … 1 files under this directory
    uutf.1.0.2/  (1 files)
      … 1 files under this directory
    yojson.1.7.0/  (1 files)
      … 1 files under this directory
  overrides/  (6 files)
    opam__s__conf_pkg_config_opam__c__2_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ctypes_opam__c__0.15.1_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ocamlbuild_opam__c__0.14.0_opam_override/  (2 files)
      … 2 files under this directory
    opam__s__ocamlfind_opam__c__1.9.1_opam_override/  (2 files)
      … 2 files under this directory
  .gitattributes
  .gitignore
  index.json
examples/  (51 files)
  stubs/  (4 files)
    ExampleStubs.re
    dune
    example_stubs.c
    example_stubs.js
  AnalogClock.re
  Border.re
  Boxshadow.re
  Calculator.re
  CanQuitExample.re
  CanvasExample.re
  CheckboxExample.re
  DefaultButton.re
  DropdownExample.re
  Examples.re
  FileDragAndDrop.re
  Flexbox.re
  FocusExample.re
  FontsExample.re
  GameOfLife.re
  Hello.re
  HitTests.re
  HoverExample.re
  ImageQualityExample.re
  Info.plist
  InputExample.re
  LayerExample.re
  MarkdownExample.re
  NativeFileExample.re
  … 23 more files
examples.esy.lock/  (76 files)
  opam/  (67 files)
    astring.0.8.5/  (1 files)
      … 1 files under this directory
    base-bigarray.base/  (1 files)
      … 1 files under this directory
    base-bytes.base/  (1 files)
      … 1 files under this directory
    base-threads.base/  (1 files)
      … 1 files under this directory
    base-unix.base/  (1 files)
      … 1 files under this directory
    base.v0.14.1/  (1 files)
      … 1 files under this directory
    biniou.1.2.1/  (1 files)
      … 1 files under this directory
    bos.0.2.0/  (1 files)
      … 1 files under this directory
    camomile.1.0.2/  (1 files)
      … 1 files under this directory
    charInfo_width.1.1.0/  (1 files)
      … 1 files under this directory
    conf-pkg-config.2/  (1 files)
      … 1 files under this directory
    cppo.1.6.7/  (1 files)
      … 1 files under this directory
    csexp.1.5.1/  (1 files)
      … 1 files under this directory
    ctypes.0.15.1/  (1 files)
      … 1 files under this directory
    dot-merlin-reader.4.1/  (1 files)
      … 1 files under this directory
    dune-build-info.2.8.5/  (1 files)
      … 1 files under this directory
    dune-configurator.2.8.5/  (1 files)
      … 1 files under this directory
    dune.2.8.5/  (1 files)
      … 1 files under this directory
    easy-format.1.3.2/  (1 files)
      … 1 files under this directory
    fix.20201120/  (1 files)
      … 1 files under this directory
    fmt.0.8.9/  (1 files)
      … 1 files under this directory
    fpath.0.7.3/  (1 files)
      … 1 files under this directory
    integers.0.4.0/  (1 files)
      … 1 files under this directory
    junit.2.0.2/  (1 files)
      … 1 files under this directory
    logs.0.7.0/  (1 files)
      … 1 files under this directory
    lwt.5.4.1/  (1 files)
      … 1 files under this directory
    lwt_ppx.2.0.1/  (1 files)
      … 1 files under this directory
    markup.0.8.2/  (1 files)
      … 1 files under this directory
    menhir.20210419/  (1 files)
      … 1 files under this directory
    menhirLib.20210419/  (1 files)
      … 1 files under this directory
    menhirSdk.20210419/  (1 files)
      … 1 files under this directory
    merlin-extend.0.6/  (1 files)
      … 1 files under this directory
    mmap.1.1.0/  (1 files)
      … 1 files under this directory
    ocaml-compiler-libs.v0.12.3/  (1 files)
      … 1 files under this directory
    ocaml-lsp-server.1.6.1/  (1 files)
      … 1 files under this directory
    ocaml-migrate-parsetree.1.8.0/  (1 files)
      … 1 files under this directory
    ocamlbuild.0.14.0/  (1 files)
      … 1 files under this directory
    ocamlfind.1.9.1/  (1 files)
      … 1 files under this directory
    ocplib-endian.1.1/  (1 files)
      … 1 files under this directory
    pp.1.1.2/  (1 files)
      … 1 files under this directory
    ppx_derivers.1.2.1/  (1 files)
      … 1 files under this directory
    ppx_deriving.4.5/  (1 files)
      … 1 files under this directory
    ppx_optcomp.v0.14.0/  (1 files)
      … 1 files under this directory
    ppx_tools.6.3/  (1 files)
      … 1 files under this directory
    ppx_tools_versioned.5.4.0/  (1 files)
      … 1 files under this directory
    ppx_yojson_conv_lib.v0.14.0/  (1 files)
      … 1 files under this directory
    ppxfind.1.4/  (1 files)
      … 1 files under this directory
    ppxlib.0.15.0/  (1 files)
      … 1 files under this directory
    printbox.0.5/  (1 files)
      … 1 files under this directory
    psq.0.2.0/  (1 files)
      … 1 files under this directory
    ptime.0.8.5/  (1 files)
      … 1 files under this directory
    re.1.9.0/  (1 files)
      … 1 files under this directory
    reason.3.7.0/  (1 files)
      … 1 files under this directory
    result.1.5/  (1 files)
      … 1 files under this directory
    rresult.0.6.0/  (1 files)
      … 1 files under this directory
    seq.base/  (3 files)
      … 3 files under this directory
    sexplib0.v0.14.0/  (1 files)
      … 1 files under this directory
    stdio.v0.14.0/  (1 files)
      … 1 files under this directory
    stdlib-shims.0.3.0/  (1 files)
      … 1 files under this directory
    topkg.1.0.3/  (1 files)
      … 1 files under this directory
    tyxml.4.5.0/  (1 files)
      … 1 files under this directory
    uchar.0.0.2/  (1 files)
      … 1 files under this directory
    uucp.13.0.0/  (1 files)
      … 1 files under this directory
    uutf.1.0.2/  (1 files)
      … 1 files under this directory
    yojson.1.7.0/  (1 files)
      … 1 files under this directory
  overrides/  (6 files)
    opam__s__conf_pkg_config_opam__c__2_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ctypes_opam__c__0.15.1_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ocamlbuild_opam__c__0.14.0_opam_override/  (2 files)
      … 2 files under this directory
    opam__s__ocamlfind_opam__c__1.9.1_opam_override/  (2 files)
      … 2 files under this directory
  .gitattributes
  .gitignore
  index.json
include/  (3 files)
  KHR/  (1 files)
    khrplatform.h
  glad/  (1 files)
    glad.h
  COPYING.txt
js.esy.lock/  (81 files)
  opam/  (72 files)
    astring.0.8.5/  (1 files)
      … 1 files under this directory
    base-bigarray.base/  (1 files)
      … 1 files under this directory
    base-bytes.base/  (1 files)
      … 1 files under this directory
    base-threads.base/  (1 files)
      … 1 files under this directory
    base-unix.base/  (1 files)
      … 1 files under this directory
    base.v0.14.1/  (1 files)
      … 1 files under this directory
    biniou.1.2.1/  (1 files)
      … 1 files under this directory
    bos.0.2.0/  (1 files)
      … 1 files under this directory
    camomile.1.0.2/  (1 files)
      … 1 files under this directory
    charInfo_width.1.1.0/  (1 files)
      … 1 files under this directory
    cmdliner.1.0.4/  (1 files)
      … 1 files under this directory
    conf-pkg-config.2/  (1 files)
      … 1 files under this directory
    cppo.1.6.7/  (1 files)
      … 1 files under this directory
    csexp.1.5.1/  (1 files)
      … 1 files under this directory
    ctypes.0.15.1/  (1 files)
      … 1 files under this directory
    dot-merlin-reader.4.1/  (1 files)
      … 1 files under this directory
    dune-build-info.2.8.5/  (1 files)
      … 1 files under this directory
    dune-configurator.2.8.5/  (1 files)
      … 1 files under this directory
    dune.2.8.5/  (1 files)
      … 1 files under this directory
    easy-format.1.3.2/  (1 files)
      … 1 files under this directory
    fix.20201120/  (1 files)
      … 1 files under this directory
    fmt.0.8.9/  (1 files)
      … 1 files under this directory
    fpath.0.7.3/  (1 files)
      … 1 files under this directory
    integers.0.4.0/  (1 files)
      … 1 files under this directory
    js_of_ocaml-compiler.3.9.1/  (1 files)
      … 1 files under this directory
    js_of_ocaml-lwt.3.9.0/  (1 files)
      … 1 files under this directory
    js_of_ocaml-ppx.3.9.0/  (1 files)
      … 1 files under this directory
    js_of_ocaml.3.9.0/  (1 files)
      … 1 files under this directory
    junit.2.0.2/  (1 files)
      … 1 files under this directory
    logs.0.7.0/  (1 files)
      … 1 files under this directory
    lwt.5.4.1/  (1 files)
      … 1 files under this directory
    lwt_ppx.2.0.1/  (1 files)
      … 1 files under this directory
    markup.0.8.2/  (1 files)
      … 1 files under this directory
    menhir.20210419/  (1 files)
      … 1 files under this directory
    menhirLib.20210419/  (1 files)
      … 1 files under this directory
    menhirSdk.20210419/  (1 files)
      … 1 files under this directory
    merlin-extend.0.6/  (1 files)
      … 1 files under this directory
    mmap.1.1.0/  (1 files)
      … 1 files under this directory
    ocaml-compiler-libs.v0.12.3/  (1 files)
      … 1 files under this directory
    ocaml-lsp-server.1.6.1/  (1 files)
      … 1 files under this directory
    ocaml-migrate-parsetree.1.8.0/  (1 files)
      … 1 files under this directory
    ocamlbuild.0.14.0/  (1 files)
      … 1 files under this directory
    ocamlfind.1.9.1/  (1 files)
      … 1 files under this directory
    ocplib-endian.1.1/  (1 files)
      … 1 files under this directory
    pp.1.1.2/  (1 files)
      … 1 files under this directory
    ppx_derivers.1.2.1/  (1 files)
      … 1 files under this directory
    ppx_deriving.4.5/  (1 files)
      … 1 files under this directory
    ppx_optcomp.v0.14.0/  (1 files)
      … 1 files under this directory
    ppx_tools.6.3/  (1 files)
      … 1 files under this directory
    ppx_tools_versioned.5.4.0/  (1 files)
      … 1 files under this directory
    ppx_yojson_conv_lib.v0.14.0/  (1 files)
      … 1 files under this directory
    ppxfind.1.4/  (1 files)
      … 1 files under this directory
    ppxlib.0.15.0/  (1 files)
      … 1 files under this directory
    printbox.0.5/  (1 files)
      … 1 files under this directory
    psq.0.2.0/  (1 files)
      … 1 files under this directory
    ptime.0.8.5/  (1 files)
      … 1 files under this directory
    re.1.9.0/  (1 files)
      … 1 files under this directory
    reason.3.7.0/  (1 files)
      … 1 files under this directory
    result.1.5/  (1 files)
      … 1 files under this directory
    rresult.0.6.0/  (1 files)
      … 1 files under this directory
    seq.base/  (3 files)
      … 3 files under this directory
    sexplib0.v0.14.0/  (1 files)
      … 1 files under this directory
    stdio.v0.14.0/  (1 files)
      … 1 files under this directory
    stdlib-shims.0.3.0/  (1 files)
      … 1 files under this directory
    topkg.1.0.3/  (1 files)
      … 1 files under this directory
    tyxml.4.5.0/  (1 files)
      … 1 files under this directory
    uchar.0.0.2/  (1 files)
      … 1 files under this directory
    uucp.13.0.0/  (1 files)
      … 1 files under this directory
    uutf.1.0.2/  (1 files)
      … 1 files under this directory
    yojson.1.7.0/  (1 files)
      … 1 files under this directory
  overrides/  (6 files)
    opam__s__conf_pkg_config_opam__c__2_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ctypes_opam__c__0.15.1_opam_override/  (1 files)
      … 1 files under this directory
    opam__s__ocamlbuild_opam__c__0.14.0_opam_override/  (2 files)
      … 2 files under this directory
    opam__s__ocamlfind_opam__c__1.9.1_opam_override/  (2 files)
      … 2 files under this directory
  .gitattributes
  .gitignore
  index.json
packages/  (71 files)
  reason-harfbuzz/  (13 files)
    examples/  (3 files)
      … 3 files under this directory
    src/  (6 files)
      … 6 files under this directory
    test/  (4 files)
      … 4 files under this directory
  reason-sdl2/  (9 files)
    src/  (9 files)
      … 9 files under this directory
  reason-skia/  (40 files)
    bench/  (7 files)
      … 7 files under this directory
    examples/  (9 files)
      … 9 files under this directory
    src/  (18 files)
      … 18 files under this directory
    test/  (6 files)
      … 6 files under this directory
  revery-text-wrap/  (6 files)
    examples/  (2 files)
      … 2 files under this directory
    src/  (4 files)
      … 4 files under this directory
  zed/  (3 files)
    src/  (3 files)
      … 3 files under this directory
scripts/  (5 files)
  docker/  (2 files)
    archlinux/  (1 files)
      … 1 files under this directory
    centos/  (1 files)
      … 1 files under this directory
  docker-build.sh
  make-binary-file.js
  release.sh
src/  (234 files)
  Core/  (32 files)
    App.re
    App.rei
    Color.re
    Color.rei
    Colors.re
    Environment.re
    Environment.rei
    Event.re
    Events.re
    GarbageCollector.re
    Key.re
    Key.rei
    Log.re
    Log.rei
    MouseButton.re
    MouseButton.rei
    MouseCursors.re
    MouseCursors.rei
    Performance.re
    Revery_Core.re
    TextOverflow.re
    TextWrapping.re
    Tick.re
    Time.re
    … 8 more files
  Draw/  (7 files)
    CanvasContext.re
    DebugDraw.re
    ImageResizeMode.re
    Revery_Draw.re
    Text.re
    Text.rei
    dune
  Font/  (18 files)
    Discovery.re
    Feature.re
    Feature.rei
    Features.re
    Features.rei
    FontCache.re
    FontCache.rei
    FontFamily.re
    FontFamily.rei
    FontManager.re
    FontMetrics.re
    FontRenderer.re
    FontWeight.re
    FontWidth.re
    Revery_Font.re
    ShapeResult.re
    Smoothing.re
    dune
  IO/  (7 files)
    File.re
    File.rei
    Image.re
    Image.rei
    LwtLetOperators.re
    Revery_IO.re
    dune
  Lwt/  (2 files)
    Revery_Lwt.re
    dune
  Math/  (5 files)
    Angle.re
    BoundingBox2d.re
    BoundingBox2d.rei
    Revery_Math.re
    dune
  Native/  (75 files)
    cocoa/  (14 files)
      … 14 files under this directory
    config/  (2 files)
      … 2 files under this directory
    gtk/  (2 files)
      … 2 files under this directory
    Dialog.re
    Environment.re
    Gtk.re
    Icon.re
    Initialization.re
    Input.re
    Input.rei
    Locale.re
    Menu.re
    Menu.rei
    NSObject.re
    NSView.re
    Notification.re
    ReveryCocoa.h
    ReveryGtk.h
    ReveryLinux.h
    ReveryMac.h
    ReveryNSObject.c
    ReveryWin32.h
    ReveryWindows.h
    Revery_Native.c
    Revery_Native.re
    Shell.re
    Window.re
    … 33 more files
  UI/  (43 files)
    Animation.re
    Animation.rei
    CanvasNode.re
    Container.re
    Dimensions.re
    Easing.re
    FileDrop.re
    Focus.re
    Focus.rei
    HitTest.re
    ImageNode.re
    ImageResizeMode.re
    Keyboard.re
    LayerNode.re
    Layout.re
    Mouse.re
    Mouse.rei
    NativeButtonNode.re
    Node.re
    NodeDrawContext.re
    NodeEvents.re
    Offset.re
    Overflow.re
    React.re
    … 19 more files
  UI_Components/  (33 files)
    Button.re
    Button.rei
    Center.re
    Checkbox.re
    Checkbox.rei
    Clickable.re
    Clickable.rei
    ClickableText.re
    ClipContainer.re
    ClipContainer.rei
    Column.re
    Container.re
    Container.rei
    Dropdown.re
    ExpandContainer.re
    Input.re
    Link.re
    Markdown.re
    Markdown.rei
    Positioned.re
    Positioned.rei
    RadioButtons.re
    Revery_UI_Components.re
    RichTextView.re
    … 9 more files
  UI_Hooks/  (10 files)
    Effect.re
    Effect.rei
    Reducer.re
    Reducer.rei
    Ref.re
    Ref.rei
    Revery_UI_Hooks.re
    Spring.re
    State.re
    State.rei
  Platform.re
  Revery.re
.gitattributes
.gitignore
CODE_OF_CONDUCT.md
LICENSE
README.md
Revery.opam
ReveryBench.opam
ReveryExampleJs.opam
ReveryExamples.opam
ReveryTest.opam
ThirdPartyLicenses.txt
azure-pipelines.yml
bench.json
doc.json
dune
dune-project
dune-workspace
examples.json
js.json
lsan.supp
package.json
reason-harfbuzz.opam
reason-sdl2.opam
reason-skia.opam
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 33 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| include package | library | Observed | Groups 2 file(s) under include package (observed from repository paths and static analysis). |
| Native package | library | Observed | Groups 56 file(s) under native package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 9 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.ci/create-docs.yml` (config)
- `.ci/esy-bench.yml` (config)
- `.ci/esy-build-steps.yml` (config)
- `.ci/esy-check-hygiene.yml` (config)
- `.ci/publish-build-cache.yml` (config)
- `.ci/publish-release.yml` (config)
- `.ci/restore-build-cache.yml` (config)
- `.ci/use-node.yml` (config)
- `.github/FUNDING.yml` (config)
- `azure-pipelines.yml` (ci)
- `bench.esy.lock/index.json` (config)
- `bench.esy.lock/overrides/opam__s__conf_pkg_config_opam__c__2_opam_override/package.json` (manifest)
- `bench.esy.lock/overrides/opam__s__ctypes_opam__c__0.15.1_opam_override/package.json` (manifest)
- `bench.esy.lock/overrides/opam__s__ocamlbuild_opam__c__0.14.0_opam_override/package.json` (manifest)
- `bench.esy.lock/overrides/opam__s__ocamlfind_opam__c__1.9.1_opam_override/package.json` (manifest)
- `bench.json` (config)
- `doc.esy.lock/index.json` (config)
- `doc.esy.lock/overrides/opam__s__conf_pkg_config_opam__c__2_opam_override/package.json` (manifest)
- `doc.esy.lock/overrides/opam__s__ctypes_opam__c__0.15.1_opam_override/package.json` (manifest)
- `doc.esy.lock/overrides/opam__s__ocamlbuild_opam__c__0.14.0_opam_override/package.json` (manifest)
- `doc.esy.lock/overrides/opam__s__ocamlfind_opam__c__1.9.1_opam_override/package.json` (manifest)
- `doc.json` (config)
- `esy.lock/index.json` (config)
- `esy.lock/overrides/opam__s__conf_pkg_config_opam__c__2_opam_override/package.json` (manifest)
- `esy.lock/overrides/opam__s__ctypes_opam__c__0.15.1_opam_override/package.json` (manifest)
- `esy.lock/overrides/opam__s__ocamlbuild_opam__c__0.14.0_opam_override/package.json` (manifest)
- `esy.lock/overrides/opam__s__ocamlfind_opam__c__1.9.1_opam_override/package.json` (manifest)
- `examples.esy.lock/index.json` (config)
- `examples.esy.lock/overrides/opam__s__conf_pkg_config_opam__c__2_opam_override/package.json` (manifest)
- `examples.esy.lock/overrides/opam__s__ctypes_opam__c__0.15.1_opam_override/package.json` (manifest)
- `examples.esy.lock/overrides/opam__s__ocamlbuild_opam__c__0.14.0_opam_override/package.json` (manifest)
- `examples.esy.lock/overrides/opam__s__ocamlfind_opam__c__1.9.1_opam_override/package.json` (manifest)
- `examples.json` (config)
- `js.esy.lock/index.json` (config)
- `js.esy.lock/overrides/opam__s__conf_pkg_config_opam__c__2_opam_override/package.json` (manifest)
- `js.esy.lock/overrides/opam__s__ctypes_opam__c__0.15.1_opam_override/package.json` (manifest)
- `js.esy.lock/overrides/opam__s__ocamlbuild_opam__c__0.14.0_opam_override/package.json` (manifest)
- `js.esy.lock/overrides/opam__s__ocamlfind_opam__c__1.9.1_opam_override/package.json` (manifest)
- `js.json` (config)
- `package.json` (manifest)
- `scripts/docker/archlinux/Dockerfile` (container)
- `scripts/docker/centos/Dockerfile` (container)

## Top-level layout

- `src` — 234 analysed file(s)
- `js.esy.lock` — 81 analysed file(s)
- `doc.esy.lock` — 78 analysed file(s)
- `bench.esy.lock` — 76 analysed file(s)
- `esy.lock` — 76 analysed file(s)
- `examples.esy.lock` — 76 analysed file(s)
- `packages` — 71 analysed file(s)
- `examples` — 51 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `bench` — 11 analysed file(s)
- `.ci` — 10 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.github` — 3 analysed file(s)
- `include` — 3 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `141f70f69d6abd69674b46d805a783411b38cd79` is the revision these paths and observations refer to.
