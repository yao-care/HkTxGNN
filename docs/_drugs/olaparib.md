---
layout: default
title: Olaparib
parent: 高證據等級 (L1-L2)
nav_order: 640
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
description: "Olaparib：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L1）。原適應症：卵巢癌（含卵巢腺癌、遺傳性乳癌卵巢癌症候群等）"
---

# Olaparib
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Olaparib：從卵巢癌到女性乳癌

## 一句話總結

Olaparib 是一種 PARP 抑制劑，原本用於卵巢癌（含 BRCA 突變相關卵巢癌）治療。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，
目前有 **多項臨床試驗**（含 Phase 3 與 Phase 2）和**多篇高階文獻**（含 OlympiAD、OlympiA 等隨機對照試驗）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌（含卵巢腺癌、遺傳性乳癌卵巢癌症候群等） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.09% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。根據已知的 PARP 抑制劑藥理，Olaparib 透過抑制 PARP 酵素，阻斷單股 DNA 斷裂的修復。在帶有同源重組缺陷（例如 BRCA1/2 突變）的腫瘤中，雙股斷裂也無法由 BRCA 途徑修復，癌細胞因「合成致死」而死亡。

卵巢癌與乳癌同樣與 BRCA1/2 突變密切相關（如「遺傳性乳癌卵巢癌症候群」），兩者在缺陷的 DNA 修復生物學上相同。因此，在卵巢癌中有效的機轉，理論上也適用於 BRCA 突變的乳癌。TxGNN 的高分預測與這一共同的生物學基礎一致。

需特別注意：預期獲益僅限於經生物標記篩選的族群（胚系 BRCA1/2 突變、HER2 陰性），不預期對未經篩選的一般乳癌族群有效。

---

## 臨床試驗證據

資料中共有 30 筆相關試驗登記，以下列出最相關的 10 筆（依相關性分級與階段排序）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | 完成 | 99 | 單臂試驗，評估 olaparib 於 BRCA 突變乳癌／卵巢癌的反應率，為 BRCA 突變族群的直接療效訊號 |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | 完成 | 202 | 印度患者的上市後研究，涵蓋 gBRCA 突變轉移性乳癌與鉑類敏感復發卵巢癌 |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | 招募中 | 34 | Pembrolizumab 加放射治療，合併或不合併 olaparib，用於轉移性三陰性／HR 陽性 HER2 陰性乳癌 |
| [NCT02684318](https://clinicaltrials.gov/study/NCT02684318) | Phase 1/2 | 未知 | 100 | PM01183 (lurbinectedin) 合併 olaparib 用於晚期實體腫瘤 |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | 完成 | 118 | PI3K 抑制劑合併 olaparib 用於復發三陰性乳癌或高惡性度漿液性卵巢癌，提供劑量與安全性資料 |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | 完成 | 77 | Olaparib 合併 carboplatin 的藥動／藥效研究，用於難治或復發婦科癌症 |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | 進行中 | 155 | Cediranib 合併 olaparib 用於復發卵巢癌或三陰性乳癌 |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | 完成 | 25 | Carboplatin-olaparib 後接 olaparib 單藥，用於 BRCA 突變 HER2 陰性晚期乳癌第一線，Phase I 部分確定建議劑量 |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | 完成 | 24 | Olaparib 合併放射治療用於三陰性乳癌 |
| [NCT07695259](https://clinicaltrials.gov/study/NCT07695259) | Phase 4 | 招募中 | 45 | Olaparib 合併 trastuzumab 與 pertuzumab，用於高齡 HER2 陽性乳癌新輔助治療 |

此外，資料中另有 Phase 3 試驗 NCT02282020（olaparib 對照醫師選擇化療，用於 gBRCA 突變鉑類敏感復發卵巢癌，266 人，已完成），屬於原適應症（卵巢癌）的證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD：olaparib 用於胚系 BRCA 突變轉移性乳癌 |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD 最終整體存活與耐受性結果，olaparib vs. 醫師選擇化療 |
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA：輔助性 olaparib 用於 BRCA1/2 突變早期乳癌 |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA 整體存活分析，用於 gBRCA1/2 突變高風險 HER2 陰性早期乳癌 |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 | J Clin Oncol | TBCRC 048：olaparib 用於體細胞 BRCA 或其他同源重組相關基因突變的轉移性乳癌 |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | Phase 2 | J Clin Oncol | Olaparib 單藥用於胚系 BRCA1/2 突變的晚期癌症 |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 | Cancer Cell | I-SPY2：durvalumab 合併 olaparib 與 paclitaxel 提高 HER2 陰性乳癌的病理完全緩解率 |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | 延長追蹤 | Eur J Cancer | OlympiAD 延長追蹤的整體存活與安全性 |
| [32249603](https://pubmed.ncbi.nlm.nih.gov/32249603/) | 2020 | Review | Future Oncol | Olaparib 用於晚期乳癌的回顧 |
| [39742383](https://pubmed.ncbi.nlm.nih.gov/39742383/) | 2024 | 系統性回顧 | Breast J | 轉移性三陰性乳癌標靶治療的系統性回顧 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65987 | LYNPARZA TABLETS 150MG | 錠劑 | 資料未提供 |
| HK-65988 | LYNPARZA TABLETS 100MG | 錠劑 | 資料未提供 |

兩張許可證均為單一成分製劑，持證商為 AstraZeneca Hong Kong Limited，狀態皆為有效。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 建議監測 CBC（含分類）、肝腎功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，其中較重要的包括：
  - **嚴重 (Major)**：Aprepitant、Dexamethasone、Clarithromycin
  - **中度 (Moderate)**：Metformin、Bupropion、Cimetidine、Miconazole、Clotrimazole、Glyburide、Ondansetron、Repaglinide、Rosuvastatin、Simvastatin 等
  - **輕微 (Minor)**：Prucalopride

  其中數項為 CYP3A 相關抑制劑／誘導劑，合併使用時需評估是否調整劑量。

其他警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多項隨機對照 Phase 3 試驗（OlympiAD、OlympiA）顯示 olaparib 對胚系 BRCA1/2 突變、HER2 陰性乳癌有效，機轉與原適應症（卵巢癌）一致，且 TxGNN 預測分數高（99.09%）。
- 療效僅限生物標記篩選的族群，且香港許可證適應症與仿單安全性資料尚缺，故需設定使用條件。

**若要推進需要：**
- 取得香港衛生署核准適應症與仿單內容，確認乳癌是否已涵蓋於本地適應症
- 限定使用於胚系 BRCA1/2 突變、HER2 陰性的患者，並要求事前基因檢測
- 補充 MOA 與完整安全性資料（警語、禁忌症）
- 制定血液學監測計畫，並建立 CYP3A 相關藥物交互作用的處方審查機制
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

