---
layout: default
title: Natamycin
parent: 僅模型預測 (L5)
nav_order: 600
evidence_level: L5
indication_count: 5
---

# Natamycin
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

# Natamycin：預測用於外陰陰道念珠菌症

## 一句話總結

Natamycin 是多烯類抗黴菌藥。香港登記的產品為眼用懸液劑（NATACYN 5%），但資料中未載明核准適應症。
TxGNN 模型預測它可能對**外陰陰道念珠菌症 (Vulvovaginal Candidiasis)** 有效，
目前有 **1 個已完成的 Phase 3 試驗**和 **20 篇文獻**支持這個方向。該試驗使用的是 natamycin 加乳果糖的複方栓劑。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 外陰陰道念珠菌症 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2（已完成的 Phase 3 RCT 僅 1 個，且為複方製劑；資料包原標 L1，依判定規則下修） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Natamycin 與細胞膜上的麥角固醇（ergosterol）結合，破壞黴菌細胞膜，因此對念珠菌有活性。DrugBank 目前缺乏詳細的作用機轉資料，以上機轉來自一般藥理知識與本次證據整理。念珠菌感染的病原就是黴菌，機轉與外陰陰道念珠菌症直接吻合。

Natamycin 吸收很差，只適合局部使用，這與陰道栓劑、錠劑的用法相符。多個市場早已將 natamycin 用於陰道念珠菌症，所以這個預測比較像是**標示外或資料涵蓋不足的缺口**，而不是真正的新用途。在香港推進之前，必須先確認本地法規狀態。

另有一個重點：香港目前登記的產品是**眼用懸液劑**，給藥途徑與陰道製劑不同。若要用於陰道，需要另外的陰道劑型，不能直接沿用現有產品。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | 完成 | 218 | 比較 natamycin 100 mg + 乳果糖 300 mg 陰道栓劑、Pimafucin（單方 natamycin 100 mg 栓劑）與乳果糖單方，用於非懷孕成年女性的外陰陰道念珠菌症。試驗目標為證明複方的優越性，並評估其安全性。目前資料看不到主要終點與結果，需要另行查證 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT | BMC Women's Health | 評估 natamycin + 乳果糖陰道栓劑用於成年女性外陰陰道念珠菌症的療效與安全性（與上述 Phase 3 試驗對應，摘要未含結果數據） |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | 對照臨床試驗 | Medical Journal of Australia | 比較 natamycin 與 amphotericin B 陰道栓劑治療陰道念珠菌症（無摘要） |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | 臨床研究 | Acta Obstet Gynecol Scand | 33 位患者使用 natamycin 陰道錠 10 天。伴侶用藥組治癒率 94%，安慰劑組 88%，差異不顯著 |
| [159686](https://pubmed.ncbi.nlm.nih.gov/159686/) | 1979 | 對照臨床試驗 | Aust N Z J Obstet Gynaecol | 120 位念珠菌外陰陰道炎患者。natamycin 加 Elase 酵素，比單用 natamycin 更能改善症狀並清除菌體 |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | 臨床研究 | N Z Med J | 50 位患者使用 natamycin 陰道錠 10 天，2 週治癒率 76%，4 週維持 |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | 綜述 | Ceska Gynekologie | 比較 natamycin 與 clotrimazole 治療慢性陰道黴菌感染，並探討最佳診斷方式 |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | 臨床報告 | Zentralblatt fur Gynakologie | 口服 metronidazole 加陰道 natamycin 錠。念珠菌陰道黴菌症首療程臨床治癒率 89% |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | 問卷調查 | Ceska a Slovenska Farmacie | 烏克蘭利維夫 408 位女性的外陰陰道念珠菌症處置調查，終生盛行率 72.6% |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | 製劑／體外研究 | J Pharm Sci | natamycin 與 γ-環糊精複合物的陰道黏附錠，MIC90 低於 0.0313 μg/mL |
| [5314287](https://pubmed.ncbi.nlm.nih.gov/5314287/) | 1971 | 臨床報告 | Polski Tygodnik Lekarski | pimaricin（natamycin）用於酵母樣真菌引起的外陰陰道炎（無摘要） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41714 | NATACYN OPHTHALMIC SUSPENSION 5%（廠商：LINK HEALTHCARE HONG KONG LIMITED） | 眼用懸液劑（依品名判斷） | 資料未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 作用機轉明確（麥角固醇結合），且已有 1 個完成的 Phase 3 RCT（n=218）與多篇歷史臨床研究支持陰道念珠菌症。
- 但 Phase 3 試驗測的是 natamycin 加乳果糖的複方，無法把療效單獨歸給 natamycin。香港現有產品是眼用劑型，途徑不符。這個方向也可能只是各國早已使用的既有適應症。

**若要推進需要：**
- 取得 NCT06411314 與 PMID 39979898 的主要終點與結果，確認複方相對於單方 natamycin（Pimafucin）的優勢。
- 確認 natamycin 陰道製劑在香港的法規狀態，以及是否需要新的陰道劑型登記。
- 下載並解析香港衛生署仿單，補足警語與禁忌症，這是進入安全性篩選前的必要資料。
- 補齊 DrugBank 的作用機轉資料。
- 適應症範圍只限於已確認為念珠菌的感染。

**其他預測適應症的處置：**
- 念珠菌症（廣義）與外陰陰道炎：列為研究問題。目前只有陰道亞型有 Phase 3 證據，需限定為經確認的念珠菌感染。
- 外陰炎：列為研究問題。沒有試驗單獨以外陰炎為終點，高分可能只是與陰道念珠菌症重疊。
- 滴蟲性外陰陰道炎：**Hold**。Natamycin 的機轉不適用於原蟲，現有 1959–1972 年的報告多為與 metronidazole 併用，療效可能來自併用藥或合併的念珠菌感染。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

