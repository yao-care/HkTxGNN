---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 377
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

# Hydrocortisone Acetate：從皮質類固醇抗發炎治療到圓禿（Alopecia Areata）

## 一句話總結

Hydrocortisone Acetate 是一種糖皮質激素（皮質類固醇），藥理上廣泛用於發炎性與過敏性疾病的局部或病灶內治療；目前本藥品在香港**未上市**，也缺乏官方核准適應症紀錄。
TxGNN 模型預測它可能對**圓禿 (Alopecia Areata)** 有效，目前有 **1 個已完成的 Phase 3 臨床試驗**和 **2 篇文獻**支持這個方向，但證據強度有限且安全性資料仍有關鍵缺口。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無官方核准適應症紀錄（未上市；依藥理分類屬皮質類固醇消炎用藥） |
| 預測新適應症 | 圓禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L2（1 個已完成之 Phase 3 RCT） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據已知的藥理分類，Hydrocortisone Acetate 屬於糖皮質激素，具抗發炎與免疫調節作用，可抑制毛囊周圍 CD8+ T 細胞浸潤——這正是圓禿（一種自體免疫性掉髮疾病）的核心病理機轉。

皮質類固醇（無論局部外用或病灶內注射）本已是臨床上治療圓禿的標準療法之一，因此這項預測的機轉關聯性高，並非全新假說，而是有明確臨床實作基礎的延伸。不過需特別留意兩點限制：第一，本藥品為 **acetate 酯化型態**，而現有試驗與文獻多以 hydrocortisone base（1% cream 或病灶內注射懸液）呈現，兩者效價分類同屬低效價（Class VI–VII），臨床等效性可推論但非同一分子直接證實；第二，由於原適應症資料本身缺失，本報告無法進一步比對原適應症與圓禿之間的疾病關聯性，僅能以藥理機轉作為主要論述基礎。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 已完成 | 41 | 兒童圓禿患者中比較 Clobetasol Propionate 0.05% Cream 與 Hydrocortisone 1% Cream 的療效，屬直接以 hydrocortisone 作為對照組治療圓禿的隨機對照試驗；結果通常顯示高效價 clobetasol 優於低效價 hydrocortisone，顯示 hydrocortisone 單方在中重度病灶效果有限，較適合輕度病灶或作為維持/銜接治療 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | 病例系列 | Przeglad dermatologiczny | 以病灶內皮下注射 hydrocortisone acetate 懸液治療重度圓禿之病例系列報告 |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | 文獻回顧 | MMW, Münchener medizinische Wochenschrift | 回顧皮膚科外用療法進展，指出新型外用皮質類固醇 fluocortin butyl 之抗發炎效果約與 hydrocortisone acetate 相當，但全身副作用較少 |

---

## 香港上市資訊

本藥品目前在香港**未上市**，無任何核准許可證紀錄（0 張）。

---

## 安全性考量

目前尚未取得完整的仿單警語、禁忌症與藥物交互作用資料，且此項缺口屬於 **Blocking** 等級（無法進入 S1 安全性初評）。安全性資訊請參考原廠仿單，並優先補齊上述資料後再進行下一步評估。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 個已完成的 Phase 3 RCT 直接以 hydrocortisone 治療圓禿為對照組，機轉上與圓禿的自體免疫病理相符，且局部/病灶內類固醇本為臨床已使用之標準療法之一，並非全新假說。
- 但證據強度有限：僅 1 個試驗（且結果傾向支持更高效價的 clobetasol 而非 hydrocortisone 本身），文獻證據多為 1970 年代舊資料，且本藥品專屬的安全性仿單資料仍缺（Blocking 等級），尚不足以支持全面推進。

**若要推進需要：**
- 取得 TFDA／香港衛生署仿單完整警語與禁忌症資料（目前為 Blocking 等級資料缺口，無法進入 S1 安全性初評）
- 補充作用機轉 (MOA) 詳細資料
- 確認 acetate 酯化劑型與 base/cream 劑型之臨床等效性
- 評估以病灶內注射或外用劑型作為輕度圓禿之輔助/銜接治療的適用族群，並排除中重度病人（此族群更適合高效價替代方案）

> 註：TxGNN 同時預測了其他 4 個候選適應症（telogen effluvium、alopecia mucinosa、Quinquaud's folliculitis decalvans、hereditary hypotrichosis with recurrent skin vesicles），因缺乏任何臨床試驗或文獻佐證（證據等級 L5），暫列為 Hold，本報告不深入討論。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

