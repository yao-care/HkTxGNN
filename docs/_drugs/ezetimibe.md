---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe：從膽固醇吸收抑制劑到高脂蛋白血症

## 一句話總結

Ezetimibe 是抑制腸道膽固醇吸收的降血脂藥，目前已在香港上市。
TxGNN 模型預測它可能對**高脂蛋白血症 (Hyperlipoproteinemia)** 有效，但這個疾病名稱下**沒有臨床試驗**，只有 **19 篇文獻**，其中直接涉及 ezetimibe 的隨機對照試驗僅 1 篇。此外，這項預測與已上市的原用途高度重疊，性質接近既有用途的確認，不是真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 高脂蛋白血症 (Hyperlipoproteinemia) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L2（依規則判定，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

- 香港許可證資料沒有填寫核准適應症文字，所以「原適應症」一欄無法列出。
- Evidence Pack 標示為 L1，但依判定規則，L1 需要至少 2 個已完成的 Phase 3 RCT。此疾病名稱下沒有登記試驗，文獻中只有 1 篇 Phase 3 RCT（TANDEM），因此本報告判定為 L2。

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前缺漏。不過依 Evidence Pack 的推論說明，ezetimibe 抑制 NPC1L1 蛋白介導的腸道膽固醇吸收，藉此降低 LDL-C，且與 statin 的降脂效果可以疊加。

「高脂蛋白血症」是一個涵蓋範圍很廣的疾病名稱，與已上市的原發性高血脂用途高度重疊。因此這項預測比較像是確認既有用途，不算真正的老藥新用。

機轉上，血中脂蛋白（特別是 LDL）升高的情況，抑制腸道膽固醇吸收都可能有幫助，所以預測分數高是合理的。需要注意的是，這個判斷有一個前提：ezetimibe 是否已列在香港核准的適應症內，目前無法從許可證資料確認。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM：Phase 3、雙盲、安慰劑對照，評估 obicetrapib + ezetimibe 固定劑量複方降低 LDL-C 的療效（摘要未提供結果數據） |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | 口服 PCSK9 抑制劑 enlicitide 用於雜合子家族性高膽固醇血症；主角不是 ezetimibe，僅為間接參考 |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Molecular Medicine Reports | 高脂血症藥物研究進展，治療目標為預防與管理動脈粥狀硬化性心血管疾病 |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | 餐後高脂血症的病理機轉、診斷、動脈粥狀硬化成因與治療 |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | 家族性高膽固醇血症常被漏診與治療不足；ezetimibe 列為可降低 LDL-C 的治療選項之一 |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | 家族性高膽固醇血症的盛行率、篩檢與預防策略 |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Current Cardiology Reports | 家族性高膽固醇血症的全球負擔、診斷、風險評估與治療指引 |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | 家族性高膽固醇血症的遺傳成因（LDLR、APOB、PCSK9 等）與心血管風險 |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | PCSK9 抑制劑綜述，適用於 statin 不耐受或未達標者 |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | 共識指引 | European Heart Journal | 歐洲動脈粥狀硬化學會共識：家族性高膽固醇血症的篩檢與治療指引 |

## 香港上市資訊

| 許可證號 | 品名 | 持證商 |
|---------|------|--------|
| HK-51223 | EZETROL TAB 10 MG | ORGANON HONG KONG LIMITED |
| HK-63988 | PMS-EZETIMIBE TABLETS 10MG | TRENTON-BOMA LTD |
| HK-65290 | ALZETIM TABLETS 10MG | APT PHARMA LIMITED |
| HK-66209 | LIPEZ TABLETS 10MG | JACOBSON MARKETING LIMITED |
| HK-68102 | JECEZETIM TABLETS 10MG | JULIUS CHEN & COMPANY (HK) LIMITED |

共 20 張許可證，此處列出 5 張。上述許可證資料未載明劑型與核准適應症文字。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Ezetimibe 已在香港上市，機轉（抑制腸道膽固醇吸收）與高脂蛋白血症的關聯合理。
- 但這個疾病名稱下沒有登記試驗，直接涉及 ezetimibe 的 RCT 也只有 1 篇（複方製劑），證據強度僅屬 L2。
- 香港仿單資料缺漏（Evidence Pack 標為 Blocking），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補上警語與禁忌症，這是進入安全性篩選的前提。
- 對照香港許可證的核准適應症，確認高脂蛋白血症是否已屬標示內用途，再決定是否歸類為老藥新用。
- 補上 DrugBank 的作用機轉資料。
- 補充直接以 ezetimibe 為介入藥物、針對此適應症的對照試驗證據。
- 另外，「家族性高膽固醇血症」（預測第 2 順位）已有多個 ezetimibe 相關 Phase 3 試驗，可另案評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

