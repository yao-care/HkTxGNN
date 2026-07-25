---
layout: default
title: 中證據等級 (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "HkTxGNN 中 L3-L4 等級的老藥新用候選，具觀察性研究或前臨床證據。"
---

# 中證據等級 (L3-L4)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
具初步證據、需進一步驗證的候選藥物
</p>

---

## 證據標準

| 等級 | 定義 | 臨床意義 |
|------|------|---------|
| **L3** | 觀察性研究／大型病例系列 | 初步支持，需進一步驗證 |
| **L4** | 前臨床／機轉研究 | 理論支持，距臨床尚遠 |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 等級 ({{ l3_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 等級 ({{ l4_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
