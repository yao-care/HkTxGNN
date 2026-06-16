---
layout: default
title: Gadobenic Acid
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Gadobenic Acid
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

# Gadobenic acid：從 MRI 顯影劑到骨關節炎

## 一句話總結

Gadobenic acid（鈣鹽形式常見品名 MultiHance，化學名 Gd-BOPTA）是一種釓基 MRI 顯影劑，原本用於磁振造影的對比增強診斷。
TxGNN 模型預測它可能對**骨關節炎 (osteoarthritis)** 有效，然而深入分析顯示：現有 **1 篇文獻**均屬影像學診斷性應用，並非治療性證據；所有預測高度疑似 KG 圖形傳播假陽性。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無紀錄（已知用途：MRI 顯影劑） |
| 預測新適應症 | 骨關節炎 (osteoarthritis) |
| TxGNN 預測分數 | 99.21% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

**短答：合理性極低，所有預測均高度疑似假陽性。**

Gadobenic acid 是帶有配體 BOPTA（苯氧基乙酸衍生物）的釓螯合物。靜脈注射後，它藉由縮短 T1 弛豫時間來增強 MRI 對比度，本身**無任何已知藥理治療活性**。作用機轉（MOA）資料缺失（Data Gap），但其診斷性機轉已清楚：釓離子並非靶向特定受體或酶，而是物理性地改變周圍水分子的磁共振訊號。

TxGNN 知識圖譜（KG）很可能將「此藥物曾出現在某疾病的相關研究中」誤讀為「此藥物可治療該疾病」。以排名第 1 的骨關節炎為例：dGEMRIC（delayed Gadolinium Enhanced MRI of Cartilage）技術正是以 Gd-DTPA²⁻（與 gadobenate 同為釓顯影劑）的排斥原理反映軟骨 GAG 含量——這是純診斷影像學技術，不具治療意義。

後續 9 個預測（骨關節炎易感性、類風濕性關節炎、brachyolmia、罕見骨骼發育不良、BPH、myosclerosis、alopecia 等）的機轉連結同樣建立在「診斷性共現」或「ECM/軟骨節點鄰近傳播」，均缺乏治療性生物學依據。**目前無任何臨床或前臨床證據顯示 gadobenic acid 對上述任何適應症具備治療活性。**

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻均為**診斷性影像學研究**，Gadobenic acid 在其中扮演 MRI 顯影劑角色，並非治療藥物。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [28696168](https://pubmed.ncbi.nlm.nih.gov/28696168/) | 2018 | 橫斷面影像研究 | Acta Radiologica | 以 dGEMRIC 評估肥胖膝骨關節炎患者減重前後軟骨形態變化，探討軟骨品質改善的「不歸點」——顯影劑用於影像診斷，非治療 |
| [23449952](https://pubmed.ncbi.nlm.nih.gov/23449952/) | 2013 | 橫斷面影像研究 | Radiology | 探討半劑量與全劑量 gadobenate dimeglumine 在 3T MRI 評估早期類風濕性關節炎滑膜炎的診斷價值 |
| [11289630](https://pubmed.ncbi.nlm.nih.gov/11289630/) | 2001 | 橫斷面影像研究 | Skeletal Radiology | 確定 Gd-BOPTA 用於類風濕性關節炎腕部 MRI 的適當劑量 |
| [20680496](https://pubmed.ncbi.nlm.nih.gov/20680496/) | 2010 | 橫斷面影像研究 | La Radiologia Medica | 以 MRI（含顯影劑）評估早期類風濕性關節炎寰樞椎關節受累情形 |
| [21954100](https://pubmed.ncbi.nlm.nih.gov/21954100/) | 2011 | 橫斷面影像研究 | Arthritis Care & Research | MRI 追蹤早期類風濕性關節炎緊密控制治療後寰樞椎受累變化 |

## 香港上市資訊

Gadobenic acid 在香港目前無任何已登記許可證，屬**未上市**藥物。

## 安全性考量

安全性資訊請參考原廠仿單。

> **⚠️ 特別注意（顯影劑類別）：** 釓基顯影劑（GBCAs）類別已知風險包括腎源性系統纖維化（NSF，尤其見於腎功能嚴重受損患者）及釓在腦部（齒狀核、蒼白球）的長期沉積。Gadobenate dimeglumine 為大環/線性混合結構，具體安全性評估請查閱原廠仿單或 EMA/FDA 相關警語公告。

## 結論與下一步

**決策：Hold**

**理由：**
Gadobenic acid 是診斷性 MRI 顯影劑，不具已知治療活性。TxGNN 的所有 10 項預測均來自「診斷性共現」或「KG 圖形鄰近傳播」，屬方法論假陽性，而非真實的藥物再利用機會。香港亦無任何上市許可。

**建議行動：**
- 將此藥物標記為「純診斷性顯影劑」，在 TxGNN KG 中加入排除標記（如 `drug_class: contrast_agent`），避免後續預測重複產生同類假陽性
- 若需研究「釓顯影劑 + 疾病診斷」的應用，應改以影像生物標記（biomarker）研究框架處理，而非老藥新用框架
- 無須進行進一步的老藥新用評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

