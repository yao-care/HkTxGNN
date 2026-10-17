---
layout: default
title: Etoposide
parent: 高證據等級 (L1-L2)
nav_order: 353
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Etoposide：預測新適應症為尤文氏肉瘤 (Ewing Sarcoma)（證據等級 L1）。原適應症：小細胞肺癌、睪丸癌（睪丸生殖細胞腫瘤、精原細胞瘤等）"
monitor_inn: "ETOPOSIDE"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Etoposide
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Etoposide：從小細胞肺癌與睪丸生殖細胞腫瘤到尤文氏肉瘤 (Ewing Sarcoma)

## 一句話總結

Etoposide 是拓樸異構酶 II 抑制劑類的化療藥物，原本用於小細胞肺癌及睪丸生殖細胞腫瘤（含精原細胞瘤、卵黃囊瘤、畸胎瘤）。
TxGNN 模型預測它可能對**尤文氏肉瘤 (Ewing Sarcoma)** 有效，
目前有 **32 筆臨床試驗登記**和 **20 篇文獻**支持這個方向，其中含多個 Phase 3 隨機試驗。
但 etoposide 用於尤文氏肉瘤已是臨床常規，並非全新的再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 小細胞肺癌、睪丸癌（睪丸生殖細胞腫瘤、精原細胞瘤等）（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 尤文氏肉瘤 (Ewing Sarcoma) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位無資料）。就藥物類別而言，etoposide 屬拓樸異構酶 II 抑制劑，會造成快速分裂細胞的 DNA 雙股斷裂。它在小細胞肺癌與生殖細胞腫瘤的療效已被證實。

尤文氏肉瘤對基因毒性藥物高度敏感。文獻指出 EWS-FLI1 融合蛋白會增加 R-loop 並阻礙 BRCA1 修復，使腫瘤對 etoposide 特別敏感（PMID 29513652）。在臨床上，ifosfamide 加 etoposide 已是尤文氏肉瘤標準多藥化療的一環，與 VDC（長春新鹼、小紅莓、環磷醯胺）交替使用。

因此，機轉與臨床證據都支持此預測。需注意療效來自組合療法，不是 etoposide 單藥。

## 臨床試驗證據

以下列出最相關的 10 個試驗（資料中共 32 筆，其餘為相關性較低或僅間接涉及者）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 未知 | 1200 | EURO-E.W.I.N.G.99：比較尤文氏肉瘤化療合併或不合併放療／手術 |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 完成 | 587 | 尤文氏肉瘤及相關腫瘤的間隔縮短（compression）化療強化 |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 完成 | 642 | 標準五藥（含 etoposide）加 VTC，用於非轉移性尤文氏肉瘤 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 進行中（不招募） | 312 | 在多藥化療（含 etoposide）加 ganitumab，用於轉移性尤文氏肉瘤 |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 完成 | 278 | 非轉移性尤文氏肉瘤的劑量強化 vs 標準治療 |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | 未知 | 未提供 | EICESS 92：比較尤文氏肉瘤多種組合化療方案 |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | 完成 | 未提供 | 含 etoposide 的多藥化療後接手術與放療，用於周邊原始神經外胚層腫瘤／尤文氏肉瘤 |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | 完成 | 155 | 轉移性尤文氏肉瘤的高劑量化療、放療與維持治療 |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | 完成 | 130 | 轉移性尤文氏肉瘤合併生長因子支持的強化治療 |
| [NCT00014313](https://clinicaltrials.gov/study/NCT00014313) | Phase 2 | 提前終止 | 3 | 每週順鉑加口服 etoposide，用於骨／骨髓轉移的尤文氏肉瘤，樣本過小 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 標準化療加入 ifosfamide 與 etoposide，改善新診斷尤文氏肉瘤的存活 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012：比較歐美兩種標準化療方案 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | 間隔縮短化療加 ganitumab 用於轉移性尤文氏肉瘤 |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | 間隔縮短化療（VDC/IE 交替）用於局部尤文氏肉瘤 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT 計畫書 | Trials | EURO EWING 2012 試驗設計 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | 共識指引 | Cancer | 美國國家尤文氏肉瘤腫瘤委員會的處置建議 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | 尤文氏肉瘤目前處置與未來合作方向 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | 局部病灶存活率由約 10% 提升至約 75% |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | 回溯性分析 | Sarcoma | 33 位青少年與成人復發／難治患者使用口服 etoposide |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | 機轉研究 | Nature | EWS-FLI1 造成 R-loop 並阻礙 BRCA1 修復，解釋對 etoposide 的敏感性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40551 | ETOPOSIDE INJ 20MG/ML (ABIC) | 未提供 | 未提供 |
| HK-40664 | LASTET CAP 100MG | 未提供 | 未提供 |
| HK-40663 | LASTET CAP 50MG | 未提供 | 未提供 |
| HK-42309 | ETOPOSID EBEWE CONC FOR IV INF 20MG/ML | 未提供 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（拓樸異構酶 II 抑制劑） |
| 骨髓抑制風險 | 高（知識圖譜列出血小板減少、嗜中性白血球減少、白血球減少、無顆粒性白血球症、貧血等禁忌關聯；資料亦提示累積毒性包括骨髓抑制與續發性白血病） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜關聯的禁忌疾病（非仿單內容）**：血小板減少、嗜中性白血球減少、無顆粒性白血球症、白血球減少、貧血（含巨球性貧血）、間質性肺病、肺纖維化、腎功能不全、酸中毒（含代謝性酸中毒）、藥物性肝損傷。
- **藥物交互作用**：資料庫共查得 100 筆。列出者中屬中度的有 aprepitant、rolapitant、metronidazole、tinidazole、eliglustat、rosuvastatin、simvastatin；levofloxacin 為輕度；其餘（如 cimetidine、pantoprazole、doxycycline、morphine 等）等級未知。

香港仿單的警語與禁忌尚未取得，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 隨機試驗與 NEJM 等 RCT 支持含 etoposide 的方案用於尤文氏肉瘤，證據等級為 L1。
- 此用途已是臨床常規，並非新穎再利用。療效依賴組合療法，且骨髓抑制等毒性顯著，須設置防護措施。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症，確認是否已涵蓋尤文氏肉瘤，並確認各許可證的劑型
- 補充詳細的作用機轉資料（MOA）
- 依通訊協定與風險分層使用組合療法，並訂定血液學監測與累積毒性（含續發性白血病）追蹤計畫
- 評估口服與注射劑型在各族群（兒童、青少年、成人）的適用性

**其他預測適應症（供參考）：** 肺芽細胞瘤（L3，研究性問題，僅有病例報告）、原發性肺淋巴瘤、肺高分化胎兒型腺癌、陰道葡萄狀胚胎型橫紋肌肉瘤（均為 L4，建議 Hold，證據間接）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

