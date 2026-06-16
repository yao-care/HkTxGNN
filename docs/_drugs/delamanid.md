---
layout: default
title: Delamanid
parent: 中證據等級 (L3-L4)
nav_order: 215
evidence_level: L4
indication_count: 10
---

# Delamanid
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

# Delamanid：從 MDR 結核病到牛型結核病

## 一句話總結

Delamanid 是一種新型抗分枝桿菌藥物，在日本、歐盟等地已核准用於多重抗藥性肺結核（MDR-TB）的治療，但目前尚未在香港上市。
TxGNN 模型預測它可能對**牛型結核病 (Tuberculosis, Bovine)** 有效，
目前有 **0 個臨床試驗**和 **1 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 多重抗藥性肺結核 (MDR-TB)（參考全球核准適應症；香港無收載） |
| 預測新適應症 | 牛型結核病 (Tuberculosis, Bovine) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉原始資料，但根據文獻與預測理據可知：Delamanid 屬二氫-硝基咪唑噁唑類（dihydro-nitroimidazooxazole）抗菌藥，其作用靶點為去氮黃素依賴性硝基還原酶（Ddn，deazaflavin-dependent nitroreductase），透過抑制分枝菌酸（mycolic acid）的生合成來破壞分枝桿菌細胞壁完整性，從而發揮殺菌效果。

牛型結核桿菌（*Mycobacterium bovis*）與人型結核桿菌（*Mycobacterium tuberculosis*）同屬 MTBC（*Mycobacterium tuberculosis* complex），兩者共享高度相似的分枝菌酸細胞壁結構。Delamanid 作用靶點 Ddn 在 *M. bovis* 基因組中亦存在同源序列，機轉上理論可行，這是 TxGNN 圖譜模型給出高分（99.91%）的分子基礎。

然而，牛型結核病在臨床上主要為人畜共患的獸醫公衛議題，感染途徑（主要透過受污染乳製品或直接接觸患畜）與治療場景和人用 MDR-TB 適應症存在本質差異。目前尚無直接測試 Delamanid 對 *M. bovis* 臨床分離株的體外或臨床研究，現有高分預測主要來自知識圖譜的基因組關聯推斷，尚待實驗驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | 觀察性／基因組研究 | BMC Genomics | 以全基因組定序（WGS）深入分析人類 *M. bovis* 分離株的基因型多樣性及藥物抗性基因組特徵，提供 MTBC 耐藥機轉分佈的最新全景圖；並未直接測試 Delamanid 的活性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Research Question**

**理由：**
- 現有證據僅達 L4（機轉推論／基因組觀察性研究），無任何臨床試驗直接支持 Delamanid 用於牛型結核病
- 牛型結核主要為獸醫與公衛議題，即使機轉可行，其人用藥物的臨床開發路徑（適應症定義、患者族群、監管框架）尚不明確

**若要推進需要：**
- 體外（in vitro）實驗確認 Delamanid 對 *M. bovis* 臨床分離株的最低抑菌濃度（MIC），建立活性基準
- 動物（牛／人畜共患感染）模型驗證療效與安全性
- 明確定義人類感染 *M. bovis*（人畜共患結核）的臨床需求場景，評估與現行 MDR-TB 治療指引的差異
- 取得詳細 MOA 資料（DrugBank API 查詢）以強化機轉關聯性分析

> **💡 補充說明**：在本次 10 個預測適應症中，排名第 2 的**非活動性結核病 (Inactive Tuberculosis)** 具有更強的臨床證據——包含 2 個進行中的 Phase 2/3 臨床試驗（尤其是 NCT03568383，PHOENIX 研究：直接測試 Delamanid 用於 MDR-TB 接觸者之預防，Phase 3，5,832 人）及 20 篇文獻，證據等級達 L2，建議決策為「Proceed with Guardrails」。建議優先針對此適應症深化評估。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

