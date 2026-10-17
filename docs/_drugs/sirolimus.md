---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 817
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sirolimus：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L5）。原適應症：腎細胞癌（非乳突、透明細胞型）、淋巴管平滑肌瘤病"
monitor_inn: "SIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma"]
---

# Sirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Sirolimus：從腎細胞癌／淋巴管平滑肌瘤病到脂肪肉瘤

## 一句話總結

Sirolimus 是 mTOR 抑制劑，原本與腎細胞癌、淋巴管平滑肌瘤病 (LAM) 相關。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，但目前只有 **1 個臨床試驗**（單臂 Phase 2、合併療法），文獻多為綜述，直接證據有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎細胞癌（非乳突、透明細胞型）、淋巴管平滑肌瘤病（來自知識圖譜的適應症關聯；香港許可證未載明適應症文字） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3（僅有 1 個單臂 Phase 2 試驗，非 RCT，其餘為綜述與個案；依規則未達 L2） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Sirolimus 抑制 mTORC1，而 PI3K/AKT/mTOR 路徑在軟組織肉瘤（包括脂肪肉瘤）中常被活化。這是預測合理的生物學基礎。

原適應症（腎細胞癌、LAM）同屬 mTOR 路徑相關腫瘤，與脂肪肉瘤在路徑層面有共通性。不過脂肪肉瘤常見 MDM2/CDK4 擴增，mTOR 抑制較可能是組合療法的搭配成分，而非單獨有效的機轉。

目前唯一的臨床試驗是 Sirolimus 合併 cyclophosphamide，難以把療效單獨歸因於 Sirolimus。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | 完成 | 70 | 單臂、多中心，評估 Sirolimus 合併 cyclophosphamide 用於轉移性或無法切除的黏液樣脂肪肉瘤與軟骨肉瘤。2014-06 至 2021-12 |

這個試驗為單臂設計且屬合併療法，也包含軟骨肉瘤，無法單獨評估 Sirolimus 對脂肪肉瘤的療效。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT（次要分析） | J Am Soc Nephrol | 腎移植患者提早停用 cyclosporine 並改以 Sirolimus 為主，可降低癌症風險，屬移植族群的癌症風險資料，非脂肪肉瘤療效 |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | 軟組織肉瘤新療法與分子特徵進展 |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | 晚期肉瘤的分子標靶藥物臨床試驗回顧 |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | 罕見結締組織腫瘤與肉瘤的標靶治療 |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | 腎移植長期免疫抑制患者的癌症篩檢，探討免疫抑制藥物與惡性腫瘤的關係 |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohort | Familial Cancer | PTEN 錯構瘤腫瘤症候群的臨床與基因型譜，與脂肪肉瘤僅間接相關 |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Case report | Diagn Pathol | 纖維脂肪血管異常 (FAVA) 三例，著重 mTOR 路徑，非脂肪肉瘤 |

這些文獻多為間接相關，沒有直接證明 Sirolimus 對脂肪肉瘤有效的研究。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50220 | RAPAMUNE TAB 1MG | 錠劑（依品名判斷） | 無登載資料 |
| HK-61049 | RAPAMUNE TAB 0.5MG | 錠劑（依品名判斷） | 無登載資料 |
| HK-67922 | RAPAMUNE ORAL SOLUTION 1MG/ML | 口服液劑（依品名判斷） | 無登載資料 |

三張許可證均為單方、有效，持證商為 PFIZER CORPORATION HONG KONG LIMITED。

---

## 細胞毒性

Sirolimus 的原適應症包含腎細胞癌，因此列出本章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（mTOR 抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；Sirolimus 通常需監測血藥濃度、血脂、腎功能與感染徵象 |
| 處置防護 | 請參考原廠仿單 |

若與 cyclophosphamide 等細胞毒性藥物合併，需另外考量該藥的骨髓抑制與處置防護要求。

---

## 安全性考量

- **禁忌症（知識圖譜關聯，非仿單原文）**：圖譜列出的相關疾病包括高血壓、腎臟疾病、肝臟疾病、高血糖／糖尿病、高三酸甘油酯血症／高脂血症、中風與腦血管疾病、間質性肺病、感染性疾病（含肺囊蟲肺炎、巨細胞病毒感染）、癌症、心包積液、進行性多灶性白質腦病等。
- **藥物交互作用**：共查得 100 筆。
  - 嚴重 (Major)：Amphotericin B（含脂質複合物劑型）、Mesalazine、Balsalazide、Clarithromycin。
  - 中度 (Moderate)：多種降血糖藥（Metformin、Pioglitazone、Acarbose、Alogliptin、Canagliflozin、Dapagliflozin、Chlorpropamide、Albiglutide）、皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone）、Aprepitant、Cimetidine。
  - Sirolimus 常與 CYP3A4／P-gp 受質或抑制劑發生交互作用，使用前需逐一審視。

仿單的正式警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 脂肪肉瘤僅有一個單臂、合併療法的 Phase 2 試驗，其餘為間接相關的綜述與個案，無法確認 Sirolimus 本身的貢獻。
- TxGNN 分數高 (99.89%)，但屬模型預測，需要更直接的證據才能推進。

**若要推進需要：**
- 取得 NCT02821507 的結果與脂肪肉瘤亞組的療效資料，確認試驗範圍與合併藥物。
- 設計或尋找 Sirolimus 單藥或隨機對照的脂肪肉瘤研究。
- 取得詳細作用機轉資料，並釐清 mTOR 抑制與 MDM2/CDK4 擴增的關係。
- 取得香港仿單的警語與禁忌症，完成安全性篩檢，並訂定藥物交互作用管理計畫。

**補充：**
- 同一份預測清單中的「淋巴管平滑肌瘤病 (lymphangiomyoma)」對應 LAM，本來就是 Sirolimus 的原適應症，因此不屬於真正的藥物再利用發現。
- LAM 有已完成的 Phase 3 MILES 試驗 (NCT00414648, n=89) 支持，證據等級為 L1。該試驗顯示可穩定肺功能，但屬抑制性而非治癒性，停藥後療效可能消失。
- 若以 LAM 評估，建議為 Proceed with Guardrails，需持續監測感染、口腔黏膜炎、高血脂、蛋白尿與藥物交互作用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

