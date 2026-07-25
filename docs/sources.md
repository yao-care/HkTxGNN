---
layout: default
title: 資料來源
nav_order: 93
permalink: /sources/
description: "HkTxGNN 的資料來源清單：Department of Health HK 藥證資料、TxGNN、ClinicalTrials.gov、PubMed、DrugBank。"
---

# 資料來源

<div class="key-takeaway">
所有結論都可追溯到公開資料來源，沒有黑箱。
</div>

---

## 資料來源總覽

<table class="comparison-table">
<thead>
<tr><th>資料類型</th><th>來源</th><th>用途</th></tr>
</thead>
<tbody>
<tr><td>藥證資料</td><td><a href="https://www.drugoffice.gov.hk/">Department of Health HK</a></td><td>Hong Kong核准藥品清單與成分</td></tr>
<tr><td>預測模型</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>藥物-疾病關聯預測</td></tr>
<tr><td>臨床試驗</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>證據等級判定（NCT）</td></tr>
<tr><td>學術文獻</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>證據等級判定（PMID）</td></tr>
<tr><td>藥物資訊</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>成分對應與靶點資料</td></tr>
<tr><td>交互作用</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>藥物交互作用資料</td></tr>
</tbody>
</table>

---

## 授權與使用條款

各來源有各自的授權條款，引用前請確認：

- **TxGNN**：學術用途，引用 Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**：美國 NIH 公開資料
- **DrugBank**：非商業用途需遵循其授權條款
- **Department of Health HK**：依Hong Kong主管機關的開放資料條款

---

## 更新頻率

| 資料 | 更新頻率 |
|------|---------|
| 藥證資料 | 依主管機關發布 |
| 臨床試驗／文獻證據 | 定期重新收集 |
| 交互作用資料 | 每季檢查 |

---

## 學術引用

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

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
