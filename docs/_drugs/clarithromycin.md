---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 5
---

# Clarithromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Clarithromycin：從細菌感染治療到多克隆高黏度症候群

## 一句話總結

Clarithromycin 是一種大環內酯類（macrolide）抗生素，廣泛用於呼吸道感染、幽門螺桿菌根除及非典型病原菌感染治療。
TxGNN 模型預測它可能對**多克隆高黏度症候群 (Polyclonal Hyperviscosity Syndrome)** 有效，
目前**無臨床試驗**、**無相關文獻**支持此方向，預測完全來自模型推算。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（本藥為大環內酯類抗生素，廣泛用於細菌性感染） |
| 預測新適應症 | 多克隆高黏度症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.35% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Clarithromycin 是大環內酯類抗生素，主要抗菌機轉為與細菌核糖體 50S 次單位結合，抑制蛋白質合成。此外，大環內酯類藥物具有獨立於抗菌活性之外的免疫調節效應，包括下調 IL-6、TNF-α 等促炎細胞激素，已在慢性呼吸道疾病中廣泛應用。

多克隆高黏度症候群由多種免疫球蛋白（IgG/IgM/IgA）大量分泌，導致血漿黏度異常上升。理論上，Clarithromycin 的免疫調節效應或許能間接抑制免疫球蛋白過量分泌，進而降低血漿黏度。

然而，此推測路徑的生物學合理性**極弱**，目前無任何臨床試驗、體外實驗或動物模型數據支持。TxGNN 高分數（0.993）可能反映知識圖譜中抗炎節點的遠端間接連結，而非真實適應症信號，不宜解讀為有意義的再利用候選。

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
- 多克隆高黏度症候群的預測缺乏任何臨床研究或實驗室數據支撐，僅為模型推算（L5 最低證據等級），機轉連結推測性極強。
- 本藥在香港市場目前無任何已登記許可證，監管基礎亦不足。

**若要推進需要：**
- 補充 MOA 詳細資料（查詢 DrugBank API）
- 補充安全性資訊（仿單警語與禁忌症）
- 評估大環內酯類是否有體外調節多克隆免疫球蛋白分泌的實驗證據
- 考慮以證據等級較高的排名 4（點狀上皮角結膜炎，L4 等級）優先作為下一步研究方向

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證方可應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

