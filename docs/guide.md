---
layout: default
title: 使用指南
nav_order: 92
permalink: /guide/
description: "HkTxGNN 使用指南：如何查詢藥物、解讀證據等級與決策建議。"
---

# 使用指南

<div class="key-takeaway">
先看證據等級，再看決策建議，最後查原始文獻。
</div>

---

## 如何查詢藥物

<ol class="actionable-steps">
<li>使用頁面上方的搜尋框輸入藥物名稱（英文成分名比商品名更容易命中）。</li>
<li>或從<a href="{{ '/drugs/' | relative_url }}">藥物總覽</a>瀏覽完整清單。</li>
<li>也可依證據等級瀏覽：<a href="{{ '/evidence-high/' | relative_url }}">高證據</a>、<a href="{{ '/evidence-medium/' | relative_url }}">中證據</a>、<a href="{{ '/evidence-low/' | relative_url }}">僅模型預測</a>。</li>
</ol>

---

## 如何解讀報告

<p class="key-answer" data-question="證據等級 L1-L5 代表什麼？">
每份藥物報告包含預測的新適應症清單，每個適應症標有 L1-L5 證據等級。<strong>L1 表示已有多個 Phase 3 隨機對照試驗支持，L5 表示僅有模型預測、尚無人體證據</strong>。詳細分級標準見<a href="{{ '/methodology/' | relative_url }}">方法論</a>。
</p>

| 看到這個 | 代表 | 建議動作 |
|---------|------|---------|
| L1 / L2 | 已有臨床試驗證據 | 可查閱原始 NCT 與 PMID |
| L3 / L4 | 觀察性或前臨床證據 | 視為研究線索 |
| L5 | 僅模型預測 | 僅供假說發想，勿作臨床參考 |

---

## 引用與追溯

報告中的每一條證據都附有可追溯的識別碼：

- **NCT 編號**：連向 ClinicalTrials.gov 的臨床試驗登記
- **PMID**：連向 PubMed 的文獻條目
- **DrugBank ID**：連向藥物與靶點資料

建議在引用本平台結論前，先閱讀原始文獻確認脈絡。

---

## 常見問題

<p class="key-answer" data-question="預測結果可以直接用於臨床嗎？">
<strong>不可以。</strong>本平台的預測結果是研究線索，不是臨床建議。任何老藥新用的臨床應用都必須經過完整的臨床試驗驗證與主管機關審查。
</p>

<p class="key-answer" data-question="為什麼有些藥物查不到？">
藥品成分需能對應到 DrugBank 詞彙表才會納入預測。中草藥萃取物、疫苗、賦形劑等 DrugBank 未收錄的成分不會出現在本平台。
</p>

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
