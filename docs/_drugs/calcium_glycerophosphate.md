---
layout: default
title: Calcium Glycerophosphate
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 4
---

# Calcium Glycerophosphate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Calcium Glycerophosphate：從礦物質補充到低磷血症

## 一句話總結

Calcium glycerophosphate 是一種有機磷酸鈣鹽，廣泛用於腸外營養（TPN）配方作為鈣與磷的來源。TxGNN 模型共預測 4 個新適應症，最高分預測 calcium-alkali syndrome（99.95%）研判為模型假陽性；**低磷血症 (Hypophosphatemia)** 雖排名第 4，但機轉最明確、有 **2 個臨床試驗**及 **5 篇文獻**（同類藥物 sodium glycerophosphate）支持，為本次評估最具臨床可行性的方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腸外營養用鈣磷補充劑 |
| 最具潛力預測 | 低磷血症 (Hypophosphatemia) |
| TxGNN 預測分數 | 99.25%（低磷血症，rank 4）；最高分 99.95% 研判假陽性 |
| 證據等級 | L3（低磷血症）；其餘 3 個預測均為 L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails（低磷血症）/ Hold（其餘預測） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Calcium glycerophosphate 是由鈣離子（Ca²⁺）與甘油磷酸根（glycerophosphate）結合的有機磷酸鹽複合物，其成分在礦物質補充與骨骼代謝中的作用已被廣泛認識，機轉上可能適用於低磷血症及相關骨代謝疾病。

**核心機轉假說**：Glycerophosphate 基團在體內經磷酸酶水解後釋放游離磷酸根（HPO₄²⁻），可直接補充血清磷。有機磷酸鹽的關鍵優勢在於：在靜脈輸液中與 Ca²⁺ 共存時不形成難溶的磷酸鈣沉澱（克服傳統無機磷酸鹽的相容性問題），因此可安全應用於 TPN 中同時補充鈣與磷。

**與低磷血症的關聯性**：Calcium glycerophosphate 與 sodium glycerophosphate 共享相同的活性部分（glycerophosphate moiety），後者已有多項新生兒 TPN 臨床研究驗證其在預防/治療早產兒低磷血症的療效。此機轉等效性為 calcium glycerophosphate 提供了合理的外推依據，但需注意本藥同時提供 Ca²⁺，需監控高鈣血症風險。

---

## 所有預測適應症概覽

本 Evidence Pack 共涵蓋 4 個 TxGNN 預測適應症：

| 排名 | 適應症 | 預測分數 | 證據等級 | 建議 |
|------|--------|---------|---------|------|
| 1 | Calcium-Alkali Syndrome | 99.95% | L5 | **Hold**（機轉矛盾，假陽性） |
| 2 | Primary Bone Dysplasia with Defective Bone Mineralization | 99.93% | L5 | **Research Question**（機轉合理，無臨床證據） |
| 3 | Potassium Deficiency Disease | 99.34% | L5 | **Hold**（無機轉關聯，文獻假陽性） |
| 4 | Hypophosphatemia | 99.25% | L3 | **Proceed with Guardrails** |

---

### 預測 1：Calcium-Alkali Syndrome（高分假陽性）

**TxGNN 分數：99.95%** | **建議：Hold**

Calcium-alkali syndrome（舊稱 milk-alkali syndrome）的核心病生理為過量鈣攝入引發的**高鈣血症 + 代謝性鹼中毒 + 腎功能損傷**三聯症。Calcium glycerophosphate 本身即為鈣來源，補充鈣離子只會直接加重病情，機轉上存在根本矛盾。

**判定**：TxGNN 高分源於模型對鈣代謝節點的非因果關聯誤判，屬典型假陽性。無任何臨床試驗或文獻支持，不需進一步追蹤。

---

### 預測 2：Primary Bone Dysplasia with Defective Bone Mineralization（值得列入研究規劃）

**TxGNN 分數：99.93%** | **建議：Research Question**

Calcium glycerophosphate 同時提供 Ca²⁺ 與有機磷酸根，兩者均為羥基磷灰石（hydroxyapatite）骨基質合成的必要底物，對於骨礦化缺陷型疾病（如低磷酸酶症 Hypophosphatasia、X-linked hypophosphatemia 相關骨發育不良）具有合理的補充機轉假說。

**判定**：機轉假說合理，但目前無任何臨床前或臨床證據。建議先確認具體病因亞型（Ca 缺乏型、磷缺乏型或酶缺乏型）再評估可行性，列入後續研究規劃。

---

### 預測 3：Potassium Deficiency Disease（文獻假陽性）

**TxGNN 分數：99.34%** | **建議：Hold**

雖命中 13 篇文獻，但逐一檢視後均非直接支持本藥治療低鉀血症的研究。命中原因多為磷脂（phospholipid）/磷酸肌醇（phosphoinositide）關鍵字的間接匹配（如 KCNQ/Kv7 通道的磷脂調控、腎臟缺鉀狀態下的磷脂代謝），與 calcium glycerophosphate 治療低鉀血症無因果關聯。

**判定**：文獻收集系統假陽性，無直接藥理機轉，不建議追究。

---

## 臨床試驗證據（低磷血症）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06754670](https://clinicaltrials.gov/study/NCT06754670) | N/A | 招募中 | 70 | ICU 早產兒斷奶期低磷血症與機械通氣時間的關聯性研究，評估磷補充對橫膈膜收縮功能的影響（2024 年啟動） |
| [NCT04519762](https://clinicaltrials.gov/study/NCT04519762) | Phase 4 | 不明 | 100 | 評估嚴重敗血症/敗血性休克 ICU 患者的低磷血症發生率，以及磷補充療法對死亡率與罹病率的影響 |

---

## 文獻證據（低磷血症）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35007810](https://pubmed.ncbi.nlm.nih.gov/35007810/) | 2022 | 對照研究 | Clin Nutr | Sodium glycerophosphate 早期（第 1 天）vs 晚期引入早產兒 TPN，早期引入顯著改善血磷平衡並降低高鈣血症發生率 |
| [36255046](https://pubmed.ncbi.nlm.nih.gov/36255046/) | 2023 | 世代研究 | J Pediatr | Sodium glycerophosphate 於極低出生體重兒（ELBW）TPN 中改善礦物質代謝，確認有機磷酸鹽的臨床效益 |
| [4541156](https://pubmed.ncbi.nlm.nih.gov/4541156/) | 1973 | 臨床觀察 | Circulation | 心臟手術後低磷血症導致紅血球 2,3-DPG 及 ATP 降低，血紅素氧親和力上升，確認低磷血症的系統性危害 |
| [4994546](https://pubmed.ncbi.nlm.nih.gov/4994546/) | 1971 | 臨床觀察 | Ann Intern Med | 低磷血症引起紅血球糖解能力降低的機轉研究，奠定低磷血症病理生理基礎 |
| [5122895](https://pubmed.ncbi.nlm.nih.gov/5122895/) | 1971 | 病例系列 | NEJM | 低磷血症引起紅血球硬化性溶血性貧血的早期報告，強調低磷血症的急性危險性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：本次評估有兩項資料缺口——TFDA 仿單警語/禁忌（Blocking 等級）及詳細 MOA 資料（High 等級）——尚未補齊，需於推進前優先解決。

---

## 結論與下一步

**決策：Proceed with Guardrails（低磷血症）**

**理由：**
Calcium glycerophosphate 的 glycerophosphate 活性部分機轉明確對應低磷血症的補磷需求，且同類藥物 sodium glycerophosphate 已有 2023 年 ELBW 嬰兒世代研究及 2022 年對照研究支持有機磷酸鹽在 TPN 中的療效，機轉等效性合理；其餘三個預測（calcium-alkali syndrome、potassium deficiency disease）研判為假陽性，primary bone dysplasia 雖機轉合理但無任何臨床證據，建議列入後續研究但暫不推進。

**若要推進（低磷血症）需要：**
- 補充 TFDA/原廠仿單警語與禁忌症（目前為 Blocking 資料缺口，無法進行 S1 安全性初評）
- 補充詳細 MOA 資料（DrugBank API 查詢）
- 釐清現有 sodium glycerophosphate 研究劑量方案是否可外推至 calcium glycerophosphate
- 評估同時提供 Ca²⁺ 的利弊：對早產兒或腎功能不全患者的高鈣血症風險需特別關注
- 若考慮正式香港許可適應症，需規劃直接針對 calcium glycerophosphate 的前瞻性臨床試驗
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

