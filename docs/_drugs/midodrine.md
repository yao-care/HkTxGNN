---
layout: default
title: Midodrine
parent: 僅模型預測 (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrine：從（原適應症資料缺漏）到變異性蛋白酶敏感型普里昂病

## 一句話總結

Midodrine（米多君）在香港已上市，但本次資料中沒有原適應症。
TxGNN 預測它可能對**變異性蛋白酶敏感型普里昂病 (Variably Protease-Sensitive Prionopathy)** 有效。
這項預測**沒有任何臨床試驗或文獻支持**，只是模型輸出，建議 **Hold**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 變異性蛋白酶敏感型普里昂病 (Variably Protease-Sensitive Prionopathy) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 欄位為資料缺口）。
已知 Midodrine 是前驅藥，活性代謝物 desglymidodrine 是周邊 α1 腎上腺素受體促效劑，作用是收縮血管、提高站立血壓。

普里昂病是蛋白質錯誤摺疊造成的神經退化疾病。周邊 α1 促效作用和它的病理機轉沒有已知關聯。
因此這個高分較可能是知識圖譜的統計假象，機轉上看不出合理性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68204 | MIDODRINE SUBSTIPHARM TABLETS 2.5MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-68183 | MIDORINE TABLETS 2.5MG | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-67094 | MIDODRINE HYDROCHLORIDE TABLETS USP 2.5MG | I & C (HONG KONG) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症

Evidence Pack 另有 9 個預測。多數只有模型分數，其中**低血壓相關疾病**的證據最多。

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|------|-----------|------|---------|------|
| 2 | 面指趾生殖器症候群 | 99.95% | L5 | Hold |
| 3 | 注意力不足過動症 (ADHD) | 99.94% | L4 | Hold |
| 4 | 低血壓性疾病 (Hypotensive disorder) | 99.90% | L1（見下方說明） | Proceed with Guardrails |
| 5 | ADHD，注意力不足型 | 99.86% | L5 | Hold |
| 6 | 竇房結疾病 | 99.77% | L4 | Hold |
| 7 | 單基因肥胖 | 99.71% | L5 | Hold |
| 8 | 特定發展障礙 | 99.70% | L5 | Hold |
| 9 | 過時詞條：眼距過寬 | 99.69% | L5 | Hold（建議自候選清單排除） |
| 10 | 竇房阻滯 | 99.66% | L5 | Hold |

- **ADHD（排名 3、5）**：機轉上只有間接關聯（去甲腎上腺素調節），但 Midodrine 主要作用在周邊，中樞穿透有限。檢索到的資料談的是姿勢性調節障礙，沒有在 ADHD 測試 Midodrine。
- **竇房結疾病與竇房阻滯（排名 6、10）**：Midodrine 可能引起反射性心搏過緩，在這些疾病中屬於安全性疑慮，不是治療理由。

### 排名 4：低血壓性疾病

這是證據最多的方向，但本質上接近既有或仿單適應症，不是真正的老藥新用。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02307565](https://clinicaltrials.gov/study/NCT02307565) | Phase 3 | 完成 | 19 | 脊髓損傷患者的血壓、腦血流與認知 |
| [NCT06405555](https://clinicaltrials.gov/study/NCT06405555) | Phase 2/3 | 招募中 | 56 | 低血壓的 HFrEF 患者使用 Midodrine（尚無結果） |
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Phase 2 | 完成 | 21 | 脊髓損傷低血壓患者血壓正常化對腦血流的影響 |
| [NCT05548985](https://clinicaltrials.gov/study/NCT05548985) | NA | 完成 | 58 | 口服 Midodrine 預防髖關節置換術脊髓麻醉後低血壓 |
| [NCT03431194](https://clinicaltrials.gov/study/NCT03431194) | NA | 完成 | 80 | Midodrine 處理重症急性腎損傷患者的透析中低血壓 |

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | RCT | Hepatology | 肝腎症候群：Terlipressin＋白蛋白 vs Midodrine＋Octreotide＋白蛋白 |
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Guideline | Hypertension | 美國心臟協會：高血壓成人的姿勢性低血壓科學聲明 |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | 2020 | Review | Auton Neurosci | 姿勢性低血壓的藥物治療 |
| [2480881](https://pubmed.ncbi.nlm.nih.gov/2480881/) | 1989 | Review | Drugs | Midodrine 的藥理特性，及其在姿勢性低血壓與繼發性低血壓的治療用途 |

**須注意：**
- Evidence Pack 標為 L1，但依本報告的判定規則，只有 1 個已完成的 Phase 3 試驗（NCT02307565，n=19），較接近 L2。
- 部分試驗的藥物組別是從標題推定，不是確認。

**使用上的防護重點：** 仰臥型高血壓、尿滯留、心搏過緩；心衰竭、腎功能不全、嚴重心臟疾病需謹慎。

## 結論與下一步

**決策：Hold**（針對排名 1：變異性蛋白酶敏感型普里昂病）

**理由：**
- 沒有任何臨床試驗或文獻，機轉上也看不出關聯，高分很可能是知識圖譜的假象。
- 值得追蹤的是低血壓方向（排名 4）。它接近既有用途，若要評估宜另案處理。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌症（DG001，為阻擋性缺口，目前無法進入 S1 安全性篩選）
- 從 DrugBank 補上作用機轉資料（DG002）
- 補上香港許可證的核准適應症，以確認原適應症
- 排名 4 需確認各試驗的藥物組別，並評估是否有實質的新用途價值

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

