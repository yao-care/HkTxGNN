---
layout: default
title: Rivastigmine
parent: 僅模型預測 (L5)
nav_order: 658
evidence_level: L5
indication_count: 1
---

# Rivastigmine
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

# Rivastigmine：預測新適應症為青光眼（原適應症資料缺失）

## 一句話總結

Rivastigmine（DB00989）目前香港市場資料顯示**未上市**，本次 Evidence Pack 也未提供原始適應症與正式作用機轉資料。
TxGNN 模型預測它可能對**青光眼 (Glaucoma)** 有效，
目前有 **3 篇文獻**支持這個方向，但**尚無相關臨床試驗登記**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（本次 Evidence Pack 未提供，需另行查證） |
| 預測新適應症 | 青光眼 (Glaucoma) |
| TxGNN 預測分數 | 99.27% |
| 證據等級 | L4（動物實驗 + 機轉研究，無人體臨床試驗） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

本次 Evidence Pack 未提供 Rivastigmine 正式的作用機轉（MOA）資料，此項目被標記為資料缺口（DG002，High severity）。

根據所收集文獻的內容，Rivastigmine 為一種選擇性乙醯膽鹼酯酶（AChE）抑制劑。文獻指出，非選擇性 AChE 抑制劑本身即具有降眼壓作用，而動物實驗（兔子模型）證實局部給予 Rivastigmine 可有效降低眼壓（IOP）。另一篇機轉研究進一步說明膽鹼激導性系統透過毒蕈鹼受體（M3R）調節房水排出，是降眼壓的潛在路徑。

這些線索提供了機轉層面的合理性，但目前僅止於臨床前（動物）與回顧性文獻，缺乏人體臨床試驗與正式 MOA 資料佐證，關聯性推論的強度有限。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | 機轉研究 | Frontiers in molecular biosciences | 膽鹼激導性藥物透過毒蕈鹼受體（M3R）調節眼壓，結合系統遺傳學與分子模型分析 |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | 文獻回顧（專利文獻） | Expert opinion on therapeutic patents | AChE 輕度抑制在阿茲海默症、重症肌無力、青光眼皆具治療潛力 |
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | 動物實驗 | Journal of ocular pharmacology and therapeutics | 局部給予 Rivastigmine 可降低兔子眼壓（IOP），為選擇性 AChE 抑制劑 |

---

## 香港上市資訊

目前未在香港上市，無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：本次 Evidence Pack 中，TFDA/香港仿單警語與禁忌資料屬於**阻斷型（Blocking）資料缺口**（DG001），在補齊前無法完成安全性初評（S1）。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 1 篇動物實驗（兔子模型）與 2 篇機轉性回顧文獻支持，無任何人體臨床試驗證據。
- 香港未上市（0 張許可證），且正式 MOA 與仿單安全性資料均缺失，其中仿單警語/禁忌為 Blocking 等級缺口，無法進行安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌資料（DG001，Blocking，優先處理）
- 查證並補充正式作用機轉（MOA）資料（DG002）
- 確認 Rivastigmine 原始核准適應症與現有臨床使用資料
- 若機轉假說成立，規劃人體概念驗證（proof-of-concept）研究，作為進入下一階段的前提
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

