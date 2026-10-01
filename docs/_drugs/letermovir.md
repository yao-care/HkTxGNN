---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 511
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir：從巨細胞病毒感染到外陰陰道念珠菌病

## 一句話總結

Letermovir 是一種抗巨細胞病毒（CMV）藥物，在香港以 PREVYMIS 之名上市。
TxGNN 模型預測它可能對**外陰陰道念珠菌病 (Vulvovaginal Candidiasis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，且機轉上找不到合理關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 巨細胞病毒 (CMV) 感染（香港許可證資料未載明適應症文字，此為依藥理分類判斷） |
| 預測新適應症 | 外陰陰道念珠菌病 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

**目前看不出合理性。**

Letermovir 是 CMV 抗病毒藥，作用是抑制病毒 DNA 終止酶複合體（pUL56/UL89/UL51）。資料庫中沒有詳細的作用機轉紀錄，以上說明是依一般藥理知識補充，並非來自所提供的資料。

念珠菌（如白色念珠菌）是真菌，沒有與這個病毒標靶同源的蛋白，Letermovir 也沒有已知的抗真菌活性。CMV 感染與念珠菌感染的病原體類型不同，兩者之間也沒有明顯的共通病理路徑。

因此，99.88% 的高分很可能是知識圖譜或嵌入向量的假象，例如來自共享的網路鄰居節點，而不是有生物學依據的訊號。這個分數不應被解讀為療效的支持證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66124 | PREVYMIS TABLETS 240MG | MERCK SHARP & DOHME (ASIA) LTD |
| HK-66123 | PREVYMIS TABLETS 480MG | MERCK SHARP & DOHME (ASIA) LTD |
| HK-66125 | PREVYMIS CONCENTRATE FOR SOLUTION FOR INFUSION 240MG/12ML | MERCK SHARP & DOHME (ASIA) LTD |
| HK-66122 | PREVYMIS CONCENTRATE FOR SOLUTION FOR INFUSION 480MG/24ML | MERCK SHARP & DOHME (ASIA) LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測只有模型分數支持（L5），沒有任何臨床試驗或文獻佐證。
- 從藥理上看，抗 CMV 藥物對真菌沒有已知作用，模型的高分很可能是假象。

**若要推進需要：**
- 找出可支持的證據，例如體外抗念珠菌活性的前臨床資料，或任何相關臨床觀察。
- 確認 TxGNN 給出高分的圖譜路徑，判斷是否為假象。
- 取得香港衛生署仿單的警語與禁忌資料，才能進行安全性篩選。
- 補齊詳細的作用機轉資料，以及原適應症的官方核准文字。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

