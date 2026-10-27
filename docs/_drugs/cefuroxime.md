---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefuroxime：預測新適應症為高澱粉酶血症 (Hyperamylasemia)（證據等級 L5）。原適應症：感染性中耳炎、鏈球菌感染、細菌性肺炎、細菌性腦膜炎、淋病、萊姆病等"
monitor_inn: "CEFUROXIME"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "urinary tract infection (disease)", "premalignant hematological system disease", "monoclonal gammopathy", "suppurative otitis media", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Cefuroxime
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

## Cefuroxime：從細菌感染症到高澱粉酶血症（TxGNN 首位預測）
{: .text-alpha }

> 註：TxGNN 分數最高的預測（高澱粉酶血症）缺乏任何證據支持。本報告以首位預測作為標題與快速總覽，並於後文說明證據較完整的替代方向（泌尿道感染）。

## 一句話總結

Cefuroxime 是第二代頭孢子菌素類抗生素，原本用於中耳炎、肺炎、腦膜炎、淋病、萊姆病等細菌感染。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個預測，屬於純模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 感染性中耳炎、鏈球菌感染、細菌性肺炎、細菌性腦膜炎、淋病、萊姆病等（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Cefuroxime 屬於 β-內醯胺類抗生素，一般認為是透過抑制細菌細胞壁合成而殺菌。

高澱粉酶血症是一種生化檢驗異常，並非細菌感染，沒有可供抗生素作用的細菌標的。因此，這個預測在機轉上**缺乏可信的關聯**。高分數可能只是知識圖譜結構（例如共享的節點關係）造成的假象，而非治療上的相關性。

排名第 2 至 10 的預測中，多數同樣沒有合理機轉（如多株性高黏滯症候群、先天性無白蛋白血症、血型不相容等）。較有生物學合理性的是**泌尿道感染**與**化膿性中耳炎**，但兩者本質上是現有抗菌適應症的延伸，並非真正的藥物再利用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

### 補充：較有證據的替代預測（泌尿道感染，排名第 6）

此預測的 TxGNN 分數為 99.62%，證據等級 L3，是前 10 名中證據較完整的方向之一。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | 完成 | 973 | 住院腎盂腎炎患者使用不適當 cefuroxime 治療的影響（觀察性為主） |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | 完成 | 220 | 反覆泌尿道感染孕婦產褥期的預防性抗生素 |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | 未知 | 1000 | 導尿管拔除時預防性抗生素 |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | 未知 | 150 | 微創上泌尿道取石術前抗菌預防 |

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | 隨機對照試驗 | Infection | 比較 aztreonam 與 cefuroxime 用於革蘭氏陰性菌上泌尿道感染 |
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | 系統性回顧 | Pharmacotherapy | 口服 β-內醯胺類用於複雜性泌尿道感染，與 TMP/SMX、氟喹諾酮比較 |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | 隨機試驗 | Lancet Infect Dis | 腸內菌科菌血症由抗綠膿桿菌 β-內醯胺降階的非劣性試驗 |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Review | Drugs | Cefuroxime axetil 的抗菌活性、藥動學與療效回顧 |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Review | Pharmacotherapy | Cefuroxime 的機轉、臨床應用與不良反應 |

## 香港上市資訊

香港共有 20 張有效單一成分許可證，皆為已上市狀態。資料中未提供劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-29697 | ZINNAT TAB 500MG（Sandoz） | 錠劑 | 資料未提供 |
| HK-07015 | ZINACEF FOR INJ 1.5G（Sandoz） | 注射劑 | 資料未提供 |
| HK-52841 | CEFUROXIME SODIUM FOR INJ 750MG（Jindun） | 注射劑 | 資料未提供 |
| HK-61702 | AXCEF TABLETS 250MG（LSB） | 錠劑 | 資料未提供 |
| HK-59220 | CEFUXIME 500 TAB 500MG（Aurobindo） | 錠劑 | 資料未提供 |

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、凝血疾病、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、先天性凝血酶原缺乏。此為圖譜關聯，並非仿單原文。
- **藥物交互作用**：共查得 100 筆，以下為部分中度交互作用：
  - 制酸與抑制胃酸藥物：famotidine、ranitidine、cimetidine、nizatidine、omeprazole、esomeprazole、lansoprazole、pantoprazole、rabeprazole、dexlansoprazole、氫氧化鋁、碳酸鈣、鎂鹽類
  - 胺基糖苷類：kanamycin、neomycin
  - 其他：balsalazide

其餘警語與禁忌資料缺失，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測「高澱粉酶血症」只有模型分數，沒有任何試驗或文獻，也缺乏合理機轉，屬證據等級 L5。
- 較有合理性的泌尿道感染與化膿性中耳炎，多為現有抗菌適應症的延伸，不構成新的再利用機會。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，以及香港衛生署仿單中的警語、禁忌與核准適應症。
- 若有意探索，建議改以泌尿道感染（排名第 6）為研究問題，並設計 cefuroxime 專屬的對照試驗。
- 排除圖譜假象：對高分但無證據的預測（如高澱粉酶血症、高黏滯症候群）做人工複核。
- 使用於腎、肝功能不全或凝血異常族群前，需先進行安全性評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

