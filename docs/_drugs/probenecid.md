---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 717
evidence_level: L5
indication_count: 3
---

# Probenecid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Probenecid：從痛風／高尿酸血症到腎性低尿酸血症

## 一句話總結

Probenecid（丙磺舒）是促尿酸排泄藥，一般用於痛風與高尿酸血症（本資料包未收錄原適應症，此處依一般藥理知識說明）。
TxGNN 模型預測它可能對**腎性低尿酸血症 (Hypouricemia, renal)** 有效，但目前**沒有臨床試驗**，只有 **20 篇疾病相關文獻**，且沒有一篇顯示 Probenecid 能治療這個疾病。
這個預測在藥理方向上很可能是反的，不建議推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, renal) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5（僅有模型預測，無支持療效的研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。以下推論來自一般藥理知識，不是資料包內容。Probenecid 會抑制腎小管的尿酸再吸收轉運體 URAT1（SLC22A12），也會抑制 OAT1/OAT3，因此增加尿酸從腎臟排出，血中尿酸下降。

遺傳性腎性低尿酸血症，主要成因是 URAT1 功能喪失，使腎臟尿酸再吸收不足，血尿酸本來就偏低。Probenecid 的作用等於人為重現這個疾病的病理機轉，理論上可能讓低尿酸更嚴重，而不是改善。

TxGNN 的高分（0.997）較可能來自知識圖譜中「藥物—尿酸轉運體—疾病」的鄰近關係，而不是治療方向一致。文獻中 Probenecid 多半被當作診斷探針，用來測試尿酸轉運功能（例如 PMID 8341392、7099326、854144），不是治療用途。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

資料包共 20 篇文獻，以下列出最相關的 10 篇（綜述與世代研究優先，其次為個案報告）。所有文獻的相關性標記皆為「待審」。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | 給風濕科醫師的低尿酸血症更新，依病因分類整理 |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | 遺傳性腎性低尿酸血症多由 URAT1（SLC22A12）功能喪失突變造成 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort | J Am Soc Nephrol | 32 位日本患者的臨床與 SLC22A12 基因分析，說明 URAT1 基因與尿酸排泄的關係 |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report/Review | Am J Kidney Dis | 腎性低尿酸血症與運動誘發急性腎衰竭，討論預防方式 |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | 兩位男性手足患遺傳性腎性低尿酸血症，並發運動誘發急性腎衰竭 |
| [8533596](https://pubmed.ncbi.nlm.nih.gov/8533596/) | 1995 | Case report | Acta Paediatr Jpn | 15 歲男孩運動後急性腎衰竭，Probenecid 與 Pyrazinamide 測試顯示尿酸轉運完全缺陷 |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report（機轉） | Nephron | 患者對 Probenecid 與 Pyrazinamide 皆無反應，Probenecid 作為診斷探針 |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report（機轉） | Nephron | 家族性腎性低尿酸血症，尿酸排泄在 Probenecid 後反而下降 |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | 家族性低尿酸血症，尿酸清除率對 Probenecid 與 Pyrazinamide 反應減弱 |
| [9510398](https://pubmed.ncbi.nlm.nih.gov/9510398/) | 1998 | 臨床研究（類型待確認） | Intern Med | 16 位日本腎性低尿酸血症患者，探討血尿的風險因子 |

以上文獻都只描述疾病本身或把 Probenecid 當診斷工具，沒有任何一篇評估 Probenecid 的治療效果。

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-57027 | U-ACID TAB 500MG | SYNCO (H.K.) LIMITED |
| HK-16674 | PROBENECID TAB 500MG (WHITE) | SYNCO (H.K.) LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測，沒有任何臨床試驗，文獻也不支持 Probenecid 有治療效果。
- 藥理方向很可能相反：Probenecid 會增加尿酸排泄，可能加重低尿酸血症，並增加運動誘發急性腎衰竭的風險。

**若要推進需要：**
- 由臨床藥理專家確認預測方向，通常應直接排除此適應症。
- 補齊 DrugBank 的作用機轉資料，並取得香港衛生署仿單的警語與禁忌。
- 同一藥物的另外兩項預測（Lesch-Nyhan 症候群、HPRT 部分缺乏症）也建議維持 Hold：它們只對高尿酸這一面有間接關聯，且增加尿中尿酸負荷有結石與腎病變風險，標準治療是 Allopurinol 這類黃嘌呤氧化酶抑制劑。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

