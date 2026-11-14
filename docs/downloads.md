---
layout: default
title: 資料下載
nav_order: 94
permalink: /downloads/
description: "HkTxGNN 開放資料下載：FHIR 資源、預測結果與搜尋索引。"
---

# 資料下載

<div class="key-takeaway">
預測結果以 FHIR R4 標準格式開放，可直接串接電子病歷系統。
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## 香港：本站資料

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

<!-- site-data:end -->

## FHIR 資源

本站以 FHIR R4 格式提供預測結果，可供 SMART on FHIR 應用直接取用：

| 資源 | 路徑 | 說明 |
|------|------|------|
| CapabilityStatement | `/fhir/metadata` | FHIR 伺服器能力宣告 |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | 藥物資源 |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | 預測適應症 |
| Bundle | `/fhir/Bundle/all-predictions.json` | 全部預測的打包資源 |

---

## 搜尋索引

`/data/search-index.json` 提供藥物與適應症的搜尋索引，可用於自建查詢介面。

---

## 使用條款

<ol class="actionable-steps">
<li>本站資料<strong>僅供研究參考</strong>，不得作為醫療決策依據。</li>
<li>引用時請註明來源為 HkTxGNN（藥提醒科技有限公司）並引用 TxGNN 原始論文。</li>
<li>下游資料仍受各原始來源的授權條款約束（見<a href="{{ '/sources/' | relative_url }}">資料來源</a>）。</li>
</ol>

---

## 關於開發單位

本平台由**藥提醒科技有限公司**（yao.care）開發與維運。公司資料、TxGNN 模型背景與產品線各站一覽，
見<a href="{{ '/about/' | relative_url }}">關於專案</a>。

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
