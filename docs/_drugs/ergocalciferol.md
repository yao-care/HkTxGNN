---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ergocalciferol（維生素D2）：從維生素D缺乏症到家族性孤立性副甲狀腺功能低下症

## 一句話總結

Ergocalciferol（維生素D2，DB00153）是全球廣泛用於維生素D缺乏症、佝僂病及骨軟化症的脂溶性維生素前體，目前香港無核准許可證記錄。TxGNN 模型預測其最高分適應症為**家族性孤立性副甲狀腺功能低下症（PTH 分泌缺損型）**，預測分數達 99.85%，但此特定亞型目前完全缺乏臨床試驗與文獻直接支持（L5）。值得關注的是，前 10 名預測中有 3 個適應症（低磷血症、腎性骨病、低磷血症性佝僂病）具備 L3 等級臨床證據，建議作為優先再利用評估目標。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港核准許可證記錄（全球已知用途：維生素D缺乏症、佝僂病） |
| 預測新適應症（排名第一） | 家族性孤立性副甲狀腺功能低下症（Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion） |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Ergocalciferol 的詳細作用機轉資料（MOA 待確認）。根據已知藥理學，Ergocalciferol 是植物來源的維生素D2，在體內經肝臟 CYP2R1 羥化為 25(OH)D₂，再由腎臟 CYP27B1（1α-hydroxylase）轉化為活性代謝物，最終透過核內維生素D受體（VDR）調控鈣磷代謝相關基因的轉錄，促進腸道鈣磷吸收，並回饋調節 PTH 分泌。

家族性孤立性副甲狀腺功能低下症（PTH 分泌缺損型）患者因 PTH 分泌障礙而導致嚴重低鈣血症。Ergocalciferol 理論上可透過 VDR 路徑直接促進腸道鈣吸收，**繞過 PTH 依賴途徑**來補償低鈣血症，機轉上具備一定合理性。

然而，此連結目前屬推斷性質。TxGNN 高評分（0.9985）很可能反映知識圖譜中 PTH–鈣代謝節點的廣泛鄰接，而非對此特定遺傳亞型的疾病特異性訊號。目前無任何臨床試驗或文獻直接支持 Ergocalciferol 用於此亞型。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Ergocalciferol（DB00153）目前在香港查無核准許可證，無上市記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **額外安全性警示**：TxGNN 第 9 名預測為 Calcium-Alkali Syndrome（鈣-鹼症候群），此疾病以高鈣血症為核心表現。Ergocalciferol 促進腸道鈣吸收的機轉，在此疾病中理論上屬**禁忌症而非適應症**，疑似系統在該條目產出了反向有害關聯（adverse association），而非治療性預測。評估任何 Ergocalciferol 新適應症時，均應納入高鈣血症風險監測計畫。

---

## 結論與下一步

**決策：Hold**

**理由：**
第一名預測（家族性孤立性副甲狀腺功能低下症）雖分數極高（99.85%），但完全缺乏臨床試驗與文獻支持（L5），機轉連結屬推斷性質，尚不具備再利用啟動條件。

**若要推進需要：**
- 補充 Ergocalciferol 作用機轉資料（查詢 DrugBank API）
- 取得香港原廠仿單（警語、禁忌症、藥物交互作用）
- 針對此遺傳亞型進行專項文獻搜尋（建議關鍵詞：ergocalciferol hypoparathyroidism calcium homeostasis PTH）

---

## 附錄：十大預測適應症完整摘要

本次 TxGNN 評估共產出 10 個預測適應症，排名 6–8 具備更強的再利用潛力，建議優先深入評估：

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗 | 文獻 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|------|----------|---------|
| 1 | Familial Isolated Hypoparathyroidism（PTH 分泌缺損型） | 99.85% | 0 | 0 | L5 | Hold |
| 2 | Acromesomelic Dysplasia, Campailla Martinelli Type | 99.83% | 0 | 0 | L5 | Hold |
| 3 | Renal Tubular Acidosis（腎小管酸中毒） | 99.81% | 0 | 8 | L4 | Research Question |
| 4 | Craniofacial Conodysplasia | 99.81% | 0 | 0 | L5 | Hold |
| 5 | Dahlberg-Borer-Newcomer Syndrome ⚠️ | 99.81% | 0 | 20† | L4 | Hold |
| **6** | **Hypophosphatemia（低磷血症）** | **99.72%** | **3** | **20** | **L3** | **Proceed with Guardrails** |
| **7** | **Renal Osteodystrophy（腎性骨病）** | **99.67%** | **2** | **20** | **L3** | **Proceed with Guardrails** |
| **8** | **Hypophosphatemic Rickets（低磷血症性佝僂病）** | **99.67%** | **0** | **20** | **L3** | **Proceed with Guardrails** |
| 9 | Calcium-Alkali Syndrome ⚠️ 潛在禁忌 | 99.46% | 0 | 0 | L5 | Hold |
| 10 | Vitamin D-Dependent Rickets ⚠️ 資料不完整‡ | 99.39% | 0 | 0 | L5 | Research Question |

† 排名第 5 的 20 篇文獻，經分析後均為一般性維生素D研究（代謝症候群、PCOS、VDR 自噬調節等），無一直接針對 Dahlberg-Borer-Newcomer syndrome，屬 KG 骨骼節點廣泛連接所產生的非特異性匹配。

‡ 排名第 10 的 L5 反映資料收集盲點而非真實證據缺口——Vitamin D-Dependent Rickets Type I（VDDR1A，CYP27B1 突變）為高劑量 Ergocalciferol 的教科書適應症。強烈建議補充 PubMed 搜尋（關鍵詞：ergocalciferol vitamin D-dependent rickets CYP27B1 VDDR），預期可提升至 L3–L4。

> 💡 **建議行動**：排名 6–8 的低磷血症、腎性骨病及低磷血症性佝僂病，均有臨床文獻直接記錄 Ergocalciferol 的治療效果，機轉明確，建議優先針對這三個適應症撰寫個別深度評估報告。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

