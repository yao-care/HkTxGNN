---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 9
monitor_inn: "KETOPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
last_modified_at: 2026-10-30
description: "Ketoprofen：預測新適應症為肢端中段發育不良 Hunter-Thompson 型（證據等級 L5）。原適應症：知識圖譜中記錄的關聯：類風濕性關節炎、骨關節炎、關節病變"
---

# Ketoprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Ketoprofen：從類風濕性關節炎與骨關節炎到 Hunter-Thompson 型肢中發育不良
{: .text-alpha }

## 一句話總結

Ketoprofen 是一種非類固醇抗發炎藥（NSAID），知識圖譜中記錄的相關疾病包括類風濕性關節炎、骨關節炎與關節病變。
TxGNN 模型預測它可能對**肢端中段發育不良 Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅為模型運算結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯：類風濕性關節炎、骨關節炎、關節病變（香港許可證資料未提供核准適應症文字） |
| 預測新適應症 | 肢端中段發育不良 Hunter-Thompson 型 |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ketoprofen 一般被認為是非選擇性 COX 抑制劑，可減少前列腺素合成而產生止痛與消炎作用，但這一點在本報告所整理的資料中並未提供。

Hunter-Thompson 型肢端中段發育不良是由 CDMP1/GDF5 功能喪失所致的遺傳性骨骼發育異常，核心問題在於發育訊息傳遞缺陷。COX 抑制與 GDF5/BMP 路徑之間看不出明確的機轉關聯，最多只能考慮作為關節疼痛的症狀緩解。

因此，高分較可能來自 TxGNN 模型（深度學習）所學到的相關疾病之間的相似性，而非生物學證據，也非實際的治療機轉。這個預測不應視為有療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下表為所列出的 5 張許可證（總數至少 20 張，清單可能不完整）。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68597 | HOHOTAPE MEDICAL PLASTER 30MG | 貼布（依品名） | 未提供 |
| HK-57684 | KETO-TDDS PLASTER 30MG | 貼布（依品名） | 未提供 |
| HK-62603 | DERUMA-60 CATAPLASMA PLASTER 60MG | 貼布（依品名） | 未提供 |
| HK-18544 | KETOFEN CAP 50MG | 膠囊（依品名） | 未提供 |
| HK-59428 | KETOFEN GEL 2.5% | 凝膠（依品名） | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：高血壓、肝衰竭、腎臟疾病、消化性潰瘍（含活動性）、凝血疾病、心肌梗塞、冠狀動脈血栓、血紅素病變、心血管疾病、心臟病等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：阿斯匹靈 (Acetylsalicylic acid)、氫皮質酮 (Hydrocortisone)、地塞米松 (Dexamethasone)、倍他米松 (Betamethasone)、布地奈德 (Budesonide)、曲安奈德 (Triamcinolone)、二甲雙胍 (Metformin)、格列美脲 (Glimepiride)、氯磺丙脲 (Chlorpropamide)、美沙拉秦 (Mesalazine)、納曲酮 (Naltrexone)
  - 輕度：法莫替丁 (Famotidine)、雷尼替丁 (Ranitidine)、西咪替丁 (Cimetidine)、利那洛肽 (Linaclotide)

其餘警語請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測，沒有任何直接針對此疾病的臨床試驗或文獻，證據等級為 L5。
- 該疾病為 GDF5 功能喪失的發育性遺傳疾病，COX 抑制缺乏合理的疾病修飾機轉，最多僅能緩解症狀。

**若要推進需要：**
- 補齊 Ketoprofen 的作用機轉資料，並評估與 GDF5/BMP 路徑是否有任何關聯。
- 取得香港仿單的警語與禁忌症資料（目前缺口屬阻擋性）。
- 若仍有興趣，可先進行文獻回顧與前臨床研究，確認是否有疾病相關證據。
- 在同樣的預測清單中，可優先評估機轉較合理的候選，例如 LACC1 缺陷所致的幼年型關節炎（仍僅限於症狀緩解，且需考量兒童用藥安全）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

