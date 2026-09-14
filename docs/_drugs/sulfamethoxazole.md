---
layout: default
title: Sulfamethoxazole
parent: 中證據等級 (L3-L4)
nav_order: 711
evidence_level: L4
indication_count: 1
---

# Sulfamethoxazole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Sulfamethoxazole：從抗菌治療到急性傳染性結膜炎

## 一句話總結

Sulfamethoxazole 是磺胺類抗菌藥物，作用機轉為抑制細菌葉酸合成，但本評估缺乏完整的原適應症與上市資料。
TxGNN 模型預測它可能對**急性傳染性結膜炎 (Acute Contagious Conjunctivitis)** 有效，
目前僅有 **1 篇文獻**支持此方向，且**無直接臨床試驗**驗證，證據等級為 L4。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（drug.original_indications 為空、無許可證可推算） |
| 預測新適應症 | 急性傳染性結膜炎 (Acute Contagious Conjunctivitis) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Sulfamethoxazole 為磺胺類抗菌藥，機轉為抑制二氫蝶酸合成酶（dihydropteroate synthase），阻斷細菌葉酸合成路徑，屬廣譜抗菌藥物。

急性傳染性結膜炎（細菌性結膜炎）本質上是感染性疾病，理論上對磺胺類敏感菌株具治療潛力。同類磺胺藥物（如 sulfacetamide）已有局部眼科使用先例，這使得機轉關聯具備一定的生物合理性。

然而，本藥的原始適應症資料、香港上市狀態與劑型（全身性 vs 局部眼用）均缺失，目前無法確認 sulfamethoxazole 本身是否適合、或以何種劑型用於眼科感染治療。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohort/Surveillance | Medical hypothesis, discovery & innovation ophthalmology journal | 針對希臘西部兒童急性細菌性結膜炎進行回溯性病原菌與抗生素敏感性分析（非 sulfamethoxazole 直接介入性研究） |

## 香港上市資訊

目前未在香港上市，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 注意：TFDA 仿單警語/禁忌屬 **Blocking** 等級資料缺口（DG001），在補齊前無法進入 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 1 篇非介入性監測型文獻支持，無任何臨床試驗直接驗證 sulfamethoxazole 用於急性傳染性結膜炎，證據等級為 L4（前臨床/機轉層級）。
- 香港未上市、安全性仿單資料缺失（Blocking），且原適應症與 MOA 官方資料皆缺失，尚不具備進入下一階段安全性初評（S1）的條件。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking）
- 取得 DrugBank 完整 MOA 資料以確認機轉關聯性（DG002）
- 確認可用劑型與給藥途徑（全身性 vs 局部眼用），評估是否適合眼科感染
- 尋找針對 sulfamethoxazole（或 sulfamethoxazole 複方）治療結膜炎的直接介入性臨床研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

