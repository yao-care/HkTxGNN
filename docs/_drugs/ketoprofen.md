---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 5
---

# Ketoprofen
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

# Ketoprofen：適應症資料缺失，TxGNN 預測罕見骨骼發育不良症候群

## 一句話總結

Ketoprofen 原始適應症與作用機轉資料在本次證據包中皆缺失（僅知其 DrugBank ID），且未在香港上市。
TxGNN 模型將其列為 **acromesomelic dysplasia, Hunter-Thompson type**（肢端中部骨骼發育不良，Hunter-Thompson 型）等 5 個罕見遺傳性疾病的高分候選，
但**零臨床試驗、零文獻支持**，且模型自身的機轉推理也判斷這極可能是知識圖譜稀疏節點造成的雜訊，而非真實訊號。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（DrugBank 未提供，香港未上市） |
| 預測新適應症 | acromesomelic dysplasia, Hunter-Thompson type（肢端中部骨骼發育不良症） |
| TxGNN 預測分數 | 99.98%（排名 644） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Ketoprofen 詳細的作用機轉（MOA）資料，原始適應症在本資料集中亦未記載。根據已知藥理分類，Ketoprofen 屬於非類固醇消炎止痛藥（NSAID），主要機轉為抑制 COX-1/COX-2 酶、減少前列腺素合成，發揮消炎、止痛與解熱作用。

TxGNN 將其列為 acromesomelic dysplasia、brachyolmia-amelogenesis imperfecta syndrome、myosclerosis、brachyolmia、colobomatous microphthalmia-rhizomelic dysplasia syndrome 等 5 個罕見遺傳性骨骼／發育疾病的高分候選（分數皆 >99.9%）。然而這些疾病的病理機轉（如 GDF5 基因異常、軟骨生成與生長板訊息傳導障礙、結構蛋白／礦化基因缺陷）與 NSAID 的抗發炎鎮痛機轉並無已知關聯。

證據包本身的 `repurposing_rationale` 也明確指出：這些高分很可能是知識圖譜中罕見疾病節點連結稀疏所導致的**模型雜訊**，而非真實生物學訊號，5 個候選皆呈現相同模式（高分、零試驗、零文獻）。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Ketoprofen 目前未在香港上市，無許可證登記。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA/香港仿單警語與禁忌症資料為 Blocking 等級缺口（DG001），在補齊前無法進行安全性初評（S1）。

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個預測候選皆為 L5（僅模型分數，零臨床試驗、零文獻），且證據包自身機轉分析已判斷高分可能為圖譜稀疏節點造成的雜訊，缺乏可信生物學假說。
- 原始適應症、MOA、香港上市與安全性資料全數缺失，無法建立最基本的比對基礎。

**若要推進需要：**
- 補齊 Ketoprofen 原始適應症與 MOA 資料（DrugBank API）
- 取得 TFDA／香港仿單的警語與禁忌症資料，解除 DG001 阻塞
- 若後續要重新評估，建議優先確認 TxGNN 對此類罕見疾病節點的預測是否存在系統性雜訊，而非逐一深入單一候選
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

