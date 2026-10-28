---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 730
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "Pretomanid"
predicted_indications: ["candidiasis", "leprosy", "coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery"]
description: "Pretomanid：預測新適應症為念珠菌感染 (candidiasis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Pretomanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Pretomanid: 念珠菌感染 (candidiasis)
{: .text-alpha }

## 一句話總結

Pretomanid 是一種硝基咪唑噁嗪類（nitroimidazooxazine）抗結核藥，已在香港取得許可證。TxGNN 模型預測分數最高的新適應症是**念珠菌感染 (Candidiasis)**，但目前**沒有任何臨床試驗或文獻**支持，機轉上也缺乏合理性。相對而言，Pretomanid 在耐藥結核病的證據相當充分，但那屬於其既有用途，而非新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 念珠菌感染 (candidiasis) |
| TxGNN 預測分數 | 0.9969 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。依一般藥理知識，Pretomanid 是需被活化的前驅藥物，必須由結核分枝桿菌的 Ddn（deazaflavin 依賴性硝基還原酶）活化，再透過釋放一氧化氮造成呼吸毒性，並抑制黴菌酸（mycolic acid）合成。

真菌缺乏這條活化路徑，因此 0.9969 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而不是生物學證據或有機轉依據的預測。念珠菌感染與結核病的病原體類別不同，兩者在藥理上缺乏明顯的共通靶點。

在其他高分預測中，只有**痲瘋病 (leprosy)** 在生物學上較合理，因為痲瘋桿菌同屬分枝桿菌。但痲瘋桿菌已喪失許多基因，是否仍保有 Ddn/F420 活化路徑並不清楚。檢索到的文獻全部是耐藥結核病，沒有任何針對痲瘋病的研究，屬於間接外推。


## 臨床試驗證據

目前無針對念珠菌感染的臨床試驗登記。

## 文獻證據

目前無針對念珠菌感染的相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67657 | PRETOMANID TABLETS 200MG | 未載明 | 未載明 |

製造商為 FOSUN INDUSTRIAL CO., LIMITED，狀態為有效（單方）。

## 安全性考量

- **藥物交互作用**：共查得 14 項，其中 **Major（嚴重）** 8 項，**Moderate（中度）** 6 項。
  - Major：Dexamethasone、Lumacaftor、Apalutamide、Dabrafenib、Mitotane、Lorlatinib、Enzalutamide
  - Moderate：Empagliflozin、Sitagliptin、Somatotropin、Somatrem、Baricitinib、Clofarabine、Methotrexate
- **其他提醒**：在含 linezolid 的組合療法（如 BPaL）中，血小板低下是已知不良反應；另有 QT 相關的安全考量。這些對心臟或血液方向的再利用而言是警訊，而非療效訊號。

警語與禁忌症的詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名最高的念珠菌感染預測只有模型分數，沒有任何臨床或文獻證據（L5），機轉上也缺乏依據。
- 前十名預測中，冠狀動脈疾病、心肌缺血、先天性左冠狀動脈異常起源等缺乏合理機轉，其分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而不是生物學證據。痲瘋病為 L4 但屬間接證據。

**若要推進需要：**
- 若要探索痲瘋病方向：確認痲瘋桿菌是否具備 Ddn/F420 活化路徑，並進行體外或動物模型試驗。
- 若要探索念珠菌方向：需先有體外抗真菌活性數據，否則不建議投入。
- 取得香港仿單的核准適應症、警語與禁忌症，補足完整的安全性評估。
- 補充 DrugBank 的作用機轉資料。
- 針對嚴重 DDI（如 enzalutamide、apalutamide 等）建立併用管理原則。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

