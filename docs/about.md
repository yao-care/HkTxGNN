---
layout: default
title: 關於專案
nav_order: 90
permalink: /about/
description: "HkTxGNN 是藥提醒科技有限公司開發的老藥新用預測平台，基於哈佛 TxGNN 模型，提供Hong Kong Department of Health HK 核准藥品的驗證報告。"
---

# 關於專案

<div class="key-takeaway">
用 AI 加速老藥新用的證據驗證，從預測到證據一目瞭然。
</div>

---

## 專案背景

<p class="key-answer" data-question="HkTxGNN 是什麼？">
<strong>HkTxGNN</strong> 是一個藥物再利用（Drug Repurposing）研究輔助平台，基於哈佛大學 Zitnik Lab 發表於 <em>Nature Medicine</em> 的 TxGNN 模型，針對Hong Kong Department of Health HK 核准藥品進行適應症擴展預測。本平台不僅提供 AI 預測分數，更整合 ClinicalTrials.gov、PubMed 等來源的臨床證據，讓研究人員能快速評估預測的可信度。
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

## 什麼是老藥新用？

<p class="key-answer" data-question="什麼是老藥新用？">
<strong>老藥新用（Drug Repurposing）</strong> 是指發現現有藥物的新治療用途。相較於從頭開發新藥需要 10-15 年和 10-20 億美元，老藥新用只需 3-5 年和 1-3 億美元，且已有人體安全性資料，失敗風險較低。
</p>

<table class="comparison-table">
<thead>
<tr><th>比較項目</th><th>新藥開發</th><th>老藥新用</th></tr>
</thead>
<tbody>
<tr><td>開發時間</td><td>10-15 年</td><td>3-5 年</td></tr>
<tr><td>開發成本</td><td>10-20 億美元</td><td>1-3 億美元</td></tr>
<tr><td>安全性資料</td><td>需重新建立</td><td>已有人體資料</td></tr>
<tr><td>失敗風險</td><td>極高 (&gt;90%)</td><td>較低</td></tr>
</tbody>
</table>

---

## 什麼是 TxGNN？

<p class="key-answer" data-question="什麼是 TxGNN？">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> 是由哈佛醫學院 Zitnik Lab 團隊開發的深度學習模型，發表於 <em>Nature Medicine</em>，專門用於預測藥物與疾病的新關聯，是首個專為臨床醫師設計的老藥新用基礎模型。
</p>

<blockquote class="expert-quote">
「TxGNN 整合了 17,080 個生物醫學實體的知識圖譜，使用圖神經網路學習節點間的複雜關聯，能預測藥物對罕見疾病的潛在療效。」
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## 資料來源

<table class="comparison-table">
<thead>
<tr><th>資料類型</th><th>來源</th><th>說明</th></tr>
</thead>
<tbody>
<tr><td>AI 預測</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>哈佛大學知識圖譜預測模型</td></tr>
<tr><td>臨床試驗</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>全球臨床試驗登記資料庫</td></tr>
<tr><td>學術文獻</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>生物醫學文獻資料庫</td></tr>
<tr><td>藥物資訊</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>藥物與靶點資料庫</td></tr>
<tr><td>藥證資料</td><td><a href="https://www.drugoffice.gov.hk/">Department of Health HK</a></td><td>Hong Kong藥品核准資料</td></tr>
</tbody>
</table>

---

## 學術依據

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## 專案規模

| 項目 | 數量 |
|------|------|
| 藥物報告 | 1626 份 |
| 主管機關 | Department of Health HK |
| 部署站台 | 30 個國家／地區 |

---

## 聯絡與回饋

- **GitHub Issues**：<https://github.com/yao-care/HkTxGNN/issues>
- **開發單位**：藥提醒科技有限公司（<https://www.yao.care>，service@yao.care）
- **產品總覽**：<https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
