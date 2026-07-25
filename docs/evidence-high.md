---
layout: default
title: 高證據等級 (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "HkTxGNN 中 L1-L2 等級的老藥新用候選，具多項臨床試驗或系統性回顧支持。"
---

# 高證據等級 (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
可優先考慮進入臨床評估階段的候選藥物
</p>

---

## 證據標準

| 等級 | 定義 | 臨床意義 |
|------|------|---------|
| **L1** | 多個 Phase 3 RCT／系統性回顧 | 強力支持，可考慮臨床使用 |
| **L2** | 單一 RCT 或多個 Phase 2 試驗 | 中等支持，可設計驗證試驗 |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 等級 ({{ l1_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 等級 ({{ l2_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
