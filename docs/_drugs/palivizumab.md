---
layout: default
title: Palivizumab
parent: 僅模型預測 (L5)
nav_order: 659
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Palivizumab：預測新適應症為良性舌部腫瘤 (benign neoplasm of tongue)（證據等級 L5）。原適應症：呼吸道融合病毒感染"
monitor_inn: "PALIVIZUMAB"
predicted_indications: ["benign neoplasm of tongue", "epiglottis neoplasm", "cervical neuroblastoma", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth"]
---

# Palivizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Palivizumab：從呼吸道融合病毒感染到良性舌部腫瘤（模型預測，證據極弱）

## 一句話總結

Palivizumab 是針對呼吸道融合病毒 (RSV) 的單株抗體，原本用於預防 RSV 感染。
TxGNN 模型預測它可能對**良性舌部腫瘤 (benign neoplasm of tongue)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬於模型運算的結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 呼吸道融合病毒感染（核准適應症文字於許可證資料中未提供，此處依知識圖譜的適應症資料） |
| 預測新適應症 | 良性舌部腫瘤 (benign neoplasm of tongue) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Palivizumab 是人源化單株抗體，會結合 RSV 的 F 蛋白並中和病毒。其療效限於 RSV 感染的預防。

然而，這個機轉**與舌部良性腫瘤沒有明顯關聯**。Palivizumab 的標靶是病毒蛋白，並非人體腫瘤抗原或細胞生長路徑。因此，我們找不到合理的生物學理由說明它可用於腫瘤。

TxGNN 分數雖然很高 (99.94%)，但其他預測適應症（會厭腫瘤、頸部神經母細胞瘤、下咽良性腫瘤、口底良性腫瘤）分數幾乎相同，且都屬於頭頸部或腫瘤相關名詞。這比較像是知識圖譜結構造成的系統性偏差，而非針對此藥的真實訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64445 | SYNAGIS SOLUTION FOR INJECTION 100MG/1ML | 未提供 | 未提供 |
| HK-64446 | SYNAGIS SOLUTION FOR INJECTION 50MG/0.5ML | 未提供 | 未提供 |

兩張許可證均為單一成分、現行有效，持證商為 ASTRAZENECA HONG KONG LIMITED。

---

## 安全性考量

安全性資訊請參考原廠仿單。

藥物交互作用查詢無相關紀錄。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗與文獻支持，證據等級為 L5。
- 藥物的作用標靶是病毒 F 蛋白，與腫瘤生物學沒有已知關聯，高分很可能是知識圖譜的結構假象。

**若要推進需要：**
- 補齊 Palivizumab 的作用機轉資料，並說明有無任何可能的腫瘤相關機制。
- 取得香港仿單的警語與禁忌資料，完成安全性篩選。
- 先以前臨床或機轉研究驗證是否存在真實訊號，再考慮任何臨床試驗。
- 不建議將其他四項預測（會厭腫瘤、頸部神經母細胞瘤、下咽良性腫瘤、口底良性腫瘤）列為優先方向，因為它們同樣缺乏支持證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

