---
layout: default
title: Cabazitaxel
parent: 高證據等級 (L1-L2)
nav_order: 119
evidence_level: L2
indication_count: 10
---

# Cabazitaxel
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Cabazitaxel：從前列腺癌到女性乳癌

## 一句話總結

Cabazitaxel（紫杉烷類第三代衍生物）原本經 FDA 核准用於多西他賽治療後進展的轉移性去勢抵抗性前列腺癌（mCRPC）。TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，機轉上源於其突破 P-糖蛋白（P-gp）介導多重耐藥性的獨特能力。目前有 **0 個登記臨床試驗**（本次查詢結果）及 **20 篇文獻**支持這個方向，其中包含 Phase 2 RCT 與 Phase 1/II 臨床研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性去勢抵抗性前列腺癌 mCRPC（FDA 核准；香港未上市） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（香港仿單及 DrugBank MOA 均有資料缺口）。根據已知資訊，Cabazitaxel 屬於**紫杉烷類（Taxane）**細胞毒性藥物，其核心機制為**穩定微管、抑制微管去聚合**，使細胞周期停滯於 G2/M 期，導致癌細胞凋亡。相較於第一代（Paclitaxel）及第二代（Docetaxel）紫杉烷，Cabazitaxel 對 P-糖蛋白（P-gp/MDR1）的親和力極低，可有效突破多重耐藥機制。

乳癌是紫杉烷類最重要的適應症群之一。Paclitaxel 和 Docetaxel 已是乳癌標準化療的核心成分，而相當比例的晚期乳癌患者在接受這些藥物後會發展出耐藥性。Cabazitaxel 的低 P-gp 親和力正好針對此耐藥機制提供理論上的克服途徑。PMID 25416788 直接以 MCF-7 乳癌細胞株建立 Cabazitaxel 耐藥模型，證實其交叉耐藥程度顯著低於 Paclitaxel 和 Docetaxel（15 倍 vs. 200 倍）。

更直接的支持來自 PMID 28567478，該研究證實在 **βIII-tubulin 高度表現**的乳癌模型中，Cabazitaxel 療效優於 Docetaxel，而 βIII-tubulin 高表現正是腫瘤侵襲性及紫杉烷耐藥的重要標誌物。這進一步強化了 TxGNN 預測的生物合理性。

---

## 臨床試驗證據

目前無相關臨床試驗登記（本次資料庫查詢結果為 0）。

> **附註**：部分已登記的 Cabazitaxel 乳癌相關臨床試驗（如 NCT01934894）可在 ClinicalTrials.gov 查詢，建議進行補充查詢以確認完整清單。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase 2 RCT | European Journal of Cancer | GENEVIEVE 研究：Cabazitaxel vs. 週劑量 Paclitaxel 作為可手術 HER2 陰性乳癌新輔助治療，比較 pCR 率 |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase 1/II | European Journal of Cancer | Cabazitaxel + Capecitabine 用於紫杉烷/蒽環素治療後進展的轉移性乳癌，評估 MTD、安全性及藥動學 |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II | Clinical Breast Cancer | Cabazitaxel + Lapatinib 治療合併顱內轉移的 HER2+ 轉移性乳癌（NCT01934894），探索劑量及顱內活性 |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | 機轉研究 | Molecular Cancer Therapeutics | 以 MCF-7 乳癌細胞株建立 Cabazitaxel 耐藥模型；交叉耐藥程度顯著低於 Paclitaxel/Docetaxel |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | 前臨床 | Journal for Immunotherapy of Cancer | Cabazitaxel 調節腫瘤相關巨噬細胞功能，協同增強 CD47 靶向免疫療法對三陰性乳癌的療效 |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | 前臨床 | Journal of Controlled Release | Cabazitaxel 奈米粒子在基底型患者來源乳癌異種移植模型中達 6/8 完全緩解，優於游離藥物 |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | 前臨床 | International Journal of Nanomedicine | PACA 奈米粒子載 Cabazitaxel 在三陰性乳癌 PDX 模型中療效顯著，並調節腫瘤微環境 M2 巨噬細胞 |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | 前臨床/機轉 | Cancer Chemotherapy and Pharmacology | βIII-tubulin 高表現乳癌中，Cabazitaxel 結合力及抗腫瘤療效優於 Docetaxel |
| [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/) | 2016 | 回顧/專利分析 | Expert Opinion on Therapeutic Patents | 紫杉烷類抗癌藥物專利回顧，涵蓋 Cabazitaxel 在乳癌、前列腺癌等多種癌症的開發脈絡 |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | 回顧/藥動學 | British Journal of Clinical Pharmacology | 紫杉烷類（含 Cabazitaxel）治療藥物監測（TDM）與個人化劑量調整的全面回顧 |

---

## 香港上市資訊

Cabazitaxel 目前**在香港尚未取得上市許可**，無任何登記藥品。

---

## 細胞毒性

Cabazitaxel 為紫杉烷類抗腫瘤藥物（細胞毒性化療藥），適用本章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Taxane 類，第三代半合成紫杉烷衍生物） |
| 骨髓抑制風險 | **高度**（嗜中性白血球減少為最常見嚴重不良反應，TROPIC 研究中 Grade 3/4 發生率 >80%） |
| 致吐性分級 | 低至中度（依 ASCO/MASCC 分級標準） |
| 監測項目 | CBC（含分類計數，每週期前必查）、肝功能（ALT/AST/bilirubin）、腎功能（Cr）、電解質、周邊神經病變評估 |
| 處置防護 | 需依細胞毒性藥物處置規範（Cytotoxic Handling Guidelines）操作；靜脈注射給藥，需防範藥物外滲 |

---

## 安全性考量

安全性資訊請參考原廠仿單（香港未上市，建議參照 EMA/FDA 核准仿單）。

> **注意**：根據已知毒性特性，Cabazitaxel 的嚴重骨髓抑制（尤其嗜中性白血球低下性發燒）及腸胃道毒性（腹瀉、噁心）在臨床應用上需要特別監測，建議閱讀原廠完整處方資訊。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Cabazitaxel 對多重耐藥性乳癌的療效具有明確的生物合理性（P-gp 低親和力、βIII-tubulin 優勢），且已有 Phase 2 RCT（GENEVIEVE）及多項 Phase 1/II 臨床研究直接探索乳癌適應症，文獻基礎達 L2 等級，支持進一步評估。然而香港目前無此藥上市，需考量取得藥物的途徑及臨床試驗框架。

**若要推進需要：**
- 補全香港仿單安全性資料（建議參照 FDA/EMA 核准仿單的警語、禁忌及 DDI 資訊）
- 補全 Cabazitaxel 作用機轉（MOA）的詳細資料（DrugBank API 查詢）
- 對 ClinicalTrials.gov 進行更廣泛查詢（搜尋詞：`cabazitaxel AND breast cancer`），補充目前缺失的臨床試驗登記資料
- 評估香港未上市藥物的臨床試驗申請途徑（藥物及毒藥監管局）
- 確認目標族群（建議聚焦：紫杉烷耐藥後的轉移性乳癌，尤其 TNBC 或 HER2+ 合併 CNS 轉移）
- 制定嗜中性白血球低下性發燒的預防及管理計畫（G-CSF 預防性使用方案）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

