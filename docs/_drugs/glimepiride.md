---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 5
---

# Glimepiride
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

# Glimepiride：從第二型糖尿病到僵人症候群

## 一句話總結

Glimepiride 是第三代磺醯脲類口服降血糖藥，國際上廣泛用於第二型糖尿病的血糖控制，但目前在香港尚無上市許可。TxGNN 模型預測它對 **僵人症候群 (Classic Stiff Person Syndrome)** 等 5 個罕見疾病可能有效，然而目前**無任何臨床試驗或文獻**支持，所有預測均處於最早期探索階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第二型糖尿病（國際通用；香港無上市許可） |
| 預測新適應症 | 僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 待補）。根據已知藥理知識，Glimepiride 是磺醯脲類藥物，主要透過阻斷胰臟 β 細胞的 ATP 感應性鉀通道（KATP 通道，SUR1/ABCC8 + Kir6.2/KCNJ11 複合體）促進胰島素分泌。此外，它具有輕度 PPAR-γ 部分促效活性，理論上具免疫調節潛力（抑制 NF-κB、促進調節性 T 細胞 Treg）。

僵人症候群（SPS）是以抗 GAD65 抗體為標記的自體免疫疾病，導致脊髓 GABA 能中間神經元功能喪失，引發持續性肌肉僵硬與痙攣。理論上，Glimepiride 的 PPAR-γ 部分活性可能緩解 SPS 的自體免疫驅力；KATP 通道亦廣泛表現於 GABA 能神經元，磺醯脲類在理論上可調節神經元興奮性。

然而，上述連結**高度間接且具推測性**。GAD65 抗體介導路徑與 KATP/PPAR-γ 之間的直接因果關係尚未建立，目前無任何臨床或動物模型證據支持 Glimepiride 用於 SPS。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Glimepiride 目前在香港**未上市**，無任何藥品許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他預測適應症

TxGNN 模型共預測 5 個潛在新適應症，完整摘要如下：

| 排名 | 疾病名稱 | TxGNN 分數 | 機轉連結強度 | 建議 |
|------|---------|-----------|------------|------|
| 1 | Classic Stiff Person Syndrome（僵人症候群） | 99.75% | 弱（間接推測） | Hold |
| 2 | Focal Stiff Limb Syndrome（局部僵肢症候群） | 99.75% | 弱（同 SPS，症狀更局限） | Hold |
| 3 | Opsismodysplasia（骨形成遲滯症） | 99.74% | 中等（PI3K/Akt 路徑交集） | Research Question |
| 4 | Thiamine-Responsive Dysfunction Syndrome（硫胺素反應性功能障礙症候群） | 99.73% | **強**（KATP 直接靶點，因果邏輯清晰） | Research Question |
| 5 | Drug-Induced Localized Lipodystrophy（藥物誘導局部脂肪萎縮症） | 99.62% | 弱（PPAR-γ 方向不確定且可能有害） | Hold |

> **⚑ 值得優先關注**：排名第 4 的**硫胺素反應性功能障礙症候群（TRMA，Rogers Syndrome）**具有本組最強的機轉連結。TRMA 糖尿病的核心病理為 SLC19A2 基因突變 → 硫胺素缺乏 → β 細胞 ATP 合成障礙 → **KATP 通道持續開放** → 胰島素分泌不足；而 Glimepiride 的主要靶點恰好是 SUR1/Kir6.2（KATP 通道阻斷劑），機轉具備直接因果邏輯，類似一般 T2DM 使用情境但病因不同。散在個案文獻（磺醯脲類用於 TRMA 糖尿病）存在但未被本次資料集收錄，應優先補查。

---

## 結論與下一步

**決策：Hold**

**理由：**
全數 5 個預測適應症均缺乏臨床試驗與文獻支持（L5 證據等級），機轉連結多為間接推測，安全性資料缺失，且 Glimepiride 在香港尚無上市許可，基礎監管條件未備。

**若要推進需要：**
- **補充安全性資料**：下載原廠仿單，取得警語、禁忌症、DDI 等完整資訊（Data Gap DG001）
- **補充 MOA 資料**：透過 DrugBank API 查詢 DB00222 完整作用機轉（Data Gap DG002）
- **優先搜尋 TRMA 個案文獻**：以 "sulfonylurea TRMA" / "glimepiride Rogers syndrome" 為關鍵字補充 PubMed 查詢
- **評估香港上市可行性**：確認是否需申請新許可證或借助其他監管路徑
- **若 TRMA 文獻有支持**：評估 Slc19a2 敲除鼠模型中 glimepiride 的 β 細胞保護效果作為下一步前臨床依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

