---
layout: default
title: Ergometrine
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Ergometrine
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

# Ergometrine：從（未載明原適應症）到偏頭痛

## 一句話總結

Ergometrine 是麥角生物鹼類藥物，香港登記產品為 SYNTOMETRINE 注射劑，但登記資料未載明原適應症。
TxGNN 模型的首位預測為毛髮過多症 (hypertrichosis)，但完全沒有證據支持；證據最多的方向是**偏頭痛 (Migraine Disorder)**，目前有 **0 個臨床試驗**和 **約 20 篇文獻**（多為近緣藥物 methylergonovine 的小型研究，本報告列出其中 10 篇），證據強度偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明 |
| 預測新適應症 | 毛髮過多症 (Hypertrichosis)（TxGNN 排名第 1，無任何證據）；較有研究價值的方向：偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 毛髮過多症 99.96%；偏頭痛 99.93% |
| 證據等級 | 毛髮過多症 L5；偏頭痛 L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold（偏頭痛方向可列為 Research Question） |

> 注意：TxGNN 分數僅代表模型預測，前 10 名分數皆在 99.8% 以上，差異不大，不代表臨床有效機率。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據已知資訊，Ergometrine 是麥角生物鹼，作用於子宮平滑肌，也作用於血清素、腎上腺素與多巴胺受體。

**毛髮過多症（排名第 1）：** 看不出任何機轉關聯。藥物的已知作用與毛髮生長無關，高分僅來自知識圖譜推論，沒有試驗或文獻。

**偏頭痛（排名第 7）：** 機轉上有合理性。麥角生物鹼作用於 5-HT1B/1D 等血清素受體，並造成顱內血管收縮。Ergometrine 的近緣藥物 methylergonovine 有小型非對照或回溯性研究，用於難治型偏頭痛預防與經期偏頭痛。但 ergometrine 本身的直接證據有限，從 methylergonovine 外推需要謹慎。

**其他預測：** 排名第 2–6、9 的疾病（Ambras 型先天性全身多毛症、腎因性抗利尿不適當症候群、牙周相關畸形症候群、Dandy-Walker 畸形症候群、遺傳性毛幹異常、痲瘋病）皆無合理藥理機轉。牙周炎的 20 筆文獻只是疾病關鍵字重疊，與藥物無關。偏頭痛伴腦幹先兆（排名第 8）與肺高壓（排名第 10）的文獻反而顯示麥角類血管收縮作用可能造成傷害，方向可能相反。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為偏頭痛方向（排名第 7）的文獻，依研究類型（世代研究優先）與相關性挑選：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2759844](https://pubmed.ncbi.nlm.nih.gov/2759844/) | 1989 | Cohort | Headache | 40 名經期偏頭痛患者接受間歇性 ergonovine 預防性治療，追蹤 6 個月 |
| [23432443](https://pubmed.ncbi.nlm.nih.gov/23432443/) | 2013 | Cohort | Headache | 口服 methylergonovine 用於難治型偏頭痛與叢集性頭痛預防 |
| [19895705](https://pubmed.ncbi.nlm.nih.gov/19895705/) | 2009 | Cohort | Head & Face Medicine | 急診女性偏頭痛患者靜脈注射 methylergonovine 的療效與耐受性（開放式先導研究） |
| [7216754](https://pubmed.ncbi.nlm.nih.gov/7216754/) | 1980 | Cohort | Headache | 偏頭痛間歇期治療的長期結果 |
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | Cephalalgia | Methysergide（ergometrine 衍生物）用於偏頭痛預防，兼具 5-HT2 拮抗與 5-HT1 促效作用 |
| [23216317](https://pubmed.ncbi.nlm.nih.gov/23216317/) | 2013 | Review | Headache | 偏頭痛藥物的血清素相關心臟不良事件（QT 延長、冠狀動脈痙攣） |
| [556819](https://pubmed.ncbi.nlm.nih.gov/556819/) | 1977 | Review | Neurology | 偏頭痛預防藥物似乎對頸動脈痛也有效（8 名女性） |
| [15293589](https://pubmed.ncbi.nlm.nih.gov/15293589/) | 2004 | Review | Am J Crit Care | Prinzmetal 變異型心絞痛（冠狀動脈血管痙攣）概述 |
| [5761912](https://pubmed.ncbi.nlm.nih.gov/5761912/) | 1969 | Review | Br Med J | 復發性頭痛的預防 |
| [10971665](https://pubmed.ncbi.nlm.nih.gov/10971665/) | 2000 | Case report | Headache | 有先兆慢性偏頭痛患者產後發生腦血管病變 |

以上皆非隨機對照試驗，多為小型開放式或回溯性研究，且主要針對 methylergonovine 而非 ergometrine。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-01698 | SYNTOMETRINE INJ | 資料未載明 | 資料未載明 |

製造商：DCH AURIGA (HONG KONG) LIMITED - HEALTHCARE DIVISION。

---

## 安全性考量

- **藥物交互作用**：DrugBank 查無相關資料。
- 文獻提示的潛在風險：麥角類藥物的血管收縮作用可能誘發冠狀動脈痙攣、心肌缺血；有心臟或肺血管疾病的孕產婦使用後曾出現急性肺高壓危象（PMID 26050249）；長期使用麥角類藥物（如 Sansert、Ergotrate）曾有胸膜增厚的報告（PMID 6773347）。
- 香港衛生署仿單的警語與禁忌尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（偏頭痛方向可列為 Research Question）

**理由：**
- TxGNN 首位預測（毛髮過多症）及其餘多數預測沒有證據，也沒有合理機轉，僅為模型輸出。
- 偏頭痛方向有機轉合理性與小型觀察性研究，但證據來自近緣藥物 methylergonovine，沒有登記試驗，且心血管血管痙攣風險明顯，不宜直接推進。
- 肺高壓與伴腦幹先兆偏頭痛的文獻反映的是安全警訊，而非治療證據。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、原核准適應症），完成 S1 安全性篩選（目前為阻斷性缺口）。
- 補齊 DrugBank 的作用機轉資料。
- 系統性比較 ergometrine 與 methylergonovine 的藥理與藥動差異，評估外推是否成立。
- 設計以心血管安全為核心的評估（排除冠心病、血管痙攣、周邊血管疾病族群）。
- 確認給藥途徑與劑型：現有登記為注射劑，慢性偏頭痛預防通常需要口服劑型。

---

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

