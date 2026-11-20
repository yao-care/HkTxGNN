---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 476
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Interferon Beta-1B：預測新適應症為毛細胞白血病 (Hairy Cell Leukemia)（證據等級 L5）。原適應症：復發緩解型多發性硬化症 (Relapsing-Remitting Multiple Sclerosis)"
monitor_inn: "INTERFERON BETA-1B"
predicted_indications: ["hairy cell leukemia", "autoimmune disease of central nervous system"]
---

# Interferon Beta-1B
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

## Interferon beta-1b：從復發緩解型多發性硬化症到毛細胞白血病
{: .text-alpha }

## 一句話總結

Interferon beta-1b 原本用於治療復發緩解型多發性硬化症 (RRMS)。
TxGNN 模型預測它可能對**毛細胞白血病 (Hairy Cell Leukemia)** 有效，預測分數很高。
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，只有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 復發緩解型多發性硬化症 (Relapsing-Remitting Multiple Sclerosis) |
| 預測新適應症 | 毛細胞白血病 (Hairy Cell Leukemia) |
| TxGNN 預測分數 | 0.9916 |
| 證據等級 | L5 |
| 香港上市 | 未上市（已註銷許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 0 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Interferon Beta-1B 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「BETASERON（干擾素β-1b）在多發性硬化症患者中的作用機制未明。」英文原文："The mechanism of action of BETASERON (interferon beta-1b) in patients with multiple sclerosis is unknown."（[DailyMed: Betaseron (interferon beta-1b) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5)，版本日期 2026-03-03；查閱日期 2026-11-19）。根據已知資訊，Interferon beta-1b 屬於第 I 型干擾素類別，其成分在多發性硬化症中的免疫調節作用已被臨床證實，機轉上可能適用於毛細胞白血病。

另一個干擾素，Interferon alpha，過去曾用於治療毛細胞白血病。第 I 型干擾素都透過 IFNAR 受體傳遞訊號，可能對惡性 B 細胞有抗增生和免疫調節作用。因此模型給出高分，在生物學上並非毫無根據。

但這只是**類別層級的推論**。根據美國 FDA 核准的 Interferon Beta-1B 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「BETASERON（干擾素β-1b）在多發性硬化症患者中的作用機制未明。」英文原文："The mechanism of action of BETASERON (interferon beta-1b) in patients with multiple sclerosis is unknown."（[DailyMed: Betaseron (interferon beta-1b) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5)，版本日期 2026-03-03；查閱日期 2026-11-20）。這個預測目前只能視為假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 | 狀態 |
|---------|------|--------|------|
| HK-47987 | BETAFERON PRE-FILLED SYRINGE 8MIU | BAYER HEALTHCARE LIMITED | 已註銷（單一成分） |

<!-- review:begin hk-row-20261117-interferon_beta-1b-1 -->

> **查核更正（2026-11-17）**：原文為「BAYER HEALTHCARE LIMITED／有效（單一成分）」。已更正：HK-47987 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-row-20261117-interferon_beta-1b-1 -->

本報告所整理的資料未提供此許可證的劑型與核准適應症文字。

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為已列出的部分：
  - **重大 (Major)**：Bupropion
  - **中度 (Moderate)**：Acarbose、Pioglitazone、Rosiglitazone、Clarithromycin、Levofloxacin、Minocycline、Naltrexone、Rosuvastatin、Simvastatin、Orlistat 等

主要警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高 (0.9916)，但毛細胞白血病這個適應症沒有任何臨床試驗或文獻佐證，證據等級僅為 L5。
- 缺乏作用機轉與仿單安全性資料，目前不足以支持推進。

**若要推進需要：**
- 系統性檢索 Interferon beta 與毛細胞白血病的前臨床和臨床研究。
- 與已有臨床使用歷史的 Interferon alpha 比較，評估 beta 型是否有足夠的活性依據。
- 補齊 Interferon beta-1b 的作用機轉資料。
- 取得香港仿單的警語與禁忌症，完成安全性篩選。
- 與現行毛細胞白血病標準治療比較，評估臨床定位。

**補充說明：**
模型的第二名預測為「中樞神經系統自體免疫疾病」，已有 6 個臨床試驗（含 1 個 Phase 3 BENEFIT 延伸試驗 NCT00185211）。但這個適應症與原有的多發性硬化症高度重疊，主要是確認既有用途，不算真正的藥物再利用。若延伸到其他中樞神經系統自體免疫疾病，例如水通道蛋白-4 (AQP4) 抗體陽性的視神經脊髓炎譜系疾患，Interferon beta 可能無效甚至有害，沒有疾病專屬資料前不應假設可用。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「BAYER HEALTHCARE LIMITED &#124; 有效（單一成分）」→「BAYER HEALTHCARE LIMITED &#124; 已註銷（單一成分）」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Betaseron (interferon beta-1b) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5) |
| 2026-11-20 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Betaseron (interferon beta-1b) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

