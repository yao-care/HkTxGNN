---
layout: default
title: Agomelatine
parent: 高證據等級 (L1-L2)
nav_order: 26
evidence_level: L1
indication_count: 10
---

# Agomelatine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Agomelatine：從重鬱症到憂鬱型憂鬱症 (Melancholia)

## 一句話總結

Agomelatine 是一種新型褪黑激素受體促效劑 / 5-HT2C 受體拮抗劑類抗憂鬱藥，已獲歐洲藥品管理局（EMA）核准用於**重鬱症（Major Depressive Disorder）**治療，但目前在香港尚未上市。
TxGNN 模型預測它可能對**憂鬱型憂鬱症（Melancholia）**有效（預測分數 99.88%），
目前有 **20 篇文獻**支持這個方向，包含多篇 Lancet 級別的系統性回顧與網絡 Meta-Analysis，證據等級達 **L1**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 重鬱症（Major Depressive Disorder，EMA 核准） |
| 預測新適應症 | 憂鬱型憂鬱症（Melancholia） |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Agomelatine 是第一個超越傳統單胺系統的抗憂鬱藥，具備**雙重且互補的藥理機轉**：

**MT1/MT2 褪黑激素受體促效**：激動下視丘視叉上核（SCN）的褪黑激素受體，重設生理時鐘、恢復睡眠-覺醒週期。這對憂鬱型憂鬱症尤為關鍵，因 Melancholia 的核心病理特徵正是晝夜節律嚴重紊亂（早醒、晨間症狀加重、HPA 軸過度活化）。

**5-HT2C 血清素受體拮抗**：去抑制前額葉皮質的正腎上腺素與多巴胺釋放，直接改善 Melancholia 最典型的兩個症狀：**快感缺失（Anhedonia）**與**精神動作遲滯**。現有文獻（PMID 40129874）明確將 agomelatine 列為具抗 anhedonia 療效的優先藥物。

憂鬱型憂鬱症（Melancholia）在 DSM-5 及 ICD-10/11 中均為重鬱症的特殊亞型，EMA 核准 agomelatine 的 MDD 適應症在臨床上本質上已涵蓋 Melancholia 病患族群。多個 Phase 3 RCT（已整合入 Cipriani 2018 *Lancet* 網絡 Meta-Analysis）確認了其抗憂鬱療效，使本預測具有極高的臨床與機轉合理性。

---

## 臨床試驗證據

目前無針對「憂鬱型憂鬱症（Melancholia）」的獨立臨床試驗登記。Agomelatine 的抗憂鬱療效已通過多個涵蓋 Melancholia 亞型在內的大型 Phase 3 RCT 驗證，相關試驗數據已整合於下列高品質文獻（Network Meta-Analysis）中。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network Meta-Analysis | *Lancet* | 21 種抗憂鬱藥急性期療效網絡 Meta-Analysis，agomelatine 有效性與可接受性均優於安慰劑 |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review / Meta-Analysis | *Molecular Psychiatry* | MDD 維持期抗憂鬱藥隨機對照試驗 Meta-Analysis，agomelatine 顯示良好的復發預防效果 |
| [39684343](https://pubmed.ncbi.nlm.nih.gov/39684343/) | 2024 | Systematic Review / Meta-Analysis | *Int J Molecular Sciences* | Agomelatine 治療糖尿病合併重鬱症患者之療效與安全性系統性評估 |
| [37960759](https://pubmed.ncbi.nlm.nih.gov/37960759/) | 2023 | Meta-Analysis | *Medicine* | Agomelatine 治療憂鬱症有效性與安全性的系統性 Meta-Analysis |
| [41135546](https://pubmed.ncbi.nlm.nih.gov/41135546/) | 2025 | Systematic Review | *Lancet* | 抗憂鬱藥對心臟代謝及生理參數影響的大型網絡 Meta-Analysis，含 agomelatine 副作用輪廓評估 |
| [27508501](https://pubmed.ncbi.nlm.nih.gov/27508501/) | 2016 | Systematic Review | *Psychotherapy & Psychosomatics* | 新世代抗憂鬱藥安全性批判性回顧，含 agomelatine 詳細安全性分析 |
| [24328686](https://pubmed.ncbi.nlm.nih.gov/24328686/) | 2014 | Review | *Expert Opin Pharmacotherapy* | Agomelatine 作用機轉（MT1/MT2 促效 + 5-HT2C 拮抗）、療效及耐受性完整評述 |
| [32568567](https://pubmed.ncbi.nlm.nih.gov/32568567/) | 2020 | Review | *Expert Opin Drug Discovery* | Agomelatine 從臨床前研究到憂鬱症治療的完整開發歷程，強調其超越單胺系統的創新機轉 |
| [40129874](https://pubmed.ncbi.nlm.nih.gov/40129874/) | 2025 | Narrative Review | *PCN Reports* | Anhedonia 藥物與非藥物治療全面回顧，agomelatine 列為具明確抗 anhedonia 療效的優先藥物 |
| [31206585](https://pubmed.ncbi.nlm.nih.gov/31206585/) | 2019 | Cochrane Review | *Cochrane Database Syst Rev* | Agomelatine 與褪黑激素用於預防季節性情感障礙（SAD）的 Cochrane 系統性回顧 |

---

## 香港上市資訊

Agomelatine 目前在香港**尚未上市**，無任何許可證紀錄。

> 備註：Agomelatine 以 **Valdoxan®**（Servier）品牌名稱在歐洲 EMA 核准市場銷售，適應症為成人重鬱症。如需引進香港市場，須向香港衞生署藥物辦公室提出申請。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Agomelatine 的 EMA 核准適應症（重鬱症）在臨床上本質上已涵蓋憂鬱型憂鬱症（Melancholia）亞型；其雙重藥理機轉（晝夜節律正常化 + 快感缺失改善）與 Melancholia 的核心病生理高度契合，且 Lancet 級別大型網絡 Meta-Analysis 已確認其抗憂鬱療效，達 L1 證據等級。主要障礙在於香港尚未上市，以及本次 Evidence Pack 中作用機轉（MOA）與安全性資料的缺口。

**若要推進需要：**
- 取得 EMA 原廠仿單，補齊安全性資料（肝功能監測要求、禁忌症、藥物交互作用清單）
- 向香港衞生署藥物辦公室評估藥品引進許可申請的可行性
- 確認 Melancholia 亞型在香港臨床編碼與醫療系統中的對應路徑
- 若計劃開展本地研究，建議設計以 Melancholia 核心症狀（Anhedonia、HPA 軸指標、睡眠多項生理記錄）為終點的前瞻性觀察研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

