---
layout: default
title: Obinutuzumab
parent: 高證據等級 (L1-L2)
nav_order: 634
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-14
description: "Obinutuzumab：預測新適應症為濾泡性淋巴瘤 (Follicular Lymphoma)（證據等級 L1）。原適應症：急性淋巴性白血病、Richter 症候群"
---

# Obinutuzumab
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

# Obinutuzumab：從急性淋巴性白血病／Richter 症候群到濾泡性淋巴瘤

## 一句話總結

Obinutuzumab 是一種醣基工程化的第二型抗 CD20 單株抗體，資料中記載的原適應症為急性淋巴性白血病與 Richter 症候群。
TxGNN 模型預測它可能對**濾泡性淋巴瘤 (Follicular Lymphoma)** 有效，目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向（其中包含多項隨機對照試驗）。
需要注意：濾泡性淋巴瘤其實是 obinutuzumab 已確立的治療領域，此預測較接近「補足資料庫中適應症標示的缺口」，而非全新的藥物再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴性白血病、Richter 症候群（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 濾泡性淋巴瘤 (Follicular Lymphoma) |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料欄位，但從已知文獻可知，obinutuzumab 是人源化、醣基工程化的第二型抗 CD20 IgG1 單株抗體，相較於 rituximab，能增強抗體依賴性細胞毒性（ADCC）、吞噬作用，並直接誘導 B 細胞死亡。

濾泡性淋巴瘤是 CD20 陽性的 B 細胞惡性腫瘤，藥物靶點與疾病生物學直接吻合。原適應症（B 細胞來源的白血病／淋巴增生疾病）與濾泡性淋巴瘤同屬 B 細胞惡性腫瘤，因此機轉上高度相關。

此外，所提供的文獻顯示 obinutuzumab 在濾泡性淋巴瘤已有關鍵性隨機試驗（如 GALLIUM），代表輸入資料中的適應症欄位並不完整，而不是發現了全新用途。

另有兩個預測（CLL/SLL 的分子亞型，分數同為 99.21%）僅有模型預測、沒有試驗或文獻，且屬於已核准的 CLL/SLL 適應症之子分類，對再利用評估的參考價值有限，故本報告以濾泡性淋巴瘤為主。

---

## 臨床試驗證據

資料中共有 40 個相關試驗，以下列出最相關的 10 個（優先選擇相關性評級高、與 obinutuzumab 直接相關者）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | 進行中（不再招募） | 799 | Zanubrutinib + obinutuzumab 對比 lenalidomide + rituximab，用於復發／難治性濾泡性或邊緣區淋巴瘤 |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | 完成 | 96 | Obinutuzumab + lenalidomide 用於未治療的濾泡性淋巴瘤 |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | 完成 | 114 | Obinutuzumab 短時間輸注（約 90 分鐘）的安全性與可行性，非比較療效 |
| [NCT05169658](https://clinicaltrials.gov/study/NCT05169658) | Phase 2 | 完成 | 42 | 皮下 mosunetuzumab ± polatuzumab 與 obinutuzumab 用於未治療的惰性 B 細胞淋巴瘤（探索性） |
| [NCT05387616](https://clinicaltrials.gov/study/NCT05387616) | Phase 2 | 狀態未知 | 98 | Copanlisib + obinutuzumab 免化療組合，用於高腫瘤負荷的未治療濾泡性淋巴瘤 |
| [NCT00825149](https://clinicaltrials.gov/study/NCT00825149) | Phase 1 | 完成 | 137 | Obinutuzumab 合併 CHOP、FC 或 bendamustine 的早期安全性與療效 |
| [NCT02391545](https://clinicaltrials.gov/study/NCT02391545) | Phase 1b/2 | 提前終止 | 55 | Duvelisib 合併 rituximab 或 obinutuzumab；因提前終止，證據有限 |
| [NCT04889716](https://clinicaltrials.gov/study/NCT04889716) | Phase 2 | 進行中（不再招募） | 23 | CD19 CAR-T 後接 mosunetuzumab 或 glofitamab + obinutuzumab；obinutuzumab 非主軸 |
| [NCT07126678](https://clinicaltrials.gov/study/NCT07126678) | NA | 招募中 | 15 | Zanubrutinib、bendamustine、obinutuzumab 固定療程，樣本小、尚無結果 |
| [NCT04796922](https://clinicaltrials.gov/study/NCT04796922) | Phase 3 | 已撤回 | 0 | Parsaclisib 合併 rituximab 或 obinutuzumab；未收案，無證據貢獻 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM 研究：obinutuzumab 對比 rituximab 合併化療，用於未治療濾泡性淋巴瘤；分析化療骨架對療效與安全性的影響（1,202 名患者） |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM 最終分析：先前主要分析顯示 obinutuzumab 組的無惡化存活期（PFS）優於 rituximab 組 |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT（Phase 2） | J Clin Oncol | ROSEWOOD：zanubrutinib + obinutuzumab 對比 obinutuzumab 單用，用於復發／難治性濾泡性淋巴瘤 |
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | 臨床試驗報告 | N Engl J Med | Obinutuzumab 與 rituximab 化學免疫療法用於初治晚期濾泡性淋巴瘤的比較 |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | 單臂 Phase 2 | Lancet Haematol | GALEN：obinutuzumab + lenalidomide 用於復發／難治性濾泡性淋巴瘤 |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Phase 1b/2 | Haematologica | Polatuzumab vedotin + bendamustine + rituximab 或 obinutuzumab 用於復發／難治性濾泡性淋巴瘤 |
| [38041532](https://pubmed.ncbi.nlm.nih.gov/38041532/) | 2024 | 系統性回顧／網絡統合分析 | Cancer | 初治晚期濾泡性淋巴瘤維持與鞏固治療策略的比較 |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncology | Obinutuzumab 用於 rituximab 難治或復發濾泡性淋巴瘤的回顧（含 GADOLIN 研究） |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Obinutuzumab 單用及合併治療濾泡性淋巴瘤的影響 |
| [41681868](https://pubmed.ncbi.nlm.nih.gov/41681868/) | 2026 | 治療指引 | Cancers | 西班牙淋巴瘤小組（GELTAMO）2025 濾泡性淋巴瘤診斷、治療與追蹤指引 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64100 | GAZYVA CONCENTRATE FOR SOLUTION FOR INFUSION 1000MG/40ML（廠商：ROCHE HONG KONG LIMITED） | 輸注用濃縮液 | 資料中未提供適應症文字 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 CD20 單株抗體），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單（文獻提示需留意血球低下，但本次資料未提供具體數據） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 建議監測 CBC（含分類）、B 型肝炎病毒狀態、感染徵象；輸注期間監測輸注反應 |
| 處置防護 | 請參考原廠仿單與院內抗體藥物處置規範 |

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 81 項交互作用，以下為部分主要項目：
  - 嚴重（Major）：Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib、Certolizumab pegol、Cladribine、Clozapine
  - 中度（Moderate）：Strontium chloride Sr-89、Roflumilast、Chloramphenicol、Zidovudine、Alemtuzumab、Azathioprine、Anakinra，以及多種疫苗（如破傷風類毒素、炭疽疫苗、霍亂活疫苗）
- **需特別留意的風險類別**（依藥物類別與研究判斷）：輸注相關反應、感染、血球低下、B 型肝炎再活化、進行性多灶性白質腦病（PML）。

警語與禁忌症的仿單內容尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 濾泡性淋巴瘤有多項隨機對照證據（GALLIUM 的 Phase 3 RCT、ROSEWOOD 的 Phase 2 RCT）及大量臨床試驗，機轉（CD20 靶向）也直接吻合，因此證據等級為 L1。
- 但這屬於已確立的適應症，並非真正的新用途，且香港許可證未提供適應症文字，需先釐清本地核准範圍。

**若要推進需要：**
- 取得香港仿單，確認核准適應症範圍（治療線別、合併藥物）與警語、禁忌症
- 補充作用機轉（MOA）資料
- 建立輸注反應、感染、血球低下、B 型肝炎再活化與 PML 的監測計畫
- 針對 81 項交互作用，特別是免疫抑制劑與疫苗，制定合併用藥審查流程
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

