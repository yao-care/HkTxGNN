---
layout: default
title: Fenbendazole
parent: 中證據等級 (L3-L4)
nav_order: 310
evidence_level: L4
indication_count: 10
---

# Fenbendazole
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

# Fenbendazole：從獸用驅蟲藥到膀胱癌 (Urinary Bladder Carcinoma)

## 一句話總結

Fenbendazole 是廣泛應用於獸醫臨床的苯並咪唑類（benzimidazole）驅蟲藥，透過抑制 β-微管蛋白聚合殺滅寄生蟲，在人體尚未取得任何核准適應症。
TxGNN 模型預測它可能對**膀胱癌 (Urinary Bladder Carcinoma)** 有效，預測分數高達 **99.99%**，
目前有 **0 個臨床試驗**及 **2 篇前臨床文獻**（來自相關膀胱腫瘤研究）支持此方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 獸用驅蟲藥（寄生蟲感染；人體未核准任何適應症） |
| 預測新適應症 | 膀胱癌 (Urinary Bladder Carcinoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question（暫緩） |

---

## 為什麼這個預測合理？

目前缺乏 Fenbendazole 的正式人體作用機轉資料（MOA 資料缺口）。根據其藥物類別，Fenbendazole 屬於苯並咪唑類驅蟲藥，其已知機轉為**結合並破壞 β-微管蛋白（β-tubulin）的聚合**，進而干擾寄生蟲的有絲分裂紡錘體組裝。

這個機轉在腫瘤學上具有合理的外推基礎：微管（microtubule）是癌細胞有絲分裂的關鍵結構，破壞其動態平衡可誘導腫瘤細胞發生 **G2/M 期阻滯（G2/M arrest）**並觸發細胞凋亡（apoptosis）。此作用原理與臨床已廣泛使用的微管靶向抗癌藥物（長春鹼類、紫杉醇類）在機轉上高度相似，是 TxGNN 知識圖譜對 Fenbendazole 作出膀胱癌強預測的理論基礎。

更關鍵的是，2024 年的前臨床研究（PMID 39128990）直接採用**膀胱內灌注（intravesical instillation）** 途徑，探索 Fenbendazole 與 CRISPR-Cas13a 的協同抗膀胱癌效應。此給藥路徑與現行膀胱癌標準治療（BCG、絲裂黴素 C 膀胱灌注）完全一致，可最大化腫瘤局部藥物濃度並降低全身毒性風險，為將來人體試驗的設計提供了直接的轉譯參考。

---

## 文獻證據

> 以下文獻來源於 urinary bladder neoplasm（Rank 2）適應症，因膀胱癌（bladder carcinoma，Rank 1）為其下位疾病術語，證據可合理外推。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | 前臨床（in vitro + in vivo） | J Exp Clin Cancer Res | CRISPR-Cas13a 與 Fenbendazole 聯合膀胱內灌注治療膀胱癌，展示顯著協同抗腫瘤活性；此為目前最直接支持膀胱灌注給藥途徑的關鍵文獻 |
| [23208426](https://pubmed.ncbi.nlm.nih.gov/23208426/) | 2012 | 機轉/實驗 | J Toxicol Sci | 大鼠 28 天給藥後致癌物誘發 Ubiquitin D 於 G2 期異常活化及細胞凋亡的機轉分析；提供 G2/M 阻滯凋亡通路的間接機轉佐證 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **備註**：Fenbendazole 在香港及台灣均未取得人用藥物許可，目前無法從在地藥監局資料庫取得人體安全性資料。獸用製劑的安全性資料不能直接外推至人體使用。

---

## 結論與下一步

**決策：Research Question（暫緩推進）**

**理由：**
TxGNN 對膀胱癌相關適應症群的預測分數極高（99.99%，為 10 項預測中最高），且 β-tubulin 抑制機轉在理論上對高增殖性尿路上皮癌細胞有效；2024 年的前臨床研究進一步以膀胱內灌注途徑驗證了協同抗腫瘤效應，給藥路徑與臨床標準治療相容。然而，目前完全缺乏人體臨床試驗數據，且人體 MOA、PK/PD 及安全性資料存在重要缺口，尚不具備直接進入臨床評估的條件，整體證據等級僅達 **L4（前臨床）**。

**若要推進需要：**
- 系統性文獻搜尋 Fenbendazole 抗腫瘤前臨床資料（IC₅₀、動物模型療效與毒性窗口）
- 取得完整 MOA 資料（建議查詢 DrugBank DB11410 及 benzimidazole 類藥物腫瘤學文獻）
- 評估膀胱內灌注給藥的人體 PK/PD 可行性（可外推已核准 benzimidazole 類藥物人體資料）
- 確認 BCG 抗性 NMIBC（非肌層浸潤性膀胱癌）作為 Phase 0/1 首選切入族群的合理性
- 補充香港人用藥物安全性監管路徑評估（需與 PMDA/FDA/EMA 溝通 off-label 研究策略）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

