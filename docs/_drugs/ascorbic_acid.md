---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid（維生素 C）：預測新適應症為非症候群性食道畸形

## 一句話總結

Ascorbic Acid（維生素 C）在香港已有 20 張許可證，但本次資料未提供其原適應症。
TxGNN 模型預測它可能對**非症候群性食道畸形 (Non-syndromic Esophageal Malformation)** 有效，分數很高（99.96%）。
但這個預測目前有 **0 個臨床試驗**和 **0 篇文獻**支持，屬於純模型預測，建議先擱置（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 非症候群性食道畸形 (Non-syndromic Esophageal Malformation) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，原適應症資料也未提供。維生素 C 已知的角色是抗氧化劑，也是膠原蛋白合成的輔因子。

食道畸形是先天性的結構異常，來自胚胎發育過程。目前找不到維生素 C 作用於這類結構性畸形的合理機轉。這個預測較可能是知識圖譜中的關聯訊號，而不是有生物學依據的推論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-49625 | UNITED PUNTAN VITA C EFF TAB 1G (ORANGE) | THE UNITED LABORATORIES LTD |
| HK-44632 | VICIMIN TAB 250MG CHEWABLE ORANGE | ADVANCE PHARMACEUTICAL COMPANY LIMITED |
| HK-49626 | UNITED PUNTAN VITA C EFF TAB 1G BLACKCUR | THE UNITED LABORATORIES LTD |
| HK-06460 | VITAMIN C INJ 500MG/2ML | ATLANTIC PHARMACEUTICAL LIMITED |
| HK-06465 | CECAP CHEWABLE TAB 100MG | ATLANTIC PHARMACEUTICAL LIMITED |

---

## 其他預測適應症（供參考）

第 1 名沒有任何證據，但排名較後的候選有一些研究可看。下表只列有實質證據的項目。

| 排名 | 預測適應症 | 分數 | 證據等級 | 系統建議 | 重點 |
|------|-----------|------|---------|---------|------|
| 2 | 食道疾病 (Esophageal Disease) | 99.90% | L4 | Hold | 抗氧化與抗亞硝化作用有理論基礎，但動物實驗顯示維生素 C 合併亞硝酸鹽可能促進食道致癌，訊號不一致。另有服用維生素 C 錠劑造成食道炎與狹窄的報告。Linxian 營養介入追蹤試驗（[NCT00342654](https://clinicaltrials.gov/study/NCT00342654)，n=32,902）為多種維生素礦物質複方，無法單獨判斷維生素 C 的效果。 |
| 4 | 損傷 (Injury) | 99.60% | L4 | Research Question | 燒傷復甦、急性肺損傷、肌腱與傷口癒合有合理機轉，但「損傷」範圍太廣。直接相關的試驗多為小型或已撤回（如 [NCT00350077](https://clinicaltrials.gov/study/NCT00350077)），文獻多為前臨床或敘述性回顧。 |
| 8 | 周產期疾病 (Perinatal Disease) | 99.47% | L1 | Hold | 有已完成的 Phase 3 RCT（[NCT00097110](https://clinicaltrials.gov/study/NCT00097110)，n=734，維生素 C 加 E 預防子癇前症）。等級只反映試驗存在，不代表有效，而且維生素 C 未與維生素 E 分開評估。系統性回顧（[PMID 21529757](https://pubmed.ncbi.nlm.nih.gov/21529757/)）的結論須另行核實，尤其是可能的妊娠期高血壓與胎膜早破等風險。 |
| 10 | 維生素缺乏症 (Vitamin Deficiency Disorder) | 99.47% | L3 | Proceed with Guardrails | 屬標準營養補充，而非嚴格意義的老藥新用。壞血病回顧（[PMID 37795755](https://pubmed.ncbi.nlm.nih.gov/37795755/)、[PMID 36153722](https://pubmed.ncbi.nlm.nih.gov/36153722/)）提供主要支持。維生素 C 也能促進非血基質鐵吸收。目前沒有單獨評估維生素 C 治療缺乏症的 Phase 3 RCT。 |

第 3、5、6、7、9 名（先天性凝血酶原缺乏、生物素代謝疾病、旺盛性牙骨質骨發育不良、節段性牙上頜發育不良、依亞細胞系統分類的疾病）僅有模型預測或間接證據，目前看不出可行的機轉。第 6、7 名分數完全相同，可能來自圖譜中相近的位置，而不是各自獨立的證據。

---

## 安全性考量

安全性資訊請參考原廠仿單。本次資料中沒有警語、禁忌症與藥物交互作用資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 第 1 名預測（非症候群性食道畸形）沒有任何臨床試驗或文獻，也找不到合理的機轉，不適合推進。
- 香港仿單的警語與禁忌症資料缺漏，屬阻擋性缺口，無法進入安全性篩選。

**若要推進需要：**
- 從香港衛生署下載並解析仿單，補齊警語與禁忌症（DG001）。
- 補充作用機轉與原適應症資料（DG002），例如從 DrugBank 查詢。
- 重新評估候選排序：第 10 名（維生素缺乏症）證據較完整，第 2 名（食道疾病）和第 4 名（損傷）可作為研究問題。第 2 名須先釐清食道致癌的安全疑慮。
- 若要看第 8 名（周產期疾病），須先核實 Phase 3 試驗結果與系統性回顧的結論。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

