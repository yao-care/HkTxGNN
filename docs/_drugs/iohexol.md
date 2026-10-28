---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 478
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "Iohexol"
predicted_indications: ["insomnia (disease)", "anxiety"]
description: "Iohexol：預測新適應症為失眠 (insomnia (disease)) (insomnia (disease))（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Iohexol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Iohexol: 失眠 (insomnia (disease)) (insomnia (disease))
{: .text-alpha }

## 一句話總結

Iohexol 是一種非離子型含碘 X 光造影劑，在香港以 OMNIPAQUE 注射液上市。
TxGNN 模型（深度學習）預測它可能對**失眠 (Insomnia)** 有效，但目前**沒有任何臨床試驗與文獻**支持，屬於純模型預測。此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 失眠 (insomnia (disease)) (insomnia (disease)) |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Iohexol 是非離子型含碘放射造影劑，本身在生物學上呈惰性，其用途是診斷影像，而非治療疾病。

Iohexol 對調控睡眠的路徑（GABA 能、食慾素、褪黑激素系統）沒有已知作用。TxGNN 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。因此，這項預測在機轉上**並不合理**。

其他排名靠前的預測（焦慮症）同樣缺乏機轉依據，並有同樣的限制。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對失眠的預測，目前無相關文獻。

作為參考，排名第 2 的預測「焦慮」有 4 篇檢索到的文獻，但內容均為 Iohexol 的使用情境或不良反應，並非抗焦慮療效證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | 比較 iodixanol 與 iohexol 於四肢靜脈攝影的療效、安全性與注射不適感 |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | 世代研究 | Neuroradiology | 200 名腰椎脊髓攝影患者的副作用（頭痛、噁心、輕微精神症狀）分析 |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | 臨床生理研究 | Acta Neurochirurgica | 腦血管攝影期間以經顱都卜勒監測血流動力學 |
| [39861464](https://pubmed.ncbi.nlm.nih.gov/39861464/) | 2025 | 回顧性觀察研究 | Nutrients | 腫瘤腎臟病患者營養與運動的益處，與 Iohexol 治療焦慮無直接關係 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44111 | OMNIPAQUE INJ 350MGI/ML | 注射劑 | 資料未載明 |
| HK-44112 | OMNIPAQUE INJ 300MGI/ML | 注射劑 | 資料未載明 |

兩張許可證均為單一成分、有效狀態，持有者為 GE Medical Systems Hong Kong Limited。

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下為部分列為「嚴重 (Major)」者：
  - Metformin
  - Amphotericin B
  - Vancomycin
  - Kanamycin
  - Neomycin
  - Levofloxacin
  - Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone 等皮質類固醇
  - Morphine
  - Metoclopramide
  - Bupropion
  - Mesalazine
  
  另有 Mannitol 為中度 (Moderate)。

- **文獻中的安全訊號**：有病例報告指出，低劑量口服 methotrexate 的患者重複注射含碘造影劑後，曾發生致命的多器官功能障礙。另有造影劑過敏與脫敏處置的病例報告。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗，文獻也僅涉及診斷影像或不良反應，沒有治療證據。Iohexol 是生物惰性的造影劑，沒有可信的治療機轉。

**若要推進需要：**
- 取得 Iohexol 的作用機轉資料，並確認原適應症的許可證文字。
- 取得香港仿單的警語與禁忌症資料。
- 若仍要探討，需先有前臨床證據顯示任何治療相關的生物活性；在此之前不建議投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

