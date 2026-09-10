---
layout: default
title: Pazopanib
parent: 高證據等級 (L1-L2)
nav_order: 564
evidence_level: L2
indication_count: 5
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Pazopanib：從腎細胞癌到脂肪肉瘤

## 一句話總結

Pazopanib 是多標靶酪胺酸激酶抑制劑（作用於 VEGFR-1/2/3、PDGFR-α/β、c-Kit），國外已核准用於腎細胞癌與軟組織肉瘤治療，但**目前尚未在香港上市**（0 張許可證）。TxGNN 模型針對此藥共預測出 5 個候選新適應症，其中證據最扎實的是**脂肪肉瘤 (Liposarcoma)**——有 **9 個臨床試驗**（含多個直接針對脂肪肉瘤的 Phase 2 試驗）與 **20 篇文獻**支持，證據等級達 L2。其餘 4 個候選適應症（罕見腎癌亞型）證據等級僅 L3-L5，多屬機轉推論或無實證支持。

---

## 快速總覽

> 本次 Evidence Pack 為 pazopanib 的多候選適應症評估（TxGNN 共預測 5 項）。以下總覽以**證據等級最高、最具行動性**的脂肪肉瘤候選為主，其餘候選詳見文末「其他預測適應症」。

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎細胞癌（clear-cell RCC，國外核准適應症；香港無許可證資料） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.59%（模型排名 #7876） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉完整資料（DrugBank MOA 欄位為資料缺口）。根據 Evidence Pack 中的預測推論文字，pazopanib 已知是 VEGFR-1/2/3、PDGFR-α/β、c-Kit 的多標靶酪胺酸激酶抑制劑，其抗血管新生機轉已在 clear-cell RCC 中確立療效。

軟組織肉瘤（含脂肪肉瘤）的腫瘤生長高度依賴血管新生，且部分亞型（如去分化脂肪肉瘤）已被證實有 PDGFR 訊息路徑活化，與 pazopanib 的作用標靶直接相關。事實上，pazopanib（PALETTE 試驗）已核准用於非脂肪來源（non-adipocytic）軟組織肉瘤，但仿單明確排除脂肪肉瘤亞型——這正是 TxGNN 預測「脂肪肉瘤」的合理性所在：機轉相通、但目前藥證覆蓋範圍未涵蓋，屬於典型的適應症外擴（label-expansion）候選。多項針對脂肪肉瘤的獨立 Phase 2 試驗與異種移植模型研究也支持此方向。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | 完成 | 42 | 單藥 pazopanib 於無法手術/轉移性脂肪肉瘤之療效與安全性評估 |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | 完成 | 52 | 評估 pazopanib 於復發或無標準治療之晚期/轉移性脂肪肉瘤的活性與耐受性 |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | 完成 | 54 | 雙盲隨機試驗，gemcitabine ± pazopanib 用於頑固性軟組織肉瘤 |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | 完成 | 178 | pazopanib 併用口服 topotecan 用於轉移性/無法切除之軟組織及骨肉瘤 |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | 招募中 | 139 | 維持性 pazopanib 用於非橫紋肌肉瘤軟組織肉瘤（NRSTS）之風險分層試驗 |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | 進行中未招募 | 140 | 術前 pazopanib 併用化放療於 NRSTS 之隨機試驗 |
| [NCT06263231](https://clinicaltrials.gov/study/NCT06263231) | Phase 3 | 進行中未招募 | 333 | 評估瘤內注射藥物 vs 美國標準治療於軟組織肉瘤（pazopanib 角色需人工複核） |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | 完成 | 131 | 主要藥物為 regorafenib，非 pazopanib，相關性較低 |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | 完成 | 219 | 主要藥物為 regorafenib，非 pazopanib，僅間接支持 TKI 類藥物可行性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28832986](https://pubmed.ncbi.nlm.nih.gov/28832986/) | 2017 | 前瞻性 Phase 2 單臂試驗 | Cancer | 單藥 pazopanib 於無法手術/轉移性脂肪肉瘤患者之治療活性與安全性 |
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | 臨床研究報告 | Expert Opin Investig Drugs | 晚期中/高惡性度脂肪肉瘤使用 pazopanib 之療效總結 |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2 試驗 | British Journal of Cancer | pazopanib 併用口服 topotecan 顯著延長軟組織肉瘤之無惡化存活期 |
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | Phase 2 RCT（PAPAGEMO） | JAMA Oncology | pazopanib ± gemcitabine 用於蒽環類/ifosfamide 難治性軟組織肉瘤之終末結果 |
| [36890471](https://pubmed.ncbi.nlm.nih.gov/36890471/) | 2023 | Phase 2 RCT 研究計畫（JCOG1802） | BMC Cancer | 比較 trabectedin、eribulin、pazopanib 作為晚期軟組織肉瘤二線治療 |
| [25500074](https://pubmed.ncbi.nlm.nih.gov/25500074/) | 2014 | 轉譯研究 | Translational Oncology | pazopanib 於去分化脂肪肉瘤異種移植模型中透過抗血管新生抑制腫瘤生長 |
| [30889920](https://pubmed.ncbi.nlm.nih.gov/30889920/) | 2019 | 真實世界研究 | Medical Sciences | 北加州晚期軟組織/骨肉瘤患者使用 pazopanib 之真實世界經驗 |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | 回顧文獻 | Curr Treat Options Oncol | 去分化脂肪肉瘤全身性治療選項回顧，含 pazopanib 定位 |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | 回顧文獻 | Oncol Res Treat | 晚期脂肪肉瘤現有與實驗性全身治療選項總覽 |
| [28547734](https://pubmed.ncbi.nlm.nih.gov/28547734/) | 2017 | 回顧/專家意見 | Advances in Therapy | 軟組織肉瘤中 pazopanib、trabectedin、eribulin 之最佳使用建議 |

---

## 香港上市資訊

此藥物目前尚未在香港取得任何藥品許可證（`market_status: 未上市`，`total_licenses: 0`），無登記劑型或核准適應症資料可供列出。

---

## 細胞毒性

Pazopanib 屬抗腫瘤藥物（多國核准用於腎細胞癌、軟組織肉瘤），故列出以下細胞毒性相關資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑，作用於 VEGFR-1/2/3、PDGFR-α/β、c-Kit） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本 Evidence Pack 明確標記「TFDA/香港仿單警語與禁忌」為 **Blocking 級資料缺口**（DG001），目前無法完成 S1 安全性初評；藥物交互作用查詢亦無結果（`query_status: not_found`）。

---

## 其他預測適應症（證據較弱，僅供參考）

TxGNN 對 pazopanib 另預測以下 4 項罕見腎癌相關適應症，目前證據等級偏低，暫不建議推進：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|------|-----------|-----------|---------|------|------|
| 1 | 神經母細胞瘤相關腎細胞癌 | 99.63% | L5 | Hold | 極罕見亞型，無任何臨床試驗或文獻直接支持 |
| 2 | 未分類腎細胞癌 (Unclassified RCC) | 99.63% | L3 | Research Question | 1 個 Phase 3 試驗（主要比較藥為 sorafenib）+ 6 篇回顧性/世代研究文獻，缺乏前瞻性 RCT |
| 3 | Xp11.2 轉位/TFE3 融合基因相關 RCC | 99.63% | L5 | Hold | 純機轉推論，無臨床試驗或文獻證據 |
| 5 | 兒童腎細胞癌 | 99.54% | L4 | Hold | 僅有 1 個成人族群 Phase 3 試驗可間接外推，無兒童專屬資料 |

---

## 結論與下一步

**決策：Proceed with Guardrails**（適用於脂肪肉瘤候選；其餘 4 項候選適應症建議 Hold）

**理由：**
- 脂肪肉瘤候選有多個直接針對此適應症的完成期 Phase 2 試驗（NCT01506596、NCT01692496）及一項 Phase 2 RCT（PAPAGEMO），證據等級達 L2；但 pazopanib 現有 STS 藥證明確排除脂肪肉瘤亞型，故仍屬適應症外使用，需個案審慎評估。
- 其餘 4 項罕見腎癌候選證據薄弱（L3-L5），多為機轉推論或間接外推，不建議現階段投入資源。

**若要推進需要：**
- 補齊 TFDA/香港官方仿單警語與禁忌症資料（DG001，Blocking，目前無法完成安全性初評）
- 補齊完整作用機轉資料（DG002）
- 確認香港上市／輸入許可路徑（現況 0 張許可證）
- 藥物交互作用資料庫查詢重新執行（目前 `not_found`）
- 若欲推進「未分類腎細胞癌」候選，需針對該亞型另行系統性文獻回顧以補足前瞻性證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

