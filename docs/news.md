---
layout: default
title: 健康新聞
nav_order: 30
permalink: /news/
has_children: true
description: "HkTxGNN 自動監測藥物與適應症相關的健康新聞報導。"
---

# 健康新聞

<div class="key-takeaway">
自動監測本站收錄藥物與其預測適應症的相關新聞報導。
</div>

---

## 新聞總覽

{% assign items = site.news | where_exp: "n", "n.layout != 'id_redirect'" | sort: 'title' %}
{% if items.size == 0 %}
目前沒有符合的新聞。
{% else %}
{% for item in items %}- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}
{% endif %}

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
