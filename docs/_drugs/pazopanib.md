---
layout: default
title: Pazopanib
parent: 高證據等級 (L1-L2)
nav_order: 669
evidence_level: L2
indication_count: 6
monitor_inn: "PAZOPANIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "heart fibrosarcoma", "fibroblastic neoplasm", "kidney fibrosarcoma", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-10-23
description: "Pazopanib：預測新適應症為脂肪肉瘤 (liposarcoma)（證據等級 L2）。原適應症：本地許可證資料未記載適應症"
---

# Pazopanib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **6** 個
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

## Pazopanib: 脂肪肉瘤 (liposarcoma)
{: .text-alpha }

## 一句話總結

Pazopanib 是一種多標靶酪胺酸激酶抑制劑，知識圖譜中記錄的原適應症包括軟組織肉瘤與腎細胞癌。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **6 個臨床試驗**和 **20 篇文獻**支持這個方向，其中 2 個為直接針對脂肪肉瘤的單一藥物 Phase 2 試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 脂肪肉瘤 (liposarcoma) |
| TxGNN 預測分數 | 0.9959 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Proceed with Guardrails |

證據等級說明：有 2 個直接針對脂肪肉瘤的已完成單一藥物 Phase 2 試驗（NCT01506596、NCT01692496），但沒有已完成的 Phase 3 脂肪肉瘤專屬 RCT，因此判定為 L2，而非 L1。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據一般藥理知識，Pazopanib 是多標靶酪胺酸激酶抑制劑，作用於 VEGFR、PDGFR 與 c-Kit，具有抗血管新生與抗腫瘤特性。以下機轉推論來自一般知識，並非來自本報告彙整的 MOA 資料。

脂肪肉瘤屬軟組織肉瘤的一種亞型。此預測分數（0.9959）來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據。血管新生與 PDGFR 訊號被認為可能參與去分化及中高惡性度脂肪肉瘤的進展，因此機轉上合理。

需要留意的是，據彙整資料的機轉說明，Pazopanib 在軟組織肉瘤的標示適應症一般不包含脂肪肉瘤（依 PALETTE 試驗），所以脂肪肉瘤屬於需要額外驗證的新用途。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | 完成 | 42 | 單一藥物 Pazopanib 用於無法切除或轉移性脂肪肉瘤，評估療效與安全性（直接相關） |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | 完成 | 52 | 單一藥物 Pazopanib 用於標準治療後復發的晚期或轉移性脂肪肉瘤，評估活性與耐受性（直接相關） |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | 完成 | 178 | Pazopanib 併用口服 Topotecan 治療轉移性軟組織與骨肉瘤（併用設計，難以歸因） |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | 完成 | 140 | 術前放化療或放療加減 Pazopanib，用於非橫紋肌肉瘤軟組織肉瘤（脂肪肉瘤為其中子群） |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | 完成 | 54 | 雙盲隨機試驗，Gemcitabine 加或不加 Pazopanib，用於難治性軟組織肉瘤 |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | 招募中 | 139 | 非橫紋肌肉瘤軟組織肉瘤的風險分層研究，含 Pazopanib 維持治療（尚無結果） |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 試驗相關文獻 | Expert Opin Investig Drugs | Pazopanib 用於晚期中高惡性度脂肪肉瘤；脂肪肉瘤在晚期階段治療選擇有限 |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Phase 2 試驗評論 | Lancet Oncol | 針對晚期脂肪肉瘤使用 Pazopanib 的評論 |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2 | Br J Cancer | Pazopanib 併用口服 Topotecan 於轉移性軟組織與骨肉瘤 |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Curr Treat Options Oncol | 去分化脂肪肉瘤的全身性治療選項 |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncol Res Treat | 晚期脂肪肉瘤的既有與實驗性全身治療 |
| [27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/) | 2016 | Review | Cancer | 軟組織肉瘤化療概述 |
| [28547734](https://pubmed.ncbi.nlm.nih.gov/28547734/) | 2017 | 文獻 | Adv Ther | 提出 Pazopanib、Trabectedin、Eribulin 於軟組織肉瘤的最佳使用建議 |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | 前臨床 | Tissue Cell | 在 PDGFRA 擴增的多形性脂肪肉瘤小鼠模型中，Pazopanib 使抗 Doxorubicin 腫瘤縮小 |
| [36890471](https://pubmed.ncbi.nlm.nih.gov/36890471/) | 2023 | 試驗設計 | BMC Cancer | JCOG1802：Trabectedin、Eribulin、Pazopanib 於晚期軟組織肉瘤二線治療的隨機 Phase 2 |
| [37298520](https://pubmed.ncbi.nlm.nih.gov/37298520/) | 2023 | Review | Int J Mol Sci | 免疫治療時代的去分化脂肪肉瘤治療 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68611 | PAZOPANIB TEVA TABLETS 200MG | 未載明 | 未載明 |
| HK-68625 | PAZOPANIB SANDOZ TABLETS 200MG | 未載明 | 未載明 |
| HK-68006 | TYKIPAZ TABLETS 200MG | 未載明 | 未載明 |
| HK-62096 | VOTRIENT TAB 200MG (SPAIN) | 未載明 | 未載明 |
| HK-67932 | VOTRIENT TABLETS 200MG | 未載明 | 未載明 |

以上 5 張均為單一成分、有效狀態的許可證。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，非仿單內容）：高血壓、長 QT 症候群與尖端扭轉型心律不整、肝衰竭與藥物性肝損傷、甲狀腺低下、心肌梗塞、腦內出血、胰臟炎、蛋白尿、腹瀉類疾病、活動性消化性潰瘍、高膽紅素血症（含 Gilbert 症候群）等。
- **藥物交互作用**（共查得 100 筆，以下為部分）：
  - 重大 (Major)：Famotidine、Ranitidine、Cimetidine、Omeprazole、Esomeprazole、Rabeprazole、Dexlansoprazole（胃酸抑制劑類）、Clarithromycin、Dolasetron。
  - 中度 (Moderate)：Pioglitazone、Loperamide、Aprepitant、Dexamethasone、Budesonide、Bisacodyl、Magnesium oxide、Saxagliptin、Eliglustat。

其他警語與禁忌請參考原廠仿單。

## 其他預測適應症簡述

| 預測疾病 | TxGNN 分數 | 證據等級 | 說明 |
|---------|-----------|---------|------|
| 纖維母細胞腫瘤 | 0.9935 | L5 | 有孤立性纖維性腫瘤、骨外黏液樣軟骨肉瘤等單臂 Phase 2 資料；類別異質 |
| 隆突性皮膚纖維肉瘤 | 0.9929 | L2 | 有多中心 Phase 2 研究與病例報告，但 Imatinib 仍為標準標靶治療 |
| 卵巢黏液樣脂肪肉瘤 | 0.9951 | L5 | 僅有模型預測，無相關研究 |
| 心臟纖維肉瘤 | 0.9937 | L5 | 僅有模型預測，無相關研究 |
| 腎纖維肉瘤 | 0.9933 | L5 | 僅有模型預測，無相關研究 |

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 個直接針對脂肪肉瘤的已完成單一藥物 Phase 2 試驗，加上軟組織肉瘤的相關隨機試驗，方向有支持；但缺乏脂肪肉瘤專屬的 Phase 3 證據，且 Pazopanib 在軟組織肉瘤的標示一般不含脂肪肉瘤。
- 香港已有 5 張有效單一成分許可證，但資料中未載明核准適應症，也缺少仿單警語與禁忌。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌。
- 補充 DrugBank 作用機轉資料。
- 取得 NCT01506596 與 NCT01692496 的完整結果（無惡化存活率、客觀緩解率、安全性）。
- 建立監測計畫：血壓、肝功能、QT 間期、甲狀腺功能、尿蛋白，並審查與胃酸抑制劑等藥物的交互作用。
- 低證據的罕見預測（卵巢黏液樣脂肪肉瘤、心臟及腎纖維肉瘤）暫列 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

