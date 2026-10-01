---
layout: default
title: Salicylamide
parent: 中證據等級 (L3-L4)
nav_order: 783
evidence_level: L4
indication_count: 5
---

# Salicylamide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Salicylamide：從感冒複方成分到咽炎

## 一句話總結

Salicylamide 是水楊酸類解熱鎮痛成分，在香港多用於感冒複方製劑（HK 許可證的適應症欄位未填寫）。
TxGNN 模型預測它可能對**咽炎 (Pharyngitis)** 有效，但目前**沒有臨床試驗**，只有 **3 篇 1950-60 年代的舊文獻**，且都不是針對 Salicylamide 的對照研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（品名多為感冒複方，如 COLDZEP、NEO-COLD、MECOLD） |
| 預測新適應症 | 咽炎 (Pharyngitis) |
| TxGNN 預測分數 | 99.98%（全體排名 852） |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Salicylamide 是水楊酸類解熱鎮痛藥，常作為多成分感冒藥的一部分。推測它可透過較弱的 COX 抑制作用緩解疼痛與發燒，機轉上可能適用於咽炎的喉嚨痛與發熱。

這只是症狀緩解，不是治療疾病本身。此推論僅來自藥物類別，不是來自已確認的機轉資料。

TxGNN 分數（0.9998）在所有候選適應症中幾乎都接近飽和，無法區分預測的優劣，不宜單獨作為依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

三篇都沒有摘要，以下依標題與研究類型整理，且都沒有現代標準的對照研究。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [5354503](https://pubmed.ncbi.nlm.nih.gov/5354503/) | 1969 | 雙盲試驗 | Minerva Medica | 比較兩種鉍製劑用於咽扁桃腺炎；研究藥物並非 Salicylamide，相關性低 |
| [13060598](https://pubmed.ncbi.nlm.nih.gov/13060598/) | 1953 | 臨床報告（非對照） | Gazzetta Medica Italiana | Salicylamide 合併對胺基苯甲酸鈉用於嬰兒卡他性扁桃腺炎 |
| [14126993](https://pubmed.ncbi.nlm.nih.gov/14126993/) | 1963 | 臨床經驗報告 | Kinderarztliche Praxis | 新型直腸膠囊解熱鎮痛藥的使用經驗 |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-07880 | COLDZEP TAB | Meyer Pharmaceuticals Ltd |
| HK-26015 | NEO-COLD CAP | Unicorn Laboratories（American Unicorn Laboratories Limited） |
| HK-31316 | COLIDIN TAB | Meyer Pharmaceuticals Ltd |
| HK-07883 | MECOLD (FORTE) CAP | Meyer Pharmaceuticals Ltd |
| HK-07882 | MECOLD (SCT) RED TAB | Meyer Pharmaceuticals Ltd |

## 安全性考量

以下是從感冒預測項下的文獻檢索到的安全性訊號，並非來自仿單：

- **過量毒性**：有 Salicylamide 過量中毒的報告（PMID 8864802，1996）。
- **血液學風險**：有病例報告指出，服用含 Salicylamide 的感冒複方（另含 Acetaminophen、Caffeine、Promethazine）合併 Cefadroxil 後，發生藥物誘發溶血性貧血與顆粒球缺乏症（PMID 8952318，1996）。複方成分眾多，無法確定是哪個成分造成。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 咽炎預測沒有任何臨床試驗，僅有 3 篇舊文獻，且都是非對照報告或與 Salicylamide 無關的研究，無法判斷單一成分的貢獻。
- 預測分數過於飽和，缺乏鑑別力。作用機轉缺失，且文獻中出現過量毒性與血液學安全性訊號，需先釐清。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症（目前為阻擋性缺口）。
- 補齊 DrugBank 的作用機轉資料。
- 取得 3 篇文獻全文，確認 Salicylamide 單獨或複方的實際療效數據。
- 評估 Salicylamide 相較於現有解熱鎮痛藥（如 Acetaminophen、NSAIDs）在咽炎的實際價值。

**其他預測適應症（供參考）：**
- 感冒 (common cold) 的文獻較多（L4），但多為 1950-60 年代的複方製劑報告，無法單獨歸因於 Salicylamide。
- 急性喉咽炎 (acute laryngopharyngitis) 與咽炎相近，若咽炎證據增強，可一併檢視。
- 鼻腔疾病 (nasal cavity disease) 和三叉自律神經頭痛 (trigeminal autonomic cephalalgia) 缺乏可信證據，建議維持 Hold。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

