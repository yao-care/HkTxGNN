---
layout: default
title: 方法論
nav_order: 91
permalink: /methodology/
description: "HkTxGNN 的預測與證據驗證方法：TxGNN 知識圖譜預測、證據收集、L1-L5 證據分級與決策建議。"
---

# 方法論

<div class="key-takeaway">
從 AI 預測到證據分級，每一個候選都有可追溯的判定依據。
</div>

---

## 整體流程

<p class="key-answer" data-question="HkTxGNN 如何產生預測結果？">
本平台採四階段流程：先以 TxGNN 知識圖譜模型預測藥物與疾病的潛在關聯，再針對每個預測配對自動收集臨床試驗與文獻證據，接著依證據強度判定 L1-L5 等級，最後給出決策建議。
</p>

<ol class="actionable-steps">
<li><strong>TxGNN 預測</strong>：使用知識圖譜結合圖神經網路進行藥物-疾病關係預測。</li>
<li><strong>證據收集</strong>：針對每個預測配對，自動收集 ClinicalTrials.gov、PubMed、DrugBank、Department of Health HK 等來源的證據。</li>
<li><strong>證據等級判定</strong>：依收集到的證據判定 L1-L5 等級，L1 最高（多個 Phase 3 RCT），L5 為僅模型預測。</li>
<li><strong>決策建議</strong>：依證據等級給出 Go、Proceed、Consider、Explore、Hold 建議。</li>
</ol>

---

## 證據分級標準

<table class="comparison-table">
<thead>
<tr><th>等級</th><th>定義</th><th>臨床意義</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>多個 Phase 3 RCT／系統性回顧</td><td>強力支持，可考慮臨床使用</td></tr>
<tr><td><strong>L2</strong></td><td>單一 RCT 或多個 Phase 2 試驗</td><td>中等支持，可設計驗證試驗</td></tr>
<tr><td><strong>L3</strong></td><td>觀察性研究／大型病例系列</td><td>初步支持，需進一步驗證</td></tr>
<tr><td><strong>L4</strong></td><td>前臨床／機轉研究</td><td>理論支持，距臨床尚遠</td></tr>
<tr><td><strong>L5</strong></td><td>僅模型預測</td><td>假說階段，尚無人體證據</td></tr>
</tbody>
</table>

---

## 雙引擎預測

本平台同時使用兩種方法，並以信心度標示兩者的一致性：

| 方法 | 速度 | 精準度 | 說明 |
|------|------|--------|------|
| 知識圖譜（KG） | 快 | 較低 | 以 DrugBank 關聯與圖結構推論 |
| 深度學習（DL） | 慢 | 較高 | TxGNN 圖神經網路模型 |

| 信心度 | 來源 | 說明 |
|--------|------|------|
| very_high | KG + DL | 兩種方法都支持 |
| high | 僅 DL | 深度學習模型高分支持 |
| medium | 僅 KG | 知識圖譜支持 |

---

## 藥證資料串接

Hong Kong的藥品核准資料來自 Department of Health HK。系統將藥品成分名對應到 DrugBank 詞彙表，
未能對應的成分（中草藥萃取物、疫苗、賦形劑等 DrugBank 未收錄者）不納入預測。

---

## 方法限制

<ol class="actionable-steps">
<li>預測結果為統計關聯，<strong>不等於因果關係或臨床療效</strong>。</li>
<li>L5 等級僅代表模型預測，尚無任何人體證據支持。</li>
<li>證據收集依賴公開資料庫，未公開或未索引的研究不會被納入。</li>
<li>藥品成分對應可能因命名差異而遺漏部分品項。</li>
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
