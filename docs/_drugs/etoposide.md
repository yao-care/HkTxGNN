---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
monitor_inn: "ETOPOSIDE"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
last_modified_at: 2026-10-28
description: "Etoposide：預測新適應症為Well-differentiated fetal adenocarcinoma of the lung（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Etoposide
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

## Etoposide: Well-differentiated fetal adenocarcinoma of the lung
{: .text-alpha }

## 一句話總結

Etoposide 是拓樸異構酶 II 抑制劑類的化療藥物，知識圖譜記錄的原適應症包括小細胞肺癌與睪丸生殖細胞腫瘤。
TxGNN 模型預測它可能對 **Ewing 肉瘤 (Ewing sarcoma)** 有效，
目前有 **多項 Ewing 肉瘤相關臨床試驗（含數項 Phase 3）**和 **多篇文獻（含隨機對照試驗）**支持這個方向，但 etoposide 是以組合療法成分的形式被使用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，etoposide 是拓樸異構酶 II 抑制劑，會造成 DNA 股斷裂，是肺癌與生殖細胞腫瘤化療方案中的常用成分。

Ewing 肉瘤是兒童與年輕成人的惡性骨與軟組織腫瘤。文獻指出，Ewing 肉瘤對 etoposide 這類基因毒性藥物高度敏感。標準治療為 VDC（長春新鹼、小紅莓、環磷醯胺）與 IE（ifosfamide、etoposide）交替的組合化療，加上手術或放療。

需要說明的是，etoposide 在此是組合療法的一部分，並非單藥治療；其獨立貢獻難以從現有試驗中分離。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 未知 | 1200 | EURO-E.W.I.N.G.99，Ewing 肉瘤化療合併或不合併放療／手術 |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 完成 | 587 | Ewing 肉瘤及相關腫瘤的間隔壓縮化療比較 |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 完成 | 642 | 標準五藥方案（含 etoposide）加 VTC 用於非轉移性 Ewing 肉瘤 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 進行中（不再招募） | 312 | 多藥化療（含 etoposide）加 ganitumab 用於轉移性 Ewing 肉瘤 |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 完成 | 278 | 非轉移性 Ewing 肉瘤劑量強化的隨機試驗 |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | 未知 | 未提供 | EICESS 92，比較不同組合化療方案加手術與放療 |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | 完成 | 155 | 轉移性 Ewing 肉瘤高劑量化療、放療與維持治療 |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | 完成 | 未提供 | 含 etoposide 的組合化療後接放療，用於周邊神經外胚層腫瘤／Ewing 肉瘤 |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | 進行中（不再招募） | 83 | Irinotecan 與 temozolomide 加高劑量烷化劑化療用於新診斷 Ewing 肉瘤 |
| [NCT07194044](https://clinicaltrials.gov/study/NCT07194044) | Phase 1 | 招募中 | 15 | 轉移性 Ewing 肉瘤的排程強化可行性研究 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 在標準化療中加入 ifosfamide 與 etoposide，用於新診斷 Ewing 肉瘤／骨原始神經外胚層腫瘤 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012：比較兩種新診斷 Ewing 肉瘤化療方案 |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | 間隔壓縮化療（VDC/IE 交替）用於局部 Ewing 肉瘤 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | Ganitumab 加間隔壓縮化療用於轉移性 Ewing 肉瘤 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT 方案 | Trials | EURO EWING 2012 國際隨機試驗方案 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | 共識指引 | Cancer | 美國 Ewing 肉瘤腫瘤委員會的治療共識建議 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Ewing 肉瘤綜述，局部病灶存活率由約 10% 提升至約 75% |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Ewing 肉瘤的現行處置與合作研究 |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | 回溯性分析 | Sarcoma | 33 位青少年與成人復發／難治 Ewing 肉瘤患者使用口服 etoposide |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | 機轉研究 | Nature | EWS-FLI1 造成 R-loop 並阻斷 BRCA1 修復，解釋對 etoposide 等基因毒性藥物的敏感性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40551 | ETOPOSIDE INJ 20MG/ML (ABIC) | 未提供 | 未提供 |
| HK-40664 | LASTET CAP 100MG | 未提供 | 未提供 |
| HK-40663 | LASTET CAP 50MG | 未提供 | 未提供 |
| HK-42309 | ETOPOSID EBEWE CONC FOR IV INF 20MG/ML | 未提供 | 未提供 |

以上 4 張許可證均為單一成分且有效。本次彙整的資料未包含許可證核准適應症文字，因此原適應症僅能視為知識圖譜中記錄的關聯。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（拓樸異構酶 II 抑制劑） |
| 骨髓抑制風險 | 高（知識圖譜將血小板減少、嗜中性白血球減少、白血球減少、貧血列為相關禁忌疾病） |
| 致吐性分級 | 低至中度（依藥物類別判斷，請以原廠仿單為準） |
| 監測項目 | CBC（含分類與血小板）、肝功能、腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜記錄的禁忌相關疾病**（非仿單文字）：血小板減少、嗜中性白血球減少、顆粒性白血球缺乏、貧血、間質性肺病、腎功能受損、酸中毒、藥物性肝損傷、白血球減少、肺纖維化。
- **藥物交互作用**：資料庫共記錄 100 筆，中度者包括 aprepitant、metronomidazole（Metronidazole）、eliglustat、rolapitant、rosuvastatin、simvastatin、tinidazole；輕度者包括 levofloxacin。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Ewing 肉瘤已有多個 Phase 3 隨機試驗與 NEJM 等 RCT 支持含 etoposide 的組合化療，直接研究此疾病，證據等級為 L1。
- 但 etoposide 是以組合成分使用，獨立貢獻難以分離，且本次資料缺乏香港許可證核准適應症、作用機轉與仿單安全性資料。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌
- 補充詳細作用機轉資料
- 確認 Ewing 肉瘤使用的組合方案（VDC/IE）與劑量，並建立骨髓抑制的監測計畫
- 確認香港是否已有 Ewing 肉瘤的標示或院內治療指引
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

