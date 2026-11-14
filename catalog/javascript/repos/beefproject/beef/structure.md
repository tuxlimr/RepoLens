# Project structure: beefproject/beef

**Analysed commit:** `9194fb84841bc3bdb9abc3384fa47bab100a5a30`

**Commit reference:** [9194fb84841bc3bdb9abc3384fa47bab100a5a30](https://github.com/beefproject/beef/commit/9194fb84841bc3bdb9abc3384fa47bab100a5a30)

**Tree at this commit:** [beefproject/beef@9194fb84841b](https://github.com/beefproject/beef/tree/9194fb84841bc3bdb9abc3384fa47bab100a5a30)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | beefproject/beef |
| Description | The Browser Exploitation Framework Project |
| Stars | 11096 |
| Forks | 2380 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9194fb84841bc3bdb9abc3384fa47bab100a5a30` |
| Retrieved at | 2026-11-14T19:12:26.228370+00:00 |
| Files in this snapshot | 797 |

## Directory tree

```text
.bundle/  (1 files)
  config
.github/  (12 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (5 files)
    codeql.yml
    dependabot-auto-merge.yml
    eslint.yml
    github_actions.yml
    stale.yml
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
  SECURITY.md
  dependabot.yml
  labels.yml
core/  (135 files)
  api/  (9 files)
    main/  (5 files)
      … 5 files under this directory
    extension.rb
    extensions.rb
    module.rb
    modules.rb
  filters/  (5 files)
    base.rb
    browser.rb
    command.rb
    http.rb
    page.rb
  main/  (103 files)
    ar-migrations/  (23 files)
      … 23 files under this directory
    client/  (34 files)
      … 34 files under this directory
    console/  (3 files)
      … 3 files under this directory
    constants/  (4 files)
      … 4 files under this directory
    handlers/  (7 files)
      … 7 files under this directory
    models/  (8 files)
      … 8 files under this directory
    network_stack/  (6 files)
      … 6 files under this directory
    rest/  (8 files)
      … 8 files under this directory
    router/  (2 files)
      … 2 files under this directory
    command.rb
    configuration.rb
    crypto.rb
    geoip.rb
    logger.rb
    migration.rb
    model.rb
    server.rb
  ruby/  (5 files)
    hash.rb
    module.rb
    print.rb
    security.rb
    string.rb
  api.rb
  bootstrap.rb
  core.rb
  extension.rb
  extensions.rb
  filters.rb
  hbmanager.rb
  loader.rb
  logger.rb
  module.rb
  modules.rb
  ruby.rb
  settings.rb
doc/  (2 files)
  COPYING
  boilerplate
docs/  (68 files)
  fonts/  (6 files)
    OpenSans-Bold-webfont.svg
    OpenSans-BoldItalic-webfont.svg
    OpenSans-Italic-webfont.svg
    OpenSans-Light-webfont.svg
    OpenSans-LightItalic-webfont.svg
    OpenSans-Regular-webfont.svg
  scripts/  (4 files)
    prettify/  (3 files)
      … 3 files under this directory
    linenumber.js
  styles/  (3 files)
    jsdoc-default.css
    prettify-jsdoc.css
    prettify-tomorrow.css
  BeefJS.html
  beef.browser.cookie.html
  beef.browser.popup.html
  beef.dom.html
  beef.encode.base64.html
  beef.encode.json.html
  beef.geolocation.html
  beef.hardware.html
  beef.init.html
  beef.js.html
  beef.logger.html
  beef.mitb.html
  beef.net.connection.html
  beef.net.cors.html
  beef.net.dns.html
  beef.net.html
  beef.net.local.html
  beef.net.portscanner.html
  beef.net.requester.html
  beef.net.xssrays.html
  beef.os.html
  beef.session.html
  beef.status.html
  beef.timeout.html
  … 31 more files
extensions/  (410 files)
  admin_ui/  (296 files)
    api/  (1 files)
      … 1 files under this directory
    classes/  (2 files)
      … 2 files under this directory
    constants/  (1 files)
      … 1 files under this directory
    controllers/  (5 files)
      … 5 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    media/  (284 files)
      … 284 files under this directory
    config.yaml
    extension.rb
  autoloader/  (3 files)
    config.yaml
    extension.rb
    model.rb
  customhook/  (5 files)
    html/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    extension.rb
    handler.rb
  demos/  (12 files)
    html/  (8 files)
      … 8 files under this directory
    api.rb
    config.yaml
    extension.rb
    handler.rb
  dns/  (7 files)
    rest/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    dns.rb
    extension.rb
    logger.rb
    model.rb
  dns_rebinding/  (5 files)
    views/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    dns_rebinding.rb
    extension.rb
  etag/  (4 files)
    api.rb
    config.yaml
    etag.rb
    extension.rb
  evasion/  (7 files)
    obfuscation/  (4 files)
      … 4 files under this directory
    config.yaml
    evasion.rb
    extension.rb
  events/  (4 files)
    api.rb
    config.yaml
    extension.rb
    handler.rb
  metasploit/  (6 files)
    rest/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    extension.rb
    module.rb
    rpcclient.rb
  network/  (6 files)
    models/  (2 files)
      … 2 files under this directory
    rest/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    extension.rb
  notifications/  (7 files)
    channels/  (4 files)
      … 4 files under this directory
    config.yaml
    extension.rb
    notifications.rb
  proxy/  (5 files)
    rest/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    extension.rb
    proxy.rb
  qrcode/  (3 files)
    config.yaml
    extension.rb
    qrcode.rb
  requester/  (7 files)
    api/  (1 files)
      … 1 files under this directory
    models/  (1 files)
      … 1 files under this directory
    rest/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    extension.rb
    handler.rb
  s2c_dns_tunnel/  (5 files)
    api.rb
    config.yaml
    dnsd.rb
    extension.rb
    httpd.rb
  social_engineering/  (10 files)
    droppers/  (1 files)
      … 1 files under this directory
    models/  (2 files)
      … 2 files under this directory
    powershell/  (1 files)
      … 1 files under this directory
    rest/  (1 files)
      … 1 files under this directory
    web_cloner/  (3 files)
      … 3 files under this directory
    config.yaml
    extension.rb
  webrtc/  (10 files)
    api/  (1 files)
      … 1 files under this directory
    models/  (4 files)
      … 4 files under this directory
    rest/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    extension.rb
    handlers.rb
  xssrays/  (8 files)
    api/  (1 files)
      … 1 files under this directory
    models/  (2 files)
      … 2 files under this directory
    rest/  (1 files)
      … 1 files under this directory
    api.rb
    config.yaml
    extension.rb
    handler.rb
modules/  (148 files)
  browser/  (148 files)
    avant_steal_history/  (3 files)
      … 3 files under this directory
    browser_fingerprinting/  (3 files)
      … 3 files under this directory
    detect_activex/  (3 files)
      … 3 files under this directory
    detect_evernote_clipper/  (3 files)
      … 3 files under this directory
    detect_extensions/  (3 files)
      … 3 files under this directory
    detect_firebug/  (3 files)
      … 3 files under this directory
    detect_foxit/  (3 files)
      … 3 files under this directory
    detect_lastpass/  (3 files)
      … 3 files under this directory
    detect_media_devices/  (3 files)
      … 3 files under this directory
    detect_mime_types/  (3 files)
      … 3 files under this directory
    detect_office/  (3 files)
      … 3 files under this directory
    detect_popup_blocker/  (3 files)
      … 3 files under this directory
    detect_quicktime/  (3 files)
      … 3 files under this directory
    detect_realplayer/  (3 files)
      … 3 files under this directory
    detect_silverlight/  (3 files)
      … 3 files under this directory
    detect_simple_adblock/  (3 files)
      … 3 files under this directory
    detect_toolbars/  (3 files)
      … 3 files under this directory
    detect_unity/  (3 files)
      … 3 files under this directory
    detect_unsafe_activex/  (3 files)
      … 3 files under this directory
    detect_vlc/  (3 files)
      … 3 files under this directory
    detect_wmp/  (3 files)
      … 3 files under this directory
    fingerprint_browser/  (4 files)
      … 4 files under this directory
    get_visited_domains/  (3 files)
      … 3 files under this directory
    get_visited_urls/  (3 files)
      … 3 files under this directory
    hooked_origin/  (75 files)
      … 75 files under this directory
.dockerignore
.gitignore
.rspec
.rubocop.yml
.ruby-gemset
.ruby-version
.simplecov
Dockerfile
Gemfile
Gemfile.lock
INSTALL.txt
README.md
Rakefile
VERSION
_config.yml
beef
conf.json
config.yaml
eslint.config.js
googlef1d5ff5151333109.html
install
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 34 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 72 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 19 file(s) under data layer (observed from repository paths and static analysis). |
| extensions package | library | Observed | Groups 104 file(s) under extensions package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 34 file(s) under external integrations (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 99 file(s) under modules package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 66 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/labels.yml` (config)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dependabot-auto-merge.yml` (ci)
- `.github/workflows/eslint.yml` (ci)
- `.github/workflows/github_actions.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.rubocop.yml` (config)
- `Dockerfile` (container)
- `_config.yml` (config)
- `conf.json` (config)
- `config.yaml` (config)
- `extensions/admin_ui/config.yaml` (config)
- `extensions/autoloader/config.yaml` (config)
- `extensions/customhook/config.yaml` (config)
- `extensions/demos/config.yaml` (config)
- `extensions/dns/config.yaml` (config)
- `extensions/dns_rebinding/config.yaml` (config)
- `extensions/etag/config.yaml` (config)
- `extensions/evasion/config.yaml` (config)
- `extensions/events/config.yaml` (config)
- `extensions/metasploit/config.yaml` (config)
- `extensions/network/config.yaml` (config)
- `extensions/notifications/config.yaml` (config)
- `extensions/proxy/config.yaml` (config)
- `extensions/qrcode/config.yaml` (config)
- `extensions/requester/config.yaml` (config)
- `extensions/s2c_dns_tunnel/config.yaml` (config)
- `extensions/social_engineering/config.yaml` (config)
- `extensions/webrtc/config.yaml` (config)
- `extensions/xssrays/config.yaml` (config)
- `modules/browser/avant_steal_history/config.yaml` (config)
- `modules/browser/browser_fingerprinting/config.yaml` (config)
- `modules/browser/detect_activex/config.yaml` (config)
- `modules/browser/detect_evernote_clipper/config.yaml` (config)
- `modules/browser/detect_extensions/config.yaml` (config)
- `modules/browser/detect_firebug/config.yaml` (config)
- `modules/browser/detect_foxit/config.yaml` (config)
- `modules/browser/detect_lastpass/config.yaml` (config)
- `modules/browser/detect_media_devices/config.yaml` (config)
- `modules/browser/detect_mime_types/config.yaml` (config)
- `modules/browser/detect_office/config.yaml` (config)
- `modules/browser/detect_popup_blocker/config.yaml` (config)
- `modules/browser/detect_quicktime/config.yaml` (config)
- `modules/browser/detect_realplayer/config.yaml` (config)
- `modules/browser/detect_silverlight/config.yaml` (config)
- `modules/browser/detect_simple_adblock/config.yaml` (config)
- `modules/browser/detect_toolbars/config.yaml` (config)
- `modules/browser/detect_unity/config.yaml` (config)
- `modules/browser/detect_unsafe_activex/config.yaml` (config)
- `modules/browser/detect_vlc/config.yaml` (config)
- `modules/browser/detect_wmp/config.yaml` (config)
- `modules/browser/fingerprint_browser/config.yaml` (config)
- `modules/browser/get_visited_domains/config.yaml` (config)
- `modules/browser/get_visited_urls/config.yaml` (config)
- `modules/browser/hooked_origin/ajax_fingerprint/config.yaml` (config)
- `modules/browser/hooked_origin/alert_dialog/config.yaml` (config)
- `modules/browser/hooked_origin/apache_tomcat_examples_cookie_disclosure/config.yaml` (config)
- `modules/browser/hooked_origin/cisco_asa_password_disclosure/config.yaml` (config)
- `modules/browser/hooked_origin/clear_console/config.yaml` (config)
- `modules/browser/hooked_origin/deface_web_page/config.yaml` (config)
- `modules/browser/hooked_origin/deface_web_page_component/config.yaml` (config)
- `modules/browser/hooked_origin/disable_developer_tools/config.yaml` (config)
- `modules/browser/hooked_origin/get_autocomplete_creds/config.yaml` (config)
- `modules/browser/hooked_origin/get_cookie/config.yaml` (config)
- `modules/browser/hooked_origin/get_form_values/config.yaml` (config)
- `modules/browser/hooked_origin/get_local_storage/config.yaml` (config)
- `modules/browser/hooked_origin/get_page_html/config.yaml` (config)
- `modules/browser/hooked_origin/get_page_html_iframe/config.yaml` (config)
- `modules/browser/hooked_origin/get_page_links/config.yaml` (config)
- `modules/browser/hooked_origin/get_session_storage/config.yaml` (config)
- `modules/browser/hooked_origin/get_stored_credentials/config.yaml` (config)
- `modules/browser/hooked_origin/link_rewrite/config.yaml` (config)
- `modules/browser/hooked_origin/link_rewrite_click_events/config.yaml` (config)
- `modules/browser/hooked_origin/link_rewrite_sslstrip/config.yaml` (config)
- `modules/browser/hooked_origin/link_rewrite_tel/config.yaml` (config)
- `modules/browser/hooked_origin/mobilesafari_address_spoofing/config.yaml` (config)
- `modules/browser/hooked_origin/overflow_cookiejar/config.yaml` (config)
- `modules/browser/hooked_origin/prompt_dialog/config.yaml` (config)
- `modules/browser/hooked_origin/remove_stuck_iframes/config.yaml` (config)

## Top-level layout

- `extensions` — 410 analysed file(s)
- `modules` — 148 analysed file(s)
- `core` — 135 analysed file(s)
- `docs` — 68 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.github` — 12 analysed file(s)
- `doc` — 2 analysed file(s)
- `.bundle` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9194fb84841bc3bdb9abc3384fa47bab100a5a30` is the revision these paths and observations refer to.
