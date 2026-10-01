---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 4
---

# Bupivacaine
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

# Bupivacaine：從局部麻醉到慢性萎縮性肢端皮膚炎 (Acrodermatitis Chronica Atrophicans)

## 一句話總結

Bupivacaine 是一種局部麻醉藥，在香港有多張注射劑許可證（此為一般藥理知識，許可證資料中未載明適應症）。
TxGNN 模型預測它可能對**慢性萎縮性肢端皮膚炎**有效，但目前**沒有任何臨床試驗或文獻**支持，僅是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 慢性萎縮性肢端皮膚炎 (Acrodermatitis Chronica Atrophicans) |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為，Bupivacaine 是局部麻醉藥，作用是阻斷電壓門控鈉離子通道。

慢性萎縮性肢端皮膚炎是與伯氏疏螺旋體 (Borrelia) 感染相關的晚期皮膚萎縮性病變。鈉離子通道阻斷並不是已知的治療途徑，現有資料中找不到能連結兩者的機轉。0.992 的分數只是模型預測，沒有臨床或前臨床證據佐證。

TxGNN 的其他預測適應症，包括新生兒皮肌炎、兒童結締組織病相關次發性間質性肺病、無肌病性皮肌炎，同樣沒有證據支持。其中三個屬皮肌炎相關疾病，分數可能反映的是知識圖譜中相鄰節點的相似性，而非 Bupivacaine 本身的生物學關聯。此外，Bupivacaine 一般被認為有肌肉毒性，尤其是肌肉注射或長時間暴露時，用於發炎性肌肉疾病有安全疑慮。新生兒與兒童族群對證據與安全性的要求也更高。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 9 張許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症）：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-68545 | BUPIVACAINE HYPERBARIC SINTETICA SOLUTION FOR INJECTION 20MG/4ML | MEKIM LTD |
| HK-64812 | BUPIVACAINE FOR SPINAL ANAESTHESIA AGUETTANT SOLUTION FOR INJECTION 5MG/ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-63247 | REGIVELL SOLUTION FOR INJECTION 20MG/4ML | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-42437 | MARCAIN SPINAL HEAVY INJ 0.5% | ASPEN PHARMACARE ASIA LIMITED |
| HK-35573 | MARCAIN POLYAMP DUOFIT 0.25% | ASPEN PHARMACARE ASIA LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，僅有模型預測，沒有臨床試驗、文獻或機轉資料，也找不到合理的作用途徑。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料。
- 從 DrugBank 補齊作用機轉資料，重新評估機轉關聯。
- 檢索是否有 Bupivacaine 用於慢性萎縮性肢端皮膚炎的前臨床或臨床研究。
- 評估投藥途徑的可行性（目前路徑相容性尚未評估）。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

