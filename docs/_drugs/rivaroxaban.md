---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 781
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Rivaroxaban：預測新適應症為類風濕性關節炎 (Rheumatoid Arthritis)（證據等級 L5）。原適應症：本次彙整資料未載明"
monitor_inn: "RIVAROXABAN"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Rivaroxaban：從（原適應症未載明）到類風濕性關節炎
{: .text-alpha }

## 一句話總結

Rivaroxaban 是直接 Factor Xa 抑制劑（口服抗凝血劑），在香港已有多張單方許可證，但本次彙整的資料未載明原核准適應症。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，但目前**沒有任何相關臨床試驗**，僅有 **4 篇間接相關文獻**，證據仍屬模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次彙整資料未載明 |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 0.9957 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 rivaroxaban 是直接 Factor Xa 抑制劑，主要用於抗凝血治療。

理論上，類風濕性關節炎存在「凝血與發炎的交互作用」：凝血酶與 FXa 可能透過 PAR-1/PAR-2 訊號促進滑膜發炎，且類風濕性關節炎患者本身血栓風險較高。這是此預測在機轉上可能成立的假說。

不過，目前檢索到的文獻僅涵蓋下肢靜脈血栓處置、自體免疫疾病的凝血酶生成檢測，以及心房顫動的用藥順從性，**沒有任何研究測試 rivaroxaban 是否能治療類風濕性關節炎本身**。因此這個連結仍是計算預測與理論假說，並非已被證實的疾病修飾作用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | 下肢深層靜脈血栓的診斷與治療回顧，與類風濕性關節炎療效無直接關聯 |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de medecine interne | 凝血酶生成檢測可用於評估自體免疫疾病的高凝血狀態與心血管風險 |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | 非瓣膜性心房顫動患者使用 rivaroxaban 與 apixaban 的用藥順從性比較 |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | 服用口服類固醇的類風濕性關節炎合併心房顫動患者，抗凝治療下仍發生栓塞事件的個案 |

---

## 香港上市資訊

香港共有 20 張有效單方許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57861 | XARELTO TAB 10MG（拜耳） | 未載明 | 未載明 |
| HK-61395 | XARELTO TAB 20MG（拜耳） | 未載明 | 未載明 |
| HK-61396 | XARELTO TAB 15MG（拜耳） | 未載明 | 未載明 |
| HK-67833 | RIVAROXABAN SANDOZ TABLETS 20MG（Sandoz） | 未載明 | 未載明 |
| HK-68572 | RALTEG 20 TABLETS 20MG（I & C） | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜中的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病關聯，非仿單內容）：肝衰竭、腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、凝血疾病。
- **藥物交互作用**：共查得 100 筆，以下列出部分主要者：
  - 嚴重 (Major)：Acetylsalicylic acid（阿斯匹靈）、Cobicistat、Deferasirox、Ibritumomab tiuxetan、Tositumomab (I-131)
  - 中度 (Moderate)：Aprepitant、Dexamethasone、Cimetidine、Clarithromycin、Miconazole、Clotrimazole 等

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數雖高（0.9957），但沒有任何臨床試驗，文獻也只有間接相關內容，證據等級為 L5。
- 凝血與發炎交互作用的機轉僅屬假說，且香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊原適應症、警語與禁忌資料
- 取得 DrugBank 的作用機轉資料，強化機轉連結分析
- 進行類風濕性關節炎的前臨床研究（如 FXa/PAR 訊號在滑膜發炎中的作用）
- 評估類風濕性關節炎患者的出血風險與常用藥物（如類固醇、NSAIDs）的交互作用，再考慮設計探索性臨床試驗
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

