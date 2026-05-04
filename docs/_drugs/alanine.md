---
layout: default
title: Alanine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 1
---

# Alanine
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

# Alanine：從胺基酸代謝到胃輕癱

## 一句話總結

Alanine 是一種非必需胺基酸，目前無任何核准的臨床適應症。
TxGNN 模型預測它可能對**胃輕癱 (Gastroparesis)** 有效，預測分數高達 **99.37%**；
然而，目前所有臨床試驗與文獻均與 Alanine 無直接關聯，**實質臨床證據尚付之闕如**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准臨床適應症 |
| 預測新適應症 | 胃輕癱 (Gastroparesis) |
| TxGNN 預測分數 | 99.37% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Alanine 是人體非必需胺基酸之一，參與**葡萄糖－丙胺酸循環（glucose-alanine cycle）**與糖質新生（gluconeogenesis），理論上可支援腸道黏膜的完整性與能量代謝。

然而，目前**尚無已知的直接生物機轉**可解釋 Alanine 對胃排空延遲（gastroparesis 的核心病理）具有改善效果。TxGNN 模型高分（0.994）最可能的解釋是：知識圖譜中存在「Alanine ↔ 胺基酸代謝 ↔ 糖尿病併發症 ↔ 胃輕癱」的**間接拓撲距離**，而非具體的生物機轉證據。

此外，Alanine 目前**在香港未上市、無核准適應症、藥物交互作用記錄為零**，顯示整體臨床轉化基礎相當薄弱，需審慎評估。

---

## 臨床試驗證據

> ⚠️ 以下 9 項臨床試驗**均與 Alanine 無直接關聯**（相關性等級均為 C 級），收錄目的僅作為胃輕癱治療領域的背景參考。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06452966](https://clinicaltrials.gov/study/NCT06452966) | N/A | 招募中 | 350 | 傳統中醫介入對 ICU 重症器官衰竭患者的療效研究，與 Alanine 無直接關聯 |
| [NCT02793154](https://clinicaltrials.gov/study/NCT02793154) | Phase 4 | 已終止 | 4 | 比較 Albiglutide 與 Exenatide 對胃電活動及胃排空的影響（T2DM），提前終止、樣本極小 |
| [NCT01149369](https://clinicaltrials.gov/study/NCT01149369) | Phase 2 | 已完成 | 126 | Aprepitant（NK1 受體拮抗劑）用於慢性噁心/胃輕癱的多中心 RCT，確認胃輕癱為活躍研究領域 |
| [NCT01934192](https://clinicaltrials.gov/study/NCT01934192) | Phase 2 | 已終止 | 91 | GSK962040 促進 ICU 重症患者腸道營養輸送的研究（NUTRIATE），提前終止 |
| [NCT03587142](https://clinicaltrials.gov/study/NCT03587142) | Phase 2 | 已完成 | 96 | Buspirone（5-HT1A 促動劑）用於胃輕癱早飽症狀的多中心 RCT（BESST 研究） |
| [NCT01602549](https://clinicaltrials.gov/study/NCT01602549) | Phase 2 | 已完成 | 58 | 促胃動力藥劑量探索研究，評估帕金森氏症伴胃排空遲緩患者的 L-DOPA 藥動學 |
| [NCT07270939](https://clinicaltrials.gov/study/NCT07270939) | N/A | 尚未招募 | 150 | 比較 18/20/24 小時腸道營養模式對 ICU 患者的影響，研究主體為餵食時程而非胺基酸 |
| [NCT03941288](https://clinicaltrials.gov/study/NCT03941288) | Phase 2 | 已完成 | 92 | Cannabidiol（CBD）用於胃輕癱與功能性消化不良的藥效動力學研究 |
| [NCT01262898](https://clinicaltrials.gov/study/NCT01262898) | Phase 2 | 已完成 | 79 | GSK962040 口服 Motilin 受體促效劑用於糖尿病性胃輕癱的安全性與效果評估 |

---

## 文獻證據

> ⚠️ 以下 3 篇文獻**均與 Alanine 對胃輕癱的直接療效無關**（均為 Tier 3 間接文獻），僅供背景參考。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Review | Advances in Renal Replacement Therapy | 回顧末期腎病與腎移植患者的腸胃道及肝臟疾病，提及慢性腎衰竭患者胃輕癱盛行率較高 |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | 觀察性研究 | Diabetic Medicine | 探討糖尿病性肝硬化與其他微血管併發症的關聯，間接涉及糖尿病併發症背景 |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | 個案報告 | Cureus | 1 型糖尿病患者的糖原肝病個案，病史包含胃輕癱與糖尿病酮酸中毒，與 Alanine 無直接關聯 |

---

## 香港上市資訊

Alanine（DB00160）目前**在香港未取得任何上市許可**，無相關藥品許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 備註：本藥品目前香港未上市，TFDA 仿單警語、禁忌症及藥物交互作用資料均尚待補充（數據缺口 DG001、DG002）。

---

## 結論與下一步

**決策：Hold**

**理由：**
Alanine 為非必需胺基酸，目前無任何核准適應症，亦無直接支持其用於胃輕癱的臨床或機轉證據。TxGNN 高預測分數反映的是知識圖譜中代謝通路的間接關聯，而非真實的生物療效依據；所有相關臨床試驗與文獻均針對其他藥物，證據等級僅達 L5。

**若要推進需要：**
- 補充 Alanine 的詳細作用機轉（MOA）資料，確認是否存在影響胃排空的生物學途徑
- 取得 TFDA/原廠仿單，評估警語、禁忌症與安全性基準
- 進行 **前臨床研究**，以動物模型驗證 Alanine 對胃動力的影響（如有則可升至 L4）
- 確認適合的給藥途徑與劑量（目前給藥資訊完全缺乏）
- 若前臨床結果陽性，再評估是否啟動 Proof-of-Concept 臨床試驗設計
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

