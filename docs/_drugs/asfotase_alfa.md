---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase alfa：從原適應症資料缺漏到粒線體氧化磷酸化疾患（預測）

## 一句話總結

Asfotase alfa 是重組組織非特異性鹼性磷酸酶（TNSALP）融合蛋白，在香港以 STRENSIQ 上市，但 Evidence Pack 中缺少原適應症資料。
TxGNN 模型預測它可能對**核 DNA 異常所致粒線體氧化磷酸化疾患**有效（分數 99.95%）。
目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測，機轉上也找不到合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（香港許可證未提供適應症文字） |
| 預測新適應症 | 核 DNA 異常所致粒線體氧化磷酸化疾患 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺漏）。已知 Asfotase alfa 是 TNSALP 融合蛋白，作用是水解細胞外受質（例如無機焦磷酸）。

這個預測**在機轉上並不合理**。Asfotase alfa 不作用於粒線體氧化磷酸化（OXPHOS）路徑，也沒有已知的共同機轉。高分僅來自知識圖譜的關聯，而原適應症與 MOA 資料缺漏，無法用已知生物學驗證這個分數。

其他排名前 10 的預測（Steel 症候群、外分泌胰臟功能不全、Scheie 症候群、Hurler 症候群、溶小體儲積症伴骨骼病變、家族性 apoC-II 缺乏症、食道靜脈曲張（有／無出血）、胱胺酸症）同樣沒有試驗或文獻支持，機轉連結也不成立。多數只是「酵素」或「骨骼表現」這類圖譜上的鄰近關係。兩個食道靜脈曲張條目分數完全相同，應視為同一個微弱訊號，不是兩個獨立證據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67893 | STRENSIQ SOLUTION FOR INJECTION 80MG/0.8ML | 注射液 | 未提供 |
| HK-67891 | STRENSIQ SOLUTION FOR INJECTION 28MG/0.7ML | 注射液 | 未提供 |
| HK-67890 | STRENSIQ SOLUTION FOR INJECTION 18MG/0.45ML | 注射液 | 未提供 |
| HK-67892 | STRENSIQ SOLUTION FOR INJECTION 40MG/1ML | 注射液 | 未提供 |

以上 4 張許可證的持證商皆為 AstraZeneca Hong Kong Limited。

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢結果為無資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有任何臨床試驗或文獻，且與藥物作用機轉沒有可辨識的關聯。
- 原適應症、MOA 與仿單安全性資料都缺漏，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症
- 從 DrugBank 補齊作用機轉（MOA）
- 針對預測疾病做系統性文獻與試驗檢索，確認是否有任何生物學依據
- 若仍無機轉或實證支持，建議不再投入資源

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

