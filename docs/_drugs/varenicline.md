---
layout: default
title: Varenicline
parent: 僅模型預測 (L5)
nav_order: 927
evidence_level: L5
indication_count: 10
monitor_inn: "VARENICLINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
last_modified_at: 2026-10-23
description: "Varenicline：預測新適應症為偏頭痛（證據等級 L5）。原適應症：許可證資料中未提供核准適應症文字"
---

# Varenicline
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

## Varenicline：從戒菸輔助到偏頭痛（模型預測）
{: .text-alpha }

## 一句話總結

Varenicline 是尼古丁乙醯膽鹼受體的藥物，香港已有 2 張單方許可證，但目前整理的資料中沒有核准適應症文字。
TxGNN 模型預測它可能對**偏頭痛 (migraine disorder)** 有效，但**沒有任何臨床試驗**，也沒有直接研究此疾病的文獻，因此證據僅停留在模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料中未提供核准適應症文字 |
| 預測新適應症 | 偏頭痛 |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏經核實的詳細作用機轉資料。就已知的藥理背景，Varenicline 是 α4β2 尼古丁乙醯膽鹼受體的部分促效劑，對 α7 受體則為完全促效劑。膽鹼性訊號與疼痛及三叉神經血管調控之間有間接的理論連結，但這只是推測。

需要特別注意方向性的問題：頭痛與偏頭痛本身就是 Varenicline 已知的不良反應，因此即使模型分數很高，實際效果方向仍不確定，甚至可能相反。

TxGNN 模型（深度學習）給出的高分，可能反映模型學到的相關疾病之間的相似性，並非生物學證據，也不是臨床證據。同時預測的相鄰疾病（如伴腦幹先兆的偏頭痛）的高分，也可能只是反映模型學到的與偏頭痛之間的相似性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前沒有文獻直接研究 Varenicline 治療偏頭痛。唯一與此預測關聯的一篇是心臟驟停的個案報告，與偏頭痛療效無關：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | 個案報告 | Therapie | Varenicline 相關心臟驟停個案，屬安全性通報，與偏頭痛療效無關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68451 | APO-VARENICLINE TABLETS 0.5MG | 未提供 | 未提供 |
| HK-68452 | APO-VARENICLINE TABLETS 1MG | 未提供 | 未提供 |

兩張皆為單方、有效狀態，持證商為 HIND WING CO LTD。

---

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（來自知識圖譜，並非仿單內容）：焦慮症、精神官能症、輕鬱症、雙相情感障礙、重度情感性疾患、物質濫用／依賴、急性冠心症、周邊血管疾病、間歇性跛行、周邊動脈疾病、思覺失調症。
- **藥物交互作用**：資料庫共記錄 100 筆。列出的項目中僅 Cimetidine 為輕微等級，其餘（如 Metformin、Glimepiride、Omeprazole、Morphine、Simvastatin、Prednisone、Epinephrine 等）等級未標示。
- **相關文獻訊號**：頭痛為 Varenicline 常見不良反應，另有洗澡誘發頭痛及心臟驟停的個案報告。

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何臨床試驗或直接研究偏頭痛的文獻，證據等級為 L5。
- 頭痛本身是已知不良反應，療效方向不明，且知識圖譜顯示多項精神與心血管禁忌關聯。

**若要推進需要：**
- 取得香港仿單全文，確認核准適應症、警語與禁忌。
- 補充作用機轉資料，並釐清 α4β2／α7 訊號與偏頭痛的關聯。
- 先做系統性文獻回顧，並分析既有戒菸試驗中偏頭痛發作頻率的變化，確認方向。
- 有初步訊號後，再設計小規模探索性試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

