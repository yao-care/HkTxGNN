---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 7
monitor_inn: "BENZYLPENICILLIN"
predicted_indications: ["pericoronitis", "gingival recession", "canker sore", "ulcerative stomatitis", "chemotherapy-induced oral mucositis", "denture stomatitis", "leukoplakia of gingiva"]
last_modified_at: 2026-10-28
description: "Benzylpenicillin：預測新適應症為智齒冠周炎 (pericoronitis)（證據等級 L5）。香港藥劑製品註冊：3 張（有效 3 張）"
---

# Benzylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Benzylpenicillin：青黴素類抗生素（抑制細菌細胞壁合成）→ 智齒冠周炎 (pericoronitis)
{: .text-alpha }

## 一句話總結

Benzylpenicillin（青黴素 G）是青黴素類抗生素，香港已有注射劑型上市。
TxGNN 模型預測它可能對**智齒冠周炎 (pericoronitis)** 有效，但目前**沒有臨床試驗和文獻**直接支持，僅屬模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 智齒冠周炎 (pericoronitis) |
| TxGNN 預測分數 | 0.9936 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Benzylpenicillin 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「青黴素類會與血清蛋白（主要為白蛋白）結合。在正常情況下，青黴素類在細胞外液及大多數其他身體組織中很容易達到治療濃度。青黴素類會以不同程度分布至胸膜液、心包液、腹膜液、腹水、滑液及間質液中。」英文原文："Penicillins bind to serum proteins, mainly albumin. Therapeutic levels of the penicillins are easily achieved under normal circumstances in extracellular fluid and most other body tissues. Penicillins are distributed in varying degrees into pleural, pericardial, peritoneal, ascitic, synovial, and interstitial fluids."（[DailyMed: Pfizerpen (penicillin g potassium) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efef4846-9497-41af-8dd6-518f86eca7f2)，版本日期 2026-11-04；查閱日期 2026-11-19）。就藥物類別而言，Benzylpenicillin 屬青黴素類抗生素，一般認為透過抑制細菌細胞壁合成而發揮殺菌作用。

智齒冠周炎是由鏈球菌與厭氧菌等多種細菌引起的牙源性感染，這些菌種多半對青黴素敏感，因此在機轉上有合理的推測空間。

不過，此預測目前僅來自模型分數，沒有任何試驗或文獻佐證。牙源性感染通常使用口服青黴素（如 penicillin V、amoxicillin），注射型 Benzylpenicillin 可能只在較嚴重的情況下才有意義。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43500 | PAN-PENICILLIN G SOD FOR INJ 1M IU | 注射劑 | 本地資料未記錄 |
| HK-60173 | NORAPENY FOR IM/IV INJ 1000000IU | 注射劑 | 本地資料未記錄 |
| HK-68195 | PENICILLIN G SODIUM SANDOZ POWDER FOR SOLUTION FOR INJECTION/INFUSION 1000000IU | 注射劑 | 本地資料未記錄 |

## 安全性考量

- **藥物交互作用**：已查得 21 筆交互作用紀錄，其中較重要者：
  - **Methotrexate**：嚴重（Major）等級，合併使用需特別謹慎。
  - 中度（Moderate）：Warfarin、Dicoumarol、Doxycycline、Minocycline、Tetracycline、Chloramphenicol、Ethinylestradiol、Mycophenolic acid 等。
  - 輕度（Minor）：Clarithromycin、Erythromycin。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數，沒有直接研究智齒冠周炎的臨床試驗或文獻，證據等級為 L5。
- 牙源性感染已有常規口服抗生素可用，注射型 Benzylpenicillin 的新增價值尚不明確。

**若要推進需要：**
- 搜尋並確認 Benzylpenicillin 用於冠周炎的臨床研究或文獻
- 補充詳細作用機轉資料
- 取得香港仿單的警語與禁忌症
- 釐清注射途徑對冠周炎的適用情境，並與現有口服標準治療比較

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Pfizerpen (penicillin g potassium) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efef4846-9497-41af-8dd6-518f86eca7f2) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

