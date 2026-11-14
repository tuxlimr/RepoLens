# Project structure: trailofbits/algo

**Analysed commit:** `4a1be750cb3f8e509663c1a389f9c55bb0e6a05c`

**Commit reference:** [4a1be750cb3f8e509663c1a389f9c55bb0e6a05c](https://github.com/trailofbits/algo/commit/4a1be750cb3f8e509663c1a389f9c55bb0e6a05c)

**Tree at this commit:** [trailofbits/algo@4a1be750cb3f](https://github.com/trailofbits/algo/tree/4a1be750cb3f8e509663c1a389f9c55bb0e6a05c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | trailofbits/algo |
| Description | Set up a personal VPN in the cloud |
| Stars | 30470 |
| Forks | 2375 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `4a1be750cb3f8e509663c1a389f9c55bb0e6a05c` |
| Retrieved at | 2026-11-14T19:07:09.572717+00:00 |
| Files in this snapshot | 276 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  actions/  (1 files)
    setup-uv/  (1 files)
      … 1 files under this directory
  workflows/  (3 files)
    docker-image.yaml
    integration-tests.yml
    main.yml
  FUNDING.yml
  dependabot.yml
configs/  (1 files)
  .gitinit
docs/  (31 files)
  aws-credentials.md
  client-android.md
  client-apple-ipsec.md
  client-linux-ipsec.md
  client-linux-wireguard.md
  client-linux.md
  client-macos-wireguard.md
  client-openwrt-router-wireguard.md
  client-windows.md
  cloud-alternative-ingress-ip.md
  cloud-amazon-ec2.md
  cloud-azure.md
  cloud-cloudstack.md
  cloud-do.md
  cloud-gce.md
  cloud-hetzner.md
  cloud-linode.md
  cloud-scaleway.md
  cloud-vultr.md
  deploy-from-ansible.md
  deploy-from-cloudshell.md
  deploy-from-docker.md
  deploy-from-macos.md
  deploy-from-script-or-cloud-init-to-localhost.md
  … 7 more files
files/  (4 files)
  cloud-init/  (4 files)
    README.md
    base.sh
    base.yml
    sshd_config
library/  (4 files)
  gcp_compute_location_info.py
  lightsail_region_facts.py
  scaleway_instance.py
  x25519_pubkey.py
playbooks/  (8 files)
  tmpfs/  (4 files)
    linux.yml
    macos.yml
    main.yml
    umount.yml
  cloud-post.yml
  cloud-pre.yml
  rescue.yml
  user-preflight.yml
roles/  (138 files)
  client/  (8 files)
    files/  (1 files)
      … 1 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    tasks/  (6 files)
      … 6 files under this directory
  cloud-azure/  (7 files)
    tasks/  (6 files)
      … 6 files under this directory
    templates/  (1 files)
      … 1 files under this directory
  cloud-cloudstack/  (3 files)
    tasks/  (3 files)
      … 3 files under this directory
  cloud-digitalocean/  (3 files)
    tasks/  (3 files)
      … 3 files under this directory
  cloud-ec2/  (6 files)
    defaults/  (1 files)
      … 1 files under this directory
    tasks/  (4 files)
      … 4 files under this directory
    templates/  (1 files)
      … 1 files under this directory
  cloud-gce/  (3 files)
    tasks/  (3 files)
      … 3 files under this directory
  cloud-hetzner/  (3 files)
    tasks/  (3 files)
      … 3 files under this directory
  cloud-lightsail/  (5 files)
    tasks/  (4 files)
      … 4 files under this directory
    templates/  (1 files)
      … 1 files under this directory
  cloud-linode/  (5 files)
    defaults/  (1 files)
      … 1 files under this directory
    tasks/  (4 files)
      … 4 files under this directory
  cloud-openstack/  (2 files)
    tasks/  (2 files)
      … 2 files under this directory
  cloud-scaleway/  (4 files)
    defaults/  (1 files)
      … 1 files under this directory
    tasks/  (3 files)
      … 3 files under this directory
  cloud-vultr/  (3 files)
    tasks/  (3 files)
      … 3 files under this directory
  common/  (17 files)
    defaults/  (1 files)
      … 1 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    tasks/  (9 files)
      … 9 files under this directory
    templates/  (6 files)
      … 6 files under this directory
  dns/  (13 files)
    defaults/  (1 files)
      … 1 files under this directory
    files/  (1 files)
      … 1 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    tasks/  (3 files)
      … 3 files under this directory
    templates/  (7 files)
      … 7 files under this directory
  local/  (2 files)
    tasks/  (2 files)
      … 2 files under this directory
  privacy/  (22 files)
    defaults/  (1 files)
      … 1 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    tasks/  (6 files)
      … 6 files under this directory
    templates/  (13 files)
      … 13 files under this directory
    README.md
  ssh_tunneling/  (4 files)
    defaults/  (1 files)
      … 1 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    tasks/  (1 files)
      … 1 files under this directory
    templates/  (1 files)
      … 1 files under this directory
  strongswan/  (17 files)
    defaults/  (1 files)
      … 1 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    meta/  (1 files)
      … 1 files under this directory
    tasks/  (6 files)
      … 6 files under this directory
    templates/  (8 files)
      … 8 files under this directory
  wireguard/  (11 files)
    defaults/  (1 files)
      … 1 files under this directory
    handlers/  (1 files)
      … 1 files under this directory
    tasks/  (5 files)
      … 5 files under this directory
    templates/  (4 files)
      … 4 files under this directory
scripts/  (2 files)
  lint.sh
  list_servers.py
tests/  (48 files)
  e2e/  (2 files)
    README.md
    test-vpn-connectivity.sh
  fixtures/  (2 files)
    __init__.py
    test_variables.yml
  library/  (2 files)
    test_scaleway_instance.py
    test_x25519_pubkey.py
  network/  (4 files)
    conftest.py
    test_cloud_firewalls.py
    test_dns_rebinding.py
    test_firewall.py
  unit/  (15 files)
    test_ansible_12_boolean_fix.py
    test_basic_sanity.py
    test_cloud_provider_configs.py
    test_comprehensive_boolean_scan.py
    test_destroy.py
    test_double_templating.py
    test_iptables_rules.py
    test_lightsail_boto3_fix.py
    test_list_servers.py
    test_scaleway_fix.py
    test_strongswan_hardening.py
    test_strongswan_templates.py
    test_template_rendering.py
    test_unattended_upgrades_origins.py
    test_yaml_jinja2_expressions.py
  README.md
  ansible-smoke.yml
  cloud_module_smoke.py
  conftest.py
  docker_wrapper.py
  test-aws-credentials.yml
  test_adblock.py
  test_algo_launcher.py
  test_ansible_smoke.py
  test_aws_collections.py
  test_azure_preflight.py
  test_cloud_dependencies.py
  test_destroy_dependencies.py
  test_destroy_paths.py
  test_hetzner_locations.py
  test_ipsec_certificate_chain.py
  test_linode_teardown.py
  test_openstack.py
  test_privacy_services.py
  test_provider_install.py
  test_region_persistence.py
  test_user_preflight.py
  test_wireguard_qr.py
.ansible-lint
.dockerignore
.gitignore
.pre-commit-config.yaml
.yamllint
CLAUDE.md
CODEOWNERS
CONTRIBUTING.md
Dockerfile
LICENSE
PULL_REQUEST_TEMPLATE.md
README.md
SECURITY.md
algo
algo-docker.sh
algo-showenv.sh
algo.ps1
ansible.cfg
cloud.yml
config.cfg
deploy_client.yml
destroy.yml
input.yml
install.sh
… 7 more files
```

## Entry points

- [library/gcp_compute_location_info.py:90](https://github.com/trailofbits/algo/blob/4a1be750cb3f8e509663c1a389f9c55bb0e6a05c/library/gcp_compute_location_info.py#L90)
- [library/lightsail_region_facts.py:101](https://github.com/trailofbits/algo/blob/4a1be750cb3f8e509663c1a389f9c55bb0e6a05c/library/lightsail_region_facts.py#L101)
- [library/scaleway_instance.py:246](https://github.com/trailofbits/algo/blob/4a1be750cb3f8e509663c1a389f9c55bb0e6a05c/library/scaleway_instance.py#L246)
- [library/x25519_pubkey.py:101](https://github.com/trailofbits/algo/blob/4a1be750cb3f8e509663c1a389f9c55bb0e6a05c/library/x25519_pubkey.py#L101)
- [scripts/list_servers.py:33](https://github.com/trailofbits/algo/blob/4a1be750cb3f8e509663c1a389f9c55bb0e6a05c/scripts/list_servers.py#L33)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 115 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ScalewayInstance. Observed top-level functions: collection, fetch_list, list_servers, main… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| files package | library | Observed | Groups 1 file(s) under files package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 48 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CertificateDeployment, LinodeAPIHandler, MockAnsibleModule, TestAnsible12BooleanFix, TestComprehensiveBoole… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actions/setup-uv/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docker-image.yaml` (ci)
- `.github/workflows/integration-tests.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `Dockerfile` (container)
- `ansible.cfg` (config)
- `cloud.yml` (config)
- `config.cfg` (config)
- `deploy_client.yml` (config)
- `destroy.yml` (config)
- `files/cloud-init/base.yml` (config)
- `input.yml` (config)
- `main.yml` (config)
- `playbooks/cloud-post.yml` (config)
- `playbooks/cloud-pre.yml` (config)
- `playbooks/rescue.yml` (config)
- `playbooks/tmpfs/linux.yml` (config)
- `playbooks/tmpfs/macos.yml` (config)
- `playbooks/tmpfs/main.yml` (config)
- `playbooks/tmpfs/umount.yml` (config)
- `playbooks/user-preflight.yml` (config)
- `pyproject.toml` (manifest)
- `requirements.yml` (config)
- `roles/client/handlers/main.yml` (config)
- `roles/client/tasks/main.yml` (config)
- `roles/client/tasks/systems/CentOS.yml` (config)
- `roles/client/tasks/systems/Debian.yml` (config)
- `roles/client/tasks/systems/Fedora.yml` (config)
- `roles/client/tasks/systems/Ubuntu.yml` (config)
- `roles/client/tasks/systems/main.yml` (config)
- `roles/cloud-azure/tasks/auth.yml` (config)
- `roles/cloud-azure/tasks/destroy.yml` (config)
- `roles/cloud-azure/tasks/main.yml` (config)
- `roles/cloud-azure/tasks/prompts.yml` (config)
- `roles/cloud-azure/tasks/regions.yml` (config)
- `roles/cloud-azure/tasks/select_region.yml` (config)
- `roles/cloud-cloudstack/tasks/destroy.yml` (config)
- `roles/cloud-cloudstack/tasks/main.yml` (config)
- `roles/cloud-cloudstack/tasks/prompts.yml` (config)
- `roles/cloud-digitalocean/tasks/destroy.yml` (config)
- `roles/cloud-digitalocean/tasks/main.yml` (config)
- `roles/cloud-digitalocean/tasks/prompts.yml` (config)
- `roles/cloud-ec2/defaults/main.yml` (config)
- `roles/cloud-ec2/tasks/cloudformation.yml` (config)
- `roles/cloud-ec2/tasks/destroy.yml` (config)
- `roles/cloud-ec2/tasks/main.yml` (config)
- `roles/cloud-ec2/tasks/prompts.yml` (config)
- `roles/cloud-gce/tasks/destroy.yml` (config)
- `roles/cloud-gce/tasks/main.yml` (config)
- `roles/cloud-gce/tasks/prompts.yml` (config)
- `roles/cloud-hetzner/tasks/destroy.yml` (config)
- `roles/cloud-hetzner/tasks/main.yml` (config)
- `roles/cloud-hetzner/tasks/prompts.yml` (config)
- `roles/cloud-lightsail/tasks/cloudformation.yml` (config)
- `roles/cloud-lightsail/tasks/destroy.yml` (config)
- `roles/cloud-lightsail/tasks/main.yml` (config)
- `roles/cloud-lightsail/tasks/prompts.yml` (config)
- `roles/cloud-linode/defaults/main.yml` (config)
- `roles/cloud-linode/tasks/auth.yml` (config)
- `roles/cloud-linode/tasks/destroy.yml` (config)
- `roles/cloud-linode/tasks/main.yml` (config)
- `roles/cloud-linode/tasks/prompts.yml` (config)
- `roles/cloud-openstack/tasks/destroy.yml` (config)
- `roles/cloud-openstack/tasks/main.yml` (config)
- `roles/cloud-scaleway/defaults/main.yml` (config)
- `roles/cloud-scaleway/tasks/destroy.yml` (config)
- `roles/cloud-scaleway/tasks/main.yml` (config)
- `roles/cloud-scaleway/tasks/prompts.yml` (config)
- `roles/cloud-vultr/tasks/destroy.yml` (config)
- `roles/cloud-vultr/tasks/main.yml` (config)
- `roles/cloud-vultr/tasks/prompts.yml` (config)
- `roles/common/defaults/main.yml` (config)
- `roles/common/handlers/main.yml` (config)
- `roles/common/tasks/aip/digitalocean.yml` (config)
- `roles/common/tasks/aip/main.yml` (config)
- `roles/common/tasks/aip/placeholder.yml` (config)
- `roles/common/tasks/facts.yml` (config)
- `roles/common/tasks/iptables.yml` (config)
- `roles/common/tasks/main.yml` (config)
- `roles/common/tasks/packages.yml` (config)
- `roles/common/tasks/ubuntu.yml` (config)
- `roles/common/tasks/unattended-upgrades.yml` (config)
- `roles/dns/defaults/main.yml` (config)
- `roles/dns/handlers/main.yml` (config)
- `roles/dns/tasks/dns_adblocking.yml` (config)
- `roles/dns/tasks/main.yml` (config)
- `roles/dns/tasks/ubuntu.yml` (config)
- `roles/local/tasks/main.yml` (config)
- `roles/local/tasks/prompts.yml` (config)
- `roles/privacy/defaults/main.yml` (config)
- `roles/privacy/handlers/main.yml` (config)
- `roles/privacy/tasks/advanced_privacy.yml` (config)
- `roles/privacy/tasks/auto_cleanup.yml` (config)
- `roles/privacy/tasks/clear_history.yml` (config)
- `roles/privacy/tasks/log_filtering.yml` (config)
- `roles/privacy/tasks/log_rotation.yml` (config)
- `roles/privacy/tasks/main.yml` (config)
- `roles/ssh_tunneling/defaults/main.yml` (config)
- `roles/ssh_tunneling/handlers/main.yml` (config)
- `roles/ssh_tunneling/tasks/main.yml` (config)
- `roles/strongswan/defaults/main.yml` (config)
- `roles/strongswan/handlers/main.yml` (config)
- `roles/strongswan/meta/main.yml` (config)
- `roles/strongswan/tasks/client_configs.yml` (config)
- `roles/strongswan/tasks/distribute_keys.yml` (config)
- `roles/strongswan/tasks/ipsec_configuration.yml` (config)
- `roles/strongswan/tasks/main.yml` (config)
- `roles/strongswan/tasks/openssl.yml` (config)
- `roles/strongswan/tasks/ubuntu.yml` (config)
- `roles/wireguard/defaults/main.yml` (config)
- `roles/wireguard/handlers/main.yml` (config)
- `roles/wireguard/tasks/keys.yml` (config)
- `roles/wireguard/tasks/main.yml` (config)
- `roles/wireguard/tasks/mobileconfig.yml` (config)
- `roles/wireguard/tasks/qr.yml` (config)
- `roles/wireguard/tasks/ubuntu.yml` (config)
- `server.yml` (config)
- `users.yml` (config)
- `zizmor.yml` (config)

## Top-level layout

- `roles` — 138 analysed file(s)
- `tests` — 48 analysed file(s)
- `(root files)` — 31 analysed file(s)
- `docs` — 31 analysed file(s)
- `.github` — 9 analysed file(s)
- `playbooks` — 8 analysed file(s)
- `files` — 4 analysed file(s)
- `library` — 4 analysed file(s)
- `scripts` — 2 analysed file(s)
- `configs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4a1be750cb3f8e509663c1a389f9c55bb0e6a05c` is the revision these paths and observations refer to.
