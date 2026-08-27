---
layout: default
title: Hydroquinone
parent: 中證據等級 (L3-L4)
nav_order: 378
evidence_level: L3
indication_count: 4
---

# Hydroquinone
{: .fs-9 }

證據等級: **L3** | 預測適應症: **4** 個
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

# Hydroquinone：老藥新用初步評估——聚焦脂漏性角化病及其他候選適應症

## 一句話總結

Hydroquinone 目前尚未在香港上市，也沒有核准適應症紀錄。TxGNN 模型預測它可能對**脂漏性角化病 (Seborrheic Keratosis)** 有效，目前僅有 **2 篇文獻**支持、**無臨床試驗**直接驗證，證據等級為 L3、屬早期研究假說階段。模型同時提出另外 3 項候選適應症，其中一項（exanthem）的支持性試驗經檢視後，高度懷疑是疾病名稱映射錯誤，需人工複核才能採信。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港未上市，無核准適應症資料 |
| 預測新適應症 | 脂漏性角化病 (Seborrheic Keratosis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

DrugBank 目前未收錄 Hydroquinone 正式的作用機轉描述（資料缺口 DG002，待查 DrugBank API）。但根據本評估中一致出現的文獻與試驗脈絡，Hydroquinone 是已知的**酪胺酸酶 (tyrosinase) 抑制劑**，主要作用為抑制黑色素生成，臨床上廣泛用於治療黃褐斑（melasma）與皮膚色素沉澱問題（詳見下方臨床試驗證據段落中其他候選項的資料）。

脂漏性角化病本身的病理核心是表皮角質形成細胞的良性增生，與黑色素代謝異常並無直接關係。然而，其中一個色素較深的常見亞型——Dermatosis Papulosa Nigra (DPN，好發於深色皮膚族群）——常伴隨明顯的表皮黑色素沉積。因此，Hydroquinone 的酪胺酸酶抑制機轉理論上可能改善 DPN 病灶的色素性外觀，但**對脂漏性角化病本身的角質增生病理並無直接治療作用**。這是一個以外觀症狀為導向的間接關聯，而非病因治療，需要謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | 世代研究 (Cohort) | J Plast Reconstr Aesthet Surg | 針對亞洲患者臉部色素性疾病之前瞻性觀察研究，探討多重色素病灶合併治療策略；未於摘要中明確提及脂漏性角化病或 Hydroquinone 治療結果，相關性待核實 |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | 綜述 (Review) | J Drugs Dermatol | 探討 Dermatosis Papulosa Nigra（脂漏性角化病之色素性亞型）的治療選項，指出其組織學與脂漏性角化病無顯著差異；摘要片段未具體提及 Hydroquinone 之療效數據 |

> 註：以上兩篇文獻的相關性標記皆為「待核實 (pending)」，尚未經人工確認是否直接支持 Hydroquinone 治療脂漏性角化病。

---

## 香港上市資訊

Hydroquinone 目前**未在香港上市**，無許可證登記資料。

---

## 安全性考量

目前尚無法取得 Hydroquinone 的仿單警語、禁忌症或藥物交互作用資料（查詢結果為 not_found）。這是本評估中的**阻斷性 (Blocking) 資料缺口（DG001）**：在補齊完整仿單資料前，本候選藥物**無法進入 S1 安全性初評**。

---

## 其他預測適應症摘要

除脂漏性角化病外，TxGNN 另提出 3 項候選，證據品質差異很大，一併列出以求資訊完整：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 | 備註 |
|------|------|-----------|---------|------|------|
| 2 | 外陰內翻性毛囊角化病 (Vulvar Inverted Follicular Keratosis) | 99.64% | L5 | Hold | 罕見良性毛囊腫瘤，病理與黑色素調控無關，無任何臨床試驗或文獻佐證，機轉關聯薄弱，不建議進一步調查 |
| 3 | Exanthem（廣泛性皮疹） | 99.42% | L4 | Hold | 雖有 7 個臨床試驗，但實際內容全為黃褐斑 (melasma)／色素沉澱之局部脫色治療，與 exanthem 病名不符，**高度懷疑為 TxGNN 疾病詞彙映射錯誤**，在人工核實前不應作為 exanthem 的再利用證據 |
| 4 | 扁平苔癬 (Lichen Disease) | 99.07% | L4 | Research Question | 其色素沉澱亞型 (Lichen Planus Pigmentosus) 理論上可能受益於脫色機轉，但唯一相關案例報告實際使用藥物為 tacrolimus 而非 Hydroquinone，直接證據薄弱 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首選候選（脂漏性角化病）證據等級僅 L3，且機轉關聯為間接（僅對其色素性亞型有理論relevance），目前無任何臨床試驗直接驗證。
- 安全性資料存在**阻斷性缺口**（DG001：仿單警語與禁忌症缺失），依規定無法進入 S1 安全性初評。
- 藥物在香港未上市，整體證據強度尚不足以支持推進。

**若要推進需要：**
- 取得完整仿單警語與禁忌症資料（DG001，來源：TFDA 官網仿單 PDF）
- 補齊 DrugBank 作用機轉正式資料（DG002）
- 針對「exanthem」候選之疾病映射進行人工複核，釐清是否為 hyperpigmentation/melasma 標籤錯誤
- 若脂漏性角化病（特別是 DPN 亞型）仍為優先候選，建議設計小型前驅性研究驗證色素改善效果，並釐清文獻 33046430 與本適應症的實際關聯性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

