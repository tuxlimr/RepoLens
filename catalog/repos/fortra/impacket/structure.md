# Project structure: fortra/impacket

**Analysed commit:** `5648c3776b3ebbfc2d3aff645b6c572afa398597`

**Commit reference:** [5648c3776b3ebbfc2d3aff645b6c572afa398597](https://github.com/fortra/impacket/commit/5648c3776b3ebbfc2d3aff645b6c572afa398597)

**Tree at this commit:** [fortra/impacket@5648c3776b3e](https://github.com/fortra/impacket/tree/5648c3776b3ebbfc2d3aff645b6c572afa398597)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fortra/impacket |
| Description | Impacket is a collection of Python classes for working with network protocols. |
| Stars | 16263 |
| Forks | 3989 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `5648c3776b3ebbfc2d3aff645b6c572afa398597` |
| Retrieved at | 2026-11-14T19:08:50.647705+00:00 |
| Files in this snapshot | 374 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
  workflows/  (2 files)
    build_and_test.yml
    labeler.yml
  labeler.yml
examples/  (70 files)
  CheckLDAPStatus.py
  DumpNTLMInfo.py
  Get-GPPPassword.py
  GetADComputers.py
  GetADUsers.py
  GetLAPSPassword.py
  GetNPUsers.py
  GetUserSPNs.py
  addcomputer.py
  atexec.py
  attrib.py
  badsuccessor.py
  changepasswd.py
  checkMSSQLStatus.py
  dacledit.py
  dcomexec.py
  describeTicket.py
  dpapi.py
  dpapidump.py
  esentutl.py
  exchanger.py
  filetime.py
  findDelegation.py
  getArch.py
  … 46 more files
impacket/  (170 files)
  dcerpc/  (45 files)
    v5/  (44 files)
      … 44 files under this directory
    __init__.py
  examples/  (67 files)
    ntlmrelayx/  (56 files)
      … 56 files under this directory
    __init__.py
    ldap_shell.py
    logger.py
    mssqlshell.py
    os_ident.py
    regsecrets.py
    remcomsvc.py
    rpcdatabase.py
    serviceinstall.py
    smbclient.py
    utils.py
  krb5/  (12 files)
    __init__.py
    asn1.py
    ccache.py
    constants.py
    crypto.py
    gssapi.py
    kerberosv5.py
    keytab.py
    kpasswd.py
    pac.py
    pkinit.py
    types.py
  ldap/  (4 files)
    __init__.py
    ldap.py
    ldapasn1.py
    ldaptypes.py
  mssql/  (1 files)
    version.py
  Dot11Crypto.py
  Dot11KeyManager.py
  ICMP6.py
  IP6.py
  IP6_Address.py
  IP6_Extension_Headers.py
  ImpactDecoder.py
  ImpactPacket.py
  NDP.py
  __init__.py
  acl.py
  cdp.py
  crypto.py
  dhcp.py
  dns.py
  dot11.py
  dpapi.py
  dpapi_ng.py
  eap.py
  ese.py
  helper.py
  http.py
  mqtt.py
  msada_guids.py
  … 17 more files
tests/  (118 files)
  ImpactPacket/  (13 files)
    __init__.py
    test_ICMP6.py
    test_IP.py
    test_IP6.py
    test_IP6_Address.py
    test_IP6_Extension_Headers.py
    test_IP_fragment_issue2095.py
    test_IP_option_issue990.py
    test_LinuxSLL.py
    test_TCP.py
    test_TCP_bug_issue7.py
    test_bootp_issue1900.py
    test_ethernet.py
  SMB_RPC/  (17 files)
    __init__.py
    test_acl.py
    test_ldap.py
    test_ndr.py
    test_negoex.py
    test_nmb.py
    test_ntlm.py
    test_ntlmrelayx_negoex_servers.py
    test_rpch.py
    test_rpcrt.py
    test_secretsdump.py
    test_smb.py
    test_smb3.py
    test_smbserver.py
    test_spnego.py
    test_spnego_negoex.py
    test_wmi.py
  dcerpc/  (24 files)
    __init__.py
    test_bkrp.py
    test_dcomrt.py
    test_dhcpm.py
    test_drsuapi.py
    test_epm.py
    test_even.py
    test_even6.py
    test_fasp.py
    test_fsrvp.py
    test_lsad.py
    test_lsat.py
    test_mgmt.py
    test_mimilib.py
    test_nrpc.py
    test_par.py
    test_raa.py
    test_rprn.py
    test_rrp.py
    test_samr.py
    test_scmr.py
    test_srvs.py
    test_tsch.py
    test_wkst.py
  dot11/  (29 files)
    __init__.py
    test_Dot11Base.py
    test_Dot11Decoder.py
    test_Dot11HierarchicalUpdate.py
    test_FrameControlACK.py
    test_FrameControlCFEnd.py
    test_FrameControlCFEndCFACK.py
    test_FrameControlCTS.py
    test_FrameControlPSPoll.py
    test_FrameControlRTS.py
    test_FrameData.py
    test_FrameManagement.py
    test_FrameManagementAssociationRequest.py
    test_FrameManagementAssociationResponse.py
    test_FrameManagementAuthentication.py
    test_FrameManagementDeauthentication.py
    test_FrameManagementDisassociation.py
    test_FrameManagementProbeRequest.py
    test_FrameManagementProbeResponse.py
    test_FrameManagementReassociationRequest.py
    test_FrameManagementReassociationResponse.py
    test_RadioTap.py
    test_RadioTapDecoder.py
    test_WEPDecoder.py
    … 5 more files
  misc/  (31 files)
    __init__.py
    test_addcomputer.py
    test_ccache.py
    test_changepasswd.py
    test_crypto.py
    test_dcerpc_v5_ndr.py
    test_dns.py
    test_dpapi.py
    test_ese.py
    test_ip6_address.py
    test_kerberosv5.py
    test_keylist_pac.py
    test_krb5_crypto.py
    test_krb5_gssapi.py
    test_ldap_channel_binding.py
    test_ldap_schannel.py
    test_ntfs_read.py
    test_ntlmrelayx_adcs.py
    test_ntlmrelayx_ces.py
    test_ntlmrelayx_reauth_bypass.py
    test_pac_helpers.py
    test_pkinit.py
    test_socksserver.py
    test_structure.py
    … 7 more files
  __init__.py
  conftest.py
  dcetests.cfg.template
  walkmodules.py
.gitignore
ChangeLog.md
Dockerfile
LICENSE
MANIFEST.in
README.md
SECURITY.md
TESTING.md
requirements-test.txt
requirements.txt
setup.py
tox.ini
```

## Entry points

- [impacket/dcerpc/v5/dcom/wmi.py:3471](https://github.com/fortra/impacket/blob/5648c3776b3ebbfc2d3aff645b6c572afa398597/impacket/dcerpc/v5/dcom/wmi.py#L3471)
- [impacket/dcerpc/v5/drsuapi.py:1494](https://github.com/fortra/impacket/blob/5648c3776b3ebbfc2d3aff645b6c572afa398597/impacket/dcerpc/v5/drsuapi.py#L1494)
- [impacket/dcerpc/v5/mimilib.py:220](https://github.com/fortra/impacket/blob/5648c3776b3ebbfc2d3aff645b6c572afa398597/impacket/dcerpc/v5/mimilib.py#L220)
- [impacket/krb5/ccache.py:877](https://github.com/fortra/impacket/blob/5648c3776b3ebbfc2d3aff645b6c572afa398597/impacket/krb5/ccache.py#L877)
- [impacket/krb5/types.py:274](https://github.com/fortra/impacket/blob/5648c3776b3ebbfc2d3aff645b6c572afa398597/impacket/krb5/types.py#L274)
- [impacket/mqtt.py:397](https://github.com/fortra/impacket/blob/5648c3776b3ebbfc2d3aff645b6c572afa398597/impacket/mqtt.py#L397)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: NTLMRelayxConfig. Observed top-level functions: parse_listening_ports, read. |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: ATTR, ATTRBLOCK, ATTRTYP_ARRAY, ATTRVAL, AT… |
| External integrations | external | Observed | Groups 10 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: DCSYNCRelayClient, DCSYNCRelayClientException, DummyOp, HTTPRelayClient, HTTPSRelayClient,… |
| impacket package | library | Observed | Groups 152 file(s) under impacket package (observed from repository paths and static analysis). Observed top-level classes: ACCESS_ALLOWED_ACE, ACCESS_ALLOWED_CALLBACK_ACE, ACCESS_ALLOWED_CALLBACK_OBJECT_ACE, ACCESS_ALL… |
| Tests | test | Observed | Groups 118 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH impacket.acl.lsat.hLsarLookupNames3. Observed top-level classes: ADCSCertificateSigningRequestTests, AESTests,… |

## Important files

- `.github/labeler.yml` (config)
- `.github/workflows/build_and_test.yml` (ci)
- `.github/workflows/labeler.yml` (ci)
- `Dockerfile` (container)
- `MANIFEST.in` (manifest)
- `requirements-test.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)

## Top-level layout

- `impacket` — 170 analysed file(s)
- `tests` — 118 analysed file(s)
- `examples` — 70 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5648c3776b3ebbfc2d3aff645b6c572afa398597` is the revision these paths and observations refer to.
