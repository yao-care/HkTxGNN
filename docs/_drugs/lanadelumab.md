---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
---

# Lanadelumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lanadelumab：從原適應症（許可證未載明）到 C1 抑制劑缺乏症

## 一句話總結

Lanadelumab（商品名 Takhzyro）是一種抑制血漿激肽釋放酶的單株抗體，香港已有 1 張許可證，但許可證資料未載明核准適應症。
TxGNN 模型預測它可能對 **C1 抑制劑缺乏症 (C1 inhibitor deficiency)** 有效。
目前有 **23 個臨床試驗**和 **20 篇文獻**支持，其中包含 1 個 Phase 3 隨機、雙盲、安慰劑對照試驗（HELP）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | C1 抑制劑缺乏症 (C1 inhibitor deficiency) |
| TxGNN 預測分數 | 99.996% |
| 證據等級 | L2（見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

證據等級說明：依本報告的判定規則，完成的 Phase 3 隨機對照試驗只有 HELP 一個，其餘 Phase 3 為開放標籤或單臂試驗，因此判為 L2。Evidence Pack 內部評分為 L1，兩者有落差。

---

## 為什麼這個預測合理？

Lanadelumab 是完全人源化的單株抗體，專一抑制血漿激肽釋放酶 (plasma kallikrein)。
C1 抑制劑缺乏（SERPING1 基因功能喪失或功能異常）時，激肽釋放酶的活性失去控制，會產生過量的緩激肽 (bradykinin)。緩激肽是造成血管性水腫發作的主要介質。

Lanadelumab 直接阻斷這條路徑，從源頭減少緩激肽生成。因此機轉與疾病的致病路徑高度吻合，這也是預測分數極高的合理原因。

其餘 9 個預測疾病（如 serpinopathy、胰臟炎、Glanzmann 血小板無力症等）都沒有臨床試驗或文獻，機轉關聯薄弱或不存在，建議一律 Hold，本報告不展開。

---

## 臨床試驗證據

以下依相關性挑選 10 個試驗（共 23 個）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | 完成 | 125 | HELP 試驗：多中心、隨機、雙盲、安慰劑對照，評估預防第 I/II 型 HAE 急性發作的療效與安全性，為關鍵證據 |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | 完成 | 212 | HELP 延伸試驗：開放標籤，評估長期安全性與預防發作的療效 |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | 完成 | 21 | SPRING 試驗：2 至未滿 12 歲兒童，評估安全性、藥動學、藥效學 |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | 完成 | 12 | 日本受試者開放標籤試驗，評估療效與安全性 |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | 完成 | 20 | 中國受試者開放標籤試驗，治療 26 週，評估安全性、藥動學與療效 |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | 完成 | 73 | 長期安全性與療效試驗，對象為 C1-INH 正常的非組織胺性血管性水腫（與 C1-INH 缺乏族群不同，僅供參考） |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | 完成 | 140 | ENABLE：真實世界研究，比較使用前後的 HAE 發作次數 |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | 完成 | 168 | EMPOWER：美加觀察性研究，比較開始治療前後的發作率 |
| [NCT04861090](https://clinicaltrials.gov/study/NCT04861090) | N/A | 完成 | 207 | 回溯性病歷回顧，評估真實世界中的無發作比例 |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | N/A | 完成 | 155 | 日本上市後使用成績調查，長期用藥的副作用與症狀改善 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab 與安慰劑比較，預防 HAE 發作的隨機臨床試驗（HELP 試驗結果） |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | 開放標籤延伸試驗 | Allergy | HELP OLE：評估 12 歲以上第 1/2 型 HAE 的長期療效與安全性 |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | 系統性回顧 | Clin Rev Allergy Immunol | 整理接受長期預防治療的 HAE 患者仍發生發作的比例與特徵 |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | 網絡統合分析 | Drugs R D | 間接比較 garadacimab、lanadelumab、皮下 C1INH、berotralstat 等長期預防藥物 |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | 間接治療比較 | J Comp Eff Res | 12 歲以下兒童 HAE，比較 lanadelumab 與 C1 酯酶抑制劑的療效與安全性 |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | 觀察性研究 | J Allergy Clin Immunol Pract | INTEGRATED：多國真實世界療效研究 |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | 回顧 lanadelumab 的前臨床與 Phase I 研究，說明其抑制激肽釋放酶的機轉 |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | N Engl J Med | 遺傳性血管性水腫的綜述 |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case series | J Allergy Clin Immunol Pract | Lanadelumab 用於後天性 C1 抑制劑缺乏血管性水腫的療效 |
| [36379410](https://pubmed.ncbi.nlm.nih.gov/36379410/) | 2023 | 臨床報告 | J Allergy Clin Immunol Pract | 同樣探討 lanadelumab 在後天性 C1 抑制劑缺乏血管性水腫的療效 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-67123 | TAKHZYRO SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 300MG/2ML | 注射液（預充填針筒） | Takeda Pharmaceuticals (Hong Kong) Limited |

---

## 安全性考量

安全性資訊請參考原廠仿單。

目前查無藥物交互作用資料。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉與 C1 抑制劑缺乏的致病路徑直接對應，且有 HELP 這個 Phase 3 隨機對照試驗，加上多個 Phase 3 延伸試驗與各國真實世界研究支持。
- 香港的核准適應症與仿單警語目前缺漏，無法完成安全性篩選，因此需保留防護條件。

**若要推進需要：**
- 取得香港衞生署的仿單，確認核准適應症、警語與禁忌症。
- 查證香港許可證的適應症是否已涵蓋 C1 抑制劑缺乏相關的遺傳性血管性水腫預防。
- 後天性 C1 抑制劑缺乏目前僅有病例系列證據，若要延伸此族群，需要更高等級的研究。
- 補齊詳細的作用機轉資料（DrugBank）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

