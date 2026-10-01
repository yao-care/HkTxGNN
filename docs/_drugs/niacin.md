---
layout: default
title: Niacin
parent: 僅模型預測 (L5)
nav_order: 606
evidence_level: L5
indication_count: 1
---

# Niacin
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

# Niacin：從已上市藥品到同型合子家族性高膽固醇血症

## 一句話總結

Niacin（菸鹼酸）目前在香港有 3 張許可證，但提供的資料中沒有列出核准適應症。
TxGNN 模型預測它可能對**同型合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 有效。
目前有 **2 個臨床試驗**和 **20 篇文獻**與該疾病相關，但**沒有任何一項直接測試 Niacin 用於 HoFH**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未提供 |
| 預測新適應症 | 同型合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L5（僅有模型預測，無 Niacin 用於 HoFH 的實際研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Niacin 是降血脂藥物類別，其劑型（Niaspan 緩釋錠）與血脂調節有關，機轉上可能適用於高膽固醇血症。

以下為一般藥理知識，並非來自本次提供的紀錄：Niacin 可降低肝臟 VLDL/apoB 的分泌並提升 HDL-C，這條路徑不依賴 LDL 受體。因此在 HoFH 患者 LDL 受體功能缺失或嚴重受損時，理論上仍可能有小幅 LDL-C 下降（一般血脂異常約 15–25%）。這只是機轉上的推測，尚未經 HoFH 族群驗證。

TxGNN 的高分（0.997）反映的是知識圖譜中降血脂藥物與高膽固醇血症的關聯接近，不代表臨床有效。另外，Niacin 的心血管角色已因 AIM-HIGH、HPS2-THRIVE 等結果中性的試驗而弱化，HoFH 也已有證據更充分的選擇，如 PCSK9 抑制劑、lomitapide 和 evinacumab。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 完成 | 18 | Alirocumab（PCSK9 抑制劑）用於 8–17 歲 HoFH 兒童與青少年的開放label研究，評估第 12 週 LDL-C 變化。與 Niacin 無直接關聯，反映 HoFH 已有機轉不同的標準治療 |
| [NCT03110432](https://clinicaltrials.gov/study/NCT03110432) | 不適用 | 完成 | 1695 | 德國極高心血管風險血脂異常患者的 PCSK9 抑制劑使用觀察性登錄。非 HoFH 專屬，無 Niacin 介入，僅提供間接的真實世界治療背景 |

## 文獻證據

以下文獻皆為與 HoFH 或降血脂治療相關的背景資料，並非 Niacin 用於 HoFH 的直接證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | 科學聲明 | Arterioscler Thromb Vasc Biol | 討論非 statin 降 LDL 療法在心血管預防的角色；摘要提到安慰劑對照試驗中，膽酸結合劑、Niacin 和 fibrate 單一治療各自可降低心血管終點 |
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | 綜述 | Expert Rev Cardiovasc Ther | 檢視非 statin 降脂治療，包含 fibrate、ezetimibe、膽酸結合劑、omega-3 與 Niacin，用於 statin 殘餘風險或不耐受的情況 |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | 藥物動力學研究 | Pharmacotherapy | 評估 HoFH 用藥 lomitapide 與多種降脂藥（含 Niacin）的藥物動力學交互作用 |
| [23959229](https://pubmed.ncbi.nlm.nih.gov/23959229/) | 2013 | 綜述 | Nat Rev Cardiol | statin 以外的降脂藥物，用於嚴重高膽固醇血症或混合型血脂異常的輔助或替代治療 |
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | 綜述 | Drugs | HoFH 的診斷與治療挑戰，說明 LDL 受體功能缺失造成極高 LDL-C 與早發動脈粥狀硬化 |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | 綜述 | Atherosclerosis Supplements | HoFH 現行治療成果與未滿足需求；即使有血漿分離術與降脂藥，殘餘風險仍高 |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | 綜述 | Metab Syndr Relat Disord | 家族性高膽固醇血症的現代治療，涵蓋 HoFH 與 HeFH |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | 綜述 | Medicina (Kaunas) | 家族性高膽固醇血症的診斷與治療文獻分析 |
| [19947811](https://pubmed.ncbi.nlm.nih.gov/19947811/) | 2009 | 病例報告 | Pharmacotherapy | 一位 18 歲 HoFH 女性的黃色瘤臨床表現 |
| [3548303](https://pubmed.ncbi.nlm.nih.gov/3548303/) | 1987 | 其他 | Am J Cardiol | 比較肝臟移植、藥物與血漿置換治療 HoFH（無摘要） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60373 | NIASPAN EXTENDED-RELEASE TAB 1000MG（Abbott Lab Ltd） | 未提供 | 未提供 |
| HK-60374 | NIASPAN EXTENDED-RELEASE TAB 500MG（Abbott Lab Ltd） | 未提供 | 未提供 |
| HK-54177 | AMINOLEBAN ORAL POWDER（Otsuka Pharmaceutical (H.K.) Limited） | 未提供 | 未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢未找到資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何 Niacin 用於 HoFH 的臨床試驗或文獻，高預測分數僅反映知識圖譜的關聯。
- HoFH 已有證據更充分的治療，Niacin 的心血管獲益也已被中性結果的試驗削弱，暫無推進的依據。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌症，這是進入安全性篩選的前提
- 補充 Niacin 的作用機轉資料（例如查詢 DrugBank）
- 確認各許可證的核准適應症與劑型
- 系統性搜尋 Niacin 用於 HoFH 的臨床資料，包含病例系列與小型研究
- 與 PCSK9 抑制劑、lomitapide、evinacumab 做比較，評估 Niacin 作為輔助治療的定位
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

