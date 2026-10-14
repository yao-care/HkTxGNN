---
layout: default
title: Natamycin
parent: 高證據等級 (L1-L2)
nav_order: 610
evidence_level: L2
indication_count: 5
---

# Natamycin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Natamycin：從黴菌性角膜潰瘍到外陰陰道念珠菌症

## 一句話總結

Natamycin 是多烯類（polyene）抗黴菌藥，原本用於黴菌性角膜潰瘍。
TxGNN 模型預測它可能對**外陰陰道念珠菌症 (Vulvovaginal Candidiasis)** 有效，
目前有 **1 個已完成的 Phase 3 臨床試驗**和 **14 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黴菌性角膜潰瘍 (Mycotic corneal ulcer) |
| 預測新適應症 | 外陰陰道念珠菌症 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：資料中此預測的內建分級為 L1，但依本報告的判定規則（L1 需 ≥2 個已完成的 Phase 3 RCT），目前僅有 1 個已完成的 Phase 3 試驗，且為與乳果糖的複方製劑，故保守評為 L2。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Natamycin 屬於多烯類抗黴菌藥，這類藥物會與黴菌細胞膜上的麥角固醇（ergosterol）結合，破壞細胞膜功能而殺滅黴菌。

念珠菌（Candida）同樣是含麥角固醇的黴菌，因此這個機轉可直接套用到外陰陰道念珠菌症。原適應症（黴菌性角膜炎）與新適應症都是局部黴菌感染，使用的是相同的抗黴菌機轉，改為陰道局部給藥屬於給藥途徑的延伸，而非機轉上的跳躍。

需注意：此機轉推論是根據多烯類藥物的已知特性，而非資料庫中的 Natamycin 專屬 MOA 資料。Natamycin 全身吸收很差，不適用於侵襲性念珠菌感染。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | 完成 | 218 | Natamycin 100 mg + 乳果糖 300 mg 陰道栓劑，對照 Pimafucin（單方 Natamycin）或單方乳果糖，用於非懷孕成年女性的外陰陰道念珠菌症優越性試驗 |

此試驗為複方製劑，無法單獨區分 Natamycin 的貢獻。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT | BMC Women's Health | Natamycin + 乳果糖陰道栓劑用於外陰陰道念珠菌症的療效與安全性（國際、隨機、優越性試驗） |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | RCT | Med J Aust | 比較 Amphotericin B 與 Pimafucin（Natamycin）陰道栓劑治療陰道念珠菌症 |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | 臨床研究 | Acta Obstet Gynecol Scand | 33 位患者使用 Natamycin 陰道錠 10 天；伴侶同時治療者治癒率 94%，使用安慰劑者 88%，差異不顯著 |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | 臨床研究 | N Z Med J | 50 位女性使用 Pimafucin 陰道錠 10 天，2 週治癒率 76%，4 週時維持 |
| [4584444](https://pubmed.ncbi.nlm.nih.gov/4584444/) | 1973 | 臨床研究 | The Practitioner | Natamycin 用於妊娠期陰道念珠菌症 |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Review | Ceska Gynekologie | 比較 Natamycin 與 Clotrimazole 治療陰道酵母菌感染的效果 |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | 製劑／體外研究 | J Pharm Sci | Natamycin-γ環糊精複合物的陰道黏膜附著製劑，MIC90 低於 0.0313 µg/mL |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | 問卷調查 | Ceska Slov Farm | 烏克蘭利維夫 408 位女性的外陰陰道念珠菌症處置調查，終生盛行率 72.6% |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | 臨床研究 | Zentralbl Gynakol | 口服 Metronidazole 合併陰道 Natamycin 錠，陰道念珠菌症首療程臨床治癒率 89% |
| [159686](https://pubmed.ncbi.nlm.nih.gov/159686/) | 1979 | 對照臨床試驗 | Aust N Z J Obstet Gynaecol | 120 位念珠菌外陰陰道炎患者，Elase 加 Natamycin 優於單用 Natamycin |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41714 | NATACYN OPHTHALMIC SUSPENSION 5% | 眼用懸浮液（品名所示） | 資料未載明 |

香港目前僅有眼用劑型（5% 眼用懸浮液，廠商：LINK HEALTHCARE HONG KONG LIMITED），並無陰道用劑型登記。若要用於外陰陰道念珠菌症，需另行評估劑型與註冊。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的 Phase 3 RCT（n=218）與多篇陰道念珠菌症臨床研究，機轉與目標疾病相符。但該試驗為複方製劑，無法單獨確認 Natamycin 的效果。
- 香港現有許可僅限眼用劑型，且缺乏安全性與作用機轉的完整資料。
- 同一份預測中的其他適應症證據較弱：念珠菌症（廣義）與外陰炎、外陰陰道炎僅能由念珠菌亞型間接推論；滴蟲性外陰陰道炎缺乏機轉依據，建議暫緩（Hold），其高分很可能只是反映模型對陰道感染類適應症的網絡鄰近性。

**若要推進需要：**
- 取得並審閱 PMID 39979898 的完整內容，確認對照組設計、主要終點與單方 Natamycin 組的表現
- 補齊 Natamycin 的作用機轉資料（DrugBank）
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩選
- 評估陰道用劑型在香港的註冊途徑與可及性
- 限定使用於經病原確診的念珠菌感染，避免用於細菌性或滴蟲性陰道炎
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

