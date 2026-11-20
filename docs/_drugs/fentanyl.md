---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Fentanyl：預測新適應症為腎因性抗利尿激素不適當分泌症候群 (NSIAD)（證據等級 L5）。原適應症：目前許可證資料未載明核准適應症"
monitor_inn: "FENTANYL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
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

## Fentanyl：從疼痛處置到腎因性抗利尿激素不適當分泌症候群
{: .text-alpha }

## 一句話總結

Fentanyl 是強效的 mu 類鴉片受體促效劑，在香港以貼片、口頰錠及注射劑型上市。
TxGNN 模型預測它可能對**腎因性抗利尿激素不適當分泌症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料未載明核准適應症 |
| 預測新適應症 | 腎因性抗利尿激素不適當分泌症候群 (NSIAD) |
| TxGNN 預測分數 | 0.9946 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 16 張／共 19 張） |
| 許可證數 | 19 張（有效 16 張） |
| 建議決策 | Hold |

另一個預測適應症為**妥瑞症 (Tourette syndrome)**，TxGNN 分數 0.9905，同樣無臨床試驗與文獻支持，證據等級 L5，建議 Hold（見下文說明）。

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Fentanyl 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「枸櫞酸芬太尼注射液（Fentanyl Citrate Injection）是一種類鴉片促效劑，其具治療價值的主要作用為鎮痛及鎮靜。」英文原文："Fentanyl Citrate Injection is an opioid agonist, whose principal actions of therapeutic value are analgesia and sedation."（[DailyMed: fentanyl citrate prescribing information, Phlow Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=58dcd3f7-e3d8-4929-a186-8f680a51ff11)，版本日期 2026-10-23；查閱日期 2026-11-19）。Fentanyl 是 mu 類鴉片受體促效劑，臨床上用於疼痛處置，但本報告所用資料未載明其原適應症與完整機轉。

就 NSIAD 而言，目前**找不到可信的機轉連結**。NSIAD 是由血管加壓素 V2 受體 (AVPR2) 的功能獲得性突變所致，即使血中血管加壓素偵測不到，仍會出現水分滯留與低血鈉。鴉片類藥物可能調節血管加壓素的釋放，也可能造成類似 SIADH 的效應，但那是中樞性、依賴血管加壓素的機制，無法解決 V2 受體持續活化的問題。

因此，高分預測應視為純計算結果。Fentanyl 相關的低血鈉或抗利尿作用，反而比較像安全性疑慮，而非治療依據。

**關於妥瑞症：** 理論上僅有薄弱、間接的依據。妥瑞症涉及皮質-紋狀體-視丘-皮質迴路與多巴胺過度活躍，鴉片系統確實會調節紋狀體多巴胺，也有小規模個案層級的報告探討鴉片類拮抗劑或部分促效劑（如 buprenorphine）。但這不能類推到 fentanyl：它是強效完全促效劑，具高濫用風險與呼吸抑制風險，且有 100 筆藥物交互作用紀錄。對於慢性、常見於兒童的疾病，風險效益並不理想，而替代選擇（alpha-2 促效劑、抗精神病藥、CBIT 行為治療）已經存在。

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
| HK-53755 | DUROGESIC TRANSDERMAL PATCH 25MCG/H | 貼片（依品名） | 資料未載明 |
| HK-53753 | DUROGESIC TRANSDERMAL PATCH 50MCG/H | 貼片（依品名） | 資料未載明 |
| HK-53883 | DUROGESIC TRANSDERMAL PATCH 12MCG/H | 貼片（依品名） | 資料未載明 |
| HK-64078 | FENTORA BUCCAL TABLETS 200MCG | 口頰錠（依品名） | 資料未載明 |
| HK-67174 | APT-FENTANYL CITRATE SOLUTION FOR INJECTION OR INFUSION 0.5MG/10ML | 注射液（依品名） | 資料未載明 |

香港共有 19 張許可證，皆為單一成分製劑（16 張有效；HK-53755、HK-53753、HK-53883 已註銷），以上僅列出 5 張主要許可證。

<!-- review:begin hk-lic-20261117-fentanyl-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 14 張有效許可證，皆為單一成分製劑，」。已更正：HK-53755、HK-53753、HK-53883 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。 已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69005、HK-69006、HK-69031、HK-69032、HK-69209 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-fentanyl-1 -->

---

## 細胞毒性

Fentanyl 非抗腫瘤藥物，本章節不適用。

---

## 安全性考量

- **藥物交互作用**：共記錄 100 筆交互作用。其中列為「Major（嚴重）」的包括 Alvimopan、Aprepitant、Bupropion、Clarithromycin、Clotrimazole、Dexamethasone、Dolasetron、Fenfluramine、Granisetron、Lorcaserin 等；「Moderate（中度）」的包括 Atropine、Cimetidine、Dicyclomine、Glycopyrronium、Hyoscyamine 等。此外，與中樞神經抑制劑及 CYP3A4 抑制劑併用需特別留意。
- **知識圖譜中的禁忌疾病關聯**（來自模型知識圖譜，並非仿單內容）：包括低血壓、直立性低血壓、長 QT 症候群、尖端扭轉型心室頻脈、肝衰竭與肝臟疾病、腎臟疾病、慢性阻塞性肺病、氣喘、胰臟炎、膽囊疾病、發炎性腸道疾病、良性前列腺增生、物質濫用/依賴等。
- **其他疑慮**：Fentanyl 具高濫用風險與呼吸抑制風險。若用於 NSIAD，其可能引起的抗利尿或低血鈉效應也需視為安全隱憂。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症（NSIAD 與妥瑞症）皆無臨床試驗與文獻支持，僅有模型分數，屬 L5 證據。
- NSIAD 缺乏可信的機轉連結；妥瑞症的機轉依據薄弱，且 fentanyl 的風險效益對慢性病況不利，現有替代療法已足夠。

**若要推進需要：**
- 取得香港衛生署仿單的警語、禁忌與核准適應症，補足安全性篩選所需資料
- 補充 fentanyl 詳細的作用機轉資料
- 針對 NSIAD 與妥瑞症進行系統性文獻回顧，確認是否存在任何機轉或臨床訊號
- 若仍有意推進，需先有前臨床或機轉研究證據，並規劃嚴格的風險管理（呼吸抑制、濫用、交互作用）

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 14 張有效許可證，皆為單一成分製劑，」→「香港共有 19 張許可證，皆為單一成分製劑（16 張有效；HK-53755、HK」 | 更正（2026-11-17 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: fentanyl citrate prescribing information, Phlow Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=58dcd3f7-e3d8-4929-a186-8f680a51ff11) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

