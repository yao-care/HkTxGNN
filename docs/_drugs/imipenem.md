---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 5
---

# Imipenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imipenem：從細菌感染到瀰漫性硬皮症 (Diffuse Scleroderma)

## 一句話總結

Imipenem 是碳青黴烯類 (carbapenem) 抗生素，原本用於治療細菌感染。
TxGNN 模型預測它可能對**瀰漫性硬皮症 (Diffuse Scleroderma)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 瀰漫性硬皮症 (Diffuse Scleroderma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。已知 Imipenem 是 β-內醯胺類 (carbapenem) 抗生素，透過抑制細菌細胞壁合成來殺菌。

瀰漫性硬皮症是一種自體免疫性的纖維化疾病，沒有已知的感染性成因可供碳青黴烯類藥物作用。原適應症（抗菌）與新適應症（自體免疫纖維化）在機轉上沒有合理的關聯。

因此，這個預測**缺乏機轉支持**。0.9999 的高分沒有任何試驗或文獻佐證，很可能是知識圖譜傳播 (graph propagation) 產生的假象，不應視為有效性的證據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-53560 | PREPENEM FOR INJ 500MG | I & C (HONG KONG) LIMITED |
| HK-61317 | PRIMAGAL POWDER FOR SOLUTION FOR INFUSION 500/500MG | HIND WING CO LTD |
| HK-66808 | IMCIMILL POWDER FOR SOLUTION FOR INFUSION 500MG/500MG | CHEMILL PHARMA LIMITED |
| HK-64660 | IMIPENEM/CILASTATIN KABI POWDER FOR SOLUTION FOR INFUSION 500MG/500MG | FRESENIUS KABI HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有臨床試驗和文獻，機轉上也沒有合理關聯。
- 對慢性自體免疫疾病長期使用碳青黴烯類，也不符合抗生素管理 (antimicrobial stewardship) 原則。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料，以及 DrugBank 作用機轉資料。
- 找出任何支持 Imipenem 用於硬皮症的機轉或前臨床研究。目前沒有，不建議投入資源。

**補充：** 同一份 Evidence Pack 中，其他預測適應症的證據較合理，可考慮改列為優先研究對象：
- **傷寒／副傷寒沙門氏菌感染 (Paratyphoid Fever)** 與**沙門氏菌病 (Salmonellosis)**：L4，有體外藥敏研究和個案報告，但沒有臨床試驗，也沒有療效資料。
- **鼻竇炎 (Sinusitis)**：L4，證據間接；**慢性鼻竇炎 (Chronic Rhinosinusitis)**：L4，機轉薄弱，建議 Hold。

這些候選其實是抗菌藥物在抗菌範圍內的延伸，不是真正的跨領域老藥新用。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

