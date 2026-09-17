---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 5
---

# Insulin Lispro
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Insulin Lispro：從糖尿病血糖控制到五個低證據等級預測適應症

## 一句話總結

Insulin Lispro 是速效胰島素類似物，原本用於糖尿病患者的血糖控制。
TxGNN 模型針對此藥物產生了 **5 個**預測適應症訊號，但機轉審查後判定其中 **4 個**極可能是知識圖譜共病節點造成的偽陽性連結，僅 **1 個**（TRMA/Rogers 症候群）具備間接臨床合理性；目前**無任何臨床試驗或文獻**直接支持這些預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病（血糖控制）— 詳細適應症文字缺失（許可證資料為空） |
| 作用機轉 (MOA) | 缺失（[Data Gap]，需查 DrugBank API 補齊） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 預測適應症數 | 5 個，證據等級皆為 L4-L5 |
| 最高分預測 | Autoimmune oophoritis（99.78%，L5，Hold） |
| 相對較合理預測 | Thiamine-responsive dysfunction syndrome（99.37%，L4，Research Question） |
| 建議決策 | **Hold** |

### 五個預測適應症一覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Autoimmune oophoritis | 99.78% | L5 | S0 | Hold |
| 2 | Thiamine-responsive dysfunction syndrome | 99.37% | L4 | S1 | Research Question |
| 3 | Focal stiff limb syndrome | 99.36% | L5 | S0 | Hold |
| 4 | Classic stiff person syndrome | 99.36% | L5 | S0 | Hold |
| 5 | Opsismodysplasia | 99.34% | L5 | S0 | Hold |

---

## 為什麼這些預測合理性各不相同？

作用機轉資料目前缺失。根據 evidence pack 內附的機轉審查意見，5 個預測可分為兩類：

**較具間接合理性（排名 2）**：TRMA（Thiamine-responsive megaloblastic anemia，Rogers 症候群）的典型三聯徵包含糖尿病，部分病例對 thiamine 補充無反應而仍需胰島素治療。Insulin lispro 作為速效胰島素用於控制此症候群伴隨的糖尿病，在臨床實務上並非不合理，但這是既有臨床外推、並非針對此適應症的專屬證據，TxGNN 高分很可能只是反映知識圖譜中「糖尿病」節點的廣泛連結。

**判定為知識圖譜雜訊（排名 1、3、4、5）**：
- Autoimmune oophoritis：與第一型糖尿病同屬 APS-2 型自體免疫多重內分泌症候群的共病項目，但胰島素並不作用於卵巢自體免疫破壞機轉。
- Focal stiff limb syndrome / Classic stiff person syndrome：與第一型糖尿病常見抗 GAD65 抗體共病，但胰島素對中樞抑制性神經傳導異常無已知療效。
- Opsismodysplasia：INPPL1 基因突變導致的骨骼發育不良症，與胰島素訊息路徑無已知病理連結，判斷為偽陽性。

---

## 臨床試驗證據

目前無相關臨床試驗登記（針對 5 個適應症共查詢 ClinicalTrials.gov 與 ICTRP 各 5 次，皆為 0 筆結果）。

## 文獻證據

目前無相關文獻（針對 5 個適應症的 PubMed 查詢皆為 0 筆結果）。

## 香港上市資訊

Insulin Lispro 目前**未在香港上市**，無許可證資料可列出。

---

## 安全性考量

安全性資料目前全數缺失（主要警語、禁忌症、藥物交互作用皆為 [Data Gap]），且此缺口被標記為 **Blocking**，導致所有預測適應症皆無法進入 S1 安全性初評。安全性資訊需先向 TFDA／香港藥監機構取得正式仿單後才能評估。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 安全性資料為 Blocking 缺口，任何預測適應症皆無法通過 S1 安全性初評。
- 5 個預測中 4 個經機轉審查判定為知識圖譜共病雜訊，無直接藥理學或臨床證據；唯一具間接合理性的排名 2（TRMA）也僅停留在臨床外推假設，缺乏專屬文獻或試驗佐證。

**若要推進需要：**
- 取得 TFDA／香港仿單警語與禁忌症資料（解除 Blocking 缺口）
- 補齊 DrugBank MOA 資料，用於重新檢視機轉關聯性
- 針對排名 2（TRMA 糖尿病）額外檢索罕見病文獻或病例報告，驗證胰島素外推假設是否有實證支持
- 確認 Insulin Lispro 在香港的上市/申請狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

