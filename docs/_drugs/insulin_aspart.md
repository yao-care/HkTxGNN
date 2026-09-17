---
layout: default
title: Insulin Aspart
parent: 高證據等級 (L1-L2)
nav_order: 398
evidence_level: L1
indication_count: 5
---

# Insulin Aspart
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

# INSULIN ASPART：糖尿病既有用途確認與多重適應症探索性評估

## 一句話總結

Insulin Aspart（DB01306）是快速作用胰島素類似物，原本即用於糖尿病患者的血糖控制。
TxGNN 模型對此藥物共產出 5 個高分預測，其中排名第一的**第一型糖尿病 (Type 1 Diabetes Mellitus)** 分數高達 **99.95%**，但這實際上是胰島素既有的核心適應症、並非新用途；其餘 4 個預測（自體免疫性卵巢炎、opsismodysplasia、TRMA、永久性新生兒糖尿病）目前僅有機轉推論或極少量文獻支持，證據等級偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病（血糖控制），本評估包資料中未提供香港許可證上的正式適應症文字 |
| 預測新適應症 | 第一型糖尿病 (Type 1 Diabetes Mellitus)（註：屬既有核心用途，非新適應症） |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails（僅適用於「確認既有用途」情境） |

### 其他預測適應症一覽（因證據不足暫緩）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 2 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) | 99.92% | L5 | S0 | Hold |
| 3 | Opsismodysplasia | 99.59% | L5 | S0 | Hold |
| 4 | Thiamine-Responsive Dysfunction Syndrome (TRMA) | 99.57% | L5 | S0 | Hold |
| 5 | 永久性新生兒糖尿病 (Permanent Neonatal Diabetes Mellitus) | 99.55% | L3 | S2 | Research Question |

---

## 為什麼這個預測合理？

目前 DrugBank 未提供 Insulin Aspart 詳細的作用機轉資料（MOA 為資料缺口，優先度 High）。根據評估包內建的機轉分析與公開藥理學共識：Insulin Aspart 是快速作用胰島素類似物，透過直接補充內生性胰島素，替代第一型糖尿病患者因自體免疫破壞胰島 β 細胞而喪失的胰島素分泌功能。**這是胰島素的標準核心用途，TxGNN 給出的高分預測其實是在確認既有適應症，而非發現新的老藥新用機會。**

其餘 4 個預測則屬於探索性、機轉層面的推論：
- **永久性新生兒糖尿病**：病因多為 KATP 通道（KCNJ11/ABCC8）或胰島發育基因突變，外源性胰島素是標準支持療法之一，機轉與 T1D 補充療法相通，但新生兒族群的劑量與吸收動力學有其特殊性，缺乏 aspart 專屬前瞻性試驗（現有 L3 證據僅來自 1 篇綜述文獻）。
- **自體免疫性卵巢炎、Opsismodysplasia、TRMA**：無任何臨床試驗或文獻支持胰島素於這些疾病的治療角色，TxGNN 高分可能反映知識圖譜中的間接共病關聯（如自體免疫多腺體症候群、胰島素訊息傳導路徑分子重疊），屬純模型推論，尚無實證基礎。

---

## 臨床試驗證據

以下為第一型糖尿病相關性最高的 10 個試驗（依相關性 A > B 排序）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01773798](https://clinicaltrials.gov/study/NCT01773798) | Phase 1 | 完成 | 33 | Insulin degludec/aspart 於 T1D 之 PK/PD 特性研究 |
| [NCT06948760](https://clinicaltrials.gov/study/NCT06948760) | N/A | 完成 | 11 | 青少年 T1D 自動化胰島素輸注系統中快速作用胰島素轉換因子測試（Lyumjev vs Humalog/Novolog） |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Phase 2 | 完成 | 153 | GZR101 對照 Insulin degludec/aspart 於糖尿病之療效安全性比較 |
| [NCT04711382](https://clinicaltrials.gov/study/NCT04711382) | N/A | 完成 | 438 | Faster-acting aspart（Fiasp）於 T1D 真實世界多中心經驗（比利時） |
| [NCT01271517](https://clinicaltrials.gov/study/NCT01271517) | Phase 4 | 未知 | 120 | 長效胰島素類似物對兒童/青少年 T1D 代謝控制與內生胰島素保留之比較 |
| [NCT00675493](https://clinicaltrials.gov/study/NCT00675493) | N/A | 完成 | 942 | NovoMix 30（Biphasic Insulin Aspart 30）於羅馬尼亞 T1D/T2D 患者之觀察性研究 |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | 完成 | 598 | Insulin detemir + aspart 對比 NPH + 人類胰島素於 T1D 基礎-餐前方案 |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 完成 | 350 | Insulin degludec 對比 detemir，以 aspart 為餐前胰島素之兒童青少年 T1D 研究（BEGIN Young 1） |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | 完成 | 258 | 胰島素併 GLP-1RA/SGLT2i 對比基礎-餐前胰島素方案之血糖控制持久性研究 |
| [NCT02359617](https://clinicaltrials.gov/study/NCT02359617) | N/A | 完成 | 10 | 皮下注射部位連續血糖監測新型單埠治療方式評估 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6：每週一次 insulin icodec 對比每日一次 degludec，作為 T1D 基礎-餐前方案之一部分 |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT：Insulin degludec 對比 detemir（均併用 aspart）於妊娠合併 T1D 之非劣性試驗 |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT/系統性回顧 | Diabetes Metab | 快速作用 insulin aspart 對比一般人類胰島素於 T1D/T2D 之療效安全性系統性回顧 |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | 妊娠合併 T1D 之生活型態、藥物治療與新科技管理更新 |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | 第一型糖尿病總覽：自體免疫破壞胰島 β 細胞導致胰島素缺乏 |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treat Endocrinol | Insulin aspart 於 T1D/T2D 治療之焦點回顧 |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Insulin aspart 用於第一型與第二型糖尿病管理之回顧 |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vasc Health Risk Manag | Insulin degludec/aspart 複方用於 T1D 與 T2D 治療 |
| [30789066](https://pubmed.ncbi.nlm.nih.gov/30789066/) | 2019 | Review | Expert Opin Drug Metab Toxicol | Degludec/aspart 預混胰島素於 T1D 應用之回顧 |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Review | Expert Opin Pharmacother | Biphasic insulin aspart 30 用於 T1D 治療之實證回顧 |

---

## 香港上市資訊

目前查無 Insulin Aspart 於香港的許可證登記（market_status：未上市，總許可證數：0）。此結果尚未確認是資料缺口或真實未上市狀態，建議進一步查證衛生署藥物名冊。

---

## 安全性考量

安全性資訊（主要警語、禁忌症、藥物交互作用）目前均為資料缺口，且此缺口已被標記為 **Blocking** 等級——在取得 TFDA／衛生署仿單資料前，無法進行下一步安全性初評（S1）。安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅限「確認既有核心用途」情境；其餘 4 項探索性預測維持 Hold / Research Question）

**理由：**
- TxGNN 最高分預測（第一型糖尿病，99.95%，L1）實際上是 Insulin Aspart 已知的核心適應症，而非新的老藥新用機會，證據充分但無新增價值。
- 其餘 4 個預測（自體免疫性卵巢炎、Opsismodysplasia、TRMA 為 L5；永久性新生兒糖尿病為 L3）證據不足，僅永久性新生兒糖尿病有 1 篇綜述文獻支持，可列為研究問題持續追蹤，其他 3 項暫緩。

**若要推進需要：**
- 取得 TFDA/香港衛生署仿單警語與禁忌症資料（DG001，Blocking，直接卡關安全性初評）
- 補齊 DrugBank 作用機轉資料（DG002，High）
- 確認香港上市狀態是否為真實未上市或資料缺口
- 若欲推進「永久性新生兒糖尿病」方向，需取得 Insulin Aspart 專屬之前瞻性研究或病例系列證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

