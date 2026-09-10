---
layout: default
title: Racecadotril
parent: 僅模型預測 (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
---

# Racecadotril
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

# Racecadotril：從急性腹瀉到高澱粉酶血症

## 一句話總結

Racecadotril 是腦啡肽酶（enkephalinase/NEP）抑制劑，原用於治療急性腹瀉。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，
但目前**無任何臨床試驗或文獻支持**，且該藥物在香港**未上市**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性腹瀉（依機轉描述推論，本次資料未提供正式核准適應症） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 97.72% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。根據 TxGNN 評估附帶的機轉關聯分析，Racecadotril 是腦啡肽酶抑制劑，作用於腸道，抑制內生性鴉片肽降解以減少腸液分泌，用於急性腹瀉治療。

該分析明確指出：**高澱粉酶血症涉及胰臟外分泌/胰澱粉酶代謝調控，與 Racecadotril 的腸道抗分泌機轉並無已知生物學關聯**。此預測純粹來自 TxGNN 知識圖譜的 embedding 相似性，缺乏機轉層面的合理性支持。

同一批預測中的其餘 9 個候選適應症（如先天性白蛋白缺乏症、血型不合、敗血性鼠疫、急性膀胱炎等）也都被系統性標註為「無已知機轉關聯」，其中敗血性鼠疫的候選更被特別提示：若誤用可能延誤抗生素治療，存在安全疑慮。整體而言，這批預測應視為探索性訊號，而非具生物學基礎的候選。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Racecadotril 目前在香港**未上市**，查無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA/香港仿單警語與禁忌資料為本次資料收集之關鍵缺口（Blocking），在此缺口補齊前無法進行安全性初評（S1 階段）。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 10 個 TxGNN 預測適應症均為 L5 等級（僅模型預測），且機轉分析明確指出與原藥理作用無生物學關聯，其中部分候選（如敗血性鼠疫）若誤用甚至有延誤正規治療的風險。
- 藥物尚未在香港上市，仿單警語與禁忌資料缺失（Blocking 等級缺口），無法進行安全性初評。

**若要推進需要：**
- 補齊 DrugBank 完整 MOA 資料，釐清是否有其他未被本次查詢涵蓋的機轉路徑
- 取得正式仿單警語/禁忌資料以解除 Blocking 缺口
- 針對排名較前但機轉不明的適應症（高澱粉酶血症），另行檢索胰臟外分泌相關文獻以驗證是否存在間接關聯
- 在無實證支持前，不建議投入後續開發資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

