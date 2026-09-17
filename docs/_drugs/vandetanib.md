---
layout: default
title: Vandetanib
parent: 高證據等級 (L1-L2)
nav_order: 789
evidence_level: L2
indication_count: 5
---

# Vandetanib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Vandetanib：從甲狀腺髓質癌到腎細胞癌

## 一句話總結

> Vandetanib 是一款口服多標靶酪胺酸激酶抑制劑（RET/VEGFR/EGFR），文獻顯示其原核准用於治療**甲狀腺髓質癌 (Medullary Thyroid Cancer)**。
> TxGNN 模型預測它可能對**腎細胞癌 (Renal Cell Carcinoma)** 有效，
> 目前有 **4 個臨床試驗**和 **6 篇文獻**與此方向相關，但其中 2 個試驗因故提前終止，證據強度中等。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲狀腺髓質癌（依文獻佐證，DrugBank 未提供正式 original_indications 資料） |
| 預測新適應症 | 腎細胞癌 (Renal Cell Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Vandetanib 是一款多標靶酪胺酸激酶抑制劑（TKI），同時作用於 VEGFR2/3、EGFR 及 RET 三個路徑。其原始適應症甲狀腺髓質癌主要透過抑制 RET 激酶（該基因於甲狀腺髓質癌中常見組成性活化）發揮療效，但其 VEGFR 抑制活性同時具備抗血管新生作用。

腎細胞癌（尤其是 clear cell RCC 亞型）的致病機轉高度依賴 VHL-HIF-VEGF 訊號軸，VEGFR 抑制是這類腫瘤已被充分驗證的治療策略——事實上，同屬多標靶 TKI 類別的 sunitinib、pazopanib、cabozantinib 皆已核准用於 RCC 治療，與 vandetanib 屬於同一類機轉（class effect）。

不過需注意，現有 4 個相關 Phase 2 試驗中有 2 個因故提前終止（樣本數僅 3 人及 7 人），提示可能存在療效不足、招募困難或安全性顧慮，需進一步釐清終止原因才能判斷是否值得推進。目前缺乏完整的 DrugBank MOA 正式描述，上述機轉推論主要根據試驗證據佐證的作用機制整理而成。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2（隨機對照） | 完成 | 82 | Carboplatin+Gemcitabine 併用 vandetanib 作為晚期泌尿上皮癌一線治療，樣本數最大且為隨機設計，證據品質最佳 |
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | 完成 | 37 | 評估 vandetanib 於 Von Hippel-Lindau 疾病相關腎腫瘤（clear cell RCC 重要亞群）之療效 |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | **提前終止** | 7 | Vandetanib 併用 metformin 用於 HLRCC 或 SDH 相關腎癌，樣本數極小 |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | **提前終止** | 3 | 評估 vandetanib 於晚期 clear cell RCC 之療效，極早期終止，幾無可用療效數據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educational Book | Vandetanib 為口服 RET 激酶抑制劑，已獲美國 FDA 核准用於轉移性甲狀腺髓質癌 |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets and Therapy | 回顧抗血管新生 TKI 類別藥物（含 vandetanib）於實體腫瘤之應用現況 |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bulletin du Cancer | 討論同類多標靶 TKI（cabozantinib）於 VEGFR/c-MET 路徑之機轉與腎癌相關療效 |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | 探討 fumarate hydratase 缺陷型轉移性腎細胞癌之代謝與表觀遺傳標靶治療 |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | RCT（不同藥物：guadecitabine） | Clin Cancer Res | SDH 缺陷相關腫瘤（含 HLRCC 相關腎癌）之標靶治療試驗，非直接測試 vandetanib |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical（小鼠模型） | Mol Cancer Res | TFE3 易位型腎細胞癌動物模型研究，發現新治療標靶及診斷標記 |

---

## 香港上市資訊

Vandetanib 目前**尚未在香港上市**，無許可證登記資料。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑：VEGFR2/3、EGFR、RET） |
| 骨髓抑制風險 | 資料不足，一般而言多標靶 TKI 類別骨髓抑制風險屬低至中度 |
| 致吐性分級 | 低至中度（依 TKI 類別藥物一般特性推估） |
| 監測項目 | CBC（含分類）、肝腎功能、心電圖（TKI 類別藥物常見需監測 QT 間期） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。目前 TFDA 仿單警語與禁忌症資料缺失（Blocking 等級資料缺口），尚無法完成 S1 安全性初評，也未查得藥物交互作用資料。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 項隨機對照 Phase 2 試驗（n=82，完成）及 1 項非隨機 Phase 2 試驗（n=37，完成）支持 VEGFR 抑制機轉於腎細胞癌之潛在療效，機轉關聯性強（與已核准 TKI 類藥物同屬 class effect），證據等級達 L2。
- 但另有 2 項試驗因故提前終止（n=3、n=7），且目前缺乏 TFDA 仿單安全性資料（Blocking 等級缺口），無法完成完整安全性初評，須在有條件監測下謹慎推進。

**若要推進需要：**
- 釐清 NCT02495103、NCT01372813 兩項試驗提前終止的具體原因
- 補齊 DrugBank / TFDA 正式 MOA 與仿單警語、禁忌症資料
- 若考慮推進，優先鎖定 clear cell RCC 亞型（VHL/HIF-VEGF 驅動），排除證據薄弱之罕見亞型（Xp11.2 易位型、neuroblastoma 相關型、unclassified 型、renal pelvis carcinoma，皆屬 L4-L5 證據等級，建議維持 Hold）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

