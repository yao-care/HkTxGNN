---
layout: default
title: Olaparib
parent: 高證據等級 (L1-L2)
nav_order: 541
evidence_level: L1
indication_count: 1
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Olaparib：邁向乳癌（Female Breast Carcinoma）新適應症評估

## 一句話總結

Olaparib（DrugBank ID: DB09074）是 PARP1/2 抑制劑，目前在香港/台灣**尚未上市**，核准適應症資料闕如。
TxGNN 模型預測它對**乳癌 (Female Breast Carcinoma)** 有效，
目前有 **超過 70 個臨床試驗**（含多個 Phase 3 RCT）和 **20 篇文獻**支持這個方向，證據等級達 L1。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無公開核准適應症資料（香港/台灣未上市，licenses 為空） |
| 預測新適應症 | 乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.09% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 DrugBank 結構化的 `original_moa` 欄位缺乏資料（DG002），但從證據包中的預測理由可還原其作用機轉：Olaparib 為 **PARP1/2 抑制劑**，阻斷單股 DNA 損傷的鹼基切除修復（BER）路徑。

在帶有 **BRCA1/2 生殖系突變**（同源重組修復缺陷, HRD）的腫瘤細胞中，PARP 抑制會導致雙股 DNA 損傷無法修復，產生「合成致死」效應而選擇性殺死腫瘤細胞。這個機轉並非單純的模型推測——它已是 Lynparza（olaparib）在多個國際市場中，用於 HER2 陰性、germline BRCA 突變乳癌核准適應症的核心藥理依據，並經 OlympiAD、OlympiA 等多項大型 Phase 3 RCT 驗證。

換言之，此預測的機轉關聯性極高：BRCA1/2 突變導致的 DNA 修復缺陷同時存在於卵巢癌與乳癌等腫瘤中，PARP 抑制劑的合成致死效應具有跨癌別的適用邏輯，這也是本項預測在證據等級被評為 L1（≥2 個已完成 Phase 3 RCT）的原因。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06580314](https://clinicaltrials.gov/study/NCT06580314) | Phase 3 | 招募中 | 880 | 比較 Olaparib 維持治療 1 年 vs 2 年（合併/不合併 Bevacizumab），探討 BRCA1/2 突變或 HRD 陽性腫瘤治療期程最適化 |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | 已完成 | 266 | Olaparib 單藥 vs 醫師選擇化療，用於 germline BRCA 突變之鉑敏感復發卵巢癌／乳癌族群（OlympiAD 試驗設計） |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | 已完成 | 103 | Olaparib 併用 Carboplatin 治療乳癌與卵巢癌（BRCA1/2 突變攜帶者及三陰性乳癌），評估最佳劑量與安全性 |
| [NCT05932862](https://clinicaltrials.gov/study/NCT05932862) | Phase 1 | 招募中 | 429 | XL309（ISM3091）單獨或併用 Olaparib 治療晚期實體瘤，評估安全性、藥動學與初步療效 |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | 已完成 | 77 | Olaparib 併用 Carboplatin 用於難治性/復發性婦科癌症（含乳癌），PK/PD 探索性研究 |
| [NCT02264678](https://clinicaltrials.gov/study/NCT02264678) | Phase 1/2 | 進行中未招募 | 357 | Ceralasertib 併用細胞毒性化療及/或 DNA 損傷修復抑制劑（含 Olaparib 相關機轉）之模組化安全性研究 |
| [NCT04553926](https://clinicaltrials.gov/study/NCT04553926) | N/A | 已完成 | 661 | Lynparza（Olaparib）錠劑韓國上市後監測研究，真實世界安全性與有效性資料 |
| [NCT02684318](https://clinicaltrials.gov/study/NCT02684318) | Phase 1b/2 | 狀態未知 | 100 | PM01183 併用 Olaparib 治療晚期實體瘤之探索性研究 |
| [NCT06065059](https://clinicaltrials.gov/study/NCT06065059) | Phase 1/2 | 已終止 | 7 | TNG348（USP1 抑制劑）單獨或併用 Olaparib 治療 BRCA1/2 突變或 HRD 陽性實體瘤，因故提前終止 |
| [NCT03162627](https://clinicaltrials.gov/study/NCT03162627) | Phase 1 | 進行中未招募 | 90 | Selumetinib 併用 Olaparib 治療 Ras 路徑異常之子宮內膜癌、卵巢癌等多癌別籃式試驗 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA 試驗總存活期分析：輔助 Olaparib 用於 germline BRCA1/2 突變高風險早期乳癌 |
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | NEJM | 輔助 Olaparib 用於 BRCA1/2 突變乳癌之關鍵性研究 |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | NEJM | OlympiAD 試驗：Olaparib 用於 germline BRCA 突變轉移性乳癌 |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD 最終總存活期與耐受性結果 |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD 延伸追蹤：總存活期與安全性更新 |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT | Nature | PARTNER 試驗：新輔助 Olaparib 併用化療用於三陰性乳癌 |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 單臂 | J Clin Oncol | TBCRC 048：Olaparib 用於帶有同源重組相關基因突變之轉移性乳癌 |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 1/2 併用試驗 | Cancer Cell | I-SPY2 試驗：Durvalumab 併用 Olaparib 及 Paclitaxel 用於高風險 HER2 陰性乳癌 |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Target Oncol | PARP 抑制劑用於乳癌治療之綜述 |
| [31650727](https://pubmed.ncbi.nlm.nih.gov/31650727/) | 2020 | Review | Ann Lab Med | BRCA1/2 致病變異型乳癌之治療與預防策略綜述 |

---

## 香港上市資訊

Olaparib 目前在香港（及台灣）**未上市**，`taiwan_regulatory.licenses` 無任何登記資料，故無許可證資訊可列。

---

## 細胞毒性

Olaparib 屬於**標靶抗腫瘤藥物**（PARP 抑制劑），非傳統細胞毒性化療藥物，但仍具血液學毒性風險，故列出本章節：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP1/2 抑制劑，非傳統細胞毒性化療藥） |
| 骨髓抑制風險 | 中度（PARP 抑制劑類效應，臨床上常見貧血、嗜中性白血球減少、血小板減少） |
| 致吐性分級 | 低至中度 |
| 監測項目 | 全血球計數（CBC，含分類）、腎功能、肝功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項（DG001 標記為 Blocking，尚無法完成 S1 安全性初評） |

---

## 安全性考量

安全性資訊請參考原廠仿單。（`key_warnings`、`contraindications`、DDI 查詢均無可用資料，且 TFDA 仿單警語/禁忌為 Blocking 等級的資料缺口，尚未完成安全性初評）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉關聯性極強且已有 5 個以上 Phase 3 RCT（OlympiA、OlympiAD 系列）直接支持 Olaparib 用於 BRCA1/2 突變乳癌，證據等級達 L1。
- 但香港/台灣尚未上市、無許可證資料，且仿單警語/禁忌屬於 Blocking 等級的資料缺口（DG001），安全性初評（S1）無法完成，須以防護措施推進。

**若要推進需要：**
- 補齊 TFDA／當地藥監局仿單警語與禁忌資料（DG001，Blocking）
- 補齊結構化作用機轉資料（DG002，High），與 DrugBank API 對接確認 MOA 與藥物分類
- 確認是否有意向廠商申請香港/台灣上市及乳癌適應症登記
- 補充藥物交互作用（DDI）與骨髓抑制毒性之正式監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

