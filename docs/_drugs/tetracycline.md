---
layout: default
title: Tetracycline
parent: 僅模型預測 (L5)
nav_order: 738
evidence_level: L5
indication_count: 4
---

# Tetracycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tetracycline：老藥新用機會評估（4 項預測適應症）

## 一句話總結

Tetracycline (DB00759) 目前**未在香港上市**，無有效藥品許可證，原適應症資料亦未列於本次 Evidence Pack。TxGNN 針對此藥物產生 **4 個候選新適應症**，證據強度差異很大：其中「**慢性鼻竇炎 (Chronic Rhinosinusitis)**」有 **4 個臨床試驗**與 **20 篇文獻**支持，達到 L3／Research Question 等級；但這些證據幾乎全部針對同類藥 **doxycycline** 而非 tetracycline 本身，屬 class-effect 推論。其餘 3 項適應症僅有 1-2 篇個案報告或體外研究支持，證據等級 L4-L5，建議 Hold。

---

## 快速總覽

### 整體資訊

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供；tetracycline 為典型四環素類廣效抗生素原型藥物） |
| 作用機轉 (MOA) | **[Data Gap]** — 高優先度缺口，影響機轉關聯性分析（DG002） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold**（整體），慢性鼻竇炎方向列為 Research Question |

### 四項預測適應症比較

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Punctate epithelial keratoconjunctivitis（點狀角膜結膜炎） | 99.58% | L4 | S0 | Hold |
| 2 | Chronic ethmoidal sinusitis（慢性篩竇炎） | 99.15% | L4 | S0 | Hold |
| 3 | **Chronic rhinosinusitis（慢性鼻竇炎）** | 99.15% | **L3** | **S2** | **Research Question** |
| 4 | Paranasal sinus neoplasm（副鼻竇腫瘤） | 99.10% | L5 | S0 | Hold |

---

## 為什麼這些預測合理？

> 目前缺乏 tetracycline 詳細的作用機轉資料（MOA: [Data Gap]）。以下說明皆引用 Evidence Pack 中各候選適應症提供的 `repurposing_rationale`，而非另行推測。

**1. Punctate epithelial keratoconjunctivitis**
四環素類對披衣菌（*Chlamydia trachomatis*）具經典抗菌活性，理論上可用於披衣菌性濾泡性結膜炎後遺留的角膜病變；但唯一文獻僅描述疾病病程本身，並未評估 tetracycline 的治療效果。

**2. Chronic ethmoidal sinusitis**
四環素類兼具抗菌與 MMP 抑制之抗發炎作用，機轉上對慢性篩竇炎有理論基礎，但兩篇文獻分別為組織學研究與體外藥敏測試，均非臨床療效證據。

**3. Chronic rhinosinusitis（證據最強候選）**
四環素類（含 doxycycline）之 **MMP-9／發炎介質抑制** 與**抗菌雙重機轉**，是其在慢性鼻竇炎／鼻息肉治療中的作用基礎。但目前全部 4 項臨床試驗與多數文獻研究對象皆為 **doxycycline** 而非 tetracycline 本身——兩者雖同屬四環素類，但藥動學（組織穿透力、半衰期）與臨床劑量差異大，屬 **class-effect 推論**而非直接證據；且 tetracycline 本身「未上市」，需先確認取得可行性。

**4. Paranasal sinus neoplasm**
無明確抗腫瘤機轉關聯；唯一文獻描述的是篩竇手術後藥膏導致的硬化性脂肪肉芽腫併發症（不良反應個案），與治療腫瘤無關，判斷為 TxGNN 預測雜訊。

---

## 臨床試驗證據

**僅「慢性鼻竇炎」有臨床試驗登記；其餘 3 項適應症目前無相關臨床試驗登記。**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05157412](https://clinicaltrials.gov/study/NCT05157412) | Phase 3 | 完成 | 60 | Doxycycline 作為全身性類固醇輔助療法，用於中重度 CRSwNP，Grade B（同類藥證據） |
| [NCT01825408](https://clinicaltrials.gov/study/NCT01825408) | Phase 4 | 完成 | 40 | 評估 doxycycline 於最大醫療療程中的最適療程長短（3 vs 6 週），Grade B |
| [NCT01198912](https://clinicaltrials.gov/study/NCT01198912) | Phase 2 | 完成 | 33 | 評估長期低劑量口服 doxycycline 對內視鏡鼻竇手術後傷口癒合品質之影響，Grade B |
| [NCT02569437](https://clinicaltrials.gov/study/NCT02569437) | Phase 2 | **終止** | 49 | Doxycycline + 口服類固醇治療中重度 CRSwNP，因未完成證據力最弱，Grade C |

> ⚠️ 以上 4 個試驗研究藥物均為 **doxycycline**，非 tetracycline 直接證據。

---

## 文獻證據

**「慢性鼻竇炎」文獻證據（20 篇中列出前 10 篇，優先排序 RCT／系統性回顧）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36740870](https://pubmed.ncbi.nlm.nih.gov/36740870/) | 2023 | RCT | Am J Rhinol Allergy | Doxycycline 改善 CRSwNP 患者生活品質與嗅覺喪失（RCT） |
| [27113482](https://pubmed.ncbi.nlm.nih.gov/27113482/) | 2016 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 全身性/局部抗生素治療慢性鼻竇炎之系統性回顧 |
| [35919933](https://pubmed.ncbi.nlm.nih.gov/35919933/) | 2023 | 系統性回顧/統合分析 | J Laryngol Otol | Doxycycline 於慢性鼻竇炎管理角色之統合分析 |
| [38512383](https://pubmed.ncbi.nlm.nih.gov/38512383/) | 2024 | 統合分析 | Eur Arch Otorhinolaryngol | Doxycycline 與傳統療法治療難治性 CRSwNP 之比較 |
| [32278453](https://pubmed.ncbi.nlm.nih.gov/32278453/) | 2020 | 回顧 | Immunol Allergy Clin North Am | Macrolides 與 doxycycline 於慢性鼻竇炎之角色 |
| [39937440](https://pubmed.ncbi.nlm.nih.gov/39937440/) | 2025 | 回顧 | Curr Opin Allergy Clin Immunol | Doxycycline 治療 CRS 的優缺點評述 |
| [31126631](https://pubmed.ncbi.nlm.nih.gov/31126631/) | 2019 | 世代研究 | Am J Otolaryngol | Doxycycline 於 CRSwNP 管理中的角色 |
| [37437223](https://pubmed.ncbi.nlm.nih.gov/37437223/) | 2024 | 世代研究 | J Asthma | Doxycycline 在合併氣喘之 Type 2 CRSwNP 可能更有效 |
| [41186256](https://pubmed.ncbi.nlm.nih.gov/41186256/) | 2026 | 世代研究 | Int Forum Allergy Rhinol | 鼻竇手術後傷口癒合機轉及 doxycycline 改善效果 |
| [15563907](https://pubmed.ncbi.nlm.nih.gov/15563907/) | 2004 | 世代研究 | Otolaryngol Clin North Am | 慢性鼻竇炎與嗅覺功能障礙之背景文獻 |

**其他 3 項預測適應症文獻（各僅 1-2 篇，均為個案報告/體外研究）：**

| PMID | 適應症 | 年份 | 類型 | 主要發現 |
|------|--------|-----|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | Punctate epithelial keratoconjunctivitis | 1992 | 個案報告 | 披衣菌性濾泡性結膜炎緩解後續發之點狀角膜炎，非療效評估 |
| [9546260](https://pubmed.ncbi.nlm.nih.gov/9546260/) | Chronic ethmoidal sinusitis | 1998 | 組織學研究 | 慢性鼻竇炎篩骨組織形態計量分析（非臨床） |
| [16763410](https://pubmed.ncbi.nlm.nih.gov/16763410/) | Chronic ethmoidal sinusitis | 2006 | 體外藥敏 | 上頜/篩竇分離菌株之抗生素敏感性測試 |
| [8018240](https://pubmed.ncbi.nlm.nih.gov/8018240/) | Paranasal sinus neoplasm | 1994 | 個案報告(不良反應) | 篩竇手術後藥膏導致硬化性脂肪肉芽腫，與腫瘤治療無關 |

---

## 香港上市資訊

Tetracycline 目前**未在香港上市**，無許可證記錄（`total_licenses: 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **資料缺口提醒**：TFDA/香港仿單警語與禁忌症資料尚未取得（DG001，Blocking），此為進入 S1 安全性初評的必要前提，需先補齊才能進一步評估。

---

## 結論與下一步

**決策：Hold**（整體候選），慢性鼻竇炎方向列為 **Research Question**

**理由：**
- 4 項預測適應症中，僅「慢性鼻竇炎」有實質臨床試驗與系統性回顧支持（含 1 篇 Cochrane 回顧、1 篇 RCT），但全部證據對象為 doxycycline 而非 tetracycline，屬同類藥推論而非直接證據。
- 其餘 3 項適應症僅有零星個案報告或體外/組織學研究，未達可推進門檻。
- 藥品本身**未在香港上市**，且**仿單安全性資料為 Blocking 缺口**，尚無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking）
- 取得 tetracycline 明確作用機轉資料（DG002）
- 針對慢性鼻竇炎方向，尋找 tetracycline（而非 doxycycline）本身的直接臨床證據，或評估兩者藥動學/劑量換算之可比性
- 確認 tetracycline 在香港的上市/輸入可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

