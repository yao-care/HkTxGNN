---
layout: default
title: Clemastine
parent: 中證據等級 (L3-L4)
nav_order: 203
evidence_level: L3
indication_count: 6
---

# Clemastine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **6** 個
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

# Clemastine：從過敏性疾病到過敏性蕁麻疹

## 一句話總結

Clemastine 是第一代 H1 受體拮抗劑（抗組織胺），傳統上用於過敏性鼻炎與蕁麻疹等過敏症狀。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效，
目前有 **1 個相關性待確認的臨床試驗**和 **13 篇文獻**（多數為間接證據）支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未載明適應症文字） |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Clemastine 屬於第一代 H1 受體拮抗劑，其在過敏性疾病中的療效已有長期臨床使用歷史，機轉上適用於過敏性蕁麻疹。

蕁麻疹的風團與紅斑主要由肥大細胞釋放組織胺所驅動，H1 受體阻斷與病理機轉直接對應。因此，這項預測較接近「與現有用途一致或已成熟的用途」，而非全新的老藥新用。原適應症欄位為空，較可能是資料缺漏，不代表藥物先前沒有臨床使用。

證據等級定為 L3 而非 L2，是因為唯一的 Phase 2 試驗標題被截斷，無法確認介入藥物是 clemastine；支持文獻也多半在討論其他抗組織胺藥物。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01154361](https://clinicaltrials.gov/study/NCT01154361) | Phase 2 | 完成 | 未提供 | 以 icatibant 治療 ACE 抑制劑引起的血管性水腫，與接受標準療法（甲基培尼皮質醇 + clemastine）的歷史對照組比較；clemastine 僅為對照療法的一部分 |

此試驗與 clemastine 治療蕁麻疹的關聯性有限，升級證據等級前需先至 ClinicalTrials.gov 確認。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40055203](https://pubmed.ncbi.nlm.nih.gov/40055203/) | 2025 | Review | Naunyn-Schmiedeberg's Arch Pharmacol | 回顧 2015–2024 專利，指出 clemastine 傳統用於過敏性鼻炎與蕁麻疹，並有神經退化、心血管與癌症等新興應用 |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | acrivastine 回顧；在季節性過敏性鼻炎中療效與 clemastine 相近（間接證據） |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | loratadine 回顧；療效與 clemastine 等多種抗組織胺藥相當（間接證據） |
| [2523301](https://pubmed.ncbi.nlm.nih.gov/2523301/) | 1989 | Review | Drugs | loratadine 初步回顧；對過敏性鼻炎與慢性蕁麻疹有效（間接證據） |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Review | Z Hautkr | astemizole 全球試驗回顧；優於 clemastine 等傳統抗組織胺藥（間接證據） |
| [6119852](https://pubmed.ncbi.nlm.nih.gov/6119852/) | 1981 | 臨床研究 | Wis Med J | 病患對 clemastine fumarate 的評估，並與其他抗組織胺藥比較（無摘要） |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | 觀察性研究 | Asian Pac J Allergy Immunol | 泰國兒童蕁麻疹流行病學，非 clemastine 專屬 |
| [30838475](https://pubmed.ncbi.nlm.nih.gov/30838475/) | 2019 | 病例報告 | Drug Saf Case Rep | Tc-99m macrosalb 過敏性反應，病患接受 clemastine 與 prednisone 後康復 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49809 | CLEMASTINE TAB 1MG (CHIN TENG) | 未載明 | 未載明 |
| HK-50305 | ZEMIN TAB 1MG | 未載明 | 未載明 |

## 細胞毒性

本藥為抗組織胺藥，非抗腫瘤藥物，不適用。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
H1 阻斷與蕁麻疹的機轉直接吻合，且藥物已在香港上市、臨床使用歷史長，但缺乏直接以 clemastine 治療蕁麻疹的高品質試驗，現有證據多為其他抗組織胺藥的間接資料。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 確認 NCT01154361 的介入藥物與適應症（目前看來 clemastine 僅為對照療法）
- 補充作用機轉（MOA）資料
- 尋找 clemastine 直接用於蕁麻疹的對照試驗或系統性回顧

## 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 冷型蕁麻疹 (Cold Urticaria) | 99.95% | L4 | Research Question（有 1984 年 ketotifen 與 clemastine 雙盲交叉研究，屬間接證據） |
| 鼻腔疾病 (Nasal Cavity Disease) | 99.87% | L5 | Hold（分類過於籠統，需先縮小為過敏性鼻炎等具體疾病） |
| 急性喉咽炎 (Acute Laryngopharyngitis) | 99.84% | L5 | Hold（多為感染性，抗膽鹼作用的乾燥效果可能加重不適） |
| 頑固性異位性皮膚炎 (Recalcitrant Atopic Dermatitis) | 99.65% | L5 | Hold（組織胺非主要致病因子，無證據） |
| 異位性 IgE 反應性 (IgE Responsiveness, Atopic) | 99.54% | L5 | Hold（屬表型而非可治療適應症，可能是知識圖譜的假象） |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

