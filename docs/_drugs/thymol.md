---
layout: default
title: Thymol
parent: 僅模型預測 (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
---

# Thymol
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

# Thymol：從外用複方成分到室間隔瘤 (Interventricular Septum Aneurysm)

## 一句話總結

Thymol（百里酚）是從百里香萃取的單萜類酚類化合物，在香港多為外用製劑的成分。
TxGNN 模型預測它可能對**室間隔瘤 (Interventricular Septum Aneurysm)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 室間隔瘤 (Interventricular Septum Aneurysm) |
| TxGNN 預測分數 | 99.25% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。已知 Thymol 是單萜類酚類化合物，具有抗氧化、抗發炎與抗菌活性。

這些一般性的藥理活性，並沒有被證實與心臟結構缺損有關。室間隔瘤屬結構性心臟異常，一般不預期能靠藥物治療改善。

因此這個高分預測目前找不到合理的機轉連結，較可能來自知識圖譜中相關節點的鄰近關係（graph proximity），而非藥物生物學上的依據。預測排名前 10 的其他疾病（肺動脈瓣疾病、Pierre Robin 症候群、染色體缺失症候群等）也有同樣情形：多為先天性結構或基因異常，且都沒有臨床或文獻證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

> 補充說明：系統針對其他預測適應症（如岩藻聚醣合成異常）檢索到的文獻，內容都是 Thymol 的一般性研究，例如抗氧化、抗菌，以及敗血症、脂肪肝、子宮內膜異位症的動物模型。這些是以 Thymol 為關鍵字檢索到的結果，並非針對室間隔瘤，不能當作本預測的證據。

## 香港上市資訊

下表列出 5 張主要許可證，劑型與核准適應症欄位在資料中均為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-33438 | BELANTOIN CREAM | MEYER PHARMACEUTICALS LTD |
| HK-31687 | BURN CREAM | MEDIPHARMA LTD |
| HK-33439 | BETOCAINE CREAM | MEYER PHARMACEUTICALS LTD |
| HK-54098 | SINSIN PAS PLASTER | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-59559 | EUGENPAS PATCH | EUGENPHARM INTERNATIONAL LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有臨床試驗和針對性文獻。
- 機轉上也找不到合理連結：室間隔瘤是結構性缺損，Thymol 的已知活性與之無關。

**若要推進需要：**
- 取得香港衛生署的藥品仿單，補齊警語與禁忌症，這是目前的阻斷性缺口。
- 補充 Thymol 的作用機轉資料（可查詢 DrugBank）。
- 先以文獻或前臨床研究驗證是否存在任何心臟結構或心肌重塑相關的機轉，再考慮重新評估。
- 排名前 10 的候選適應症目前都是 L5 / Hold。若要尋找有潛力的方向，建議優先檢視有針對性證據的適應症，而不是依 TxGNN 分數排序。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

