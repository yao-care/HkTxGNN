---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Glycine：從胺基酸補充劑到鼻腔疾病

## 一句話總結

Glycine（甘胺酸）是人體含量最豐富的非必需胺基酸之一，廣泛用於營養補充與藥用賦形劑，目前在台灣無正式核准藥物適應症。TxGNN 模型預測它可能對**鼻腔疾病（Nasal Cavity Disease）**與**急性喉咽炎（Acute Laryngopharyngitis）**有效，但目前可查到的臨床試驗與文獻均與 Glycine 直接治療應用無關，整體證據等級為 **L5**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式核准藥物適應症（胺基酸補充劑） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Glycine 是人體最小的胺基酸，同時具有抑制性神經傳導物質的功能，可與甘胺酸受體（GlyR）結合。動物模型研究顯示，Glycine 可透過 GlyR 介導的 Cl⁻ 內流抑制中性球活化，進而減少 IL-6、TNF-α 等促炎細胞因子釋放，因此在理論上具有抗炎潛力。

對於**鼻腔疾病**，鼻腔黏膜上皮雖有 GlyR 的理論表現位點，Glycine 的抗炎特性理論上可緩解鼻腔黏膜炎症，但目前無任何直接臨床前或臨床數據支持此路徑。TxGNN 的高分可能反映知識圖譜中「鼻腔黏膜 → 炎症 → 胺基酸代謝」的間接節點關聯，而非直接藥效路徑。

對於**急性喉咽炎**，其核心病理為中性球浸潤與促炎細胞因子（IL-1β、IL-6、TNF-α）驅動，機轉鏈「Glycine 補充 → GlyR 活化 → 抑制 NF-κB → 減少喉咽炎症」在理論上成立，但咽喉部 GlyR 表現量的臨床數據缺乏，且口服補充 Glycine 能否在局部達到有效治療濃度亦未經驗證，全段均無直接實驗證據支撐。

---

## 臨床試驗證據

### 鼻腔疾病 (Nasal Cavity Disease)

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | 完成 | 25 | 18F-FPPRGD2 PET 顯影劑研究，評估 αvβ3 整合素表現作為腫瘤血管新生生物標記。Gly 僅為 RGD 三肽的結構成分，非 Glycine 治療應用，**與本適應症無直接相關**。 |

### 急性喉咽炎 (Acute Laryngopharyngitis)

目前無相關臨床試驗登記。

---

## 文獻證據

### 鼻腔疾病 (Nasal Cavity Disease)

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | 動物基礎研究 | Veterinary Pathology | 組織化學檢測正常及牛皰疹病毒感染牛隻鼻黏膜的醣複合物組成，屬細菌定殖機制研究，與 Glycine 治療應用無直接關聯。 |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | 體外藥物遞送研究 | Chemical & Pharmaceutical Bulletin | 研究 Oligoarginine-linked 聚合物作為鼻腔黏膜疫苗佐劑，Glycine 非主角成分，不支持 Glycine 對鼻腔疾病的直接療效。 |

### 急性喉咽炎 (Acute Laryngopharyngitis)

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21617577](https://pubmed.ncbi.nlm.nih.gov/21617577/) | 2011 | 臨床世代研究 | Shock | Sivelestat（中性球彈性酶抑制劑）用於胃液吸入性急性肺損傷，研究對象與給藥機轉均與 Glycine 用於急性喉咽炎無直接相關。 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Glycine 用於鼻腔疾病及急性喉咽炎，目前僅有 TxGNN 模型預測（L5 等級），所有查詢到的臨床試驗與文獻均非 Glycine 直接治療上述疾病的研究，缺乏任何可支撐再利用假說的實驗數據，暫無推進基礎。

**若要推進需要：**
- 補充 Glycine 正式作用機轉資料（MOA），確認 GlyR 在鼻腔及咽喉黏膜的實際分佈與表現量
- 進行鼻腔／咽喉黏膜炎症動物模型的直接藥效學實驗（臨床前 Proof-of-Concept）
- 驗證口服或局部給藥途徑下，Glycine 能否在鼻腔／咽喉部位達到有效治療濃度
- 取得台灣仿單安全性資料（警語、禁忌症），完成 S1 安全性初評所需資料缺口（DG001）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

