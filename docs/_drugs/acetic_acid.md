---
layout: default
title: Acetic Acid
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 9
---

# Acetic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# 醋酸 (Acetic Acid)：從一般抗菌應用到感染後障礙

## 一句話總結

醋酸（Acetic Acid，DrugBank DB03166）是一種廣泛使用的有機弱酸，以其局部抗菌特性（透過降低 pH 值破壞細菌細胞膜）著稱，臨床上偶見於外耳道沖洗及傷口消毒製劑中，目前在香港無核准藥品許可證。
TxGNN 模型預測它最可能對**感染後障礙 (Post-Bacterial Disorder)** 有效，預測分數達 **99.98%**，
然而目前**無任何直接文獻**支持此方向，18 筆相關臨床試驗查詢結果與本適應症關聯性均低，整體證據等級為 **L5**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准藥品適應症記錄（具已知局部抗菌特性） |
| 預測新適應症 | 感染後障礙 (Post-Bacterial Disorder) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏醋酸詳細的作用機轉資料。就已知資訊而言，醋酸是一種有機弱酸（pKa ≈ 4.76），其抗菌機轉主要為降低局部微環境 pH 值，干擾細菌細胞膜完整性及 pH 依賴性酶功能，並可破壞生物膜結構。此機轉已於外耳道感染（Pseudomonas aeruginosa）及慢性傷口的局部應用中獲得初步臨床應用基礎。

然而，「感染後障礙」（Post-Bacterial Disorder）的病理核心並非活動性細菌感染，而是細菌感染消退後持續存在的免疫失調、組織損傷修復異常及殘留炎症反應。醋酸的酸性抗菌機轉與這類感染後免疫介導病理機轉之間存在根本的生物學差距。

TxGNN 模型的高分預測最可能來自知識圖譜中醋酸與「細菌感染相關節點」之間的拓撲鄰近性，屬圖譜結構推斷而非直接的藥理機轉支持。機轉關聯性評估為**極弱**，現階段不具備充分的科學依據推進此適應症。

---

## 臨床試驗證據

查詢共返回 18 筆臨床試驗，**無任何試驗直接研究醋酸用於感染後障礙**；相關性評級均為 B 級（邊緣相關）或 C 級（不相關），以下列出相關性最高的試驗供參：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05710094](https://clinicaltrials.gov/study/NCT05710094) | Phase 1 | 已完成 | 28 | 醋酸基底製劑 SoftOx Biofilm Eradicator 外用於慢性腿部傷口的安全性與耐受性評估；研究適應症為一般抗菌，與感染後障礙無直接對應 |
| [NCT03212729](https://clinicaltrials.gov/study/NCT03212729) | N/A | 已完成 | 10 | 光動力療法結合根管治療對根管持續性感染（E. faecalis、Candida sp.）的抗菌效果；研究主體為光動力療法，非醋酸 |
| [NCT05275647](https://clinicaltrials.gov/study/NCT05275647) | Phase 2 | 未知 | 75 | 低能量震波聯合肉毒桿菌素膀胱灌注治療難治性間質性膀胱炎；以非細菌性慢性骨盆腔疼痛為適應症 |
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | 已完成 | 126 | 蘋果醋（含醋酸）合併二甲雙胍 vs 單用二甲雙胍治療新診斷第 2 型糖尿病；適應症與感染後障礙完全不符 |

> ⚠️ **重要說明**：上述試驗均非針對感染後障礙設計，亦非以純醋酸為研究藥物。查詢結果反映搜尋演算法的廣義匹配，不代表醋酸對此適應症有效性的直接證據。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 附錄：預測清單中最具證據潛力的替代適應症

在本次 9 個預測適應症中，**第 9 位：體癬 (Tinea Corporis)** 具有目前最高的實際證據等級（**L3**），建議作為後續研究優先考量：

| 適應症 | TxGNN 分數 | 預測排名 | 證據等級 | 建議 |
|--------|-----------|---------|---------|------|
| Post-Bacterial Disorder（感染後障礙） | 99.98% | #1（全局 636） | L5 | Hold |
| Tinea Corporis（體癬） | 99.25% | #9（全局 12,326） | **L3** | **Research Question** |

體癬的支持依據包括：
- **機轉合理**：醋酸（pH ≈ 3–4）可抑制皮膚癬菌（*Trichophyton*、*Microsporum*、*Epidermophyton*）的 pH 依賴性酶功能及細胞膜完整性
- **RCT 文獻**：[PMID 37012894](https://pubmed.ncbi.nlm.nih.gov/37012894/)（2023，*Drug Metabolism and Personalized Therapy*）—Terminalia chebula 加醋（含醋酸）vs 特比萘芬 1% 乳膏治療體癬之非劣效性 RCT
- **歷史案例系列**：1946–1947 年稀醋酸治療頭癬（Tinea capitis）的三篇發表（PMID [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/)、[20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/)、[20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/)）
- **其他支持文獻**：醋浸泡用於甲癬/足癬的觀察性報告（PMID [28947288](https://pubmed.ncbi.nlm.nih.gov/28947288/)）

---

## 結論與下一步

**決策：Hold**（針對感染後障礙）

**理由：**
感染後障礙的病理機轉以免疫失調為核心，與醋酸的酸性抗菌機轉缺乏生物學上的關聯性；現有 18 筆臨床試驗查詢結果中，無一直接研究此適應症，亦無任何支持性文獻，整體僅達 L5（模型預測）等級，不符合進一步推進的門檻。

**若要推進需要：**
- 確立醋酸對感染後免疫失調的潛在機轉假說（基礎/體外研究）
- 補充完整 MOA 資料（查詢 DrugBank API，解決 DG002 資料缺口）
- 取得香港藥監局安全性資料（解決 DG001 Blocking 缺口）
- **優先考慮轉向評估 Rank 9（Tinea Corporis）**，此適應症具備 L3 等級證據及合理機轉，更具近期研究可行性

> ⚠️ 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證方可應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

