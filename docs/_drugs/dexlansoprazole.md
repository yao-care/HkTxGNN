---
layout: default
title: Dexlansoprazole
parent: 高證據等級 (L1-L2)
nav_order: 267
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexlansoprazole：預測新適應症為活動性消化性潰瘍 (Active Peptic Ulcer Disease)（證據等級 L1）。原適應症：消化性潰瘍、胃食道逆流症、食道炎"
---

# Dexlansoprazole
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Dexlansoprazole：從消化性潰瘍／胃食道逆流到活動性消化性潰瘍

## 一句話總結

Dexlansoprazole 是質子幫浦抑制劑（PPI），原本用於消化性潰瘍、胃食道逆流症（GERD）及食道炎。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前有 **2 個相關的 Phase 3 臨床試驗**和 **3 篇文獻**支持這個方向。
需注意：此預測與原適應症高度重疊，並非真正的新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消化性潰瘍、胃食道逆流症、食道炎（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始資料未收錄）。根據已知資訊，Dexlansoprazole 是 PPI 類藥物，
透過不可逆地抑制胃壁細胞的 H+/K+-ATPase（質子幫浦）來減少胃酸分泌。

消化性潰瘍屬酸相關疾病，降低胃酸可讓潰瘍癒合。活動性消化性潰瘍與其原適應症（消化性潰瘍、GERD、食道炎）本就同屬酸相關疾病，因此預測在機轉上合理。

不過，目前登記的 Phase 3 試驗主要是**糜爛性食道炎**的癒合與維持研究，並非潰瘍癒合的直接終點，屬於透過共同的抑酸機轉提供的間接支持。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | 完成 | 2054 | Dexlansoprazole MR 60/90 mg 對比 Lansoprazole 30 mg，治療糜爛性食道炎 8 週的癒合效果 |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | 完成 | 2038 | 同上設計的姊妹試驗，評估糜爛性食道炎癒合 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統性回顧／網絡統合分析 | Am J Gastroenterol | 比較 P-CAB 與 PPI 治療 LA 分級 C/D 食道炎的療效與安全性 |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Review | Curr Opin Investig Drugs | 介紹 Dexlansoprazole 緩釋劑型用於逆流性食道炎的開發 |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | 前臨床／機轉研究 | J Chin Med Assoc | 探討 PPI 抑制液泡型 ATPase 與內質網壓力，及其與胃癌風險的可能關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61373 | DEXILANT DELAYED RELEASE CAPSULES 30MG（Takeda） | 延遲釋放膠囊 | 資料未載明 |
| HK-61372 | DEXILANT DELAYED RELEASE CAPSULES 60MG（Takeda） | 延遲釋放膠囊 | 資料未載明 |

## 安全性考量

- **知識圖譜標示的疾病關聯禁忌**（非仿單內容，僅供參考）：肝病、膽囊疾病、骨質疏鬆、停經後骨質疏鬆、骨折。
- **藥物交互作用**：共查詢到 100 筆，以下為部分重點：
  - 嚴重（Major）：Acalabrutinib、Atazanavir
  - 中度（Moderate）：Fosamprenavir、Foscarnet、Fostamatinib、Furosemide、Gefitinib、Hydrochlorothiazide、Bosutinib、Bumetanide 等
  - 輕微（Minor）：Acetylsalicylic acid、Axitinib、Brivaracetam、Cyanocobalamin

主要警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 個已完成的大型 Phase 3 RCT（超過 2000 人）支持其抑酸療效與安全性，且已在香港上市。但試驗終點為糜爛性食道炎，並非潰瘍癒合，且此適應症屬於原有用途範圍，不是真正的藥物再利用。

**若要推進需要：**
- 確認香港許可證核准的適應症文字，釐清是否已涵蓋消化性潰瘍
- 取得潰瘍癒合為主要終點的直接臨床證據（可關注進行中的 Phase 4 試驗 NCT07344506 之結果）
- 取得詳細的作用機轉資料及仿單的警語與禁忌症
- 針對肝病、骨質疏鬆／骨折風險族群及 Acalabrutinib、Atazanavir 等重大交互作用，制定用藥監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

