---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 3
---

# Empagliflozin
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

# Empagliflozin：從 SGLT2 抑制劑到古典僵人症候群

## 一句話總結

Empagliflozin 是一種 SGLT2 抑制劑，在香港已有多張上市許可證，但資料中未載明原核准適應症。
TxGNN 模型預測它可能對**古典僵人症候群 (Classic Stiff Person Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 古典僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Empagliflozin 屬於 SGLT2 抑制劑，作用在腎臟的葡萄糖再吸收。
但現有資料無法支持它與僵人症候群之間有直接的機轉關聯。

僵人症候群是一種以自體免疫為主的神經系統疾病，常見抗 GAD65 抗體陽性，
也常與第一型糖尿病及其他自體免疫疾病並存。
TxGNN 的高分（99.06%）較可能來自知識圖譜中「糖尿病」或「自體免疫」節點的距離相近，
而不是藥物真的具有治療效果。這個推論屬於推測，尚未經任何驗證。

此外，排名第 2 的**局部僵肢症候群 (Focal Stiff Limb Syndrome)** 是僵人症候群譜系的局部變異型，分數完全相同（99.06%）。
兩者在知識圖譜中幾乎重複，不能視為兩個獨立的訊號。
SGLT2 抑制劑也沒有理由影響中樞運動神經元的過度興奮或 GABA 功能異常。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 10 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-64095 | JARDIANCE TABLETS 10MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-64096 | JARDIANCE TABLETS 25MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-65353 | GLYXAMBI TABLETS 10MG/5MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-65354 | GLYXAMBI TABLETS 25MG/5MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-64242 | JARDIANCE DUO TABLETS 12.5MG/1000MG | BOEHRINGER INGELHEIM (HK) LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有臨床試驗、文獻或機轉證據支持。
- 高分可能只是知識圖譜中「糖尿病／自體免疫」的鄰近效應，並非真正的治療訊號。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症資料，才能進行安全性初篩。
- 補充 empagliflozin 的作用機轉資料（可查詢 DrugBank）。
- 進行文獻回顧，確認 SGLT2 抑制與僵人症候群病理（抗 GAD65 自體免疫、GABA 功能異常）之間是否有任何實證連結。
- 若上述都找不到支持，建議不再往此適應症推進。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

