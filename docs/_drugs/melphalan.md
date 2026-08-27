---
layout: default
title: Melphalan
parent: 中證據等級 (L3-L4)
nav_order: 400
evidence_level: L3
indication_count: 5
---

# Melphalan
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

# MELPHALAN：從（原適應症資料缺失）到性腺生殖細胞腫瘤

## 一句話總結

Melphalan（苯丙氨酸氮芥）是傳統烷化劑類化療藥物，本 Evidence Pack 未提供其原適應症的詳細登記資料。
TxGNN 模型預測它可能對**性腺生殖細胞腫瘤 (Gonadal Germ Cell Tumor)** 有效，
目前有 **8 個臨床試驗**和 **4 篇文獻**支持這個方向，但多數研究設計為 Phase 1/2 單臂試驗，尚無專屬此適應症的隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未收錄（本 Evidence Pack 無核准適應症資料；Melphalan 藥理上為苯丙氨酸氮芥類烷化劑） |
| 預測新適應症 | 性腺生殖細胞腫瘤 (Gonadal Germ Cell Tumor) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。根據已知資訊，Melphalan 是苯丙氨酸氮芥類烷化劑（alkylating agent），透過與 DNA 形成交聯而抑制腫瘤細胞分裂，是血液腫瘤與高劑量化療領域廣泛使用的細胞毒性藥物。

值得注意的是，文獻證據顯示 Melphalan（早期文獻中稱為 "sarcolysin"）自 1950-1970 年代即被用於治療睪丸精原細胞瘤 (seminoma) 及睪丸生殖細胞腫瘤（PMID 13392619、4270380、24913），顯示此次 TxGNN 的預測方向並非全新概念，而是呼應了歷史上已存在的臨床使用經驗。

在近代臨床試驗中，Melphalan 常作為高劑量化療合併自體幹細胞移植前置方案的組成藥物之一。其中 NCT00936936 專門針對「預後不良之復發性生殖細胞腫瘤」設計，第一階段化療即包含 gemcitabine、docetaxel、melphalan、carboplatin 四藥合併，第二階段接續 ifosfamide、carboplatin、etoposide，顯示 Melphalan 在此類腫瘤的救援性治療中具實質臨床角色，與 TxGNN 99.77% 的預測分數相符。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | 完成 | 64 | 兩階段高劑量化療（含 melphalan）用於預後不良之復發性生殖細胞腫瘤，並評估安全性 |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | 完成 | 25 | 遞增劑量 melphalan 併用自體周邊血幹細胞支持及 amifostine 細胞保護於癌症病人 |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | 完成 | 25 | Busulfan+Melphalan+Topotecan 高劑量化療後接自體造血幹細胞移植，用於晚期/復發腫瘤 |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | 完成 | 451 | 8 種不同高劑量化療方案（含 melphalan）合併自體移植，用於血液腫瘤及特定實體瘤 |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | 完成 | 174 | 不同高劑量化療方案（含/不含全身放療）於自體移植前使用，涵蓋血液腫瘤及實體瘤 |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | N/A | 完成 | 36 | 非骨髓清除式異體移植，前置方案採 melphalan+cladribine 或全淋巴照射 |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | 完成 | 6 | 鞘內注射 melphalan 治療復發性/持續性腫瘤性腦膜炎 |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | 終止 | 13 | Amifostine 細胞保護併自體幹細胞移植，用於高風險/復發小兒實體瘤及腦瘤 |

**註**：上述試驗多數非專門針對性腺生殖細胞腫瘤設計（僅 NCT00936936 直接相關），其餘為涵蓋多種腫瘤之高劑量化療/幹細胞移植前置方案研究，Melphalan 在其中作為方案組成成分之一。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Review | Oncology | 睪丸生殖細胞腫瘤化療回顧，涵蓋烷化劑類藥物角色 |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | The Urologic Clinics of North America | 精原細胞瘤 (Seminoma) 治療綜述 |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | 病例系列 | Voprosy onkologii | 以 sarcolysin（melphalan）治療睪丸精原細胞瘤及其轉移之臨床經驗 |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | 機轉研究 | Acta Unio Internationalis Contra Cancrum | 荷爾蒙及烷化劑類藥物對腦下垂體促濾泡功能之影響 |

**註**：以上文獻多為 1950-1970 年代之早期回顧或病例系列，摘要內容未完整收錄，尚無近代隨機對照試驗直接針對此適應症。

---

## 香港上市資訊

目前無香港上市許可證登記，Melphalan 未在本地上市（`market_status: 未上市`，許可證數 0）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Nitrogen Mustard 類烷化劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項（本 Evidence Pack 無 toxicity 資料；惟依藥物類別及臨床試驗設計普遍需搭配幹細胞救援研判，預期具顯著骨髓抑制風險） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | CBC（含白血球分類）、血小板、肝腎功能、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

安全性資訊請參考原廠仿單。本 Evidence Pack 標記 TFDA 仿單警語/禁忌症資料為 **Blocking** 等級缺口（DG001），目前無法完成安全性初評；藥物交互作用查詢亦無結果（`query_status: not_found`）。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 存在 Blocking 等級資料缺口（仿單警語與禁忌症未取得，DG001），依規則無法進入安全性初評（S1）。
- 性腺生殖細胞腫瘤此一預測適應症目前僅有 Phase 1/2 單臂試驗及早期回顧文獻支持，尚無完成之隨機對照試驗，證據等級僅達 L3；且藥物目前未於香港上市。

**若要推進需要：**
- 取得 TFDA／原廠仿單完整警語與禁忌症資料，解除 Blocking 缺口（DG001）
- 補充 DrugBank 作用機轉 (MOA) 資料，強化機轉關聯性分析（DG002）
- 針對性腺生殖細胞腫瘤設計或尋找專屬之前瞻性對照試驗以驗證療效
- 評估香港上市或恩慈療法（compassionate use）申請路徑之可行性

---

### 附錄：其他預測適應症一覽（供參考）

| 排名 | 預測適應症 | TxGNN 分數 | 臨床試驗數 | 文獻數 | 備註 |
|------|-----------|-----------|-----------|--------|------|
| 2 | Ovarian primitive germ cell tumor | 99.75% | 3 | 1 | 僅 1 篇病例報告直接相關，證據薄弱（近似 L4） |
| 3 | Choriocarcinoma of ovary | 99.74% | 0 | 0 | 無任何試驗或文獻證據（L5，僅模型預測） |
| 4 | Female breast carcinoma | 99.67% | 5 | 20 | 文獻中含多篇歷史 RCT（如 vinorelbine vs. melphalan、SWOG 輔助化療研究），證據相對充分，但需另立候選案評估 |
| 5 | Malignant non-epithelial tumor of ovary | 99.55% | 0 | 0 | 無任何試驗或文獻證據（L5，僅模型預測） |

> 排名 4（female breast carcinoma）證據量明顯較豐富，若後續資源允許，建議另立獨立評估報告深入分析。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

