---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
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
| 香港上市 | 上市中（有效許可證 14 張／共 14 張） |
| 許可證數 | 14 張（有效 14 張） |
| 建議決策 | Hold |

另一個預測適應症為**妥瑞症 (Tourette syndrome)**，TxGNN 分數 0.9905，同樣無臨床試驗與文獻支持，證據等級 L5，建議 Hold（見下文說明）。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Fentanyl 是 mu 類鴉片受體促效劑，臨床上用於疼痛處置，但本報告所用資料未載明其原適應症與完整機轉。

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

香港共有 14 張有效許可證，皆為單一成分製劑，以上僅列出 5 張主要許可證。

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
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

