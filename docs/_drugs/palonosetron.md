---
layout: default
title: Palonosetron
parent: 中證據等級 (L3-L4)
nav_order: 661
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-28
description: "Palonosetron：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L4）。原適應症：香港許可證資料未載明核准適應症"
monitor_inn: "PALONOSETRON"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

## Palonosetron：從化療相關噁心嘔吐到偏頭痛（模型預測，不建議推進）
{: .text-alpha }

## 一句話總結

Palonosetron 是 5-HT3 受體拮抗劑，在香港已上市，通常用於預防噁心嘔吐。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇個案報告**，而且該報告指出 palonosetron 反而會**誘發**偏頭痛型頭痛。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 0.9974 |
| 證據等級 | L4 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 palonosetron 屬於 5-HT3 受體拮抗劑，而血清素訊號傳遞與偏頭痛有關，因此理論上存在一定的關聯。

不過，唯一檢索到的臨床證據是一篇個案報告，描述的是 palonosetron **誘發**偏頭痛型頭痛。這是指向反方向的安全性訊號，並不支持治療用途。

TxGNN 模型（深度學習）給出的高分（0.9974）可能反映模型從相關疾病之間學到的相似性，並非生物學證據，也無臨床資料佐證。其他預測的適應症（如腦幹先兆偏頭痛、蠕蟲狀皮膚萎縮、眉部毛囊萎縮性紅斑）同樣缺乏機轉依據與研究證據，多半是模型學到的疾病相似性所造成的假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | 個案報告 | Can J Anaesth | Palonosetron 誘發偏頭痛型頭痛（無摘要，依標題判讀） |

另有一篇 2026 年的綜述（[42748473](https://pubmed.ncbi.nlm.nih.gov/42748473/)，Eur Heart J Cardiovasc Pharmacother）探討止吐藥相關的 QT 延長，屬於心臟安全性議題，並非偏頭痛療效證據，僅供參考。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62549 | ALOXI CAPSULES 500MCG | — | — |
| HK-67549 | PALSET SOLUTION FOR INJECTION 0.25MG/5ML | — | — |
| HK-62573 | ALOXI SOLUTION FOR INJECTION 0.075MG/1.5ML | — | — |
| HK-57102 | ALOXI SOLN FOR INJ 50MCG/ML | — | — |
| HK-67828 | AKYNZEO CONCENTRATE FOR SOLUTION FOR INFUSION 235MG/0.25MG IN 20ML | — | — |

另有 HK-65260（AKYNZEO CAPSULES 300MG/0.5MG），共 6 張有效許可證。

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，其中多項為重大（Major）等級，主要包括：
  - 鴉片類／止痛藥：Fentanyl、Alfentanil、Tramadol、Dextromethorphan
  - 血清素相關藥物：Sumatriptan、Almotriptan、Amitriptyline
  - 可能影響心律（QT）的藥物：Amiodarone、Amisulpride、Anagrelide
- **頭痛誘發訊號**：有個案報告指出 palonosetron 可能誘發偏頭痛型頭痛，用於偏頭痛患者需特別留意。
- **心臟安全性**：近期綜述指出止吐藥類別有 QT 延長風險，對有長 QT 症候群的患者需謹慎評估。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛預測僅來自 TxGNN 模型（深度學習），分數可能反映模型學到的相關疾病之間的相似性，並非生物學證據；目前無臨床試驗支持，且唯一的文獻證據顯示該藥可能誘發偏頭痛，與預期療效方向相反。
- 其餘預測適應症缺乏機轉依據與研究資料，不具備推進條件。

**若要推進需要：**
- 補齊 palonosetron 的作用機轉資料，釐清與偏頭痛的實質關聯
- 取得香港仿單的警語、禁忌症與核准適應症
- 系統性檢視 5-HT3 拮抗劑與頭痛／偏頭痛的臨床與藥物安全資料
- 若仍要探索，應先進行前臨床或小規模探索性研究，並建立頭痛誘發與 QT 延長的監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

