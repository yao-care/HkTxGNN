---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 559
evidence_level: L5
indication_count: 8
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-11-24
description: "Meloxicam：預測新適應症為肢中發育不良，Hunter-Thompson 型（證據等級 L5）。原適應症：香港許可證資料中未載明核准適應症文字"
---

# Meloxicam
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

## Meloxicam：從關節炎類疾病到 Hunter-Thompson 型肢中發育不良
{: .text-alpha }

## 一句話總結

Meloxicam 是一種 COX-2 偏好性的非類固醇消炎止痛藥（NSAID），知識圖譜中記錄的使用方向為類風濕性關節炎、骨關節炎等關節疾病。
TxGNN 模型預測它可能對**肢中發育不良，Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料中未載明核准適應症文字；知識圖譜中記錄的關聯為類風濕性關節炎、骨關節炎、幼年型特發性關節炎、脊椎關節病等 |
| 預測新適應症 | 肢中發育不良，Hunter-Thompson 型 |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 27 張／共 29 張） |
| 許可證數 | 29 張（有效 27 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Meloxicam 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Meloxicam具有止痛、抗發炎及退燒特性。Zybic™的作用機轉與其他NSAIDs相同，尚未完全明瞭，但涉及抑制環氧化酶（COX-1及COX-2）。」英文原文："Meloxicam has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of Zybic™, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)."（[DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec)，版本日期 2026-09-25；查閱日期 2026-11-19）。Meloxicam 屬於 COX-2 偏好性 NSAID，一般認為是透過降低前列腺素合成來發揮消炎與止痛作用，此為藥物類別的一般知識，並非本次彙整資料所提供。

Hunter-Thompson 型肢中發育不良是罕見的骨骼發育異常，已知與 CDMP1/GDF5 功能喪失變異有關，會影響軟骨生成中的 BMP 訊號傳遞。COX-2 抑制不會矯正這種發育缺陷，因此機轉上缺乏合理連結。

高分預測來自 TxGNN 模型（深度學習），可能反映模型從關節、骨骼表型相關疾病之間學到的相似性，而非生物學證據。若有任何益處，最多是緩解關節疼痛的症狀性效果，且尚無資料證實。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 29 張含本藥成分的許可證（有效 27 張、已註銷 2 張；皆為單一成分），資料中未提供劑型與核准適應症文字。以下列出其中 5 張主要許可證：

<!-- review:begin hk-lic-20261117-meloxicam-1 -->

> **查核更正（2026-11-17）**：原文為「本次彙整的清單列出 20 張有效的單一成分許可證，實際張數可能更多。」。已更正：HK-64633、HK-64473 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。 已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 29 張含本藥成分的許可證（有效 27 張、已註銷 2 張；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-meloxicam-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-41788 | MOBIC TAB 7.5MG | 單一成分 | BOEHRINGER INGELHEIM (HK) LTD | 有效 |
| HK-41789 | MOBIC TAB 15MG | 單一成分 | BOEHRINGER INGELHEIM (HK) LTD | 有效 |
| HK-54749 | APO-MELOXICAM TAB 7.5MG | 單一成分 | HIND WING CO LTD | 有效 |
| HK-54750 | APO-MELOXICAM TAB 15MG | 單一成分 | HIND WING CO LTD | 有效 |
| HK-53980 | MOXIC FORTE TAB 15MG | 單一成分 | HANG LUNG TRADING (H.K.) CO | 有效 |

上表列出其中 5 張（共 29 張）。

<!-- licenses:end -->

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：高血壓、充血性心衰竭、心肌梗塞、腦中風與腦血管疾病、心血管疾病、腎臟疾病與腎功能不全、活動性消化性潰瘍、胃炎、凝血疾病、貧血、糖尿病、高血脂等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Hydrocortisone、Dexamethasone、Triamcinolone、Betamethasone、Budesonide 等皮質類固醇；Acetylsalicylic acid；Metformin；Glimepiride、Chlorpropamide；Mesalazine、Balsalazide；Vancomycin、Kanamycin
  - 輕度：Linaclotide

詳細警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有臨床試驗或文獻佐證，且 COX-2 抑制與 GDF5/BMP 訊號缺陷之間缺乏機轉連結。
- 該疾病為罕見遺傳性骨骼發育異常，NSAID 最多只可能緩解症狀，不會改變疾病進程。

**若要推進需要：**
- 補充 meloxicam 的作用機轉資料
- 系統性搜尋該疾病與 NSAID 的相關病例報告或研究
- 取得香港仿單的警語與禁忌資料，進行安全性評估
- 如仍有臨床興趣，先釐清目標是症狀控制（如關節疼痛）還是疾病修飾

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本次彙整的清單列出 20 張有效的單一成分許可證，實際張數可能更多。」→「香港共有 29 張含本藥成分的許可證（有效 27 張、已註銷」 | 更正（2026-11-17 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

