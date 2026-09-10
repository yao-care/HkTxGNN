---
layout: default
title: Mycophenolic Acid
parent: 中證據等級 (L3-L4)
nav_order: 513
evidence_level: L3
indication_count: 5
---

# Mycophenolic Acid
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# MYCOPHENOLIC ACID：從免疫抑制用藥到血紅蛋白病 (Hemoglobinopathy)

## 一句話總結

> MYCOPHENOLIC ACID（MPA，常見劑型為 mycophenolate mofetil, MMF）是一種 IMPDH 抑制劑，目前主要作為異體造血幹細胞移植（HSCT）後的標準免疫抑制／移植物抗宿主病（GVHD）預防用藥，香港未有正式上市許可證登記。
> TxGNN 模型預測它可能對**血紅蛋白病 (Hemoglobinopathy)**——如地中海貧血、鎌形血球病——的移植治療流程有效，
> 目前有 **27 個臨床試驗**和 **9 篇文獻**支持這個方向，但多數證據屬於「支持性用藥」而非直接治療機轉。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式登記資料（依證據脈絡推論為異體移植後免疫抑制／GVHD 預防用藥） |
| 預測新適應症 | 血紅蛋白病 (Hemoglobinopathy) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

DrugBank 未提供 MYCOPHENOLIC ACID 的正式作用機轉紀錄（Data Gap），以下說明整理自證據包中試驗與文獻脈絡的一致描述：MPA（MMF 之活性代謝物）是 IMPDH（次黃嘌呤核苷單磷酸脫氫酶）抑制劑，能阻斷淋巴球的 de novo purine 合成路徑，因而發揮免疫抑制作用。這是異體造血幹細胞移植（allo-HSCT）後預防 GVHD 的標準用藥之一，常與 tacrolimus、cyclosporine 或 abatacept 併用。

地中海貧血（thalassemia major）與鎌形血球病（sickle cell disease）等血紅蛋白病，目前唯一根治手段是 allo-HSCT。MPA 在此脈絡下並非直接治療血紅蛋白病本身的病因（單基因血紅素合成缺陷），而是作為移植流程中促進 mixed chimerism、降低排斥反應與 GVHD 的輔助免疫抑制劑——證據包中的機轉關聯明確，但屬於「支持性治療」而非「病因治療」，這也是本預測未被評為最高等級的主因。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04009525](https://clinicaltrials.gov/study/NCT04009525) | Phase 4 | 完成 | 823 | 地中海貧血 allo-HSCT 大型前瞻性多中心研究，評估移植根治療效 |
| [NCT00004485](https://clinicaltrials.gov/study/NCT00004485) | Phase 1/2 | 完成 | 50 | HLA 相合骨髓移植誘導穩定混合嵌合體，治療兒童鎌形血球病 |
| [NCT06872333](https://clinicaltrials.gov/study/NCT06872333) | Phase 2 | 招募中 | 62 | 高風險血紅蛋白病及紅血球輸血依賴疾病之異體 HSCT |
| [NCT01050855](https://clinicaltrials.gov/study/NCT01050855) | Phase 2 | 進行中（未招募） | 75 | 非惡性疾病減強度預處理方案，評估植入率與毒性 |
| [NCT03171831](https://clinicaltrials.gov/study/NCT03171831) | Phase 4 | 未知 | 30 | 單倍體 HSCT 治療重型地中海貧血之安全性與療效 |
| [NCT02867800](https://clinicaltrials.gov/study/NCT02867800) | Phase 1 | 完成 | 24 | Abatacept 併入標準 GVHD 預防方案（含 MMF），用於兒童鎌形血球病 |
| [NCT02776202](https://clinicaltrials.gov/study/NCT02776202) | Phase 2 | 未知 | 15 | HLA 相合手足供者減強度預處理骨髓移植治療重型鎌形血球病 |
| [NCT01350232](https://clinicaltrials.gov/study/NCT01350232) | NA | 已終止 | 2 | 減強度異體 HSCT 治療鎌形血球貧血，樣本數過小 |
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | 完成 | 10 | Abatacept 併用 cyclosporine 與 MMF 作為兒童非惡性疾病移植後 GVHD 預防 |
| [NCT01279616](https://clinicaltrials.gov/study/NCT01279616) | Phase 2 | 已終止 | 8 | 非親屬供者異體移植治療重型鎌形血球病之預處理方案 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | Review／族群藥動學 | Eur J Drug Metab Pharmacokinet | 建立地中海貧血兒童 HSCT 後 MMF 之族群藥動學模型，提出離標劑量建議 |
| [26860634](https://pubmed.ncbi.nlm.nih.gov/26860634/) | 2016 | Cohort | Biol Blood Marrow Transplant | 替代供者 HSCT 併用移植後 cyclophosphamide 治療非惡性疾病 |
| [36372358](https://pubmed.ncbi.nlm.nih.gov/36372358/) | 2023 | Cohort | Transplant Cell Ther | MMF 加強免疫抑制以維持地中海貧血移植後混合嵌合體 |
| [18940682](https://pubmed.ncbi.nlm.nih.gov/18940682/) | 2008 | Cohort | Biol Blood Marrow Transplant | 減強度 HSCT 用於鎌形血球病，長期穩定供者植入 |
| [28578010](https://pubmed.ncbi.nlm.nih.gov/28578010/) | 2017 | Cohort（Phase 1） | Biol Blood Marrow Transplant | 減強度預處理臍帶血移植治療鎌形血球病之 Phase 1 結果 |
| [29061531](https://pubmed.ncbi.nlm.nih.gov/29061531/) | 2018 | Cohort | Biol Blood Marrow Transplant | 非親屬供者移植併用移植後 cyclophosphamide 及 MMF 治療重型鎌形血球病 |
| [17454192](https://pubmed.ncbi.nlm.nih.gov/17454192/) | 2007 | Cohort（併發症分析，非 MMF 特異） | Hematology | ABO 不相合異體 HSCT 後純紅血球再生不良之風險因子分析 |
| [17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/) | 2007 | Case report（安全性警訊） | J Perinatol | 孕期使用 MMF 個案報告，新生兒發生嚴重貧血與水腫 |
| [15126382](https://pubmed.ncbi.nlm.nih.gov/15126382/) | 2004 | Commentary（關聯性低） | Genetics | 遺傳學與醫學交會之評論文章，與本適應症直接關聯性低 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。

證據包標記 TFDA／衛生當局仿單警語與禁忌症資料為 **Blocking 等級缺口（DG001）**，目前無法完成 S1 安全性初評。文獻中另有一則個案報告（PMID 17180133）提示孕期使用 MMF 可能造成新生兒貧血與水腫，屬已知安全性訊號，建議納入後續風險評估。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個 Phase 2/4 世代研究與大型前瞻性試驗支持 MMF 作為血紅蛋白病（地中海貧血、鎌形血球病）根治性 HSCT 流程中的標準 GVHD 預防／免疫抑制用藥，證據等級達 L3。
- 但此關聯屬「支持性用藥」而非直接病因治療，且原廠 MOA（DG002）與仿單安全性資料（DG001，Blocking）皆缺失，須補齊後才能完整評估。

**若要推進需要：**
- 取得 TFDA／衛生當局官方仿單警語與禁忌症資料（DG001，Blocking，方法：下載仿單 PDF 並解析）
- 查詢 DrugBank API 取得正式作用機轉資料，強化機轉關聯性分析（DG002）
- 釐清此候選為「移植輔助用藥」定位還是可獨立申請之適應症，以決定後續開發路徑
- 追蹤香港上市／許可證現況（目前 0 張許可證，未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

