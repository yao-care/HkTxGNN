---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Cyanocobalamin：預測新適應症為生物素代謝疾病 (Biotin Metabolic Disease)（證據等級 L5）。原適應症：維生素 B12 缺乏症、惡性貧血、缺鐵性貧血、葉酸缺乏性貧血等"
monitor_inn: "CYANOCOBALAMIN"
predicted_indications: ["biotin metabolic disease"]
---

# Cyanocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Cyanocobalamin：從維生素 B12 缺乏症到生物素代謝疾病

## 一句話總結

Cyanocobalamin（氰鈷胺，維生素 B12）原本用於治療維生素 B12 缺乏症與各類貧血（如惡性貧血）。
TxGNN 模型預測它可能對**生物素代謝疾病 (Biotin Metabolic Disease)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**關聯性很低的文獻（一般性綜述），屬於僅有模型預測的階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素 B12 缺乏症、惡性貧血、缺鐵性貧血、葉酸缺乏性貧血等（來自知識圖譜的適應症關聯） |
| 預測新適應症 | 生物素代謝疾病 (Biotin Metabolic Disease) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Cyanocobalamin 是維生素 B12 的人工合成形式，在體內轉化為活性輔酶，其在 B12 缺乏症與相關貧血中的療效已被廣泛確立。

生物素與鈷胺素同屬 B 群維生素，都是代謝酶的輔因子。例如，丙醯輔酶 A 羧化酶依賴生物素，甲基丙二醯輔酶 A 變位酶依賴鈷胺素，兩者都參與丙酸代謝路徑。這可能是模型給出高分的原因之一。

不過，這**僅是未經驗證的假設**。現有資料並未顯示 cyanocobalamin 能治療生物素代謝疾病（如生物素酶缺乏症或全羧化酶合成酶缺乏症）。這類疾病的標準治療是補充生物素。高預測分數反映的是知識圖譜中的關聯，不等於臨床有效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | 綜述以生物技術方法（發酵、生物轉化）生產維生素、輔酶及相關生化物質；內容為製造工藝，並未探討 cyanocobalamin 在生物素代謝疾病的臨床使用 |

---

## 香港上市資訊

本藥在香港有 20 張有效單一成分許可證，下表列出 5 張主要許可證。資料中未收錄核准適應症文字與劑型。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63076 | VIDALIC B12 SOLUTION FOR INJECTION 2000MCG/ML | 注射液 | 未提供 |
| HK-12579 | BITAMIN INJ 1000MCG/ML | 注射劑 | 未提供 |
| HK-56543 | VITAMIN B12 INJ 1000MCG/ML | 注射劑 | 未提供 |
| HK-26263 | NEO-ACTIVE VITAMIN B12 TAB 100MCG | 錠劑 | 未提供 |
| HK-46964 | COBAMIN OPHTHALMIC SOLUTION 0.02% | 眼用溶液 | 未提供 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分列出的項目，嚴重度皆為輕微或未知：
  - 輕微 (Minor)：組織胺 H2 受體拮抗劑（famotidine、ranitidine、cimetidine、nizatidine）、質子幫浦抑制劑（omeprazole、esomeprazole、lansoprazole、dexlansoprazole、pantoprazole、rabeprazole）、氯化鉀
  - 嚴重度未知 (Unknown)：metformin、glimepiride、acarbose、rosiglitazone、mesalazine、doxycycline、morphine、sucralfate

  制酸類藥物與 metformin 可能降低 B12 吸收，長期併用時宜留意。

其他警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.60%），但目前沒有任何臨床試驗，唯一的文獻為與臨床無關的製造工藝綜述，機轉連結也未獲資料支持。
- 生物素代謝疾病已有明確的標準治療（補充生物素），沒有證據顯示 cyanocobalamin 能提供額外益處。

**若要推進需要：**
- 補齊作用機轉資料，並以文獻檢索驗證 B12 與生物素代謝疾病（如生物素酶缺乏症、全羧化酶合成酶缺乏症）之間是否有實際關聯
- 搜尋是否有病例報告或前臨床研究支持此用途
- 取得香港衛生署核准的仿單，確認警語與禁忌症，完成安全性篩選
- 若前述證據支持，再考慮設計小規模探索性研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

