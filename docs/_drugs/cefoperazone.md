---
layout: default
title: Cefoperazone
parent: 高證據等級 (L1-L2)
nav_order: 171
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefoperazone：預測新適應症為肺炎 (Pneumonia)（證據等級 L1）。原適應症：資料中未提供許可證核准適應症文字"
monitor_inn: "CEFOPERAZONE"
predicted_indications: ["sclerosing cholangitis", "rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "gout", "bronchitis", "meningococcal infection", "infectious otitis media", "IgG4-related sclerosing cholangitis"]
---

# Cefoperazone
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Cefoperazone：從細菌感染到肺炎

## 一句話總結

Cefoperazone 是第三代頭孢菌素類抗生素，在香港以單方及與 sulbactam 的複方注射劑上市。
TxGNN 模型預測它可能對**肺炎 (Pneumonia)** 有效，目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含 2 項隨機對照試驗。
需注意：肺炎本來就屬於抗生素的使用範圍，嚴格來說較接近既有用途的延伸，而非全新的再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未提供許可證核准適應症文字 |
| 預測新適應症 | 肺炎 (Pneumonia) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

**說明：**排名第 1 的預測為硬化性膽管炎（分數 99.98%），但完全沒有臨床試驗與文獻支持，屬於僅有模型預測（L5）。本報告改以證據最完整的**肺炎**為主要評估對象。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。根據已知資訊，Cefoperazone 是第三代頭孢菌素，具抗綠膿桿菌活性，一般認為是透過結合青黴素結合蛋白（PBP）、抑制細菌細胞壁合成而殺菌。

它常與 sulbactam（β-內醯胺酶抑制劑）合用。Sulbactam 本身對鮑氏不動桿菌 (*Acinetobacter baumannii*) 也有內在活性，因此複方能涵蓋醫院內感染及多重抗藥性病原體。

肺炎是細菌感染，與抗生素的作用相符。已有隨機試驗將 cefoperazone-sulbactam 與 cefepime、piperacillin-tazobactam 比較，用於院內肺炎。需留意，目前證據主要針對 **sulbactam 複方**，而非單用 cefoperazone。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07671755](https://clinicaltrials.gov/study/NCT07671755) | 不適用 (NA) | 完成 | 80 | Colistin 單用 vs. colistin 併用 cefoperazone-sulbactam，治療多重抗藥鮑氏不動桿菌呼吸器相關肺炎；與該複方直接相關，但設計與結果未載明 |
| [NCT02060149](https://clinicaltrials.gov/study/NCT02060149) | Phase 1/2 | 未知 | 90 | 霧化鹼性溶液輔助 cefoperazone-sulbactam 加 minocycline，治療廣泛抗藥鮑氏不動桿菌肺炎；試驗重點是鹼性溶液，不是 cefoperazone 本身 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31138577](https://pubmed.ncbi.nlm.nih.gov/31138577/) | 2019 | RCT | Antimicrob Agents Chemother | 開放label非劣性試驗：cefoperazone-sulbactam 對比 cefepime，用於院內及醫療照護相關肺炎 |
| [34168466](https://pubmed.ncbi.nlm.nih.gov/34168466/) | 2021 | RCT/臨床比較 | Infect Drug Resist | Cefoperazone-sulbactam 對比 piperacillin-tazobactam，用於院內肺炎與呼吸器相關肺炎 |
| [41110353](https://pubmed.ncbi.nlm.nih.gov/41110353/) | 2025 | RCT | Phytomedicine | 新加大元散治療多重抗藥革蘭氏陰性菌肺炎，並非以 cefoperazone 為主要介入 |
| [17120738](https://pubmed.ncbi.nlm.nih.gov/17120738/) | 2006 | 臨床比較 | J Huazhong Univ Sci Technol | 靜脈 moxifloxacin 對比 cefoperazone 加 azithromycin，用於社區型肺炎（40 人） |
| [6456894](https://pubmed.ncbi.nlm.nih.gov/6456894/) | 1981 | 臨床試驗 | Drugs | 15 例肺炎與 15 例腎盂腎炎，分離菌均對 cefoperazone 敏感 |
| [35685727](https://pubmed.ncbi.nlm.nih.gov/35685727/) | 2022 | 臨床比較 | Evid Based Complement Alternat Med | Polymyxin B、cefoperazone-sulbactam 及 tigecycline 治療多重抗藥鮑氏不動桿菌肺炎（該文後來已被撤稿，應審慎看待） |
| [24726664](https://pubmed.ncbi.nlm.nih.gov/24726664/) | 2014 | 回顧性分析 | Int J Infect Dis | 老年碳青黴烯抗藥鮑氏不動桿菌院內肺炎，並評估 cefoperazone/sulbactam 的體外效果 |
| [41868911](https://pubmed.ncbi.nlm.nih.gov/41868911/) | 2026 | 模型研究 | Am J Transl Res | 肝功能不全患者使用 cefoperazone-sulbactam 的劑量優化 |
| [2671141](https://pubmed.ncbi.nlm.nih.gov/2671141/) | 1989 | Review | Infect Dis Clin North Am | 第三代頭孢菌素回顧，包括 cefoperazone 的抗綠膿桿菌活性 |
| [1754734](https://pubmed.ncbi.nlm.nih.gov/1754734/) | 1991 | 回顧 | Semin Respir Infect | 比較胺基糖苷類與 β-內醯胺類（含 cefoperazone）治療革蘭氏陰性菌肺炎 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61003 | CEFOPERAZONE AND SULBACTAM FOR INJECTION 1G (SHENZHEN LIJIAN) | 注射劑 | 資料中未提供 |
| HK-63480 | SITANDING POWDER FOR SOLUTION FOR INJECTION 1G | 注射劑 | 資料中未提供 |
| HK-56893 | NASPALUN FOR INTRAVENOUS INJ | 靜脈注射劑 | 資料中未提供 |
| HK-32893 | SULPERAZON FOR INJ 500MG/500MG | 注射劑 | 資料中未提供 |

## 安全性考量

- **知識圖譜中的禁忌疾病關聯**（來自模型的藥物-疾病關係，非仿單內容）：肝病、膽囊疾病、凝血疾病、困難梭狀桿菌結腸炎、新生兒壞死性腸炎、先天性凝血酶原缺乏、維生素 K 缺乏出血症、消化系統疾病、腸道疾病。
- **藥物交互作用**：共查得 14 項，皆為中度。主要包括：
  - 抗凝血劑：warfarin、heparin
  - 胺基糖苷類：kanamycin、neomycin、streptomycin、amikacin（含脂質體）、gentamicin
  - 其他：ethanol、chloramphenicol、picosulfuric acid、ethinylestradiol、mycophenolic acid、pemetrexed

仿單的警語與禁忌症資料尚未取得，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 肺炎有 2 項隨機對照試驗（對比 cefepime 及 piperacillin-tazobactam）支持 cefoperazone-sulbactam，且用途符合抗生素類別，屬既有用途的延伸。
- 但證據主要針對 sulbactam 複方，仿單安全性資料尚未取得，因此需附帶限制條件。

**若要推進需要：**
- 取得並解析香港衛生署仿單，確認核准適應症、警語與禁忌症
- 使用前確認病原菌藥物敏感性，並遵循抗生素管理原則
- 針對肝功能不全、凝血異常、併用抗凝血劑或胺基糖苷類的患者建立監測計畫
- 釐清證據是否適用於單方 cefoperazone，或僅適用於 sulbactam 複方
- 補充作用機轉資料

**其他預測的處理建議：**
- **支氣管炎**（L3）、**腦膜炎雙球菌感染**（L3）、**感染性中耳炎**（L4）：證據多為老舊、小型或間接研究，建議 Hold，視為既有抗菌用途的延伸。腦膜炎方面，cefoperazone 的腦脊髓液穿透性不如 ceftriaxone 與 cefotaxime，無優先使用理由。
- **類風濕性關節炎**（L4）：檢索到的文獻僅為感染併發症個案報告，並非針對疾病本身，建議 Hold。
- **硬化性膽管炎、IgG4 相關硬化性膽管炎、痛風、先天發育異常症候群**：僅有模型預測，無證據與合理機轉，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

