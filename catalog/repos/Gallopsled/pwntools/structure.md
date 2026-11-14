# Project structure: Gallopsled/pwntools

**Analysed commit:** `af4918c43fe1e605ea4caf98ff9ebb1e70b97bae`

**Commit reference:** [af4918c43fe1e605ea4caf98ff9ebb1e70b97bae](https://github.com/Gallopsled/pwntools/commit/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae)

**Tree at this commit:** [Gallopsled/pwntools@af4918c43fe1](https://github.com/Gallopsled/pwntools/tree/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Gallopsled/pwntools |
| Description | CTF framework and exploit development library |
| Stars | 13860 |
| Forks | 1876 |
| Licence | Other |
| Language | Python |
| Default branch | dev |
| Analysed commit | `af4918c43fe1e605ea4caf98ff9ebb1e70b97bae` |
| Retrieved at | 2026-11-14T19:09:41.057819+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
  workflows/  (6 files)
    changelog.yml
    ci.yml
    docker.yml
    lint.yml
    merge-conflict.yml
    pylint.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
docs/  (84 files)
  source/  (81 files)
    elf/  (3 files)
      … 3 files under this directory
    install/  (2 files)
      … 2 files under this directory
    libc/  (1 files)
      … 1 files under this directory
    rop/  (3 files)
      … 3 files under this directory
    shellcraft/  (9 files)
      … 9 files under this directory
    term/  (1 files)
      … 1 files under this directory
    tubes/  (5 files)
      … 5 files under this directory
    util/  (14 files)
      … 14 files under this directory
    about.rst
    adb.rst
    args.rst
    asm.rst
    atexception.rst
    atexit.rst
    commandline.rst
    conf.py
    config.rst
    constants.rst
    context.rst
    dynelf.rst
    elf.rst
    encoders.rst
    exception.rst
    filepointer.rst
    filesystem.rst
    flag.rst
    fmtstr.rst
    gdb.rst
    globals.rst
    index.rst
    install.rst
    intro.rst
    … 19 more files
  .gitignore
  Makefile
  requirements.txt
examples/  (31 files)
  exit-handlers/  (2 files)
    exploit.py
    vulnerable.c
  fmtstr/  (5 files)
    Makefile
    exploit.py
    exploit2.py
    printf-loop.c
    printf.c
  README.md
  android.py
  args.py
  asm.py
  attach.py
  clean_and_log.py
  gdb_api.py
  gen-README.py
  indented.py
  listen_uroboros.py
  options.py
  port_forward.py
  readline_completers.py
  remote.py
  remote_gdb_debugging.py
  sigreturn_corefile_aarch64.py
  sigreturn_corefile_amd64.py
  sigreturn_corefile_arm.py
  sigreturn_corefile_i386.py
  spinners.py
  splash.py
  ssh.py
  text.py
  yesno.py
extra/  (19 files)
  bash_completion.d/  (4 files)
    README.md
    install.sh
    pwn
    shellcraft
  docker/  (9 files)
    base/  (1 files)
      … 1 files under this directory
    beta/  (1 files)
      … 1 files under this directory
    dev/  (1 files)
      … 1 files under this directory
    develop/  (3 files)
      … 3 files under this directory
    stable/  (1 files)
      … 1 files under this directory
    Makefile
    README.md
  textmate/  (3 files)
    README.md
    pwntools.YAML-tmLanguage
    pwntools.tmLanguage
  zsh_completion/  (3 files)
    README.md
    _pwn
    install.zsh
pwn/  (2 files)
  __init__.py
  toplevel.py
pwnlib/  (638 files)
  adb/  (5 files)
    __init__.py
    adb.py
    bootimg.py
    bootloader.py
    protocol.py
  commandline/  (23 files)
    __init__.py
    asm.py
    checksec.py
    common.py
    constgrep.py
    cyclic.py
    debug.py
    disablenx.py
    disasm.py
    elfdiff.py
    elfpatch.py
    errno.py
    hex.py
    libcdb.py
    main.py
    phd.py
    pwnstrip.py
    scramble.py
    shellcraft.py
    template.py
    unhex.py
    update.py
    version.py
  constants/  (26 files)
    cgc/  (2 files)
      … 2 files under this directory
    darwin/  (3 files)
      … 3 files under this directory
    linux/  (17 files)
      … 17 files under this directory
    LICENSE.txt
    __init__.py
    constant.py
    freebsd.py
  context/  (1 files)
    __init__.py
  data/  (133 files)
    elf/  (8 files)
      … 8 files under this directory
    includes/  (117 files)
      … 117 files under this directory
    syscalls/  (3 files)
      … 3 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    useragents/  (2 files)
      … 2 files under this directory
    __init__.py
    crcsums.txt
  elf/  (7 files)
    __init__.py
    config.py
    corefile.py
    datatypes.py
    elf.py
    maps.py
    plt.py
  encoders/  (18 files)
    amd64/  (2 files)
      … 2 files under this directory
    arm/  (8 files)
      … 8 files under this directory
    i386/  (4 files)
      … 4 files under this directory
    mips/  (2 files)
      … 2 files under this directory
    __init__.py
    encoder.py
  filesystem/  (3 files)
    __init__.py
    path.py
    ssh.py
  flag/  (2 files)
    __init__.py
    flag.py
  internal/  (3 files)
    __init__.py
    dochelper.py
    typing.py
  libc/  (2 files)
    __init__.py
    glibc.py
  protocols/  (2 files)
    adb/  (1 files)
      … 1 files under this directory
    __init__.py
  rop/  (7 files)
    __init__.py
    call.py
    gadgets.py
    ret2csu.py
    ret2dlresolve.py
    rop.py
    srop.py
  shellcraft/  (383 files)
    templates/  (380 files)
      … 380 files under this directory
    __init__.py
    internal.py
    registers.py
  __init__.py
  abi.py
  args.py
  asm.py
  atexception.py
  atexit.py
  config.py
  device.py
  dynelf.py
  exception.py
  filepointer.py
  fmtstr.py
  gdb.py
  gdb_api_bridge.py
  gdb_faketerminal.py
  lexer.py
  libcdb.py
  log.py
  memleak.py
  qemu.py
  regsort.py
  replacements.py
  runner.py
.gitattributes
.gitignore
.isort.cfg
.readthedocs.yaml
.sublime-settings
CHANGELOG.md
CONTRIBUTING.md
DOCKER.md
LICENSE-pwntools.txt
MANIFEST.in
README.md
SECURITY.md
TESTING.md
mypy-baseline.txt
```

## Entry points

- [pwnlib/adb/bootloader.py:119](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/adb/bootloader.py#L119)
- [pwnlib/commandline/asm.py:137](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/asm.py#L137)
- [pwnlib/commandline/checksec.py:38](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/checksec.py#L38)
- [pwnlib/commandline/constgrep.py:132](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/constgrep.py#L132)
- [pwnlib/commandline/cyclic.py:102](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/cyclic.py#L102)
- [pwnlib/commandline/debug.py:101](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/debug.py#L101)
- [pwnlib/commandline/disablenx.py:23](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/disablenx.py#L23)
- [pwnlib/commandline/disasm.py:108](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/disasm.py#L108)
- [pwnlib/commandline/elfdiff.py:58](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/elfdiff.py#L58)
- [pwnlib/commandline/elfpatch.py:33](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/elfpatch.py#L33)
- [pwnlib/commandline/errno.py:202](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/errno.py#L202)
- [pwnlib/commandline/hex.py:49](https://github.com/Gallopsled/pwntools/blob/af4918c43fe1e605ea4caf98ff9ebb1e70b97bae/pwnlib/commandline/hex.py#L49)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Disabled, Enabled, EnabledIfPresent, KernelConfig, Minimum. Observed top-level functi… |
| Data layer | data | Observed | Groups 125 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: get, getxml, loop. |
| Application entry point | entrypoint | Observed | Groups 23 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: BootloaderImage, bootloader_images_header, img_info. Observed top-level functions: _conte… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| extra package | library | Observed | Groups 3 file(s) under extra package (observed from repository paths and static analysis). Observed top-level classes: ClassicPrompts. |
| pwn package | library | Observed | Groups 2 file(s) under pwn package (observed from repository paths and static analysis). |
| pwnlib package | library | Observed | Groups 100 file(s) under pwnlib package (observed from repository paths and static analysis). Observed top-level classes: ABI, AdbClient, AdbDevice, AppendedArgument, ArmEncoder, ArmXorEncoder. Observed top-level functi… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/changelog.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/merge-conflict.yml` (ci)
- `.github/workflows/pylint.yml` (ci)
- `.isort.cfg` (config)
- `.readthedocs.yaml` (config)
- `MANIFEST.in` (manifest)
- `docs/requirements.txt` (manifest)
- `extra/docker/base/Dockerfile` (container)
- `extra/docker/beta/Dockerfile` (container)
- `extra/docker/dev/Dockerfile` (container)
- `extra/docker/develop/Dockerfile` (container)
- `extra/docker/stable/Dockerfile` (container)

## Top-level layout

- `pwnlib` — 638 analysed file(s)
- `docs` — 84 analysed file(s)
- `examples` — 31 analysed file(s)
- `extra` — 19 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 12 analysed file(s)
- `pwn` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `af4918c43fe1e605ea4caf98ff9ebb1e70b97bae` is the revision these paths and observations refer to.
