---
layout: default
title: Prasugrel
parent: 中證據等級 (L3-L4)
nav_order: 409
evidence_level: L4
indication_count: 10
---

# Prasugrel
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Prasugrel：從抗血小板治療到肺動脈高壓

## 一句話總結

Prasugrel 是一種 thienopyridine 類 P2Y12 血小板抑制劑，目前尚未在香港上市，也缺乏正式的核准適應症與作用機轉資料。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，
目前有 **2 個臨床試驗**和 **2 篇文獻**與此方向相關，但均非直接測試 Prasugrel 於肺動脈高壓的療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗血小板治療（急性冠心症／PCI 術後，屬藥物已知用途背景，非香港許可證資料） |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏官方作用機轉（MOA）資料。根據評估包內的文獻佐證，Prasugrel 屬於 thienopyridine 類 P2Y12 血小板抑制劑，其抗血小板效果已於急性冠心症合併經皮冠狀動脈介入術（PCI）患者中被證實（見文獻 PMID 21241206）。

肺動脈高壓的病理機轉涉及原位血栓形成（in-situ thrombosis），抗血小板／抗凝藥物理論上可能有輔助角色。然而，目前所附的臨床試驗與文獻均非直接測試 Prasugrel 於肺動脈高壓之療效，僅為抗栓藥物領域的旁支資料，機轉連結薄弱且缺乏特異性證據。

換言之，這個預測目前仍停留在「藥理類別層級」的間接推論階段，尚無針對 Prasugrel 與肺動脈高壓的直接研究。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | 已完成 | 500 | 觀察性橫斷面研究，描述西班牙高齡非瓣膜性心房顫動患者使用 NOAC（新型口服抗凝血劑）之情形；藥物類別（抗凝血劑而非抗血小板）與疾病（心房顫動而非肺動脈高壓）均與本適應症不符，相關性低 |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | 已完成 | 300 | 回溯性多中心研究，探討癌症相關血栓（CAT）病人是否符合 CARAVAGGIO 試驗收案條件，與 Prasugrel 及肺動脈高壓皆無直接關聯 |

**注意：** 以上兩個試驗經相關性評分均為 C 級（低相關），僅反映抗栓藥物研究領域的背景資料，非 Prasugrel 用於肺動脈高壓的直接證據。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | 探討 ACS 患者接受 PCI 後使用 clopidogrel／prasugrel 之遵從性與持續性影響因素，屬用藥行為研究，非療效證據 |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | 分析 COVID-19 感染前慢性病背景治療對重症死亡風險的影響（ACTIV 登記研究），與肺動脈高壓治療無直接關聯 |

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本評估包標記「TFDA/香港仿單警語與禁忌」為 **Blocking** 等級資料缺口（DG001），在此資料補齊前，無法進行 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
- 現有的 2 個臨床試驗與 2 篇文獻均非直接測試 Prasugrel 於肺動脈高壓之療效，僅為抗栓藥物領域的間接背景資料，機轉連結薄弱（證據等級 L4，決策階段 S0）。
- 藥物本身缺乏作用機轉（MOA）與安全性仿單資料（Blocking 等級缺口），尚不足以支持推進至下一階段評估。

**若要推進需要：**
- 補齊 TFDA／香港仿單的警語與禁忌資料（DG001，Blocking）
- 補齊 Prasugrel 完整作用機轉資料（DG002）
- 尋找直接針對「Prasugrel + 肺動脈高壓」的臨床試驗或機轉研究，而非僅類別層級的間接推論
- 確認香港上市登記狀態（目前為 0 張許可證，未上市）

---

**補充觀察：** 同一評估包中，排名第 2 的候選適應症「偏頭痛 (migraine disorder)」證據等級較高（L3，決策階段 S1，建議為 Research Question），有同類 P2Y12 抑制劑（ticagrelor）及 thienopyridine 類藥物於 PFO 相關偏頭痛的直接文獻支持（PMID 30478067、30478066），機轉推論較肺動脈高壓更具體，建議後續評估時可一併比較優先順序。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

