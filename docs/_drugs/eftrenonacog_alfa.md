---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Eftrenonacog Alfa：預測新適應症為類血管性血友病 (pseudo-von Willebrand disease)（證據等級 L5）。原適應症：血友病（hemophilia）、女性帶因者的症狀性血友病"
monitor_inn: "EFTRENONACOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia"]
---

# Eftrenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Eftrenonacog alfa：從血友病到類血管性血友病（pseudo-von Willebrand disease）

## 一句話總結

Eftrenonacog alfa 是重組第九凝血因子 Fc 融合蛋白，原本用於血友病（hemophilia）的治療。
TxGNN 模型預測它可能對**類血管性血友病 (pseudo-von Willebrand disease)** 有效，
但目前**沒有臨床試驗和文獻**支持這個方向，僅屬於模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血友病（hemophilia）、女性帶因者的症狀性血友病 |
| 預測新適應症 | 類血管性血友病 (pseudo-von Willebrand disease) |
| TxGNN 預測分數 | 99.48% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Eftrenonacog alfa 是重組第九凝血因子 Fc 融合蛋白（rFIXFc），可補充 B 型血友病患者缺乏的第九凝血因子活性，其在血友病中的療效機轉已相當明確。

然而，類血管性血友病（血小板型 von Willebrand 病）的病因是血小板 GPIbα 的功能獲得性變異，使其與 von Willebrand 因子（VWF）的結合增加，造成高分子量 VWF 多聚體流失及血小板低下。缺陷在於血小板與 VWF 的軸線，而非第九因子缺乏，因此**機轉上沒有明顯的直接關聯**。

TxGNN 的高分數（99.48%）僅是計算預測，可能源自知識圖譜中「出血性疾病」的共通網路關係，而非生物學上的合理性。此預測應視為待驗證的假說，而非有力的再利用候選。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67048 | ALPROLIX POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 500IU | 注射用粉末及溶劑 | 未提供 |
| HK-67045 | ALPROLIX POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 1000IU | 注射用粉末及溶劑 | 未提供 |
| HK-67046 | ALPROLIX POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 2000IU | 注射用粉末及溶劑 | 未提供 |
| HK-67047 | ALPROLIX POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 3000IU | 注射用粉末及溶劑 | 未提供 |

以上 4 張許可證均為單一成分、現行有效，持證商為 SANOFI HONG KONG LIMITED。

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症

另有兩項預測，同樣僅有模型分數而無任何臨床試驗或文獻支持，證據等級皆為 L5：

| 排名 | 預測適應症 | TxGNN 分數 | 機轉評估 |
|------|-----------|-----------|---------|
| 2 | 原發性血小板釋放障礙 (primary release disorder of platelets) | 99.42% | 缺陷在血小板顆粒內容物釋放或訊號傳遞，第九因子替代作用於內源性凝血路徑，預期無法矯正血小板功能缺陷 |
| 3 | Glanzmann 血小板無力症 (Glanzmann thrombasthenia) | 99.28% | 缺陷在血小板整合素 αIIbβ3 (GPIIb/IIIa)，與第九因子無關；標準處置為血小板輸注、抗纖溶藥物及重組第七因子 |

## 結論與下一步

**決策：Hold**

**理由：**
- 三項預測適應症皆屬血小板或 VWF 功能缺陷，與第九因子缺乏的機轉並無直接關聯，且完全沒有臨床試驗或文獻佐證，僅有模型分數（證據等級 L5）。
- 作用機轉與安全性資料皆有缺口，目前不足以支持推進。

**若要推進需要：**
- 補充詳細的作用機轉資料，並釐清第九因子替代與血小板/VWF 缺陷之間是否有任何生物學連結
- 取得香港衛生署的仿單（警語、禁忌症），完成安全性篩選
- 進行系統性文獻回顧，確認是否存在個案報告或前臨床證據
- 與血液科專家討論，評估這些預測是否有臨床意義，或僅為知識圖譜的雜訊
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

