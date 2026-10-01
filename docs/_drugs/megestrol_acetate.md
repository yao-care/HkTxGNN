---
layout: default
title: Megestrol Acetate
parent: 高證據等級 (L1-L2)
nav_order: 549
evidence_level: L2
indication_count: 5
---

# Megestrol Acetate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Megestrol Acetate：從黃體素類藥物到子宮體子宮內膜癌

## 一句話總結

Megestrol Acetate（甲地孕酮）是合成黃體素，香港已有多張許可證上市，但許可證資料未登載原核准適應症。
TxGNN 模型預測它可能對**子宮體子宮內膜癌 (Uterine Corpus Endometrial Carcinoma)** 有效。
目前有 **3 個臨床試驗**支持，**0 篇直接文獻**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 子宮體子宮內膜癌 (Uterine Corpus Endometrial Carcinoma) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，原適應症也未登載。Megestrol Acetate 是合成黃體素，屬黃體素類藥物。黃體素療法在有荷爾蒙反應的子宮內膜樣癌（黃體素受體陽性）上，機轉上合理。

TxGNN 的預測分數很高（99.94%）。三個已登記的試驗中，兩個是使用黃體素類藥物的 Phase 2 隨機試驗。

需要注意，這個關聯目前主要建立在藥物類別的機轉推論和試驗登記上，並非來自 DrugBank 整理的機轉資料。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | 完成 | 73 | 晚期、持續或復發性子宮內膜癌：Temsirolimus 單用，對比 Temsirolimus 加荷爾蒙療法（含 Megestrol Acetate 與 Tamoxifen）。Megestrol 是對照組的一部分，並非主要試驗藥物 |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | 提前終止 | 9 | 比較持續與週期性黃體素療法，用於想保留子宮的子宮內膜上皮內瘤變或非典型增生患者。僅收 9 人，無法得出療效結論 |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | 未知 | 60 | PD-1 抑制劑加黃體素，對比單用黃體素，用於想保留生育力的早期子宮內膜癌。無法確認所用黃體素是否為 Megestrol，屬探索性研究 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 6 張許可證，以下列出 5 張。許可證資料未登載劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60399 | MEGESIN TAB 160MG | Teva Pharmaceutical Hong Kong |
| HK-44293 | MEGAPLEX TAB 40MG | Teva Pharmaceutical Hong Kong |
| HK-68146 | MEGEJOHN TABLETS 40MG | Synmosa Biopharma (Hong Kong) |
| HK-68644 | MEGESIA TABLETS 40MG | SB Pharma |
| HK-42289 | APO-MEGESTROL TAB 40MG | Hind Wing |

## 安全性考量

安全性資訊請參考原廠仿單。目前查無藥物交互作用資料。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有一個已完成的 Phase 2 隨機試驗（NCT00729586）涉及 Megestrol 相關的荷爾蒙療法，且黃體素療法用於子宮內膜癌在機轉上合理。
- 但 Megestrol 在該試驗中只是對照組的一部分，其他試驗也不是規模夠大的確證性試驗。目前沒有直接文獻，安全性資料也缺乏，不宜直接推進。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症，這是目前的阻擋項目。
- 補充 DrugBank 的作用機轉與原適應症資料。
- 確認 NCT00729586 的 Megestrol 組別結果，並確認 NCT04046185、NCT00503581 所用的黃體素是否為 Megestrol。
- 限定在黃體素受體陽性、子宮內膜樣組織型的族群，並檢查受體狀態。

**其他預測適應症：**
- 子宮內膜移行細胞癌、遺傳性乳癌卵巢癌症候群、卵巢交界性上皮腫瘤：無試驗，或文獻並未評估黃體素療法，建議 Hold。
- 子宮癌肉瘤：僅有間接的荷爾蒙受體文獻，列為研究問題，需先確認受體狀態。

本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

