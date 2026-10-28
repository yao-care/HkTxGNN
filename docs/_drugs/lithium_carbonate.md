---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
monitor_inn: "LITHIUM CARBONATE"
predicted_indications: ["pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "brachydactyly-syndactyly syndrome", "Behr syndrome", "WHIM syndrome", "combined immunodeficiency due to moesin deficiency"]
last_modified_at: 2026-10-28
description: "Lithium Carbonate：預測新適應症為假性軟骨發育不全 (Pseudoachondroplasia)（證據等級 L5）。原適應症：本次整理的資料中，香港許可證未載明核准適應症文字"
---

# Lithium Carbonate
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

## 碳酸鋰（Lithium Carbonate）：從雙相情緒障礙到假性軟骨發育不全
{: .text-alpha }

## 一句話總結

碳酸鋰是情緒穩定劑，知識圖譜中記錄的相關用途包括雙相情緒障礙、類風濕性關節炎等。
TxGNN 模型預測它可能對**假性軟骨發育不全 (Pseudoachondroplasia)** 有效，
但目前**沒有任何臨床試驗或直接相關文獻**支持，屬於僅有模型預測的階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，香港許可證未載明核准適應症文字；知識圖譜記錄的相關關係包含雙相情緒障礙、躁鬱症、類風濕性關節炎等（非核准適應症） |
| 預測新適應症 | 假性軟骨發育不全 (Pseudoachondroplasia) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理學，鋰會抑制 GSK-3β，並調節 Wnt 訊號與自噬作用。

假性軟骨發育不全由 COMP 基因突變引起，會造成軟骨細胞內質網壓力與細胞外基質缺陷。鋰對 Wnt 與自噬的調節，理論上可能與軟骨細胞壓力有關，但這純屬推測，本次資料中沒有任何研究支持。

此分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無直接研究假性軟骨發育不全的文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66420 | CAMCOLIT CONTROLLED RELEASE TABLETS 400MG | 未載明 | 未載明 |
| HK-60530 | PMS-LITHIUM CARBONATE CAP 300MG | 未載明 | 未載明 |
| HK-62229 | APO-LITHIUM CARBONATE CAPSULES 300MG | 未載明 | 未載明 |
| HK-67216 | LITHIUM CARBONATE ESSENTIAL PHARMA TABLETS 250MG | 未載明 | 未載明 |
| HK-62228 | APO-LITHIUM CARBONATE CAPSULES 150MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：腎臟疾病、認知障礙、甲狀腺功能低下（含黏液水腫、先天性甲狀腺功能低下）、乾癬、猝死性心臟驟停、心臟傳導疾病、尿崩症（含中樞性）等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 重大：Bupropion、Lorcaserin
  - 中度：Acarbose、Famotidine、Metformin、Pioglitazone、Morphine、Metronidazole、Clarithromycin 等
  - 輕微：Doxycycline、Epinephrine、Acetylsalicylic acid

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗或直接相關文獻，證據等級為 L5。
- 鋰的機轉與假性軟骨發育不全之間的連結缺乏資料支持，且鋰具有腎臟、甲狀腺等安全性風險，不宜在缺乏證據下推進。

**若要推進需要：**
- 補齊藥物作用機轉資料
- 取得香港仿單的警語與禁忌資訊
- 進行 COMP 突變軟骨細胞或動物模型的前臨床研究
- 評估鋰在兒童骨骼疾病族群的風險效益

**其他候選的備註：** 在 TxGNN 其他預測中，WHIM 症候群（分數 0.9956）的機轉相對較可解釋（鋰可提升嗜中性白血球數），但同樣沒有任何臨床證據，仍屬假說層級。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

