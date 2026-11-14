# Project structure: python-telegram-bot/python-telegram-bot

**Analysed commit:** `41e3633bd1b4e51693ee57059828a59a9773618a`

**Commit reference:** [41e3633bd1b4e51693ee57059828a59a9773618a](https://github.com/python-telegram-bot/python-telegram-bot/commit/41e3633bd1b4e51693ee57059828a59a9773618a)

**Tree at this commit:** [python-telegram-bot/python-telegram-bot@41e3633bd1b4](https://github.com/python-telegram-bot/python-telegram-bot/tree/41e3633bd1b4e51693ee57059828a59a9773618a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | python-telegram-bot/python-telegram-bot |
| Description | We have made you a wrapper you can't refuse |
| Stars | 29594 |
| Forks | 6186 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `41e3633bd1b4e51693ee57059828a59a9773618a` |
| Retrieved at | 2026-11-14T19:07:11.751646+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (23 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.yml
    config.yml
    feature-request.yml
    question.yml
  workflows/  (15 files)
    assets/  (1 files)
      … 1 files under this directory
    chango.yml
    copilot-setup-steps.yml
    docs-admonitions.yml
    docs-linkcheck.yml
    gha_security.yml
    lock.yml
    prek.yml
    release_pypi.yml
    release_test_pypi.yml
    stale.yml
    test_official.yml
    type_completeness.yml
    type_completeness_monthly.yml
    unit_tests.yml
  CONTRIBUTING.rst
  copilot-instructions.md
  pull_request_template.md
  renovate.json5
changes/  (343 files)
  22.0_2025-03-15/  (11 files)
    4671.7B3boYRvHdGzsrZgkpKp7B.toml
    4672.G9szuJ7pRafycByfem2DrT.toml
    4697.GzyGCEgj74G6bTEDbuFjUU.toml
    4698.Fkzr3oU2qcFmFX28xfoja5.toml
    4699.LYAYfKXX7C7wqT54kRPnVy.toml
    4700.nm6R6YTnkmCo5evbykz4kz.toml
    4701.ah8Wi4SWc22EbgBc4KQeqH.toml
    4709.dbwPVaU8vSacVkMLhiMjyJ.toml
    4710.CSNixpvxJdLFaM6xSQ39Zf.toml
    4712.8ckkAPAXGzedityWEyv363.toml
    4719.d4xMztC8JjrbVgEscxvMWX.toml
  22.1_2025-05-15/  (21 files)
    4692.dVZs28GuwTFnNJdWkvPbNv.toml
    4730.GsSUQSXzV8TF2Wav4CXRdd.toml
    4733.BRLwsEuh76974FPJRuiBjf.toml
    4741.nVLBrFX4p8jTCBjMRqaYoQ.toml
    4742.oEA6MjYXMafdbu2akWT5tC.toml
    4743.SpMm4vvAMjEreykTcGwzcF.toml
    4744.a4tsF64kZPA2noP7HtTzTX.toml
    4745.emNmhxtvtTP9uLNQxpcVSj.toml
    4746.gWnX3BCxbvujQ8B2QejtTK.toml
    4747.MLmApvpGdwN7J24j7fXsDU.toml
    4748.j3cKusZZKqTLbc542K4sqJ.toml
    4756.JT5nmUmGRG6qDEh5ScMn5f.toml
    4758.dSyCdBJWEJroH2GynR2VaJ.toml
    4761.mmsngFA6b4ccdEzEpFTZS3.toml
    4762.PbcJGM8KPBMbKri3fdHKjh.toml
    4775.kkLon84t7Vy5REKRe9LwPH.toml
    4776.g83DxRk4WVWCC8rCd6ocFC.toml
    4777.Lhgz8xFtQjgrKM2KvNfxwD.toml
    4778.CeUSPNLbGGsqP2Vo4xKkdp.toml
    4779.UqcbJVKYxwTtrBEGDgb3VS.toml
    4791.QycEvQbiaiJKraKDhAfFWM.toml
  22.2_2025-06-29/  (21 files)
    4750.jJBu7iAgZa96hdqcpHK96W.toml
    4792.YsK6LmbEhZv6y3dvhHbXD7.toml
    4793.mDR5p3mrSmPFQkvWFGWBmD.toml
    4798.g7G3jRf2ns4ath9LRFEcit.toml
    4800.2Z9Q8uvzdU2TqMJ9biBLam.toml
    4801.feKaYKKZTZq2KBjhyxVVAM.toml
    4802.RMLufX4UazobYg5aZojyoD.toml
    4810.KyRnffWk3ARyQFNcF88Uh3.toml
    4811.TQgVr5Sa6uDFtWXdTS5wfw.toml
    4812.i4aqsTfCkdEs8uYNYS59si.toml
    4813.cnbzL2eSRzj3i9NcUMFyFo.toml
    4814.RMQVXTNywcpBQ3HkX2TuyA.toml
    4815.9dLSFHFozQiAM7oCpX4NyL.toml
    4816.hhYVDfdzUgoQoMNRKkCDjb.toml
    4817.ZHx38jvj9zKRNZfQh9Xrpb.toml
    4818.3VPDqqEWEhDCrTipFY8KKU.toml
    4820.7bFkjLSeWKdNVhThPpVMAT.toml
    4822.DrW3tJ3KoB8kTmHtNnNEpQ.toml
    4825.R7wiTzvN37KAV656s9kfnC.toml
    4830.EZzGEAk7DiFuedKPoQMMvd.toml
    4834.oBWsiGWNMuoSXvJNom6N6A.toml
  22.3_2025-07-20/  (11 files)
    4837.cVTsY7pxfQqgVXfFW9hgZK.toml
    4839.gExNhF7C6kR5VrBg6cBaar.toml
    4840.jz9uGugc5DUd8x8pQHPyzg.toml
    4841.HHVCCXXZbYAaaQVmKHCJm2.toml
    4842.PSW9ZbxENhwfRhbSfemCwE.toml
    4843.f5aZ5Vpxevw8fEEudawU5u.toml
    4847.8ujbbBbaZ2VTEdRLeqirSZ.toml
    4852.mz3RDjX636ZdGoR456C6v9.toml
    4855.8hCFRFMeMaRWpBEYaxrTMq.toml
    4858.ajt46xDsbfzFqcghJ2rP6g.toml
    4870.QeVo4BE5TNouLRJjCFbRMo.toml
  22.4_2025-09-13/  (29 files)
    4869.7GK56NC89XswBFUCiWXtqc.toml
    4875.29srP6fENz7FrGGoWSkPNa.toml
    4878.AbGo6aozTWquUjnzzpSdyX.toml
    4879.kABAi45KpR2H6jqJu6NtDS.toml
    4880.42PW26hGpLypMJMxTeiQZ6.toml
    4881.dJNT656MVxJk9DgcoRePip.toml
    4882.JpgQAHHnCponMKStbC4JsG.toml
    4884.ADcdCj6GrMaKffYSLzWdsL.toml
    4886.XSHPk83uhDQdYzurbb4xx9.toml
    4887.5yypYZV7Sq5PN4ihmf2NUr.toml
    4890.oCzELerGo8dqPygShWMV9S.toml
    4892.iRGvURLUGiMSMEDfdpP5jB.toml
    4893.Fbkdqj4bmTTH6e54gRPwvc.toml
    4894.PLQSCgnKXygrGdkekTbx8q.toml
    4895.UECAN369MCuQaLnTmtYFGr.toml
    4896.R92Xq7W6PDbabuk6aZ5FZt.toml
    4906.Fju7LDJgwCz2sxgQy9muBG.toml
    4908.KnwujH2JruNRZSrTTvvc9B.toml
    4911.kiF45Y4cfPGMq5cuLpa5da.toml
    4915.D3x6MoyYYDaUcB7jmLUyeY.toml
    4923.AEztvspxU4Ajz7N3ms56Wq.toml
    4925.FCwe9rrjgv5GmfvuhHXjHg.toml
    4926.GMcTfT2hSAdmdT7wi73mzZ.toml
    4927.mHtL79KfGaRw3LEMdHN6Ry.toml
    … 5 more files
  22.5_2025-09-27/  (32 files)
    4861.HEoGVs2mYXWzqMahi6SEhV.toml
    4938.U2x6X7ZGikYv5eo9aUSNGc.toml
    4943.DdNTkLjQbNGeG3nEBGHjBo.toml
    4944.mYorcTojrvwihYQ5NPwNcE.toml
    4945.LDiTvYjbXuQBp7kLyQMYa5.toml
    4946.KujJLUNcND72Y8aKs3bzSx.toml
    4947.CcLd8YTb8XaANn8gQXruNb.toml
    4948.ernZikrNEarFtTZgLN7huS.toml
    4949.YhMnQj57Qpm9HD5zkkhfZC.toml
    4950.VA9pgTVrLPABkUrxifLZnh.toml
    4951.7ZExRZuEwEoGXX5FMPWctm.toml
    4952.bVCE8YehtKGcwLYdiXkmQb.toml
    4953.8aPTEQhSPSgTrguzvsw4tq.toml
    4954.XrYn8gzjeQF9LoPQomutuW.toml
    4955.2BXmasa9Ms9vqXngSMKSVX.toml
    4958.ktVtuEvzAxxFxSwk7KXQ66.toml
    4959.H2BCKBh9WXaoFKmwiMX4m7.toml
    4960.KyngeakT6uHLQXYftm2Cpe.toml
    4961.nd2KdJpSCyLC3K5xninxZL.toml
    4962.mZAGRv4sXnpirJCkrKniVJ.toml
    4964.KbKLtQ5MYHdt49gpBxCaja.toml
    4965.488hEhfeZfPvfZszvRKdkJ.toml
    4967.a9vCqXXpyAfzTb8TD7ouqB.toml
    4968.ecxiPBroDpMUkab6uBCUde.toml
    … 8 more files
  22.6_2026-01-24/  (68 files)
    4827.PBXyEEjvXz5sJbiDWkeGFX.toml
    4980.86EojeXUgUSi87JKMZojGD.toml
    4984.XKkS99HJWztHscs6N6wpEh.toml
    4985.LrPNHbexoHAmim6zXB9nMp.toml
    4986.fwbZif2YKWgeugPof8Fikj.toml
    4987.PLoqzvYm725uVfKcWhwuCb.toml
    4988.Lncn8TNDcQF4hLQZJvyzQY.toml
    4989.TjTuqb5LqcEXDLvArDzcEY.toml
    4990.HxHP2zqbTAcGzjapkgX3E5.toml
    4994.K8XVzJe4kuoHmc2yRsrYTb.toml
    4995.TGRtuG8BUqB6S9JxpPxiNR.toml
    4996.bRG2iuMsWDR47wDt556q57.toml
    4997.hJRqz3id5FnzSzPeMhY3k6.toml
    4998.jvTA7u2hEA7xwa87XoUqec.toml
    4999.NGTC66pJdAhjtoLykBsxQc.toml
    5000.A5P7pNDw2Bc5Uaq3psVEWZ.toml
    5001.DXjSVgk4h3o8WoPTy8Jpng.toml
    5002.cube9Ku57EajUDF8xoSdfV.toml
    5004.k7NzG5uTwQxcHP6shbogHL.toml
    5006.hRJtYPL4nBeZ43DWqii68V.toml
    5007.ANT5x4yXn667UnjSHsCSUb.toml
    5008.4XBBoZAXkrtsuHRxPqAW9V.toml
    5009.QuigkwxAs8bemB9gnKbXhz.toml
    5011.PSJLmKo5LhUXjPbnGbZ3bn.toml
    … 44 more files
  22.7_2026-03-16/  (41 files)
    5110.NfCAazzRFNXvNn9CNmMZpZ.toml
    5112.Na2dk8jzBTtTg3EvNSo6kh.toml
    5113.YfEbfC8WGAxMFb8rKBCUej.toml
    5114.LGfvVo5cdK74VyVWHFJDW3.toml
    5115.CgTBPjBCWJ7reRZG4vu8vJ.toml
    5116.9YKyNfUgP73QatTcuD5qNm.toml
    5117.ZoYfowizxLvCbfWcABcezC.toml
    5119.CA8avHeQnMdHNFQKvonFK6.toml
    5122.8DXxjQycntr4ecdcrcWZ7f.toml
    5122.EZ5hbq74CEoTbixKNcSmQz.toml
    5124.ZMLaT6JfSLD4orqRAqrZXj.toml
    5125.Shtxta26FemMvrpd3bWFeF.toml
    5135.7NGhdLCnjTdBHFpwbxdLQt.toml
    5137.AMrRwuXMvfMK8HHe3Udu9q.toml
    5140.jcXPuwWiM4zqtxGPWgYSoo.toml
    5142.h7G2mCUQ2PobeTyLNewpvx.toml
    5143.HYNP5H8WQXGydLcnAa2pkf.toml
    5145.3uQNphqhEArdGYLTFDSShP.toml
    5146.YwQ5dRVNyvkZ3mtmFQWtzJ.toml
    5150.6rzZ8vRQrj3NqDiyLjcuPY.toml
    5151.fvex2RmXotXPkFAXSxosHn.toml
    5152.TgxyAT2Wwb7DQpxKhWRdt4.toml
    5153.4vV6k9bXfCRAiY9m7VNk3s.toml
    5154.gRV9eXpMQPJHJb7idaBYXS.toml
    … 17 more files
  22.8_2026-06-12/  (38 files)
    5125.filter-fix.toml
    5177.fg9Y3ZSboi94mttv3eas2L.toml
    5183.Enoyw5yoT4S9uRxn7v5ud5.toml
    5184.YKdeCfWDDXk8v3DJx8nTeg.toml
    5185.VTFw6hNJ4A9mGayu2rduUt.toml
    5190.5mL9K6trXT6Y4vLgqxy9jE.toml
    5191.B6JK8KhgoqqawRrrWaSCDH.toml
    5192.VYDBGMwXeTVyvXESmEnfFa.toml
    5193.GqEK23Erwr49GQ79uJho38.toml
    5194.bnCTjH5QVYuyFDp4iCwJoV.toml
    5196.7keq7yJhXbMb9RyShLHz4D.toml
    5198.haofa4LoE6k2WQoAUSizM8.toml
    5199.4qywU9Faav8YhWivBBykyJ.toml
    5203.jxMZ7aSe7eDKXTvfEdZGzw.toml
    5205.KBqhJA9kouNAJmQYNwZHT2.toml
    5206.nXEjjZXrYZiWroBfBeQR3N.toml
    5209.msPrg8bYnmr89qXR4fr5bG.toml
    5217.5AVeFbQnudaXWyZ3TM7E5B.toml
    5220.iAgLEYgfuW46wtvCUx3dhM.toml
    5221.UEBLb7KFNwZkZ5fC3CyDBD.toml
    5222.dGHpTKrbVb9VQV8pVv9Lii.toml
    5223.6Ttu6UoyzkVQddzKrz947W.toml
    5224.YVKcje5xUdXTjJJurmAVVD.toml
    5229.87PBN4GFkuAaDhhgFwCYkY.toml
    … 14 more files
  unreleased/  (69 files)
    .gitkeep
    5186.VngJMeztfXKDXAhcqTxJjK.toml
    5264.X28jz5XU2gBXFoCpnQn7na.toml
    5265.o75uzmqPxDpYx8JwXRbqeF.toml
    5268.GKZnfBkMcLqBC4rTgznsnY.toml
    5271.H8posH7FA8X3BZrmC52ueg.toml
    5273.ZKFjVYwRse9MA9BuF4dUEW.toml
    5274.BMgKbj7LZwGKbx8jg6mzM4.toml
    5276.mYSU5bdepgvEnuztjTmcV3.toml
    5277.WktkduZbpMYLjqTRzcrphW.toml
    5278.eb9D9NeRPkyNoNusYAqe8D.toml
    5280.ithVrhgXtP4S774Mp4f2Dc.toml
    5283.4feBMWUxBfZdj4koEneVmA.toml
    5286.CdJJrjsRJHALMgiEZLeumT.toml
    5287.75WNudSbZQ2uPUwbwKLjrH.toml
    5288.C8AoiRWDdZmCZeiiz4Gujz.toml
    5289.MFnVwiitS3Kdrs6rv2De4a.toml
    5290.VrpedfUnvcaMn75byHfeSY.toml
    5291.79JdLrT5P97c9rDDxvrcob.toml
    5297.pickle-empty-flush.toml
    5298.webhook-html-escaping.toml
    5299.5mQXHwskDhSY3Rx6Nd26CR.toml
    5302.bhpiKviDS5QTSKncz35DN2.toml
    5303.7uN6w2W6EiLMn2KqzYyYNs.toml
    … 45 more files
  LEGACY.rst
  config.py
contrib/  (9 files)
  debian/  (8 files)
    source/  (2 files)
      … 2 files under this directory
    changelog
    compat
    control
    copyright
    install
    rules
  build-debian.sh
docs/  (414 files)
  auxil/  (6 files)
    __init__.py
    admonition_inserter.py
    bot_insertion.py
    link_code.py
    sphinx_hooks.py
    tg_const_role.py
  source/  (406 files)
    _static/  (7 files)
      … 7 files under this directory
    inclusions/  (4 files)
      … 4 files under this directory
    changelog.rst
    coc.rst
    conf.py
    contributing.rst
    examples.arbitrarycallbackdatabot.rst
    examples.chatmemberbot.rst
    examples.contexttypesbot.rst
    examples.conversationbot.rst
    examples.conversationbot2.rst
    examples.customwebhookbot.rst
    examples.deeplinking.rst
    examples.echobot.rst
    examples.errorhandlerbot.rst
    examples.inlinebot.rst
    examples.inlinekeyboard.rst
    examples.inlinekeyboard2.rst
    examples.nestedconversationbot.rst
    examples.passportbot.rst
    examples.paymentbot.rst
    examples.persistentconversationbot.rst
    examples.pollbot.rst
    examples.rawapibot.rst
    examples.rst
    examples.timerbot.rst
    … 371 more files
  Makefile
  __init__.py
.git-blame-ignore-revs
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
AUTHORS.rst
CODE_OF_CONDUCT.rst
LICENSE
LICENSE.dual
LICENSE.lesser
README.rst
codecov.yml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 342 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ChangoSectionChangeNote, CustomChango. |
| contrib package | library | Observed | Groups 1 file(s) under contrib package (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/workflows/assets/release_template.html` (ci)
- `.github/workflows/chango.yml` (ci)
- `.github/workflows/copilot-setup-steps.yml` (ci)
- `.github/workflows/docs-admonitions.yml` (ci)
- `.github/workflows/docs-linkcheck.yml` (ci)
- `.github/workflows/gha_security.yml` (ci)
- `.github/workflows/lock.yml` (ci)
- `.github/workflows/prek.yml` (ci)
- `.github/workflows/release_pypi.yml` (ci)
- `.github/workflows/release_test_pypi.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test_official.yml` (ci)
- `.github/workflows/type_completeness.yml` (ci)
- `.github/workflows/type_completeness_monthly.yml` (ci)
- `.github/workflows/unit_tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `changes/22.0_2025-03-15/4671.7B3boYRvHdGzsrZgkpKp7B.toml` (config)
- `changes/22.0_2025-03-15/4672.G9szuJ7pRafycByfem2DrT.toml` (config)
- `changes/22.0_2025-03-15/4697.GzyGCEgj74G6bTEDbuFjUU.toml` (config)
- `changes/22.0_2025-03-15/4698.Fkzr3oU2qcFmFX28xfoja5.toml` (config)
- `changes/22.0_2025-03-15/4699.LYAYfKXX7C7wqT54kRPnVy.toml` (config)
- `changes/22.0_2025-03-15/4700.nm6R6YTnkmCo5evbykz4kz.toml` (config)
- `changes/22.0_2025-03-15/4701.ah8Wi4SWc22EbgBc4KQeqH.toml` (config)
- `changes/22.0_2025-03-15/4709.dbwPVaU8vSacVkMLhiMjyJ.toml` (config)
- `changes/22.0_2025-03-15/4710.CSNixpvxJdLFaM6xSQ39Zf.toml` (config)
- `changes/22.0_2025-03-15/4712.8ckkAPAXGzedityWEyv363.toml` (config)
- `changes/22.0_2025-03-15/4719.d4xMztC8JjrbVgEscxvMWX.toml` (config)
- `changes/22.1_2025-05-15/4692.dVZs28GuwTFnNJdWkvPbNv.toml` (config)
- `changes/22.1_2025-05-15/4730.GsSUQSXzV8TF2Wav4CXRdd.toml` (config)
- `changes/22.1_2025-05-15/4733.BRLwsEuh76974FPJRuiBjf.toml` (config)
- `changes/22.1_2025-05-15/4741.nVLBrFX4p8jTCBjMRqaYoQ.toml` (config)
- `changes/22.1_2025-05-15/4742.oEA6MjYXMafdbu2akWT5tC.toml` (config)
- `changes/22.1_2025-05-15/4743.SpMm4vvAMjEreykTcGwzcF.toml` (config)
- `changes/22.1_2025-05-15/4744.a4tsF64kZPA2noP7HtTzTX.toml` (config)
- `changes/22.1_2025-05-15/4745.emNmhxtvtTP9uLNQxpcVSj.toml` (config)
- `changes/22.1_2025-05-15/4746.gWnX3BCxbvujQ8B2QejtTK.toml` (config)
- `changes/22.1_2025-05-15/4747.MLmApvpGdwN7J24j7fXsDU.toml` (config)
- `changes/22.1_2025-05-15/4748.j3cKusZZKqTLbc542K4sqJ.toml` (config)
- `changes/22.1_2025-05-15/4756.JT5nmUmGRG6qDEh5ScMn5f.toml` (config)
- `changes/22.1_2025-05-15/4758.dSyCdBJWEJroH2GynR2VaJ.toml` (config)
- `changes/22.1_2025-05-15/4761.mmsngFA6b4ccdEzEpFTZS3.toml` (config)
- `changes/22.1_2025-05-15/4762.PbcJGM8KPBMbKri3fdHKjh.toml` (config)
- `changes/22.1_2025-05-15/4775.kkLon84t7Vy5REKRe9LwPH.toml` (config)
- `changes/22.1_2025-05-15/4776.g83DxRk4WVWCC8rCd6ocFC.toml` (config)
- `changes/22.1_2025-05-15/4777.Lhgz8xFtQjgrKM2KvNfxwD.toml` (config)
- `changes/22.1_2025-05-15/4778.CeUSPNLbGGsqP2Vo4xKkdp.toml` (config)
- `changes/22.1_2025-05-15/4779.UqcbJVKYxwTtrBEGDgb3VS.toml` (config)
- `changes/22.1_2025-05-15/4791.QycEvQbiaiJKraKDhAfFWM.toml` (config)
- `changes/22.2_2025-06-29/4750.jJBu7iAgZa96hdqcpHK96W.toml` (config)
- `changes/22.2_2025-06-29/4792.YsK6LmbEhZv6y3dvhHbXD7.toml` (config)
- `changes/22.2_2025-06-29/4793.mDR5p3mrSmPFQkvWFGWBmD.toml` (config)
- `changes/22.2_2025-06-29/4798.g7G3jRf2ns4ath9LRFEcit.toml` (config)
- `changes/22.2_2025-06-29/4800.2Z9Q8uvzdU2TqMJ9biBLam.toml` (config)
- `changes/22.2_2025-06-29/4801.feKaYKKZTZq2KBjhyxVVAM.toml` (config)
- `changes/22.2_2025-06-29/4802.RMLufX4UazobYg5aZojyoD.toml` (config)
- `changes/22.2_2025-06-29/4810.KyRnffWk3ARyQFNcF88Uh3.toml` (config)
- `changes/22.2_2025-06-29/4811.TQgVr5Sa6uDFtWXdTS5wfw.toml` (config)
- `changes/22.2_2025-06-29/4812.i4aqsTfCkdEs8uYNYS59si.toml` (config)
- `changes/22.2_2025-06-29/4813.cnbzL2eSRzj3i9NcUMFyFo.toml` (config)
- `changes/22.2_2025-06-29/4814.RMQVXTNywcpBQ3HkX2TuyA.toml` (config)
- `changes/22.2_2025-06-29/4815.9dLSFHFozQiAM7oCpX4NyL.toml` (config)
- `changes/22.2_2025-06-29/4816.hhYVDfdzUgoQoMNRKkCDjb.toml` (config)
- `changes/22.2_2025-06-29/4817.ZHx38jvj9zKRNZfQh9Xrpb.toml` (config)
- `changes/22.2_2025-06-29/4818.3VPDqqEWEhDCrTipFY8KKU.toml` (config)
- `changes/22.2_2025-06-29/4820.7bFkjLSeWKdNVhThPpVMAT.toml` (config)
- `changes/22.2_2025-06-29/4822.DrW3tJ3KoB8kTmHtNnNEpQ.toml` (config)
- `changes/22.2_2025-06-29/4825.R7wiTzvN37KAV656s9kfnC.toml` (config)
- `changes/22.2_2025-06-29/4830.EZzGEAk7DiFuedKPoQMMvd.toml` (config)
- `changes/22.2_2025-06-29/4834.oBWsiGWNMuoSXvJNom6N6A.toml` (config)
- `changes/22.3_2025-07-20/4837.cVTsY7pxfQqgVXfFW9hgZK.toml` (config)
- `changes/22.3_2025-07-20/4839.gExNhF7C6kR5VrBg6cBaar.toml` (config)
- `changes/22.3_2025-07-20/4840.jz9uGugc5DUd8x8pQHPyzg.toml` (config)
- `changes/22.3_2025-07-20/4841.HHVCCXXZbYAaaQVmKHCJm2.toml` (config)
- `changes/22.3_2025-07-20/4842.PSW9ZbxENhwfRhbSfemCwE.toml` (config)
- `changes/22.3_2025-07-20/4843.f5aZ5Vpxevw8fEEudawU5u.toml` (config)
- `changes/22.3_2025-07-20/4847.8ujbbBbaZ2VTEdRLeqirSZ.toml` (config)
- `changes/22.3_2025-07-20/4852.mz3RDjX636ZdGoR456C6v9.toml` (config)
- `changes/22.3_2025-07-20/4855.8hCFRFMeMaRWpBEYaxrTMq.toml` (config)
- `changes/22.3_2025-07-20/4858.ajt46xDsbfzFqcghJ2rP6g.toml` (config)
- `changes/22.3_2025-07-20/4870.QeVo4BE5TNouLRJjCFbRMo.toml` (config)
- `changes/22.4_2025-09-13/4869.7GK56NC89XswBFUCiWXtqc.toml` (config)
- `changes/22.4_2025-09-13/4875.29srP6fENz7FrGGoWSkPNa.toml` (config)
- `changes/22.4_2025-09-13/4878.AbGo6aozTWquUjnzzpSdyX.toml` (config)
- `changes/22.4_2025-09-13/4879.kABAi45KpR2H6jqJu6NtDS.toml` (config)
- `changes/22.4_2025-09-13/4880.42PW26hGpLypMJMxTeiQZ6.toml` (config)
- `changes/22.4_2025-09-13/4881.dJNT656MVxJk9DgcoRePip.toml` (config)
- `changes/22.4_2025-09-13/4882.JpgQAHHnCponMKStbC4JsG.toml` (config)
- `changes/22.4_2025-09-13/4884.ADcdCj6GrMaKffYSLzWdsL.toml` (config)
- `changes/22.4_2025-09-13/4886.XSHPk83uhDQdYzurbb4xx9.toml` (config)
- `changes/22.4_2025-09-13/4887.5yypYZV7Sq5PN4ihmf2NUr.toml` (config)
- `changes/22.4_2025-09-13/4890.oCzELerGo8dqPygShWMV9S.toml` (config)
- `changes/22.4_2025-09-13/4892.iRGvURLUGiMSMEDfdpP5jB.toml` (config)
- `changes/22.4_2025-09-13/4893.Fbkdqj4bmTTH6e54gRPwvc.toml` (config)
- `changes/22.4_2025-09-13/4894.PLQSCgnKXygrGdkekTbx8q.toml` (config)
- `changes/22.4_2025-09-13/4895.UECAN369MCuQaLnTmtYFGr.toml` (config)
- `changes/22.4_2025-09-13/4896.R92Xq7W6PDbabuk6aZ5FZt.toml` (config)
- `changes/22.4_2025-09-13/4906.Fju7LDJgwCz2sxgQy9muBG.toml` (config)
- `changes/22.4_2025-09-13/4908.KnwujH2JruNRZSrTTvvc9B.toml` (config)
- `changes/22.4_2025-09-13/4911.kiF45Y4cfPGMq5cuLpa5da.toml` (config)
- `changes/22.4_2025-09-13/4915.D3x6MoyYYDaUcB7jmLUyeY.toml` (config)
- `changes/22.4_2025-09-13/4923.AEztvspxU4Ajz7N3ms56Wq.toml` (config)
- `changes/22.4_2025-09-13/4925.FCwe9rrjgv5GmfvuhHXjHg.toml` (config)
- `changes/22.4_2025-09-13/4926.GMcTfT2hSAdmdT7wi73mzZ.toml` (config)
- `changes/22.4_2025-09-13/4927.mHtL79KfGaRw3LEMdHN6Ry.toml` (config)
- `changes/22.4_2025-09-13/4928.ej4TvW3TjhqhpUHNyne2r4.toml` (config)
- `changes/22.4_2025-09-13/4929.P2dSYTjRtQtXPdKyaDHPJA.toml` (config)
- `changes/22.4_2025-09-13/4933.CPGgVg7gvHC3dqmhzAVDVo.toml` (config)
- `changes/22.4_2025-09-13/4934.W4nUZkUHd9Hw4mGaLA6Ayf.toml` (config)
- `changes/22.4_2025-09-13/4939.YDNzLiFegKD2difT6yr6P7.toml` (config)
- `changes/22.5_2025-09-27/4861.HEoGVs2mYXWzqMahi6SEhV.toml` (config)
- `changes/22.5_2025-09-27/4938.U2x6X7ZGikYv5eo9aUSNGc.toml` (config)
- `changes/22.5_2025-09-27/4943.DdNTkLjQbNGeG3nEBGHjBo.toml` (config)
- `changes/22.5_2025-09-27/4944.mYorcTojrvwihYQ5NPwNcE.toml` (config)
- `changes/22.5_2025-09-27/4945.LDiTvYjbXuQBp7kLyQMYa5.toml` (config)
- `changes/22.5_2025-09-27/4946.KujJLUNcND72Y8aKs3bzSx.toml` (config)
- `changes/22.5_2025-09-27/4947.CcLd8YTb8XaANn8gQXruNb.toml` (config)
- `changes/22.5_2025-09-27/4948.ernZikrNEarFtTZgLN7huS.toml` (config)
- `changes/22.5_2025-09-27/4949.YhMnQj57Qpm9HD5zkkhfZC.toml` (config)
- `changes/22.5_2025-09-27/4950.VA9pgTVrLPABkUrxifLZnh.toml` (config)
- `changes/22.5_2025-09-27/4951.7ZExRZuEwEoGXX5FMPWctm.toml` (config)
- `changes/22.5_2025-09-27/4952.bVCE8YehtKGcwLYdiXkmQb.toml` (config)
- `changes/22.5_2025-09-27/4953.8aPTEQhSPSgTrguzvsw4tq.toml` (config)
- `changes/22.5_2025-09-27/4954.XrYn8gzjeQF9LoPQomutuW.toml` (config)
- `changes/22.5_2025-09-27/4955.2BXmasa9Ms9vqXngSMKSVX.toml` (config)
- `changes/22.5_2025-09-27/4958.ktVtuEvzAxxFxSwk7KXQ66.toml` (config)
- `changes/22.5_2025-09-27/4959.H2BCKBh9WXaoFKmwiMX4m7.toml` (config)
- `changes/22.5_2025-09-27/4960.KyngeakT6uHLQXYftm2Cpe.toml` (config)
- `changes/22.5_2025-09-27/4961.nd2KdJpSCyLC3K5xninxZL.toml` (config)
- `changes/22.5_2025-09-27/4962.mZAGRv4sXnpirJCkrKniVJ.toml` (config)
- `changes/22.5_2025-09-27/4964.KbKLtQ5MYHdt49gpBxCaja.toml` (config)
- `changes/22.5_2025-09-27/4965.488hEhfeZfPvfZszvRKdkJ.toml` (config)
- `changes/22.5_2025-09-27/4967.a9vCqXXpyAfzTb8TD7ouqB.toml` (config)
- `changes/22.5_2025-09-27/4968.ecxiPBroDpMUkab6uBCUde.toml` (config)
- `changes/22.5_2025-09-27/4972.RX4QftpcFPCv2wXbTAhDAh.toml` (config)
- `changes/22.5_2025-09-27/4973.PtSpAPsm7wh4PWc4p3uajX.toml` (config)
- `changes/22.5_2025-09-27/4974.c4UDqA4q7eBr9mYGmJL4CQ.toml` (config)
- `changes/22.5_2025-09-27/4975.cxvpDwNRvRzK9aZxRbav6b.toml` (config)
- `changes/22.5_2025-09-27/4976.GVUSXmvHEopzdff7bVCNF4.toml` (config)
- `changes/22.5_2025-09-27/4977.YYYUcDY7oSNQ9FXUGZq7sp.toml` (config)
- `changes/22.5_2025-09-27/4978.9hhbtgMWDjm7BUNaNozjoV.toml` (config)
- `changes/22.5_2025-09-27/4979.gRpn8vd66DtorTtkMN4AsU.toml` (config)
- `changes/22.6_2026-01-24/4827.PBXyEEjvXz5sJbiDWkeGFX.toml` (config)
- `changes/22.6_2026-01-24/4980.86EojeXUgUSi87JKMZojGD.toml` (config)
- `changes/22.6_2026-01-24/4984.XKkS99HJWztHscs6N6wpEh.toml` (config)
- `changes/22.6_2026-01-24/4985.LrPNHbexoHAmim6zXB9nMp.toml` (config)
- `changes/22.6_2026-01-24/4986.fwbZif2YKWgeugPof8Fikj.toml` (config)
- `changes/22.6_2026-01-24/4987.PLoqzvYm725uVfKcWhwuCb.toml` (config)
- `changes/22.6_2026-01-24/4988.Lncn8TNDcQF4hLQZJvyzQY.toml` (config)
- `changes/22.6_2026-01-24/4989.TjTuqb5LqcEXDLvArDzcEY.toml` (config)
- `changes/22.6_2026-01-24/4990.HxHP2zqbTAcGzjapkgX3E5.toml` (config)
- `changes/22.6_2026-01-24/4994.K8XVzJe4kuoHmc2yRsrYTb.toml` (config)
- `changes/22.6_2026-01-24/4995.TGRtuG8BUqB6S9JxpPxiNR.toml` (config)
- `changes/22.6_2026-01-24/4996.bRG2iuMsWDR47wDt556q57.toml` (config)
- `changes/22.6_2026-01-24/4997.hJRqz3id5FnzSzPeMhY3k6.toml` (config)
- `changes/22.6_2026-01-24/4998.jvTA7u2hEA7xwa87XoUqec.toml` (config)
- `changes/22.6_2026-01-24/4999.NGTC66pJdAhjtoLykBsxQc.toml` (config)
- `changes/22.6_2026-01-24/5000.A5P7pNDw2Bc5Uaq3psVEWZ.toml` (config)
- `changes/22.6_2026-01-24/5001.DXjSVgk4h3o8WoPTy8Jpng.toml` (config)
- `changes/22.6_2026-01-24/5002.cube9Ku57EajUDF8xoSdfV.toml` (config)
- `changes/22.6_2026-01-24/5004.k7NzG5uTwQxcHP6shbogHL.toml` (config)
- `changes/22.6_2026-01-24/5006.hRJtYPL4nBeZ43DWqii68V.toml` (config)
- `changes/22.6_2026-01-24/5007.ANT5x4yXn667UnjSHsCSUb.toml` (config)
- `changes/22.6_2026-01-24/5008.4XBBoZAXkrtsuHRxPqAW9V.toml` (config)
- `changes/22.6_2026-01-24/5009.QuigkwxAs8bemB9gnKbXhz.toml` (config)
- `changes/22.6_2026-01-24/5011.PSJLmKo5LhUXjPbnGbZ3bn.toml` (config)
- `changes/22.6_2026-01-24/5012.CBCzSf2FaoALedVnSyExqD.toml` (config)
- `changes/22.6_2026-01-24/5013.FrUE8G2c4xicUxiTj4Drfn.toml` (config)
- `changes/22.6_2026-01-24/5014.MzMmSLFoUDeCV6JeJNuL2H.toml` (config)
- `changes/22.6_2026-01-24/5015.6PQeFxBMxfEdw82aAqoRSy.toml` (config)
- `changes/22.6_2026-01-24/5016.bmfLnKrJ932h5QGKWs9kke.toml` (config)
- `changes/22.6_2026-01-24/5022.Kz9z6826xjnfjXhXTaJhGE.toml` (config)
- `changes/22.6_2026-01-24/5023.Zeup3tNhhr2F6M5KHxcj5f.toml` (config)
- `changes/22.6_2026-01-24/5024.8UrFV8RpA74s8VaD4FFwaZ.toml` (config)
- `changes/22.6_2026-01-24/5025.Zzz5pN2Rmu8DZGtKFzi7wx.toml` (config)
- `changes/22.6_2026-01-24/5026.UgTNGQ3nckNfhFJrRYYznN.toml` (config)
- `changes/22.6_2026-01-24/5027.2ostaGWzx3TtWpQACbgDLs.toml` (config)
- `changes/22.6_2026-01-24/5029.8qJNkyaEhhMckJjNZSyUMT.toml` (config)
- `changes/22.6_2026-01-24/5030.bBRC3598kUYHL2Qpo4gjMb.toml` (config)
- `changes/22.6_2026-01-24/5032.gJe5x9EV6iFcEFDy5ov3Qf.toml` (config)
- `changes/22.6_2026-01-24/5033.JX2YjsVeznxTBqZF5yPyHw.toml` (config)
- `changes/22.6_2026-01-24/5034.TboLf7ySS68mHXaoDkQLJa.toml` (config)
- `changes/22.6_2026-01-24/5035.LvduDeof5HBLViwSE3D7Tj.toml` (config)
- `changes/22.6_2026-01-24/5040.fdwnytzmSECx9qsps5YQ8p.toml` (config)
- `changes/22.6_2026-01-24/5041.KvQgtUQd4LsSVxifJurtCa.toml` (config)
- `changes/22.6_2026-01-24/5042.EsubhGfoUGEXXD3iYhpscb.toml` (config)
- `changes/22.6_2026-01-24/5044.QdtCmSghVutBX7hdFxy39Y.toml` (config)
- `changes/22.6_2026-01-24/5048.GCKPwc255mjcVTXBemz9PS.toml` (config)
- `changes/22.6_2026-01-24/5049.S5gFYpudshPwYzoLYVJQM4.toml` (config)
- `changes/22.6_2026-01-24/5050.V7Svc2KJrD2Rpn3YnDuYoi.toml` (config)
- `changes/22.6_2026-01-24/5055.B8q4kJCbfLU8km5JAGSFZj.toml` (config)
- `changes/22.6_2026-01-24/5056.XnhzpGSAsyoXMGS5mV47Ec.toml` (config)
- `changes/22.6_2026-01-24/5057.F3hY56ZMSYAUszphSqQHiK.toml` (config)
- `changes/22.6_2026-01-24/5058.28oHRt4BwX6yeg2LRMaCXQ.toml` (config)
- `changes/22.6_2026-01-24/5059.4hDeRNcVVVgJkN8fV2ahxJ.toml` (config)
- `changes/22.6_2026-01-24/5060.3thn8ynSueq4pZEDBTTs52.toml` (config)
- `changes/22.6_2026-01-24/5061.FmvsKgVUc4Rgb9avL4Wmws.toml` (config)
- `changes/22.6_2026-01-24/5062.T5v63ioaphzU2yjAkvQnz2.toml` (config)
- `changes/22.6_2026-01-24/5067.V47rAvnekJ8nizGaGfXKbb.toml` (config)
- `changes/22.6_2026-01-24/5068.3Z2v29SeC8j3oB7kDNcpEd.toml` (config)
- `changes/22.6_2026-01-24/5070.guYXqNjxEqyktC3ndMsdqc.toml` (config)
- `changes/22.6_2026-01-24/5075.YxKmAd2uSaR5xJZG6Zf6h9.toml` (config)
- `changes/22.6_2026-01-24/5078.FoNwUYLbXQFRebTFhR6UPn.toml` (config)
- `changes/22.6_2026-01-24/5080.BYez3ivHiHpRDEjnsCStKM.toml` (config)
- `changes/22.6_2026-01-24/5083.MebfmAm8GVX9To4ZWxeU4h.toml` (config)
- `changes/22.6_2026-01-24/5088.dbco4MBy5FHuS4qawHww3M.toml` (config)
- `changes/22.6_2026-01-24/5100.NnTUgrxZibXT6N3SAw28aH.toml` (config)
- `changes/22.6_2026-01-24/5101.SUFGhSSTbqovDSZpVF2LYi.toml` (config)
- `changes/22.6_2026-01-24/5107.dkBZXpsYuApxXCiLSPkeZR.toml` (config)
- `changes/22.6_2026-01-24/5108.CUt49oxmPxDZ3BPhDDCAm5.toml` (config)
- `changes/22.7_2026-03-16/5110.NfCAazzRFNXvNn9CNmMZpZ.toml` (config)
- `changes/22.7_2026-03-16/5112.Na2dk8jzBTtTg3EvNSo6kh.toml` (config)
- `changes/22.7_2026-03-16/5113.YfEbfC8WGAxMFb8rKBCUej.toml` (config)
- `changes/22.7_2026-03-16/5114.LGfvVo5cdK74VyVWHFJDW3.toml` (config)
- `changes/22.7_2026-03-16/5115.CgTBPjBCWJ7reRZG4vu8vJ.toml` (config)
- `changes/22.7_2026-03-16/5116.9YKyNfUgP73QatTcuD5qNm.toml` (config)
- `changes/22.7_2026-03-16/5117.ZoYfowizxLvCbfWcABcezC.toml` (config)
- `changes/22.7_2026-03-16/5119.CA8avHeQnMdHNFQKvonFK6.toml` (config)
- `changes/22.7_2026-03-16/5122.8DXxjQycntr4ecdcrcWZ7f.toml` (config)
- `changes/22.7_2026-03-16/5122.EZ5hbq74CEoTbixKNcSmQz.toml` (config)
- `changes/22.7_2026-03-16/5124.ZMLaT6JfSLD4orqRAqrZXj.toml` (config)
- `changes/22.7_2026-03-16/5125.Shtxta26FemMvrpd3bWFeF.toml` (config)
- `changes/22.7_2026-03-16/5135.7NGhdLCnjTdBHFpwbxdLQt.toml` (config)
- `changes/22.7_2026-03-16/5137.AMrRwuXMvfMK8HHe3Udu9q.toml` (config)
- `changes/22.7_2026-03-16/5140.jcXPuwWiM4zqtxGPWgYSoo.toml` (config)
- `changes/22.7_2026-03-16/5142.h7G2mCUQ2PobeTyLNewpvx.toml` (config)
- `changes/22.7_2026-03-16/5143.HYNP5H8WQXGydLcnAa2pkf.toml` (config)
- `changes/22.7_2026-03-16/5145.3uQNphqhEArdGYLTFDSShP.toml` (config)
- `changes/22.7_2026-03-16/5146.YwQ5dRVNyvkZ3mtmFQWtzJ.toml` (config)
- `changes/22.7_2026-03-16/5150.6rzZ8vRQrj3NqDiyLjcuPY.toml` (config)
- `changes/22.7_2026-03-16/5151.fvex2RmXotXPkFAXSxosHn.toml` (config)
- `changes/22.7_2026-03-16/5152.TgxyAT2Wwb7DQpxKhWRdt4.toml` (config)
- `changes/22.7_2026-03-16/5153.4vV6k9bXfCRAiY9m7VNk3s.toml` (config)
- `changes/22.7_2026-03-16/5154.gRV9eXpMQPJHJb7idaBYXS.toml` (config)
- `changes/22.7_2026-03-16/5155.J9c3dKTpfBJ3TkZy3ShDXN.toml` (config)
- `changes/22.7_2026-03-16/5156.DJGYhbSstpVvdEiQ74PocD.toml` (config)
- `changes/22.7_2026-03-16/5157.WGzqbomDJMYKd84XsZz4G9.toml` (config)
- `changes/22.7_2026-03-16/5159.oRWyrKjKtGSS28NxvnJnCy.toml` (config)
- `changes/22.7_2026-03-16/5161.BXtxdWhwpuvW4duoMvVFUB.toml` (config)
- `changes/22.7_2026-03-16/5164.AS7dPamV4u4kerj6wbkjrv.toml` (config)
- `changes/22.7_2026-03-16/5166.5cZDXUcYWLrCCWCRnBKktb.toml` (config)
- `changes/22.7_2026-03-16/5167.UqMXpUqQEjk8jpwWe5Tyht.toml` (config)
- `changes/22.7_2026-03-16/5168.2fnSt8zjs3pkiboD72J5Hr.toml` (config)
- `changes/22.7_2026-03-16/5169.WBArfhkfSaQfvHCRv99dz8.toml` (config)
- `changes/22.7_2026-03-16/5170.c4Bf2hQjpaGuJgeDGiCRaU.toml` (config)
- `changes/22.7_2026-03-16/5171.cF3xtCJWpbozHafFQ7Cfxv.toml` (config)
- `changes/22.7_2026-03-16/5172.aHAPm7vzNdhWTPujRJSWcT.toml` (config)
- `changes/22.7_2026-03-16/5173.PdpaRKNF2yLRfMVZV3hqnQ.toml` (config)
- `changes/22.7_2026-03-16/5174.irY8o7m4ewVRnb9jHSqk9y.toml` (config)
- `changes/22.7_2026-03-16/5175.jLYXTSX7ASFuFwHuHd9knc.toml` (config)
- `changes/22.7_2026-03-16/5176.UzCwJkd4nVg8LM4WeTdn9a.toml` (config)
- `changes/22.8_2026-06-12/5125.filter-fix.toml` (config)
- `changes/22.8_2026-06-12/5177.fg9Y3ZSboi94mttv3eas2L.toml` (config)
- `changes/22.8_2026-06-12/5183.Enoyw5yoT4S9uRxn7v5ud5.toml` (config)
- `changes/22.8_2026-06-12/5184.YKdeCfWDDXk8v3DJx8nTeg.toml` (config)
- `changes/22.8_2026-06-12/5185.VTFw6hNJ4A9mGayu2rduUt.toml` (config)
- `changes/22.8_2026-06-12/5190.5mL9K6trXT6Y4vLgqxy9jE.toml` (config)
- `changes/22.8_2026-06-12/5191.B6JK8KhgoqqawRrrWaSCDH.toml` (config)
- `changes/22.8_2026-06-12/5192.VYDBGMwXeTVyvXESmEnfFa.toml` (config)
- `changes/22.8_2026-06-12/5193.GqEK23Erwr49GQ79uJho38.toml` (config)
- `changes/22.8_2026-06-12/5194.bnCTjH5QVYuyFDp4iCwJoV.toml` (config)
- `changes/22.8_2026-06-12/5196.7keq7yJhXbMb9RyShLHz4D.toml` (config)
- `changes/22.8_2026-06-12/5198.haofa4LoE6k2WQoAUSizM8.toml` (config)
- `changes/22.8_2026-06-12/5199.4qywU9Faav8YhWivBBykyJ.toml` (config)
- `changes/22.8_2026-06-12/5203.jxMZ7aSe7eDKXTvfEdZGzw.toml` (config)
- `changes/22.8_2026-06-12/5205.KBqhJA9kouNAJmQYNwZHT2.toml` (config)
- `changes/22.8_2026-06-12/5206.nXEjjZXrYZiWroBfBeQR3N.toml` (config)
- `changes/22.8_2026-06-12/5209.msPrg8bYnmr89qXR4fr5bG.toml` (config)
- `changes/22.8_2026-06-12/5217.5AVeFbQnudaXWyZ3TM7E5B.toml` (config)
- `changes/22.8_2026-06-12/5220.iAgLEYgfuW46wtvCUx3dhM.toml` (config)
- `changes/22.8_2026-06-12/5221.UEBLb7KFNwZkZ5fC3CyDBD.toml` (config)
- `changes/22.8_2026-06-12/5222.dGHpTKrbVb9VQV8pVv9Lii.toml` (config)
- `changes/22.8_2026-06-12/5223.6Ttu6UoyzkVQddzKrz947W.toml` (config)
- `changes/22.8_2026-06-12/5224.YVKcje5xUdXTjJJurmAVVD.toml` (config)
- `changes/22.8_2026-06-12/5229.87PBN4GFkuAaDhhgFwCYkY.toml` (config)
- `changes/22.8_2026-06-12/5233.YJVhiqtdZZ57TBRdNh2swZ.toml` (config)
- `changes/22.8_2026-06-12/5237.effective-user-fix.toml` (config)
- `changes/22.8_2026-06-12/5240.iJXyH8RNWNNQpC47SfNHzw.toml` (config)
- `changes/22.8_2026-06-12/5245.3Xu2uH53fGn822LB5Y7Pqk.toml` (config)
- `changes/22.8_2026-06-12/5247.3DSJ9C36s7HCYSNTEUnDpT.toml` (config)
- `changes/22.8_2026-06-12/5250.dTuzQhYiw2T8gfvp6Skj89.toml` (config)
- `changes/22.8_2026-06-12/5252.Qo4J766e8AEw35gf9gLaJE.toml` (config)
- `changes/22.8_2026-06-12/5253.A9BQTN98eeqDPBrVZ674qa.toml` (config)
- `changes/22.8_2026-06-12/5254.kaanCYDk82Jg6P8S9pJG3C.toml` (config)
- `changes/22.8_2026-06-12/5255.Sx6a4Mf4dD3bUfNWSty78T.toml` (config)
- `changes/22.8_2026-06-12/5256.VFGHhZz3SchcMmJJLETLzs.toml` (config)
- `changes/22.8_2026-06-12/5257.c4g6KoZswRyGb9ypHwfKzB.toml` (config)
- `changes/22.8_2026-06-12/5259.iZALQbcHZUBRwuvxwMLpf4.toml` (config)
- `changes/22.8_2026-06-12/5262.nZcWnWfJyHhUwG484KJx9q.toml` (config)
- `changes/unreleased/5186.VngJMeztfXKDXAhcqTxJjK.toml` (config)
- `changes/unreleased/5264.X28jz5XU2gBXFoCpnQn7na.toml` (config)
- `changes/unreleased/5265.o75uzmqPxDpYx8JwXRbqeF.toml` (config)
- `changes/unreleased/5268.GKZnfBkMcLqBC4rTgznsnY.toml` (config)
- `changes/unreleased/5271.H8posH7FA8X3BZrmC52ueg.toml` (config)
- `changes/unreleased/5273.ZKFjVYwRse9MA9BuF4dUEW.toml` (config)
- `changes/unreleased/5274.BMgKbj7LZwGKbx8jg6mzM4.toml` (config)
- `changes/unreleased/5276.mYSU5bdepgvEnuztjTmcV3.toml` (config)
- `changes/unreleased/5277.WktkduZbpMYLjqTRzcrphW.toml` (config)
- `changes/unreleased/5278.eb9D9NeRPkyNoNusYAqe8D.toml` (config)
- `changes/unreleased/5280.ithVrhgXtP4S774Mp4f2Dc.toml` (config)
- `changes/unreleased/5283.4feBMWUxBfZdj4koEneVmA.toml` (config)
- `changes/unreleased/5286.CdJJrjsRJHALMgiEZLeumT.toml` (config)
- `changes/unreleased/5287.75WNudSbZQ2uPUwbwKLjrH.toml` (config)
- `changes/unreleased/5288.C8AoiRWDdZmCZeiiz4Gujz.toml` (config)
- `changes/unreleased/5289.MFnVwiitS3Kdrs6rv2De4a.toml` (config)
- `changes/unreleased/5290.VrpedfUnvcaMn75byHfeSY.toml` (config)
- `changes/unreleased/5291.79JdLrT5P97c9rDDxvrcob.toml` (config)
- `changes/unreleased/5297.pickle-empty-flush.toml` (config)
- `changes/unreleased/5298.webhook-html-escaping.toml` (config)
- `changes/unreleased/5299.5mQXHwskDhSY3Rx6Nd26CR.toml` (config)
- `changes/unreleased/5302.bhpiKviDS5QTSKncz35DN2.toml` (config)
- `changes/unreleased/5303.7uN6w2W6EiLMn2KqzYyYNs.toml` (config)
- `changes/unreleased/5304.6rKY3k6kGsCdnZFP8jdsQ2.toml` (config)
- `changes/unreleased/5305.reduce-collection-time.toml` (config)
- `changes/unreleased/5306.bLrpQxCgGfzN97UASvrrh8.toml` (config)
- `changes/unreleased/5308.HzaS8Voh4Avaaq8yieH55r.toml` (config)
- `changes/unreleased/5316.hfEygQTuEytxqhraediVD4.toml` (config)
- `changes/unreleased/5317.4K3QULRwtLbU2Vb4489BcV.toml` (config)
- `changes/unreleased/5318.AxkHxtPmi6TBvAtJNrgak5.toml` (config)
- `changes/unreleased/5319.eTV2gFhvARJoSFqj55K6Ke.toml` (config)
- `changes/unreleased/5320.E4iACsWepX8esLg9dQzwCM.toml` (config)
- `changes/unreleased/5321.kvqxGZL9Yw8R5on9pitBda.toml` (config)
- `changes/unreleased/5324.H7nkdXLb3RYjnKUorXnsm6.toml` (config)
- `changes/unreleased/5327.TGHQYPSvC33fT2qFUG7QjZ.toml` (config)
- `changes/unreleased/5331.5f9aSMvjRqe493h22LkCkt.toml` (config)
- `changes/unreleased/5332.g2wSvoFSBNHF8DkjvKFAnu.toml` (config)
- `changes/unreleased/5333.XJxQarLuGEuWyaST9RKYDR.toml` (config)
- `changes/unreleased/5339.Kl6xS6VYDf2DSsRNH10eLp.toml` (config)
- `changes/unreleased/5342.QhycnvRNrLwa3595eX4UbU.toml` (config)
- `changes/unreleased/5345.QB7p2o46PnZ98e94orWHjb.toml` (config)
- `changes/unreleased/5346.5NG6qjXeLZ43RTCqHNfDPG.toml` (config)
- `changes/unreleased/5347.Xvzf7zUrJ6JJ3c8YmbZBgR.toml` (config)
- `changes/unreleased/5348.Kbn3Pr5feMiG8V5KtJTBXW.toml` (config)
- `changes/unreleased/5349.2kw3bAcz8dAFsxMZ9w7YrW.toml` (config)
- `changes/unreleased/5350.7LMXCxpoH9nRwWt6vjeuAs.toml` (config)
- `changes/unreleased/5352.h8oS6vnQMtDmqu2VgMZRvY.toml` (config)
- `changes/unreleased/5353.nCXJnXBhsMpX3eDiDj2fEf.toml` (config)
- `changes/unreleased/5357.6AwXaVPahu8ZWVj6AmAQCL.toml` (config)
- `changes/unreleased/5358.4RAeZUaHuA5dLiFsj7ejvN.toml` (config)
- `changes/unreleased/5360.CCVegGQs4j7rCdmnrrH7nM.toml` (config)
- `changes/unreleased/5361.mLykZxuYrAk2mcPPkThyPx.toml` (config)
- `changes/unreleased/5364.kLAAhq7NvyuWUPDzgufSWH.toml` (config)
- `changes/unreleased/5368.kSUQms8CvTzwdXzj62ACaB.toml` (config)
- `changes/unreleased/5369.oPKaDpwgLLWgzcJvLzbTdP.toml` (config)
- `changes/unreleased/5370.AsUmQF3gQ9tEeUjnzgEQax.toml` (config)
- `changes/unreleased/5371.FgaUgNafWpDxGevZvyKXd7.toml` (config)
- `changes/unreleased/5372.Qw4t3DZR6LC9piPxnfuSfA.toml` (config)
- `changes/unreleased/5373.Gs83BkGAj7RCrub4ZojiFu.toml` (config)
- `changes/unreleased/5374.3bhnruS777NWwcegakz5L8.toml` (config)
- `changes/unreleased/5376.MBCohzg8ATmK4nqMBUuZ4M.toml` (config)
- `changes/unreleased/5381.ZjSe37LqD24fLfxi3Uc38B.toml` (config)
- `changes/unreleased/5392.Am7fgG24e5pvNLcaA4kK6r.toml` (config)
- `changes/unreleased/5393.5iF9frRu8ZyZtUkP5e2Wbn.toml` (config)
- `changes/unreleased/5394.Cr7GXsKDHHZb5A9mN3nVqa.toml` (config)
- `changes/unreleased/5395.dvu549cfKavvmpWYJziUjn.toml` (config)
- `changes/unreleased/5396.kaWZfdL6uZT2nD9WrmbDVn.toml` (config)
- `changes/unreleased/pickle-get-empty-cache.toml` (config)
- `codecov.yml` (config)

## Top-level layout

- `docs` — 414 analysed file(s)
- `changes` — 343 analysed file(s)
- `.github` — 23 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `contrib` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `41e3633bd1b4e51693ee57059828a59a9773618a` is the revision these paths and observations refer to.
