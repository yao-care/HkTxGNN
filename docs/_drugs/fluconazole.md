---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 1
---

# Fluconazole
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

# Fluconazole：從抗黴菌感染到點狀上皮角膜結膜炎

## 一句話總結

Fluconazole 是一種唑類（azole）抗黴菌藥。
TxGNN 模型預測它可能對**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效。
目前**沒有臨床試驗與文獻**支持，僅有模型預測，證據等級為 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Fluconazole 是唑類抗黴菌藥，已知作用是抑制黴菌的 CYP51（羊毛甾醇 14-α-去甲基酶），阻斷黴菌細胞膜成分的合成。

點狀上皮角膜結膜炎最常見的原因是病毒感染（如腺病毒）、毒性反應或乾眼症，抗黴菌機轉與這些常見病因沒有明確關聯。

模型給出高分，可能只是知識圖譜中的鄰近關係所致，例如與黴菌性角膜炎等眼部感染疾病相鄰，並不代表已驗證有療效。目前也沒有原適應症與機轉資料，機轉層面的評估相當有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67056 | DIFLUVID CAPSULES 150MG | HOVID LIMITED |
| HK-60609 | SYSCAN - 150 CAP 150MG | TRENTON-BOMA LTD |
| HK-60027 | FLUCONAZOL FARMOZ CAP 200MG (WEST PHARMA) | TRENTON-BOMA LTD |
| HK-67485 | FLUCONAZOLE SOLUTION FOR INFUSION 100MG/50ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-67082 | FLUZAMED CAPSULES 50MG | THE INTERNATIONAL MEDICAL COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有 TxGNN 模型預測，沒有任何臨床試驗或文獻支持，機轉上也與此疾病的常見病因缺乏明確關聯。

**若要推進需要：**
- 針對 fluconazole 與眼表疾病，進行 PubMed 與 ClinicalTrials.gov 的專項搜尋
- 確認是否存在黴菌病因的亞群，這是機轉上唯一可能成立的切入點
- 補齊香港衛生署仿單中的警語與禁忌症
- 從 DrugBank 補充作用機轉資料
- 評估給藥途徑（口服、注射或眼用製劑）是否適用於眼表疾病

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

