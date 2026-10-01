---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 3
---

# Olanzapine
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

# Olanzapine：從抗精神病藥到嬰兒良性陣發性斜頸

## 一句話總結

Olanzapine（奧氮平）在香港已上市，但本次資料未收錄其原適應症。
TxGNN 模型預測它可能對**嬰兒良性陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 嬰兒良性陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy) |
| TxGNN 預測分數 | 99.54%（模型排名第 8,464） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，本次資料也沒有收錄 Olanzapine 的原適應症。

從機轉來看，現有資料**無法支持**這個預測。這種病是自限性的嬰兒疾病，屬偏頭痛譜系，與 CACNA1A 離子通道異常有關，通常不需治療就會自行緩解。Olanzapine 的 D2/5-HT2A 受體拮抗作用，在此疾病中沒有已知的治療角色。

此外，Olanzapine 本身可能引起肌張力不全 (dystonia) 和斜頸等不良反應。因此 99.54% 的高分可能只反映知識圖譜中，該藥與動作障礙相關節點距離接近，並不代表有治療效益。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60432 | APO-OLANZAPINE TAB 5MG | HIND WING CO LTD |
| HK-60725 | APO-OLANZAPINE TAB 2.5MG | HIND WING CO LTD |
| HK-62522 | NYKOB ORODISPERSIBLE TABLETS 10MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-63034 | OZAPEX ORODISPERSIBLE TABLETS 10MG | I & C (HONG KONG) LIMITED |
| HK-65790 | ZYLANZA ORODISPERSIBLE TABLETS 10MG | LSB (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，如上所述，Olanzapine 可能引起肌張力不全與斜頸，用於斜頸相關疾病需特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有臨床試驗或文獻。
- 該疾病本身會自行緩解，且藥物可能誘發類似症狀，缺乏機轉上的合理性。

**若要推進需要：**
- 取得 Olanzapine 的作用機轉與原適應症資料
- 取得香港衛生署仿單的警語與禁忌資料
- 確認預測是否只是圖譜鄰近性造成的假訊號
- 找到任何支持此適應症的臨床或病例證據

**其他預測適應症（供參考）：**
- **懼曠症 (Agoraphobia)**（分數 99.47%，L3）：有一項開放標籤試驗與數則病例報告，但研究對象是恐慌症，沒有隨機對照試驗。
- **輕度慢性憂鬱症 (Dysthymic Disorder)**（分數 99.28%，L4）：僅有間接證據，只能支持藥物類別層級的推論。

這兩項的證據都比嬰兒良性陣發性斜頸多，若要優先研究，可考慮先從它們著手。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

