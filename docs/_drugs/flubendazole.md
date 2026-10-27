---
layout: default
title: Flubendazole
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flubendazole：預測新適應症為膀胱尿路上皮癌 (Urinary Bladder Carcinoma)（證據等級 L5）。原適應症：本次整理的資料未載明"
monitor_inn: "Flubendazole"
predicted_indications: ["urinary bladder carcinoma", "urinary bladder neoplasm", "infiltrating bladder urothelial carcinoma", "non-invasive bladder urothelial carcinoma", "bladder urachal urothelial carcinoma", "bladder squamous papilloma", "bladder signet ring cell adenocarcinoma", "bladder colonic type adenocarcinoma", "bladder colloid adenocarcinoma", "bladder mixed adenocarcinoma"]
---

# Flubendazole
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

## Flubendazole：從（原適應症未載明）到膀胱癌
{: .text-alpha }

## 一句話總結

Flubendazole 是苯并咪唑（benzimidazole）類驅蟲藥，香港已有一張上市許可證，但本次compiled 資料未載明其核准適應症。
TxGNN 模型預測它可能對**膀胱尿路上皮癌 (Urinary Bladder Carcinoma)** 有效，預測分數極高。
但目前**沒有任何臨床試驗**，也**沒有 flubendazole 本身的文獻**；僅有 2 篇針對近緣藥物 fenbendazole 的前臨床研究，屬間接線索。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料未載明 |
| 預測新適應症 | 膀胱尿路上皮癌 (Urinary Bladder Carcinoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅模型預測）；相關的「膀胱腫瘤」項目為 L4（僅有近緣藥物的前臨床文獻） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Flubendazole 屬於苯并咪唑類驅蟲藥，此類藥物一般認為可結合 β-微管蛋白（beta-tubulin）、干擾微管聚合，這在抗增殖上是合理的機轉。需要說明的是，這項推論來自一般藥理學知識，並非本次整理的資料所直接支持。

TxGNN 對膀胱癌相關的多個詞條（如浸潤性、非浸潤性尿路上皮癌及各種罕見亞型）都給出約 99.98%–99.99% 的高分。這些高分很可能反映知識圖譜中疾病詞條彼此相近，而不是各亞型各自有獨立證據。對良性病灶（如膀胱鱗狀乳頭瘤），抗腫瘤的理論基礎更弱。

間接線索方面，有兩篇近期研究探討 fenbendazole（同屬苯并咪唑類，但**不是** flubendazole）用於膀胱癌模型：一篇結合光熱療法誘導鐵死亡，另一篇結合 CRISPR-Cas13a 做膀胱內灌注。本次僅取得標題與部分摘要，無法驗證研究設計與結果，只能視為類別層級的間接支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下兩篇皆針對 fenbendazole，並非 flubendazole，且為前臨床研究（依標題推斷）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41861111](https://pubmed.ncbi.nlm.nih.gov/41861111/) | 2026 | 前臨床 | Advanced Science | 膀胱內奈米平台結合 fenbendazole、鐵死亡誘導與光熱療法，用於膀胱癌的協同治療 |
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | 前臨床 | J Exp Clin Cancer Res | CRISPR-Cas13a 與 fenbendazole 的膀胱內灌注組合治療膀胱癌 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37527 | VERMIFLU TAB 500MG | 未載明（品名為錠劑） | 未載明 |

## 細胞毒性

Flubendazole 目前的核准用途為驅蟲藥，並非傳統抗腫瘤藥物，因此依規則省略此章節。若日後轉向腫瘤適應症，需另行評估細胞毒性與骨髓抑制風險。

## 安全性考量

安全性資訊請參考原廠仿單。本次整理的資料中，仿單的警語與禁忌症尚未取得，藥物交互作用查詢也沒有結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 膀胱癌的預測僅來自模型分數，沒有 flubendazole 的臨床試驗或直接文獻。
- 僅有近緣藥物 fenbendazole 的兩篇前臨床研究，屬間接證據，且高分可能源自疾病詞條的圖譜相近性。
- 仿單的安全性資料缺漏，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌症、核准適應症）並完成安全性篩選。
- 補充 flubendazole 的作用機轉資料（如 DrugBank）。
- 進行 flubendazole 本身在膀胱癌細胞株與動物模型的前臨床研究，並與 fenbendazole 比較。
- 評估給藥途徑的可行性（口服吸收有限，膀胱內灌注是否可行）。
- 確認 fenbendazole 兩篇文獻的完整內容與研究設計。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

