---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Niraparib：預測新適應症為囊性腫瘤 (Cystic Neoplasm)（證據等級 L5）。原適應症：卵巢上皮惡性腫瘤、原發性腹膜癌"
monitor_inn: "Niraparib"
predicted_indications: ["epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of hypopharynx", "benign neoplasm of tongue", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "tumor of testis and paratestis", "inner ear neoplasm", "pre-malignant neoplasm", "schwannoma of jugular foramen"]
---

# Niraparib
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

## Niraparib：從卵巢癌／腹膜癌到囊性腫瘤（Cystic Neoplasm）
{: .text-alpha }

## 一句話總結

Niraparib 是一種 PARP 抑制劑，原本用於卵巢上皮惡性腫瘤與原發性腹膜癌等婦科腫瘤。
TxGNN 模型預測它可能對**囊性腫瘤 (Cystic Neoplasm)** 有效，目前有 **3 個臨床試驗**（均未完成）和 **10 篇文獻**與此方向相關，但實際證據多集中於漿液性子宮內膜癌與卵巢漿液性癌，與原適應症高度相近。

> 說明：預測排名第 1 的是「會厭腫瘤 (epiglottis neoplasm)」，但該項僅有模型預測、完全沒有試驗或文獻。本報告以證據最充分的第 2 名「囊性腫瘤」為主要評估對象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢上皮惡性腫瘤、原發性腹膜癌（核准適應症文字缺漏，依知識圖譜資料） |
| 預測新適應症 | 囊性腫瘤 (Cystic Neoplasm) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（嚴格依規則，無已完成之 RCT；實際上有 Phase 2 試驗進行中，系統評為 L2，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold（可列為研究性問題，持續追蹤） |

**證據等級說明：** 資料中的系統評級為 L2，但依本報告判定規則，L2 需有「已完成」的 Phase 2/3 RCT。目前相關試驗為進行中（NCT04716686）、已提前終止（NCT04159155）或撤案（NCT05289648），無一完成，故保守判定為 L3 以下；僅有已發表的世代研究與前臨床研究，實際接近 **L3–L4**。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Niraparib 是 PARP 抑制劑，透過同源重組缺陷（HRD）造成的合成致死機制殺傷腫瘤細胞，在卵巢癌與腹膜癌的療效已被證實。

「囊性腫瘤」是範圍很廣的本體論標籤，從現有證據看，它實際對應的是漿液性／囊性婦科腫瘤（如漿液性子宮內膜癌、高惡性度漿液性卵巢癌）。這類腫瘤常有 HRD 與染色體不穩定性，分子特徵與卵巢漿液性癌相似，機轉上確實可能適用 PARP 抑制劑。

但也需注意：此預測與 Niraparib 已核准的卵巢／腹膜適應症高度重疊，新穎性有限，且「囊性腫瘤」未必代表一個獨立疾病。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Phase 2 | 招募中 | 83 | Niraparib 單藥用於漿液性子宮內膜癌的維持與復發治療；尚無結果 |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Phase 2/3 | 提前終止 | 11 | 加拿大多臂多階段隨機試驗，評估漿液性或 p53 突變子宮內膜癌的前線與維持治療；僅收 11 人，無可用療效資料 |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Early Phase 1 | 撤案 | 0 | 高惡性度子宮內膜癌術前使用 Niraparib 的探索性試驗；未收案，無資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | 臨床試驗方案 | BMJ Open | Niraparib 維持治療用於 III/IV 期或復發漿液性子宮癌的 Phase 2 試驗設計 |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | 世代研究 | Pathol Oncol Res | F1CDx 基因體檢測評估 HRD，用以指引高惡性度漿液性卵巢癌的 PARP 抑制劑治療 |
| [42157333](https://pubmed.ncbi.nlm.nih.gov/42157333/) | 2026 | 世代研究 | Clin Epigenetics | 以 HRR 基因啟動子甲基化建立預測 PARP 抑制劑療效與無惡化存活的列線圖 |
| [42442041](https://pubmed.ncbi.nlm.nih.gov/42442041/) | 2026 | 世代研究 | Gynecol Oncol | 評估 BRCA 野生型高惡性度漿液性癌中 HRD 檢測的實務價值，並探討 MYC 擴增作為替代標記 |
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | 病例報告 | BMJ Case Rep | Niraparib 維持治療用於卵巢癌合併腦轉移的病例 |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | 前臨床 | Cancer Biol Ther | 以高惡性度漿液性癌球體與類器官評估 Carboplatin 合併 PARP 抑制劑的效果 |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | 前臨床 | Cancer Res | RAD51C 啟動子甲基化喪失導致高惡性度漿液性卵巢癌對 PARP 抑制劑產生抗藥性 |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | 前臨床 | Int J Mol Sci | 以蛋白質體學分析 PARP 抑制劑在高惡性度漿液性卵巢癌細胞中的多重藥理作用 |

（另有 2 篇前臨床研究：PMID 40702505、41214101，主題為卵巢癌幹細胞亞型與 Claudin-4，與 Niraparib 直接關聯較弱，未列入表中。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65945 | ZEJULA CAPSULES 100MG（ZAI LAB） | 未提供 | 未提供 |
| HK-67238 | ZEJULA CAPSULES 100MG（ZAI LAB） | 未提供 | 未提供 |
| HK-68295 | AKEEGA TABLETS 50MG/500MG（Johnson & Johnson） | 未提供 | 未提供 |
| HK-68296 | AKEEGA TABLETS 100MG/500MG（Johnson & Johnson） | 未提供 | 未提供 |

---

## 細胞毒性

Niraparib 屬於抗腫瘤藥物（PARP 抑制劑，標靶藥物類）。本報告所編整的資料缺乏細胞毒性相關細節，請參考原廠仿單的警語與注意事項。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單（資料中提及有骨髓抑制與高血壓風險） |
| 監測項目 | 至少應包含血液學參數（CBC）與血壓，詳細請參考仿單 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分代表：
  - **嚴重 (Major)**：Deferiprone、Samarium (153Sm) lexidronam
  - **中度 (Moderate)**：Acetylsalicylic acid（阿斯匹靈）、Apixaban、Dipyridamole、Cilostazol、Abciximab、Alteplase、Bivalirudin 等抗凝血／抗血小板藥物；以及 I-131 Iobenguane、Ibritumomab tiuxetan、Strontium chloride Sr-89 等放射性藥物
  - 整體而言，與抗凝血／抗血小板藥物及放射性藥物併用時需特別留意出血與骨髓抑制風險。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數極高，但支持證據僅限於進行中、終止或撤案的子宮內膜漿液性癌試驗，沒有任何已完成的 RCT；且「囊性腫瘤」本身是寬泛標籤，與原適應症高度重疊，新穎性有限。
- 其餘 9 個預測（如會厭腫瘤、各種良性腫瘤、內耳腫瘤等）完全沒有臨床或文獻證據，其中良性腫瘤因 Niraparib 的毒性（骨髓抑制、高血壓）風險效益比不佳，不建議推進。

**若要推進需要：**
- 釐清「囊性腫瘤」實際對應的具體疾病（如漿液性子宮內膜癌），改以明確疾病名稱重新評估
- 追蹤 NCT04716686 的試驗結果
- 補充作用機轉（MOA）資料
- 取得香港衛生署核准仿單，確認適應症、警語與禁忌症
- 若考慮漿液性子宮內膜癌，需建立 HRD 生物標記篩選與血液學／血壓監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

