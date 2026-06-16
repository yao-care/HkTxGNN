---
layout: default
title: Cefditoren
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Cefditoren
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

# Cefditoren：從細菌感染到骨關節炎易感性

## 一句話總結

Cefditoren 為第三代口服頭孢菌素類（Cephalosporin）抗生素，原本用於治療細菌性感染（呼吸道、皮膚軟組織等），目前香港無核准上市紀錄。
TxGNN 模型預測它可能對**骨關節炎易感性 (Osteoarthritis Susceptibility)** 有效，預測分數高達 **99.16%**；
然而，目前**無任何臨床試驗或文獻**支持，模型自身的推理也指出此預測最可能源自知識圖譜中骨骼肌肉疾病節點的**系統性群集偏差（Cluster Bias）**，而非真實生物學連結。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性感染（頭孢菌素類抗生素，香港無核准上市紀錄） |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.16% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**簡短回答：此預測高度疑似為模型偏差產物，生物學連結不成立。**

Cefditoren 是純殺菌性（bactericidal）口服頭孢菌素，作用機轉為 β-lactam 環與細菌青黴素結合蛋白（PBP）共價鍵結，抑制細菌細胞壁肽聚糖合成，屬宿主細胞外（extracellular）作用，對宿主骨關節炎相關病理路徑無任何已知干預能力。

骨關節炎易感性（Osteoarthritis Susceptibility）為多基因遺傳傾向性疾病，病理核心在於軟骨退化、基質金屬蛋白酶（MMP）異常活化及低度滑膜發炎。Cefditoren 對上述路徑均無文獻支持的效應，無軟骨保護、MMP 抑制或遺傳調控機轉。

更值得注意的是，本次前 10 名預測結果**全部集中於骨骼/肌肉系統疾病**（骨關節炎、類風濕性關節炎、brachyolmia、Hunter-Thompson 型短肢侏儒症、肌硬化症、染色體 16p 缺失等），預測分數高度集中在 0.982–0.992 區間，強烈提示 TxGNN 知識圖譜中骨骼肌肉疾病節點對 Cefditoren 所在節點產生了**系統性群集過預測（Cluster Bias）**，並非真實再利用訊號。

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
前 10 項預測均為 L5（僅模型預測），無任何臨床試驗或文獻支持；Cefditoren 為純殺菌性頭孢菌素，對骨關節炎等骨骼肌肉病理路徑無已知作用機轉，且預測結果高度集中於同一疾病 cluster，具典型 KG 圖譜拓撲偏差特徵，不構成再利用探索依據。

**若要推進需要：**
- 確認 MOA 完整資料（DrugBank API），排除是否有非抗菌的免疫調節或抗發炎副作用尚未被收錄
- 分析 Cefditoren 在 TxGNN 知識圖譜中的一階與二階鄰居節點，量化 cluster bias 程度
- 若仍考慮抗生素對骨關節炎的潛力探索，應改以 minocycline（已有 Phase 3 抗發炎機轉證據）等具免疫調節屬性的抗生素為優先候選，而非 Cefditoren
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

