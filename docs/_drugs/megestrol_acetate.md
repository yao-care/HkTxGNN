---
layout: default
title: Megestrol Acetate
parent: 高證據等級 (L1-L2)
nav_order: 398
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

# Megestrol Acetate：從黃體素類藥物到子宮內膜癌

## 一句話總結

Megestrol Acetate（DB00351）是一種合成黃體素（progestin），本次評估的原始核准適應症資料尚未取得。
TxGNN 模型預測它可能對**子宮內膜癌 (Uterine Corpus Endometrial Carcinoma)** 有效，
目前有 **3 個相關臨床試驗**支持這個方向，但**尚無直接對應的文獻證據**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（原始核准適應症未記錄，DrugBank 查詢未回傳指標性資料） |
| 預測新適應症 | 子宮內膜癌 (Uterine Corpus Endometrial Carcinoma) |
| TxGNN 預測分數 | 99.94%（排名第 1615） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉正式資料（DrugBank MOA 查詢為資料缺口，列為 High 嚴重度）。根據本次預測模型所引用的藥理資訊，Megestrol Acetate 是一種**合成黃體素（progestin）**，其藥理作用為**黃體素受體（progesterone receptor, PR）促效劑**。

由於原始核准適應症資料同樣缺失，目前無法具體說明原適應症與子宮內膜癌之間的臨床關聯路徑。不過從機轉角度來看，子宮內膜癌組織（尤其是分化良好、PR 陽性的類型）普遍表現黃體素受體，黃體素類藥物理論上可透過**抑制內膜增生、誘導細胞分化**來達成腫瘤抑制效果，這使得此預測具備一定的生物學合理性。

值得注意的是，現有臨床試驗證據多為 megestrol acetate 與其他藥物（如 temsirolimus、PD-1 抑制劑）的**合併療法**，而非單獨使用的直接驗證，這點在解讀證據強度時需特別留意。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | 已完成 | 73 | 比較 Temsirolimus 單用 vs. 合併 megestrol acetate + tamoxifen，治療晚期/復發性子宮內膜癌；為目前最直接、樣本數最完整的證據來源 |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | 已終止 | 9 | 比較連續型 vs. 序貫型黃體素治療子宮內膜上皮內瘤變／非典型增生，探討 megestrol 於保留子宮治療的效果；因收案不足提早終止 |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | 未知 | 60 | PD-1 抑制劑合併黃體素治療早期子宮內膜癌、欲保留生育力患者；試驗標題未明確標示 megestrol acetate，屬機轉相關但非直接驗證 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

此藥物目前**未於香港上市**，無許可證登記紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本評估之藥物層級資料存在兩項待補資訊：TFDA 仿單警語/禁忌屬 Blocking 等級，會阻礙進入 S1 安全性初評；作用機轉 MOA 屬 High 等級資料缺口。）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 個已完成的 Phase 2 隨機分派試驗（NCT00729586，n=73）支持含 megestrol acetate 的合併療法用於晚期/復發性子宮內膜癌，機轉上具生物學合理性（PR 促效劑對 PR 陽性內膜癌組織的作用），但現有證據以合併療法為主，缺乏單一藥物的直接驗證，故評為 L2、S2 階段，需在guardrail下謹慎推進。

**若要推進需要：**
- 補齊 DrugBank 完整作用機轉（MOA）資料
- 取得原廠仿單警語與禁忌症資訊（目前為 Blocking 等級缺口，需先解除才能進入安全性初評）
- 確認原始核准適應症內容，釐清與子宮內膜癌預測之機轉延伸關係
- 若考慮香港上市，需評估藥物引進與許可證申請流程（目前為 0 張許可證、未上市狀態）
- 尋找針對 megestrol acetate 單獨用於子宮內膜癌之直接臨床試驗或文獻證據，以強化 L2 等級的證據基礎
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

