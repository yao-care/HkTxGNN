---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 605
evidence_level: L5
indication_count: 3
---

# Nevirapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Nevirapine：從 HIV-1 感染到貓後天免疫缺乏症候群

## 一句話總結

Nevirapine 是一種 HIV-1 非核苷類逆轉錄酶抑制劑（NNRTI），原本用於 HIV-1 感染的治療。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，
但目前**沒有臨床試驗，也沒有文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（香港許可證未載明適應症文字，此為依藥理分類的判斷） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Nevirapine 是 HIV-1 逆轉錄酶的別構抑制劑（NNRTI），在 HIV-1 感染中的療效已被證實。模型給出高分，最可能是因為貓免疫缺乏病毒 (FIV) 和 HIV 同屬逆轉錄病毒，在知識圖譜中彼此相近。

但這個機轉推論很薄弱。一般報告指出，FIV 的逆轉錄酶對 NNRTI 不敏感，現有資料也無法驗證這個連結。

另外，這是獸醫領域的疾病，不是人類的老藥新用目標。0.998 的分數只是知識圖譜的相似度推論，不等於療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63478 | PMS-NEVIRAPINE TABLETS 200MG | TRENTON-BOMA LTD |
| HK-65069 | NEVIRAPINE TABLETS USP 200MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-66786 | APT-NEVIRAPINE TABLETS 200MG | JACOBSON MARKETING LIMITED |
| HK-62889 | NEVIRAPINE TABLETS 200MG | I & C (HONG KONG) LIMITED |
| HK-64848 | NEVIRAPINE TABLETS USP 200MG | CHEMILLENNIUM INTERNATIONAL (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- FIV 逆轉錄酶通常對 NNRTI 不敏感，機轉基礎薄弱，且疾病屬於獸醫範疇，沒有人類臨床目標。

**補充說明：** 同一份預測清單中的第二項「猴免疫缺乏病毒 (SIV) 感染」有 17 筆文獻，但都是體外、嵌合病毒與獼猴模型的前臨床研究，證據等級為 L4，建議同樣是 Hold。這些研究的價值在於作為 HIV-1 RT 抑制劑與抗藥性的研究模型，不能視為臨床療效證據。第三項罕見神經發育疾病則完全無法建立機轉連結，證據等級為 L5。

**若要推進需要：**
- 確認是否將獸醫適應症納入本專案範圍；若不納入，建議直接排除此預測。
- 補充 Nevirapine 的作用機轉資料（DrugBank）。
- 取得香港衞生署仿單的警語與禁忌資料（目前為阻斷性缺口）。
- 若仍要評估，需先有 Nevirapine 對 FIV 逆轉錄酶的體外活性資料。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

