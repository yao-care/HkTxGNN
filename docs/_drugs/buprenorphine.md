---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Buprenorphine：預測新適應症為急性間歇性紫質症 (Acute Intermittent Porphyria)（證據等級 L5）。原適應症：鴉片類依賴、物質濫用/依賴、嗎啡依賴"
monitor_inn: "BUPRENORPHINE"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorphine：從鴉片類依賴到急性間歇性紫質症

## 一句話總結

Buprenorphine（丁基原啡因）原本用於治療鴉片類藥物依賴與物質濫用/依賴。
TxGNN 模型預測它可能對**急性間歇性紫質症 (Acute Intermittent Porphyria)** 有效，
但目前**沒有臨床試驗**，只有 **1 篇文獻**（1993 年麻醉管理病例報告），且該文獻並未顯示藥物對疾病本身有治療效果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鴉片類依賴、物質濫用/依賴、嗎啡依賴 |
| 預測新適應症 | 急性間歇性紫質症 (Acute Intermittent Porphyria) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L4（僅有 1 篇病例報告，無直接療效證據，實質接近模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Buprenorphine 為鴉片類受體的部分促效劑，在鴉片類依賴治療中的角色已獲確立，但與紫質症之間尚無可信的機轉連結。

唯一檢索到的文獻是一篇麻醉管理病例報告，顯示 buprenorphine 類鴉片藥物可在紫質症病人的手術期間使用。這只說明「可以在這類病人身上使用」，並不表示對疾病本身有治療作用。

TxGNN 的高分（99.41%）屬於模型預測，並未獲得臨床資料支持。此外，紫質症病人用藥須特別留意合併藥物是否可能誘發紫質症發作，需另行評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | 病例報告 | Masui（日本麻醉學雜誌） | 一名疑似急性間歇性紫質症的 40 歲女性接受卵巢惡性腫瘤手術，報告其麻醉管理經驗；未評估對疾病的治療效果 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-28718 | TEMGESIC SUBLINGUAL TAB 0.2MG | 舌下錠 | 無資料 |
| HK-28719 | TEMGESIC INJ 0.3MG/ML | 注射劑 | 無資料 |
| HK-56198 | SUBOXONE SUBLINGUAL TAB 2MG/0.5MG | 舌下錠 | 無資料 |
| HK-56197 | SUBOXONE SUBLINGUAL TAB 8MG/2MG | 舌下錠 | 無資料 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜，非仿單內容），主要包括：
  - 呼吸系統：慢性阻塞性肺病 (COPD)、呼吸衰竭
  - 心血管與心律：長 QT 症候群、尖端扭轉型心律不整、姿位性低血壓、姿勢性心搏過速症候群
  - 肝膽：肝病、膽囊疾病、慢性 B 型/C 型肝炎
  - 內分泌：腎上腺皮質功能不足（Addison 病）、甲狀腺功能低下
  - 消化與泌尿：麻痺性腸阻塞、腸阻塞、良性攝護腺肥大、尿道狹窄
  - 神經：顱內壓升高、假性腦瘤
  - 物質相關：藥物依賴、物質濫用/依賴
- **藥物交互作用**：資料庫共記錄 100 筆，以下為部分列為 **Major（重大）** 者：
  - Alvimopan
  - Bupropion
  - Morphine
  - Cisapride
  - Dolasetron

  另有多項中度交互作用（如 Famotidine、Loperamide、Clarithromycin、Aprepitant、Dexamethasone 等）。

仿單的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但缺乏臨床試驗，唯一的文獻是與療效無關的麻醉病例報告，且找不到可信的機轉連結。
- 紫質症病人用藥安全需特別審慎，目前不具備推進的依據。

**若要推進需要：**
- 取得 buprenorphine 的作用機轉資料，並釐清與紫質症病理（血基質合成路徑）的關聯
- 針對紫質症的致紫質性（porphyrinogenicity）進行獨立安全性評估
- 取得香港仿單的警語與禁忌症資料
- 進行系統性文獻檢索，確認是否有任何直接療效證據，再評估是否值得設計探索性研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

