---
layout: default
title: Palmitic Acid
parent: 僅模型預測 (L5)
nav_order: 556
evidence_level: L5
indication_count: 10
---

# Palmitic Acid
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

# Palmitic Acid：無核准適應症藥物的多重訊號初篩，乾眼症為證據等級最高方向

## 一句話總結

Palmitic Acid（棕櫚酸，DrugBank DB03796）是人體內普遍存在的飽和脂肪酸，目前在香港**未上市、無許可證**，DrugBank 也未記錄核准適應症與作用機轉。TxGNN 模型對其掃描出 **10 個**潛在新適應症方向，但整體證據非常薄弱：多數方向僅有模型分數、無任何臨床試驗或文獻佐證（L5），唯一累積到有意義證據的是**乾眼症（Dry Eye Syndrome）**，達到 **L3** 等級並進入 S1（安全性初評）階段，其餘方向皆維持 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無記錄（DrugBank 未列核准適應症，屬內源性脂肪酸而非上市藥品） |
| TxGNN 最高分預測 | non-syndromic esophageal malformation（95.47%，但無任何證據支持） |
| 證據等級最高方向 | 乾眼症 Dry Eye Syndrome（L3，決策階段 S1，建議 Research Question） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

### 十個候選方向總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | non-syndromic esophageal malformation | 95.47% | L5 | Hold |
| 2 | esotropia（內斜視） | 95.22% | L5 | Hold |
| 3 | esophageal disease | 94.81% | L4 | Hold |
| 4 | HER2 positive breast carcinoma | 93.54% | L4 | Hold |
| 5 | atypical coarctation of aorta | 93.02% | L5 | Hold |
| **6** | **dry eye syndrome** | 92.87% | **L3** | **Research Question** |
| 7 | normal breast-like subtype of breast carcinoma | 91.86% | L5 | Hold |
| 8 | progesterone-receptor positive breast cancer | 91.86% | L4 | Hold |
| 9 | breast tumor luminal A or B | 91.84% | L4 | Hold |
| 10 | progesterone-receptor negative breast cancer | 91.76% | L4 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Palmitic Acid 的詳細作用機轉資料（MOA 為 Data Gap）。作為體內普遍存在的飽和脂肪酸，它並非傳統定義下的「藥物」，因此大多數 TxGNN 預測方向（先天性食道畸形、內斜視、主動脈縮窄）在生物學上找不到合理連結，文獻檢索也完全掛零，屬於純模型分數雜訊。

唯一具生理學合理性的方向是**乾眼症**：棕櫚酸是瞼板腺分泌物（meibum）與淚膜脂質層的天然組成成分之一，已有文獻指出瞼板腺功能障礙（MGD）患者的脂肪酸組成與健康人不同（PMID 18156378），淚膜脂質層的物理特性也與棕櫚酸等長鏈脂肪酸的表面張力調控有關（PMID 34958775）。但這些都是「成分關聯」研究，並非「補充/給予棕櫚酸可治療乾眼症」的介入性證據，唯一相關的臨床試驗（NCT02802150）測試的也是山椒籽油口服補充品而非棕櫚酸本身（relevance grade C）。

其餘乳癌相關方向（HER2 陽性、PR 陽性/陰性、Luminal 型）的文獻多為「脂肪酸暴露與癌症風險」的流行病學關聯或體外機轉研究，部分甚至顯示棕櫚酸偏向促癌／脂毒性方向而非治療效果，不支持再利用假說。

---

## 臨床試驗證據（乾眼症方向）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02802150](https://clinicaltrials.gov/study/NCT02802150) | NA | 完成 | 20 | 口服 Zanthoxylum schinifolium 籽油（非棕櫚酸本身）10 週，評估對輕度乾眼症之療效與安全性；間接相關（relevance grade C） |

其餘 9 個預測方向均無相關臨床試驗登記。

---

## 文獻證據（乾眼症方向）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18156378](https://pubmed.ncbi.nlm.nih.gov/18156378/) | 2008 | Cohort（成分分析） | Br J Ophthalmol | 瞼板腺功能障礙與缺水型乾眼症患者的瞼板腺脂肪酸組成有差異 |
| [34958775](https://pubmed.ncbi.nlm.nih.gov/34958775/) | 2022 | 基礎生物物理研究 | Biophysical Journal | 淚膜脂質層的表面張力與流變特性，脂肪酸為關鍵組成 |
| [28420093](https://pubmed.ncbi.nlm.nih.gov/28420093/) | 2017 | Review | Int J Mol Sci | 游離脂肪酸在牙周病與原發性乾燥症候群致病機轉中的潛在角色 |

**其他方向重點文獻（非治療性介入證據）：**
- Esophageal disease（L4）：STING 透過抑制 CPT1A 脂肪酸 β-氧化來抑制食道鱗癌進展（PMID 40394235）——顯示棕櫚酸代謝路徑偏向促癌而非治療角色。
- 乳癌相關方向（L4）：PPAR-γ 保護 ERBB2+ 乳癌細胞免於棕櫚酸誘導之脂毒性（PMID 19298655），暗示棕櫚酸可能對此類細胞具細胞毒性，但為體外機轉研究，方向性複雜。
- 需注意 rank 9（breast tumor luminal A/B）之 19 篇檢索結果中，僅 1 篇（PMID 41193432，棕櫚酸誘導 UPR 維持 TNBC 侵襲性）與棕櫚酸真正相關，其餘 18 篇為「B」關鍵字誤匹配（B 細胞發育、B 型肝炎疫苗等不相關文獻），檢索品質需留意。

---

## 安全性考量

安全性資訊請參考原廠仿單。TFDA/香港仿單警語與禁忌症資料目前為 Blocking 等級資料缺口（DG001），無法進行 S1 安全性初評的完整判斷。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Palmitic Acid 在香港未上市、無許可證、無記錄之核准適應症，也缺乏 MOA 資料，作為再利用候選藥物的基礎資訊嚴重不足。
- 10 個預測方向中僅乾眼症達到 L3 證據等級，其餘皆為 L4-L5，且多為關聯性/機轉研究而非治療性介入證據；部分文獻甚至顯示棕櫚酸代謝路徑偏向促癌方向。

**若要推進需要：**
- 補齊 MOA 與 TFDA/仿單安全性資料（DG001、DG002），解除 Blocking 缺口。
- 針對乾眼症方向，尋找棕櫚酸（或其醫藥劑型如局部用配方）直接介入性臨床證據，而非替代脂肪酸補充品的間接證據。
- 釐清 Palmitic Acid 作為「藥物」候選的定位（賦形劑/內源性代謝物 vs. 治療性藥物），評估是否適合納入本專案的再利用篩選流程。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

