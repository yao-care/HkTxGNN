---
layout: default
title: Paclitaxel
parent: 高證據等級 (L1-L2)
nav_order: 552
evidence_level: L1
indication_count: 5
---

# Paclitaxel
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

# Paclitaxel：原適應症資料缺口下的乳癌（Female Breast Carcinoma）適應症驗證

## 一句話總結

Paclitaxel（紫杉醇）為全球廣泛使用的微管抑制劑類化療藥物，但本站香港藥品登記資料庫目前**未收錄任何許可證、原適應症亦為空白**。TxGNN 模型預測其對**乳癌 (Female Breast Carcinoma)** 有效，證據等級達 **L1**，目前有 **50+ 個臨床試驗**支持——值得注意的是，Paclitaxel 本身即為全球乳癌標準化療藥物之一，此預測性質上更接近「還原已知療效」而非全新老藥新用假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本站資料庫未收錄（licenses 與 original_indications 均為空），但依機轉證據，Paclitaxel 屬全球公認之實體腫瘤（含乳癌）標準化療藥物 |
| 預測新適應症 | 乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Paclitaxel 的作用機轉為穩定微管聚合、抑制紡錘體解聚，阻斷細胞有絲分裂 M 期，對高增殖率的乳癌細胞具直接細胞毒殺效果；此機轉為全球乳癌化療核心藥物（如 Taxol、Abraxane）之基礎，機轉與臨床應用高度一致。

本站藥品資料庫顯示 Paclitaxel「未上市」且無許可證登記，原適應症欄位空白，這屬於**在地登記/資料收錄缺口**，並非藥理證據不足。換言之，TxGNN 預測出「乳癌」高分並非發現新用途，而是模型正確辨識出這個藥物與疾病之間本已存在的強關聯——目前排名前五的預測適應症中，除第 4 名（Ehrlich tumor，屬小鼠腹水癌動物模型，非人類疾病實體，建議 Hold）外，其餘（女性乳癌、ER 陰性乳癌、荷爾蒙抗性乳癌、ER 陽性乳癌）皆為乳癌臨床亞型，彼此高度一致，進一步佐證此為穩定的已知信號而非雜訊。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Phase 3 | 完成 | 444 | 雙盲安慰劑對照，評估 Lapatinib+Paclitaxel 於 ErbB2 陽性轉移性乳癌，高品質直接證據 |
| [NCT00006256](https://clinicaltrials.gov/study/NCT00006256) | Phase 2 | 完成 | 44 | Paclitaxel 併同步放療於早期（Stage II-III）乳癌，直接支持適應症 |
| [NCT00004067](https://clinicaltrials.gov/study/NCT00004067) | Phase 3 | 完成 | 2130 | AC-T ± Herceptin 於 HER2 過度表現、淋巴結陽性乳癌，樣本量大 |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | 完成 | 455 | Neo ALTTO：Lapatinib/Trastuzumab 併 Paclitaxel 新輔助治療 HER2 陽性乳癌 |
| [NCT03799679](https://clinicaltrials.gov/study/NCT03799679) | Phase 4 | 狀態不明 | 60 | Nab-paclitaxel 續接 Epirubicin+Cyclophosphamide 新輔助治療三陰性乳癌 |
| [NCT02954055](https://clinicaltrials.gov/study/NCT02954055) | Phase 2 | 完成 | 140 | Metronomic 方案 vs 傳統 Paclitaxel 單藥治療 ER+/HER2- 轉移性乳癌 |
| [NCT01091428](https://clinicaltrials.gov/study/NCT01091428) | Phase 2 | 完成 | 191 | MLN8237 併每週 Paclitaxel vs Paclitaxel 單藥，用於復發性卵巢/乳癌族群 |
| [NCT03289819](https://clinicaltrials.gov/study/NCT03289819) | Phase 2 | 完成 | 53 | Pembrolizumab 併 Nab-paclitaxel 新輔助治療三陰性乳癌 |
| [NCT02301988](https://clinicaltrials.gov/study/NCT02301988) | Phase 2 | 完成 | 151 | Ipatasertib（AKT 抑制劑）併 Paclitaxel 新輔助治療早期三陰性乳癌 |
| [NCT00044525](https://clinicaltrials.gov/study/NCT00044525) | Phase 2 | 完成 | 82 | 評估紫杉類抗藥性轉移性乳癌之替代藥物療效與安全性 |

## 文獻證據

目前無相關文獻（PubMed 針對「Paclitaxel + female breast carcinoma」查詢結果為 0 篇，見 query_log id 4）。

## 香港上市資訊

本站資料庫未收錄 Paclitaxel 之香港許可證資訊（`market_status`：未上市，`total_licenses`：0）。

## 細胞毒性

**此章節顯示，因 Paclitaxel 屬傳統細胞毒性化療藥物（taxane 類）。**

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Taxane 類，微管聚合穩定劑，阻斷有絲分裂 M 期） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項（本站無毒性資料） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。（本站 `key_warnings`、`contraindications`、DDI 查詢均無資料）

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
乳癌相關證據等級達 L1，且多個已完成 Phase 3 RCT（如 NCT00281658、NCT00004067、NCT00553358）直接支持 Paclitaxel 於乳癌之療效，機轉合理性高。但本站對 Paclitaxel 的**藥品安全性資料（TFDA/香港仿單警語與禁忌）屬 Blocking 缺口**，在補齊前無法完成 S1 安全性初評，故不宜直接 Go。

**若要推進需要：**
- 補齊香港（或參考地區）仿單之警語與禁忌資料（DG001，Blocking，來源：官方仿單 PDF 解析）
- 補齊正式作用機轉（MOA）資料（DG002，High，來源：DrugBank API）
- 確認 Paclitaxel 是否應於本站藥品資料庫新增上市/許可證登記，釐清目前「未上市」是否為資料收錄缺口而非實際市場狀態
- 排除 Ehrlich tumor（動物模型）等非人類疾病實體的預測結果，避免混入決策評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

