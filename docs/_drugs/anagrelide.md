---
layout: default
title: Anagrelide
parent: 中證據等級 (L3-L4)
nav_order: 59
evidence_level: L4
indication_count: 2
---

# Anagrelide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# Anagrelide：從血小板增多症相關治療到反應性血小板增多症

## 一句話總結

Anagrelide 是一種降血小板藥物，目前缺乏原適應症的官方登載資料。
TxGNN 模型預測它可能對**反應性血小板增多症 (Reactive Thrombocytosis)** 有效，
目前**沒有臨床試驗**，僅有 **10 篇文獻**（多為回顧與個案，且多數談的是原發性血小板增多症），實質支持度有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未登載適應症文字 |
| 預測新適應症 | 反應性血小板增多症 (Reactive Thrombocytosis) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。以下依一般藥理知識補充：Anagrelide 透過干擾巨核細胞成熟來降低血小板數量，其抗血小板作用（PDE3 抑制）是另一種獨立效應。這條途徑理論上能降低任何類型的血小板增多。

然而，Anagrelide 的既有用途是原發性血小板增多症 (essential thrombocythemia)，那是一種血液幹細胞的克隆性疾病。反應性血小板增多症則是由發炎、缺鐵、感染、惡性腫瘤或脾臟切除後，細胞激素（如 IL-6、TPO）升高所引起。通常處理的是原因，血栓風險一般偏低，多數情況不需要降血小板治療。文獻也明確指出，反應性血小板增多症通常不需要治療介入。

TxGNN 的高分（0.998）較可能反映知識圖譜中「反應性血小板增多症」與「原發性血小板增多症」兩個節點距離很近，並非針對此適應症的獨立證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻多在討論原發性血小板增多症或血小板增多症的鑑別診斷，並非直接證明 Anagrelide 對反應性血小板增多症有效。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Rev Anticancer Ther | 回顧 Anagrelide 的作用機轉與治療潛力；指出反應性血小板增多症不需治療介入，克隆性者才需降血小板治療 |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leuk Lymphoma | 評析 Anagrelide 用於原發性血小板增多症及相關疾病；反應性血小板增多症通常影響不大 |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Aust | 原發性血小板增多症的診斷需排除反應性血小板增多症；血小板 >1000×10⁹/L 應接受降血小板治療 |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | 說明血小板增多症與血小板增多症候群的臨床譜系 |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki | 原發性血小板增多症的診斷與治療；Anagrelide 為降血小板藥物之一，並討論與反應性者的鑑別 |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leuk Res | 骨髓增生性腫瘤極端血小板增多時，血小板分離術的角色 |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective cohort | Pediatr Blood Cancer | 回溯 12 例兒童原發性與反應性血小板增多症 |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case report | Eur J Case Rep Intern Med | 原發性血小板增多症患者使用 Anagrelide 期間發生急性心肌梗塞 |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case report | Srp Arh Celok Lek | 原發性血小板增多症合併僵直性脊椎炎，以 Anagrelide 等藥物合併治療 |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case report | Medicine | 脾臟切除後血小板增多症患者成功接受斷指再植 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68231 | ANAGRELIDE SANDOZ CAPSULES 0.5MG | 未登載 | 未登載 |
| HK-51737 | AGRYLIN CAP. 0.5 MG | 未登載 | 未登載 |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢無結果。

## 結論與下一步

**決策：Hold**

**理由：**
沒有臨床試驗，文獻多為原發性血小板增多症的回顧與個案，並無直接證據顯示 Anagrelide 對反應性血小板增多症有益。反應性血小板增多症的標準處理是治療原因，且血栓風險通常低，使用細胞減量藥物的臨床需求不明。高 TxGNN 分數可能只是知識圖譜相近性造成的假象。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料
- 取得香港衞生署仿單的警語與禁忌症，完成安全性篩檢
- 釐清是否存在「反應性血小板增多症且血栓風險高、需降血小板」的特定族群（例如脾臟切除後極端血小板增多）
- 針對該族群搜尋或設計對照研究，並確認與原發性血小板增多症的診斷區隔

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

