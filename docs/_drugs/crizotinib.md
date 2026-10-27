---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Crizotinib：預測新適應症為遺傳性牙齦纖維瘤病 (Fibromatosis, Gingival)（證據等級 L5）。原適應症：非小細胞肺癌、肺癌"
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Crizotinib：從非小細胞肺癌到牙齦纖維瘤病
{: .text-alpha }

## 一句話總結

Crizotinib 是一種口服激酶抑制劑，原本用於治療非小細胞肺癌（NSCLC）與肺癌。
TxGNN 模型預測它可能對**遺傳性牙齦纖維瘤病 (Fibromatosis, Gingival)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個預測，僅為模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、肺癌（依知識圖譜適應症資料；香港許可證未載明適應症文字） |
| 預測新適應症 | 遺傳性牙齦纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知文獻，Crizotinib 是 ALK、ROS1 與 c-MET 受體酪胺酸激酶的 ATP 競爭性抑制劑，在 ALK 或 ROS1 重排的非小細胞肺癌中療效已被證實。

然而，就現有資料而言，ALK/ROS1/MET 抑制與遺傳性牙齦纖維瘤病之間**沒有任何支持的機轉連結**。TxGNN 分數雖然很高（0.998），但排名僅為 4427，且沒有試驗或文獻佐證，應視為尚待驗證的假說，不宜過度解讀。

## 其他排名較前的預測（供參考）

為協助判斷，以下列出其他高分預測的證據概況：

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|-----------|-----------|---------|------|
| 肺纖維瘤 | 99.75% | L5 | 僅模型預測，無試驗與文獻 |
| 肺錯構瘤 | 99.75% | L4 | 僅有 1 篇 ALK 陰性炎性肌纖維母細胞瘤個案報告，與錯構瘤不同，屬間接證據 |
| 肺門癌 | 99.73% | L4 | 2 篇個案報告，實質上屬已核准的 NSCLC 適應症，並非新的再利用訊號 |
| 肺良性腫瘤 | 99.73% | L4 | 文獻為 ALK 陽性 NSCLC 的 RCT，屬惡性疾病，為疾病標籤對應的假象 |
| 肺溝腫瘤 | 99.73% | L5 | 僅模型預測；若為 NSCLC 則療效取決於 ALK/ROS1 狀態 |
| 肺生殖細胞腫瘤 | 99.73% | L3 | 有 2 個籃式試驗，但屬基因型導向而非組織型特異；僅在腫瘤帶有可介入的 ALK/ROS1/MET 變異時才值得探討 |

## 臨床試驗證據

目前無相關臨床試驗登記（針對預測的牙齦纖維瘤病）。

## 文獻證據

目前無相關文獻（針對預測的牙齦纖維瘤病）。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61968 | XALKORI CAP 250MG | 膠囊 | 資料未載明 |
| HK-61969 | XALKORI CAP 200MG | 膠囊 | 資料未載明 |

兩張許可證皆為單方、有效，持證商為 Pfizer Corporation Hong Kong Limited。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（ALK/ROS1/MET 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 文獻個案顯示可能發生肝毒性（含致命性肝衰竭）與心臟毒性（心搏過緩、QT 延長），建議監測肝功能與心電圖；其餘請參考原廠仿單 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用，以下為部分代表：
  - **嚴重 (Major)**：Clarithromycin、Cisapride、Dolasetron、Eliglustat、Granisetron
  - **中度 (Moderate)**：Famotidine、Metformin、Loperamide、Bupropion、Aprepitant、Dexamethasone、Budesonide 等
- **文獻中的安全訊號**（個案報告）：致命性肝衰竭、心臟毒性（心搏過緩、QT 延長、病竇症候群）、多形性紅斑、食道炎。

其餘警語與禁忌症資料缺乏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或文獻支持，也找不到合理的機轉連結，僅屬模型預測（L5）。
- 其他高分預測多為已核准 NSCLC 適應症的疾病標籤對應，並非真正的新適應症訊號；唯一值得進一步探討的是肺生殖細胞腫瘤（L3），且僅限帶有可介入基因變異的情況。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並評估 ALK/ROS1/MET 與牙齦纖維瘤病的生物學關聯
- 取得香港衛生署原廠仿單，補全警語、禁忌症與核准適應症
- 進行前臨床或機轉驗證，確認是否存在合理的標靶
- 若考慮其他預測適應症，需先確認腫瘤的 ALK/ROS1/MET 分子狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

