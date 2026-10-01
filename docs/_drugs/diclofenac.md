---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac：從非類固醇消炎止痛藥 (NSAID) 到頭皮單純性毛髮稀少症

## 一句話總結

Diclofenac 是一種 COX 抑制型 NSAID，在香港已有多張上市許可證。
TxGNN 模型預測它可能對**頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅是模型預測，且機轉上找不到合理關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 99.69%（模型排名 6405） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Diclofenac 屬於 NSAID 類藥物，一般認為它透過抑制 COX-1/COX-2 來減少前列腺素相關的發炎與疼痛。

不過，頭皮單純性毛髮稀少症是一種遺傳性毛囊疾病，已知與 CDSN、APCDD1、RPL21 等基因變異有關。COX 抑制並不作用於這些致病路徑，因此**機轉上沒有合理關聯**。99.69% 的分數只是知識圖譜的預測結果，不代表有臨床意義。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-37120 | VOLTAREN SR 75 TAB | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-36029 | VOLTAREN SUPP 50MG (FOR ADULTS) | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-68555 | EFORMAT DICLOFENAC SODIUM TABLETS 25MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-67188 | OCIPIL DICLOFENAC SODIUM GASTRO-RESISTANT TABLETS 50MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-67920 | JOINTISH GASTRO-RESISTANT TABLETS 50MG | WELLDONE PHARMACEUTICALS LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測僅有模型分數，沒有臨床試驗、文獻或機轉依據，證據等級為 L5。
- 該疾病由基因變異導致，NSAID 的 COX 抑制作用無法對應其致病機轉。

**補充觀察：** 在同一藥物的其他預測中，只有**幼年型特發性關節炎 (Juvenile Idiopathic Arthritis)**（第 9 名，分數 99.25%）有相關資料，證據等級 L4，建議為「研究問題 (Research Question)」。
- 機轉上合理：NSAID 本來就是 JIA 的症狀控制療法，屬於緩解症狀，而非改變疾病進程。
- 目前的 2 個試驗都不是直接檢驗 Diclofenac 的研究：
  - [NCT00688545](https://clinicaltrials.gov/study/NCT00688545) 是 NSAID 與 celecoxib 的觀察性安全登記研究，已終止，共 275 人。
  - [NCT05871086](https://clinicaltrials.gov/study/NCT05871086) 是輔酶 Q10 的 Phase 2/3 試驗，狀態未知，共 60 人。
- 若要考慮兒童使用，需另做安全性與劑量評估。

**若要推進需要：**
- 補齊香港衛生署 (Department of Health) 仿單的警語與禁忌症資料，目前這是阻擋進入安全性篩選的缺口。
- 補齊 DrugBank 的作用機轉資料，以利機轉關聯分析。
- 若要繼續探索，建議把資源轉向 JIA 這類機轉合理的適應症，並先做針對 Diclofenac 的文獻與試驗檢索。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

