---
layout: default
title: Bictegravir
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 3
---

# Bictegravir
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

# Bictegravir：從 HIV-1 感染到猴免疫缺陷病毒感染

## 一句話總結

Bictegravir 是第二代整合酶鏈轉移抑制劑（INSTI），原本核准用於 HIV-1 感染的抗病毒治療。
TxGNN 模型預測它可能對**猴免疫缺陷病毒感染（Simian Immunodeficiency Virus Infection, SIV）** 有效，
目前有 **3 篇前臨床/基礎文獻**支持此方向，但無任何臨床試驗登記。

> ⚠️ **特別說明**：SIV 感染為**非人靈長類動物疾病**，在藥物研發中主要作為 HIV 前臨床模型使用，並非直接的人類治療標靶。此預測的臨床轉化路徑需特別謹慎評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（抗病毒治療） |
| 預測新適應症 | 猴免疫缺陷病毒感染（Simian Immunodeficiency Virus Infection） |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L4（前臨床研究/基礎研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Bictegravir 的作用機轉為**整合酶鏈轉移抑制（INSTI）**：透過與整合酶催化核心的保守 DDE 基序（Asp-Asp-Glu motif）緊密結合，阻斷病毒 cDNA 整合至宿主細胞基因組，從而阻斷病毒複製週期。相較於第一代 INSTI（Raltegravir、Elvitegravir），Bictegravir 具有更高的耐藥遺傳屏障。

HIV-1 與 SIV 均屬慢病毒科（Lentivirus），兩者的整合酶在 intasome 結構與催化口袋的胺基酸序列相似度超過 80%。PMID:28923862 直接證明 Bictegravir 對整合酶抑制劑耐藥的 SIVmac239 具有抗病毒活性，機轉連結具有紮實的結構生物學基礎。

然而，**SIV 感染本質上是動物模型工具**，而非人類臨床治療標靶。TxGNN 高分反映的是 Bictegravir 抑制 SIV 整合酶的生物活性，其臨床意義在於支持 Bictegravir 作為 HIV 感染前臨床研究模型的工具，而非真正意義上的「老藥新用」適應症擴展。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | 體外/前臨床研究 | Antimicrobial Agents and Chemotherapy | 直接證明 Bictegravir 對 INSTI 耐藥 SIVmac239 及 HIV-1 臨床分離株均具抗病毒活性 |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | 結構生物學綜述 | The FEBS Journal | 解析 HIV/SIV intasome 結構，闡明 Bictegravir 等第二代 INSTI 的結合模式與耐藥逃逸機轉 |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | 動物模型研究（人源化小鼠） | Frontiers in Immunology | 建立可同時測試 SIV 和 HIV 抗病毒策略的雙用途人源化小鼠模型，評估新型 ARV 方案 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
雖然 Bictegravir 抑制 SIV 整合酶的機轉連結清晰，並有前臨床文獻佐證，但 SIV 感染屬於非人靈長類動物疾病，本質上是 HIV 研究的動物模型工具而非人類治療標靶，無法直接形成人類臨床適應症擴展的業務或監管路徑。此外，Bictegravir 在台灣目前尚未取得任何上市許可，安全性及作用機轉資料亦存在資料缺口。

**若要推進需要：**
- 重新定義臨床轉化問題：是否意圖用於「HIV 感染的前臨床模型研究工具」，而非真正的人類適應症擴展
- 補充 Bictegravir 完整作用機轉資料（DrugBank MOA）
- 取得台灣/香港上市許可及仿單安全性資料（警語、禁忌、DDI）
- 若目標為人類適應症，建議重新篩選 TxGNN 預測清單中的**人類疾病**適應症（Rank 3 以後的預測需進一步評估）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

