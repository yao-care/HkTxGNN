---
layout: default
title: 藥物總覽
nav_order: 20
permalink: /drugs/
description: "HkTxGNN 收錄的所有藥物驗證報告與證據等級統計。"
---
{%- comment -%}2026-10-27 build gate：站上各頁的藥物數讀 site.data.drug_stats；它和實際公開藥物頁數／等級分布不一致時，
故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign gate_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign gate_ds = site.data.drug_stats -%}
{%- assign gate_l1 = gate_listed | where: "evidence_level", "L1" | size -%}
{%- assign gate_l2 = gate_listed | where: "evidence_level", "L2" | size -%}
{%- assign gate_l3 = gate_listed | where: "evidence_level", "L3" | size -%}
{%- assign gate_l4 = gate_listed | where: "evidence_level", "L4" | size -%}
{%- assign gate_l5 = gate_listed | where: "evidence_level", "L5" | size -%}
{%- if gate_listed.size != gate_ds.total_drugs or gate_l1 != gate_ds.level_counts.L1 or gate_l2 != gate_ds.level_counts.L2 or gate_l3 != gate_ds.level_counts.L3 or gate_l4 != gate_ds.level_counts.L4 or gate_l5 != gate_ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign l1_count = listed_drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = listed_drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = listed_drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = listed_drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = listed_drugs | where: "evidence_level", "L5" | size %}

# 藥物總覽

共 {{ listed_drugs.size }} 個藥物的驗證報告

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
本列表依據[衛生署藥物辦公室](https://www.drugoffice.gov.hk/)的許可證資料（香港）。

<!-- local-home:end -->

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

{% assign all_drugs = listed_drugs | sort: 'title' %}

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
