---
layout: default
title: 藥物總覽
nav_order: 20
permalink: /drugs/
description: "HkTxGNN 收錄的所有藥物驗證報告與證據等級統計。"
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# 藥物總覽

共 {{ site.drugs.size }} 個藥物的驗證報告

---

## 證據等級統計

| 證據等級 | 藥物數 | 說明 |
|---------|--------|------|
| **L1** | {{ l1_count }} | 多個 RCT／系統性回顧 |
| **L2** | {{ l2_count }} | 單一 RCT／Phase 2 試驗 |
| **L3** | {{ l3_count }} | 觀察性研究／大型病例系列 |
| **L4** | {{ l4_count }} | 前臨床／機轉研究 |
| **L5** | {{ l5_count }} | 僅模型預測 |

---

## 完整藥物列表

{% assign all_drugs = site.drugs | sort: 'title' %}

| 藥物名稱 | 證據等級 | 適應症數 |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
