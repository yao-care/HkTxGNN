---
layout: home
title: HkTxGNN - 香港老藥新用預測系統
description: "TxGNN 老藥新用報告：衛生署藥物辦公室藥劑製品清單中 924 個藥品，附臨床試驗與文獻證據的 L1–L5 證據等級。"
---

# HkTxGNN - 香港老藥新用預測系統

以 [TxGNN](https://github.com/mims-harvard/TxGNN) 模型（深度學習）預測香港藥品老藥新用的研究系統。

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## 香港：本站涵蓋範圍

本站公開 **{{ site.data.drug_stats.total_drugs }}** 個藥品的報告，藥品來自[衛生署藥物辦公室](https://www.drugoffice.gov.hk/)的許可證資料（香港）。

資料集：[衛生署藥物辦公室 藥劑製品清單（DrugList.xml）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)，每週一自動下載比對。詳見[資料來源]({{ '/sources/' | relative_url }})。

各證據等級報告數：

| 證據等級 | 報告數 | 占比 |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

本站有 16 組預測的藥物–疾病配對，在其他 29 個 TxGNN 站台都沒有。

### 本站證據等級最高的藥品

| 藥品 | 證據等級 |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Propofol](/drugs/propofol/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Naftidrofuryl](/drugs/naftidrofuryl/) | L1 |
| [Acetylcysteine](/drugs/acetylcysteine/) | L2 |
| [Brentuximab Vedotin](/drugs/brentuximab-vedotin/) | L2 |

### 30 個 TxGNN 站台中只有本站涵蓋的藥品

| 藥品 | 證據等級 |
|---|---|
| [Glycocholic Acid](/drugs/glycocholic-acid/) | L5 |
| [Calcium Glycerophosphate](/drugs/calcium-glycerophosphate/) | L5 |
| [Pipenzolate](/drugs/pipenzolate/) | L5 |
| [Benzoin](/drugs/benzoin/) | N/A |
| [Palmitic Acid](/drugs/palmitic-acid/) | N/A |
| [Tazemetostat](/drugs/tazemetostat/) | N/A |

<!-- local-home:end -->

## 系統概覽

| 項目 | 數值 |
|------|------|
| 香港註冊藥品 | 14,252 |
| DrugBank 映射成功 | 1,291 |
| 映射率 | 84% |
| 預測新適應症（已排除已知用途） | {{ site.data.site_stats.indications }} |

## 資料來源

- **藥品資料**：[香港藥物辦公室](https://www.drugoffice.gov.hk/)
- **知識圖譜**：[TxGNN](https://github.com/mims-harvard/TxGNN) (Harvard MIMS Lab)
- **藥物識別**：[DrugBank](https://www.drugbank.com/)

## FHIR API

本系統提供 FHIR R4 相容的 API：

- [CapabilityStatement](/fhir/metadata)
- MedicationKnowledge：`/fhir/MedicationKnowledge/{id}.json`（範例：[db00331.json](/fhir/MedicationKnowledge/db00331.json)）
- ClinicalUseDefinition：`/fhir/ClinicalUseDefinition/{id}.json`（範例：[db00331-classic-stiff-person-syndrome.json](/fhir/ClinicalUseDefinition/db00331-classic-stiff-person-syndrome.json)）

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

© 2026 藥提醒科技有限公司 (yao.care)。保留所有權利。

---

## 關於開發單位

本平台由**藥提醒科技有限公司**（yao.care）開發與維運。公司資料、TxGNN 模型背景與產品線各站一覽，
見<a href="{{ '/about/' | relative_url }}">關於專案</a>。
