---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 9
monitor_inn: "Ioversol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-10-28
description: "Ioversol：預測新適應症為骨關節炎 (Osteoarthritis)（證據等級 L5）。原適應症：本次整理的資料中，香港許可證未提供核准適應症文字"
---

# Ioversol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Ioversol：從放射顯影造影劑到退化性關節炎（骨關節炎）的預測評估
{: .text-alpha }

## 一句話總結

Ioversol 是含碘的放射顯影造影劑，用於影像檢查，並非治療藥物。
TxGNN 模型預測它可能對**骨關節炎 (Osteoarthritis)** 有效，但目前**沒有任何臨床試驗**，僅有 **1 篇**間接相關的文獻，且該文獻研究的並非 ioversol，因此證據實質上僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，香港許可證未提供核准適應症文字 |
| 預測新適應症 | 骨關節炎 (Osteoarthritis) |
| TxGNN 預測分數 | 0.9963 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

> 說明：資料中雖將此預測標示為 L4，但唯一的文獻研究的是使用碘化油（Lipiodol）的膝動脈栓塞術，並未研究 ioversol 本身。依證據等級上限規則，應判定為 L5。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ioversol 是含碘的放射顯影造影劑，沒有已知的抗骨關節炎藥理作用。

唯一連結的文獻（LipioJoint-1 試驗）研究的是以碘化油乳劑進行膝動脈栓塞術來治療膝骨關節炎，使用的栓塞劑並非 ioversol。兩者的關聯僅是間接的影像或程序上的關聯（同屬含碘造影相關材料），並不支持 ioversol 具有治療角色。

因此，這個極高的預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據，**不宜視為合理的藥理假說**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | 臨床試驗（單臂、栓塞術） | Diagnostic and Interventional Imaging | 評估以碘化油乳劑進行暫時性膝動脈栓塞治療膝骨關節炎的安全性與療效；使用的是 Lipiodol，並非 ioversol |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-38527 | OPTIRAY-350 INJ 74% | 注射劑 | 資料未提供 |
| HK-38528 | OPTIRAY-300 INJ 64% | 注射劑 | 資料未提供 |
| HK-38526 | OPTIRAY-320 INJ 68% | 注射劑 | 資料未提供 |

三張許可證皆為單一成分製劑，持證商為 GUERBET ASIA PACIFIC LIMITED，狀態均為有效。

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為部分列出的主要項目：
  - 嚴重（Major）：Metformin、Amphotericin B（含脂質複合體、膽固醇硫酸酯、脂質體劑型）、Mesalazine、Balsalazide、Olsalazine、Sulfasalazine、Vancomycin、Kanamycin、Neomycin、Streptomycin、Polymyxin B
  - 中度（Moderate）：Mannitol
  - 等級未明：Atropine、Famotidine、Acetylsalicylic acid、Morphine、Omeprazole

其餘警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Ioversol 是造影劑，沒有已知的抗骨關節炎機轉；唯一的文獻研究的是另一種含碘油劑的栓塞術，並非 ioversol。
- 預測僅依賴模型分數，無臨床試驗或直接研究支持，證據等級為 L5。

**若要推進需要：**
- 取得 ioversol 的作用機轉與完整仿單安全性資料（警語、禁忌症）
- 找到直接以 ioversol 研究骨關節炎的前臨床或臨床證據
- 確認此預測是否僅反映模型從相關疾病間學到的相似性，而非生物學證據；在缺乏上述證據前，不建議投入開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

