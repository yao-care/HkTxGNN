---
layout: default
title: Etelcalcetide
parent: 中證據等級 (L3-L4)
nav_order: 339
evidence_level: L4
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

# Etelcalcetide：從次發性副甲狀腺功能亢進到高磷血症

## 一句話總結

Etelcalcetide 是靜脈注射的擬鈣劑（鈣敏感受體促效劑），一般用於血液透析患者的次發性副甲狀腺功能亢進（此適應症依一般藥理知識，登記資料未載明）。
TxGNN 模型預測它可能對**高磷血症 (Hyperphosphatemia)** 有效，目前有 **1 個臨床試驗**（間接證據）和 **3 篇文獻**，但都沒有直接證明它能治療高磷血症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 次發性副甲狀腺功能亢進（依一般藥理知識，香港許可證未載明適應症文字） |
| 預測新適應症 | 高磷血症 (Hyperphosphatemia) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。以下說明來自一般藥理知識，並非登記資料。Etelcalcetide 是擬鈣劑，作用於鈣敏感受體，降低副甲狀腺素 (PTH)。PTH 下降後，血清鈣與磷通常也會跟著下降，所以對血磷有間接影響是合理的。

高磷血症在慢性腎臟病的礦物質與骨骼異常 (CKD-MBD) 中，通常與次發性副甲狀腺功能亢進一起處理，很少是單獨的治療目標。血磷的變化也會被磷結合劑、活性維生素 D 和透析處方干擾，很難歸因於 etelcalcetide。

目前沒有直接證據顯示 etelcalcetide 能以高磷血症作為主要適應症。要判斷臨床價值，需要先設計以血磷為預先設定終點的研究。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | 不適用 | 完成 | 21 | 探討活性維生素 D 與 etelcalcetide 對慢性腎臟病患者人類蝕骨細胞的影響。屬機轉研究，不是治療試驗，也沒有血磷終點，只能提供間接支持。 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney International Reports | DUET 試驗，評估 etelcalcetide 控制血液透析患者次發性副甲狀腺功能亢進的療效。主題是 SHPT，不是高磷血症。 |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | International Journal of Nephrology and Renovascular Disease | 回顧 etelcalcetide 在血液透析患者次發性副甲狀腺功能亢進的角色。它在每次透析結束時靜脈給藥，每週三次，可有效降低 PTH。 |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case report | Clinical Nephrology | 一名腹膜透析患者因副甲狀腺功能亢進出現暫時性轉移性肺鈣化的個案。與 CKD-MBD 相關，但不是藥效證據。 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 製造商 |
|---------|------|------|--------|
| HK-65659 | PARSABIV SOLUTION FOR INJECTION 5 MG/1 ML | 注射液 | AMGEN HONG KONG LIMITED |
| HK-65657 | PARSABIV SOLUTION FOR INJECTION 10 MG/2 ML | 注射液 | AMGEN HONG KONG LIMITED |
| HK-65658 | PARSABIV SOLUTION FOR INJECTION 2.5 MG/0.5 ML | 注射液 | AMGEN HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，本次預測的其他候選適應症評估中提到，etelcalcetide 仿單有上消化道出血的警語（此點未經本次資料核實）。若用於有出血風險的族群，需特別謹慎。

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 證據只有一個間接的機轉研究和幾篇 SHPT 相關文獻，沒有以高磷血症為終點的直接證據。血磷變化也難以與併用的磷結合劑、維生素 D 類似物和透析處方區分。
- 香港藥品安全性資料（仿單警語與禁忌）缺漏，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌資料
- 補充作用機轉資料（如查詢 DrugBank）
- 以血清磷為預先設定的主要終點，設計或檢索相關研究，並控制磷結合劑與透析處方的干擾
- 其他預測適應症（食道靜脈曲張出血、食道靜脈曲張未出血、靜脈曲張疾病）只有模型分數，沒有任何臨床或文獻證據，機轉上也缺乏合理連結，很可能是知識圖譜的假象，建議維持 Hold

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

