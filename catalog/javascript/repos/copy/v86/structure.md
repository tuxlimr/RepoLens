# Project structure: copy/v86

**Analysed commit:** `315b2b0b758703ef0e6cc7b4088d6068f83f3c20`

**Commit reference:** [315b2b0b758703ef0e6cc7b4088d6068f83f3c20](https://github.com/copy/v86/commit/315b2b0b758703ef0e6cc7b4088d6068f83f3c20)

**Tree at this commit:** [copy/v86@315b2b0b7587](https://github.com/copy/v86/tree/315b2b0b758703ef0e6cc7b4088d6068f83f3c20)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | copy/v86 |
| Description | x86 PC emulator and x86-to-wasm JIT, running in the browser |
| Stars | 23688 |
| Forks | 1947 |
| Licence | BSD-2-Clause |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `315b2b0b758703ef0e6cc7b4088d6068f83f3c20` |
| Retrieved at | 2026-11-14T19:11:04.541897+00:00 |
| Files in this snapshot | 584 |

## Directory tree

```text
.cargo/  (1 files)
  config.toml
.devcontainer/  (2 files)
  Dockerfile
  devcontainer.json
.github/  (2 files)
  ISSUE_TEMPLATE/  (1 files)
    issue.md
  workflows/  (1 files)
    ci.yml
.vscode/  (1 files)
  tasks.json
bios/  (5 files)
  .gitignore
  COPYING.LESSER
  fetch-and-build-seabios.sh
  seabios-debug.config
  seabios.config
docs/  (13 files)
  .gitignore
  archlinux.md
  dos.md
  filesystem.md
  how-it-works.md
  linux-9p-image.md
  modem.md
  networking.md
  profiling.md
  sse-shifts.txt
  windows-31x.md
  windows-9x.md
  windows-nt.md
examples/  (19 files)
  alpine.html
  arch.html
  async_load.html
  basic.html
  broadcast-network.html
  debian-9p.html
  debian-raw-disk.html
  destroy.html
  lang.html
  lua.html
  nodejs.js
  nodejs_state.js
  save_restore.html
  sectorc.html
  serial.html
  tcp_terminal.html
  two_instances.html
  worker.html
  worker.js
gen/  (6 files)
  generate_analyzer.js
  generate_interpreter.js
  generate_jit.js
  rust_ast.js
  util.js
  x86_table.js
lib/  (3 files)
  9p.js
  filesystem.js
  marshall.js
src/  (91 files)
  browser/  (18 files)
    ansi_screen.js
    dummy_screen.js
    fake_network.js
    fetch_network.js
    filestorage.js
    inbrowser_network.js
    keyboard.js
    main.js
    modem.js
    mouse.js
    network.js
    print_stats.js
    screen.js
    serial.js
    speaker.js
    starter.js
    wisp_network.js
    worker_bus.js
  rust/  (41 files)
    cpu/  (17 files)
      … 17 files under this directory
    gen/  (1 files)
      … 1 files under this directory
    wasmgen/  (3 files)
      … 3 files under this directory
    analysis.rs
    codegen.rs
    config.rs
    control_flow.rs
    cpu_context.rs
    dbg.rs
    jit.rs
    js_api.rs
    leb.rs
    lib.rs
    modrm.rs
    opstats.rs
    page.rs
    paging.rs
    prefix.rs
    profiler.rs
    regs.rs
    softfloat.rs
    state_flags.rs
    zstd.rs
  acpi.js
  buffer.js
  bus.js
  cjs.js
  const.js
  cpu.js
  dma.js
  elf.js
  externs.js
  floppy.js
  ide.js
  io.js
  iso9660.js
  kernel.js
  lib.js
  log.js
  main.js
  ne2k.js
  parallel.js
  pci.js
  pit.js
  ps2.js
  rtc.js
  sb16.js
  … 8 more files
tests/  (405 files)
  api/  (13 files)
    2g-mem.js
    cdrom-insert-eject.js
    clean-shutdown.js
    floppy.js
    iso9660.js
    parallel.js
    pic.js
    reboot-buildroot.js
    reboot.js
    reset.js
    serial.js
    state.js
    test.js
  benchmark/  (5 files)
    arch-bytemark.js
    arch-python.js
    fetch-download.js
    linux-boot.js
    snapshot.js
  devices/  (9 files)
    testfs/  (2 files)
      … 2 files under this directory
    fetch_network.js
    fetch_network_post.js
    testfs.json
    virtio_9p.js
    virtio_balloon.js
    virtio_console.js
    wisp_network.js
  expect/  (51 files)
    tests/  (49 files)
      … 49 files under this directory
    readme.md
    run.js
  full/  (1 files)
    run.js
  jit-paging/  (6 files)
    Makefile
    README.md
    run-smc.js
    run.js
    test-jit-smc.c
    test-jit.c
  kvm-unit-tests/  (173 files)
    api/  (11 files)
      … 11 files under this directory
    lib/  (93 files)
      … 93 files under this directory
    x86/  (61 files)
      … 61 files under this directory
    .gitignore
    COPYRIGHT
    MAINTAINERS
    Makefile
    README.md
    build.sh
    configure
    run.mjs
  manual/  (1 files)
    gc.html
  nasm/  (131 files)
    Readme.md
    arith-optimisations.asm
    btc-imm.asm
    btc-reg16.asm
    btc-reg32.asm
    btr-imm.asm
    btr-reg16.asm
    btr-reg32.asm
    bts-imm.asm
    bts-reg16.asm
    bts-reg32.asm
    cmp16-setbe.asm
    cmpxchg-setbe.asm
    cmpxchg.asm
    cmpxchg8b.asm
    comiss.asm
    create_tests.js
    cvtpi2ps.asm
    cvtps2pi.asm
    cvttps2pi.asm
    double-segment-prefix.asm
    emms.asm
    f2xm1.asm
    fchs.asm
    … 107 more files
  qemu/  (13 files)
    LICENSE
    Makefile
    Readme.md
    compiler.h
    config-host.h
    run-qemu.js
    run.js
    test-i386-code16.S
    test-i386-muldiv.h
    test-i386-shift.h
    test-i386-vm86.S
    test-i386.c
    test-i386.h
  rust/  (1 files)
    verify-wasmgen-dummy-output.js
  Readme.md
tools/  (20 files)
  docker/  (14 files)
    alpine/  (4 files)
      … 4 files under this directory
    debian/  (6 files)
      … 6 files under this directory
    exec/  (2 files)
      … 2 files under this directory
    test-image/  (1 files)
      … 1 files under this directory
    README.md
  copy-to-sha256.py
  fetch_network_harness.mjs
  fs2json.py
  mkisofs.js
  rust-lld-wrapper
  split-image.py
.editorconfig
.gitattributes
.gitignore
.rustfmt.toml
Cargo.toml
LICENSE
LICENSE.MIT
Makefile
Readme.md
debug.html
eslint.config.mjs
index.html
manifest.json
package.json
v86.css
v86.d.ts
```

## Entry points

- [tools/copy-to-sha256.py:138](https://github.com/copy/v86/blob/315b2b0b758703ef0e6cc7b4088d6068f83f3c20/tools/copy-to-sha256.py#L138)
- [tools/fs2json.py:274](https://github.com/copy/v86/blob/315b2b0b758703ef0e6cc7b4088d6068f83f3c20/tools/fs2json.py#L274)
- [src/browser/main.js](https://github.com/copy/v86/blob/315b2b0b758703ef0e6cc7b4088d6068f83f3c20/src/browser/main.js)
- [src/main.js](https://github.com/copy/v86/blob/315b2b0b758703ef0e6cc7b4088d6068f83f3c20/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| acpi.js package | library | Observed | Groups 1 file(s) under acpi.js package (observed from repository paths and static analysis). |
| bios package | library | Observed | Groups 1 file(s) under bios package (observed from repository paths and static analysis). |
| browser package | library | Observed | Groups 18 file(s) under browser package (observed from repository paths and static analysis). |
| buffer.js package | library | Observed | Groups 1 file(s) under buffer.js package (observed from repository paths and static analysis). |
| bus.js package | library | Observed | Groups 1 file(s) under bus.js package (observed from repository paths and static analysis). |
| cjs.js package | library | Observed | Groups 1 file(s) under cjs.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| const.js package | library | Observed | Groups 1 file(s) under const.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| cpu.js package | library | Observed | Groups 1 file(s) under cpu.js package (observed from repository paths and static analysis). |
| dma.js package | library | Observed | Groups 1 file(s) under dma.js package (observed from repository paths and static analysis). |
| elf.js package | library | Observed | Groups 1 file(s) under elf.js package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ZstdCompress. Observed top-level functions: handle_dir, handle_tar, hash_file, hash_fileob… |
| externs.js package | library | Observed | Groups 1 file(s) under externs.js package (observed from repository paths and static analysis). |
| floppy.js package | library | Observed | Groups 1 file(s) under floppy.js package (observed from repository paths and static analysis). |
| gen package | library | Observed | Groups 6 file(s) under gen package (observed from repository paths and static analysis). |
| ide.js package | library | Observed | Groups 1 file(s) under ide.js package (observed from repository paths and static analysis). |
| io.js package | library | Observed | Groups 1 file(s) under io.js package (observed from repository paths and static analysis). |
| iso9660.js package | library | Observed | Groups 1 file(s) under iso9660.js package (observed from repository paths and static analysis). |
| kernel.js package | library | Observed | Groups 1 file(s) under kernel.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 3 file(s) under lib package (observed from repository paths and static analysis). |
| lib.js package | library | Observed | Groups 1 file(s) under lib.js package (observed from repository paths and static analysis). |
| log.js package | library | Observed | Groups 1 file(s) under log.js package (observed from repository paths and static analysis). |
| main.js package | library | Observed | Groups 1 file(s) under main.js package (observed from repository paths and static analysis). |
| ne2k.js package | library | Observed | Groups 1 file(s) under ne2k.js package (observed from repository paths and static analysis). |
| parallel.js package | library | Observed | Groups 1 file(s) under parallel.js package (observed from repository paths and static analysis). |
| pci.js package | library | Observed | Groups 1 file(s) under pci.js package (observed from repository paths and static analysis). |
| pit.js package | library | Observed | Groups 1 file(s) under pit.js package (observed from repository paths and static analysis). |
| ps2.js package | library | Observed | Groups 1 file(s) under ps2.js package (observed from repository paths and static analysis). |
| rtc.js package | library | Observed | Groups 1 file(s) under rtc.js package (observed from repository paths and static analysis). |
| rust package | library | Observed | Groups 41 file(s) under rust package (observed from repository paths and static analysis). |
| sb16.js package | library | Observed | Groups 1 file(s) under sb16.js package (observed from repository paths and static analysis). |
| state.js package | library | Observed | Groups 1 file(s) under state.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 405 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 10 file(s) under tools package (observed from repository paths and static analysis). |
| uart.js package | library | Observed | Groups 1 file(s) under uart.js package (observed from repository paths and static analysis). |
| vga.js package | library | Observed | Groups 1 file(s) under vga.js package (observed from repository paths and static analysis). |
| virtio_balloon.js package | library | Observed | Groups 1 file(s) under virtio_balloon.js package (observed from repository paths and static analysis). |
| virtio_console.js package | library | Observed | Groups 1 file(s) under virtio_console.js package (observed from repository paths and static analysis). |
| virtio.js package | library | Observed | Groups 1 file(s) under virtio.js package (observed from repository paths and static analysis). |
| virtio_net.js package | library | Observed | Groups 1 file(s) under virtio_net.js package (observed from repository paths and static analysis). |
| vmware.js package | library | Observed | Groups 1 file(s) under vmware.js package (observed from repository paths and static analysis). |

## Important files

- `.cargo/config.toml` (config)
- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.rustfmt.toml` (config)
- `.vscode/tasks.json` (config)
- `Cargo.toml` (manifest)
- `manifest.json` (config)
- `package.json` (manifest)
- `tools/docker/alpine/Dockerfile` (container)
- `tools/docker/debian/Dockerfile` (container)
- `tools/docker/exec/Dockerfile` (container)
- `tools/docker/test-image/Dockerfile` (container)

## Top-level layout

- `tests` — 405 analysed file(s)
- `src` — 91 analysed file(s)
- `tools` — 20 analysed file(s)
- `examples` — 19 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `docs` — 13 analysed file(s)
- `gen` — 6 analysed file(s)
- `bios` — 5 analysed file(s)
- `lib` — 3 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `.github` — 2 analysed file(s)
- `.cargo` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `315b2b0b758703ef0e6cc7b4088d6068f83f3c20` is the revision these paths and observations refer to.
