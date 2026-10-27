---
layout: default
title: Aminophylline
parent: 中證據等級 (L3-L4)
nav_order: 53
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Aminophylline：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L4）。原適應症：目前許可證資料未載明"
monitor_inn: "AMINOPHYLLINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "Prinzmetal angina", "pulmonary hypertension", "sciatic neuropathy", "hyperthyroidism", "kyphoscoliotic heart disease"]
---

# Aminophylline
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Aminophylline：從（原適應症未載明）到偏頭痛
{: .text-alpha }

## 一句話總結

Aminophylline（胺茶鹼）是一種注射用的甲基黃嘌呤類藥物，在香港已有 2 張有效許可證，但目前資料中未載明核准適應症。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，目前**沒有臨床試驗**，僅有 **4 篇相關文獻**（1 篇 2023 年綜述、其餘為病例報告或間接資料），證據偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料未載明 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏來自藥物資料庫的詳細作用機轉資料。根據文獻，Aminophylline 是非選擇性腺苷受體拮抗劑，同時也是磷酸二酯酶抑制劑。

偏頭痛的病理機轉尚未完全釐清，但有研究認為可能與腦能量代謝受損及腺苷濃度異常升高有關。腺苷訊號與三叉神經血管活化及腦血管擴張有關，因此以 Aminophylline 阻斷腺苷受體，在機轉上有可能緩解症狀。2023 年有一篇專文討論 Aminophylline 在疼痛與偏頭痛的應用，指出它對疼痛（尤其是硬脊膜穿刺後頭痛）可能有明顯緩解效果。

不過，其他佐證都是間接的：例如 regadenoson（腺苷 A2A 受體促效劑）誘發偏頭痛的病例，以及腺苷過量導致「心臟型偏頭痛」的個案。這些資料只能說明腺苷拮抗「可能」有保護作用，尚不足以證明療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review | Pain management | 偏頭痛可能與腦能量代謝受損及腺苷過高有關；Aminophylline 作為腺苷拮抗劑，對疼痛（特別是硬脊膜穿刺後頭痛）可能有療效 |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case report | J Nucl Cardiol | Regadenoson（腺苷 A2A 促效劑）誘發偏動性偏頭痛發作，間接支持腺苷參與偏頭痛 |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case report | Can J Cardiol | 腺苷效應過強導致的 X 症候群（心臟型偏頭痛），間接相關 |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Review | Aggiornamenti clinicoterapeutici | 頭痛相關舊文獻，無摘要可供判讀 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-06484 | AMINOPHYLLINE INJ 250MG/10ML | 未載明 | 未載明 |
| HK-59560 | AMINOPHYLLINE INJ 250MG/10ML | 未載明 | 未載明 |

---

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下為部分代表：
  - **重大 (Major)**：Bupropion
  - **中度 (Moderate)**：Famotidine、Ranitidine、Cimetidine、Nizatidine（H2 受體拮抗劑）；Doxycycline、Tetracycline、Minocycline、Clarithromycin（抗生素）；Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide（皮質類固醇）
  - **輕微 (Minor)**：Lansoprazole

其他警語與禁忌症請參考原廠仿單。

另外，在其他預測適應症的文獻中也出現值得留意的信號：Aminophylline 在變異型心絞痛（Prinzmetal angina）患者中曾被報告誘發冠狀動脈痙攣；在甲狀腺機能亢進患者中，茶鹼類藥物可能加重震顫。若未來對偏頭痛族群進行研究，需特別留意心血管疾病與甲狀腺疾病患者。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛的預測分數雖高，但沒有任何臨床試驗，文獻多為綜述、病例報告與間接機轉資料，屬於「研究問題」階段，尚不足以推進。
- 香港許可證資料缺少核准適應症與仿單安全性資訊，無法進行完整的安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料（例如 DrugBank）
- 針對偏頭痛（尤其是急性發作或硬脊膜穿刺後頭痛）設計小型隨機對照試驗
- 評估注射劑型用於偏頭痛的可行性，並建立心血管、甲狀腺疾病患者的排除與監測計畫
- 針對茶鹼治療窗窄的特性，規劃血中濃度監測
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

