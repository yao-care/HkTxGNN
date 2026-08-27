---
layout: default
title: Icosapent Ethyl
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 1
---

# Icosapent Ethyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the evidence pack provided, here is the report:

---

# ICOSAPENT ETHYL：原適應症資料缺失，預測新適應症為血紅蛋白病 (Hemoglobinopathy)

## 一句話總結

ICOSAPENT ETHYL（DrugBank: DB08887）目前在台灣**未上市**，且本地缺乏原適應症與作用機轉（MOA）資料。
TxGNN 模型預測它可能對**血紅蛋白病 (Hemoglobinopathy)**（如鐮刀型細胞病相關疾病）有效，
但目前**無相關臨床試驗**登記，僅有 **1 篇動物模型文獻**間接支持，且該文獻測試的其實是同類化合物而非本藥物本身，證據非常初步。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（無核准適應症紀錄） |
| 預測新適應症 | 血紅蛋白病 (Hemoglobinopathy) |
| TxGNN 預測分數 | 99.09% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 ICOSAPENT ETHYL 詳細的作用機轉（MOA）資料，本地也沒有核准適應症紀錄，因此無法從已知療效直接推論其藥理關聯性。

唯一的佐證文獻研究的其實是合成 ω-3 脂肪酸類似物 **Epeleuton**（並非 ICOSAPENT ETHYL 本身），該研究在小鼠模型中顯示 Epeleuton 可降低與血紅蛋白病（如鐮刀型細胞病）相關的缺血再灌流 (hypoxia/reperfusion) 壓力。理論上，EPA 類化合物具有抗發炎、抗氧化、改善微循環的作用，可能對血管阻塞性血紅蛋白病帶來潛在助益。

然而，這個機轉推論屬於**跨藥物外推**（以類似化合物的結果推論本藥），並非直接針對 ICOSAPENT ETHYL 進行的實驗證據。加上原藥物的 MOA 與原適應症皆為資料缺口，這個機轉關聯目前僅屬理論性、間接推測，尚不足以構成藥理學上的確定連結。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38105727](https://pubmed.ncbi.nlm.nih.gov/38105727/) | 2024 | 臨床前研究（動物模型） | Haematologica | 合成 ω-3 脂肪酸類似物 Epeleuton 在鐮刀型細胞病小鼠模型中，可降低缺血再灌流相關的發炎性血管病變壓力（注意：測試藥物為 Epeleuton，非 ICOSAPENT ETHYL 本身） |

## 香港上市資訊

ICOSAPENT ETHYL 目前尚未於台灣上市，許可證數為 0，無許可證資料可列。

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：目前無法取得 TFDA 仿單警語與禁忌資料（屬 Blocking 等級資料缺口），在補齊前無法進行安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5——沒有任何臨床試驗，僅有 1 篇動物模型文獻，且該文獻測試的是類似化合物而非 ICOSAPENT ETHYL 本身，機轉關聯屬間接推測。
- 藥物在台灣未上市，且原適應症、作用機轉、安全性資料皆缺失，目前不具備進入下一階段安全性初評（S1）的基礎條件。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌資料（下載仿單 PDF 並解析，屬 Blocking 缺口）
- 查詢 DrugBank 取得 ICOSAPENT ETHYL 的作用機轉（MOA）資料
- 尋找針對 ICOSAPENT ETHYL 本身（而非類似物）於血紅蛋白病相關動物或臨床前研究的直接證據
- 若後續考慮發展，需評估台灣上市與適應症申請路徑
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

