---
layout: default
title: Capmatinib
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Capmatinib：預測新適應症為類風濕性關節炎 (Rheumatoid Arthritis)（證據等級 L5）。原適應症：許可證資料未載明"
monitor_inn: "Capmatinib"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "heart disease", "Jeune syndrome situs inversus", "Pierre Robin syndrome associated with a chromosomal anomaly", "orofacial clefting syndrome", "Laubry-Pezzi syndrome", "interventricular septum aneurysm", "hyperthyroidism"]
---

# Capmatinib
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

## Capmatinib：從 MET 陽性腫瘤治療到類風濕性關節炎
{: .text-alpha }

## 一句話總結

Capmatinib 是一種選擇性 MET 酪胺酸激酶抑制劑，在香港已取得許可證上市。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
但目前**沒有臨床試驗**，只有 **1 篇**一般性文獻（激酶抑制劑綜述），與類風濕性關節炎沒有直接關聯，證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.45% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Capmatinib 是選擇性 MET 酪胺酸激酶抑制劑。目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未收錄），上述機轉描述來自本報告編纂的分析。

MET 訊號被認為與類風濕性關節炎的滑膜發炎與血管新生有關，因此在機轉上有一定合理性。不過，目前唯一連結的文獻是 2021 年一篇涵蓋 FDA 核准激酶抑制劑的綜述，並未提供任何類風濕性關節炎的專屬數據。

因此，高預測分數只是計算模型的結果，沒有臨床證據支持。此外，TxGNN 在此藥物的其他高分預測（如罕見先天發育症候群）也多缺乏機轉依據，應謹慎看待模型分數。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | FDA 核准小分子蛋白激酶抑制劑的性質整理，無類風濕性關節炎專屬數據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66993 | TABRECTA TABLETS 200MG | 未載明 | 未載明 |
| HK-66992 | TABRECTA TABLETS 150MG | 未載明 | 未載明 |

兩張許可證均為單一成分、現行有效，持證商為 Novartis Pharmaceuticals (HK) Limited。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（MET 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共記錄 100 筆交互作用，以下列出部分重點：
  - **嚴重（Major）**：Dexamethasone、Clarithromycin
  - **中度（Moderate）**：Metformin、Alosetron、Loperamide、Aprepitant、Empagliflozin、Naltrexone 等
  - **輕微（Minor）**：Rabeprazole、Omeprazole、Esomeprazole、Lansoprazole、Pantoprazole 等質子幫浦抑制劑
- **其他安全訊號**：一篇文獻報告 crizotinib（另一種 MET/ALK 抑制劑）與 sofosbuvir/velpatasvir 的藥物交互作用造成心臟毒性，提示同類藥物併用時需留意，但該報告並非針對 capmatinib。

香港仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自 TxGNN 模型（證據等級 L5），沒有任何臨床試驗，唯一的文獻是與類風濕性關節炎無直接關聯的一般性綜述。
- 腫瘤用的標靶藥物若要用於慢性發炎性疾病，需審慎評估長期安全性，且現有的 Major 等級交互作用（如 dexamethasone、clarithromycin）在類風濕性關節炎患者中可能相當常見。

**若要推進需要：**
- 取得 MET 訊號在類風濕性關節炎的專屬證據（細胞或動物模型）
- 取得詳細的作用機轉資料（MOA）
- 取得香港原廠仿單的警語與禁忌症，完成安全性初篩
- 評估與現有類風濕性關節炎治療（如類固醇、免疫抑制劑）的併用風險
- 若考慮其他預測方向，以「心臟疾病」為例，目前僅有 1 篇前臨床研究（顯示 capmatinib 可減輕 doxorubicin 心臟毒性與 cisplatin 腎毒性），證據等級為 L4，同樣屬 Hold，需人體資料才能進一步評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

