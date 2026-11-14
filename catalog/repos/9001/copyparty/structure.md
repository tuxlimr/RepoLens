# Project structure: 9001/copyparty

**Analysed commit:** `1af7efeca858dcfa29f797d7ae93f22eb2fdecf0`

**Commit reference:** [1af7efeca858dcfa29f797d7ae93f22eb2fdecf0](https://github.com/9001/copyparty/commit/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0)

**Tree at this commit:** [9001/copyparty@1af7efeca858](https://github.com/9001/copyparty/tree/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 9001/copyparty |
| Description | Portable file server with accelerated resumable uploads, dedup, WebDAV, SFTP, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file |
| Stars | 47360 |
| Forks | 1924 |
| Licence | MIT |
| Language | Python |
| Default branch | hovudstraum |
| Analysed commit | `1af7efeca858dcfa29f797d7ae93f22eb2fdecf0` |
| Retrieved at | 2026-11-14T19:06:35.445818+00:00 |
| Files in this snapshot | 469 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    something-else.md
  branch-rename.md
  pull_request_template.md
.vscode/  (4 files)
  launch.json
  launch.py
  settings.json
  tasks.json
bin/  (71 files)
  handlers/  (9 files)
    404-to-fail2ban.py
    README.md
    caching-proxy.py
    ip-ok.py
    never404.py
    nooo.py
    randpic.py
    redirect.py
    sorry.py
  hooks/  (24 files)
    README.md
    discord-announce.py
    image-noexif.py
    import-me.py
    into-the-cache-it-goes.py
    msg-log.py
    notify.py
    notify2.py
    phonecam-sorter.py
    podcast-normalizer.py
    qbittorrent-magnet.py
    reject-and-explain.py
    reject-extension.py
    reject-mimetype.py
    reject-ramdisk.py
    reloc-by-ext.py
    reloc-by-wark-xau.py
    reloc-by-wark-xbu.py
    usb-eject.js
    usb-eject.py
    wget-i.py
    wget.py
    xiu-sha.py
    xiu.py
  mtag/  (23 files)
    res/  (3 files)
      … 3 files under this directory
    README.md
    audio-bpm.py
    audio-key-slicing.py
    audio-key.py
    cksum.py
    exe.py
    file-ext.py
    geotag.py
    guestbook-read.py
    guestbook.py
    image-noexif.py
    install-deps.sh
    media-hash.py
    mousepad.py
    rclone-upload.py
    sleep.py
    very-bad-idea.py
    vidchk.py
    wget.py
    yt-ipr.py
  thumbs/  (3 files)
    README.md
    collabora.py
    randomcolor.py
  README.md
  bubbleparty.sh
  dbtool.py
  partyfuse-streaming.py
  partyfuse.py
  partyfuse2.py
  partyjournal.py
  prisonparty.sh
  u2c.py
  unforget.py
  up2k.sh
  zmq-recv.py
contrib/  (66 files)
  apache/  (1 files)
    copyparty.conf
  haproxy/  (1 files)
    copyparty.conf
  lighttpd/  (2 files)
    subdomain.conf
    subpath.conf
  nginx/  (1 files)
    copyparty.conf
  nixos/  (1 files)
    modules/  (1 files)
      … 1 files under this directory
  openrc/  (1 files)
    copyparty
  package/  (15 files)
    arch/  (2 files)
      … 2 files under this directory
    makedeb-mpr/  (5 files)
      … 5 files under this directory
    nix/  (7 files)
      … 7 files under this directory
    rpm/  (1 files)
      … 1 files under this directory
  plugins/  (11 files)
    README.md
    banner.js
    browser-icons.css
    graft-thumbs.js
    meadup.js
    minimal-up2k.html
    minimal-up2k.js
    quickmove.js
    rave.js
    up2k-hook-ytid.js
    up2k-hooks.js
  podman-systemd/  (3 files)
    README.md
    copyparty.conf
    copyparty.container
  rc/  (1 files)
    copyparty
  systemd/  (9 files)
    cfssl.service
    copyparty-user.service
    copyparty.conf
    copyparty.example.conf
    copyparty.service
    copyparty@.service
    index.md
    prisonparty.service
    prisonparty@.service
  themes/  (1 files)
    bsod.css
  traefik/  (4 files)
    traefik-docker/  (3 files)
      … 3 files under this directory
    copyparty.yaml
  windows/  (1 files)
    copyparty-ctmp.bat
  README.md
  cfssl.sh
  copyparty.bat
  explorer-nothumbs-nofoldertypes.reg
  flameshot.sh
  index.html
  ishare.iscu
  media-osd-bgone.ps1
  send-to-cpp.contextlet.json
  setup-ashell.sh
  sharex.sxcu
  sharex12.sxcu
  webdav-cfg.bat
  zfs-tune.py
copyparty/  (117 files)
  bos/  (3 files)
    __init__.py
    bos.py
    path.py
  res/  (1 files)
    __init__.py
  stolen/  (17 files)
    dnslib/  (9 files)
      … 9 files under this directory
    ifaddr/  (5 files)
      … 5 files under this directory
    __init__.py
    qrcodegen.py
    surrogateescape.py
  web/  (61 files)
    a/  (1 files)
      … 1 files under this directory
    deps/  (2 files)
      … 2 files under this directory
    tl/  (22 files)
      … 22 files under this directory
    Makefile
    Makefile.s1
    baguettebox.js
    browser.css
    browser.html
    browser2.html
    cf.html
    dbg-audio.js
    idp.html
    md.css
    md.html
    md.js
    md2.css
    md2.js
    mde.css
    mde.html
    mde.js
    msg.html
    opds.xml
    opds_osd.xml
    rups.css
    rups.html
    rups.js
    shares.css
    … 12 more files
  __init__.py
  __main__.py
  __version__.py
  authsrv.py
  broker_mp.py
  broker_mpw.py
  broker_thr.py
  broker_util.py
  cert.py
  cfg.py
  dxml.py
  fsutil.py
  ftpd.py
  httpconn.py
  httpsrv.py
  ico.py
  mdns.py
  metrics.py
  mtag.py
  multicast.py
  pwhash.py
  qrkode.py
  sftpd.py
  smbd.py
  … 11 more files
docs/  (58 files)
  copyparty.d/  (5 files)
    foo/  (2 files)
      … 2 files under this directory
    more-users/  (2 files)
      … 2 files under this directory
    some.conf
  cursed-usecases/  (1 files)
    README.md
  examples/  (16 files)
    docker/  (14 files)
      … 14 files under this directory
    README.md
    windows.md
  rice/  (2 files)
    README.md
    rtl.patch
  README.md
  TODO.md
  bad-codecs.md
  biquad.html
  bufsize.txt
  chungus.conf
  chunksizes.py
  design.txt
  devnotes.md
  example.conf
  example2.conf
  hls.html
  idp.md
  lics.txt
  logo-sq.svg
  logo.svg
  logo256.svg
  multisearch.html
  music-analysis.sh
  notes.bat
  notes.md
  notes.sh
  nuitka.txt
  pretend-youre-alaskan.patch
  … 10 more files
scripts/  (106 files)
  bench/  (1 files)
    filehash.sh
  deps-docker/  (17 files)
    Dockerfile
    Makefile
    busy-mp3.sh
    codemirror.patch
    easymde-ln.patch
    easymde-marked6.patch
    easymde.patch
    genprism.py
    genprism.sh
    markdown-it.patch
    marked-ln.patch
    marked.patch
    mini-fa.css
    mini-fa.sh
    shiftbase.py
    showdown.patch
    zopfli.makefile
  docker/  (27 files)
    base/  (12 files)
      … 12 files under this directory
    Dockerfile.ac
    Dockerfile.dj
    Dockerfile.djd
    Dockerfile.djf
    Dockerfile.djff
    Dockerfile.dju
    Dockerfile.im
    Dockerfile.iv
    Dockerfile.min
    Dockerfile.min.pip
    Makefile
    README.md
    devnotes.md
    innvikler.sh
    make.sh
  lics/  (8 files)
    1.r13
    2.r13
    3.r13
    4.r13
    5.r13
    6.r13
    README.md
    rot.py
  patches/  (2 files)
    pyftpdlib-fe80.patch
    pyftpdlib-win313.patch
  py2/  (1 files)
    queue/  (1 files)
      … 1 files under this directory
  pyinstaller/  (15 files)
    README.md
    build.sh
    depchk.sh
    deps.sha512
    deps.txt
    ffmpeg.patch
    ffmpeg.txt
    icon.sh
    loader.py
    loader.rc
    notes.txt
    up2k.rc
    up2k.sh
    up2k.spec
    up2k.spec.sh
  strip_hints/  (1 files)
    a.py
  test/  (5 files)
    ptrav.py
    race.py
    redup.sh
    smoketest.py
    tftp.sh
  tl/  (2 files)
    1.sh
    1.txt
  copyparty-android.sh
  fusefuzz.py
  genhelp.sh
  genlic.py
  help2html.py
  help2txt.sh
  install-githooks.sh
  logpack.sh
  make-pypi-release.sh
  make-pyz.sh
  make-rpm.sh
  make-sfx.sh
  make-tgz-release.sh
  prep.sh
  profile.py
  rls.sh
  run-tests.sh
  sfx.ls
  sfx.py
  sfx.sh
  speedtest-fs.py
  tl.js
  tl.py
  tlcheck.sh
  … 3 more files
srv/  (6 files)
  expand/  (1 files)
    README.md
  ceditable.html
  chat.md
  extend.md
  ping.html
  test.md
tests/  (25 files)
  res/  (8 files)
    idp/  (8 files)
      … 8 files under this directory
  __init__.py
  ptrav.py
  run.py
  test_cp.py
  test_dedup.py
  test_dots.py
  test_dxml.py
  test_hooks.py
  test_httpcli.py
  test_idp.py
  test_metrics.py
  test_mv.py
  test_shr.py
  test_utils.py
  test_vfs.py
  test_webdav.py
  util.py
.eslintrc.json
.gitattributes
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
SECURITY.md
flake.lock
flake.nix
pyproject.toml
setup.py
```

## Entry points

- [bin/dbtool.py:304](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/dbtool.py#L304)
- [bin/hooks/discord-announce.py:76](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/discord-announce.py#L76)
- [bin/hooks/image-noexif.py:68](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/image-noexif.py#L68)
- [bin/hooks/into-the-cache-it-goes.py:139](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/into-the-cache-it-goes.py#L139)
- [bin/hooks/msg-log.py:135](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/msg-log.py#L135)
- [bin/hooks/notify.py:65](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/notify.py#L65)
- [bin/hooks/notify2.py:72](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/notify2.py#L72)
- [bin/hooks/phonecam-sorter.py:84](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/phonecam-sorter.py#L84)
- [bin/hooks/podcast-normalizer.py:117](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/podcast-normalizer.py#L117)
- [bin/hooks/qbittorrent-magnet.py:126](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/qbittorrent-magnet.py#L126)
- [bin/hooks/reject-and-explain.py:59](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/reject-and-explain.py#L59)
- [bin/hooks/reject-extension.py:34](https://github.com/9001/copyparty/blob/1af7efeca858dcfa29f797d7ae93f22eb2fdecf0/bin/hooks/reject-extension.py#L34)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 8 file(s) under api layer (observed from repository paths and static analysis). Observed top-level functions: main, say_no, send_errorpage_with_redirect_link, send_http_301_permanent_redirect, send_http_302_tempo… |
| bin package | library | Observed | Groups 20 file(s) under bin package (observed from repository paths and static analysis). Observed top-level classes: PE2, Wrapper. Observed top-level functions: create_gif, do_stuff, iterate, main, make_headers, open_p… |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: clean2. |
| contrib package | library | Observed | Groups 11 file(s) under contrib package (observed from repository paths and static analysis). |
| copyparty package | library | Observed | Groups 89 file(s) under copyparty package (observed from repository paths and static analysis). Observed top-level classes: A, AAAA, AXS, Adapter, AuthSrv, BadXML. Observed top-level functions: B, H, I, IP4, IP6, _add_m… |
| Application entry point | entrypoint | Observed | Groups 51 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: APF, BasicDodge11874, CPPF, CTermsize, CacheNode, Ctl. Observed top-level functions: _lsd… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 41 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: ckck, confirm, meichk, meicln. |
| Tests | test | Observed | Groups 30 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CState, Cfg, Conn, Cpp, NullBroker, TC. Observed top-level functions: _parse, allget, chkcmd, curl, eprint,… |

## Important files

- `.eslintrc.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/tasks.json` (config)
- `contrib/package/nix/copyparty/pin.json` (config)
- `contrib/package/nix/partftpy/pin.json` (config)
- `contrib/send-to-cpp.contextlet.json` (config)
- `contrib/traefik/copyparty.yaml` (config)
- `contrib/traefik/traefik-docker/copyparty.compose.yml` (config)
- `contrib/traefik/traefik-docker/traefik.compose.yml` (config)
- `docs/examples/docker/basic-docker-compose/docker-compose.yml` (container)
- `docs/examples/docker/idp-authelia-traefik/authelia/configuration.yml` (config)
- `docs/examples/docker/idp-authelia-traefik/authelia/users_database.yml` (config)
- `docs/examples/docker/idp-authelia-traefik/docker-compose.yml` (container)
- `docs/examples/docker/idp-authentik-traefik/based-on/docker-compose-authentik.yml` (config)
- `docs/examples/docker/idp-authentik-traefik/based-on/docker-compose-traefik.yml` (config)
- `docs/examples/docker/idp-authentik-traefik/docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `scripts/deps-docker/Dockerfile` (container)
- `scripts/docker/Dockerfile.ac` (container)
- `scripts/docker/Dockerfile.dj` (container)
- `scripts/docker/Dockerfile.djd` (container)
- `scripts/docker/Dockerfile.djf` (container)
- `scripts/docker/Dockerfile.djff` (container)
- `scripts/docker/Dockerfile.dju` (container)
- `scripts/docker/Dockerfile.im` (container)
- `scripts/docker/Dockerfile.iv` (container)
- `scripts/docker/Dockerfile.min` (container)
- `scripts/docker/Dockerfile.min.pip` (container)
- `scripts/docker/base/Dockerfile.zlibng` (container)
- `setup.py` (manifest)

## Top-level layout

- `copyparty` — 117 analysed file(s)
- `scripts` — 106 analysed file(s)
- `bin` — 71 analysed file(s)
- `contrib` — 66 analysed file(s)
- `docs` — 58 analysed file(s)
- `tests` — 25 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `srv` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `.vscode` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1af7efeca858dcfa29f797d7ae93f22eb2fdecf0` is the revision these paths and observations refer to.
