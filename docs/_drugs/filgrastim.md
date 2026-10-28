---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
monitor_inn: "FILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
last_modified_at: 2026-10-23
description: "Filgrastim：預測新適應症為原發性血小板釋放障礙（證據等級 L5）。原適應症：知識圖譜記錄的關聯：體質性嗜中性白血球低下症、嚴重先天性嗜中性白血球低下症、週期性造血、慢性家族性嗜中性白血球低下症"
---

# Filgrastim
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

## Filgrastim：從先天性嗜中性白血球低下症到原發性血小板釋放障礙
{: .text-alpha }

## 一句話總結

Filgrastim（重組人類 G-CSF）在知識圖譜中記錄的相關疾病為體質性嗜中性白血球低下症、嚴重先天性嗜中性白血球低下症等。
TxGNN 模型預測它可能對**原發性血小板釋放障礙 (primary release disorder of platelets)** 有效，但目前**沒有直接研究**該疾病的臨床試驗或文獻，預測僅來自模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：體質性嗜中性白血球低下症、嚴重先天性嗜中性白血球低下症、週期性造血、慢性家族性嗜中性白血球低下症（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 原發性血小板釋放障礙 |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Filgrastim 是 G-CSF 類藥物，一般透過 G-CSF 受體訊號作用於顆粒球系列，促進嗜中性白血球的生成與成熟。

血小板釋放障礙屬於血小板功能缺陷（分泌功能異常），與嗜中性白血球數量不足是不同的病理機制。G-CSF 並無已知的作用可矯正血小板分泌缺陷。因此，目前無法建立合理的機轉連結，高分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而非生物學證據，應視為待驗證的假說。

同批預測的其他疾病（如假性血管性血友病、Glanzmann 血小板無力症、Scott 症候群、遺傳性血管性水腫等）同樣缺乏機轉與證據支持。

## 臨床試驗證據

針對「原發性血小板釋放障礙」本身，目前無相關臨床試驗登記。

下表為排名第 10 的相近預測「血小板型出血性疾病」所連結的試驗。這些皆為造血幹細胞移植研究，filgrastim 僅作為動員或植入的輔助用藥，並非受試的治療對象，與本預測疾病無直接關聯。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | 已撤回 | 0 | Busulfan 加 fludarabine 作為非親緣配對移植前處置；未收案，無數據 |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | 完成 | 未提供 | T 細胞去除之部分配對親緣移植，重點在移植技術 |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | 不適用 | 未知 | 35 | 非清髓性異體幹細胞移植，用於血液惡性腫瘤與再生不良性貧血 |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | 完成 | 未提供 | CD34 富集周邊血幹細胞輔助異體移植 |
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | 不適用 | 完成 | 25 | 低劑量異體周邊血幹細胞移植，用於高風險低惡性度血液腫瘤 |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | 完成 | 55 | 多臍帶血單位移植，用於血液疾病或嚴重再生不良性貧血 |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | 完成 | 20 | T 細胞去除之減量強度單倍體移植 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 8 張有效的單一成分許可證（均為 filgrastim 製劑），資料中未載明核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45427 | NEUPOGEN PRE-FILLED SYRINGE 0.3MG/0.5ML | 預充填注射筒 | 請參考原廠仿單 |
| HK-60951 | NIVESTIM 300MCG/0.5ML 預充填注射筒 | 預充填注射筒 | 請參考原廠仿單 |
| HK-64300 | ZARZIO 48MU/0.5ML 預充填注射筒 | 預充填注射筒 | 請參考原廠仿單 |
| HK-35878 | NEUPOGEN INJ 0.3MG/ML | 注射劑 | 請參考原廠仿單 |
| HK-68517 | ACCOFIL 30MU/0.5ML 預充填注射筒 | 預充填注射筒 | 請參考原廠仿單 |

（另有 3 張：HK-60949、HK-62169、HK-45426，同為有效的單一成分許可證。）

## 安全性考量

- **藥物交互作用**：資料庫查詢到 100 筆交互作用，已列出的多為中度。主要包括：
  - 放射性藥物與放射免疫治療：Iobenguane (I-131)、Fludeoxyglucose (18F)、Ibritumomab tiuxetan、Tositumomab
  - 細胞毒性化療或骨髓抑制藥物：Paclitaxel、Mercaptopurine、Trimetrexate、Azacitidine、Bendamustine、Arsenic trioxide、Altretamine
  - 其他：Levamisole、Abemaciclib、Acalabrutinib、Aldesleukin、Alemtuzumab、Avapritinib、Belantamab mafodotin、Asparaginase

其他警語與禁忌症資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測疾病沒有任何直接研究，G-CSF 作用於顆粒球系列，與血小板功能缺陷之間找不到合理的機轉連結，證據等級僅為 L5。
- 相近疾病所連結的試驗均為移植研究，filgrastim 只是輔助用藥，不能作為療效證據。

**若要推進需要：**
- 取得 filgrastim 的作用機轉資料，並釐清是否存在任何血小板相關的生物學連結
- 針對血小板釋放障礙進行系統性文獻檢索，確認是否有病例報告或前臨床研究
- 取得香港原廠仿單，確認核准適應症與安全性資訊
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

