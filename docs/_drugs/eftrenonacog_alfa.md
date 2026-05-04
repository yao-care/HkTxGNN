---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Eftrenonacog Alfa：從血友病 B 到 Pseudo-von Willebrand Disease

## 一句話總結

Eftrenonacog alfa 是一種重組延長型第九凝血因子（Factor IX Fc 融合蛋白），原本用於血友病 B（先天性第九凝血因子缺乏症）的出血預防與治療。TxGNN 模型預測它可能對 **Pseudo-von Willebrand Disease** 有效，但目前**無任何臨床試驗或文獻**支持此方向，且機轉關聯性極弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血友病 B（先天性第九凝血因子缺乏症） |
| 預測新適應症 | Pseudo-von Willebrand Disease |
| TxGNN 預測分數 | 99.48% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Eftrenonacog alfa 是一種基因工程重組蛋白，由第九凝血因子（Factor IX）與免疫球蛋白 Fc 片段融合而成，可延長體內半衰期（相比傳統 FIX 製劑），減少患者的注射頻率。其核心作用為補充缺乏的 FIX，使內因性凝血途徑（intrinsic pathway）得以正常運作，達到次級止血（secondary hemostasis）的效果。

然而，Pseudo-von Willebrand Disease（假性 VWD）屬於**初級止血障礙**，其根本缺陷在於血小板 GPIbα 受體發生功能增益型突變，導致其與 von Willebrand Factor（VWF）異常高度結合，進而加速高分子量 VWF 多聚體的清除，並引發血小板消耗性減少。這與 Factor IX 所作用的凝血途徑**在止血生理學上屬不同分支**，無直接機轉連結。

TxGNN 的高預測分數極可能源自知識圖譜中「出血性疾病」節點群聚效應（graph clustering）——eftrenonacog alfa 與 pseudo-VWD 同屬「出血性疾病」大類，模型因此產生高相關性評分，而非反映真實的藥理機轉連結。標準治療為血小板輸注與重組 VWF，而非凝血因子補充療法。

> **評估額外預測項目**：本次分析同時評估另外兩個 TxGNN 預測——「血小板原發性釋放障礙（Primary Release Disorder of Platelets）」（分數 99.42%）與「Glanzmann 血小板無力症（Glanzmann Thrombasthenia）」（分數 99.27%），均屬初級止血障礙，與 Factor IX 的次級止血機轉存在相同的根本性不相容問題。其中 Glanzmann 血小板無力症雖有重組 FVIIa 的旁路治療先例，但該機轉需直接作用於血小板表面磷脂質，FIX 路徑之間接效率極低，且目前亦無任何臨床試驗或病例報告支持 eftrenonacog alfa 用於此症。

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
三項 TxGNN 預測（Pseudo-von Willebrand Disease、血小板原發性釋放障礙、Glanzmann 血小板無力症）均為 L5 等級——僅有模型預測，無任何臨床試驗或文獻支持；且機轉分析顯示 Factor IX（次級止血）與上述初級止血疾病之間缺乏直接藥理連結，預測高分可能為圖譜群聚偽信號。此外，本藥在香港尚未取得上市許可（0 張許可證），商業化路徑需從頭建立。

**若要推進需要：**

- 補充完整的作用機轉資料（MOA）以進行更嚴謹的機轉關聯性評估
- 取得原廠仿單，完成安全性初評（目前 Blocking 資料缺口尚未解除）
- 重新審視 TxGNN 預測是否因「出血性疾病」節點群聚而產生假陽性，建議優先評估其他分數相近但機轉更吻合的候選適應症
- 若仍考慮推進其中任一適應症，最低需先完成前臨床（in vitro / animal model）機轉驗證
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

