---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 5
---

# Gemcitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Gemcitabine：從原適應症（資料未提供）到女性乳癌

## 一句話總結

Gemcitabine（吉西他濱）是一種核苷類似物抗腫瘤藥，香港已有多張許可證，但本次資料未提供原適應症。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效。
目前**沒有臨床試驗和文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證的適應症欄位皆為空白） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Gemcitabine 屬於核苷類似物，一般認為它會抑制 DNA 合成和核糖核苷酸還原酶，對增生快速的腫瘤細胞有廣泛的抗腫瘤活性。

這種細胞毒性機轉在機轉上可能適用於乳癌。不過目前沒有針對乳癌的機轉分析，原適應症與新適應症的關聯性也尚未評估。

另外要注意：原適應症資料是空的，而 Gemcitabine 在一般認知中本來就有乳癌相關的仿單適應症。這個預測可能是仿單內既有適應症，而不是真正的老藥新用。這部分需要對照香港仿單確認，才能判斷它是否算老藥新用候選。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

共 18 張許可證，以下列出 5 張主要許可證。各許可證的劑型與核准適應症欄位皆無資料。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62671 | DBL GEMCITABINE INJECTION 1G/26.3ML | Pfizer Corporation Hong Kong Limited |
| HK-64297 | GEMITA POWDER FOR SOLUTION FOR INFUSION 200MG | Fresenius Kabi Hong Kong Limited |
| HK-62670 | DBL GEMCITABINE INJECTION 200MG/5.3ML | Pfizer Corporation Hong Kong Limited |
| HK-58235 | GITRABIN POWDER FOR SOL FOR INF 1G/VIAL | Teva Pharmaceutical Hong Kong Limited |
| HK-60082 | GEMCITABIN EBEWE CONC FOR SOLN FOR INF 200MG/20ML | Sandoz Hong Kong Limited |

## 細胞毒性

以下依藥物類別的一般知識判斷，並非來自本次 Evidence Pack 的 toxicity 資料，實際內容請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（核苷類似物／抗代謝藥） |
| 骨髓抑制風險 | 中至高（一般可見嗜中性白血球、血小板減少） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測分數很高，沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 原適應症和作用機轉資料缺漏，無法判斷乳癌是既有適應症還是真正的新用途。
- 香港仿單的警語與禁忌症資料也還沒取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，確認乳癌是否已是核准適應症，並補齊警語與禁忌症
- 補充 DrugBank 作用機轉（MOA）資料
- 檢索 Gemcitabine 用於乳癌的臨床試驗與文獻
- 若乳癌確認是既有適應症，改用其他預測適應症評估。其中結腸黏液腺癌有間接證據（L4），但相關性偏低。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

