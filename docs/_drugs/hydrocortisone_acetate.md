---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Hydrocortisone Acetate：預測新適應症為圓形禿 (Alopecia Areata)（證據等級 L5）。原適應症：自體免疫疾病、腎上腺皮質功能不全、克隆氏症、先天性腎上腺增生等"
monitor_inn: "HYDROCORTISONE ACETATE"
predicted_indications: ["alopecia areata", "telogen effluvium", "alopecia mucinosa", "Quinquaud's folliculitis decalvans", "hereditary hypotrichosis with recurrent skin vesicles"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Hydrocortisone Acetate：從自體免疫疾病與腎上腺皮質功能不全到圓形禿
{: .text-alpha }

## 一句話總結

Hydrocortisone acetate 是一種皮質類固醇，原本用於自體免疫疾病、腎上腺皮質功能不全、克隆氏症等。
TxGNN 模型預測它可能對**圓形禿 (Alopecia Areata)** 有效，
目前有 **1 個臨床試驗**（本藥為對照組）和 **2 篇文獻**（皆為較早期的報告），整體證據偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 自體免疫疾病、腎上腺皮質功能不全、克隆氏症、先天性腎上腺增生等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 圓形禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L3（見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

**證據等級說明：** 唯一的 Phase 3 試驗雖已完成，但本藥只是對照組，並非受試藥物，無法視為直接證據，因此不判為 L1。目前僅有病例系列與回顧性文獻，故判定為 L3。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，hydrocortisone 屬於皮質類固醇，具有抗發炎與免疫抑制作用，其在自體免疫疾病中的用途已被確立。

圓形禿是一種 T 細胞媒介攻擊毛囊的自體免疫疾病。由於 hydrocortisone 的原適應症本來就包含自體免疫疾病，從機轉上推論，它可能透過抑制毛囊周圍的免疫發炎反應而發揮作用。

不過需要注意，hydrocortisone 屬於低效價外用類固醇，圓形禿的治療通常偏好較高效價的類固醇。現有試驗是以 hydrocortisone 1% 作為對照，並非作為受試藥物。因此機轉上合理，但是否具有足夠療效仍需驗證。

其他預測的新適應症（休止期落髮、毛囊黏蛋白症、禿髮性毛囊炎、遺傳性少毛症合併反覆皮膚水泡）皆只有模型預測，沒有臨床試驗或文獻支持，證據等級為 L5。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 完成 | 41 | 比較 0.05% clobetasol propionate 乳膏與 1% hydrocortisone 乳膏用於兒童圓形禿；hydrocortisone 為對照組，僅提供間接證據，樣本數小 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | 病例系列 | Przeglad dermatologiczny | 以 hydrocortisone acetate 懸浮液進行皮損內皮下注射，治療嚴重型圓形禿（無摘要） |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | 皮膚疾病外用治療進展回顧；指出 fluocortin butyl ester 的抗發炎效果約與 hydrocortisone acetate 相當 |

---

## 香港上市資訊

共有 20 張有效許可證，皆為單一成分製劑，無已註銷者。以下列出 5 張主要許可證（許可證資料未載明劑型與核准適應症）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57592 | NERIDERM CREAM 1% | 乳膏（依品名） | 未載明 |
| HK-52240 | SIGMACORT CREAM 1% | 乳膏（依品名） | 未載明 |
| HK-06471 | HYTISONE CREAM 1% | 乳膏（依品名） | 未載明 |
| HK-08072 | HYDROCORTISONE CREAM 1% | 乳膏（依品名） | 未載明 |
| HK-41466 | HYDROCORTISONE-POS N EYE OINT 1% | 眼用軟膏（依品名） | 未載明 |

---

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自藥物－疾病關聯，並非仿單內容）：高血壓、癲癇、胃潰瘍、腎臟疾病、肝臟疾病、膽囊疾病、高血糖、麻疹、單純疱疹病毒角膜炎，以及腦下垂體功能低下相關疾病（如生長激素缺乏症、低促性腺激素性性腺功能低下、Kallmann 症候群、Sheehan 症候群等）。

其餘仿單警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一的臨床試驗中 hydrocortisone 僅為對照組，其他文獻為 1970 年代的病例系列與回顧，無法證明療效；且 hydrocortisone 效價偏低，圓形禿通常採用較高效價的類固醇，臨床上缺乏優先選擇的理由。
- 目前仍屬研究假說階段，尚不足以進入實質開發。

**若要推進需要：**
- 以 hydrocortisone 為受試藥物、與安慰劑或較高效價類固醇比較的對照試驗
- 詳細的作用機轉資料（MOA）
- 取得香港仿單的警語、禁忌與核准適應症資料
- 評估劑型與給藥途徑的相容性（現有許可證以外用乳膏為主，皮損內注射劑型需另行確認）
- 兒童與長期使用的局部及全身性安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

