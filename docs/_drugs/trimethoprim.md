---
layout: default
title: Trimethoprim
parent: 高證據等級 (L1-L2)
nav_order: 774
evidence_level: L1
indication_count: 2
---

# Trimethoprim
{: .fs-9 }

證據等級: **L1** | 預測適應症: **2** 個
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

# Trimethoprim：預測用於結膜炎（Conjunctivitis）

## 一句話總結

Trimethoprim 是一種抗菌藥物，機轉為抑制細菌二氫葉酸還原酶（DHFR）以阻斷葉酸合成路徑；此藥目前在香港未上市，亦無核准適應症登記紀錄。
TxGNN 模型預測它可能對**結膜炎 (Conjunctivitis)** 有效，
目前有 **3 個臨床試驗**（含 1 個直接相關的 Phase 4 RCT）與 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尚無登記資料（香港未上市，無核准適應症紀錄） |
| 預測新適應症 | 結膜炎 (Conjunctivitis) |
| TxGNN 預測分數 | 99.17% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

藥物層級的作用機轉資料目前為資料缺口（DG002），但針對「結膜炎」這項預測，證據包已提供具體的機轉關聯：Trimethoprim 抑制細菌二氫葉酸還原酶（DHFR），阻斷葉酸合成路徑，對結膜炎常見致病菌（*Haemophilus influenzae*、*Staphylococcus*、*Streptococcus* 等）具直接抗菌活性。

這並非單純的知識圖譜外推——Trimethoprim 與 polymyxin B 併用的眼用製劑（如 Polytrim）已是國際臨床常規用藥，用於治療細菌性結膜炎多年，機轉與適應症高度吻合。這也解釋了為何此項預測有實際的頭對頭臨床試驗（NCT00581542）與多篇歷史文獻支持。

需注意：同一份證據包中另有一項分數更高（99.57%）的預測——點狀上皮角結膜炎 (punctate epithelial keratoconjunctivitis)，但該適應症多與病毒性感染或角膜上皮損傷相關，與 trimethoprim 的抗菌機轉缺乏直接病理生理連結，且無任何臨床試驗或文獻佐證（L5，Hold），故本報告聚焦於證據等級較高的結膜炎預測。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | 完成 | 124 | 頭對頭比較 Polytrim（polymyxin B/trimethoprim）眼用溶液與 moxifloxacin 治療兒童結膜炎，直接相關 |
| [NCT00168532](https://clinicaltrials.gov/study/NCT00168532) | Phase 3 | 完成 | 218 | 麻疹感染預防性抗生素試驗，結膜炎為次要評估終點之一，間接相關 |
| [NCT03187834](https://clinicaltrials.gov/study/NCT03187834) | Phase 4 | 完成 | 252 | 抗生素抗藥性與腸道/鼻咽微生物體研究，非以結膜炎治療效果為主要終點 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | 比較 polymyxin B/trimethoprim 與 0.5% moxifloxacin 治療細菌性結膜炎的臨床起效速度 |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Cohort | Am J Ophthalmol | 評估含 trimethoprim 眼用製劑（併 polymyxin B ± sulfacetamide）治療細菌性結膜炎/瞼緣炎之療效與安全性 |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Cohort | Clin Ther | 兒童急性細菌性結膜炎使用 trimethoprim-polymyxin B 眼用溶液治療之調查結果 |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Review | J Pediatric Infect Dis Soc | 新生兒披衣菌結膜炎治療系統性回顧與統合分析，含口服 trimethoprim 等抗生素方案 |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review | J Pediatr Ophthalmol Strabismus | 探討細菌性結膜炎疫情控制，強調使用抗菌藥物縮短病程與傳染期 |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Review | Paediatr Child Health | 兒童急性感染性結膜炎之病因、臨床特徵與治療回顧 |
| [24892274](https://pubmed.ncbi.nlm.nih.gov/24892274/) | 2015 | Case Report | Ophthalmic Plast Reconstr Surg | 矽膠支架相關慢性結膜炎，培養出對 trimethoprim/sulfamethoxazole 敏感之 Nocardia nova |
| [34943657](https://pubmed.ncbi.nlm.nih.gov/34943657/) | 2021 | Pending | Antibiotics (Basel) | 台灣 MSSA 眼部感染之臨床特徵與分子特性分析 |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | 1999 | Case Report | Curr Opin Ophthalmol | 貓抓病之眼部表現，涵蓋相關結膜/淋巴腺症候群 |
| [8924168](https://pubmed.ncbi.nlm.nih.gov/8924168/) | 1996 | Review | Laryngorhinootologie | 貓抓病病因、臨床表現、診斷與治療概述 |

---

## 香港上市資訊

目前無許可證登記資料（香港未上市，`total_licenses` = 0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 資料缺口提醒：TFDA/HK 仿單警語與禁忌症資料（DG001）為 **Blocking** 等級缺口，尚無法完成 S1 安全性初評。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 結膜炎預測有 L1 等級證據支持，包含 1 個直接相關的完成 Phase 4 RCT（NCT00581542），且含 trimethoprim 的眼用複方製劑已是國際臨床常規用藥，機轉與適應症高度吻合。
- 另一項預測（點狀上皮角結膜炎，TxGNN 分數 99.57%）證據等級僅 L5，無臨床試驗或文獻支持，且機轉關聯性存疑，建議維持 Hold，不列入此階段推進範圍。

**若要推進需要：**
- 補齊 TFDA/HK 仿單警語與禁忌症資料（DG001，Blocking，來源：TFDA 官網仿單 PDF）
- 補齊藥物層級作用機轉（MOA）完整資料（DG002，來源：DrugBank API）
- 確認香港上市/引進路徑，目前無任何許可證登記
- 若欲評估點狀上皮角結膜炎適應症，需先補足臨床試驗與文獻證據，再重新進行機轉關聯性分析
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

