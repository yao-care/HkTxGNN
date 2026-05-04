---
layout: default
title: Crotamiton
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Crotamiton
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

# Crotamiton：從疥瘡到恙蟎病

## 一句話總結

Crotamiton 是一種外用殺蟎劑與止癢劑，傳統上用於治療**疥瘡（Scabies）**及相關搔癢症狀。
TxGNN 模型預測它可能對**恙蟎病（Trombiculiasis）** 有效，機轉上具有高度生物學合理性——兩者同屬蜱蟎目寄生蟲感染。
然而目前**無任何臨床試驗或文獻**支持此方向，屬純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 疥瘡（Scabies）及搔癢症 |
| 預測新適應症 | 恙蟎病（Trombiculiasis） |
| TxGNN 預測分數 | 96.24% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

Crotamiton 是一種外用小分子化合物，具有已知的殺疥蟎（Sarcoptes scabiei）及止癢活性，廣泛用於疥瘡治療。目前本份 Evidence Pack 中正式 MOA 資料標記為缺失，惟根據藥理文獻，其作用機制可能涉及直接神經毒性效應對蟎蟲的干擾，以及抑制搔癢感受器的局部止癢作用。

恙蟎病（Trombiculiasis）是由恙螨科（Trombiculidae）幼蟲叮咬所引起的皮膚感染，與疥瘡同屬**蜱蟎目（Acari）寄生蟲感染**。這是本次 TxGNN 預測清單中唯一具有直接機轉依據的適應症——兩種疾病的病原體生物學分類相近，殺疥蟎藥物延伸應用至恙蟎具有合理的生物學基礎。

儘管機轉關聯性強，此預測目前仍停留在假說階段，缺乏任何體外、動物模型或臨床層級的驗證數據，須謹慎評估後續研究價值。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Crotamiton 目前在香港**未有核准上市許可證**，無相關品項資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Research Question**

**理由：**
Crotamiton 對恙蟎病的預測在機轉上為本清單中最具生物學合理性的候選，兩者同屬蜱蟎目感染，殺蟎作用延伸有其依據。然而，目前完全缺乏臨床或前臨床驗證數據（L5 等級），且香港無上市紀錄，尚不具備推進至臨床評估的條件。

**若要推進需要：**
- 補充正式 MOA 資料（查詢 DrugBank API 或原廠仿單）
- 檢索 Crotamiton 對 Trombiculidae 的體外或動物模型研究文獻（包含非英文語言，如日文、泰文相關報告）
- 收集 TFDA 仿單警語與禁忌症（目前為資料缺口，阻礙安全性初評）
- 評估香港或台灣藥政機關對此外用殺蟎適應症擴展的監管路徑
- 若文獻搜索有初步支持，建議啟動小規模概念驗證（PoC）皮膚科試驗設計評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

