---
layout: default
title: Lactic Acid
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Lactic Acid
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

# Lactic Acid：原適應症資料缺乏，TxGNN 預測方向指向 Atypical Coarctation of Aorta（主動脈狹窄變異型）

## 一句話總結

Lactic acid（DB04398）在本資料包中沒有記錄任何原始適應症、作用機轉或香港上市資訊，目前**未於香港取得任何藥品許可證**。TxGNN 模型針對此藥物列出 10 個候選新適應症，分數最高者為**主動脈狹窄變異型（Atypical Coarctation of Aorta，99.59%）**，但這個候選**沒有任何臨床試驗或文獻支持**；其餘 9 個候選中雖有部分檢索到試驗與文獻，但多數證據顯示乳酸/乳酸化在這些疾病中扮演的是**致病因子**而非治療角色，方向與「治療假設」相反。10 個候選的建議決策**全數為 Hold**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料包未提供（無 original_indications、無香港許可證記錄） |
| 預測新適應症（排名第一） | Atypical Coarctation of Aorta（主動脈狹窄變異型） |
| TxGNN 預測分數 | 99.59%（KG rank 7767） |
| 證據等級 | L5（純模型預測，無臨床試驗或文獻） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 候選適應症總覽（10 項排序候選）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 試驗數 | 文獻數 | 建議 |
|------|-----------|-----------|---------|--------|--------|------|
| 1 | Atypical coarctation of aorta | 99.59% | L5 | 0 | 0 | Hold |
| 2 | Aortic malformation | 99.35% | L4 | 9 | 20 | Hold |
| 3 | Non-syndromic esophageal malformation | 99.23% | L5 | 0 | 0 | Hold |
| 4 | Amenorrhea (disease) | 99.16% | L5 | 2 | 5 | Hold |
| 5 | Dry eye syndrome | 99.13% | L4 | 6 | 9 | Hold |
| 6 | Esophageal disease | 98.94% | L4 | 27 | 20 | Hold |
| 7 | DORV + AVSD + PS + heterotaxy | 98.82% | L5 | 0 | 0 | Hold |
| 8 | 淚道系統異常 | 98.77% | L5 | 0 | 0 | Hold |
| 9 | Eye disease | 98.68% | L4 | 50 | 20 | Hold |
| 10 | Cauda equina syndrome | 98.67% | L5 | 0 | 0 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（original_moa 未填）。根據資料包本身的評述，Lactic acid 是糖解代謝的天然中間產物，這次排名第一的預測（主動脈狹窄）**在生理機轉上未見已知關聯**——資料包明確標註「乳酸/乳酸鹽與主動脈狹窄之間無已知生理機轉」，屬於知識圖譜統計連結，尚無外部驗證。

更值得注意的是，在有實際文獻支持的候選（rank 2、5、6、9）中，證據呈現的方向**多與「治療」假設相反**：
- **Dry eye syndrome（rank 5）**：文獻顯示乳酸誘導的 mtDNA 累積會活化 cGAS-STING 發炎路徑，加重 Sjögren 症候群相關發炎，屬致病機轉而非治療。
- **Esophageal disease（rank 6）**：多篇文獻指出「乳酸化（lactylation）」促進食道鱗狀細胞癌進展（如 H2BC9 lactylation 活化 Wnt/β-catenin），乳酸代謝物是腫瘤驅動因子。
- **Eye disease（rank 9）**：文獻顯示乳酸上調巨噬細胞 VEGF 促進脈絡膜新生血管、乳酸化驅動近視進展、糖尿病患者玻璃體乳酸升高與視網膜病變相關。
- **Aortic malformation（rank 2）**：檢索到的試驗多為心臟手術圍術期血氧/灌注管理研究，乳酸僅作為組織灌注不良的**監測生物標記**，並非治療性介入。

整體而言，現有證據傾向支持乳酸在這些疾病中是**病理標記或致病因子**，而非具治療潛力的老藥新用候選。

## 臨床試驗證據

**Rank 1（Atypical coarctation of aorta）**：目前無相關臨床試驗登記。

**其他候選之代表性試驗**（供參考，非首選候選正式證據）：

| 試驗編號 | 候選適應症 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|-----------|------|------|------|---------|
| [NCT01134302](https://clinicaltrials.gov/study/NCT01134302) | Aortic malformation | Phase 3 | 未知 | 50 | 單心室手術術後神經功能結果研究，乳酸僅為灌注監測指標 |
| [NCT01920594](https://clinicaltrials.gov/study/NCT01920594) | Aortic malformation | Phase 2 | 完成 | 57 | HIF-PH 抑制劑試驗，與乳酸無直接關係 |
| [NCT02546687](https://clinicaltrials.gov/study/NCT02546687) | Esophageal disease | N/A | 未知 | 50 | 以靜脈血氣（含乳酸）預測食道切除術後吻合口滲漏 |
| [NCT00139282](https://clinicaltrials.gov/study/NCT00139282) | Eye disease | Phase 3 | 終止 | N/A | Squalamine lactate（非乳酸本身）用於濕性老年黃斑部病變 |

## 文獻證據

**Rank 1（Atypical coarctation of aorta）**：目前無相關文獻。

**其他候選之代表性文獻**（呈現機轉方向多與治療假設相反）：

| PMID | 候選適應症 | 年份 | 類型 | 主要發現 |
|------|-----------|-----|------|---------|
| [37786436](https://pubmed.ncbi.nlm.nih.gov/37786436/) | Dry eye syndrome | 2023 | 機轉研究 | 乳酸誘導 mtDNA 累積活化 cGAS-STING，加重 Sjögren 症候群發炎 |
| [41088127](https://pubmed.ncbi.nlm.nih.gov/41088127/) | Esophageal disease | 2025 | 機轉研究 | H2BC9 乳酸化經 Wnt/β-catenin 促進食道鱗狀細胞癌進展 |
| [30046816](https://pubmed.ncbi.nlm.nih.gov/30046816/) | Eye disease | 2018 | 機轉研究 | 乳酸上調巨噬細胞 VEGF，促進脈絡膜新生血管 |
| [38232735](https://pubmed.ncbi.nlm.nih.gov/38232735/) | Eye disease | 2024 | 機轉研究 | 鞏膜糖解增加經組蛋白乳酸化促進近視進展 |
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | Aortic malformation | 1988 | 世代研究 | 主動脈壁代謝與動脈粥狀硬化易感性之觀察性關聯 |

## 香港上市資訊

Lactic acid 目前**未於香港取得任何藥品許可證**（`total_licenses: 0`），無上市品項可列。

## 安全性考量

安全性資訊請參考原廠仿單。（key_warnings、contraindications、DDI 查詢均無資料）

## 結論與下一步

**決策：Hold**

**理由：**
- 所有 10 個候選適應症的證據等級均為 L4 或 L5，且無任一候選達到 L1-L3（缺乏隨機對照試驗支持）。
- 分數最高的候選（主動脈狹窄）完全沒有外部證據；有證據的候選（乾眼症、食道疾病、眼科疾病）文獻反而顯示乳酸/乳酸化是**致病驅動因子**，機轉方向與治療假設相反，存在潛在安全疑慮而非機會。
- 藥物本身缺乏 MOA、原適應症、香港上市與安全性資料，無法完成 S1 安全性初評（DG001 為 Blocking 等級缺口）。

**若要推進需要：**
- 補齊 TFDA／香港仿單警語與禁忌症資料（DG001，Blocking）。
- 透過 DrugBank API 或原廠資料補齊作用機轉（DG002，High）。
- 針對排名第一候選，須先取得任何形式的機轉或臨床證據，否則建議直接排除，改聚焦於證據等級較高但方向仍待釐清的候選（如 rank 2 aortic malformation），並進一步查證乳酸在該情境下是否為監測指標而非治療標的。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

