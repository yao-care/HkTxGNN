---
layout: default
title: Dienogest
parent: 中證據等級 (L3-L4)
nav_order: 202
evidence_level: L4
indication_count: 10
---

# Dienogest
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Dienogest：從子宮內膜異位症到閉經 (Amenorrhea)

## 一句話總結

Dienogest 是一種第四代合成黃體素，在多個國家被核准用於**子宮內膜異位症**的治療（代表品牌：Visanne）。TxGNN 模型預測其對**閉經 (Amenorrhea)** 可能有效，目前共檢索到 **4 個臨床試驗**及 **6 篇文獻**，惟現有證據顯示閉經為 Dienogest 的藥理機轉表現型（預期副作用），而非真正的治療新適應症，此為典型的機轉假陽性預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 子宮內膜異位症（由臨床試驗推斷；正式仿單資料缺失） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉原始資料，以下說明根據現有臨床文獻推斷。

**藥物機轉：** Dienogest 為第四代純黃體素（pure progestin），具有高選擇性黃體素受體結合能力及極低的雄激素活性。其核心作用機轉為**抑制 GnRH 脈衝分泌**，進而降低促性腺激素（LH/FSH）釋放，最終抑制卵巢雌激素合成，製造低雌激素的「假性停經」環境。2026 年的最新研究（PMID 41329046）更進一步量化了其高抑制率（inhibition ratio）與轉化指數（transformation index），證實其對子宮內膜的深度抑制能力。

**機轉關聯性：** 子宮內膜異位症（原適應症）與閉經（預測新適應症）的關聯在於：Dienogest 治療過程中，閉經是其**刻意誘導的藥理效果**——藉由停止月經來切斷異位內膜組織的荷爾蒙驅動。臨床試驗中閉經發生率常被列為觀察指標，但這是機轉效果的呈現，而非治療目標疾病。

**預測合理性的根本限制：** TxGNN 預測分數高達 99.71%，反映的是知識圖譜中「Dienogest → 誘導閉經」的強烈節點關聯，而非 Dienogest 可用來「治療疾病態閉經（如下視丘性閉經、原發性閉經）」的臨床證據。目前所有相關試驗均以**子宮內膜異位症患者**為研究對象，閉經僅為次要觀察終點或不良事件記錄，而非主要療效指標。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | 招募中 | 290 | 比較 Indinol Forto® 200mg 與 Visanne 2mg 治療子宮內膜異位症的療效與安全性（非劣效性設計）；與閉經治療無直接關聯 |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | 完成 | 968 | 真實世界臨床實踐中 Dienogest（Visanne）治療子宮內膜異位症的觀察研究；閉經為次要觀察終點，非主要療效指標 |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | 完成 | 895 | 亞洲女性子宮內膜異位症患者使用 Dienogest 的生活品質改善前瞻性觀察研究；閉經為觀察側面 |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | 招募結束進行中 | 138 | 比較 Dienogest vs Drospirenone 搭配經皮雌激素在子宮內膜異位症患者的滿意度與耐受性；聚焦荷爾蒙補充組合，與治療閉經無直接關聯 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review | BMC Pharmacology & Toxicology | 系統性回顧並以 Bayesian 分析量化 Dienogest 不良反應盛行率；閉經為高頻副作用，支持其機轉表現型的理解 |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Clinical Study | Eur J Contraception & Reprod Health Care | 2mg Dienogest 的高抑制率與轉化指數研究，進一步佐證其誘導閉經的機轉特性 |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Reviews in Endocrine & Metabolic Disorders | 子宮內膜異位症荷爾蒙治療的內分泌背景回顧，詳述雌激素依賴性、黃體素阻抗及 Dienogest 的角色 |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Prospective Cohort | Reproductive Sciences | 514 名卵巢子宮內膜異位瘤患者長期使用 Dienogest（>12 個月）的療效、安全性及復發率多中心回顧研究 |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Observational | J Pediatric & Adolescent Gynecology | 米勒管異常的 3D 模型與虛擬實境可視化研究，探討與閉經相關的婦科結構異常診斷及手術規劃 |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case Report | Medicine | 多囊性卵巢症候群合併卵巢顆粒細胞瘤案例報告；與閉經鑑別診斷相關背景文獻 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 模型雖給出 99.71% 的高預測分數，但「閉經」在此語境下是 Dienogest 本身的**藥理機轉效果**，而非其治療的目標疾病。以 Dienogest 治療疾病態閉經（如下視丘性閉經、原發性閉經）在機轉上是矛盾的——Dienogest 本身即為誘導閉經的藥物，適用於有月經的子宮內膜異位症患者，而非用於補充荷爾蒙缺乏狀態的閉經患者。此為**機轉假陽性 (mechanistic false positive)** 的典型案例，知識圖譜的拓撲相似性產生了誤導性高分。

**若要推進需要：**
- 明確界定目標閉經類型（下視丘性、垂體性、子宮性、卵巢性），評估 Dienogest 的機轉是否對特定亞型有真正的治療意義
- 補充完整的 Dienogest 作用機轉資料（DrugBank MOA 查詢）
- 取得原廠仿單安全性資料（主要警語、禁忌症、TFDA 核准適應症）
- 優先評估排名第 3 的預測適應症**纖維囊性乳房疾病 (Breast Fibrocystic Disease)**（評分：Research Question，L4），其有 1 篇先導研究（[PMID 19499407](https://pubmed.ncbi.nlm.nih.gov/19499407/)）顯示高劑量 Dienogest 可使乳腺組織顯著縮小，機轉合理性（抗雌激素效應）較閉經更具臨床意義，值得進一步探索
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

