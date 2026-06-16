---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 4
---

# Darunavir
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

# Darunavir：從 HIV 感染到猿猴免疫缺乏病毒感染

## 一句話總結

Darunavir 是第二代 HIV 蛋白酶抑制劑，全球廣泛用於 HIV-1 感染的治療。
TxGNN 模型預測它可能對**猿猴免疫缺乏病毒感染 (Simian Immunodeficiency Virus Infection)** 有效，
目前有 **0 個臨床試驗**和 **4 篇文獻**（均為非人靈長類動物研究）支持這個方向，尚無人類臨床試驗登記。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（人類免疫缺乏病毒感染）|
| 預測新適應症 | 猿猴免疫缺乏病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4（非人靈長類動物研究）|
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Darunavir 是第二代非肽類 HIV-1 蛋白酶抑制劑，透過與病毒蛋白酶活性位點形成緊密的氫鍵結合，阻斷病毒多蛋白前體的切割，從而抑制新病毒顆粒的成熟。目前缺乏詳細的 MOA 文件，但其作用機轉在 HIV 領域已被充分研究。

猿猴免疫缺乏病毒（SIV）與 HIV-1 具有高度同源性——兩者均屬慢病毒屬（Lentivirus），使用結構相似的天冬氨酸蛋白酶（aspartate protease）進行病毒複製。靶向 HIV-1 蛋白酶的 Darunavir，理論上對 SIV 蛋白酶同樣具有抑制活性，這使 TxGNN 的預測在機轉層面有一定合理性。

然而，需特別注意的是：SIV 感染本質上是非人靈長類動物（NHP）疾病，現有文獻將 Darunavir 納入多藥物聯合抗病毒方案（cART）的目的，是以 SIV/恒河猴模型作為 HIV 藥物的臨床前驗證平台，而非開發 Darunavir 作為「治療 SIV 感染」的新人類適應症。此預測的臨床轉化意義偏向「模型工具應用」，而非傳統意義上的老藥新用開發方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

> SIV 感染為非人靈長類動物疾病，不適用人類臨床試驗框架，因此此適應症本質上不會有 ClinicalTrials.gov 登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | 動物研究（NHP）| AIDS Research and Human Retroviruses | 評估兩種新型 cART 方案（含 Darunavir）在 SIVmac239 感染恒河猴中的病毒抑制效果，建立可靠的 NHP 模型 |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | 動物研究（NHP）| PLoS One | 以含 Darunavir 的 cART 方案聯合 HDAC 抑制劑 SAHA，研究中國恒河猴中 SIV 病毒庫的持續性與清除策略 |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | 動物研究（NHP）| PLoS Pathogens | 高強度 ART（含 Darunavir）在廣範圍病毒量（10³–10⁷ copies/mL）SIVmac251 感染恒河猴中達成長期病毒抑制，並顯著縮小病毒庫 |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | 動物研究（NHP）| AIDS | 金化合物 auranofin 聯合含 Darunavir 的 cART 方案，評估 SIV 病毒庫的 CD4 T 細胞持續性；停藥後仍可部分維持病毒抑制 |

> ⚠️ **重要提示**：所有文獻均為 Tier 3 非人靈長類動物研究，Darunavir 在這些研究中均作為 **cART 方案的組成成分之一**使用，並非專門研究其對 SIV 蛋白酶的直接專一性抑制活性。現有文獻支持的是「Darunavir 是 SIV/NHP 模型中有效的 cART 組成藥物」，而非「Darunavir 是 SIV 感染的新候選治療藥物」。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測的機轉合理性有一定基礎（SIV 與 HIV-1 蛋白酶高度同源），Darunavir 作為 SIV/NHP 模型中標準 cART 成分的使用已有文獻佐證。然而，SIV 感染為非人靈長類動物疾病，此「適應症」本質上是 HIV 藥物開發管線中的臨床前動物模型工具，而非可直接進入人類開發的再利用機會。其他三個預測適應症（貓後天免疫缺乏症候群、罕見神經發育障礙、家族性高脂血症）亦均建議 Hold——分別因疾病映射錯誤、無機轉支持、及存在反向機轉警示（Darunavir/ritonavir 本身可能誘發血脂異常）。

**若要推進需要：**
- **明確研究目的**：若目標是 NHP 模型優化，現有 cART 方案已具備充分依據，可直接作為工具藥物應用，無需另立「再利用」研究計畫
- **補充 MOA 詳細文件**（目前為 Data Gap）：確認 Darunavir 對 SIV 蛋白酶的直接抑制活性數據（IC₅₀、結晶結構等）
- **重新定向評估**：若目標為真正的老藥新用開發，建議以 Darunavir 對 HIV 以外的人類疾病（如 SARS-CoV-2 蛋白酶抑制、相關機轉疾病）為優先評估方向
- **補充香港上市資訊**：目前無許可登記，若需在港使用，需釐清引進或臨床試驗申請路徑
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

