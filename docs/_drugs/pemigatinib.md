---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 675
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pemigatinib：預測新適應症為多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Pemigatinib"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "amyotrophic lateral sclerosis, susceptibility to", "axial spondylometaphyseal dysplasia"]
---

# Pemigatinib
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

# Pemigatinib：從（原適應症未載明）到多發性內分泌腫瘤

## 一句話總結

Pemigatinib 是一種選擇性 FGFR1-3 抑制劑，目前在香港已有 3 張有效許可證，但本報告所整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，但目前**沒有臨床試驗與文獻**支持，僅屬於模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pemigatinib 屬於 FGFR1-3 選擇性抑制劑（激酶抑制劑類別），透過阻斷 FGFR 訊號傳遞來抑制腫瘤生長。

多發性內分泌腫瘤 (MEN) 主要由 MEN1 功能喪失突變與 RET 活化突變所驅動。目前整理的資料中，並未確立 FGFR 路徑與 MEN 之間的直接關聯。因此，這個預測目前僅是計算層面的推論，機轉上的合理性有待進一步驗證。

TxGNN 分數雖然很高（99.71%），但高分不等於有臨床證據，仍需實際研究佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67328 | PEMAZYRE TABLETS 13.5MG | 錠劑 | 資料未載明 |
| HK-67329 | PEMAZYRE TABLETS 4.5MG | 錠劑 | 資料未載明 |
| HK-67330 | PEMAZYRE TABLETS 9MG | 錠劑 | 資料未載明 |

三張許可證均由 Innovent Biologics (HK) Limited 持有，皆為單方製劑，狀態有效。

---

## 細胞毒性

Pemigatinib 為抗腫瘤的標靶藥物（FGFR 抑制劑），非傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（FGFR 激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單 |
| 處置防護 | 請參考原廠仿單 |

請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：已查詢到 50 筆交互作用，以下列出部分主要項目：
  - **嚴重 (Major)**：Aprepitant、Dexamethasone、Clarithromycin、Cobicistat、Lumacaftor、Chloramphenicol、Erythromycin、Ketoconazole、Fluconazole
  - **中度 (Moderate)**：Cimetidine、Metreleptin、Clotrimazole、Glycerol phenylbutyrate、Troglitazone、Deferasirox、Ivacaftor、Zafirlukast、Griseofulvin、Elagolix、Osilodrostat

  多數嚴重交互作用涉及 CYP3A4 抑制劑或誘導劑，併用時需特別留意。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的新適應症（多發性內分泌腫瘤）目前沒有任何臨床試驗或文獻支持，證據等級僅為 L5。
- FGFR 抑制與 MEN 的致病機轉（MEN1、RET）之間缺乏已知的直接連結，高 TxGNN 分數可能只是知識圖譜的推論結果。

**若要推進需要：**
- 補齊 Pemigatinib 的作用機轉資料與香港核准適應症
- 取得香港仿單的警語與禁忌症資料
- 進行 FGFR 路徑與 MEN 相關的機轉文獻回顧或前臨床研究
- 若機轉獲得支持，再評估是否設計早期臨床試驗

---

**補充說明：** 其他排名較前的預測（閉經、HER2 陽性乳癌、巨細胞病毒感染、肌萎縮性脊隨側索硬化症等）同樣缺乏臨床試驗證據，皆為 L5 與 Hold。其中 HER2 陽性乳癌因 FGFR 訊號與 HER2 標靶治療抗藥性有關，具有相對合理的生物學假說，但目前僅有一篇一般性激酶抑制劑綜述（Roskoski, *Pharmacol Res*, 2021, [PMID 33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/)），並無該適應症的直接證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

