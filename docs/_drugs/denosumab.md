---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Denosumab：從骨質疏鬆／骨相關疾病到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Denosumab 是 RANKL 抑制劑，香港已有 Prolia、Xgeva 等產品上市。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Evidence Pack 未提供核准適應症文字（依產品名稱與試驗背景，推測為骨質疏鬆與骨相關疾病） |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Denosumab 是 RANKL 抑制劑，用於骨代謝相關疾病，其在原適應症中的作用已被廣泛使用。

從 RANK/RANKL/OPG 訊號通路連到視網膜的發炎或血管病變，在機轉上有可能，但目前只是推測。本資料集中沒有試驗或文獻證實這條路徑。TxGNN 的高分來自知識圖譜的關聯，不等於已有實證。

**相鄰預測：糖尿病視網膜病變（一般）**，TxGNN 分數 99.23%，證據同樣薄弱：
- 臨床試驗 [NCT00925600](https://clinicaltrials.gov/study/NCT00925600)（Phase 3、已完成、769 人）評估攝護腺癌患者因雄性素剝奪治療而使用 Denosumab 時的水晶體混濁。它的終點是水晶體，不是視網膜，只能提供眼部安全性參考，不能視為療效證據。
- 文獻 [PMID 38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/)（2024，Diabetes Obes Metab）探討 Denosumab 對第 2 型糖尿病發生率與併發症的影響，屬間接證據。
- 文獻 [PMID 36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/)（2023，Cureus）評估第 2 型糖尿病患者的骨折風險工具 FRAX，與視網膜結果無關。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68757 | WYOST SOLUTION FOR INJECTION 120MG/1.7ML | SANDOZ HONG KONG LIMITED |
| HK-68756 | JUBBONTI SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 60MG/1ML | SANDOZ HONG KONG LIMITED |
| HK-61163 | XGEVA SOLUTION FOR INJECTION 120MG | AMGEN HONG KONG LIMITED |
| HK-60588 | PROLIA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 60MG/ML (USA) | AMGEN HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測新適應症沒有任何直接的臨床或文獻證據，只有模型分數，證據等級為 L5。
- 機轉資料缺漏，RANKL 與視網膜病變的關聯仍屬推測，香港仿單的安全性資料也尚未取得。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，完成安全性初篩。
- 補齊 Denosumab 的作用機轉資料（DrugBank）。
- 進行 RANKL/OPG 與糖尿病視網膜病變的機轉文獻回顧，尋找前臨床證據。
- 若有前臨床或觀察性證據，再評估設計小型概念驗證研究；目前也需考量全身性給藥用於眼部疾病的可行性與風險。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

