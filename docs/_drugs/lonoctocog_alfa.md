---
layout: default
title: Lonoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 536
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Lonoctocog Alfa：預測新適應症為類血管性血友病 (pseudo-von Willebrand disease)（證據等級 L5）。原適應症：血友病（hemophilia）、女性帶因者的症狀性血友病"
monitor_inn: "LONOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome"]
---

# Lonoctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Lonoctocog alfa：從血友病到類血管性血友病（pseudo-von Willebrand disease）

## 一句話總結

Lonoctocog alfa 是重組單鏈第八因子（rVIII-SingleChain）製劑，原本用於血友病（包含女性帶因者出現症狀的血友病）。
TxGNN 模型預測它可能對**類血管性血友病 (pseudo-von Willebrand disease)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血友病（hemophilia）、女性帶因者的症狀性血友病 |
| 預測新適應症 | 類血管性血友病 (pseudo-von Willebrand disease) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Lonoctocog alfa 是重組單鏈第八因子，重鏈與輕鏈以共價鍵相連，對血管性血友病因子（VWF）具有高親和力，其補充第八因子的療效在血友病中已被確立。

類血管性血友病（血小板型 VWD）的成因是血小板 GPIbα 發生功能增強型缺陷，使其與 VWF 的結合增加，導致高分子量 VWF 多聚體流失而出血。病變在血小板端，第八因子濃度通常正常或僅輕度下降，因此補充第八因子在機轉上沒有明確依據。

TxGNN 的高分數（99.85%）較可能來自凝血與 VWF-FVIII 軸相關註解在知識圖譜上的鄰近性，而不是經過驗證的治療機轉。因此這個預測應視為待檢驗的假說，而非有力的再利用候選。

排名較後的其他預測（皆為 L5、建議 Hold）：

| 排名 | 預測疾病 | 分數 | 機轉評估 |
|------|---------|------|---------|
| 2 | 血小板原發性釋放障礙 (primary release disorder of platelets) | 99.84% | 缺陷在血小板顆粒釋放，第八因子無法矯正，僅有間接止血支持作用 |
| 3 | Glanzmann 血小板無力症 | 99.76% | 缺陷在 αIIbβ3 整合素，標準處置為血小板輸注、重組 FVIIa 與抗纖溶藥物 |
| 4 | Scott 症候群 | 99.44% | 缺陷在血小板磷脂絲胺酸暴露，補充第八因子無法恢復所缺的磷脂表面，機轉合理性弱 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66199 | AFSTYLA POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 1000 IU | 注射用粉劑及溶劑 | 資料未載明 |
| HK-66200 | AFSTYLA POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 1500 IU | 注射用粉劑及溶劑 | 資料未載明 |
| HK-66201 | AFSTYLA POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 250 IU | 注射用粉劑及溶劑 | 資料未載明 |
| HK-66202 | AFSTYLA POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 500 IU | 注射用粉劑及溶劑 | 資料未載明 |

四張許可證皆為單一成分、現行有效，持證商為 CSL Behring Asia Pacific Limited。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗或文獻佐證。
- 預測疾病的病變主要在血小板功能或 VWF 結合，補充第八因子缺乏明確機轉依據。

**若要推進需要：**
- 取得 Lonoctocog alfa 的作用機轉資料，並與預測疾病的病理機轉做比對。
- 取得香港仿單的警語與禁忌資料，完成安全性篩選。
- 以文獻回顧確認類血管性血友病患者是否有第八因子偏低的亞群，以及補充第八因子的實際經驗。
- 若上述回顧出現正面訊號，再設計小規模探索性研究；否則建議不投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

