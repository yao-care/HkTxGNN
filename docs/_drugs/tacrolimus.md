---
layout: default
title: Tacrolimus
parent: 高證據等級 (L1-L2)
nav_order: 717
evidence_level: L1
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
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

# Tacrolimus：從器官移植免疫抑制到脂漏性皮膚炎

## 一句話總結

Tacrolimus 是全身性 calcineurin 抑制劑，臨床上廣泛用於器官移植後之免疫抑制（本證據包未提供香港核准適應症資料，此為業界公認之藥理用途）。
TxGNN 模型預測其外用劑型可能對**脂漏性皮膚炎 (Seborrheic Dermatitis)** 有效，
目前有 **2 個已完成的臨床試驗**（Phase 3 與 Phase 4）和 **20 篇相關文獻**支持這個方向。

> ⚠️ 本證據包中 `drug.original_moa`、`taiwan_regulatory.licenses`、`safety` 相關欄位均為 Data Gap，且 DG001（仿單警語/禁忌）被標記為 **Blocking**，代表尚無法完成安全性初評（S1）。以下報告嚴格依證據包內容撰寫，未逕行補入外部仿單資訊。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港無許可證資料（`taiwan_regulatory.licenses` 為空陣列，market_status 為未上市） |
| 預測新適應症 | 脂漏性皮膚炎 (Seborrheic Dermatitis) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

`drug.original_moa` 欄位標記為 Data Gap，證據包本身沒有提供 Tacrolimus 的作用機轉描述。不過在 `repurposing_rationale.mechanistic_link` 中，針對脂漏性皮膚炎的機轉關聯有明確說明：

> Tacrolimus 為 calcineurin 抑制劑，抑制 T 細胞活化與促發炎細胞激素（IL-2, IFN-γ）釋放，可降低脂漏性皮膚炎相關的發炎反應與 Malassezia 誘發之免疫失調，局部外用已有多項機轉相符之皮膚科文獻支持。

脂漏性皮膚炎與異位性皮膚炎（Tacrolimus 外用劑型 Protopic® 的經典適應症）同屬 T 細胞浸潤主導之慢性發炎性皮膚病，兩者在發炎路徑上高度重疊，這也是 TxGNN 在知識圖譜上能給出高分預測（99.26%）的合理基礎。多篇臨床試驗與文獻（見下方）已直接針對脂漏性皮膚炎測試 Tacrolimus 外用劑型的療效，支持這個機轉推論不僅止於理論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | 完成 | 120 | Protopic® 軟膏用於成人臉部重度脂漏性皮膚炎之維持治療，評估減少復發頻率與類固醇使用量 |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | 完成 | 104 | 每週 1-2 次主動式（proactive）使用 0.1% Tacrolimus 軟膏，評估維持成人臉部脂漏性皮膚炎緩解、降低惡化發生率之效果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Annals of Parasitology | 60 名脂漏性皮膚炎患者比較 Sertaconazole 2% 乳膏與 Tacrolimus 0.03% 乳膏之療效 |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Review (Cochrane) | Clin Exp Allergy | 濕疹外用抗發炎藥物之網絡統合分析，比較各類藥物相對療效與安全性 |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Cohort | Annals of Dermatology | 0.1% Tacrolimus 軟膏用於臉部脂漏性皮膚炎之維持治療研究 |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | 外用 Tacrolimus（Protopic）用於異位性皮膚炎及其他發炎性皮膚病之機轉與療效綜述 |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | 臉部脂漏性皮膚炎現況報告與治療展望 |
| [38576147](https://pubmed.ncbi.nlm.nih.gov/38576147/) | 2024 | Review | The Medical Letter | Roflumilast 泡沫劑（Zoryve）用於脂漏性皮膚炎之新藥評述，可作為 Tacrolimus 替代方案之對照參考 |
| [28685715](https://pubmed.ncbi.nlm.nih.gov/28685715/) | 2017 | Cohort | Chinese Medical Journal | 臉部脂漏性皮膚炎患者之高 Staphylococcus epidermidis 群落及皮膚屏障受損研究 |
| [16094289](https://pubmed.ncbi.nlm.nih.gov/16094289/) | 2005 | Cohort | Jpn J Med Mycol | 脂漏性皮膚炎與異位性皮膚炎患者之 Malassezia 菌種分析 |
| [20347654](https://pubmed.ncbi.nlm.nih.gov/20347654/) | 2010 | Case Report | Clinics in Dermatology | Tinea incognito 綜述，提及外用 Tacrolimus/Pimecrolimus 可能掩蓋皮癬菌感染臨床表現，需與脂漏性皮膚炎鑑別診斷 |
| [38809527](https://pubmed.ncbi.nlm.nih.gov/38809527/) | 2024 | Review | JAMA | 慢性搔癢症綜述，涵蓋發炎性皮膚病相關搔癢機轉與治療原則 |

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 2 個直接針對脂漏性皮膚炎的已完成臨床試驗（Phase 3、Phase 4，共 224 人），加上 1 篇 RCT 及多篇支持性文獻，證據等級達 L1，機轉關聯性（calcineurin 抑制 T 細胞路徑）具生物學合理性。
- 但香港目前**無 Tacrolimus 許可證上市**（`total_licenses = 0`），且安全性初評所需之仿單警語/禁忌資料（DG001）為 **Blocking** 等級缺口，代表本候選案尚未能進入 S1 安全性初評，「Proceed with Guardrails」須以取得下列資料為前提方可落地。

**若要推進需要：**
- 取得 TFDA／香港對應主管機關官方仿單，解析警語與禁忌症（DG001，Blocking，阻斷 S1 安全性初評）
- 補齊 DrugBank MOA 完整資料，用以強化機轉關聯性分析（DG002，High）
- 確認 Tacrolimus 外用劑型（軟膏）在香港之上市／引進計畫，因目前無許可證，臨床落地前需先解決法規上市路徑
- 補充藥物交互作用（DDI）查詢結果，目前 `query_status: not_found`
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

