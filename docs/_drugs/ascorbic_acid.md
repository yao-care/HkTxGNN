---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid（抗壞血酸）：從維生素C缺乏症到非症候性食道畸形

## 一句話總結

Ascorbic Acid（維生素C，抗壞血酸）是人體不可或缺的水溶性維生素，其最核心的確立用途為預防與治療維生素C缺乏症（壞血病）。TxGNN 模型預測它可能對**非症候性食道畸形 (Non-syndromic Esophageal Malformation)** 有效，惟目前**無任何臨床試驗或文獻**直接支持此方向，屬純粹模型推測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素C缺乏症（壞血病） |
| 預測新適應症 | 非症候性食道畸形 (Non-syndromic Esophageal Malformation) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的 DrugBank 作用機轉資料。根據已知資訊，Ascorbic Acid 是**膠原蛋白合成的必要輔因子**，負責催化脯胺酸羥化酶（prolyl hydroxylase）和賴胺酸羥化酶（lysyl hydroxylase）的活化反應，對穩定膠原蛋白三股螺旋結構至關重要。此外，它是強效水溶性抗氧化劑，能清除自由基，並作為 TET 雙加氧酶（TET dioxygenase）的輔因子，參與 DNA 去甲基化等表觀遺傳調控過程。

食道壁的結構完整性高度依賴結締組織中的膠原蛋白支架。從理論角度，維生素C可能透過促進食道上皮及基底膜的膠原蛋白合成，對食道組織的形成產生間接影響，提供了一條遠端機制路徑。

然而，非症候性食道畸形為**先天性結構發育異常**（典型如食道閉鎖 Esophageal Atresia、氣管食道瘻管 Tracheoesophageal Fistula），其病因主要涉及胚胎發育早期的基因調控障礙（如 SOX2、FOXF1、GLI3 突變），與維生素C的代謝路徑並無已知直接交集。TxGNN 高分（99.96%）可能反映知識圖譜中「維生素C → 膠原蛋白 → 食道結構」的遠端路徑連接，而非直接致病機制。目前推論極度薄弱，完全缺乏機轉研究佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
非症候性食道畸形為先天性基因調控異常所致的結構缺陷，其病因與維生素C的膠原蛋白合成或抗氧化路徑無直接交集。目前完全缺乏任何臨床前、動物或臨床研究支持此預測（L5，Decision Stage S0），不具備推進條件。

**若要推進需要：**
- 建立孕期維生素C缺乏影響胚胎食道形態發育的機制假說
- 動物模型驗證（維生素C缺乏孕鼠後代食道畸形發生率）
- 探索 TET 酶輔因子功能與先天食道異常的表觀遺傳學關聯
- 流行病學資料：孕期維生素C攝取與先天食道異常發生率的相關性分析

---

> **📌 補充說明（其他高證據等級預測）**
>
> 本 Evidence Pack 涵蓋 10 項預測，其中以下三項具有更強的臨床證據，建議優先評估：
>
> | 預測適應症 | 排名 | 證據等級 | 建議 |
> |-----------|------|---------|------|
> | 維生素缺乏症 (Vitamin Deficiency Disorder) | #10 | L1 | Proceed with Guardrails |
> | 圍產期疾病 (Perinatal Disease) | #8 | L1 | Proceed with Guardrails |
> | 損傷 (Injury) | #4 | L2 | Research Question |
>
> 其中**維生素缺乏症**本為維生素C的核心確立適應症（包含壞血病治療與缺鐵性貧血鐵吸收促進），有多項已完成的 RCT 支持；**圍產期疾病**（子癇前症預防、新生兒缺氧缺血性腦病）則有來自多個 Phase 3 RCT 的高品質證據，最具研究價值。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

