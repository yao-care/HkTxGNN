---
layout: home
title: HkTxGNN - 香港老藥新用預測系統
---

# HkTxGNN - 香港老藥新用預測系統

以 [TxGNN](https://github.com/mims-harvard/TxGNN) 模型（深度學習）預測香港藥品老藥新用的研究系統。

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## 香港：本站涵蓋範圍

本站公開 **{{ site.data.drug_stats.total_drugs }}** 個藥品的報告，藥品來自[衛生署藥物辦公室](https://www.drugoffice.gov.hk/)的許可證資料（香港）。

各證據等級報告數： L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### 本站證據等級最高的藥品

| 藥品 | 證據等級 |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Natamycin](/drugs/natamycin/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Oteracil](/drugs/oteracil/) | L1 |
| [Tegafur](/drugs/tegafur/) | L1 |
| [Triptorelin](/drugs/triptorelin/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |

### 30 個 TxGNN 站台中只有本站涵蓋的藥品

| 藥品 | 證據等級 |
|---|---|
| [Glycocholic Acid](/drugs/glycocholic-acid/) | L5 |
| [Calcium Glycerophosphate](/drugs/calcium-glycerophosphate/) | L5 |
| [Pipenzolate](/drugs/pipenzolate/) | L5 |
| [Benzoin](/drugs/benzoin/) | N/A |
| [Monensin](/drugs/monensin/) | N/A |
| [Palmitic Acid](/drugs/palmitic-acid/) | N/A |
| [Tazemetostat](/drugs/tazemetostat/) | N/A |

<!-- local-home:end -->

## 系統概覽

| 項目 | 數值 |
|------|------|
| 香港註冊藥品 | 14,252 |
| DrugBank 映射成功 | 1,261 |
| 映射率 | 82% |
| 預測新適應症（已排除已知用途） | {{ site.data.site_stats.indications }} |

## 資料來源

- **藥品資料**：[香港藥物辦公室](https://www.drugoffice.gov.hk/)
- **知識圖譜**：[TxGNN](https://github.com/mims-harvard/TxGNN) (Harvard MIMS Lab)
- **藥物識別**：[DrugBank](https://www.drugbank.com/)

## FHIR API

本系統提供 FHIR R4 相容的 API：

- [CapabilityStatement](/fhir/metadata)
- [MedicationKnowledge](/fhir/MedicationKnowledge/)
- [ClinicalUseDefinition](/fhir/ClinicalUseDefinition/)

## SMART on FHIR

支援 SMART on FHIR 整合：

- [SMART Launch](/smart/launch.html)

## 免責聲明

⚠️ **重要提示**：本系統的預測結果僅供研究參考，不構成醫療建議。
老藥新用候選需經過嚴格的臨床驗證才能應用於臨床實踐。
使用者應諮詢專業醫療人員以獲得適當的醫療建議。

## 專案資訊

- **GitHub**: [yao-care/HkTxGNN](https://github.com/yao-care/HkTxGNN)
- **開發者**: [藥提醒科技有限公司 (yao.care)](https://yao.care)
- **授權**: MIT License

---

© 2026 藥提醒科技有限公司 (yao.care). All rights reserved.

---

## 關於開發單位

本平台由**藥提醒科技有限公司**（yao.care，統一編號 83620786，地址：台中市西區台灣大道二段220號12樓）開發與維運。

HkTxGNN 是該公司「TxGNN 老藥新用」產品線的香港站。同一套系統已部署於 30 個國家／地區，
各站依 `{國碼}TxGNN` 命名（JpTxGNN、UsTxGNN、DETxGNN…），網址格式為 `{國碼}txgnn.yao.care`。
產品總覽見 <https://www.yao.care/medical/txgnn/>。

TxGNN 模型本身由哈佛醫學院 Zitnik Lab 開發並發表於 *Nature Medicine*；
本平台是藥提醒科技有限公司以該模型為基礎建置的落地系統，負責各國藥證資料串接、
深度學習預測（已排除知識圖譜中已記錄的用途）、PubMed／ClinicalTrials 證據分級，以及 SMART on FHIR 電子病歷整合。
