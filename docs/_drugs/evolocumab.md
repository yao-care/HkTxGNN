---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
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

# Evolocumab：從高脂血症到女性血友病帶因者症狀

## 一句話總結

Evolocumab 是一種 PCSK9 抑制劑，透過阻斷 PCSK9 蛋白來增加 LDL 受體數量，從而大幅降低血漿 LDL 膽固醇，用於高脂血症及動脈粥樣硬化性心血管疾病的治療。
TxGNN 模型預測它最可能對**女性血友病帶因者症狀 (Symptomatic Form of Hemophilia in Female Carriers)** 有效，
然而目前**無任何臨床試驗或文獻**支持此方向，且生物學機轉連結不成立。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高脂血症 / 動脈粥樣硬化性心血管疾病（香港未上市，以 FDA/EMA 核准適應症為準）|
| 預測新適應症 | 女性血友病帶因者症狀 (Symptomatic Form of Hemophilia in Female Carriers) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Evolocumab 是一種全人源單株抗體，透過抑制 PCSK9（前蛋白轉化酶枯草桿菌蛋白酶 9 型）阻止 LDL 受體被降解，增強肝臟清除 LDL-C 的能力，達到顯著降低血漿 LDL 膽固醇的效果。此機轉完全屬於脂質代謝路徑。

女性血友病帶因者症狀的致病機轉截然不同：源於 Factor VIII 基因所在的 X 染色體不均等失活（Lyonization），導致部分帶因女性因活性 X 染色體比例偏低而出現出血症狀。PCSK9-LDLR 脂質代謝軸與凝血因子 VIII 的功能、基因活化或出血表現型之間，目前在任何已知生物學路徑中均無交集。

**TxGNN 給出高預測分數（99.82%）最可能源於知識圖譜（KG）本體論中的圖近鄰效應，而非真實療效連結。** 觀察全部 10 個預測適應症可發現一致規律：所有預測均圍繞凝血異常、血液疾病或代謝疾病的上位分類節點，無一具備與 PCSK9 抑制的合理機轉連結，提示此批預測結果屬系統性假陽性。

---

## 所有預測適應症機轉評估

本 Evidence Pack 共包含 10 個預測適應症，所有適應症均無臨床試驗或文獻支持（L5），建議決策均為 **Hold**。

| 排名 | 適應症 | 預測分數 | 機轉連結評估 |
|------|--------|---------|-------------|
| 1 | Symptomatic form of hemophilia in female carriers | 99.82% | ❌ PCSK9 與 X 染色體不均等失活無交集 |
| 2 | Familial apolipoprotein C-II deficiency | 99.50% | ❌ 同屬脂質代謝但機轉截然不同（LPL vs LDLR） |
| 3 | Thrombocytopenic purpura | 99.42% | ❌ 免疫/ADAMTS13 機轉，與 PCSK9 無連結 |
| 4 | Factor XI deficiency | 99.29% | ❌ 凝血因子 XI 合成不受 PCSK9 影響 |
| 5 | Hemophilia A with vascular abnormality | 99.22% | ❌ Factor VIII 缺乏合併血管異常，與 PCSK9 無已知療效 |
| 6 | Disease of catalytic activity | 99.08% | ❌ KG 廣義上位節點效應，非臨床實體 |
| 7 | Hemorrhagic disease of newborn | 98.89% | ❌ 維生素 K 缺乏相關，PCSK9 無法補充凝血因子 |
| 8 | Ichthyosis, X-linked (non-STS) | 98.84% | ❌ 皮膚角質化異常，無 PCSK9-LDLR 生物學依據 |
| 9 | Inherited thrombophilia | 98.82% | ❌ 促凝血遺傳異常，與 PCSK9 抑制連結屬推測層級 |
| 10 | Disorder of vitamins/cofactors metabolism and transport | 98.80% | ❌ KG 代謝疾病上位節點效應 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

所有 10 個預測適應症均已查詢 ClinicalTrials.gov 及 ICTRP，結果皆為零。

---

## 文獻證據

目前無相關文獻。

所有 10 個預測適應症均已查詢 PubMed，結果皆為零。

---

## 香港上市資訊

Evolocumab 目前在香港未上市，無任何藥品許可證紀錄。

> **參考背景**：Evolocumab 以 Repatha® 品名在美國 FDA（2015年）、歐盟 EMA（2015年）已核准上市，適應症包括原發性高脂血症、同型合子型家族性高膽固醇血症（HoFH），以及確診動脈粥樣硬化性心血管疾病患者的心血管事件預防。本次 Evidence Pack 中香港許可證為零，可能反映本地監管申請狀態，建議進一步確認。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 模型雖對前 10 個預測適應症給出 98.80%–99.82% 的高分，但所有預測均缺乏生物學機轉合理性，且無任何臨床試驗或文獻佐證。預測高分的根本原因最可能為 KG 本體論中「血液疾病/代謝疾病」節點群與脂質代謝藥物之間的圖近鄰效應（假陽性模式），而非真實療效信號。此為 TxGNN 模型在疾病本體論上位節點的已知侷限。

**若要推進需要：**
- 補充 Evolocumab 完整 MOA 資料及全球已核准適應症（查詢 DrugBank API 或 FDA/EMA 藥品標籤）
- 評估 Evolocumab 在香港申請藥品許可證的可行性（目前許可證為零需確認原因）
- 若仍要探索老藥新用方向，建議**重新聚焦在脂質代謝相關疾病**，例如非酒精性脂肪性肝病（NAFLD/NASH）、糖尿病合併高脂血症、或心衰竭合併高脂血症等，這些領域與 PCSK9 抑制機轉有直接關聯且已有新興臨床數據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

