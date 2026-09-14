---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 718
evidence_level: L5
indication_count: 5
---

# Tadalafil
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

Using the report as a synthesis task (no applicable coding/debugging skill) — generating directly per the specified template and evidence pack.

# Tadalafil：原適應症資料缺失，預測適應症為 Ambras 型先天性全身多毛症

## 一句話總結

Tadalafil 的原始核准適應症在本次 Evidence Pack 中缺失（`original_indications` 為空），僅能從各候選適應症的機轉推論文字得知它是 **PDE5 抑制劑**。TxGNN 模型對它提出 5 個高分預測適應症，但排名最高的是罕見遺傳性疾病 **Ambras 型先天性全身多毛症**，目前**無任何臨床試驗、無藥物特異性文獻**支持，另外 4 個候選也全數落在 L5（純模型預測）等級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未收錄，屬 DG002 影響範圍） |
| 預測新適應症 | Ambras type hypertrichosis universalis congenita（先天性全身多毛症） |
| TxGNN 預測分數 | 99.98%（rank 708） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 五個候選適應症總覽

此候選為多適應症評估（multi），5 個候選全數為 Hold，整理如下：

| Rank | 預測適應症 | TxGNN 分數 | 臨床試驗/文獻 | 判定 |
|------|-----------|-----------|--------------|------|
| 1 | Ambras type hypertrichosis universalis congenita | 99.98% | 0 / 0 | 嵌入雜訊，Hold |
| 2 | Hypertrichosis (disease) | 99.98% | 0 / 0 | 嵌入雜訊，Hold |
| 3 | 牙周病相關畸形症候群 | 99.97% | 0 / 20 | 文獻非藥物特異性，Hold |
| 4 | Dandy-Walker 畸形相關症候群 | 99.97% | 0 / 0 | 嵌入雜訊，Hold |
| 5 | 孤立性遺傳性毛幹異常 | 99.96% | 0 / 0 | 嵌入雜訊，Hold |

## 為什麼這個預測合理？

目前缺乏 Tadalafil 正式登錄的作用機轉資料（`original_moa` 為 [Data Gap]，對應 DG002）。但依各候選適應症的機轉推論文字可確認，Tadalafil 是已知的 **PDE5 抑制劑**，透過抑制磷酸二酯酶第 5 型、提升細胞內 cGMP 濃度，達到血管平滑肌鬆弛與局部血流增加的效果。

排名第 1、2、4、5 的候選適應症（先天性全身多毛症、多毛症、Dandy-Walker 畸形相關症候群、遺傳性毛幹異常）皆屬**基因缺陷或結構發育異常**導致的先天性疾病，與 PDE5 抑制的血管擴張路徑並無已知生物學關聯。這類「TxGNN 分數極高、但完全無支持證據」的組合，是知識圖譜嵌入模型常見的雜訊模式（embedding artifact），尤其容易發生在資料稀疏的罕見遺傳疾病節點上。

排名第 3 的牙周病相關症候群理論上有較合理的間接連結——PDE5 抑制劑增加 cGMP 或可改善牙周組織局部血流灌注。然而檢視提供的 20 篇文獻，全數是牙周病一般性回顧與致病機轉研究，**沒有一篇提及 tadalafil 或 PDE5 抑制劑**，屬於「疾病相關」而非「藥物特異性」文獻，實質佐證力等同於無直接證據。

## 臨床試驗證據

目前無相關臨床試驗登記（5 個候選適應症的 `clinical_trials` 與 `ictrp_trials` 皆為空）。

## 文獻證據

排名第 1 預測適應症（Ambras 型多毛症）目前無相關文獻。

> 補充：排名第 3（牙周病相關症候群）雖有 20 篇文獻，但均為牙周病領域一般性回顧/機轉研究，未提及 tadalafil，不構成藥物特異性證據，故不列入本節主表。

## 香港上市資訊

目前未在香港上市，無許可證資料（`total_licenses = 0`）。

## 安全性考量

安全性資訊請參考原廠仿單。（`key_warnings`、`contraindications`、DDI 查詢皆無資料，其中仿單警語/禁忌屬 DG001，為 Blocking 等級缺口）

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個候選適應症證據等級皆為 L5（僅有模型預測分數，無臨床試驗、無藥物特異性文獻）。
- 4 個候選（多毛症、Dandy-Walker 畸形、遺傳性毛幹異常等）與 Tadalafil 已知 PDE5 抑制機轉無合理生物學連結，判斷為知識圖譜嵌入雜訊。
- 唯一有文獻的候選（牙周病相關症候群）文獻與藥物無直接關聯，等同無實質佐證。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking，屬進入 S1 安全性初評的必要條件）
- 補齊正式的 MOA 與原始核准適應症資料（DG002，High）
- 若要繼續追蹤牙周病候選，需針對「tadalafil／PDE5 抑制劑 + 牙周病」進行藥物特異性文獻檢索，目前尚無此類研究
- 在無新證據前，不建議投入後續資源於本候選組的任一適應症
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

