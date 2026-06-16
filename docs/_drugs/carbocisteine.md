---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 1
---

# Carbocisteine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Carbocisteine：從黏液溶解到痛風

## 一句話總結

Carbocisteine 是一種黏液溶解劑（mucolytic），廣泛用於呼吸道疾病的痰液稀化治療。
TxGNN 模型預測它可能對**痛風 (Gout)** 有效，預測分數高達 99.67%，
但目前**無任何臨床試驗或文獻**支持此方向，屬純模型預測結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黏液溶解劑，用於呼吸道疾病痰液稀化（香港未上市，無核准適應症資料） |
| 預測新適應症 | 痛風 (Gout) |
| TxGNN 預測分數 | 99.67% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Carbocisteine 屬於含硫胺基酸衍生物，其藥理機轉主要有兩個面向：
**（一）黏液調節作用**：藉由修改呼吸道黏液中 sialomucin 與 fucomucin 的比例，降低痰液黏稠度，促進痰液排出；
**（二）輕度抗氧化活性**：來自其分子中的 cysteine 硫醇基團（-SH），具清除自由基的能力。

痛風的核心發病機轉為高尿酸血症導致單鈉尿酸鹽結晶沉積，進而活化 **NLRP3 炎症小體**，引發急性關節炎症反應。理論上，Carbocisteine 的抗氧化特性可能間接抑制 NLRP3 炎症小體活化，從而減輕痛風急性發作的炎症程度。此外，TxGNN 知識圖譜可能透過共享蛋白質靶點或代謝路徑的多跳連結，建立了兩者之間的關聯。

然而，目前作用機轉資料標記為缺失（Data Gap），且 Carbocisteine 與痛風之間**無已知直接藥理機轉連結**。TxGNN 的高預測分數（排名 6,723）很可能反映的是知識圖譜拓撲相似性，而非真實的生物學合理性。此預測需謹慎看待，機轉研究驗證為必要前提。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測目前屬純模型輸出（L5 證據等級），無任何臨床試驗或文獻佐證，且 Carbocisteine 與痛風之間的藥理機轉連結薄弱，生物學合理性尚待驗證。此外，該藥物在香港未上市，無任何核准適應症紀錄可供參考，整體評估尚不具備推進條件（決策階段 S0，安全性初評前）。

**若要推進需要：**
- 補齊作用機轉（MOA）資料：查詢 DrugBank API（DB04339），確認是否有已知的 NLRP3 或尿酸代謝相關靶點
- 取得原廠仿單：查詢原廠安全性警語與禁忌症，以完成 S1 安全性初評
- 進行文獻搜尋廣化：嘗試以 `carbocisteine AND inflammation`、`carbocisteine AND uric acid`、`mucolytic AND gout` 等組合搜尋，確認是否存在間接相關文獻
- 評估知識圖譜路徑：分析 TxGNN 預測中連結 Carbocisteine 與痛風的具體節點路徑，判斷是否具生物學意義
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

