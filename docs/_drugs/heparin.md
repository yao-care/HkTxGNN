---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 2
---

# Heparin
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

# Heparin（肝素）：從抗凝血藥到蛋白 C 缺乏所致血栓形成傾向

## 一句話總結

Heparin 是一種抗凝血藥，在香港已有多張上市許可證。
TxGNN 模型預測它可能對**體染色體隱性蛋白 C 缺乏所致血栓形成傾向 (Thrombophilia due to protein C deficiency, autosomal recessive)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個預測，只有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 體染色體隱性蛋白 C 缺乏所致血栓形成傾向 (Thrombophilia due to protein C deficiency, autosomal recessive) |
| TxGNN 預測分數 | 99.29% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，資料庫中也未收錄原適應症。就一般藥理知識，Heparin 會增強抗凝血酶 (antithrombin) 的作用，進而抑制凝血酶 (thrombin) 與第 Xa 因子。

蛋白 C 缺乏會讓體內天然抗凝機制減弱，造成血栓形成傾向。抗凝治療也常用於嚴重蛋白 C 缺乏的處置。因此在機轉上，Heparin 用於此類血栓形成傾向是說得通的。

不過，這只是模型分數與機轉推論。本次資料中沒有任何直接證據支持，原適應症與機轉資料也都缺漏，因此只能視為「僅有預測」的訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-10765 | HEPARIN (LEO) INJ 1000U/ML | DKSH HONG KONG LIMITED |
| HK-57802 | HEPARIN SODIUM INJ 1,000 IU/ML | PFIZER CORPORATION HONG KONG LIMITED |
| HK-27750 | MULTIPARIN INJ 5000 UNITS/ML | LUEN CHEONG HONG LTD |
| HK-33423 | REPARCOL CREAM 250U/G（外用乳膏） | MEYER PHARMACEUTICALS LTD |
| HK-64529 | VAXCEL HEPARIN SODIUM SOLUTION FOR INJECTION 5000IU/ML | KOTRA PHARMA (HONG KONG) COMPANY |

上表僅列出 20 張許可證中的 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高（99.29%），機轉上也說得通，但沒有任何臨床試驗或文獻佐證，證據等級只有 L5。
- 原適應症、作用機轉與安全性資料都缺漏，現階段無法進入安全性篩選。

**若要推進需要：**
- 針對性檢索：蛋白 C 缺乏、暴發性紫癜 (purpura fulminans)、新生兒血栓等主題的臨床試驗與文獻。
- 補齊 Heparin 的作用機轉（可查詢 DrugBank）。
- 取得香港衞生署仿單，確認核准適應症、警語與禁忌症。
- 評估劑型與給藥途徑是否適用於目標族群（特別是新生兒或嚴重病例）。

**補充：**排名第 2 的預測「血小板釋放障礙 (primary release disorder of platelets)」目前只有間接證據（等級 L4，決策同為 Hold）。該疾病本身有出血傾向，而 Heparin 會增加出血風險，機轉方向可疑，不建議優先推進。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

