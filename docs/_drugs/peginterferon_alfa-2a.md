---
layout: default
title: Peginterferon Alfa-2A
parent: 高證據等級 (L1-L2)
nav_order: 567
evidence_level: L1
indication_count: 5
---

# Peginterferon Alfa-2A
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# PEGINTERFERON ALFA-2A：原適應症資料缺口 → B型肝炎病毒感染（TxGNN 預測強化）

## 一句話總結

Peginterferon Alfa-2a（DrugBank DB00008）目前在台灣尚未上市，原始核准適應症資料尚未建檔（TFDA 仿單資料缺口，DG001）。
TxGNN 模型預測它對**B型肝炎病毒感染（Hepatitis B Virus Infection）**有效，
且這並非全新假說——已有 **50 個臨床試驗紀錄**（含 1 個 Phase 3 Grade A 直接證據）與 **20 篇文獻**（含多篇 RCT、系統性回顧）支持 peginterferon alfa-2a 用於慢性 B 型肝炎治療。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未提供（Blocking 資料缺口，需查 TFDA 仿單，見 DG001） |
| 預測新適應症 | B型肝炎病毒感染 (Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L1 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

DrugBank 正式收錄的作用機轉欄位目前是資料缺口（DG002），但根據試驗與文獻證據可還原其機轉：Interferon alfa-2a 透過 JAK-STAT 路徑活化干擾素刺激基因（ISGs），抑制 HBV cccDNA 的轉錄活性，並增強宿主免疫系統清除 HBsAg 的能力。

值得注意的是，這項預測並非全新假說——peginterferon alfa-2a（原廠品名 Pegasys）在多數國家早已是慢性 B 型肝炎的既有核准適應症，只是在台灣尚未上市、也缺乏本地仿單資料。因此 TxGNN 的高分預測（99.94%）實質上反映的是「已在他國驗證、尚待引入本地市場」的成熟藥理學關聯性，而非機轉上的推測性延伸。

多筆大型 Phase 3/4 試驗與一篇 2005 年 NEJM 指標性 RCT（PMID 15987917）皆證實 peginterferon alfa-2a 對 HBeAg 陽性/陰性慢性 B 肝有明確療效，佐證此預測在機轉與臨床實證上均具合理性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01095835](https://clinicaltrials.gov/study/NCT01095835) | Phase 3 | 完成 | 131 | 40kD PEG-IFN 治療 HBeAg 陰性慢性B肝：48週 vs 96週療程比較，±lamivudine合併（Grade A 直接證據） |
| [NCT01011738](https://clinicaltrials.gov/study/NCT01011738) | N/A | 完成 | 1842 | 大型前瞻性觀察世代研究，探討 Pegasys 治療慢性B肝的療效預測因子 |
| [NCT02646189](https://clinicaltrials.gov/study/NCT02646189) | Phase 1/2 | 完成 | 12 | REP2139核酸聚合物合併 peginterferon 治療HBV感染之安全性與療效 |
| [NCT04412863](https://clinicaltrials.gov/study/NCT04412863) | Phase 2 | 完成 | 84 | VIR-2218 單用或合併 peginterferon alfa-2a 治療慢性HBV之安全性、PK與抗病毒活性 |
| [NCT01172392](https://clinicaltrials.gov/study/NCT01172392) | Phase 3 | 未知 | 185 | ANRS HB06 Pegan：NA治療達病毒學抑制之HBeAg陰性CHB病人加打48週PEG-IFN後，96週HBsAg清除率 |
| [NCT01706575](https://clinicaltrials.gov/study/NCT01706575) | Phase 2b | 完成 | 76 | NA治療穩定病人加用48週Pegasys對血清HBsAg的影響（HBeAg陰性、基因型D） |
| [NCT01373684](https://clinicaltrials.gov/study/NCT01373684) | Phase 4 | 完成 | 90 | PAS研究：PEG-IFN alfa-2a加用於NA治療中的HBeAg陰性CHB病人，觀察HBsAg下降幅度是否提升 |
| [NCT01086085](https://clinicaltrials.gov/study/NCT01086085) | Phase 4 | 完成 | 265 | 以反應導向療法(RGT)優化HBeAg陽性CHB病人之Pegasys治療方案 |
| [NCT00940485](https://clinicaltrials.gov/study/NCT00940485) | Phase 4 | 完成 | 200 | entecavir預治療後合併或序貫使用Pegasys，優化HBeAg血清轉換率 |
| [NCT06092333](https://clinicaltrials.gov/study/NCT06092333) | Phase 2 | 進行中 | 50 | 進行中的先導研究：VIR-2218合併peginterferon alfa-2a治療輕度/非活動性HBV感染 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | NEJM | 比較PegIFN alfa-2a單用、PegIFN+lamivudine合併、lamivudine單用治療HBeAg陽性慢性B肝之療效（指標性RCT） |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | 評估entecavir合併peginterferon alfa-2a於免疫耐受期成人CHB之安全性與療效 |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | RCT | Hepatology | 評估entecavir合併peginterferon於免疫耐受期兒童CHB病人之療效與安全性 |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | 系統性回顧/統合分析 | Antiviral Therapy | 個案資料統合分析，探討peginterferon alfa-2a於慢性B肝治療的最佳停藥規則 |
| [26700861](https://pubmed.ncbi.nlm.nih.gov/26700861/) | 2015 | Cohort/雙盲RCT | Virology Journal | 日本CHB患者接受PegIFN alfa-2a治療之長期療效雙盲隨機試驗 |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | 慢性B型肝炎感染之整體性回顧，涵蓋流行病學、自然病程與治療選項 |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nat Rev Gastroenterol Hepatol | B型肝炎治療目標與現行療法之回顧 |
| [16013986](https://pubmed.ncbi.nlm.nih.gov/16013986/) | 2005 | Review | Expert Opin Pharmacother | Peginterferon-alpha2a用於慢性B型肝炎治療之藥物療法專論 |
| [29689122](https://pubmed.ncbi.nlm.nih.gov/29689122/) | 2018 | Phase III RCT | Hepatology | PEG-B-ACTIVE (NCT01519960)研究：peginterferon alfa-2a治療3-18歲慢性B肝兒童之療效與安全性 |
| [41312046](https://pubmed.ncbi.nlm.nih.gov/41312046/) | 2025 | Review | Drug Des Devel Ther | 回顧peginterferon-α誘導慢性B肝「功能性治癒」於特殊族群之現況、挑戰與展望 |

## 台灣上市資訊

本藥品目前**未在台灣上市**，登記許可證數為 0，無可列出的許可證資料。此為進入下一階段安全性初評（S1）的阻礙項（DG001，Blocking）。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多筆 Phase 3/4 臨床試驗（含 Grade A 直接證據）與 2005 年 NEJM 指標性 RCT 一致支持 peginterferon alfa-2a 用於慢性 B 型肝炎治療，證據等級達 L1；但因藥物尚未在台灣上市，且 TFDA 仿單警語/禁忌症（DG001，Blocking）與正式 MOA 紀錄（DG002，High）均為資料缺口，需先補齊才能進入安全性初評（S1）。

**若要推進需要：**
- 取得 TFDA 仿單或國際仿單之完整警語與禁忌症資料（DG001）
- 補齊 DrugBank 正式 MOA 紀錄以利機轉關聯性分析（DG002）
- 若擬在台上市，需評估藥證申請與在地臨床試驗銜接
- 人工複核證據中標記 grade C／pending 的試驗，排除因 KG 鄰近節點造成的 HCV/HBV 混淆項
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

