---
layout: default
title: Etelcalcetide
parent: 中證據等級 (L3-L4)
nav_order: 344
evidence_level: L3
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

證據等級: **L3** | 預測適應症: **4** 個
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

# Etelcalcetide：從副甲狀腺機能亢進到高磷血症

## 一句話總結

Etelcalcetide 是一種靜脈注射的擬鈣劑（calcimimetic），原本用於治療副甲狀腺機能亢進（hyperparathyroidism）。
TxGNN 模型預測它可能對**高磷血症 (Hyperphosphatemia)** 有效，
目前**沒有臨床試驗登記**，但有 **6 篇文獻**與此方向相關，其中多數談的是透析病人的繼發性副甲狀腺機能亢進，直接證據有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 副甲狀腺機能亢進 (Hyperparathyroidism) |
| 預測新適應症 | 高磷血症 (Hyperphosphatemia) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Etelcalcetide 屬於擬鈣劑，會活化副甲狀腺細胞上的鈣敏感受體（CaSR），進而降低副甲狀腺素（PTH）。

PTH 下降後，骨轉換減少，鈣與磷從骨骼釋出的量也可能隨之降低，因此血磷有機會間接下降。高磷血症與慢性腎臟病的礦物質與骨骼疾病（CKD-MBD）密切相關，和 Etelcalcetide 原本使用的情境相同。

不過要特別留意：這個效果是**間接**的，來自 PTH 與鈣磷平衡的改變，並不是直接結合或排除磷。Etelcalcetide 並非已確立的降磷藥物，這個預測目前屬於合理的研究假說，還不是臨床上可採用的結論。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney Int Rep | DUET 試驗：評估 Etelcalcetide 用於血液透析病人繼發性副甲狀腺機能亢進的控制效果 |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | Int J Nephrol Renovasc Dis | Etelcalcetide 於每次血液透析結束時靜脈給藥，臨床試驗中可有效降低 PTH |
| [42495460](https://pubmed.ncbi.nlm.nih.gov/42495460/) | 2026 | Review | Cureus | 回顧透析病人繼發性副甲狀腺機能亢進的藥物治療，涵蓋擬鈣劑、維生素 D 類似物與磷結合劑 |
| [42044867](https://pubmed.ncbi.nlm.nih.gov/42044867/) | 2026 | 前臨床/機轉研究 | Kidney Int | Etelcalcetide 在慢性高磷血症情境下，經由 CaSR-cAMP 活化改善心臟功能 |
| [42853437](https://pubmed.ncbi.nlm.nih.gov/42853437/) | 2026 | Case report | CEN Case Rep | 血液透析病人由 cinacalcet 換成 Etelcalcetide 後，尿毒症性腫瘤樣鈣化消退 |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case report | Clin Nephrol | 腹膜透析合併副甲狀腺機能亢進病人出現暫時性轉移性肺鈣化 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65659 | PARSABIV SOLUTION FOR INJECTION 5 MG/1 ML | 注射液 | 無資料 |
| HK-65657 | PARSABIV SOLUTION FOR INJECTION 10 MG/2 ML | 注射液 | 無資料 |
| HK-65658 | PARSABIV SOLUTION FOR INJECTION 2.5 MG/0.5 ML | 注射液 | 無資料 |

## 安全性考量

- **藥物交互作用**：已查得 21 筆交互作用，其中絕大多數為「嚴重（Major）」等級，1 筆為「中度（Moderate）」。主要包括：
  - 其他擬鈣劑：Cinacalcet
  - 雙磷酸鹽類：Alendronic acid、Risedronic acid、Ibandronate、Pamidronic acid、Zoledronic acid、Etidronic acid、Tiludronic acid
  - 骨質相關生物製劑：Denosumab、Romosozumab、Salmon calcitonin；Burosumab 為中度
  - 利尿劑：Furosemide、Bumetanide、Torasemide、Etacrynic acid
  - 其他：Cisplatin、Foscarnet、Pentamidine、Amifostine

  這些藥物多與血鈣下降或電解質失衡風險有關，合併使用時需密切監測血鈣。

其餘警語與禁忌症資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何針對高磷血症的臨床試驗，現有文獻多為繼發性副甲狀腺機能亢進的研究、病例報告與前臨床研究，並未直接證明可降低血磷。
- 降磷效果僅是透過 PTH 的間接作用推測而來，且 Etelcalcetide 並非已確立的降磷藥物。

**若要推進需要：**
- 取得 Etelcalcetide 的詳細作用機轉資料（MOA）
- 取得香港衛生署核准的仿單，確認核准適應症、警語與禁忌症
- 分析既有 Etelcalcetide 臨床試驗中血磷的次要療效指標，評估降磷效果的大小
- 若數據支持，設計以血磷為主要終點的臨床試驗，並與磷結合劑做比較
- 擬定合併雙磷酸鹽、利尿劑等藥物時的血鈣與電解質監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

