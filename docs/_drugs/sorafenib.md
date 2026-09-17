---
layout: default
title: Sorafenib
parent: 高證據等級 (L1-L2)
nav_order: 700
evidence_level: L2
indication_count: 5
---

# Sorafenib
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

Using `superpowers:using-superpowers`要求檢查技能——本任務為純格式化文件產出（依既定 v5 prompt 撰寫評估報告），非程式開發／除錯，未觸發流程類技能，直接依模板產出。

---

# Sorafenib：從腎細胞癌到脂肪肉瘤

## 一句話總結

Sorafenib 是已核准用於腎細胞癌（Renal Cell Carcinoma）等癌症的多重激酶抑制劑。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **2 個臨床試驗**（其中 1 個直接使用 sorafenib）和 **8 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎細胞癌（Renal Cell Carcinoma，已核准適應症；資料來自本評估之機轉關聯性描述） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏完整登錄的作用機轉（MOA）資料。但根據本評估中機轉關聯性分析的描述，Sorafenib 是多重酪氨酸激酶抑制劑，主要透過抑制 VEGFR（血管內皮生長因子受體）與 PDGFR（血小板衍生生長因子受體）介導的腫瘤血管新生，並透過 RAF-MEK-ERK 訊息傳遞路徑抑制部分腫瘤細胞增生。

Sorafenib 已核准用於腎細胞癌等血管新生依賴性腫瘤的治療。軟組織肉瘤（含脂肪肉瘤）在生物學上同樣具有明顯的血管新生依賴特性，這使得 sorafenib 的抗血管新生機轉在機轉層面上可能延伸適用。

事實上，sorafenib（原始代號 BAY 43-9006）曾直接於晚期軟組織肉瘤（含脂肪肉瘤亞型）進行 Phase 2 臨床試驗並完成收案，這進一步支持了 TxGNN 模型預測的合理性，而非僅為理論推論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | 完成 | 51 | BAY-9006（即 sorafenib 原始代號）直接用於晚期軟組織肉瘤（含脂肪肉瘤亞型），透過阻斷腫瘤生長所需酵素及血管新生發揮抗腫瘤作用 |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | 完成 | 131 | SARC024 研究測試口服 regorafenib（sorafenib 之衍生藥物，非同一分子）於多種肉瘤亞型；為類比證據，非直接以 sorafenib 進行 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | RCT | Cancer | SWOG S0505 Phase 2 試驗評估 sorafenib 於晚期軟組織肉瘤之療效，此族群治療選項有限 |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 Trial | Ann Surg Oncol | 新輔助放療併用 sorafenib 治療局部晚期肢體軟組織肉瘤之 I 期試驗，顯示抗血管新生療法與放療併用具協同效果 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 回顧肉瘤患者衍生異種移植（PDOX）模型，探討合併療法（含激酶抑制劑）之臨床應用潛力 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar onkologia | 依組織學亞型回顧軟組織肉瘤藥物治療現況，含標靶藥物角色 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 依組織學及非組織學導向探討軟組織肉瘤治療策略 |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib 於去分化脂肪肉瘤（LS141、DDLS）等細胞株中抑制生長及 MAPK 訊息傳遞 |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Cohort (Xenograft/Preclinical) | Am J Pathol | 去分化脂肪肉瘤異種移植模型顯示 PTEN 下降為惡性標記，並對 PI3K 路徑抑制有反應 |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case Report（非 sorafenib） | Anti-cancer drugs | Trabectedin（非 sorafenib）於滑膜肉瘤肺轉移個案之治療反應，僅供肉瘤治療背景參考 |

---

## 香港上市資訊

目前無香港上市許可證登記（market status: 未上市，total licenses: 0）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多重酪氨酸激酶抑制劑，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Sorafenib 本身（BAY 43-9006）已於一項 Phase 2 試驗（51 人，完成）直接測試於含脂肪肉瘤亞型之晚期軟組織肉瘤，另有一項 SWOG Phase 2 RCT 支持其於軟組織肉瘤的療效，機轉上與已核准之抗血管新生適應症一致，構成 L2 等級證據，足以支持在防護措施下進一步評估。

**若要推進需要：**
- 補齊 TFDA／原廠仿單警語與禁忌症資料（目前為 Blocking 等級資料缺口，無法完成 S1 安全性初評）
- 補齊完整作用機轉（MOA）文獻，強化機轉關聯性分析
- 針對脂肪肉瘤亞型（而非泛軟組織肉瘤）設計專屬臨床試驗
- 評估香港上市或引進計畫（目前完全未上市，0 張許可證）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

