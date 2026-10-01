---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine：從淋巴系惡性腫瘤到漿細胞骨髓瘤

## 一句話總結

Fludarabine（氟達拉濱）是嘌呤類似物（purine analog）的細胞毒性化療藥，文獻描述其用於 B 細胞淋巴球性白血病、毛細胞白血病與惰性淋巴瘤。
TxGNN 模型預測它可能對**漿細胞骨髓瘤 (Plasma Cell Myeloma)** 有效。
目前有約 **50 筆臨床試驗**登記，但多數只把它當作 CAR-T 前的淋巴清除或移植前的預處理藥物，**沒有文獻**直接支持這個適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未列載適應症文字；文獻描述為 B 細胞淋巴球性白血病、毛細胞白血病、惰性淋巴瘤 |
| 預測新適應症 | 漿細胞骨髓瘤 (Plasma Cell Myeloma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2（依 Evidence Pack 判定；骨髓瘤相關試驗多為單臂，缺乏直接檢驗 fludarabine 的隨機對照試驗） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold（列為研究問題，待補齊安全性資料） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。已知 fludarabine 是嘌呤類似物，其活性代謝物 F-ara-ATP 會抑制 DNA 聚合酶與核糖核苷酸還原酶，並誘導淋巴細胞凋亡。

漿細胞骨髓瘤與淋巴惡性腫瘤同屬 B 細胞譜系的血液腫瘤，因此抗淋巴細胞的機轉在理論上可能延伸到漿細胞。相關的「惰性漿細胞骨髓瘤」預測項目中，有一篇前臨床研究（[PMID 17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/)，2007 年）顯示，fludarabine 在體外與體內都能抑制骨髓瘤細胞株。

但目前臨床試驗中的 fludarabine 多數是當作「預處理骨幹」使用：
- 與低劑量全身放射線（TBI）、melphalan 等併用，做為異體移植的減低強度預處理。
- 與 cyclophosphamide 併用，做為 CAR-T 前的淋巴清除。

這些試驗的療效無法歸因於 fludarabine 本身，所以「單獨用於骨髓瘤」的證據仍然不足。

## 臨床試驗證據

Evidence Pack 中此適應症約有 50 筆試驗，以下列出最相關的 10 筆（優先列 fludarabine 為直接治療成分、且明確納入骨髓瘤的試驗）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | 完成 | 20 | Fludarabine 併用 methoxyamine (TRC102)，用於復發/難治性血液惡性腫瘤（骨髓瘤為納入疾病之一），評估副作用與最佳劑量 |
| [NCT01453101](https://clinicaltrials.gov/study/NCT01453101) | Phase 2 | 完成 | 54 | 異體移植，以 fludarabine + melphalan + bortezomib 預處理，與歷史對照（Flu/Mel）比較無惡化存活率與反應率 |
| [NCT00054353](https://clinicaltrials.gov/study/NCT00054353) | Phase 1/2 | 完成 | 16 | 多中心減低強度異體移植（fludarabine + melphalan ± TBI）用於多發性骨髓瘤 |
| [NCT00802568](https://clinicaltrials.gov/study/NCT00802568) | Phase 2 | 完成 | 48 | Fludarabine + busulfan + ATG 預處理後做異體移植，用於多發性骨髓瘤 |
| [NCT01503242](https://clinicaltrials.gov/study/NCT01503242) | Phase 1 | 完成 | 15 | 90Y-BC8-DOTA 抗體 + fludarabine + TBI 後接異體移植，用於多發性骨髓瘤 |
| [NCT00006251](https://clinicaltrials.gov/study/NCT00006251) | Phase 1/2 | 完成 | 21 | Fludarabine + 低劑量 TBI 誘導混合嵌合體，納入骨髓瘤患者，fludarabine 的貢獻無法單獨評估 |
| [NCT01408563](https://clinicaltrials.gov/study/NCT01408563) | Phase 2 | 完成 | 33 | 雙臍帶血移植，以 fludarabine + melphalan + 低劑量 TBI 為減低強度預處理，單臂試驗 |
| [NCT00301951](https://clinicaltrials.gov/study/NCT00301951) | Phase 1 | 完成 | 7 | 減低強度臍帶血移植（含 fludarabine 預處理），樣本很小且疾病混合 |
| [NCT02447055](https://clinicaltrials.gov/study/NCT02447055) | Early Phase 1 | 撤回 | 0 | 異體移植（Flu/Mel + 移植後 cyclophosphamide + tocilizumab）用於骨髓瘤，未實際收案 |
| [NCT06196255](https://clinicaltrials.gov/study/NCT06196255) | Phase 1/2 | 招募中 | 20 | Anti-FcRL5 CAR-T，fludarabine 僅用於淋巴清除，療效來自 CAR-T 產品 |

另有多項 BCMA 等 CAR-T 試驗（如 NCT07477912、NCT05594797），fludarabine 只是淋巴清除成分，療效屬於 CAR-T，不列入上表。

## 文獻證據

目前無相關文獻。此預測項目沒有檢索到任何文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60491 | FLUDALYM LYOPHILISATE FOR SOLUTION FOR INJECTION OR INFUSION 50MG | TEVA PHARMACEUTICAL HONG KONG |
| HK-58036 | FLUDARABIN EBEWE SOL FOR INJ 50MG/2ML | SANDOZ HONG KONG |
| HK-64955 | FLUDARABINE PHOSPHATE POWDER FOR SOLUTION FOR INJECTION OR INFUSION 50MG | JINDUN PHARMA (H.K.) |

三張許可證皆為注射劑型，Evidence Pack 未提供核准適應症文字。

## 細胞毒性

Fludarabine 屬嘌呤類似物，為傳統細胞毒性化療藥。DrugBank 未提供 toxicity 資料，以下依藥物類別與 Evidence Pack 的風險提示整理，細節請參考原廠仿單。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤類似物） |
| 骨髓抑制風險 | 高（Evidence Pack 提示需監測骨髓抑制） |
| 致吐性分級 | 低（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、腎功能、神經毒性徵象、感染跡象 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

腎功能不全時 fludarabine 會蓄積，需依腎功能調整劑量。

## 安全性考量

安全性資訊請參考原廠仿單。香港衛生署仿單中的警語與禁忌尚未取得，DDI 查詢也無結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 骨髓瘤試驗多為單臂的移植預處理或 CAR-T 淋巴清除試驗，fludarabine 的獨立療效無法分離，也沒有文獻直接支持。
- 香港仿單的警語與禁忌尚未取得（標為阻擋性缺口），無法進入安全性篩選。
- 同一份 Evidence Pack 中，「骨髓增生異常症候群 (MDS)」的證據較強（L2，含隨機試驗，用於移植預處理），可另案以 Proceed with Guardrails 評估。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症。
- 取得作用機轉資料（DrugBank）。
- 檢索並確認 fludarabine 用於骨髓瘤的文獻，特別是直接比較含／不含 fludarabine 預處理的研究。
- 若以移植預處理為定位，需限定移植適格患者，依腎功能調整劑量，並監測神經毒性、骨髓抑制與伺機性感染。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

