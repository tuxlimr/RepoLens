# Project structure: mukul975/Anthropic-Cybersecurity-Skills

**Analysed commit:** `54a798831d2266a3ca61ce68a7acb80b81160d57`

**Commit reference:** [54a798831d2266a3ca61ce68a7acb80b81160d57](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/commit/54a798831d2266a3ca61ce68a7acb80b81160d57)

**Tree at this commit:** [mukul975/Anthropic-Cybersecurity-Skills@54a798831d22](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/tree/54a798831d2266a3ca61ce68a7acb80b81160d57)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mukul975/Anthropic-Cybersecurity-Skills |
| Description | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF & MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 29 security domains ·… |
| Stars | 36139 |
| Forks | 4422 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `54a798831d2266a3ca61ce68a7acb80b81160d57` |
| Retrieved at | 2026-11-14T19:06:55.406258+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.github/  (12 files)
  ISSUE_TEMPLATE/  (6 files)
    bug-report.yml
    config.yml
    improve-skill.md
    new-skill-request.yml
    new-skill.md
    skill-improvement.yml
  workflows/  (4 files)
    sync-marketplace-version.yml
    update-contributors.yml
    update-index.yml
    validate-skills.yml
  FUNDING.yml
  copilot-instructions.md
assets/  (1 files)
  .gitkeep
docs/  (1 files)
  mitre-f3-mapping.md
mappings/  (7 files)
  mitre-attack/  (2 files)
    README.md
    coverage-summary.md
  nist-csf/  (2 files)
    README.md
    csf-alignment.md
  owasp/  (1 files)
    README.md
  README.md
  attack-navigator-layer.json
skills/  (765 files)
  abusing-dpapi-for-credential-access/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  abusing-shadow-credentials-for-privesc/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  achieving-cmmc-level-2-compliance/  (5 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  acquiring-disk-image-with-dd-and-dcfldd/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-active-directory-acl-abuse/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-android-malware-with-apktool/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-api-gateway-access-logs/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-apt-group-with-mitre-navigator/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-azure-activity-logs-for-threats/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-bootkit-and-rootkit-samples/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-browser-forensics-with-hindsight/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-campaign-attribution-evidence/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-certificate-transparency-for-phishing/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-cloud-storage-access-patterns/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-cobalt-strike-beacon-configuration/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-cobaltstrike-malleable-c2-profiles/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-command-and-control-communication/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-cyber-kill-chain/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-disk-image-with-autopsy/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-dns-logs-for-exfiltration/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-docker-container-forensics/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-email-headers-for-phishing-investigation/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-ethereum-smart-contract-vulnerabilities/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-golang-malware-with-ghidra/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-heap-spray-exploitation/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-indicators-of-compromise/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-ios-app-security-with-objection/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-kubernetes-audit-logs/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-linux-audit-logs-for-intrusion/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-linux-elf-malware/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-linux-kernel-rootkits/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-linux-system-artifacts/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-lnk-file-and-jump-list-artifacts/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-macro-malware-in-office-documents/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-malicious-pdf-with-peepdf/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-malicious-url-with-urlscan/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-malware-behavior-with-cuckoo-sandbox/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-malware-family-relationships-with-malpedia/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-malware-persistence-with-autoruns/  (7 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-malware-sandbox-evasion-techniques/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-memory-dumps-with-volatility/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-memory-forensics-with-lime-and-volatility/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-mft-for-deleted-file-recovery/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-network-covert-channels-in-malware/  (7 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-network-flow-data-with-netflow/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-network-packets-with-scapy/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-network-traffic-for-incidents/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-network-traffic-of-malware/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-network-traffic-with-wireshark/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-office365-audit-logs-for-compromise/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-outlook-pst-for-email-forensics/  (6 files)
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-packed-malware-with-upx-unpacker/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-pdf-malware-with-pdfid/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-persistence-mechanisms-in-linux/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-powershell-empire-artifacts/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-powershell-script-block-logging/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-prefetch-files-for-execution-history/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-ransomware-encryption-mechanisms/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-ransomware-leak-site-intelligence/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-ransomware-network-indicators/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-ransomware-payment-wallets/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-sbom-for-supply-chain-vulnerabilities/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-security-logs-with-splunk/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-slack-space-and-file-system-artifacts/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-supply-chain-malware-artifacts/  (7 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-threat-actor-ttps-with-mitre-attack/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  analyzing-threat-actor-ttps-with-mitre-navigator/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-threat-intelligence-feeds/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-threat-landscape-with-misp/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-tls-certificate-transparency-logs/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-typosquatting-domains-with-dnstwist/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-uefi-bootkit-persistence/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-usb-device-connection-history/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-web-server-logs-for-intrusion/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-windows-amcache-artifacts/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-windows-event-logs-in-splunk/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-windows-lnk-files-for-artifacts/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-windows-prefetch-with-python/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-windows-registry-for-artifacts/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  analyzing-windows-shellbag-artifacts/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  assessing-vector-and-embedding-weaknesses/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  attacking-entra-id-with-roadtools/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  attacking-oauth-with-device-code-phishing/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-aws-s3-bucket-permissions/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-azure-active-directory-configuration/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-cloud-with-cis-benchmarks/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-entra-id-with-aadinternals/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-foundry-smart-contract-security/  (6 files)
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-gcp-iam-permissions/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-kubernetes-cluster-rbac/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-kubernetes-rbac-privilege-escalation/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-mcp-servers-for-tool-poisoning/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-terraform-infrastructure-for-security/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-tls-certificate-transparency-logs/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  auditing-uefi-firmware-with-chipsec/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  automating-ioc-enrichment/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  benchmarking-kubernetes-with-kube-bench/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-adversary-infrastructure-tracking-system/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-attack-pattern-library-from-cti-reports/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-automated-malware-submission-pipeline/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-c2-infrastructure-with-sliver-framework/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-c2-redirector-infrastructure/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-cloud-siem-with-sentinel/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-detection-rule-with-splunk-spl/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-detection-rules-with-sigma/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-devsecops-pipeline-with-gitlab-ci/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-identity-federation-with-saml-azure-ad/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-identity-governance-lifecycle-process/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-incident-response-dashboard/  (5 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.es.md
    SKILL.md
  building-incident-response-playbook/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-incident-timeline-with-timesketch/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-ioc-defanging-and-sharing-pipeline/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-ioc-enrichment-pipeline-with-opencti/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-malware-incident-communication-template/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-patch-tuesday-response-process/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-phishing-reporting-button-workflow/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-ransomware-playbook-with-cisa-framework/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-red-team-c2-infrastructure-with-havoc/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-role-mining-for-rbac-optimization/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-soc-escalation-matrix/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-soc-metrics-and-kpi-tracking/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-soc-playbook-for-ransomware/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-super-timelines-with-plaso/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-threat-actor-profile-from-osint/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-threat-feed-aggregation-with-misp/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-threat-hunt-hypothesis-framework/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-threat-intelligence-enrichment-in-splunk/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-threat-intelligence-feed-integration/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  building-threat-intelligence-platform/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-vulnerability-aging-and-sla-tracking/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-vulnerability-dashboard-with-defectdojo/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-vulnerability-exception-tracking-system/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  building-vulnerability-scanning-workflow/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  bypassing-authentication-with-forced-browsing/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  coercing-authentication-with-coercer-petitpotam/  (5 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  collecting-indicators-of-compromise/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  collecting-open-source-intelligence/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  collecting-threat-intelligence-with-misp/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  collecting-volatile-evidence-from-compromised-host/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  conducting-api-security-testing/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  conducting-cloud-incident-response/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  conducting-cloud-penetration-testing/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  conducting-cyber-risk-assessment-with-nist-800-30/  (5 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  conducting-domain-persistence-with-dcsync/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  conducting-external-reconnaissance-with-osint/  (4 files)
    references/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
  conducting-full-scope-red-team-engagement/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  conducting-gdpr-compliance-assessment/  (9 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    LICENSE
    SKILL.md
  conducting-internal-network-penetration-test/  (8 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    LICENSE
    SKILL.md
  conducting-internal-reconnaissance-with-bloodhound-ce/  (7 files)
    assets/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    LICENSE
    SKILL.md
.gitignore
AGENTS.md
ATTACK_COVERAGE.md
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.fr.md
README.md
SCOPE.md
SECURITY.md
SUPPORT.md
```

## Entry points

- [skills/abusing-dpapi-for-credential-access/scripts/agent.py:153](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/abusing-dpapi-for-credential-access/scripts/agent.py#L153)
- [skills/abusing-shadow-credentials-for-privesc/scripts/agent.py:144](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/abusing-shadow-credentials-for-privesc/scripts/agent.py#L144)
- [skills/achieving-cmmc-level-2-compliance/scripts/process.py:197](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/achieving-cmmc-level-2-compliance/scripts/process.py#L197)
- [skills/acquiring-disk-image-with-dd-and-dcfldd/scripts/agent.py:153](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/acquiring-disk-image-with-dd-and-dcfldd/scripts/agent.py#L153)
- [skills/analyzing-active-directory-acl-abuse/scripts/agent.py:257](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-active-directory-acl-abuse/scripts/agent.py#L257)
- [skills/analyzing-android-malware-with-apktool/scripts/agent.py:227](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-android-malware-with-apktool/scripts/agent.py#L227)
- [skills/analyzing-api-gateway-access-logs/scripts/agent.py:175](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-api-gateway-access-logs/scripts/agent.py#L175)
- [skills/analyzing-apt-group-with-mitre-navigator/scripts/agent.py:184](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-apt-group-with-mitre-navigator/scripts/agent.py#L184)
- [skills/analyzing-azure-activity-logs-for-threats/scripts/agent.py:177](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-azure-activity-logs-for-threats/scripts/agent.py#L177)
- [skills/analyzing-bootkit-and-rootkit-samples/scripts/agent.py:156](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-bootkit-and-rootkit-samples/scripts/agent.py#L156)
- [skills/analyzing-browser-forensics-with-hindsight/scripts/agent.py:215](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-browser-forensics-with-hindsight/scripts/agent.py#L215)
- [skills/analyzing-browser-forensics-with-hindsight/scripts/process.py:29](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/54a798831d2266a3ca61ce68a7acb80b81160d57/skills/analyzing-browser-forensics-with-hindsight/scripts/process.py#L29)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 184 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ATTACKAnalyzer, AttributionEngine, BeaconAnalyzer, DefectDojoClient, DetectionRuleLibrar… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/new-skill-request.yml` (config)
- `.github/ISSUE_TEMPLATE/skill-improvement.yml` (config)
- `.github/workflows/sync-marketplace-version.yml` (ci)
- `.github/workflows/update-contributors.yml` (ci)
- `.github/workflows/update-index.yml` (ci)
- `.github/workflows/validate-skills.yml` (ci)
- `mappings/attack-navigator-layer.json` (config)

## Top-level layout

- `skills` — 765 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 12 analysed file(s)
- `mappings` — 7 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `assets` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `54a798831d2266a3ca61ce68a7acb80b81160d57` is the revision these paths and observations refer to.
