---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 709
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel：從急性冠心症抗血小板治療到肺高壓

## 一句話總結

Prasugrel 是 P2Y12 抗血小板藥物，文獻脈絡顯示它用於接受經皮冠狀動脈介入（PCI）的急性冠心症（ACS）患者。
TxGNN 模型預測它可能對**肺高壓 (Pulmonary Hypertension)** 有效，但目前**沒有直接相關的臨床試驗或文獻**，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；文獻脈絡為 ACS 患者 PCI 後的抗血小板治療 |
| 預測新適應症 | 肺高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.88%（模型排名 3040） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Prasugrel 是不可逆的 P2Y12 受體拮抗劑，屬 thienopyridine 類，作用是抑制血小板活化與聚集。目前資料缺乏完整的作用機轉說明，以下推論僅來自證據包中的機轉假設。

血小板活化與肺血管病變之間存在理論上的關聯，因此機轉上可以想像抗血小板治療對肺高壓有幫助。但這只是概念性的推測，目前沒有任何資料直接支持，高分只代表模型的預測。

## 臨床試驗證據

檢索到的 2 項試驗與 Prasugrel、肺高壓都無直接關係（相關性評為 C 級），僅供參考。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | 完成 | 500 | 西班牙高齡非瓣膜性心房顫動患者的 NOAC 使用管理，觀察性研究，與本藥無關 |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | 完成 | 300 | 癌症相關血栓患者是否符合 CARAVAGGIO 試驗收案條件的回溯研究，與本藥無關 |

## 文獻證據

下列 2 篇為世代研究，同樣沒有直接討論 Prasugrel 與肺高壓的關係。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | ACS 患者 PCI 後使用 clopidogrel 及依從性的相關因素，Prasugrel 僅在指引背景中提及 |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | COVID-19 前的共病用藥對致死結果的影響（ACTIVE 登錄研究），與肺高壓治療無關 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66424 | PRASUGREL TABLETS 5MG（Camber Pharmaceuticals Hong Kong Limited） | — | — |
| HK-66423 | PRASUGREL TABLETS 10MG（Camber Pharmaceuticals Hong Kong Limited） | — | — |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 肺高壓這項預測只有模型分數，沒有任何直接的臨床試驗或文獻支持，證據等級為 L5。
- 檢索到的試驗與文獻都與 Prasugrel 和肺高壓無關，機轉連結也只是假設。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症。
- 補齊 DrugBank 的作用機轉資料，並分析 P2Y12 抑制與肺血管病變的機轉關聯。
- 搜尋 P2Y12 抑制劑用於肺高壓的前臨床或臨床研究。

**其他預測方向（供參考）：**
- 偏頭痛 (Migraine Disorder) 的證據相對較多，等級為 L4。
- 有 thienopyridine 類藥物的回溯性研究和 ticagrelor 的開放標示先導試驗，主要用於合併卵圓孔未閉（PFO）的患者。
- 這些證據屬於藥物類別層級，不是 Prasugrel 本身的資料。
- 該方向可作為研究問題，建議另行評估。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

