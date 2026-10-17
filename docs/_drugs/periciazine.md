---
layout: default
title: Periciazine
parent: 僅模型預測 (L5)
nav_order: 683
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Periciazine：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：本報告資料中未載明"
monitor_inn: "periciazine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "dysthymic disorder", "migraine with or without aura, susceptibility to", "ulerythema ophryogenesis"]
---

# Periciazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Periciazine：從精神病相關行為障礙到偏頭痛

## 一句話總結

Periciazine（pericyazine）是一種吩噻嗪（phenothiazine）類抗精神病藥物，香港已核准上市，但本報告所編列的資料中沒有記載其核准適應症文字。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告資料中未載明（香港許可證未附適應症文字） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，periciazine 屬於吩噻嗪類抗精神病藥，藥理上具有多巴胺 D2 受體拮抗作用，並兼具抗組織胺、抗膽鹼與 α 腎上腺素受體阻斷活性。藥理資料另顯示其與多巴胺 D1 受體（DRD1）有關聯，但該資料也註明尚無經同儕審查的資料可確認其主要分子標靶。

在英國，該藥獲准用於思覺失調症或其他精神病，以及嚴重焦慮、精神運動性激動和危險衝動行為的短期輔助治療。

同屬吩噻嗪類的藥物（如 chlorpromazine、prochlorperazine）已被用於急性偏頭痛及偏頭痛相關噁心，因此以藥物類別推論，機轉上有合理性。不過，這只是類別層面的推論，並無 periciazine 本身的臨床資料。0.9989 的高分是計算預測，很可能受類別相似性驅動，不應視為獨立證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56693 | VICK-PERICYAZINE TAB 10MG | 未載明（品名為錠劑） | 未載明 |
| HK-56692 | VICK-PERICYAZINE TAB 2.5MG | 未載明（品名為錠劑） | 未載明 |

兩張許可證皆為單一成分、狀態有效，持有廠商為 VICKMANS LABORATORIES LTD。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他排名較後的預測

| 排名 | 預測疾病 | TxGNN 分數 | 評估 |
|------|---------|-----------|------|
| 2 | 腦幹先兆偏頭痛 | 99.84% | 為偏頭痛亞型，分數可能來自與上層偏頭痛節點的重疊，並非獨立證據 |
| 3 | 蠕蟲狀皮膚萎縮 (Atrophoderma vermiculata) | 99.36% | 無合理機轉關聯，可能是知識圖譜的假象 |
| 4 | 輕型憂鬱症 (Dysthymic disorder) | 99.25% | 僅有寬鬆的神經精神學推論；鎮靜型吩噻嗪在慢性情緒障礙有耐受性疑慮 |
| 5 | 偏頭痛易感性 | 99.22% | 代表遺傳易感性而非可治療的臨床適應症 |
| 6 | 眉部毛囊萎縮性紅斑 (Ulerythema ophryogenesis) | 99.16% | 無機轉關聯，可能來自圖譜上相近的皮膚疾病節點 |

以上預測皆無臨床試驗或文獻佐證，證據等級均為 L5。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛的預測僅有吩噻嗪類藥物的類別推論支持，沒有 periciazine 專屬的臨床或文獻證據。
- 關鍵資料（原適應症、作用機轉、仿單警語與禁忌）仍有缺口，尚無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補齊作用機轉資料（如查詢 DrugBank）
- 系統性檢索 periciazine 或同類吩噻嗪用於偏頭痛的臨床與文獻證據
- 評估鎮靜、錐體外症狀等類別不良反應在偏頭痛族群的風險效益
- 確認劑型與給藥途徑是否符合偏頭痛（特別是急性期）的治療需求
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

