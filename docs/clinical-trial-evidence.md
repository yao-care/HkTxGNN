---
layout: default
title: "香港藥物：新適應症已有臨床試驗證據的藥物"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "香港註冊藥劑製品中，TxGNN 預測新適應症已有臨床試驗證據（L1–L2）的藥物：預測適應症、證據等級與已註冊試驗數。"
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「見藥物報告」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "預測新適應症" | split: "|" -%}
{%- assign lev_labels = "證據等級" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# 香港藥物中，新適應症已有臨床試驗證據的藥物

<p class="key-answer" data-question="香港的藥物中，哪些新適應症已有臨床試驗證據？">
HkTxGNN 已有報告的 {{ listed.size }} 種藥物中，有 <strong>{{ trial_drugs.size }}</strong> 種的 TxGNN 預測新適應症證據等級達 <strong>L1 或 L2</strong>（L1 {{ l1.size }} 種、L2 {{ l2.size }} 種），即已找到臨床試驗證據（隨機對照試驗、Phase 2–3 試驗或系統性回顧）。
</p>

藥物來自衛生署藥物辦公室的[藥劑製品清單](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)（香港註冊藥劑製品，各藥物報告列出註冊狀態）；清單反映最後更新於 {{ latest_date }} 的藥物報告。

<div class="key-takeaway">
預測適應症有試驗證據，不等於療效已獲證實。以下每個候選<strong>仍需臨床驗證</strong>及監管審查，才可考慮臨床應用。
</div>

---

## 有試驗證據的藥物（L1–L2）

<div class="table-wrapper"><table>
<thead>
<tr><th>藥物</th><th>預測新適應症</th><th>證據等級</th><th>引用的已註冊試驗（NCT）</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}見藥物報告{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">（附保留說明）</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## 如何閱讀這份清單

- **證據等級**依本站[標準]({{ '/evidence-high/' | relative_url }})：L1＝多個 Phase 3 RCT／系統性回顧；L2＝單一 RCT 或多個 Phase 2 試驗。「（附保留說明）」表示報告對該等級另有保留，請先閱讀報告內的說明。
- **預測新適應症**是各報告的主要預測。TxGNN 知識圖譜已記錄的適應症與禁忌症已排除，但部分預測仍可能與既有用途重疊；適用時報告內會說明。
- **引用的已註冊試驗**是報告引用的 ClinicalTrials.gov（NCT）編號數。報告只引用找到的部分試驗；0 表示報告未引用已註冊試驗，等級依據見報告的文獻證據部分。
- 各等級與完整方法見[高證據等級 (L1-L2)]({{ '/evidence-high/' | relative_url }})、[藥物總覽]({{ '/drugs/' | relative_url }})與[研究方法]({{ '/methodology/' | relative_url }})。

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>審核者: 藥提醒科技有限公司 (yao.care)</small>
</div>
