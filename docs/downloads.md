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

本平台由**藥提醒科技有限公司**（yao.care，統一編號 83620786，地址：台中市西區台灣大道二段220號12樓）開發與維運。

HkTxGNN 是該公司「TxGNN 老藥新用」產品線的Hong Kong站。同一套系統已部署於 30 個國家／地區，
各站依 `{國碼}TxGNN` 命名（JpTxGNN、UsTxGNN、DETxGNN…），網址格式為 `{國碼}txgnn.yao.care`。
產品總覽見 <https://www.yao.care/medical/txgnn/>。

TxGNN 模型本身由哈佛醫學院 Zitnik Lab 開發並發表於 *Nature Medicine*；
本平台是藥提醒科技有限公司以該模型為基礎建置的落地系統，負責各國藥證資料串接、
知識圖譜與深度學習雙引擎預測、PubMed／ClinicalTrials 證據分級，以及 SMART on FHIR 電子病歷整合。

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
