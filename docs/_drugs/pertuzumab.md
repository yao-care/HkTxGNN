---
layout: default
title: Pertuzumab
parent: 高證據等級 (L1-L2)
nav_order: 685
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Pertuzumab：預測新適應症為黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)（證據等級 L1）。原適應症：HER2 陽性乳癌（HER2 positive breast carcinoma）"
---

# Pertuzumab
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Pertuzumab：從 HER2 陽性乳癌到黃體素受體陽性乳癌

## 一句話總結

Pertuzumab 是一種抗 HER2 單株抗體，原本用於 HER2 陽性乳癌治療。
TxGNN 模型預測它可能對**黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)** 有效，
目前有 **1 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過這比較像是 HER2 陽性乳癌下的亞型延伸，而非真正的跨疾病再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（HER2 positive breast carcinoma） |
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Pertuzumab 會結合 HER2 細胞外二聚化區域（subdomain II），阻斷 HER2 與 HER3、EGFR 形成異源二聚體，進而抑制 PI3K/AKT 與 MAPK 訊號路徑。（註：資料庫中缺乏正式的作用機轉欄位，以上說明來自本報告整理的機轉分析。）

黃體素受體陽性乳癌大多屬於 HR+/HER2+ 乳癌，也就是已核准的 HER2 陽性乳癌族群中的一個子集。因此這屬於**亞型延伸**，而非真正的再利用。HER2 訊號軸是驅動因素，而 HER2 訊號與荷爾蒙受體之間的交互作用會造成內分泌治療抗藥性，這支持將 pertuzumab 與內分泌治療合併使用。

需要注意：此預測只適用於 HER2 陽性的患者，不適用於 HER2 陰性的黃體素受體陽性乳癌。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | 完成 | 517 | QL1209（pertuzumab 生物相似藥）與原廠 pertuzumab 併用 trastuzumab、docetaxel，用於 HER2 陽性、ER/PR 陰性的早期或局部晚期乳癌術前治療的等效性試驗；對原廠藥療效僅為間接支持，且無 PR 分層的療效估計 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Annals of Oncology | WSG-ADAPT HER2+/HR- 試驗：評估 trastuzumab + pertuzumab 雙重阻斷 12 週（±每週 paclitaxel）的療效與預測標記 |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT | British Journal of Cancer | QL1209 與原廠 pertuzumab 在 HER2 陽性、ER/PR 陰性乳癌術前治療的 Phase 3 等效性試驗 |
| [42150145](https://pubmed.ncbi.nlm.nih.gov/42150145/) | 2026 | RCT | Journal of Clinical Oncology | WSG TP-II 試驗存活分析：HR+/HER2+ 早期乳癌，術前 trastuzumab + pertuzumab 加內分泌治療 vs. 化療 |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II：HR+/HER2+ 早期乳癌，內分泌治療加雙重 HER2 阻斷與減量化療的比較 |
| [41401771](https://pubmed.ncbi.nlm.nih.gov/41401771/) | 2026 | RCT | ESMO Open | TQB2440（pertuzumab 生物相似藥）與原廠藥在 HER2 陽性早期或局部晚期乳癌的等效性試驗 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | Journal of Clinical Oncology | ASCO 晚期 HER2 陽性乳癌全身治療指引更新 |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Cohort | The Lancet Oncology | NeoSphere 5 年分析：術前 pertuzumab + trastuzumab 的無惡化存活、無病存活與安全性 |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treatment Reviews | HR+/HER2+ 乳癌的現況與未來，探討兩條訊號路徑的交互作用 |
| [41387082](https://pubmed.ncbi.nlm.nih.gov/41387082/) | 2026 | Review | Breast | 停經前 HR+/HER2+ 乳癌輔助卵巢功能抑制與芳香環轉化酶抑制劑的回溯性世代分析 |
| [42623567](https://pubmed.ncbi.nlm.nih.gov/42623567/) | 2026 | 次級分析 | Journal of Clinical Oncology | EA1181/CompassHER2 pCR：taxane + trastuzumab + pertuzumab 的 pCR 率與預測因子 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62758 | PERJETA CONCENTRATE FOR SOLUTION FOR INFUSION 420MG | 未提供 | 未提供 |
| HK-67118 | PHESGO SOLUTION FOR SUBCUTANEOUS INJECTION 1200MG/600MG IN 15ML | 未提供 | 未提供 |
| HK-67119 | PHESGO SOLUTION FOR SUBCUTANEOUS INJECTION 600MG/600MG IN 10ML | 未提供 | 未提供 |

---

## 細胞毒性

Pertuzumab 為標靶單株抗體，非傳統細胞毒性藥物，但屬於抗腫瘤藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 HER2 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫查詢到 Idelalisib（中度，來源 DDInter）。另有藥理資料顯示其作用標的為 ERBB2（HER2），此為藥理作用標的，不屬於臨床交互作用。

其餘警語與禁忌症資料缺乏，請參考原廠仿單。文獻中也提到，pertuzumab 與 trastuzumab 併用時需留意心臟安全性（TRYPHAENA、BERENICE 試驗專門評估此點），以及懷孕期間使用的風險。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有完成的 Phase 3 RCT 及多項 RCT 文獻（含 WSG-TP-II 針對 HR+/HER2+ 族群）支持，但這是已核准 HER2 陽性適應症下的亞型延伸；唯一登記的 Phase 3 試驗是生物相似藥等效性試驗，且收案對象為 ER/PR 陰性，並非針對 PR 陽性族群。
- 香港已有 3 張有效許可證，且機轉上有明確依據。

**若要推進需要：**
- 確認適用範圍限於 HER2 陽性患者，並以 HER2 檢測為前提條件
- 取得 PR 陽性族群的分層療效數據（如 WSG-TP-II、PERTAIN 的子群分析）
- 取得香港衛生署核准的仿單，確認適應症文字、警語與禁忌症
- 建立心臟功能監測計畫（如 LVEF 追蹤）
- 補充正式的作用機轉資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

