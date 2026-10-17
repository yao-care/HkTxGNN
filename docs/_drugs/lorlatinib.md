---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 540
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lorlatinib：預測新適應症為牙齦纖維瘤病 (Fibromatosis, gingival)（證據等級 L5）。原適應症：非小細胞肺癌"
monitor_inn: "LORLATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm"]
---

# Lorlatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lorlatinib：從非小細胞肺癌到牙齦纖維瘤病（預測排名第一）

## 一句話總結

Lorlatinib 是第三代 ALK/ROS1 酪胺酸激酶抑制劑，原本用於 ALK 陽性非小細胞肺癌。
TxGNN 模型預測它可能對**牙齦纖維瘤病 (Fibromatosis, gingival)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純計算預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 牙齦纖維瘤病 (Fibromatosis, gingival) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Lorlatinib 是 ALK/ROS1 酪胺酸激酶抑制劑，在 ALK 陽性非小細胞肺癌中的療效已被多項研究證實。

然而，牙齦纖維瘤病是一種纖維化／遺傳性牙齦過度增生的疾病，從現有資料看不出它與 ALK/ROS1 訊號傳遞有合理的關聯。這個高分更可能來自知識圖譜中的網路鄰近性，而非真實的生物學機轉，因此應視為尚未驗證的假說。

**同一藥物的其他預測（供參考）：**

| 排名 | 預測疾病 | 分數 | 證據等級 | 說明 |
|------|---------|------|---------|------|
| 2 | 肺纖維瘤 (fibroma of lung) | 99.75% | L5 | 無試驗或文獻；良性纖維腫瘤無已知 ALK/ROS1 驅動 |
| 3 | 肺錯構瘤 (hamartoma of lung) | 99.75% | L5 | 無試驗或文獻；機轉與 ALK/ROS1 無明確關聯 |
| 4 | 肺門癌 (lung hilum carcinoma) | 99.74% | L4 | 僅 1 篇個案報告，本質上是原適應症的延伸 |
| 5 | 肺良性腫瘤 (lung benign neoplasm) | 99.74% | L4 | 文獻皆針對惡性 ALK/ROS1 陽性肺癌，不應視為支持此適應症 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（註：預測排名第 4、5 的疾病有文獻，但內容多為原適應症 ALK 陽性非小細胞肺癌的研究，例如 Phase 3 CROWN 試驗及其 5 年、7 年更新，並不能作為牙齦纖維瘤病的證據。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66412 | LORVIQUA TABLETS 25MG | — | — |
| HK-66411 | LORVIQUA TABLETS 100MG | — | — |

兩張許可證均為單方、有效，持有者為 Pfizer Corporation Hong Kong Limited。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（ALK/ROS1 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；文獻提及需留意肝毒性與中樞神經系統不良反應 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 項交互作用，以下列出主要的重度項目：
  - **Dexamethasone**（重度）
  - **Clarithromycin**（重度）
  - 另有多項中度交互作用，例如 Hydrocortisone、Bupropion、Aprepitant、Morphine、Cimetidine 等。
- **文獻提示**：已發表文獻指出 Lorlatinib 具有獨特的不良反應特徵（包括高脂血症、中樞神經系統反應），並有 ALK/ROS1 抑制劑肝毒性的藥物安全監測研究。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.81%），但沒有任何臨床試驗或文獻，也找不到 ALK/ROS1 抑制與牙齦纖維瘤病之間合理的機轉關聯，屬於純模型預測（L5）。
- 此外，香港仿單的警語與禁忌症資料缺漏，尚無法進行安全性篩選。

**若要推進需要：**
- 取得 Lorlatinib 完整的作用機轉資料（DrugBank）
- 以文獻回顧或實驗研究驗證 ALK/ROS1 訊號是否參與牙齦纖維瘤病
- 下載並解析香港衛生署仿單，補齊警語與禁忌症
- 若目標是肺部相關疾病，建議改為評估肺門癌等屬於原適應症延伸的項目，並確認 ALK 狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

