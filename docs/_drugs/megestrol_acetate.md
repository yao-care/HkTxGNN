---
layout: default
title: Megestrol Acetate
parent: 高證據等級 (L1-L2)
nav_order: 558
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Megestrol Acetate：預測新適應症為子宮體子宮內膜癌 (Uterine Corpus Endometrial Carcinoma)（證據等級 L2）。原適應症：子宮內膜癌（Endometrial Carcinoma）"
monitor_inn: "MEGESTROL ACETATE"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma"]
---

# Megestrol Acetate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Megestrol Acetate：從子宮內膜癌到子宮體子宮內膜癌

## 一句話總結

Megestrol Acetate（醋酸甲地孕酮）是一種合成黃體素，原本用於子宮內膜癌治療。
TxGNN 模型預測它可能對**子宮體子宮內膜癌 (Uterine Corpus Endometrial Carcinoma)** 有效，
目前有 **1 個臨床試驗**支持這個方向，但此預測與原適應症本質上是同一種疾病，屬於既有用途的再確認，而非真正的新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 子宮內膜癌（Endometrial Carcinoma） |
| 預測新適應症 | 子宮體子宮內膜癌 (Uterine Corpus Endometrial Carcinoma) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

> 註：原適應症取自 TxGNN 知識圖譜的適應症資料；香港許可證資料中未載明核准適應症文字。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Megestrol Acetate 是合成黃體素（progestin），
對荷爾蒙受體陽性的子宮內膜腫瘤，黃體素作用是已確立的治療機轉。

預測的新適應症「子宮體子宮內膜癌」與原適應症「子宮內膜癌」基本上是同一種疾病，
因此這個預測較接近對既有用途的確認，而非跨疾病的再利用。

補充：此機轉說明來自一般藥理知識，並非提供資料中的 MOA 欄位，仍需以正式資料佐證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | 完成 | 73 | 隨機分派試驗，比較 Temsirolimus，或荷爾蒙治療（Megestrol Acetate 加 Tamoxifen）合併 Temsirolimus，用於晚期、持續或復發性子宮內膜癌 |

> 註：試驗標題不完整，各組別的實際組成需對照完整登記資料再確認。

## 文獻證據

針對預測新適應症（子宮體子宮內膜癌），目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60399 | MEGESIN TAB 160MG | 未載明 | 未載明 |
| HK-44293 | MEGAPLEX TAB 40MG | 未載明 | 未載明 |
| HK-68146 | MEGEJOHN TABLETS 40MG | 未載明 | 未載明 |
| HK-68644 | MEGESIA TABLETS 40MG | 未載明 | 未載明 |
| HK-42289 | APO-MEGESTROL TAB 40MG | 未載明 | 未載明 |

> 另有 1 張許可證（HK-44543，MEGAPLEX TAB 160MG），全部 6 張皆為有效的單一成分許可證。

## 細胞毒性

Megestrol Acetate 屬荷爾蒙治療藥物，不屬於傳統細胞毒性化療藥物。
請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜中標記的禁忌相關疾病**（來自 TxGNN 知識圖譜，非仿單文字）：高血壓、腎臟疾病、肝臟疾病、膽囊疾病、高血糖、糖尿病（含糖尿病酮酸中毒）、腎上腺皮質功能不全（Addison 病）、男性性腺功能低下、早發性停經、雄激素不敏感症候群等。
- **藥物交互作用**：共查得 100 筆，以下為部分中度交互作用：
  - 降血糖藥物：Acarbose、Metformin、Pioglitazone、Glimepiride、Repaglinide、Chlorpropamide
  - DPP-4 抑制劑與 GLP-1 類藥物：Alogliptin、Linagliptin、Saxagliptin、Sitagliptin、Albiglutide、Dulaglutide、Semaglutide
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin
  - 胰島素：Insulin aspart、Insulin degludec
  - 其他：Aprepitant、Clarithromycin

整體而言，併用降血糖藥物時應留意血糖變化。香港仿單的警語與禁忌資料尚未取得，其他安全性資訊請參考原廠仿單。

## 其他預測適應症

| 預測疾病 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|---------|-----------|---------|------|------|
| 子宮內膜移行細胞癌 | 99.94% | L5 | Hold | 罕見組織型，僅憑模型預測，無試驗或文獻 |
| 遺傳性乳癌卵巢癌症候群 | 99.89% | L5 | Hold | 無明確機轉依據，高分可能來自知識圖譜的鄰近關係 |
| 卵巢邊緣性上皮腫瘤 | 99.88% | L5 | Hold | 理論上可能表現荷爾蒙受體，但主要以手術處理，無證據 |
| 子宮癌肉瘤 | 99.84% | L4 | Research Question | 有間接文獻：[PMID 19767065](https://pubmed.ncbi.nlm.nih.gov/19767065/)（2009，世代研究，子宮肉瘤的荷爾蒙受體表現與治療角色）；[PMID 31157684](https://pubmed.ncbi.nlm.nih.gov/31157684/)（2020，病例報告，非直接使用 Megestrol） |

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 主要預測（子宮體子宮內膜癌）有 1 個已完成的 Phase 2 隨機試驗，證據等級為 L2，且與原適應症本質相同，屬既有用途的確認。
- 香港仿單的警語與禁忌資料尚缺，且藥物交互作用與知識圖譜標記的相關疾病（如糖尿病、高血壓、肝腎疾病）需審慎評估，因此建議附帶防護條件推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌
- 補充詳細作用機轉資料（MOA）
- 核對 NCT00729586 各組別組成及 Megestrol 組別的實際療效結果
- 針對糖尿病、高血壓、肝腎功能異常患者建立監測計畫
- 其他預測適應症（L4–L5）僅列為研究問題，不建議推進
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

