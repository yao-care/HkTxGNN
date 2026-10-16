---
layout: default
title: Cabozantinib
parent: 中證據等級 (L3-L4)
nav_order: 143
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Cabozantinib：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L3）。原適應症：腎細胞癌、透明細胞腎癌、甲狀腺髓質癌"
monitor_inn: "Cabozantinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal cell carcinoma associated with neuroblastoma", "childhood kidney cell carcinoma", "renal carcinoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Cabozantinib：從腎細胞癌到脂肪肉瘤

## 一句話總結

Cabozantinib 是一種口服多激酶抑制劑，原本用於腎細胞癌與甲狀腺髓質癌的治療。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **1 個臨床試驗**和 **1 篇文獻**支持這個方向，但兩者都不是脂肪肉瘤專屬的研究，證據仍屬初步。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎細胞癌、透明細胞腎癌、甲狀腺髓質癌（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold（僅適合作為研究問題追蹤） |

> 補充：在 TxGNN 前 10 名預測中，「未分類腎細胞癌」（L2，Proceed with Guardrails）和「腎癌 (Renal carcinoma)」（L1）的證據明顯較強，但後者與已核准適應症高度重疊，屬於確認而非真正的再利用。本報告依排名第 1 的脂肪肉瘤撰寫。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空白）。根據已知資訊，Cabozantinib 是 VEGFR2、MET、AXL 的多激酶抑制劑，這些路徑與腫瘤血管新生及腫瘤進展有關，在腎細胞癌中已有臨床證實的療效。

軟組織肉瘤的血管新生與腫瘤進展同樣與這些路徑有關，因此在機轉上有可能適用。文獻也指出 Cabozantinib 在多種軟組織肉瘤亞型中顯示活性。不過，目前提供的資料並未確認脂肪肉瘤專屬的結果，脂肪肉瘤只是軟組織肉瘤試驗中可能納入的亞群。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | 進行中（不再招募） | 66 | 隨機分派，比較 Ipilimumab + Nivolumab 單獨使用與加上 Cabozantinib 用於晚期軟組織肉瘤；尚無結果，亦無脂肪肉瘤亞型資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 試驗 | Am J Clin Oncol | 評估 Cabozantinib 併用放射治療作為四肢軟組織肉瘤術前治療的安全性；背景是擔心瘻管或穿孔風險 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65656 | CABOMETYX TABLETS 20MG | 錠劑 | 未載明 |
| HK-65654 | CABOMETYX TABLETS 40MG | 錠劑 | 未載明 |
| HK-65655 | CABOMETYX TABLETS 60MG | 錠劑 | 未載明 |

三張許可證皆為單方、有效，持有者為 BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多激酶抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（一般包含血液學參數、肝腎功能等） |
| 處置防護 | 請參考原廠仿單 |

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分主要項目：
  - **嚴重 (Major)**：Acetylsalicylic acid、Cisapride、Clarithromycin、Dolasetron、Granisetron、Levofloxacin
  - **中等 (Moderate)**：Loperamide、Aprepitant、Dexamethasone、Bisacodyl、Clotrimazole、Fenfluramine 等

其他警語與禁忌症請參考原廠仿單。另有一項研究提到 Cabozantinib 併用放射治療時，需留意瘻管或穿孔風險。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數雖高（99.83%），但目前僅有 1 個非脂肪肉瘤專屬的 Phase 2 試驗（尚無結果）與 1 篇 Phase 1 研究，證據只能視為研究假設。
- 缺乏作用機轉資料與仿單安全性資料，無法進入安全性篩選。

**若要推進需要：**
- 取得脂肪肉瘤亞型專屬的療效資料（例如 NCT05836571 的亞群分析）
- 補齊 DrugBank 作用機轉資料
- 下載並解析香港衛生署仿單，取得警語與禁忌症
- 評估肉瘤族群的安全性（含與放射治療併用時的瘻管／穿孔風險）及藥物交互作用管理計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

