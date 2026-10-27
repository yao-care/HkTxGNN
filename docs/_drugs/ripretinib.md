---
layout: default
title: Ripretinib
parent: 僅模型預測 (L5)
nav_order: 776
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ripretinib：預測新適應症為多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)（證據等級 L5）。原適應症：香港許可證未載明適應症"
monitor_inn: "Ripretinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma", "malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "amenorrhea (disease)", "progesterone-receptor negative breast cancer", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "breast tumor luminal A or B"]
---

# Ripretinib
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

## Ripretinib：從消化道間質瘤（GIST）到多發性內分泌腫瘤
{: .text-alpha }

## 一句話總結

Ripretinib 是一種口服 KIT/PDGFRA 廣譜激酶抑制劑，已於香港上市（商品名 QINLOCK）。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，但目前**沒有臨床試驗與文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；文獻顯示其核准用途為晚期消化道間質瘤（GIST） |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 98.84% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ripretinib 是 KIT/PDGFRA 的「開關口袋 (switch-pocket)」激酶抑制劑，可同時抑制原發與次發的 KIT、PDGFRA 突變，用於已接受多線治療的晚期 GIST。

此藥對其他激酶（如與 RET 相關的活性、VEGFR2）也可能有一定程度的抑制。第 2 型多發性內分泌腫瘤（MEN2）由 RET 驅動，因此理論上有一個鬆散的關聯。

不過，本報告所整理的資料中沒有任何證據支持這個連結。這項預測目前只能視為假說，需要先做機轉與前臨床驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無針對多發性內分泌腫瘤的相關文獻。

補充說明：排名第 2 的預測（HER2 陽性乳癌）僅連結到一篇一般性的激酶抑制劑綜述（PMID 33513356），沒有乳癌專屬的 ripretinib 證據。排名第 10 的預測（管腔型乳癌）連結的 12 篇文獻（顯示 10 篇）都在談 GIST、藥物動力學或分析方法，與該適應症無關，屬於檢索誤連，不能當作支持證據。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67004 | QINLOCK TABLETS 50MG（持證商：ZAI LAB (HONG KONG) LIMITED） | 未載明 | 未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（激酶抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；文獻另有心毒性與脂質代謝不良反應的處置指引（PMID 37692846） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查詢到 90 筆潛在交互作用，以下為部分例子。
  - **重大 (Major)**：Clarithromycin、Cobicistat
  - **中度 (Moderate)**：Pioglitazone、Aprepitant、Dexamethasone、Canagliflozin、Cimetidine、Eliglustat、Miconazole、Repaglinide 等
- 文獻提示，CYP3A4 與 P-gp 抑制劑（如 verapamil）可能提高 ripretinib 的暴露量（大鼠研究，PMID 37831396）。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（98.84%），但沒有任何臨床試驗或文獻支持，證據等級僅 L5。機轉連結（RET）只是推測，且作用機轉資料缺漏。
- 其他排名前列的預測（如牛傳染性鼻氣管炎、巨細胞病毒感染、閉經）缺乏合理的機轉，很可能是知識圖譜的假象。

**若要推進需要：**
- 取得完整的作用機轉資料，並確認 ripretinib 對 RET 的實際抑制強度。
- 進行前臨床驗證，例如 RET 驅動的細胞或動物模型。
- 取得香港仿單的警語與禁忌症，完成安全性篩選。
- 取得香港許可證載明的核准適應症與劑型，確認原適應症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

