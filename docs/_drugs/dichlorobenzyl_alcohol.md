---
layout: default
title: Dichlorobenzyl Alcohol
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 2
---

# Dichlorobenzyl Alcohol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Dichlorobenzyl Alcohol：從喉嚨不適到支氣管炎

## 一句話總結

Dichlorobenzyl Alcohol（二氯苄醇）是一種常見於喉嚨含片的溫和局部抗菌劑。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，
但目前僅有 **0 個臨床試驗**和 **1 篇間接相關文獻**，證據極為薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證的適應症欄位皆為空白） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.21% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dichlorobenzyl Alcohol 是喉嚨含片的成分，
一般背景知識認為它具有溫和的抗菌、抗病毒及類局部麻醉作用（此為輸入資料以外的背景說明）。

這些特性可能緩解上呼吸道（喉嚨）的刺激。但支氣管炎屬於下呼吸道疾病，
含片在下呼吸道幾乎沒有局部暴露，因此無法僅憑現有資料確認機轉上適用於支氣管炎。
0.992 的 TxGNN 分數僅是計算模型的預測，屬於提出假說的訊號。

另外，TxGNN 也預測它可能與**偏頭痛 (Migraine Disorder)** 有關（分數 99.02%），
但目前沒有任何臨床試驗或文獻，也沒有可支持的機轉連結，僅視為假說。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1036939](https://pubmed.ncbi.nlm.nih.gov/1036939/) | 1976 | 個案／觀察性（依標題推斷） | Arzneimittel-Forschung | 25 位慢性支氣管炎患者口服 clenbuterol（一種含二氯苄醇結構的 β2 受體促效劑）後，血清肌酸激酶活性升高 |

**注意：** 此文獻研究的是 clenbuterol，並非 Dichlorobenzyl Alcohol 本身，僅因化學名稱中含有 dichlorobenzyl alcohol 字樣而被檢索到，**不能視為支持該預測的證據**。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67542 | DIFFLAM ANTISEPTIC LOZENGES BLACKCURRANT FLAVOUR | 未提供 | 未提供 |
| HK-54273 | THROATSIL LOZENGE - HONEY & LEMON | 未提供 | 未提供 |
| HK-59174 | THROATSIL LOZENGE - PRUNE | 未提供 | 未提供 |
| HK-54274 | THROATSIL LOZENGE - SALA | 未提供 | 未提供 |
| HK-67433 | BETACARE SORE THROAT ORANGE LOZENGES 0.6MG/1.2MG | 未提供 | 未提供 |

共 20 張許可證，以上僅列出 5 張。從品名可知，這些產品皆為喉嚨含片。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
證據等級僅為 L5，只有模型預測，沒有任何直接支持的臨床試驗或文獻。
支氣管炎位於下呼吸道，含片的給藥途徑與作用部位也不匹配；偏頭痛則完全沒有機轉依據。

**若要推進需要：**
- 補齊作用機轉（MOA）資料（可查詢 DrugBank）
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症
- 評估給藥途徑是否能讓藥物到達下呼吸道
- 搜尋 Dichlorobenzyl Alcohol 本身（而非其他化合物）在支氣管炎的臨床或前臨床研究

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

