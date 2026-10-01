---
layout: default
title: Roxithromycin
parent: 僅模型預測 (L5)
nav_order: 776
evidence_level: L5
indication_count: 10
---

# Roxithromycin
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

# Roxithromycin：從細菌感染治療到痲瘋病 (Leprosy)

## 一句話總結

Roxithromycin 是巨環內酯類 (macrolide) 抗生素，原本用於抗菌治療。
TxGNN 模型預測它可能對**痲瘋病 (Leprosy)** 有效，
目前**沒有臨床試驗**，只有 **5 篇文獻**，其中 3 篇是前臨床研究，2 篇是回顧性文章。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 痲瘋病 (Leprosy) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L4（僅有前臨床研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold（列為研究問題） |

香港許可證資料未載明核准適應症，因此無法列出原適應症。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Roxithromycin 屬於巨環內酯類，這類藥物的已知機轉是結合細菌 50S 核糖體次單元，抑制蛋白質合成。

巨環內酯類在體外和小鼠模型中，對麻風桿菌 (*Mycobacterium leprae*) 都有活性，所以這個預測在生物學上說得通。1991 年的小鼠足墊感染研究發現，roxithromycin 和 clarithromycin 都有穩定的活性，而且具殺菌效果；erythromycin 和 azithromycin 則無效。

不過，同一研究顯示 clarithromycin 的效果比 roxithromycin 好，部分原因可能是 clarithromycin 在感染部位的濃度較高。另有 1999 年日本的回顧文章提到，roxithromycin 等藥物兼具抗發炎和免疫調節作用，可能有助於控制痲瘋病的周邊神經病變。目前沒有針對 roxithromycin 的人體試驗。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1648889](https://pubmed.ncbi.nlm.nih.gov/1648889/) | 1991 | 前臨床（小鼠模型） | Antimicrob Agents Chemother | Roxithromycin 與 clarithromycin 對小鼠麻風桿菌感染穩定有效且具殺菌力，clarithromycin 較佳；erythromycin 與 azithromycin 無效 |
| [3072920](https://pubmed.ncbi.nlm.nih.gov/3072920/) | 1988 | 前臨床（體外／體內） | Antimicrob Agents Chemother | 比較多種新型巨環內酯類對麻風桿菌的體外與體內活性 |
| [2665640](https://pubmed.ncbi.nlm.nih.gov/2665640/) | 1989 | 前臨床（體外） | Antimicrob Agents Chemother | 在小鼠巨噬細胞中快速篩選 25 種以上抗菌藥對麻風桿菌的作用 |
| [10481449](https://pubmed.ncbi.nlm.nih.gov/10481449/) | 1999 | Review | Nihon Hansenbyo Gakkai Zasshi | Clarithromycin、roxithromycin 等藥物兼具抗麻風桿菌、抗發炎與免疫調節作用，討論其用於痲瘋病周邊神經病變 |
| [12762831](https://pubmed.ncbi.nlm.nih.gov/12762831/) | 2003 | Review | Am J Clin Dermatol | 巨環內酯類用於皮膚感染的選擇與使用指引 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-59865 | RUXID TAB 150MG | AUSTRALIAN MEDIC-CARE COMPANY LTD |
| HK-45894 | ROXINOX TAB 150MG | DELTAPHARM LIMITED |
| HK-59862 | RUXID TAB 300MG | AUSTRALIAN MEDIC-CARE COMPANY LTD |
| HK-64539 | ROXITHRO TABLETS 150MG | MEDILINE (HONG KONG) COMPANY LIMITED |
| HK-51356 | POLIROXIN TAB 150MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。DrugBank 未查到藥物交互作用資料。

另有一項前臨床訊號值得留意：巨環內酯類在體外會抑制 trastuzumab emtansine (T-DM1) 對 HER2 陽性乳癌細胞的細胞毒性（PMID 37971309）。若病人同時使用抗體藥物複合體，需評估這項潛在交互作用。

## 結論與下一步

**決策：Hold**

**理由：**
- 痲瘋病的證據只有 1980 至 1990 年代的前臨床研究和回顧文章，沒有人體試驗。
- 巨環內酯類中，clarithromycin 的抗痲瘋病證據比 roxithromycin 更完整，所以 roxithromycin 比較適合當作研究問題，不適合直接推進。
- 其餘 9 個預測適應症（如多毛症、牙周相關畸形症候群、肺高壓、偏頭痛、乳癌等）多為 L5 或 L4，缺乏機轉連結或證據，也都建議 Hold。

**若要推進需要：**
- 補齊 roxithromycin 的作用機轉資料（可由 DrugBank 查詢）
- 取得香港衛生署的仿單，確認警語與禁忌症
- 搜尋 roxithromycin 用於痲瘋病的人體研究，並與 clarithromycin 做比較
- 確認痲瘋病的現行標準療法，評估 roxithromycin 是否只適合當輔助或替代用藥

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

