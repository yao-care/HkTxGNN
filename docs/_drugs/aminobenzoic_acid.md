---
layout: default
title: Aminobenzoic Acid
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Aminobenzoic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Aminobenzoic Acid：從（無登記適應症）到遺傳性血管性水腫（C1 抑制劑缺乏症）

## 一句話總結

Aminobenzoic Acid（PABA，對胺基苯甲酸）是一種結構簡單的芳香族胺基酸衍生物，目前在香港並無任何已核准的臨床適應症。TxGNN 模型預測其最高可能對**遺傳性血管性水腫伴 C1 抑制劑缺乏症（Hereditary Angioedema with C1Inh Deficiency）**有效，預測分數達 99.73%，然而此方向目前**無任何臨床試驗或文獻支持**。在全部 10 項預測中，以**局限性系統性硬化症（Rank 6）**具備最多歷史間接依據，為本批次唯一達 L4 證據等級的候選適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無已登記核准適應症（香港） |
| 預測新適應症 | 遺傳性血管性水腫伴 C1 抑制劑缺乏症（Hereditary Angioedema with C1Inh Deficiency） |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5（僅模型預測，無直接研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Aminobenzoic Acid 詳細的作用機轉（MOA 資料缺口，DG002）。根據已知資訊，PABA 是葉酸生物合成的前驅物，其鉀鹽形式 Potassium aminobenzoate（POTABA）在 1950–1990 年代曾被推測能透過**抑制單胺氧化酶（MAO）活性**（從而減少 5-HT 促纖維化效應）及**抑制 TGF-β 介導的纖維母細胞活化**，抑制過度的膠原蛋白沉積。然而，這些機轉均屬舊版推測性描述，游離酸（free acid）形式的現代藥理資料付之闕如。

針對第 1 名預測（遺傳性血管性水腫伴 C1Inh 缺乏症），HAE 的病理核心為 C1 抑制劑（serpin 家族）缺乏，導致激肽釋放酶—緩激肽路徑失控，引發反覆性血管性水腫發作。PABA 雖具微弱抗纖溶特性，但結構上遠不及已核准用於 HAE 預防的 tranexamic acid 或 epsilon-aminocaproic acid，與本適應症缺乏直接藥理連結。此項 TxGNN 預測最可能反映補體/凝血路徑在知識圖譜中的拓撲鄰近性，而非獨立的藥理機轉。

在全部 10 項預測中，**局限性系統性硬化症（Rank 6，證據等級 L4）**是唯一具有歷史間接臨床依據的候選適應症：POTABA 曾在舊版文獻中被討論用於系統性硬化症的抗纖維化治療，與 PABA 推測的抑制膠原沉積機轉最為吻合。其餘 8 項預測（Rank 1–5、7–10）均屬 L5，僅基於知識圖譜拓撲相鄰，缺乏藥理學支撐。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻來自第 6 名預測適應症（局限性系統性硬化症），為本批次 10 項預測中唯一具有相關文獻的候選方向，在此一併列出供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [17217320](https://pubmed.ncbi.nlm.nih.gov/17217320/) | 2006 | Narrative Review（替代醫學） | Alternative Medicine Review | 回顧 SSc 自然療法，PABA 被列為具推測性抗纖維化潛力的候選療法，提及其鉀鹽（POTABA）的歷史臨床使用 |
| [2406809](https://pubmed.ncbi.nlm.nih.gov/2406809/) | 1990 | Clinical Review | Rheumatic Diseases Clinics of North America | 系統性硬化症多種療法整合回顧，指出多項早期單臂研究的結果難以在對照試驗中複製（包括 colchicine、n-acetylcysteine 等），需謹慎詮釋 |

> ⚠️ **注意**：上述文獻均為舊版敘述性回顧（1990–2006 年），並非針對 PABA 游離酸形式或 Limited Systemic Sclerosis 亞型的隨機對照試驗，屬間接、低強度證據，不計入高等級支持。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
全部 10 項 TxGNN 預測中，9 項為 L5（僅模型預測，無任何直接支持研究），整體證據強度極弱；唯一例外（局限性系統性硬化症，L4）僅有 1990 年代的敘述性回顧佐證，且藥物在香港未上市、作用機轉（MOA）完全缺失，依現行評估標準無法進入 S1 安全性初評（Blocking 資料缺口 DG001 尚未解決）。

**若要推進需要：**
- 解決 DG001（Blocking）：取得仿單警語與禁忌資訊，以解除 S1 安全性初評封鎖
- 解決 DG002（High）：補充完整的 MOA 資料（DrugBank API 查詢），重建機轉關聯性分析基礎
- 針對最具潛力的候選方向（局限性系統性硬化症），進行現代前臨床研究（體外纖維母細胞模型），以重新驗證 PABA 游離酸的抗纖維化效果
- 確認 Potassium aminobenzoate（POTABA）與游離 PABA 的藥理等效性，評估歷史 POTABA 文獻是否可轉化為游離酸的證據基礎
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

