---
layout: default
title: 資料來源
nav_order: 93
permalink: /sources/
description: "HkTxGNN 的資料來源清單：衛生署藥物辦公室藥劑製品清單（DrugList.xml）、TxGNN、ClinicalTrials.gov、PubMed、DrugBank。"
---

# 資料來源

<div class="key-takeaway">
所有結論都可追溯到公開資料來源，沒有黑箱。
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## 香港：本站資料

本站公開 **{{ site.data.drug_stats.total_drugs }}** 個藥品的報告，藥品來自[衛生署藥物辦公室](https://www.drugoffice.gov.hk/)的許可證資料（香港）。

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

## 資料來源總覽

<table class="comparison-table">
<thead>
<tr><th>資料類型</th><th>來源</th><th>用途</th></tr>
</thead>
<tbody>
<tr><td>藥證資料</td><td>衛生署藥物辦公室 <a href="https://www.drugoffice.gov.hk/eps/psi/DrugList.xml">藥劑製品清單（DrugList.xml）</a></td><td>香港現行註冊的藥劑製品（註冊編號 HK-xxxxx）與成分</td></tr>
<tr><td>預測模型</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>藥物-疾病關聯預測</td></tr>
<tr><td>臨床試驗</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>證據等級判定（NCT）</td></tr>
<tr><td>學術文獻</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>證據等級判定（PMID）</td></tr>
<tr><td>藥物資訊</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>成分對應與靶點資料</td></tr>
<tr><td>交互作用</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>藥物交互作用資料</td></tr>
</tbody>
</table>

DrugList.xml 只列現行註冊的產品、沒有狀態欄；某個註冊編號不在新清單裡時，本站保留原狀態，不推定為已撤銷。

---

## 授權與使用條款

各來源有各自的授權條款，引用前請確認：

- **TxGNN**：學術用途，引用 Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**：美國 NIH 公開資料
- **DrugBank**：非商業用途需遵循其授權條款
- **衛生署藥物辦公室 DrugList.xml**：公開檔案、免註冊即可下載；依藥物辦公室網站的使用條款

---

## 更新頻率

| 資料 | 更新頻率 |
|------|---------|
| 註冊狀態 | 每週一自動以 DrugList.xml 比對更新 |
| 臨床試驗／文獻證據 | 定期重新收集 |
| 交互作用資料 | 每季檢查 |

---

## 學術引用

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

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
