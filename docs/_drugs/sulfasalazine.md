---
layout: default
title: Sulfasalazine
parent: 僅模型預測 (L5)
nav_order: 825
evidence_level: L5
indication_count: 5
---

# Sulfasalazine
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

# Sulfasalazine：TxGNN 預測新適應症評估（首位預測：先天性短指並指症候群）

## 一句話總結

Sulfasalazine 在香港已有 5 張上市許可證，但資料中沒有登載原適應症。
TxGNN 預測分數最高的新適應症是**先天性短指並指症候群 (Brachydactyly-Syndactyly Syndrome)**，目前**沒有任何臨床試驗或文獻**支持，推測是知識圖譜的拓樸假象。
五個預測中，只有**骨關節炎 (Osteoarthritis)** 有間接的前臨床證據（1 篇動物實驗、數篇細胞實驗），沒有人體療效資料。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症（排名第 1） | 先天性短指並指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Sulfasalazine 屬於抗發炎／免疫調節類藥物，但資料包內的作用機轉欄位是空的，且原適應症也沒有登載。

先天性短指並指症候群是罕見的先天性肢體畸形。抗發炎藥物與這類先天畸形之間，找不到合理的生物學連結，也沒有任何試驗或文獻。0.999 的高分很可能是知識圖譜結構造成的假象，不能當作療效依據。

其他四個預測的狀況：

| 排名 | 預測疾病 | 分數 | 證據等級 | 判斷 |
|------|---------|------|---------|------|
| 2 | 眼缺損性小眼症－根段肢體發育不良症候群 | 99.94% | L5 | 罕見發育異常，無連結，疑為圖譜假象 |
| 3 | 骨關節炎易感性 | 99.88% | L5 | 是基因易感性標籤，不是可治療的臨床疾病，只能透過下方「骨關節炎」間接關聯 |
| 4 | 先天性毛髮稀少合併青少年黃斑部失養症 | 99.66% | L5 | 罕見單基因疾病，無生物學依據 |
| 5 | 骨關節炎 | 99.64% | L4 | 有間接前臨床證據，見下節 |

## 值得關注的替代方向：骨關節炎

骨關節炎是五個預測中唯一有實質證據的，雖然分數排名第 5。其間接機轉線索包括：

- 抑制 NF-κB 訊號。
- 抑制胱胺酸／麩胺酸反向轉運體（system xc⁻，SLC7A11），這與鐵死亡 (ferroptosis) 有關。
- 前臨床研究顯示，它能減少細胞激素誘發的軟骨蛋白聚醣與膠原釋放，並下調基質金屬蛋白酶。
- 在前十字韌帶切斷合併半月板切除的動物模型中，它能減輕軟骨破壞。
- 含 sulfasalazine 的玻尿酸製劑在大鼠骨關節炎模型中，減輕了發炎與軟骨降解。
- 較早期的研究顯示，它能抑制前列腺素與白三烯的釋放。

目前**沒有任何人體骨關節炎療效資料**。

## 臨床試驗證據

首位預測（先天性短指並指症候群）：目前無相關臨床試驗登記。

骨關節炎預測下的 2 筆試驗，經檢視後都不能當作直接證據：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00551707](https://clinicaltrials.gov/study/NCT00551707) | Phase 2 | 完成 | 51 | CRx-102（dipyridamole 加低劑量 prednisolone）用於類風濕性關節炎的隨機雙盲試驗；資料未顯示 sulfasalazine 是試驗藥物，不能視為直接證據 |
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | 完成 | 479 | 回溯性世代研究，比較 tofacitinib 合併 methotrexate 後停用或繼續 MTX 的結果；未評估 sulfasalazine，也非針對骨關節炎，不相關 |

## 文獻證據

首位預測（先天性短指並指症候群）：目前無相關文獻。

骨關節炎預測下的相關文獻（依證據強度挑選，皆為前臨床或回顧性質）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | 前臨床（細胞／動物） | Int J Biol Macromol | Sulfasalazine 玻尿酸製劑可持續釋放藥物達 60 天，並減輕大鼠骨關節炎模型的發炎與軟骨降解 |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | 前臨床（動物） | J Orthop Res | 抑制 system xc⁻，減輕前十字韌帶切斷合併半月板切除造成的軟骨破壞 |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | 前臨床（細胞） | Rheumatology (Oxford) | 阻斷細胞激素刺激的軟骨釋放蛋白聚醣與膠原，並下調 MMP |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | 前臨床（細胞） | Mod Rheumatol | Sulfasalazine 與 tofacitinib 會改變關節軟骨細胞的蛋白質表現 |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | 前臨床（細胞） | Wien Klin Wochenschr | Sulfasalazine 及其代謝物影響人類滑膜組織的前列腺素與白三烯釋放 |
| [12205730](https://pubmed.ncbi.nlm.nih.gov/12205730/) | 2002 | 臨床觀察 | Yonsei Med J | 類風濕性關節炎患者使用 sulphasalazine 與尿液膠原交聯物排泄的關係（研究對象為類風濕性關節炎，非骨關節炎） |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | 回顧鐵死亡在發炎性關節炎（含骨關節炎）中的角色 |

## 香港上市資訊

資料中的劑型與核准適應症欄位皆為空白，因此只列許可證號、品名與廠商：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-61726 | ZOPYRIN ENTERIC-COATED TABLETS 500MG | LSB (HK) LIMITED |
| HK-53542 | SULPHASALAZINE ENTERIC COATED TAB 500MG | EUROPHARM LAB CO LTD |
| HK-60601 | SARIDINE-E ENTERIC COATED TAB 500MG | ATLANTIC PHARMACEUTICAL LIMITED |
| HK-43380 | PMS-SULFASALAZINE E.C. TAB 500MG | TRENTON-BOMA LTD |
| HK-25960 | SALAZOPYRIN EN TAB 0.5G ENTERIC COATED | PFIZER CORPORATION HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢也沒有找到資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測沒有任何試驗、文獻或機轉支持，高分很可能是圖譜假象，不宜投入資源。
- 骨關節炎有間接前臨床證據，可列為「研究問題 (Research Question)」。但目前沒有人體療效資料，兩筆登記試驗也不相關。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌症（資料缺口 DG001，目前阻擋安全性篩選）。
- 補齊作用機轉資料（資料缺口 DG002，可查詢 DrugBank）。
- 若要探索骨關節炎方向，需先檢索 sulfasalazine 用於骨關節炎的人體試驗。可檢查 NCT00551707 的試驗內容是否真的涉及 sulfasalazine。
- 先天性短指並指症候群等罕見疾病預測，建議不要推進，除非另有基因或通路層面的證據。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

