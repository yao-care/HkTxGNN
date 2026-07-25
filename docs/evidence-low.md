---
layout: default
title: 僅模型預測 (L5)
nav_order: 23
permalink: /evidence-low/
description: "HkTxGNN 中 L5 等級的候選，僅由模型預測，尚無臨床或文獻證據支持。"
---

# 僅模型預測 (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
僅有模型預測、尚無人體證據的候選藥物
</p>

---

## 證據標準

| 等級 | 定義 | 臨床意義 |
|------|------|---------|
| **L5** | 僅模型預測 | 假說階段，尚無人體證據 |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 等級 ({{ l5_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
