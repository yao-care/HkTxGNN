---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Everolimus：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L5）。原適應症：腎細胞癌、乳癌、腎血管平滑肌脂肪瘤、結節性硬化症等"
monitor_inn: "EVEROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Everolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Everolimus：從腎細胞癌到脂肪肉瘤

## 一句話總結

Everolimus 是 mTOR 抑制劑，原本用於腎細胞癌、乳癌、腎血管平滑肌脂肪瘤及結節性硬化症等適應症。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **1 個臨床試驗**和 **4 篇文獻**與這個方向相關，但其中僅 1 個試驗與 1 篇文獻直接針對此疾病，且皆為合併療法的研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎細胞癌、乳癌、腎血管平滑肌脂肪瘤、結節性硬化症等（依知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L2（保守判定，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold（列為研究問題，待更多證據） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 everolimus 屬於 mTOR 抑制劑，會抑制 mTORC1，而 mTORC1 位於 PI3K/AKT 訊號路徑的下游，與細胞增生和存活有關。

去分化脂肪肉瘤 (DDLPS) 的特徵是 MDM2/CDK4 擴增。同時抑制 CDK4/6（ribociclib）與 mTOR（everolimus），可同時阻斷平行的增生與存活路徑，並可能對抗單一藥物治療時出現的回饋活化與抗藥性。臨床前模型也顯示兩者合併有協同的生長抑制作用。極高的 TxGNN 分數與此生物學推論一致。

需要注意：此推論目前主要來自合併療法的研究，無法單獨確認 everolimus 本身的貢獻。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 進行中（不再收案） | 48 | Ribociclib 合併 everolimus 用於晚期去分化脂肪肉瘤 (DDL) 與平滑肌肉瘤 (LMS)，已接受過至少一線全身治療；評估抗腫瘤活性。預計 2026 年 12 月完成 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 試驗報告 | Clin Cancer Res | Ribociclib 合併 everolimus 用於晚期 DDL 與 LMS 的 Phase 2 研究；腫瘤模型中兩者有協同抑制作用 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 肉瘤患者來源原位異種移植 (PDOX) 模型與 CDK 抑制劑 palbociclib 的合併療法（非 everolimus 專屬） |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | 臨床前 | Oncogene | XPO1 抑制劑 KPT-330 在去分化脂肪肉瘤的作用（非 everolimus 專屬） |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 臨床前 | Anticancer Res | Eribulin 與不同機轉抗癌藥物的合併篩選（非 everolimus 專屬） |

## 香港上市資訊

香港共有 14 張有效的單一成分許可證，以下列出 5 張主要許可證。資料中未提供核准適應症文字與劑型。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59060 | AFINITOR TAB 5MG（Novartis） | — | — |
| HK-61710 | AFINITOR TABLETS 2.5MG（Novartis） | — | — |
| HK-59061 | AFINITOR TAB 10MG（Novartis） | — | — |
| HK-54335 | CERTICAN TAB 0.5MG（Novartis） | — | — |
| HK-68853 | EVEROLIMUS TEVA TABLETS 10MG（Teva） | — | — |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（mTOR 抑制劑） |
| 骨髓抑制風險 | 知識圖譜顯示與血小板減少、嗜中性球減少、白血球減少、貧血等相關，需留意 |
| 監測項目 | CBC（含分類）、肝腎功能、血糖、血脂 |

其餘（致吐性分級、處置防護）請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎的疾病**（來自藥物－疾病關聯，非仿單文字）：肝衰竭／肝病、腎病、血小板減少、嗜中性球減少、白血球減少、貧血、高血糖／糖尿病、高三酸甘油脂血症／高脂血症、間質性肺病、充血性心衰竭、心包積液、口腔炎、溶血性尿毒症候群等。
- **藥物交互作用**（共 100 筆，以下為主要者）：
  - 重大 (Major)：Amphotericin B、Aprepitant、Dexamethasone、Clarithromycin
  - 中度 (Moderate)：Metformin 及多種降血糖藥（如 Acarbose、Canagliflozin、Dapagliflozin、Empagliflozin、Glimepiride）、Cimetidine、Eliglustat、Eluxadoline 等

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 1 個單臂 Phase 2 合併療法試驗（ribociclib + everolimus）直接針對去分化脂肪肉瘤，尚未完成，且無法分離 everolimus 單藥的貢獻。形式上屬 L2，但因非隨機設計，證據力偏弱，故保守處理。
- 其他預測適應症（卵巢黏液樣脂肪肉瘤、隆突性皮膚纖維肉瘤、橫紋肌肉瘤等）幾乎沒有直接證據，僅為模型預測。

**若要推進需要：**
- 等待 NCT03114527 完成並取得療效與安全性結果
- 取得 everolimus 作用機轉資料與香港仿單的警語、禁忌與核准適應症
- 針對脂肪肉瘤亞型（尤其去分化型）設計隨機對照或單藥試驗
- 針對骨髓抑制、代謝異常及藥物交互作用制定監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

