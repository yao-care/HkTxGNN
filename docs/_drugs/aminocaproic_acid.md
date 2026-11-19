---
layout: default
title: Aminocaproic Acid
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-17
monitor_inn: "AMINOCAPROIC ACID"
predicted_indications: ["severe nonproliferative diabetic retinopathy"]
description: "Aminocaproic Acid：預測新適應症為嚴重非增殖性糖尿病視網膜病變 (severe nonproliferative diabetic retinopathy)（證據等級 L5）。香港藥劑製品註冊：2 張（有效 1 張）"
---

# Aminocaproic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Aminocaproic Acid: 嚴重非增殖性糖尿病視網膜病變 (severe nonproliferative diabetic retinopathy)
{: .text-alpha }

## 一句話總結

Aminocaproic Acid（胺基己酸）是一種離胺酸類似物抗纖維蛋白溶解藥，香港目前有 2 張含此成分的眼藥水許可證，但許可證上未登載核准適應症。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (severe nonproliferative diabetic retinopathy) |
| TxGNN 預測分數 | 0.9927 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 2 張） |
| 許可證數 | 2 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位尚未取得）。根據藥理學的一般知識，Aminocaproic Acid 是離胺酸類似物，可抑制纖溶酶原活化及纖溶酶活性，達到抗纖維蛋白溶解的效果。

與糖尿病視網膜病變的關聯только是間接的：理論上它可能減少增殖期的纖溶相關出血或玻璃體出血。然而，非增殖性視網膜病變的主要成因是高血糖引起的微血管損傷、VEGF 訊號、發炎及微血管無灌流，抗纖溶藥物並不作用於這些路徑。

因此，0.9927 的高分僅是運算預測，機轉上的支持相當薄弱，需要更多實驗與臨床資料驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42060 | DAIGAKU EYE DROPS | 未登載 | 未登載 |
| HK-45441 | ROHTO KODOMO SOFT EYE DROPS | 未登載 | 未登載 |

兩張許可證皆為單一成分製劑，HK-42060（DAIGAKU EYE DROPS）已註銷、另一張仍有效，持證商分別為參天製藥（香港）及曼秀雷敦（亞太）。

<!-- review:begin hk-lic-20261117-aminocaproic_acid-1 -->

> **查核更正（2026-11-17）**：原文為「兩張許可證皆為單一成分製劑且仍有效，」。已更正：HK-42060 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-aminocaproic_acid-1 -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯資料，非仿單原文）：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、瀰漫性血管內凝血 (DIC)、猛爆性紫斑、後天性猛爆性紫斑、血栓性疾病。
- **藥物交互作用**：共查得 75 筆，多數嚴重度未分級。其中分級為中度的包括 Alteplase 與 Anistreplase（溶栓藥物，與抗纖溶作用相拮抗）。其他列出的藥物還有 Morphine、Omeprazole、Vancomycin、Simvastatin、Acetylsalicylic acid 等，嚴重度未知。
- **特別提醒**：抗纖維蛋白溶解藥可能增加血栓風險，罹患微血管病變的糖尿病患者可能特別容易出現視網膜血管栓塞，需格外審慎。

仿單的警語與禁忌資料尚未取得，其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有臨床試驗或文獻佐證，且機轉上與非增殖性視網膜病變的主要病理路徑關聯薄弱。
- 血栓風險對糖尿病微血管病變患者是實質顧慮，加上仿單安全性資料尚缺，目前不宜推進。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌資料（此為阻斷性資料缺口）
- 從 DrugBank 補充作用機轉（MOA）
- 進行系統性文獻檢索與前臨床研究，評估抗纖溶作用對視網膜微血管病變的影響
- 確認眼用劑型的給藥途徑是否適合視網膜疾病（藥物到達視網膜的可行性）
- 對 DDI 清單中的未分級項目進行人工審查，並評估血栓風險

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「兩張許可證皆為單一成分製劑且仍有效，」→「兩張許可證皆為單一成分製劑，HK-42060（DAIGAKU EYE DROPS」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

