# Project structure: swisskyrepo/PayloadsAllTheThings

**Analysed commit:** `08ea40e77db3f42ef8f20c65196f3936a19b6c86`

**Commit reference:** [08ea40e77db3f42ef8f20c65196f3936a19b6c86](https://github.com/swisskyrepo/PayloadsAllTheThings/commit/08ea40e77db3f42ef8f20c65196f3936a19b6c86)

**Tree at this commit:** [swisskyrepo/PayloadsAllTheThings@08ea40e77db3](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/08ea40e77db3f42ef8f20c65196f3936a19b6c86)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | swisskyrepo/PayloadsAllTheThings |
| Description | A list of useful payloads and bypass for Web Application Security and Pentest/CTF |
| Stars | 82679 |
| Forks | 17582 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `08ea40e77db3f42ef8f20c65196f3936a19b6c86` |
| Retrieved at | 2026-11-14T19:06:09.632148+00:00 |
| Files in this snapshot | 356 |

## Directory tree

```text
.github/  (6 files)
  overrides/  (1 files)
    main.html
  workflows/  (2 files)
    check-markdown.yml
    mkdocs-build.yml
  .markdownlint.json
  FUNDING.yml
  hopla_config.json
API Key Leaks/  (2 files)
  IIS-Machine-Keys.md
  README.md
Account Takeover/  (2 files)
  README.md
  mfa-bypass.md
Brute Force Rate Limit/  (1 files)
  README.md
Business Logic Errors/  (1 files)
  README.md
CORS Misconfiguration/  (1 files)
  README.md
CRLF Injection/  (2 files)
  Files/  (1 files)
    crlfinjection.txt
  README.md
CSS Injection/  (1 files)
  README.md
CSV Injection/  (1 files)
  README.md
CVE Exploits/  (2 files)
  Log4Shell.md
  README.md
Clickjacking/  (1 files)
  README.md
Client Side Path Traversal/  (1 files)
  README.md
Command Injection/  (3 files)
  Intruder/  (2 files)
    command-execution-unix.txt
    command_exec.txt
  README.md
Cross-Site Request Forgery/  (1 files)
  README.md
DNS Rebinding/  (1 files)
  README.md
DOM Clobbering/  (1 files)
  README.md
Denial of Service/  (1 files)
  README.md
Dependency Confusion/  (1 files)
  README.md
Directory Traversal/  (4 files)
  Intruder/  (3 files)
    deep_traversal.txt
    directory_traversal.txt
    traversals-8-deep-exotic-encoding.txt
  README.md
Encoding Transformations/  (1 files)
  README.md
External Variable Modification/  (1 files)
  README.md
File Inclusion/  (19 files)
  Files/  (3 files)
    LFI2RCE.py
    phpinfolfi.py
    uploadlfi.py
  Intruders/  (13 files)
    BSD-files.txt
    JHADDIX_LFI.txt
    LFI-FD-check.txt
    LFI-WindowsFileCheck.txt
    Linux-files.txt
    List_Of_File_To_Include.txt
    List_Of_File_To_Include_NullByteAdded.txt
    Mac-files.txt
    Web-files.txt
    Windows-files.txt
    dot-slash-PathTraversal_and_LFI_pairing.txt
    php-filter-iconv.txt
    simple-check.txt
  LFI-to-RCE.md
  README.md
  Wrappers.md
Google Web Toolkit/  (1 files)
  README.md
GraphQL Injection/  (1 files)
  README.md
HTTP Parameter Pollution/  (1 files)
  README.md
Headless Browser/  (3 files)
  files/  (2 files)
    iframe.html
    window_location_js.html
  README.md
Hidden Parameters/  (1 files)
  README.md
Insecure Deserialization/  (10 files)
  Files/  (3 files)
    Ruby_universal_gadget_generate_verify.rb
    node-serialize.js
    ruby-serialize.yaml
  DotNET.md
  Java.md
  Node.md
  PHP.md
  Python.md
  README.md
  Ruby.md
Insecure Direct Object References/  (1 files)
  README.md
Insecure Management Interface/  (2 files)
  Intruder/  (1 files)
    springboot_actuator.txt
  README.md
Insecure Randomness/  (1 files)
  README.md
Insecure Source Code Management/  (6 files)
  Files/  (1 files)
    github-dorks.txt
  Bazaar.md
  Git.md
  Mercurial.md
  README.md
  Subversion.md
JSON Web Token/  (1 files)
  README.md
Java RMI/  (1 files)
  README.md
LDAP Injection/  (4 files)
  Intruder/  (3 files)
    LDAP_FUZZ.txt
    LDAP_FUZZ_SMALL.txt
    LDAP_attributes.txt
  README.md
LaTeX Injection/  (1 files)
  README.md
Mass Assignment/  (1 files)
  README.md
Methodology and Resources/  (33 files)
  Active Directory Attack.md
  Bind Shell Cheatsheet.md
  Cloud - AWS Pentest.md
  Cloud - Azure Pentest.md
  Cobalt Strike - Cheatsheet.md
  Container - Docker Pentest.md
  Container - Kubernetes Pentest.md
  Escape Breakout.md
  HTML Smuggling.md
  Hash Cracking.md
  Initial Access.md
  Linux - Evasion.md
  Linux - Persistence.md
  Linux - Privilege Escalation.md
  MSSQL Server - Cheatsheet.md
  Metasploit - Cheatsheet.md
  Methodology and enumeration.md
  Network Discovery.md
  Network Pivoting Techniques.md
  Office - Attacks.md
  Powershell - Cheatsheet.md
  Reverse Shell Cheatsheet.md
  Source Code Management.md
  Vulnerability Reports.md
  … 9 more files
NoSQL Injection/  (3 files)
  Intruder/  (2 files)
    MongoDB.txt
    NoSQL.txt
  README.md
OAuth Misconfiguration/  (1 files)
  README.md
ORM Leak/  (1 files)
  README.md
Open Redirect/  (4 files)
  Intruder/  (3 files)
    Open-Redirect-payloads.txt
    open_redirect_wordlist.txt
    openredirects.txt
  README.md
Prompt Injection/  (1 files)
  README.md
Prototype Pollution/  (1 files)
  README.md
Race Condition/  (1 files)
  README.md
Regular Expression/  (1 files)
  README.md
Request Smuggling/  (1 files)
  README.md
Reverse Proxy Misconfigurations/  (1 files)
  README.md
SAML Injection/  (1 files)
  README.md
SQL Injection/  (31 files)
  Intruder/  (21 files)
    Auth_Bypass.txt
    Auth_Bypass2.txt
    FUZZDB_MSSQL-WHERE_Time.txt
    FUZZDB_MSSQL.txt
    FUZZDB_MSSQL_Enumeration.txt
    FUZZDB_MYSQL.txt
    FUZZDB_MySQL-WHERE_Time.txt
    FUZZDB_MySQL_ReadLocalFiles.txt
    FUZZDB_Oracle.txt
    FUZZDB_Postgres_Enumeration.txt
    Generic_ErrorBased.txt
    Generic_Fuzz.txt
    Generic_TimeBased.txt
    Generic_UnionSelect.txt
    SQL-Injection
    SQLi_Polyglots.txt
    payloads-sql-blind-MSSQL-INSERT
    payloads-sql-blind-MSSQL-WHERE
    payloads-sql-blind-MySQL-INSERT
    payloads-sql-blind-MySQL-ORDER_BY
    payloads-sql-blind-MySQL-WHERE
  BigQuery Injection.md
  Cassandra Injection.md
  DB2 Injection.md
  MSSQL Injection.md
  MySQL Injection.md
  OracleSQL Injection.md
  PostgreSQL Injection.md
  README.md
  SQLite Injection.md
  SQLmap.md
Server Side Include Injection/  (2 files)
  Files/  (1 files)
    ssi_esi.txt
  README.md
Server Side Request Forgery/  (12 files)
  Files/  (9 files)
    SSRF_expect.svg
    SSRF_url.svg
    ip.py
    ssrf_iframe.svg
    ssrf_svg_css_import.svg
    ssrf_svg_css_link.svg
    ssrf_svg_css_xmlstylesheet.svg
    ssrf_svg_image.svg
    ssrf_svg_use.svg
  README.md
  SSRF-Advanced-Exploitation.md
  SSRF-Cloud-Instances.md
Server Side Template Injection/  (9 files)
  Intruder/  (1 files)
    ssti.fuzz
  ASP.md
  Elixir.md
  Java.md
  JavaScript.md
  PHP.md
  Python.md
  README.md
  Ruby.md
Tabnabbing/  (1 files)
  README.md
Type Juggling/  (1 files)
  README.md
Upload Insecure Files/  (69 files)
  CVE FFmpeg HLS/  (2 files)
    gen_avi_bypass.py
    gen_xbin_avi.py
  CVE ZIP Symbolic Link/  (2 files)
    generate.sh
    passwd
  Configuration Apache .htaccess/  (5 files)
    .htaccess
    .htaccess_phpinfo
    .htaccess_rce_files
    .htaccess_shell
    README.md
  Configuration IIS web.config/  (1 files)
    web.config
  Configuration Python __init__.py/  (1 files)
    python-generate-init.py
  Configuration uwsgi.ini/  (1 files)
    uwsgi.ini
  EICAR/  (1 files)
    eicar.txt
  Extension ASP/  (9 files)
    extensions.lst
    shell.asa
    shell.ashx
    shell.asmx
    shell.asp
    shell.aspx
    shell.cer
    shell.soap
    shell.xamlx
  Extension HTML/  (1 files)
    xss.html
  Extension PHP/  (29 files)
    extensions.lst
    php-script-tag.php
    phpinfo.jpg.php
    phpinfo.phar
    phpinfo.php
    phpinfo.php3
    phpinfo.php4
    phpinfo.php5
    phpinfo.php7
    phpinfo.php8
    phpinfo.phpt
    phpinfo.pht
    phpinfo.phtml
    shell.gif^shell.php
    shell.jpeg.php
    shell.jpg.php
    shell.jpg^shell.php
    shell.phar
    shell.php
    shell.php3
    shell.php4
    shell.php5
    shell.php7
    shell.phpt
    … 5 more files
  Jetty RCE/  (1 files)
    JettyShell.xml
  Picture Compression/  (4 files)
    createBulletproofJPG.py
    createCompressedPNG_110x110.php
    createGIFwithGlobalColorTable.php
    createPNGwithPLTE.php
  Picture ImageMagick/  (7 files)
    convert_local_etc_passwd.svg
    convert_local_etc_passwd_html.svg
    imagetragik1_payload_url_bind_shell_nc.mvg
    imagetragik1_payload_url_remote_connection.mvg
    imagetragik1_payload_url_reverse_shell_bash.mvg
    imagetragik1_payload_xml_reverse_shell_nctraditional.xml
    imagetragik1_payload_xml_reverse_shell_netcat_encoded.xml
  Picture Metadata/  (1 files)
    Build_image_to_LFI.py
  Server Side Include/  (3 files)
    exec.shtml
    include.shtml
    index.stm
  README.md
Virtual Hosts/  (1 files)
  README.md
Web Cache Deception/  (2 files)
  Intruders/  (1 files)
    param_miner_lowercase_headers.txt
  README.md
Web Sockets/  (2 files)
  Files/  (1 files)
    ws-harness.py
  README.md
XPATH Injection/  (1 files)
  README.md
XS-Leak/  (1 files)
  README.md
XSLT Injection/  (16 files)
  Files/  (15 files)
    enum-system-version-vendor.xsl
    file-write.xsl
    rce-dotnet-2.xsl
    rce-dotnet.xsl
    rce-java-1.xsl
    rce-java-2.xsl
    rce-php-assert.xsl
    rce-php-file-create.xsl
    rce-php-file-read.xsl
    rce-php-meterpreter.xsl
    rce-php-scandir.xsl
    read-and-ssrf.xsl
    system-properties.xml
    system-properties.xsl
    xxe.xsl
  README.md
XSS Injection/  (48 files)
  Files/  (27 files)
    JupyterNotebookXSS.ipynb
    SVG_XSS1.svg
    SVG_XSS2.svg
    SVG_XSS3.svg
    SVG_XSS_green_triangle.svg
    SVG_XSS_nested_img_xlink.svg
    SVG_XSS_nested_svg.svg
    SVG_XSS_nested_use_xlink.svg
    SVG_XSS_red_lightning.svg
    xml.xsd
    xss.cer
    xss.dtd
    xss.htm
    xss.html.demo
    xss.hxt
    xss.mno
    xss.rdf
    xss.url.url
    xss.vml
    xss.wsdl
    xss.xht
    xss.xhtml
    xss.xml
    xss.xsd
    … 3 more files
  Intruders/  (15 files)
    0xcela_event_handlers.txt
    BRUTELOGIC-XSS-JS.txt
    BRUTELOGIC-XSS-STRINGS.txt
    IntrudersXSS.txt
    JHADDIX_XSS.txt
    MarioXSSVectors.txt
    RSNAKE_XSS.txt
    XSSDetection.txt
    XSS_Polyglots.txt
    jsonp_endpoint.txt
    port_swigger_xss_cheatsheet_event_handlers.txt
    xss_alert.txt
    xss_alert_identifiable.txt
    xss_payloads_quick.txt
    xss_swf_fuzz.txt
  1 - XSS Filter Bypass.md
  2 - XSS Polyglot.md
  3 - XSS Common WAF Bypass.md
  4 - CSP Bypass.md
  5 - XSS in Angular.md
  README.md
XXE Injection/  (9 files)
  Files/  (6 files)
    Classic XXE - etc passwd.xml
    Classic XXE B64 Encoded.xml
    Classic XXE.xml
    Deny Of Service - Billion Laugh Attack
    XXE OOB Attack (Yunusov, 2013).xml
    XXE PHP Wrapper.xml
  Intruders/  (2 files)
    XXE_Fuzzing.txt
    xml-attacks.txt
  README.md
Zip Slip/  (1 files)
  README.md
_LEARNING_AND_SOCIALS/  (3 files)
  BOOKS.md
  TWITTER.md
  YOUTUBE.md
_template_vuln/  (1 files)
  README.md
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
DISCLAIMER.md
LICENSE
README.md
custom.css
mkdocs.yml
```

## Entry points

- [File Inclusion/Files/phpinfolfi.py:198](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/08ea40e77db3f42ef8f20c65196f3936a19b6c86/File%20Inclusion/Files/phpinfolfi.py#L198)
- [Upload Insecure Files/CVE FFmpeg HLS/gen_avi_bypass.py:27](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/08ea40e77db3f42ef8f20c65196f3936a19b6c86/Upload%20Insecure%20Files/CVE%20FFmpeg%20HLS/gen_avi_bypass.py#L27)
- [Upload Insecure Files/CVE FFmpeg HLS/gen_xbin_avi.py:141](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/08ea40e77db3f42ef8f20c65196f3936a19b6c86/Upload%20Insecure%20Files/CVE%20FFmpeg%20HLS/gen_xbin_avi.py#L141)
- [Upload Insecure Files/Picture Compression/createBulletproofJPG.py:59](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/08ea40e77db3f42ef8f20c65196f3936a19b6c86/Upload%20Insecure%20Files/Picture%20Compression/createBulletproofJPG.py#L59)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ThreadWorker. Observed top-level functions: echo_block, echo_seq, gen_xbin_packet_header,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| File Inclusion package | library | Observed | Groups 2 file(s) under file inclusion package (observed from repository paths and static analysis). |
| Insecure Deserialization package | library | Observed | Groups 2 file(s) under insecure deserialization package (observed from repository paths and static analysis). |
| Server Side Request Forgery package | library | Observed | Groups 1 file(s) under server side request forgery package (observed from repository paths and static analysis). Observed top-level functions: DECIMAL_SINGLE, DEC_OVERFLOW_SINGLE, HEX_SINGLE, OCT_SINGLE, RANDOM_TEXT, RA… |
| Upload Insecure Files package | library | Observed | Groups 17 file(s) under upload insecure files package (observed from repository paths and static analysis). |
| Web Sockets package | library | Observed | Groups 1 file(s) under web sockets package (observed from repository paths and static analysis). Observed top-level classes: myWebServer. Observed top-level functions: FuzzWebSocket, LoadMessage. |

## Important files

- `.github/.markdownlint.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/hopla_config.json` (config)
- `.github/workflows/check-markdown.yml` (ci)
- `.github/workflows/mkdocs-build.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Insecure Deserialization/Files/ruby-serialize.yaml` (config)
- `Upload Insecure Files/Configuration uwsgi.ini/uwsgi.ini` (config)
- `mkdocs.yml` (config)

## Top-level layout

- `Upload Insecure Files` — 69 analysed file(s)
- `XSS Injection` — 48 analysed file(s)
- `Methodology and Resources` — 33 analysed file(s)
- `SQL Injection` — 31 analysed file(s)
- `File Inclusion` — 19 analysed file(s)
- `XSLT Injection` — 16 analysed file(s)
- `Server Side Request Forgery` — 12 analysed file(s)
- `Insecure Deserialization` — 10 analysed file(s)
- `Server Side Template Injection` — 9 analysed file(s)
- `XXE Injection` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 6 analysed file(s)
- `Insecure Source Code Management` — 6 analysed file(s)
- `Directory Traversal` — 4 analysed file(s)
- `LDAP Injection` — 4 analysed file(s)
- `Open Redirect` — 4 analysed file(s)
- `Command Injection` — 3 analysed file(s)
- `Headless Browser` — 3 analysed file(s)
- `NoSQL Injection` — 3 analysed file(s)
- `_LEARNING_AND_SOCIALS` — 3 analysed file(s)
- `API Key Leaks` — 2 analysed file(s)
- `Account Takeover` — 2 analysed file(s)
- `CRLF Injection` — 2 analysed file(s)
- `CVE Exploits` — 2 analysed file(s)
- `Insecure Management Interface` — 2 analysed file(s)
- `Server Side Include Injection` — 2 analysed file(s)
- `Web Cache Deception` — 2 analysed file(s)
- `Web Sockets` — 2 analysed file(s)
- `Brute Force Rate Limit` — 1 analysed file(s)
- `Business Logic Errors` — 1 analysed file(s)
- `CORS Misconfiguration` — 1 analysed file(s)
- `CSS Injection` — 1 analysed file(s)
- `CSV Injection` — 1 analysed file(s)
- `Clickjacking` — 1 analysed file(s)
- `Client Side Path Traversal` — 1 analysed file(s)
- `Cross-Site Request Forgery` — 1 analysed file(s)
- `DNS Rebinding` — 1 analysed file(s)
- `DOM Clobbering` — 1 analysed file(s)
- `Denial of Service` — 1 analysed file(s)
- `Dependency Confusion` — 1 analysed file(s)
- `Encoding Transformations` — 1 analysed file(s)
- `External Variable Modification` — 1 analysed file(s)
- `Google Web Toolkit` — 1 analysed file(s)
- `GraphQL Injection` — 1 analysed file(s)
- `HTTP Parameter Pollution` — 1 analysed file(s)
- `Hidden Parameters` — 1 analysed file(s)
- `Insecure Direct Object References` — 1 analysed file(s)
- `Insecure Randomness` — 1 analysed file(s)
- `JSON Web Token` — 1 analysed file(s)
- `Java RMI` — 1 analysed file(s)
- `LaTeX Injection` — 1 analysed file(s)
- `Mass Assignment` — 1 analysed file(s)
- `OAuth Misconfiguration` — 1 analysed file(s)
- `ORM Leak` — 1 analysed file(s)
- `Prompt Injection` — 1 analysed file(s)
- `Prototype Pollution` — 1 analysed file(s)
- `Race Condition` — 1 analysed file(s)
- `Regular Expression` — 1 analysed file(s)
- `Request Smuggling` — 1 analysed file(s)
- `Reverse Proxy Misconfigurations` — 1 analysed file(s)
- `SAML Injection` — 1 analysed file(s)
- `Tabnabbing` — 1 analysed file(s)
- `Type Juggling` — 1 analysed file(s)
- `Virtual Hosts` — 1 analysed file(s)
- `XPATH Injection` — 1 analysed file(s)
- `XS-Leak` — 1 analysed file(s)
- `Zip Slip` — 1 analysed file(s)
- `_template_vuln` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `08ea40e77db3f42ef8f20c65196f3936a19b6c86` is the revision these paths and observations refer to.
