---
layout: default
title: Pazopanib
parent: 高證據等級 (L1-L2)
nav_order: 669
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Pazopanib：預測新適應症為脂肪肉瘤 (Liposarcoma)，為證據最完整的預測（證據等級 L2）。原適應症：腎細胞癌、軟組織肉瘤"
monitor_inn: "PAZOPANIB"
predicted_indications: ["liposarcoma"]
---

# Pazopanib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

## Pazopanib：從腎細胞癌與軟組織肉瘤到脂肪肉瘤
{: .text-alpha }

## 一句話總結

Pazopanib 是多標靶酪胺酸激酶抑制劑，原本用於腎細胞癌與軟組織肉瘤。
TxGNN 模型的預測結果中，**脂肪肉瘤 (Liposarcoma)** 是證據最完整的方向，目前有 **6 個臨床試驗**和 **20 篇文獻**支持，其中包含一項專門針對脂肪肉瘤的 Phase 2 試驗。
其他預測（如未分類腎細胞癌）證據較少，其餘多數僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎細胞癌、軟組織肉瘤（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma)，為證據最完整的預測 |
| TxGNN 預測分數 | 99.59% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails |

**說明：** 預測排名第 1 的是「與神經母細胞瘤相關的腎細胞癌」（分數 99.63%），但目前沒有任何試驗或文獻，證據等級為 L5，建議 Hold。本報告以證據最完整的脂肪肉瘤為主軸。

### 其他預測適應症一覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 與神經母細胞瘤相關的腎細胞癌 | 99.63% | L5 | Hold |
| 2 | 未分類腎細胞癌 | 99.63% | L3 | Research Question |
| 3 | Xp11.2 易位／TFE3 基因融合相關腎細胞癌 | 99.63% | L5 | Hold |
| 4 | 脂肪肉瘤 | 99.59% | L2 | Proceed with Guardrails |
| 5 | 兒童腎細胞癌 | 99.54% | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Pazopanib 是多標靶 VEGFR／PDGFR／c-Kit 酪胺酸激酶抑制劑，透過抑制血管新生與腫瘤生長訊號發揮作用，其在腎細胞癌與非脂肪細胞性軟組織肉瘤中的療效已被證實。

脂肪肉瘤同屬軟組織肉瘤，血管新生與 PDGFR 訊號與腫瘤生長有關，因此機轉上可能適用。不過，脂肪肉瘤當初被排除在關鍵的 PALETTE Phase 3 試驗之外，目前證據主要來自 Phase 2 研究。文獻也強調軟組織肉瘤應依組織亞型選擇治療，藥效具有亞型依賴性。另有前臨床研究（患者來源異種移植小鼠模型）顯示，具 PDGFRA 擴增的多形性脂肪肉瘤對 Pazopanib 有反應。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | 完成 | 42 | 單藥 Pazopanib 用於無法切除或轉移性脂肪肉瘤，直接針對此適應症 |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | 完成 | 52 | 單藥 Pazopanib 用於復發之晚期／轉移性脂肪肉瘤，評估活性與耐受性 |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | 完成 | 140 | 隨機分派，術前放化療或放療加／不加 Pazopanib，用於非橫紋肌肉瘤軟組織肉瘤 |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | 完成 | 54 | 雙盲隨機，Gemcitabine 加／不加 Pazopanib，用於難治性軟組織肉瘤 |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | 完成 | 178 | Pazopanib 併用口服 Topotecan，用於轉移性軟組織與骨肉瘤 |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | 招募中 | 139 | 非橫紋肌肉瘤軟組織肉瘤的風險適應性研究，含維持性 Pazopanib，僅間接相關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 試驗報告 | Expert Opin Investig Drugs | Pazopanib 用於晚期中高度惡性脂肪肉瘤，脂肪肉瘤缺乏有效治療 |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | 評論 | Lancet Oncol | 評論 Pazopanib 用於晚期脂肪肉瘤 |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | 臨床試驗 | Br J Cancer | Pazopanib 併用口服 Topotecan 用於轉移性軟組織與骨肉瘤 |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncol Res Treat | 晚期脂肪肉瘤現有與實驗性全身治療選項 |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Curr Treat Options Oncol | 去分化脂肪肉瘤的全身治療選項 |
| [28547734](https://pubmed.ncbi.nlm.nih.gov/28547734/) | 2017 | 評論 | Adv Ther | 軟組織肉瘤中 Pazopanib、Trabectedin、Eribulin 的最佳使用建議 |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | 前臨床 | Tissue Cell | PDGFRA 擴增的多形性脂肪肉瘤異種移植模型中，Pazopanib 使腫瘤退縮 |
| [27918201](https://pubmed.ncbi.nlm.nih.gov/27918201/) | 2017 | Review | Future Oncol | 晚期軟組織肉瘤依組織亞型治療的重要性 |
| [36890471](https://pubmed.ncbi.nlm.nih.gov/36890471/) | 2023 | 試驗計畫書 | BMC Cancer | JCOG1802：比較 Trabectedin、Eribulin、Pazopanib 作為二線治療的隨機 Phase 2 |
| [27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/) | 2016 | Review | Cancer | 軟組織肉瘤化療總覽 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62096 | VOTRIENT TAB 200MG (SPAIN)（Novartis） | 未載明 | 未載明 |
| HK-67932 | VOTRIENT TABLETS 200MG（Novartis） | 未載明 | 未載明 |
| HK-68611 | PAZOPANIB TEVA TABLETS 200MG（Teva） | 未載明 | 未載明 |
| HK-68625 | PAZOPANIB SANDOZ TABLETS 200MG（Sandoz） | 未載明 | 未載明 |
| HK-68006 | TYKIPAZ TABLETS 200MG（Lotus） | 未載明 | 未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑），非傳統細胞毒性化療 |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 肝功能（知識圖譜顯示肝衰竭、藥物性肝損傷為禁忌相關疾病）、血壓、心電圖 QT 間期、甲狀腺功能、尿蛋白、電解質（鉀、鈣、磷） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

目前缺乏香港仿單的警語與禁忌文字，以下為知識圖譜與交互作用資料庫的資訊，並非仿單內容，僅供參考：

- **知識圖譜標示的禁忌相關疾病：**
  - 心血管：高血壓、長 QT 症候群（含家族性）、尖端扭轉型心律不整、心肌梗塞、冠狀動脈血栓
  - 肝臟：肝衰竭、藥物性肝損傷、高膽紅素血症（含吉爾伯特症候群）
  - 內分泌與代謝：甲狀腺功能低下、黏液水腫、低鉀、高鈣、腎鈣質沉著症、磷代謝異常
  - 其他：血紅蛋白病、腹瀉、活動性消化性潰瘍、腦內出血、胰臟炎、蛋白尿
- **藥物交互作用：** 資料庫共 100 筆，以下為部分範例。
  - 重大 (Major)：制酸／抑酸藥類（Famotidine、Ranitidine、Cimetidine、Omeprazole、Esomeprazole、Rabeprazole、Dexlansoprazole）、Clarithromycin、Dolasetron
  - 中度 (Moderate)：Pioglitazone、Loperamide、Aprepitant、Dexamethasone、Budesonide、Bisacodyl、Saxagliptin、Eliglustat、氧化鎂等

其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（針對脂肪肉瘤）**

**理由：**
- 有專門針對脂肪肉瘤的完成 Phase 2 試驗（NCT01506596、NCT01692496）及對應文獻，另有數個軟組織肉瘤的 Phase 2 與 Phase 2/3 研究，證據等級為 L2。但脂肪肉瘤被排除在 PALETTE Phase 3 試驗之外，缺乏確證性 Phase 3 結果，且藥效具有亞型依賴性。
- 未分類腎細胞癌（L3）目前僅有回溯性研究與一項單臂 Phase 2，列為研究性問題；其他腎細胞癌亞型預測（神經母細胞瘤相關、Xp11.2/TFE3、兒童型）無任何試驗或文獻，建議 Hold。

**若要推進需要：**
- 取得並解析香港仿單，補齊警語、禁忌與核准適應症
- 補充 DrugBank 作用機轉資料
- 取得 NCT01506596 與 NCT01692496 的完整療效結果（PFS、ORR）及脂肪肉瘤各亞型（高分化／去分化、黏液樣、多形性）的反應差異
- 限定明確的目標族群，並建立肝毒性、血壓、QT 間期與甲狀腺功能的監測計畫
- 評估與抑酸藥類（PPI、H2 阻斷劑）等重大交互作用的處理方案
- 若考慮兒童腎細胞癌或罕見腎癌亞型，需另行收集專屬療效與兒童安全性、劑量資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

