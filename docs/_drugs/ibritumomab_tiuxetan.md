---
layout: default
title: Ibritumomab Tiuxetan
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 8
monitor_inn: "IBRITUMOMAB TIUXETAN"
predicted_indications: ["acute lymphoblastic/lymphocytic leukemia", "small intestinal Burkitt lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "mantle cell lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation"]
last_modified_at: 2026-10-28
description: "Ibritumomab Tiuxetan：預測新適應症為Acute lymphoblastic/lymphocytic leukemia（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ibritumomab Tiuxetan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Ibritumomab Tiuxetan: Acute lymphoblastic/lymphocytic leukemia
{: .text-alpha }

## 一句話總結

Ibritumomab Tiuxetan 是以釔-90 (Y-90) 標記的抗 CD20 放射免疫治療抗體，知識圖譜中記錄的使用範圍為濾泡性淋巴瘤與成熟 B 細胞腫瘤。
TxGNN 模型預測它可能對**被套細胞淋巴瘤 (Mantle Cell Lymphoma)** 有效，
目前有 **20 個臨床試驗**和 **20 篇文獻**與此方向相關，其中包含直接研究被套細胞淋巴瘤的 Phase 2 試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Acute lymphoblastic/lymphocytic leukemia |
| TxGNN 預測分數 | 0.9978 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ibritumomab Tiuxetan 是以 Y-90 標記的抗 CD20 抗體，藉由抗體鎖定 CD20 陽性的 B 細胞，並由 Y-90 釋放 β 輻射殺傷腫瘤細胞。

被套細胞淋巴瘤細胞表現 CD20，且對放射線敏感。Y-90 的 β 射線具有「交叉火力」效應，也能影響鄰近未被抗體結合的腫瘤細胞。因此機轉上適用於被套細胞淋巴瘤是合理的。

臨床資料顯示，已有單藥用於復發／難治型疾病、一線治療後鞏固，以及搭配 BEAM/BEAC 移植前處理、bortezomib 等組合的 Phase 2 研究。不過這些試驗規模偏小，且多為單臂設計，資料中未見 Phase 3 隨機對照試驗。

## 臨床試驗證據

以下列出與被套細胞淋巴瘤最相關的 10 個試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00038623](https://clinicaltrials.gov/study/NCT00038623) | Phase 2 | 完成 | 35 | Y-90 ibritumomab 用於復發／難治型被套細胞淋巴瘤，為單臂試驗，直接相關 |
| [NCT00514475](https://clinicaltrials.gov/study/NCT00514475) | Phase 2 | 完成 | 160 | 一線治療後未達完全緩解者，於移植前處理 BEAM/BEAC 加入 Y-90 ibritumomab |
| [NCT00070447](https://clinicaltrials.gov/study/NCT00070447) | Phase 2 | 完成 | 未提供 | R-CHOP 後接 Y-90 ibritumomab，用於未曾治療的被套細胞淋巴瘤 |
| [NCT00505232](https://clinicaltrials.gov/study/NCT00505232) | Phase 2 | 完成 | 30 | 抗 CD20 + Hyper-CVAD 誘導，之後以 Y-90 ibritumomab 鞏固 |
| [NCT00119730](https://clinicaltrials.gov/study/NCT00119730) | Phase 2 | 完成 | 30 | 簡短 FMR 化療後接 Zevalin，用於復發型被套細胞淋巴瘤 |
| [NCT01497275](https://clinicaltrials.gov/study/NCT01497275) | Phase 2 | 提前終止 | 5 | Zevalin 合併 bortezomib，因人數過少無法判讀療效 |
| [NCT00334438](https://clinicaltrials.gov/study/NCT00334438) | Phase 1 | 完成 | 12 | Zevalin 合併 bortezomib，僅提供組合安全性訊號 |
| [NCT00058292](https://clinicaltrials.gov/study/NCT00058292) | Phase 1 | 完成 | 44 | Y-90 ibritumomab 合併高劑量 BEAM 及幹細胞移植，可行性與安全性，族群為混合型淋巴瘤 |
| [NCT00438880](https://clinicaltrials.gov/study/NCT00438880) | Phase 1/2 | 完成 | 38 | CpG 7909、rituximab 合併 Y-90 Zevalin，為混合型 B 細胞非何杰金氏淋巴瘤 |
| [NCT01448928](https://clinicaltrials.gov/study/NCT01448928) | 不適用 | 完成 | 400 | 日本上市後藥物使用調查，涵蓋被套細胞淋巴瘤，提供真實世界安全性資訊 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19770379](https://pubmed.ncbi.nlm.nih.gov/19770379/) | 2009 | Phase 2 試驗 | J Clin Oncol | Y-90 ibritumomab 用於復發／難治型被套細胞淋巴瘤的安全性與療效 |
| [24652994](https://pubmed.ncbi.nlm.nih.gov/24652994/) | 2014 | Phase 2 試驗 | Blood | Nordic MCL3：未達完全緩解者於 BEAM/C 加入 Y-90 ibritumomab 後接受移植 |
| [22851557](https://pubmed.ncbi.nlm.nih.gov/22851557/) | 2012 | Phase 2 試驗 | J Clin Oncol | E1499：R-CHOP 後以 Y-90 ibritumomab 鞏固，用於未曾治療的被套細胞淋巴瘤 |
| [27780968](https://pubmed.ncbi.nlm.nih.gov/27780968/) | 2017 | Phase 2 長期追蹤 | Leukemia | E1499 研究的 10 年追蹤 |
| [30961415](https://pubmed.ncbi.nlm.nih.gov/30961415/) | 2019 | Phase 2 試驗 | Leuk Lymphoma | 不適合高劑量治療的患者以 Y-90 鞏固，8 年追蹤 |
| [26702476](https://pubmed.ncbi.nlm.nih.gov/26702476/) | 2016 | Phase 2 試驗 | Clin Lymphoma Myeloma Leuk | 第一線自體幹細胞移植後以 Y-90 ibritumomab 鞏固 |
| [23753021](https://pubmed.ncbi.nlm.nih.gov/23753021/) | 2013 | Phase 2 試驗 | Haematologica | R-hyperCVAD 交替 R-MTX-Ara-C 後以 Y-90 ibritumomab 鞏固（GELTAMO） |
| [21812533](https://pubmed.ncbi.nlm.nih.gov/21812533/) | 2012 | Phase 1 試驗 | Leuk Lymphoma | Ibritumomab 合併 bortezomib，用於復發／難治型被套細胞及低惡性度 B 細胞淋巴瘤 |
| [17722077](https://pubmed.ncbi.nlm.nih.gov/17722077/) | 2008 | Review | Am J Hematol | 被套細胞淋巴瘤的抗 CD20 免疫治療回顧 |
| [28978845](https://pubmed.ncbi.nlm.nih.gov/28978845/) | 2017 | Review | Rinsho Ketsueki | 被套細胞淋巴瘤治療回顧 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-54925 | ZEVALIN FOR INFUSION 1.6MG/ML | 未提供 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 放射免疫治療（Y-90 標記抗 CD20 抗體） |
| 骨髓抑制風險 | 請參考原廠仿單；輻射劑量會影響骨髓，併用移植前處理或化療時須特別留意 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 血球計數（CBC，含分類與血小板）、肝腎功能 |
| 處置防護 | 屬放射性藥品，須依放射性藥物處置規範操作 |

## 安全性考量

- **藥物交互作用**：已完成交互作用查詢，共 100 筆。其中列為 Major 的包括 acetylsalicylic acid（阿斯匹靈）、ibuprofen、ketorolac、abciximab、acalabrutinib、adalimumab、alteplase、anagrelide、antithrombin III 等，多與出血風險（抗血小板、NSAID、抗凝血或溶栓藥物）或免疫抑制相關。Moderate 的包括 alemtuzumab、anakinra、zidovudine、sibutramine 及部分疫苗等。

主要警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項直接以被套細胞淋巴瘤為對象的 Phase 2 試驗與發表文獻（含復發／難治型單藥及一線鞏固），但多為小型單臂研究，且沒有 Phase 3 隨機對照試驗，證據以 L2 為上限。
- 香港已有 1 張有效許可證，但資料中未提供核准適應症文字，無法確認被套細胞淋巴瘤是否在核准範圍內。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 取得作用機轉的詳細資料
- 與現行標準治療（含 BTK 抑制劑等新型標靶藥物）比較療效與定位
- 擬定骨髓抑制監測計畫，以及放射性藥品的處置與防護流程
- 評估是否需要隨機對照試驗或真實世界資料來確認效益

---

**附註：其他預測適應症**

另有 7 個預測適應症（急性淋巴芽細胞白血病、小腸 Burkitt 淋巴瘤、小腸／甲狀腺／乳房 MALT 淋巴瘤、扁桃腺淋巴瘤、突變型慢性淋巴球性白血病／小淋巴球淋巴瘤）目前僅有模型預測，無臨床試驗或文獻，證據等級均為 L5，建議決策為 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

