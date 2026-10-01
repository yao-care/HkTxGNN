---
layout: default
title: Cefoperazone
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Cefoperazone
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

# Cefoperazone：從細菌感染到肺炎

## 一句話總結

Cefoperazone 是第三代頭孢菌素類抗生素，在香港以單方或與 sulbactam 複方注射劑上市。
TxGNN 模型預測分數最高的是**硬化性膽管炎**，但該項僅為模型預測、毫無研究支持；證據最完整的是**肺炎 (Pneumonia)**，有 **2 個臨床試驗**和 **20 篇文獻**（其中 1 篇已撤稿）。
肺炎本身落在抗菌譜範圍內，較接近既有用途而非真正的老藥新用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未提供（許可證資料中的核准適應症皆為空白） |
| 預測新適應症 | 肺炎 (Pneumonia)，為證據最完整的候選；TxGNN 排名第 1 者為硬化性膽管炎 |
| TxGNN 預測分數 | 肺炎 99.93%（硬化性膽管炎 99.98%） |
| 證據等級 | L1（肺炎；注意事項見下） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails（肺炎）；其餘候選 Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cefoperazone 是第三代頭孢菌素，對多種革蘭氏陰性菌有活性，在香港多以 sulbactam 複方形式使用。

肺炎屬於細菌感染，落在其抗菌譜之內。醫院內感染肺炎與醫療照護相關肺炎已有 cefoperazone-sulbactam 的隨機對照研究。因此這更像是既有抗菌用途的驗證，而非跨疾病類別的再利用。

其他高分預測則缺乏合理機轉：

- **硬化性膽管炎**：cefoperazone 有大量膽汁排泄，可能有助於繼發性細菌性膽管炎。但原發性硬化性膽管炎屬免疫介導疾病，沒有已知抗菌機轉。
- **類風濕性關節炎**：檢索到的 4 篇皆為 RA 病人感染的個案報告，反映的是感染風險，並非療效，很可能是共現造成的假象。
- **痛風、罕見發育異常症候群**：無機轉、無證據，推測為知識圖譜的假象。

---

## 臨床試驗證據（肺炎）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01280461](https://clinicaltrials.gov/study/NCT01280461) | N/A（註冊資料未標示，摘要自稱 Phase 3） | 未知 | 142 | 開放標籤隨機試驗，比較 cefoperazone/sulbactam 與 cefepime 用於醫院內及醫療照護相關肺炎 |
| [NCT02060149](https://clinicaltrials.gov/study/NCT02060149) | Phase 1/2 | 未知 | 90 | 霧化鹼性溶液合併 cefoperazone/sulbactam 加 minocycline，用於廣泛抗藥性鮑氏不動桿菌肺炎；介入重點非 cefoperazone，相關性較低 |

---

## 文獻證據（肺炎）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31138577](https://pubmed.ncbi.nlm.nih.gov/31138577/) | 2019 | RCT | Antimicrob Agents Chemother | Cefoperazone-sulbactam 對比 cefepime 治療 HAP/HCAP 的非劣性隨機試驗 |
| [34168466](https://pubmed.ncbi.nlm.nih.gov/34168466/) | 2021 | RCT | Infect Drug Resist | Cefoperazone-sulbactam 對比 piperacillin-tazobactam 治療 HAP/VAP 的療效比較 |
| [1643821](https://pubmed.ncbi.nlm.nih.gov/1643821/) | 1992 | 隨機試驗 | Diagn Microbiol Infect Dis | 院內肺炎單藥治療，cefoperazone 成功率 80%，ceftriaxone 70%，療效相當 |
| [6456894](https://pubmed.ncbi.nlm.nih.gov/6456894/) | 1981 | 臨床試驗 | Drugs | 肺炎與腎盂腎炎各 15 例，分離菌皆對 cefoperazone 敏感 |
| [34871744](https://pubmed.ncbi.nlm.nih.gov/34871744/) | 2022 | 回溯性比較 | Int J Antimicrob Agents | Cefoperazone-sulbactam 對比 piperacillin-tazobactam 用於老年肺炎 |
| [37443505](https://pubmed.ncbi.nlm.nih.gov/37443505/) | 2023 | 回溯性研究 | Medicine | 815 位重症社區型肺炎病人，比較 cefoperazone-sulbactam 與 piperacillin-tazobactam |
| [29319497](https://pubmed.ncbi.nlm.nih.gov/29319497/) | 2018 | 比較研究 | Int J Clin Pharmacol Ther | Tigecycline 加高劑量 cefoperazone-sulbactam 對比 tigecycline 單用，治療廣泛抗藥鮑氏不動桿菌 VAP |
| [24726664](https://pubmed.ncbi.nlm.nih.gov/24726664/) | 2014 | 世代研究 | Int J Infect Dis | 老年碳青黴烯抗藥鮑氏不動桿菌 HAP，及 cefoperazone/sulbactam 的體外效果 |
| [17120738](https://pubmed.ncbi.nlm.nih.gov/17120738/) | 2006 | 比較研究 | J Huazhong Univ Sci Technol | 靜脈 moxifloxacin 對比 cefoperazone 加 azithromycin 治療社區型肺炎（n=40） |

> ⚠ PMID 35685727 已遭撤稿（撤稿通知為 PMID 38125170），不應納入證據。

---

## 其他預測適應症摘要

| 預測適應症 | TxGNN 分數 | 證據等級 | 決策 | 說明 |
|-----------|-----------|---------|------|------|
| 硬化性膽管炎 | 99.98% | L5 | Hold | 無試驗、無文獻；僅有膽汁排泄的理論推想 |
| 類風濕性關節炎 | 99.97% | L5 | Hold | 4 篇皆為感染個案報告，非療效證據 |
| 支氣管炎 | 99.77% | L3 | 研究問題 | 有 1980–90 年代臨床研究與痰液滲透資料，但年代久遠，未反映現今抗藥性 |
| 腦膜炎雙球菌感染 | 99.51% | L4 | Hold | 僅 1987 年一篇細菌性腦膜炎初步報告，且腦脊髓液滲透有限，非首選 |
| 感染性中耳炎 | 99.50% | L4 | Hold | 文獻無 cefoperazone 療效結果，僅間接證據 |
| IgG4 相關硬化性膽管炎 | 99.48% | L5 | Hold | 屬免疫性疾病，無抗菌機轉、無證據 |
| 痛風 | 99.83% | L5 | Hold | 與尿酸代謝或發炎無已知關聯 |
| 科洛波瘤性小眼症-肢根型骨發育不良症候群 | 99.92% | L5 | Hold | 罕見遺傳疾病，無證據，疑為知識圖譜假象 |
| 短指併指症候群 | 99.90% | L5 | Hold | 罕見先天畸形，無證據，疑為知識圖譜假象 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61003 | CEFOPERAZONE AND SULBACTAM FOR INJECTION 1G (SHENZHEN LIJIAN) | 注射劑 | 未提供 |
| HK-63480 | SITANDING POWDER FOR SOLUTION FOR INJECTION 1G | 注射劑 | 未提供 |
| HK-56893 | NASPALUN FOR INTRAVENOUS INJ | 靜脈注射劑 | 未提供 |
| HK-32893 | SULPERAZON FOR INJ 500MG/500MG（輝瑞） | 注射劑 | 未提供 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（僅限肺炎）；其他所有候選 Hold**

**理由：**
- 肺炎有多項 cefoperazone-sulbactam 的隨機比較研究，機轉合理。但這屬於既有抗菌用途，並非嚴格意義的老藥新用。
- 其餘高分預測（如硬化性膽管炎、類風濕性關節炎、痛風）沒有機轉或臨床證據，僅為模型輸出，不宜推進。

**若要推進需要：**
- 確認證據等級：試驗為複方（含 sulbactam）而非單方，且 NCT01280461 註冊資料階段為 N/A，需查全文核實是否為 Phase 3；也需確認已完成的 Phase 3 RCT 數量是否達 L1 標準。
- 排除已撤稿的 PMID 35685727。
- 依本地抗菌譜與抗藥性資料（特別是碳青黴烯抗藥鮑氏不動桿菌）評估使用。
- 補充香港衛生署仿單的警語、禁忌與核准適應症（目前為阻擋性資料缺口，無法進入安全性篩選）。
- 補充作用機轉資料（DrugBank）。
- 如評估支氣管炎，需現代對照研究或確認現有標示。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

