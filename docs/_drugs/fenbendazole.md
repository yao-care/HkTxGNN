---
layout: default
title: Fenbendazole
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fenbendazole：預測新適應症為膀胱癌 (Urinary Bladder Carcinoma)（證據等級 L5）。原適應症：許可證資料未載明（香港登記為獸用製劑）"
monitor_inn: "Fenbendazole"
predicted_indications: ["urinary bladder carcinoma", "urinary bladder neoplasm", "infiltrating bladder urothelial carcinoma", "non-invasive bladder urothelial carcinoma", "bladder urachal urothelial carcinoma", "bladder squamous papilloma", "bladder signet ring cell adenocarcinoma", "bladder colloid adenocarcinoma", "bladder colonic type adenocarcinoma", "bladder mixed adenocarcinoma"]
---

# Fenbendazole
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

# Fenbendazole：從（未載明適應症）到膀胱癌

## 一句話總結

Fenbendazole 是苯并咪唑類驅蟲藥，香港登記為獸用製劑，許可證資料中未載明核准適應症。
TxGNN 模型預測它可能對**膀胱癌 (Urinary Bladder Carcinoma)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇相關的前臨床研究**可作間接參考，整體屬於模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（香港登記為獸用製劑） |
| 預測新適應症 | 膀胱癌 (Urinary Bladder Carcinoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（相近術語「膀胱腫瘤」有前臨床研究，屬 L4） |
| 香港上市 | ✓ 已上市（獸用） |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Fenbendazole 是苯并咪唑類驅蟲藥，可結合微管蛋白（tubulin），可能干擾微管聚合。微管是細胞分裂的關鍵結構，這與部分抗癌藥物的作用方向相似。

前臨床報告也提到它可能影響 p53 與葡萄糖代謝，但這些都沒有針對膀胱癌的臨床資料支持。由於原適應症是驅蟲，與腫瘤之間沒有直接的疾病關聯，這個預測主要來自知識圖譜的整體相似性，而非已證實的臨床關聯。

在相近術語「膀胱腫瘤 (Urinary Bladder Neoplasm)」下，有近期前臨床研究探討 Fenbendazole 的組合療法，提示鐵死亡（ferroptosis）、免疫活化與微管破壞可能是作用機制。但這些研究都是組合療法，無法分離 Fenbendazole 單獨的效果。

此外，TxGNN 還預測了多種膀胱癌亞型（浸潤性、非浸潤性尿路上皮癌，以及罕見的腺癌亞型等），分數都在 99.98%–99.99% 之間。這些亞型沒有任何臨床試驗或文獻，高分很可能反映的是疾病本體論上的相近性，而非各亞型的特定生物學。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻是在相近術語「膀胱腫瘤」下檢索到的，皆非臨床試驗。研究類型係依標題推斷，需對照全文確認。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41861111](https://pubmed.ncbi.nlm.nih.gov/41861111/) | 2026 | 前臨床（組合療法） | Advanced Science | 膀胱內給藥奈米平台 FBZ@BSA@PDA，結合 Fenbendazole 誘導鐵死亡、免疫原性細胞死亡與光熱療法，用於膀胱癌 |
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | 前臨床（組合療法） | J Exp Clin Cancer Res | CRISPR-Cas13a 與 Fenbendazole 組合的膀胱內灌注療法 |
| [23208426](https://pubmed.ncbi.nlm.nih.gov/23208426/) | 2012 | 前臨床機轉 | J Toxicol Sci | 大鼠 28 天致癌物實驗中的細胞增殖與凋亡標記；可能與 Fenbendazole 無特定關聯，僅供背景參考 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50424 | QUANTEL TAB (VET) | 未載明 | 未載明（獸用製劑） |

---

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢無結果。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 膀胱癌預測僅有模型分數支持，沒有任何臨床試驗或人體資料。
- 最相關的文獻都是前臨床組合療法研究，無法判斷 Fenbendazole 單獨的效果。
- 香港登記產品為獸用製劑，安全性與警語資料缺口屬阻擋性，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症資料。
- 補充作用機轉資料（例如查詢 DrugBank）。
- 閱讀前臨床文獻全文，確認 Fenbendazole 單獨使用的效果與劑量。
- 評估人用製劑與給藥途徑（尤其是膀胱內給藥）的可行性。
- 以進一步的體外與動物實驗，驗證對膀胱癌的單藥活性，再評估是否規劃早期臨床試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

