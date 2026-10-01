---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 5
---

# Hydrocortisone Acetate
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

# Hydrocortisone Acetate：從外用皮質類固醇到圓禿 (Alopecia Areata)

## 一句話總結

Hydrocortisone Acetate 是低效價皮質類固醇，香港已有多張 1% 乳膏的許可證，但資料中未載明核准適應症。
TxGNN 模型預測它可能對**圓禿 (Alopecia Areata)** 有效，
目前有 **1 個臨床試驗**和 **2 篇文獻**，但該試驗是把它當對照組，並不能證明它本身有效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 圓禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L2（依判定規則；僅 1 個已完成的 Phase 3 RCT，且為對照組設計） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Hydrocortisone Acetate 屬於皮質類固醇類，機轉上可能適用於圓禿。

圓禿是 T 細胞介導的自體免疫疾病，免疫細胞攻擊毛囊。皮質類固醇能抑制局部免疫反應，外用與病灶內注射類固醇本來就是圓禿的既有療法，所以這個預測在生物學上說得通。

不過 Hydrocortisone 是低效價類固醇，效果不如 clobetasol 這類強效藥物。目前唯一的 Phase 3 試驗把它放在對照組，只能看出相對療效，不能證明它自己有效。試驗紀錄也沒有確認使用的是醋酸鹽（acetate）型態。

其他四個預測（休止期落髮、毛囊黏蛋白症、禿髮性毛囊炎、遺傳性少毛症伴反覆皮膚水泡）都沒有臨床試驗或文獻。其中休止期落髮和遺傳性少毛症主要不是發炎性疾病，類固醇缺乏機轉依據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 完成 | 41 | 隨機對照試驗（2002-08 至 2003-08），比較 0.05% clobetasol propionate 乳膏與 1% hydrocortisone 乳膏用於兒童圓禿。Hydrocortisone 為低效價對照組；樣本數小，且未確認是否為醋酸鹽 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | 病例系列（依標題推定） | Przeglad dermatologiczny | 以 hydrocortisone acetate 懸浮液做病灶內皮下注射，治療嚴重型圓禿（無摘要） |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | 皮膚病外用療法進展；提到 fluocortin butyl ester 的抗發炎效果約與 hydrocortisone acetate 相當，未直接針對圓禿 |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中未提供劑型欄位與核准適應症，僅從品名可知為 1% 乳膏。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57592 | NERIDERM CREAM 1% | EUROPHARM LAB CO LTD |
| HK-52240 | SIGMACORT CREAM 1% | ASPEN PHARMACARE ASIA LIMITED |
| HK-06471 | HYTISONE CREAM 1% | ATLANTIC PHARMACEUTICAL LIMITED |
| HK-08072 | HYDROCORTISONE CREAM 1% | EUROPHARM LAB CO LTD |
| HK-57594 | ADDICORT CREAM 1% | EUROPHARM LAB CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉合理，但唯一的 Phase 3 試驗把 hydrocortisone 當作低效價對照組，不能證明它對圓禿有效。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症。
- 查證 NCT01453686 的完整結果，確認 hydrocortisone 組的實際反應，以及使用的鹽類型態。
- 確認劑型是否相容：現有許可證皆為外用乳膏，而早期文獻用的是病灶內注射。
- 補充作用機轉資料（MOA）。
- 評估是否已有更高效價的類固醇（如 clobetasol）作為標準選擇，以判斷本藥的實際價值。

> 本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

