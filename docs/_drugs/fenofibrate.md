---
layout: default
title: Fenofibrate
parent: 中證據等級 (L3-L4)
nav_order: 312
evidence_level: L3
indication_count: 5
---

# Fenofibrate
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

# Fenofibrate：從高脂蛋白血症到同合子家族性高膽固醇血症

## 一句話總結

Fenofibrate 是 fibrate 類藥物，透過活化 PPARα 調節脂質代謝，主要用於治療高三酸甘油酯血症與混合型高脂蛋白血症。TxGNN 模型預測它可能對**同合子家族性高膽固醇血症（Homozygous Familial Hypercholesterolemia, HoFH）**有效，目前有 **11 篇文獻**支持這個方向，但尚無直接以 fenofibrate 為研究藥物的 HoFH 登記臨床試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高三酸甘油酯血症 / 混合型高脂蛋白血症（香港無核准許可證） |
| 預測新適應症 | 同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Fenofibrate 屬於 fibrate 類藥物，透過活化核轉錄因子 **PPARα（peroxisome proliferator-activated receptor alpha）**發揮多重降脂機轉（詳細 MOA 資料尚待補充，以下摘自現有文獻推論）：

- **上調 LPL**（脂蛋白脂酶）→ 加速分解 VLDL 與 chylomicron 中的三酸甘油酯
- **下調 ApoC-III**（LPL 內源性抑制劑）→ 進一步增強 TG 清除效率
- **增加肝臟脂肪酸 β-氧化** → 減少 VLDL 從頭合成
- **上調 ApoA-I / ApoA-II** → 提升 HDL 膽固醇水平

HoFH 的核心病理為 LDL receptor（LDLR）**完全缺失或嚴重缺陷**，導致血漿 LDL-C 居高不下（常見 > 500 mg/dL），造成極早期且嚴重的心血管疾病。Fenofibrate 雖不能直接修補 LDLR 缺陷，但可作為多藥聯合方案的**輔助角色**：

1. **降低殘餘 TG 負擔**：清除 VLDL/IDL 等 atherogenic 微粒，改善整體脂質譜
2. **改善次要心血管風險**：減少炎症指標（如 ICAM-1、MCP-1）、改善內皮功能
3. **聯合治療加成**：與 PCSK9 抑制劑（如 alirocumab）或 lomitapide 聯用時，可在 HoFH 主力藥物降低 LDL-C 之外，進一步優化 TG 和 HDL 指標

最直接的支持來自 1984 年的長期臨床研究（PMID 6593751）：22 例 Type II 高脂蛋白血症患者（含 1 名 HoFH 患者）接受 fenofibrate 300 mg/day 治療 4–12 個月，總膽固醇平均下降 22%、LDL-C 下降 24%，其中 HoFH 患者降幅最為顯著，支持此預測的生物合理性。

---

## 臨床試驗證據

目前無直接以 fenofibrate 為研究藥物的 HoFH 登記臨床試驗。以下試驗提供 HoFH 治療領域的背景脈絡：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 完成 | 18 | 評估 Alirocumab（PCSK9 抑制劑）於 8–17 歲 HoFH 兒童/青少年的 LDL-C 降低療效，顯示 HoFH 領域對輔助降脂治療的強烈需求（研究藥物非 fenofibrate） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | 臨床縱貫研究 | Pharmacological Research Communications | 22 例 Type II 高脂蛋白血症（含 1 名 HoFH）fenofibrate 300 mg/day 治療 4–12 個月；總膽固醇降 22%、LDL 降 24%，HoFH 患者降幅最大 |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | 藥動學研究 | Pharmacotherapy | Lomitapide（HoFH 核准藥物）與 fenofibrate 的藥物動力學交互作用研究，確認 fenofibrate 在 HoFH 多藥管理中的臨床使用情境 |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | 回顧 / 病例系列 | Internal Medicine Journal | HoFH 治療回顧：標準降脂藥物效果有限，新興療法（PCSK9i、mipomersen）及肝移植作為替代；確立了聯合藥物治療在 HoFH 的地位 |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | 回顧 | Annals of the New York Academy of Sciences | FH 兒童/青少年藥物治療回顧：fenofibrate 在減少 atherogenic 脂蛋白方面有效，列為選項之一 |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | 臨床實務指引 | Endocrine Practice | AACE/ACE 血脂異常與心血管疾病預防指引，涵蓋 fenofibrate 等非他汀類藥物在複雜高脂血症（包括家族性高膽固醇血症）中的地位 |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | 回顧 | Indian Heart Journal | 非他汀類降脂藥物最新綜述：fenofibrate 單藥最明確適應症為 TG > 500 mg/dL；在混合型血脂異常或他汀不耐患者中有補充價值 |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | 回顧 | Indian Heart Journal | LDL-C、他汀類藥物與 PCSK9 抑制劑回顧，討論嚴重高膽固醇血症（含 HoFH）的殘餘風險管理，提供聯合治療背景 |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | 回顧 | Current Atherosclerosis Reports | 妊娠期血脂異常管理回顧，討論 fibrate 類藥物使用限制，提供特殊族群安全性背景 |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | 藥物回顧 | Pharmacotherapy | Ezetimibe 膽固醇吸收抑制劑詳細評估；fenofibrate 作為比較對象，顯示在混合高脂血症聯合治療中的應用背景 |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | 藥物回顧 | Drugs | Atorvastatin 在高膽固醇血症及高三酸甘油酯血症的療效回顧，提供 HoFH 高強度降脂需求的對照背景 |

---

## 香港上市資訊

Fenofibrate 目前在香港**無核准藥品許可證登記**（香港衛生署藥物辦公室資料：0 張許可證）。如需使用，須透過特殊用藥申請途徑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 藥品警語、禁忌症及藥物交互作用資料目前尚缺（Data Gap DG001）。如需詳細資料，請至衛生署官網或原廠網站下載仿單 PDF 取得完整資訊。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
1984 年的直接臨床研究（PMID 6593751）提供了 fenofibrate 在 HoFH 患者中降脂效果的初步人體證據，多藥動學與回顧性文獻進一步支持其作為聯合治療輔助藥物的合理性。然而，目前缺乏針對 HoFH 適應症的 fenofibrate 專屬 Phase 2/3 RCT，整體證據主要為觀察性研究與文獻回顧（L3 等級），且香港目前無相關上市許可，臨床轉化需謹慎推進。

**若要推進需要：**
- 補充完整 MOA 資料（DrugBank DB01039 API 查詢，Data Gap DG002）
- 取得香港衛生署仿單或原廠安全性資料，補充警語與禁忌症（Data Gap DG001）
- 設計 fenofibrate 作為輔助藥物的 HoFH 聯合治療方案（與 PCSK9 抑制劑、lomitapide 的搭配評估）
- 評估香港特殊用藥申請（Named Patient / Hospital Authority 特別申請）可行性
- 若條件許可，考慮發起 Investigator-Initiated Trial（IIT），研究 fenofibrate 在 HoFH 標準治療基礎上的輔助效益
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

