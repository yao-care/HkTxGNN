---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# DIGOXIN：從心房顫動到 Prinzmetal 心絞痛

## 一句話總結

Digoxin 是一種傳統心臟配醣體，臨床上主要用於心房顫動的心率控制及慢性心臟衰竭的輔助治療。
TxGNN 模型預測它可能對 **Prinzmetal 心絞痛 (Prinzmetal angina)** 有效，
目前有 **0 個臨床試驗**和 **2 篇文獻**間接相關，但兩者均與此適應症無直接支持關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房顫動、慢性心臟衰竭（歷史核准適應症，本資料庫未收錄） |
| 預測新適應症 | Prinzmetal 心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。根據已知臨床資訊，Digoxin 是心臟配醣體，透過**抑制細胞膜 Na⁺/K⁺-ATPase**使細胞內鈉離子濃度升高，進而促進鈣離子（Ca²⁺）內流，產生正性肌力作用，並透過抑制房室結傳導來控制心室率。

然而，Prinzmetal 心絞痛（變異型心絞痛）的核心病理為**冠狀動脈血管痙攣**，標準治療是以鈣離子拮抗劑（如硝苯地平）和硝酸鹽類藥物（血管擴張劑）緩解痙攣。Digoxin 透過升高細胞內 Ca²⁺，理論上可能**加劇**血管平滑肌收縮與冠狀動脈痙攣，與 Prinzmetal 心絞痛的治療方向**相悖**，存在潛在加害風險。

兩篇標記為相關的文獻，均與「Digoxin 治療 Prinzmetal 心絞痛」無直接關聯：一篇（PMID 10736610）探討時間藥理學對降壓藥的影響；另一篇（PMID 9206110）討論臥位性心絞痛（angina decubitus）的機轉再評估，臨床定義與 Prinzmetal 不完全相同，且均未主張 Digoxin 對此適應症具療效。**此預測極可能為知識圖譜共現性導致的假陽性，機轉層面亦不支持此再利用方向。**

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Narrative Review | Acta Physiologica et Pharmacologica Bulgarica | 討論晝夜節律對降壓治療之影響，未涉及 Digoxin 治療 Prinzmetal 心絞痛 |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Clinical Review | Chinese Medical Sciences Journal | 再評估臥位性心絞痛（30 例）機轉，發現與勞力性心絞痛相似，未提出 Digoxin 治療主張 |

---

## 香港上市資訊

Digoxin 在香港目前**未上市**，無任何登記許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：Digoxin 屬於治療窗（therapeutic window）極窄的藥物，臨床上需嚴格監測血中濃度。其在 Prinzmetal 心絞痛患者中使用，在無充分安全性評估前，存在理論上加劇冠狀動脈痙攣的風險，應特別謹慎。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 本預測為純 KG 模型輸出（L5 證據等級），無任何直接臨床試驗或文獻支持。
- 藥理機轉分析顯示，Digoxin 升高細胞內 Ca²⁺ 的作用方向與 Prinzmetal 心絞痛的標準治療（鈣離子拮抗、血管擴張）**相反**，理論上存在加重病情的潛在風險，判定為高可能性假陽性。

**若要推進需要：**
- 取得 Digoxin 完整作用機轉（MOA）資料，評估是否有尚未被發現的血管作用機制
- 搜尋是否有基礎研究（細胞或動物模型）提供任何正向機理連結
- 釐清知識圖譜中導致此共現預測的節點關係來源，排除資料品質問題
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

