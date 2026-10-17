---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 706
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pirfenidone：預測新適應症為纖維母細胞腫瘤 (Fibroblastic Neoplasm)（證據等級 L5）。原適應症：特發性肺纖維化、急性間質性肺炎、特發性間質性肺炎"
monitor_inn: "Pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
---

# Pirfenidone
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

# Pirfenidone：從特發性肺纖維化到纖維母細胞腫瘤

## 一句話總結

Pirfenidone 是一種抗纖維化藥物，原本用於治療特發性肺纖維化及相關間質性肺炎。
TxGNN 模型預測分數最高的是**肥大細胞瘤外型 (extracutaneous mastocytoma)**，但該預測沒有任何臨床試驗或文獻支持。
本報告改以**纖維母細胞腫瘤 (fibroblastic neoplasm)** 為主要評估對象，因為它是前 10 名中唯一有文獻（6 篇，多為前臨床研究與個案報告）的方向，且目前**沒有臨床試驗**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 特發性肺纖維化、急性間質性肺炎、特發性間質性肺炎（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 纖維母細胞腫瘤 (Fibroblastic Neoplasm)；排名第 1 的預測為肥大細胞瘤外型 (extracutaneous mastocytoma) |
| TxGNN 預測分數 | 99.23%（纖維母細胞腫瘤）；排名第 1 者為 99.71% |
| 證據等級 | L4（纖維母細胞腫瘤）；排名第 1 者為 L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據文獻摘要，pirfenidone 被認為能抑制 TGF-β 與 PDGF 等生長因子，進而減少上皮與纖維母細胞增生及膠原合成。

原適應症（肺纖維化）與纖維母細胞腫瘤的共同點在於纖維母細胞的異常活化與增生。前臨床研究顯示，pirfenidone 能抑制 Dupuytren 病（一種良性纖維增生性疾病）來源纖維母細胞中 TGF-β1 驅動的活性。這在機轉上提供了間接的合理性。

但必須強調：**抗纖維化活性不等於抗腫瘤療效**。現有證據僅限於良性纖維增生模型，尚未證實對腫瘤有效。此外，有個案報告指出使用 pirfenidone 後出現未分化多形性肉瘤，另有報告指出皮膚纖維瘤在 pirfenidone 合併 mycophenolate 使用期間惡化，這些反而是需要留意的安全訊號。

其他排名較高的預測（如肥大細胞瘤、皮膚纖維肉瘤、侵襲性全身性肥大細胞增生症）同樣缺乏資料支持。肥大細胞疾病主要由 KIT 突變驅動，與 pirfenidone 沒有已知的機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | 先導研究（家族性腺瘤性息肉症的desmoid 腫瘤；設計未經確認） | Am J Gastroenterol | 評估 pirfenidone 對 FAP 相關 desmoid 腫瘤的療效；摘要僅說明其為非細胞毒性抗纖維化藥物，結果無法評估 |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | 體外/前臨床 | BMC Musculoskelet Disord | Pirfenidone 可抑制 Dupuytren 病纖維母細胞中 TGF-β1 介導的作用 |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | 體外/前臨床 | BMC Musculoskelet Disord | 探討 pirfenidone 對 TGF-β1 刺激的非 SMAD 訊號路徑之影響 |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | 體外/前臨床 | Pharm Dev Technol | 評估 pirfenidone 作為 Dupuytren 病局部注射抗纖維化劑的可能性 |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | 個案報告 | Perm J | 使用 pirfenidone 後出現未分化多形性肉瘤（潛在安全訊號） |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | 個案報告 | Rheumatology (Oxford) | 系統性硬化症患者使用 mycophenolate mofetil 與 pirfenidone 後，多發性皮膚纖維瘤惡化 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67135 | ESBRIET TABLETS 267MG（羅氏，ROCHE HONG KONG LIMITED） | 未載明 | 未載明 |
| HK-67136 | ESBRIET TABLETS 801MG（羅氏，ROCHE HONG KONG LIMITED） | 未載明 | 未載明 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下列出部分中度（Moderate）等級的藥物：bupropion、omeprazole、cimetidine、eliglustat、obeticholic acid、oxandrolone、naltrexone、lansoprazole、miconazole、nitisinone、esomeprazole 等。
- **文獻中的安全訊號**：有個案報告指出使用 pirfenidone 後出現未分化多形性肉瘤，以及皮膚纖維瘤惡化。這些為個案層級資訊，因果關係未確立，但在腫瘤相關的再利用情境中須特別留意。

警語與禁忌症的詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有前 10 名預測皆為 L4 或 L5 等級，沒有任何臨床試驗，且僅有間接的前臨床證據。
- 唯一有文獻的方向（纖維母細胞腫瘤）中，還出現了與肉瘤和纖維瘤相關的安全訊號，目前不支持推進。

**若要推進需要：**
- 取得 pirfenidone 的作用機轉資料，並釐清對腫瘤細胞（而非僅對良性纖維母細胞）的作用。
- 取得 2003 年 desmoid 腫瘤先導研究的全文，確認其設計與結果。
- 針對纖維母細胞腫瘤進行腫瘤細胞株與動物模型的前臨床驗證。
- 取得香港原廠仿單，完成警語與禁忌症的安全性篩檢。
- 評估肉瘤個案報告的因果關聯性，再決定是否設計臨床試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

