---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amylmetacresol：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症（產品皆為喉嚨含片）"
monitor_inn: "AMYLMETACRESOL"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
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

# Amylmetacresol：從喉嚨不適（咽喉抗菌錠劑）到脊髓馬尾症候群

## 一句話總結

Amylmetacresol 是常見於喉糖（含片）的局部抗菌成分，香港已有多款含片上市。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，
但目前**沒有任何臨床試驗與文獻**支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症（產品皆為喉嚨含片） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，amylmetacresol 是局部口咽抗菌劑，常見於喉糖類產品。有文獻提及其可能具有類似局部麻醉的活性（鈉通道阻斷），但這在本次整理的資料中並未獲得證實。

馬尾症候群是脊神經根受壓迫所致的神經系統急症，通常需要手術減壓處理。抗菌含片的局部作用與此病的病理機轉缺乏合理關聯，因此**無法建立機轉上的連結**。

高達 99.99% 的 TxGNN 分數僅代表知識圖譜的計算結果，並非藥理或臨床證據。其他排名前列的預測（如大腸激躁症、多種眼部疾病）同樣缺乏證據，部分眼部預測彼此重疊，可能反映模型的非特異性訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下列為 20 張有效單一成分許可證中的 5 張（資料中未載明劑型與核准適應症，品名皆為含片產品）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67542 | DIFFLAM ANTISEPTIC LOZENGES BLACKCURRANT FLAVOUR | INOVA PHARMACEUTICALS (HONG KONG) |
| HK-54273 | THROATSIL LOZENGE - HONEY & LEMON | DELTAPHARM |
| HK-19288 | STREPSILS + HONEY & LEMON ANTISEPTIC LOZ | RECKITT BENCKISER HONG KONG |
| HK-67433 | BETACARE SORE THROAT ORANGE LOZENGES 0.6MG/1.2MG | INOVA PHARMACEUTICALS (HONG KONG) |
| HK-46071 | COLDANGIN LOZENGES | FORTUNE NATIONAL (HONG KONG) |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有任何臨床試驗或文獻，且作用機轉與馬尾症候群之間無合理關聯。
- 馬尾症候群需緊急手術處理，局部抗菌含片不具備相關治療角色。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並重新評估與神經疾病的潛在連結
- 取得香港衛生署仿單的警語與禁忌資料
- 若仍要探討，需先有前臨床或機轉研究支持
- 預測清單中「obsolete neurogenic bladder」為已廢止的疾病術語，需先對應至現行術語再評估
- 其他眼部預測彼此重疊，建議合併檢視後再決定是否值得追蹤
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

