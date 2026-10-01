---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 766
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Rivaroxaban：從抗凝血治療到類風濕性關節炎

## 一句話總結

Rivaroxaban（利伐沙班）是直接 Factor Xa 抑制劑，屬於口服抗凝血藥。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效。
目前有 **0 個臨床試驗**，另有 **3 篇文獻**，但都沒有直接測試 rivaroxaban 用於類風濕性關節炎，因此這個預測仍停留在假說層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L4（依 Evidence Pack 評級，僅有機轉層級的假說） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Rivaroxaban 是直接 Factor Xa 抑制劑。目前缺乏詳細的作用機轉資料，以下推論僅屬假說。

可能的關聯在於凝血與發炎的交互作用。自體免疫疾病患者的凝血酶生成 (thrombin generation) 會改變。凝血酶與 Factor Xa 可能透過 PAR 受體訊號促進關節滑膜發炎。若此推論成立，抑制 Factor Xa 在機轉上有可能影響類風濕性關節炎的發炎過程。

需要強調的是，0.996 的高分是知識圖譜的預測結果，沒有臨床資料支持。目前尚無研究證實 rivaroxaban 能改善類風濕性關節炎的疾病活動度或結局。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | 下肢靜脈血栓栓塞的診斷與治療回顧。下肢深層靜脈栓塞的發生率為每 10 萬人年 88–112 例，且隨年齡上升。初次事件後 10 年內的復發率為 20–36%。與類風濕性關節炎無直接關聯。 |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | 凝血酶生成試驗 (TGA) 可用於評估自體免疫疾病（如抗磷脂症候群）的高凝血狀態與心血管風險。僅提供凝血與自體免疫關聯的背景，未測試 rivaroxaban。 |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | 比較非瓣膜性心房顫動患者使用 rivaroxaban 與 apixaban 的服藥順從性。與類風濕性關節炎無關。 |

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。Evidence Pack 未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68572 | RALTEG 20 TABLETS 20MG | I & C (HONG KONG) LIMITED |
| HK-68378 | RIVACRYST TABLETS 20MG | ABBOTT LAB LTD |
| HK-61395 | XARELTO TAB 20MG | BAYER HEALTHCARE LIMITED |
| HK-68356 | XARELTO TABLETS 10MG | BAYER HEALTHCARE LIMITED |
| HK-65785 | XARELTO TABLETS 20MG (ITALY) | BAYER HEALTHCARE LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也未直接測試 rivaroxaban 用於類風濕性關節炎，目前僅有模型預測與假說層級的機轉推論。
- 香港藥物主管機關的仿單警語與禁忌症資料缺口屬於阻擋性缺口，無法進入安全性初篩。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與核准適應症，以通過安全性初篩。
- 補充 rivaroxaban 的作用機轉資料（例如查詢 DrugBank）。
- 文獻檢索：針對 Factor Xa／凝血酶訊號與類風濕性關節炎滑膜發炎的前臨床研究。
- 評估抗凝血治療用於慢性關節炎的出血風險與效益，並說明類風濕性關節炎常用藥物（如 NSAIDs）併用時的出血風險。

**其他預測適應症（同樣建議 Hold）：**
- 痛風（L5）：無可信的機轉關聯，唯一一篇文獻是 benzbromarone 的 CYP450 體外交互作用研究。
- HIV 感染（L4）：既有試驗與文獻是抗凝血治療在 HIV 患者的出血風險與 CYP3A4／P-gp 藥物交互作用，屬於安全性議題，不是療效訊號。
- 短指併指症候群（L5）：無任何試驗與文獻，也沒有機轉依據。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

