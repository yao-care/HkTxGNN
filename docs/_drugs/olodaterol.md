---
layout: default
title: Olodaterol
parent: 中證據等級 (L3-L4)
nav_order: 629
evidence_level: L3
indication_count: 2
---

# Olodaterol
{: .fs-9 }

證據等級: **L3** | 預測適應症: **2** 個
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

# Olodaterol：從 COPD 到支氣管炎

## 一句話總結

Olodaterol 是長效 β2 受體促效劑（LABA），依試驗與文獻推斷，原本用於慢性阻塞性肺病（COPD）的維持治療。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，目前有 **3 個臨床試驗**和 **2 篇文獻**與此方向相關。
這些試驗與文獻全是 COPD 族群的觀察性研究、上市後監測、指引或回顧，沒有任何研究直接以支氣管炎為評估終點。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性阻塞性肺病（COPD）（由試驗與文獻推得，許可證資料未載明） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Olodaterol 是長效 β2 受體促效劑，透過 cAMP 路徑放鬆呼吸道平滑肌，產生持續的支氣管擴張效果。

慢性支氣管炎是 COPD 的表型之一，所以 COPD 的支氣管擴張療效在機轉上有可能延伸到慢性支氣管炎。日本的上市後監測（NCT02850978）就把慢性支氣管炎與肺氣腫都納入 COPD 族群。

要注意的是，99.84% 的高分很可能只是反映 COPD 與支氣管炎在知識圖譜中的高度重疊，並不是獨立的療效證據。目前沒有任何證據支持急性支氣管炎。若要推進，必須先把適應症明確定義為「COPD 內的慢性支氣管炎」。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | 完成 | 1,335 | 日本 Tiotropium+Olodaterol 複方長期上市後監測，評估 COPD（含慢性支氣管炎、肺氣腫）的真實世界安全性與療效 |
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | 完成 | 11,316 | 比較 Tiotropium/Olodaterol 與 FF/UMEC/VI 起始治療後的 COPD 醫療資源使用、費用與臨床結果（觀察性研究） |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | 完成 | 22,155 | Aclidinium 藥物使用安全性研究，屬不同藥物，僅提供 COPD 族群的間接背景 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | Am J Health Syst Pharm | 回顧 Olodaterol（每日一次的 LABA）的藥理、藥動、療效與安全性資料，對象為 COPD |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | 芬蘭穩定期 COPD 的診斷與藥物治療指引，主要供基層醫療使用 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63776 | STRIVERDI RESPIMAT SOLUTION FOR INHALATION 2.5MCG | 吸入溶液（Respimat） | 資料未載明 |
| HK-64356 | SPIOLTO RESPIMAT INHALATION SOLUTION 2.5MCG/2.5MCG | 吸入溶液（Respimat，與 Tiotropium 複方） | 資料未載明 |

兩張許可證的持有廠商皆為 BOEHRINGER INGELHEIM (HK) LTD。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據都是 COPD 族群的觀察性研究、上市後監測與回顧，沒有任何研究以支氣管炎為獨立終點，證據等級僅 L3。
- 高 TxGNN 分數很可能來自 COPD 的重疊，不能當作獨立證據。

**若要推進需要：**
- 明確定義目標適應症為「COPD 內的慢性支氣管炎」，並釐清與急性支氣管炎的區別。
- 從 COPD 試驗中取出慢性支氣管炎亞群的分析，或設計以其為終點的研究。
- 補齊許可證的核准適應症、DrugBank 作用機轉，以及香港衛生署仿單的警語與禁忌症。
- 若日後以 COPD 為範圍推進，需限定於 COPD、不延伸到氣喘單方治療，並監測心血管事件與 β 受體促效劑的類別效應。這一步實際上是確認既有適應症，並非新的老藥新用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

