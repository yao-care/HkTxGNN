---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 674
evidence_level: L5
indication_count: 3
monitor_inn: "PEMETREXED"
predicted_indications: ["pleural adenomatoid tumor", "pericardium cancer", "iminoglycinuria"]
last_modified_at: 2026-10-30
description: "Pemetrexed：預測新適應症為Pleural adenomatoid tumor（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Pemetrexed
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Pemetrexed: Pleural adenomatoid tumor
{: .text-alpha }

## 一句話總結

Pemetrexed 是一種抗葉酸類的化療藥物，知識圖譜中記錄其原適應症為非小細胞肺癌與惡性胸膜間皮瘤。
TxGNN 模型預測它可能對**心包膜癌 (Pericardium Cancer)** 有效，目前**沒有臨床試驗**，僅有 **17 篇文獻**（以病例報告、小型病例系列與一般性間皮瘤回顧為主），且未見直接證明其在心包膜部位療效的研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Pleural adenomatoid tumor |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 17 張／共 17 張） |
| 許可證數 | 17 張（有效 17 張） |
| 建議決策 | Hold（列為研究問題，暫不推進） |

> 說明：本報告以預測排名第 1 的「胸膜腺瘤樣瘤」以外，選擇文獻最完整的「心包膜癌」作為主要討論對象。排名第 1 與第 3 的預測（胸膜腺瘤樣瘤、亞胺基甘胺酸尿症）無任何臨床試驗或文獻，詳見後文「其他預測」。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pemetrexed 屬於抗葉酸類抗代謝藥物，一般認為其作用在於抑制胸苷酸合成酶 (thymidylate synthase)、二氫葉酸還原酶 (DHFR) 與 GARFT 等葉酸依賴酵素，阻斷 DNA 合成。

原發性心包膜間皮瘤在組織學上與惡性胸膜間皮瘤屬於同一類疾病，而知識圖譜中記錄 pemetrexed 與惡性胸膜間皮瘤有關聯（常與鉑類藥物併用），因此從機轉與疾病相似性推論，用於心包膜間皮瘤具有合理性。

不過這是由胸膜間皮瘤外推而來的間接證據。現有文獻多為個案報告，例如以 carboplatin 加 pemetrexed 治療後腫瘤有反應的個案，無法確立療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻皆未直接以前瞻性研究評估 pemetrexed 在心包膜癌的療效。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30594459](https://pubmed.ncbi.nlm.nih.gov/30594459/) | 2019 | Review | Clinical Lung Cancer | 回顧 103 例已發表的原發性心包膜間皮瘤，整理危險因子、治療模式與預後，目前無治療共識 |
| [17936406](https://pubmed.ncbi.nlm.nih.gov/17936406/) | 2008 | Review | Lung Cancer | 一名 44 歲男性接受 carboplatin 加 pemetrexed 後腫瘤有反應，再以放射線鞏固，後續進展 |
| [17762349](https://pubmed.ncbi.nlm.nih.gov/17762349/) | 2007 | 病例報告 | J Thorac Oncol | 心包膜間皮瘤合併肝轉移，對 pemetrexed 加鉑類化療反應良好，無惡化存活期延長 |
| [15955137](https://pubmed.ncbi.nlm.nih.gov/15955137/) | 2005 | Review | Respirology | 惡性胸膜間皮瘤的診斷、評估與處置進展 |
| [18473795](https://pubmed.ncbi.nlm.nih.gov/18473795/) | 2008 | Review | Curr Med Chem | 惡性間皮瘤的分子標的與標靶治療 |
| [22104079](https://pubmed.ncbi.nlm.nih.gov/22104079/) | 2012 | Review | Cancer Treat Rev | 瀰漫性惡性腹膜間皮瘤的治療更新 |
| [26281826](https://pubmed.ncbi.nlm.nih.gov/26281826/) | 2015 | Cohort | Int J Radiat Oncol Biol Phys | 保留肺臟手術後的根治性放射治療用於惡性胸膜間皮瘤的存活與失敗模式 |
| [36602504](https://pubmed.ncbi.nlm.nih.gov/36602504/) | 2022 | 病例報告 | Heart Surg Forum | 以心包切開術確診的原發性惡性心包膜間皮瘤個案 |
| [32787452](https://pubmed.ncbi.nlm.nih.gov/32787452/) | 2020 | 病例報告 | J Investig Med High Impact Case Rep | 以腹部症狀表現的惡性間皮瘤個案 |
| [20035722](https://pubmed.ncbi.nlm.nih.gov/20035722/) | 2010 | 前臨床 | Biochem Biophys Res Commun | 間皮瘤細胞對 capecitabine 抗藥性的表觀遺傳機制；提及標準治療為 pemetrexed 加 cisplatin |

## 香港上市資訊

以下為主要許可證（共 17 張，皆為單一成分製劑，核准適應症文字未於資料中提供），僅列出 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53331 | ALIMTA 注射用濃縮輸注液粉末 500MG（ELI LILLY ASIA, INC.） | 輸注用濃縮液粉末 | 資料未提供 |
| HK-58016 | ALIMTA 注射用濃縮輸注液粉末 100MG（ELI LILLY ASIA, INC.） | 輸注用濃縮液粉末 | 資料未提供 |
| HK-64687 | PEMETREXED 100MG（CHEMILLENNIUM INTERNATIONAL (HK) LIMITED） | 輸注用濃縮液粉末 | 資料未提供 |
| HK-64688 | PEMETREXED 500MG（CHEMILLENNIUM INTERNATIONAL (HK) LIMITED） | 輸注用濃縮液粉末 | 資料未提供 |
| HK-64649 | PEMETREXED SANDOZ 100MG（SANDOZ HONG KONG LIMITED） | 輸注用濃縮液粉末 | 資料未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗葉酸類抗代謝藥物） |
| 骨髓抑制風險 | 知識圖譜記錄的禁忌關聯包含嗜中性白血球低下、血小板低下、顆粒球缺乏症與貧血，顯示骨髓抑制為重要風險 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 全血球計數（含分類）、腎功能、肝功能 |
| 處置防護 | 請參考原廠仿單，並依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單文字）**：腎臟疾病、腎功能不全、血小板低下、嗜中性白血球低下、顆粒球缺乏症、貧血、巨球性貧血、輸尿管積膿。
- **藥物交互作用**：資料庫共記錄 100 筆，顯示的項目皆為中度等級，包括：
  - 腎毒性藥物：amphotericin B（含各種劑型）、vancomycin、kanamycin、neomycin、polymyxin B
  - 組織胺 H2 受體阻斷劑：famotidine、ranitidine、cimetidine
  - 其他：metformin、acetylsalicylic acid（阿斯匹靈）、mesalazine、balsalazide、olsalazine、amoxicillin、levofloxacin、sapropterin

  本藥經腎臟排除，併用腎毒性藥物或影響腎小管分泌的藥物時須特別留意。

警語與禁忌的仿單文字目前未取得，請參考原廠仿單。

## 其他預測

- **胸膜腺瘤樣瘤 (Pleural Adenomatoid Tumor)**，分數 0.9999，證據等級 L5，建議 Hold：無臨床試驗與文獻。
- **亞胺基甘胺酸尿症 (Iminoglycinuria)**，分數 0.9997，證據等級 L5，建議 Hold：無臨床試驗與文獻。這是良性遺傳性腎小管轉運異常，非增生性疾病，使用細胞毒性藥物風險效益不佳，應降低優先順序。

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 心包膜癌（主要為原發性心包膜間皮瘤）有機轉上的合理外推，但現有證據只有個案報告、病例系列與一般性回顧，沒有針對此疾病的臨床試驗，亦無文獻直接證明療效。依證據等級規則，證據等級定為 L5。
- 另兩個預測（胸膜腺瘤樣瘤、亞胺基甘胺酸尿症）缺乏機轉依據與證據，不建議推進。

**若要推進需要：**
- 取得 pemetrexed 完整的作用機轉資料
- 取得香港仿單的警語、禁忌與核准適應症文字
- 系統性蒐集心包膜間皮瘤使用 pemetrexed 加鉑類的病例，評估反應率與存活期
- 評估設計罕見疾病的前瞻性研究或登錄研究的可行性
- 針對腎功能不全與血球低下族群建立安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

