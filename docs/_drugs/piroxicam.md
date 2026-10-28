---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
last_modified_at: 2026-10-23
description: "Piroxicam：預測新適應症為眼缺損小眼症－肢根型骨發育不良症候群 (colobomatous microphthalmia-rhizomelic dysplasia syndrome)（證據等級 L3）。原適應症：類風濕性關節炎、骨關節炎"
---

# Piroxicam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Piroxicam：從類風濕性關節炎到眼缺損小眼症－肢根型骨發育不良症候群
{: .text-alpha }

## 一句話總結

Piroxicam 是一種非類固醇消炎止痛藥（NSAID），在知識圖譜中記錄的原適應症為類風濕性關節炎與骨關節炎。
TxGNN 模型的首位預測為罕見的骨骼發育異常症候群，但這些預測缺乏任何證據。本報告改以有實際文獻的第 10 名預測 **幼年特發性關節炎 (Juvenile Idiopathic Arthritis, JIA)** 為重點評估。目前有 **0 個臨床試驗**登記，以及 **11 篇文獻**（其中直接研究 piroxicam 於兒童關節炎者有數篇，但多為 1986–1991 年的舊研究）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、骨關節炎（來自知識圖譜的關聯記錄；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 幼年特發性關節炎 (Juvenile Idiopathic Arthritis)（第 10 名預測；第 1 名為 colobomatous microphthalmia-rhizomelic dysplasia syndrome，無任何證據） |
| TxGNN 預測分數 | 0.9993（第 1 名預測為 1.0000） |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold（JIA 為研究問題，需進一步驗證） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 欄位無資料）。根據藥理學常識，piroxicam 屬於 COX-1/COX-2 抑制劑，透過減少前列腺素合成來降低發炎與疼痛。這與其在類風濕性關節炎、骨關節炎的作用方向一致。

幼年特發性關節炎同為發炎性關節疾病，關節腫痛的病理過程同樣涉及前列腺素，因此 NSAID 機轉上可能適用。已有針對兒童的 piroxicam 研究，包括與 naproxen 的比較試驗與藥物動力學研究。

需注意：幾項系統性回顧與網絡統合分析（2021、2024）比較了 JIA 的各種 NSAID，但僅憑標題與摘要無法確認 piroxicam 是否納入及其表現。

另外，其餘 TxGNN 高分預測（如短指症、肢中發育不良、假性軟骨發育不全、WHIM 症候群等）皆為遺傳性罕見疾病，與 COX 抑制並無可辨識的機轉關聯，分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而非生物學證據，且無臨床試驗與文獻支持，證據等級皆為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | 系統性回顧／網絡統合分析 | World J Clin Cases | 比較不同 NSAID 用於 JIA，piroxicam 是否納入未能確認 |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | 系統性回顧／網絡統合分析 | Indian Pediatrics | 比較九種 NSAID 於 JIA 的療效與安全性，piroxicam 是否納入未能確認 |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | 多中心雙盲交叉比較 | Br J Rheumatol | 47 名 5–16 歲兒童，piroxicam 與 naproxen 無顯著差異 |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | 臨床研究（可能為開放標示） | Eur J Rheumatol Inflamm | 26 名患者隨機接受 piroxicam 或 naproxen，疼痛與腫脹關節數顯著減少 |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | 藥物動力學研究 | Eur J Clin Pharmacol | 10 名兒童每日一次給藥，平均半衰期約 32.6 小時 |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | 回顧（兒童毒性） | Clin Rheumatol | 描述兒童風濕科病人抗風濕與消炎藥的長期毒性 |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | 藥物治療概述 | Kinderarztliche Praxis | 介紹幼年慢性關節炎藥物治療，含 piroxicam |

## 香港上市資訊

下表為資料中列出的主要許可證（共至少 20 張，清單可能不完整），資料未載明核准適應症文字與劑型：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44672 | PIROXICAM CAP 20MG | 膠囊（依品名） | 資料未載明 |
| HK-61587 | PIROXICAM TABLETS 10MG | 錠劑（依品名） | 資料未載明 |
| HK-37734 | ROSIDEN INJ 20MG/ML | 注射劑（依品名） | 資料未載明 |
| HK-66650 | PIRADEN GEL 0.5% W/W | 凝膠（依品名） | 資料未載明 |
| HK-35197 | APO-PIROXICAM CAP 10MG | 膠囊（依品名） | 資料未載明 |

所有已列許可證皆為單一成分製劑、狀態有效。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：高血壓、腎臟疾病、肝臟疾病、充血性心衰竭、急性肝衰竭、肝炎、凝血疾病、中風／腦血管疾病、心肌梗塞、心血管疾病、活動性消化性潰瘍、貧血、血栓性疾病、藥物性肝損傷等。
- **藥物交互作用**（共 100 筆，列出部分）：
  - 中度：阿斯匹靈、類固醇（hydrocortisone、dexamethasone、betamethasone、triamcinolone、budesonide）、metformin、glimepiride、chlorpropamide、aprepitant、mesalazine、balsalazide 等
  - 輕度：famotidine、ranitidine、cimetidine、linaclotide

其他安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位 TxGNN 預測及其他罕見遺傳疾病預測皆無證據與機轉依據。JIA 雖有數項兒童研究，但多為 1980–90 年代、設計有限，且無登記中的臨床試驗，療效尚未被現代證據確立。
- 目前僅屬研究問題，不宜視為已確立的新適應症。

**若要推進需要：**
- 確認 2021、2024 年網絡統合分析是否納入 piroxicam 及其相對療效
- 取得香港仿單的核准適應症、警語與禁忌，以及兒童用藥資訊
- 補充作用機轉資料
- 評估兒童族群的安全性（心血管、腸胃、腎臟風險）與劑量
- 規劃現代設計的比較研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

