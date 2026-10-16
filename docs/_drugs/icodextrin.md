---
layout: default
title: Icodextrin
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Icodextrin：預測新適應症為腸躁症 (Irritable Bowel Syndrome)（證據等級 L5）。原適應症：香港許可證未載明適應症文字（依其劑型與用途，為腹膜透析液）"
monitor_inn: "Icodextrin"
predicted_indications: ["irritable bowel syndrome", "non-syndromic esophageal malformation", "C1 inhibitor deficiency", "potassium deficiency disease", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "esophageal disease", "familial visceral myopathy", "renal tubular acidosis", "vitamin deficiency disorder"]
---

# Icodextrin
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

# Icodextrin：從腹膜透析到大腸急躁症（腸躁症）

## 一句話總結

Icodextrin 是一種高分子量葡萄糖聚合物，在腹膜透析中作為滲透劑使用。
TxGNN 模型預測它可能對**腸躁症 (Irritable Bowel Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症文字（依其劑型與用途，為腹膜透析液） |
| 預測新適應症 | 腸躁症 (Irritable Bowel Syndrome) |
| TxGNN 預測分數 | 98.53% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Icodextrin 是腹膜透析液中的滲透劑成分，
透過高分子量葡萄糖聚合物產生滲透超濾作用，且在腸道中吸收極少。

從現有資料看，無法建立 Icodextrin 與腸躁症病理機轉（內臟高敏感、腸道動力異常、腸道菌群）之間的合理路徑。
0.985 的 TxGNN 分數僅代表知識圖譜上的關聯預測，並非獨立的生物學或臨床證據。

因此，這個預測目前只能視為待驗證的假說，不宜視為有機轉支持的再利用候選。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46627 | EXTRANEAL SOLN 7.5% | 未載明 | 未載明（廠商：VANTIVE HEALTHCARE LIMITED） |

## 其他 TxGNN 預測的適應症（供參考）

以下預測同樣僅有模型分數，無臨床試驗或文獻，且均未發現機轉關聯，建議決策皆為 Hold：

| 排名 | 預測適應症 | TxGNN 分數 | 備註 |
|------|-----------|-----------|------|
| 2 | 非症候群性食道畸形 | 97.41% | 先天結構異常，滲透性透析劑不預期有效 |
| 3 | C1 酯酶抑制劑缺乏症 | 97.29% | 涉及補體／緩激肽路徑，與 Icodextrin 無關 |
| 4 | 缺鉀症 | 97.19% | Icodextrin 非鉀調節藥物 |
| 5 | 絲胺酸蛋白酶抑制劑病（毒性聚合） | 97.06% | 無蛋白摺疊相關作用 |
| 6 | 遺傳性血管性水腫（C1Inh 缺乏） | 96.81% | 分數可能反映與第 3 項的圖譜重疊 |
| 7 | 食道疾病 | 96.77% | 類別過於廣泛，無合理標的 |
| 8 | 家族性內臟肌病 | 96.34% | 無已知對內臟平滑肌的作用 |
| 9 | 腎小管酸中毒 | 95.81% | 代謝物累積反而可能影響酸鹼平衡，關聯偏向不良反應 |
| 10 | 維生素缺乏症 | 95.78% | Icodextrin 不補充或調節維生素 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有 TxGNN 模型預測（證據等級 L5），沒有任何臨床試驗或文獻，且無法建立合理的機轉關聯。
- Icodextrin 在腸道吸收極少，與腸躁症的病理生理缺乏可辨識的連結，目前不建議投入資源。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並評估對腸躁症病理機轉是否有任何合理路徑
- 取得香港衛生署許可證的仿單，補全核准適應症、警語與禁忌症
- 進行系統性文獻與臨床試驗檢索，確認是否存在任何支持性證據
- 若仍要探索，先以前臨床或機轉研究驗證假說，再考慮臨床試驗設計
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

