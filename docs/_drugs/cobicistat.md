---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Cobicistat：從 HIV 合併療法增效劑 到 猿免疫缺陷病毒感染

## 一句話總結

Cobicistat 是一種 CYP3A 抑制劑，作為藥動學增效劑（pharmacokinetic booster）廣泛用於 HIV 抗病毒合併療法中，透過提升共同投予藥物的血中濃度來增強整體療效。TxGNN 模型預測它可能對**猿免疫缺陷病毒感染（Simian Immunodeficiency Virus Infection）** 有效，但目前**無臨床試驗**、**無文獻**支持，所有預測依據均來自模型的知識圖譜推斷。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 合併療法藥動學增效劑（依 DrugBank 資料；台灣許可證資料待補） |
| 預測新適應症 | 猿免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Cobicistat 本身**不具直接抗病毒活性**，而是透過強力抑制 CYP3A4 及部分藥物轉運蛋白（如 P-gp、OATP1B1/3），提升共同投予的抗病毒藥物（如 elvitegravir、darunavir、atazanavir）的系統曝露量，從而增強 HIV 療效。目前作用機轉詳細資料尚未從 DrugBank 取得（資料缺口 DG002），以上說明係依據公開知識整理。

猿免疫缺陷病毒（SIV）與人類免疫缺陷病毒（HIV）同屬靈長類慢病毒（Lentivirus）屬，基因組結構高度相似，兩者所依賴的宿主 CYP3A 代謝路徑亦接近。從知識圖譜的藥病關聯角度來看，TxGNN 預測 cobicistat 與 SIV 感染具有關聯性，推測機制為：若增效劑能提升抗 SIV 藥物的暴露量，則有助於動物模型的療效。

然而，值得注意的是：本次預測前三名均為**動物疾病**（SIV 感染猴、貓愛滋病）或一種**極罕見人類神經發育疾患**，而非人類 HIV 感染本身。這一現象可能反映資料集中 cobicistat 的「直接適應症」標註缺失，導致模型透過旁系關聯推斷出間接相關的病症。臨床再利用價值需審慎評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單（台灣許可證仿單資料尚未取得，為阻斷性資料缺口 DG001，需下載 TFDA 仿單 PDF 後解析）。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前三項預測新適應症均為動物疾病或極罕見人類疾患，且完全缺乏臨床試驗與文獻支持（L5 等級），同時台灣尚無上市許可，安全性資料亦屬阻斷性缺口，無法進行有效的臨床再利用評估。

**若要推進需要：**
- 補齊 DG001：下載並解析 TFDA 仿單 PDF，取得正式警語與禁忌資料
- 補齊 DG002：查詢 DrugBank API，確認完整 MOA 及藥物分類
- 重新確認預測目標：評估是否應以**人類 HIV 感染**或其他人類疾病作為再利用方向，而非動物疾病
- 若確定以 SIV／貓愛滋為目標，說明其動物模型或轉譯醫學意義
- 取得 DDI 完整資料，評估 CYP3A 交互作用的安全風險
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

