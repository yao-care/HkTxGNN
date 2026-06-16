---
layout: default
title: Glucagon
parent: 中證據等級 (L3-L4)
nav_order: 351
evidence_level: L4
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Glucagon：從低血糖急救到腸躁症

## 一句話總結

Glucagon 是一種由胰臟 alpha 細胞分泌的多肽激素，原本主要用於低血糖急救及胃腸道造影程序的腸蠕動抑制。TxGNN 模型預測它可能對**腸躁症 (Irritable Bowel Syndrome)** 有效，目前有 **11 個間接相關臨床試驗**與 **20 篇文獻**支持此方向，但現有證據幾乎全來自同源的 GLP-1 受體促效劑，而非 glucagon 本身。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 低血糖急救、GI 造影程序腸蠕動抑制 |
| 預測新適應症 | 腸躁症 (Irritable Bowel Syndrome) |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Glucagon 由 proglucagon 基因（GCG）編碼，與 GLP-1（Glucagon-like Peptide-1）共同源自同一前驅蛋白，兩者均為 proglucagon 轉譯後加工的產物。Glucagon 本身在歷史上曾作為胃腸道內視鏡及影像學程序的抗痙攣劑，透過鬆弛胃腸平滑肌來暫時抑制蠕動；此特性在理論上與腹瀉型腸躁症（IBS-D）的過度蠕動症狀管理具有潛在相關性。

TxGNN 模型的高預測分數（0.9924）主要反映 proglucagon 家族整體與腸道功能調節的廣泛連結，而非 glucagon 本身的特異臨床證據。現有臨床研究幾乎全部聚焦於 GLP-1 受體促效劑（ROSE-010、liraglutide、exendin-4），這些藥物已在 IBS 試驗中展示對腹痛與腸蠕動的調節效果，為 proglucagon 家族介入 IBS 提供了間接機轉支持。

然而，glucagon 與 GLP-1 的作用受體不同（glucagon receptor vs GLP-1 receptor），兩者的胃腸道效應不能直接類比。目前無任何直接以 glucagon 為介入藥物的 IBS Phase 2/3 RCT，現有機轉連結屬於推論性質，需獨立臨床研究加以驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | 完成 | 52 | ROSE-010（GLP-1 受體促效劑）在 IBS-C 女性患者中可延緩胃排空並改善腹痛，為 proglucagon 家族調節 IBS 蠕動的最具相關性試驗 |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | 完成 | 12 | 比較原生 GLP-1 與 ROSE-010 對人體餐後上消化道蠕動的抑制效果，補充 proglucagon 家族 GI 運動調節的橋接機轉依據 |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | 終止 | 8 | Liraglutide 用於迴腸-肛門吻合術後高頻排便，因招募困難提前終止，結果受限 |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | 不適用 | 完成 | 66 | 運動訓練對 IBS 合併前期糖尿病肥胖患者之腸道菌叢與 GLP 激素的影響，顯示 GLP 系統在 IBS 中具生物活性角色 |

> ⚠️ 目前無直接以 glucagon 為介入藥物的 IBS 臨床試驗登記。以上試驗均為 GLP-1 相關藥物之間接參考。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review + Meta-analysis | Frontiers in Endocrinology | GLP-1 受體促效劑可有效改善 IBS 症狀，為 proglucagon 家族用於 IBS 提供最高層級間接證據 |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Phase 2 次群分析 | Scandinavian J Gastroenterology | ROSE-010 對 IBS 腹痛有顯著緩解，交叉分析確認最適治療族群（IBS-C 與 IBS-M） |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Mechanistic Review | Experimental Physiology | 腸道 L 細胞分泌 GLP-1 在 IBS 病生理中的角色，奠定 proglucagon 家族介入的機轉基礎 |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | 真實世界世代研究 | Annals of Gastroenterology | 真實世界 IBS 患者使用 GLP-1 RA 的處方模式與停藥原因分析，揭示實際臨床應用限制 |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | J Headache and Pain | GLP-1 受體促效劑在疼痛調節的系統性回顧，支持 GLP-1 系統具廣泛神經鎮痛潛力 |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | 前臨床研究 | Neurogastroenterol Motility | Exendin-4 在 Wistar Kyoto IBS 大鼠模型中改善 GI 功能障礙，提供 GLP-1R 促效的動物模型證據 |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | 橫斷面研究 | Clin Res Hepatol Gastroenterol | IBS-C 患者血清 GLP-1 水平降低，與腹痛程度呈負相關，支持 GLP-1 系統缺失假說 |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | 臨床試驗 | Frontiers in Nutrition | 低 FODMAP 飲食後 IBS 患者循環 GLP-1 濃度上升，顯示 GLP-1 在 IBS 症狀改善中的生物標誌角色 |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | 探索性研究 | Adv Exp Med Biol | 氣霧化 GLP-1 給藥途徑用於糖尿病及 IBS 治療的概念探索 |
| [41480755](https://pubmed.ncbi.nlm.nih.gov/41480755/) | 2026 | Review | J Clin Investigation | GLP-1 受體促效劑作為 incretin 療法的腸-腦互動機轉最新綜述，強調 GLP-1 系統在功能性腸道疾病的治療潛力 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.24%），但現有臨床與文獻證據幾乎全來自 GLP-1 受體促效劑（ROSE-010、exendin-4 等）而非 glucagon 本身；加上 glucagon 在香港未有上市許可，且作用受體與 GLP-1 不同，現有間接證據尚不足以支持直接進入臨床試驗階段。

**若要推進需要：**
- 建立 glucagon 直接用於 IBS 的機轉研究，釐清 glucagon receptor 與 GLP-1 receptor 在 GI 平滑肌的效應差異
- 取得 glucagon 完整 MOA 資料及安全性仿單（目前為 Data Gap，影響安全性初評）
- 評估給藥途徑可行性（glucagon 目前主要為注射劑型，慢性 IBS 治療需口服或其他非侵入性給藥方式）
- 若機轉研究支持，設計針對 IBS-D 的小規模 Phase 2 探索性試驗，直接評估 glucagon 的療效與安全性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

