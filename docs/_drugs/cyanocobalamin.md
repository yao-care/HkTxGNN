---
layout: default
title: Cyanocobalamin
parent: 中證據等級 (L3-L4)
nav_order: 228
evidence_level: L4
indication_count: 1
---

# Cyanocobalamin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Cyanocobalamin：從維生素 B12 製劑到生物素代謝疾病

## 一句話總結

Cyanocobalamin（氰鈷胺，維生素 B12）在香港以注射劑、錠劑與眼用溶液等形式上市，但現有資料中沒有記載原適應症。
TxGNN 模型預測它可能對**生物素代謝疾病 (Biotin Metabolic Disease)** 有效。
目前有 **15 個相關臨床試驗**和 **20 篇文獻**，但**沒有任何一項直接證明**它能治療此疾病，證據等級僅為 L4。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 生物素代謝疾病 (Biotin Metabolic Disease) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Cyanocobalamin 是維生素 B12 的一種形式，屬於維生素輔因子類藥物。它的原適應症在現有資料中未載明，因此無法獨立驗證機轉。

不過，兩者在代謝路徑上有關聯。生物素是丙醯輔酶 A 羧化酶 (propionyl-CoA carboxylase) 的輔因子，腺苷鈷胺 (adenosylcobalamin) 則是下一個酵素甲基丙二醯輔酶 A 變位酶 (methylmalonyl-CoA mutase) 的輔因子。兩者都參與丙酸與支鏈胺基酸的粒線體代謝，也都出現在「維生素反應性疾病」的回顧文獻中（PMID 23622402、11031989）。

需要注意的是，這只是**路徑相鄰的關聯**。生物素依賴性疾病（如生物素酶缺乏症、全羧化酶合成酶缺乏症）的標準治療是生物素本身。提供的資料中，沒有任何來源顯示 cyanocobalamin 能治療原發性生物素代謝缺陷。0.996 的預測分數來自知識圖譜，不是臨床證據。

## 臨床試驗證據

以下試驗依相關性排序。沒有任何一項是以 cyanocobalamin 治療生物素代謝疾病。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | NA | 已終止 | 5 | 術前補充纖維與生物素以改善減重手術腸道菌相；生物素為介入，但僅收 5 人即終止，未測試 cyanocobalamin |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | 完成 | 75 | 維生素與礦物質補充對第二型糖尿病神經與腎臟併發症的影響；疾病不同，屬間接證據 |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | 完成 | 33 | Carglumic acid 用於丙酸血症或甲基丙二酸血症的長期療效；藥物不同，但疾病位於相鄰的代謝路徑 |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | 未知 | 1000 | 強化食品改善營養不良兒童的微量營養素狀態（含血清維生素 B12）；屬營養補充，非代謝缺陷 |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | NA | 完成 | 30 | 天然與合成維生素 B 群的生體可用率比較（健康受試者） |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | NA | 完成 | 39 | 針對自閉症氧化壓力與代謝異常的營養介入；與適應症關聯間接 |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | NA | 完成 | 202 | 綜合維生素/礦物質補充對衝動與攻擊行為的影響；與適應症無直接關聯 |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | NA | 未知 | 200 | Q10 ubiquinol 加維生素 B、E 複合物用於自閉症；無證據針對生物素代謝疾病 |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | 完成 | 6824 | 新生兒基因體篩檢計畫，可能篩出先天代謝異常，但未測試任何治療 |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | 完成 | 99 | 減重手術後經皮維生素貼片的吸收與缺乏情形 |

## 文獻證據

沒有找到 RCT，以下依綜述優先、其後為其他研究排列。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | 回顧鈷胺素、葉酸、生物素等維生素反應性疾病，以及相關先天代謝缺陷 |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | 維生素 B12 缺乏與神經系統：B12 為琥珀醯輔酶 A 與甲硫胺酸合成的輔因子 |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | 維生素依賴症候群回顧（無摘要） |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminol Enzymol | 維生素透過吸收不良、代謝錯誤與維生素依賴症候群影響代謝疾病 |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatr Clin North Am | 對維生素有反應的胺基酸代謝異常；建議以維生素進行治療性試驗 |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | 臨床代謝研究 | Pediatr Res | 以 13C 丙酸研究丙酸代謝異常患者，含 4 位對 B12 有反應的甲基丙二酸血症患者 |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | 未分類 | Adv Clin Chem | 維生素反應性先天代謝異常（無摘要） |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | 前臨床 | J Endocrinol | 大鼠 B12 缺乏導致葡萄糖不耐受並促進酮體生成 |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | 維生素與第二型糖尿病的關係 |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterol Clin North Am | 發炎性腸道疾病中的維生素與礦物質缺乏及補充 |

## 香港上市資訊

共 20 張許可證，以下列出 5 張。現有資料未提供劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-63076 | VIDALIC B12 SOLUTION FOR INJECTION 2000MCG/ML | DELTAPHARM LIMITED |
| HK-12579 | BITAMIN INJ 1000MCG/ML | MOUNTAIN TRADING CO LTD |
| HK-56543 | VITAMIN B12 INJ 1000MCG/ML | DELTAPHARM LIMITED |
| HK-26263 | NEO-ACTIVE VITAMIN B12 TAB 100MCG | CHRISTO PHARM LTD |
| HK-46964 | COBAMIN OPHTHALMIC SOLUTION 0.02% | SANTEN PHARMACEUTICAL (HONG KONG) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢未找到相關記錄。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測只有知識圖譜分數和路徑相鄰的機轉推論支持，沒有任何試驗或文獻顯示 cyanocobalamin 能治療生物素代謝疾病。
- 這類疾病的標準治療是生物素本身，且原適應症、作用機轉與安全性資料均缺漏，無法進入安全性篩選。

**若要推進需要：**
- 從香港衞生署取得仿單，補齊警語、禁忌症與核准適應症。
- 補充 DrugBank 的作用機轉資料，重新檢視機轉連結。
- 尋找 cyanocobalamin 用於生物素代謝缺陷的直接臨床或病例證據，並與代謝科專家討論其相對於生物素的價值。
- 評估此預測是否可能是知識圖譜中維生素類藥物相互關聯所造成的假訊號。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

