---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Evolocumab：預測新適應症為女性帶因者的症狀型血友病 (symptomatic form of hemophilia in female carriers)（證據等級 L5）。原適應症：同型合子家族性高膽固醇血症、症候群性血脂異常"
monitor_inn: "Evolocumab"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity", "hemorrhagic disease of newborn", "ichthyosis, X-linked, without steroid sulfatase deficiency", "inherited thrombophilia", "disorder of other vitamins and cofactors metabolism and transport"]
---

# Evolocumab
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

# Evolocumab：從家族性高膽固醇血症到血友病女性帶因者症狀型（模型預測）

## 一句話總結

Evolocumab 是一種 PCSK9 抑制型單株抗體，原本用於治療同型合子家族性高膽固醇血症與症候群性血脂異常。
TxGNN 模型預測它可能對**女性帶因者的症狀型血友病 (symptomatic form of hemophilia in female carriers)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，且機轉上找不到合理的關聯，僅屬模型推測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 同型合子家族性高膽固醇血症、症候群性血脂異常（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 女性帶因者的症狀型血友病 (symptomatic form of hemophilia in female carriers) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Evolocumab 是針對 PCSK9 的單株抗體。PCSK9 會促進 LDL 受體降解，抑制它可增加 LDL 受體數量並降低 LDL-C。它在家族性高膽固醇血症等血脂疾病中的療效已被確立。

然而，女性帶因者的症狀型血友病，成因是 X 染色體連鎖變異造成凝血因子 VIII 或 IX 不足，與 LDL 受體或 PCSK9 路徑無關。Evolocumab 不會補充或提升凝血因子，因此**找不到合理的機轉關聯**。

TxGNN 的高分（99.82%）僅代表知識圖譜中的計算性預測，沒有臨床或文獻佐證，不應直接視為療效訊號。

其他排名前 10 的預測（如家族性 ApoC-II 缺乏症、血栓性血小板減少紫斑症、第 XI 因子缺乏症等）同樣沒有試驗或文獻支持。其中僅 ApoC-II 缺乏症與脂質代謝有間接關聯，但 Evolocumab 主要降低 LDL-C，對三酸甘油酯影響有限，也無法矯正脂蛋白脂解酶的活化缺陷，療效仍屬推測。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64509 | REPATHA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 140MG/ML | 注射劑（預充填注射器） | 資料未載明 |
| HK-64510 | REPATHA SOLUTION FOR INJECTION IN PRE-FILLED AUTOINJECTOR 140MG/ML | 注射劑（自動注射筆） | 資料未載明 |

兩張許可證皆由 AMGEN HONG KONG LIMITED 持有，狀態為有效。

---

## 安全性考量

- **藥物交互作用**：藥理資料庫僅顯示 Evolocumab 與其作用標的 PCSK9（proprotein convertase subtilisin/kexin type 9）的結合關係，屬藥理作用本身，並非臨床上的藥物間交互作用。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻佐證（證據等級 L5），機轉上也與 PCSK9/LDL 受體路徑無關。
- 缺少仿單的警語與禁忌資料，且作用機轉欄位尚未補齊，無法進入安全性篩選。

**若要推進需要：**
- 補齊香港衛生署仿單的警語、禁忌症與核准適應症文字
- 補齊 Evolocumab 的作用機轉資料（可由 DrugBank 取得）
- 先以文獻檢索或前臨床研究，確認 PCSK9 抑制與凝血因子缺乏之間是否存在任何生物學連結
- 若上述查證仍找不到合理依據，建議改為優先評估與脂質代謝較相關的預測（例如家族性 ApoC-II 缺乏症），並先蒐集初步證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

