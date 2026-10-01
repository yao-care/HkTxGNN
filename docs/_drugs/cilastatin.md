---
layout: default
title: Cilastatin
parent: 中證據等級 (L3-L4)
nav_order: 193
evidence_level: L3
indication_count: 10
---

# Cilastatin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Cilastatin：從細菌感染（複方成分）到金黃色葡萄球菌感染

## 一句話總結

Cilastatin 是 imipenem/cilastatin 複方的成分之一，本身是腎臟脫氫肽酶-I 抑制劑，沒有抗菌活性。
TxGNN 模型預測它可能對**金黃色葡萄球菌感染 (Staphylococcus aureus infection)** 有效，
目前有 **3 個臨床試驗**和 **20 篇文獻**與此方向相關，但療效實際來自 imipenem，並非 cilastatin 本身。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（許可證核准適應症欄位皆為空） |
| 預測新適應症 | 金黃色葡萄球菌感染 (Staphylococcus aureus infection) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold（僅作為研究問題） |

> 補充：所有預測適應症中，證據最強的是**肺炎 (pneumonia)**（L1，多個 Phase 3 RCT，建議 Proceed with Guardrails），詳見下方「其他預測適應症」。但這屬於複方的既有適應症，並非 cilastatin 的新用途。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 尚未取得）。根據文獻，Cilastatin 抑制腎臟刷狀緣的脫氫肽酶-I (DHP-I)，
避免 imipenem 被水解，以維持其尿中與全身暴露量。Cilastatin 本身**不具抗菌活性**。

因此，任何對金黃色葡萄球菌的作用都來自 imipenem。Imipenem/cilastatin 已核准用於敏感的革蘭氏陽性菌感染，
所以這個預測更像是「複方訊號」，不是 cilastatin 的真正老藥新用。
對 MRSA 的活性不穩定，複方主要被當作輔助或合併治療來研究（例如與 fosfomycin、arbekacin、vancomycin 合併）。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | 未知 | 60 | Linezolid 單用或合併 carbapenem 對呼吸機相關肺炎 MRSA 的活性；規模小 |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Phase 2 | 終止 | 108 | Tigecycline 對比 imipenem/cilastatin 治療院內肺炎；非葡萄球菌專屬終點 |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | 完成 | 274 | Imipenem/cilastatin/relebactam 對比 pip/tazo 治療 HABP/VABP；與金黃色葡萄球菌關聯未證實 |

以上試驗皆非直接針對 cilastatin 或金黃色葡萄球菌的療效驗證。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | 臨床研究 | Antimicrob Agents Chemother | 23 例 MSSA/MRSA 感染以 imipenem-cilastatin 治療，評估療效與毒性 |
| [8072190](https://pubmed.ncbi.nlm.nih.gov/8072190/) | 1994 | 臨床研究 | Jpn J Antibiot | Arbekacin 合併 imipenem/cilastatin 對 MRSA 的 MIC 較低，具合併效果 |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | 病例評論 | Antimicrob Agents Chemother | Imipenem/cilastatin 合併 fosfomycin 治療難治性 MRSA 感染 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | 多重抗藥菌感染抗生素仿單外使用與正式建議之比較 |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Review | Int J Antimicrob Agents | MRSA 致病機轉、治療與抗藥性的新進展 |
| [3378959](https://pubmed.ncbi.nlm.nih.gov/3378959/) | 1988 | 動物實驗 | J Antimicrob Chemother | 兔 MRSA 心內膜炎模型中，imipenem-cilastatin 效果優於 vancomycin |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | 體外/動物 | J Antimicrob Chemother | Vancomycin 合併 imipenem 對 MRSA 有協同作用 |
| [8514648](https://pubmed.ncbi.nlm.nih.gov/8514648/) | 1993 | 動物實驗 | J Antimicrob Chemother | Imipenem/cilastatin 合併 cefotiam 對 MRSA 菌血症模型具協同作用 |
| [12878512](https://pubmed.ncbi.nlm.nih.gov/12878512/) | 2003 | 動物實驗 | Antimicrob Agents Chemother | 新頭孢菌素 S-3578 對 MRSA 感染模型；imipenem-cilastatin 活性較弱 |
| [3859208](https://pubmed.ncbi.nlm.nih.gov/3859208/) | 1985 | 臨床研究 | Am J Med | 43 例細菌性肺炎的開放性試驗，評估 imipenem/cilastatin 療效與耐受性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53560 | PREPENEM FOR INJ 500MG | 未提供 | 未提供 |
| HK-61317 | PRIMAGAL POWDER FOR SOLUTION FOR INFUSION 500/500MG | 未提供 | 未提供 |
| HK-66808 | IMCIMILL POWDER FOR SOLUTION FOR INFUSION 500MG/500MG | 未提供 | 未提供 |
| HK-64660 | IMIPENEM/CILASTATIN KABI POWDER FOR SOLUTION FOR INFUSION 500MG/500MG | 未提供 | 未提供 |

## 其他預測適應症

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|-----------|-----------|---------|------|------|
| 肺炎 (pneumonia) | 99.81% | L1 | Proceed with Guardrails | 有多個 Phase 3 RCT（如 RESTORE-IMI 2）；屬複方既有適應症，療效來自 imipenem（含 relebactam）。注意當地抗生素敏感性、carbapenem 管理、癲癇風險 |
| 支氣管炎 (bronchitis) | 99.65% | L3 | Research Question | 1980-90 年代開放性研究；範圍應限於嚴重或抗藥病例 |
| 沙門氏菌感染 (salmonellosis) | 99.43% | L3 | Research Question | 多為 1980 年代兒科研究與個案；有較安全的第一線替代藥 |
| 鼻竇炎 (sinusitis) | 99.88% | L4 | Hold | 僅有間接證據 |
| 慢性鼻竇炎、慢性篩竇炎、副鼻竇腫瘤、副傷寒、瀰漫性硬皮病 | 99.86%–99.89%（副傷寒 99.65%、硬皮病 99.55%） | L5 | Hold | 無臨床試驗或文獻，多為知識圖譜推論的假象 |

## 安全性考量

安全性資訊請參考原廠仿單。（香港衛生署仿單的警語與禁忌資料尚未取得，此為阻擋性資料缺口。）

文獻中另有 imipenem/cilastatin 相關不良反應個案報告：白血球破裂性血管炎 (PMID 9158321)、急性嗜酸性肺炎 (PMID 26944380)。

## 結論與下一步

**決策：Hold**

**理由：**
- Cilastatin 本身沒有抗菌活性，金黃色葡萄球菌的訊號來自 imipenem。證據多為舊的體外、動物與小型臨床研究，對 MRSA 效果不穩定，因此不構成 cilastatin 的真正新適應症。
- 唯一證據充分的方向是肺炎，但那屬於複方既有適應症。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 補齊 DrugBank 作用機轉（MOA）
- 釐清香港各許可證的核准適應症（目前皆為空）
- 確認試驗中 cilastatin 的實際暴露與金黃色葡萄球菌的直接終點
- 若要推進，建議以複方「imipenem/cilastatin」為評估單位，並搭配當地抗生素敏感性資料與 carbapenem 管理

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

