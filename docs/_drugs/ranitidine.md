---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 757
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ranitidine：預測新適應症為活動性消化性潰瘍 (Active Peptic Ulcer Disease)（證據等級 L5）。原適應症：胃潰瘍、胃食道逆流、食道炎、消化不良、十二指腸潰瘍、Zollinger-Ellison 症候群等"
monitor_inn: "RANITIDINE"
predicted_indications: ["duodenal obstruction"]
---

# Ranitidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Ranitidine：從消化性潰瘍相關疾病到活動性消化性潰瘍

## 一句話總結

Ranitidine（雷尼替丁）是 H2 受體拮抗劑，原本用於胃潰瘍、十二指腸潰瘍、胃食道逆流等酸相關疾病。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前有 **0 個臨床試驗**和 **約 20 篇文獻**支持這個方向。
但此預測實質上屬於原有適應症範圍，並非真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃潰瘍、胃食道逆流、食道炎、消化不良、十二指腸潰瘍、Zollinger-Ellison 症候群等（許可證上未載明適應症文字） |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3（僅有綜述等文獻，無臨床試驗登記；資料編譯結果標示為 L1，但依本報告判定規則，缺乏已完成的 Phase 3 RCT 資料，故以 L3 計） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ranitidine 是 H2 受體拮抗劑，透過阻斷胃壁細胞上的組織胺 H2 受體來抑制胃酸分泌，而抑制胃酸正是促進消化性潰瘍癒合的既定機轉。

活動性消化性潰瘍包含胃潰瘍與十二指腸潰瘍，與 Ranitidine 原本的適應症高度重疊，因此這項預測本質上是「適應症內」的延伸，並非嚴格意義上的藥物再利用。

需要注意的是，Ranitidine 因 NDMA 雜質問題，在 2019–2020 年間於許多市場下架，供應與製劑品質需要另外確認。此外，其他 H2 受體拮抗劑（如 famotidine）或質子幫浦抑制劑可能是更合適的選擇。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intell Clin Pharm | Ranitidine 抑制胃酸的效力為 cimetidine 的 4–10 倍，療效相當且耐受性佳 |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | 探討前列腺素與 H2 受體拮抗劑在消化性潰瘍中的角色 |
| [9506245](https://pubmed.ncbi.nlm.nih.gov/9506245/) | 1998 | Review | Drugs | Rabeprazole 的藥理與臨床試驗比較（含與 famotidine 等比較） |
| [8736619](https://pubmed.ncbi.nlm.nih.gov/8736619/) | 1996 | Review | Drugs | Ebrotidine 的抗分泌作用與 ranitidine 相近 |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Nizatidine 用於消化性潰瘍的初步回顧 |
| [1717223](https://pubmed.ncbi.nlm.nih.gov/1717223/) | 1991 | Review | Drugs | Roxatidine 的藥效學與治療潛力回顧 |
| [3527658](https://pubmed.ncbi.nlm.nih.gov/3527658/) | 1986 | Review | Drugs | Omeprazole 用於消化性潰瘍與 Zollinger-Ellison 症候群 |
| [12635419](https://pubmed.ncbi.nlm.nih.gov/12635419/) | 2003 | Review | Gastroenterol Clin North Am | 懷孕期間胃與十二指腸潰瘍的處置 |
| [11249534](https://pubmed.ncbi.nlm.nih.gov/11249534/) | 2000 | Review | Expert Opin Pharmacother | Clarithromycin 用於幽門螺旋桿菌感染 |
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | 臨床研究 | Scand J Gastroenterol | Ranitidine 300 mg/日，4 週癒合率：十二指腸潰瘍 91%、幽門前潰瘍 68%、胃體潰瘍 81%；並評估維持治療預防復發 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41546 | EUROTAC TAB 150MG | — | 未載明 |
| HK-60962 | STOMACHAL TAB 150MG | — | 未載明 |
| HK-55824 | RANTIN TAB 150MG | — | 未載明 |

## 安全性考量

- **知識圖譜標示之疾病風險（非仿單內容）**：卟啉症（紫質症）、腎臟疾病、肝臟疾病、膽囊疾病、胃癌（含胃腺癌、瀰漫性胃癌等）
- **藥物交互作用**：共查得 100 筆，以下為部分範例
  - 重大 (Major)：Atazanavir
  - 中度 (Moderate)：Acalabrutinib、Acetohexamide、Aminophylline、Bosutinib、Brigatinib、Cefuroxime、Ceritinib、Chlorpropamide 等
  - 輕微 (Minor)：Acetaminophen、Alendronic acid、Aluminum hydroxide、Calcium carbonate、Cisapride 等

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 此適應症屬於 Ranitidine 原有的消化性潰瘍治療範圍，機轉明確、文獻豐富，但缺乏臨床試驗登記，且 NDMA 污染事件使供應與品質有疑慮。

**若要推進需要：**
- 確認香港市場產品的 NDMA 檢測結果與供應狀況
- 與 famotidine 或 PPI 等替代療法比較，評估是否仍有使用價值
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症資料
- 補充詳細的作用機轉（MOA）資料
- 針對肝腎功能不全、卟啉症患者及重大藥物交互作用（如 atazanavir）制定用藥監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

