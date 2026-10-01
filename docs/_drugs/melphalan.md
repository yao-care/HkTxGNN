---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 551
evidence_level: L5
indication_count: 5
---

# Melphalan
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

# Melphalan：從原適應症（許可證未載明）到性腺生殖細胞腫瘤

## 一句話總結

Melphalan 是一種雙功能氮芥類（nitrogen mustard）烷化劑，香港有 2 張許可證，但證據包中未載明原適應症。
TxGNN 模型預測它可能對**性腺生殖細胞腫瘤 (Gonadal Germ Cell Tumor)** 有效。
目前有 **7 個臨床試驗**和 **4 篇文獻**與此方向相關，其中直接對應的只有 1 個 Phase 2 試驗，而且是多藥合併方案。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 性腺生殖細胞腫瘤 (Gonadal Germ Cell Tumor) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L3（證據包標示 L2，但唯一的 Phase 2 試驗未確認為 RCT，依規則下修） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 尚未取得）。根據已知資訊，Melphalan 是雙功能氮芥類烷化劑，透過使 DNA 交叉鏈結來殺傷腫瘤細胞。

生殖細胞腫瘤對 DNA 損傷型化療藥物高度敏感。高劑量 Melphalan 搭配自體幹細胞救援，是復發、預後不良個案的合理挽救策略。

不過，現有試驗多為合併方案，Melphalan 的獨立貢獻無法從資料中區分。此預測目前只能視為「值得研究的問題」，還不是已證實的療效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | 完成 | 64 | 復發、預後不良生殖細胞腫瘤的兩輪高劑量化療（含 Melphalan），與適應症最貼近；Melphalan 的角色未能單獨確認 |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | 完成 | 451 | 血液惡性腫瘤與部分實體瘤的自體移植，八種高劑量方案；生殖細胞腫瘤僅是其中一個亞群 |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | 完成 | 25 | 劑量遞增 Melphalan 併自體幹細胞支持與 Amifostine 保護；族群為混合實體瘤 |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | 完成 | 25 | Busulfan/Melphalan/Topotecan 後接自體移植，支持含 Melphalan 方案的可行性與安全性 |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | NA | 完成 | 174 | 血液惡性腫瘤與部分實體瘤的自體移植，無對照比較 |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | NA | 完成 | 36 | 非清髓性異體移植，Melphalan 最多只是預處理成分，間接相關 |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | 完成 | 6 | 鞘內注射 Melphalan 用於腫瘤性腦膜炎，途徑與情境不同，僅有間接的安全性參考 |

另有 NCT00003926（Phase 1，Amifostine 化學保護，人數 13，已終止）屬支持性照護研究，不評估療效，未列入表中。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | 回顧 | Urologic Clinics of North America | 精原細胞瘤（Seminoma）相關回顧，無摘要 |
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | 回顧 | Oncology | 睪丸生殖細胞腫瘤的化療回顧，無摘要 |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | 歷史病例系列 | Voprosy Onkologii | 以 Sarcolysin（Melphalan）治療睪丸精原細胞瘤及其轉移的經驗，無摘要 |

另有 1 篇（PMID 14151951）為 1964 年的藥理生理研究，與主題無關，已排除。

文獻皆為 1950–1970 年代的舊資料，且沒有摘要可供核對。這些文獻只能說明 Melphalan 在此領域有歷史使用紀錄，不能作為現代療效證據。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-03792 | ALKERAN TAB 2MG | Aspen Pharmacare Asia Limited |
| HK-37994 | ALKERAN FOR INJ 50MG | Aspen Pharmacare Asia Limited |

## 細胞毒性

以下為依藥物類別（烷化劑）所作的判斷，並非來自證據包內的 toxicity 資料。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氮芥類烷化劑） |
| 骨髓抑制風險 | 高（高劑量使用時需要幹細胞救援） |
| 致吐性分級 | 中度（依劑型與劑量而異） |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

正式警語與注意事項請參考原廠仿單。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 直接對應的證據只有 1 個多藥合併的 Phase 2 試驗，Melphalan 的獨立貢獻不明，文獻也都是數十年前的舊資料。
- 香港藥品仿單的警語與禁忌尚未取得，這是阻擋性缺口，無法進入安全性篩選。

**若要推進需要：**
- 下載並解析香港衛生署的 Melphalan 仿單，補齊警語、禁忌症與原適應症。
- 查詢 DrugBank 取得作用機轉（MOA）。
- 取得 NCT00936936 的結果，確認 Melphalan 在方案中的角色與療效數據。
- 補充現代（近 20 年）生殖細胞腫瘤高劑量化療的文獻。

**其他預測適應症（供參考）：**
- 乳癌（女性）：有多項高劑量 Melphalan 併幹細胞救援的 Phase 1–2 研究，但資料多已陳舊，且以合併方案為主。
- 卵巢原始生殖細胞腫瘤：僅有間接的混合實體瘤證據。
- 卵巢絨毛膜癌、卵巢惡性非上皮腫瘤：僅有模型預測，無試驗或文獻，建議 Hold。

本報告結果僅供研究參考，不構成醫療建議。預測適應症需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

