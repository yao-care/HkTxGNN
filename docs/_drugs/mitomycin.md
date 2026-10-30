---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 593
evidence_level: L5
indication_count: 10
monitor_inn: "MITOMYCIN"
predicted_indications: ["solid pseudopapillary carcinoma of pancreas", "osteoclastic giant cell tumor of pancreas", "pancreatic carcinoma with mixed differentiation", "pancreatic intraductal papillary-mucinous carcinoma", "mixed ductal-endocrine carcinoma of pancreas", "pancreatic signet ring cell adenocarcinoma", "undifferentiated pancreatic carcinoma", "malignant exocrine pancreas neoplasm", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
last_modified_at: 2026-10-30
description: "Mitomycin：預測新適應症為胰臟固態偽乳突癌（證據等級 L5）。原適應症：胰腺腺癌"
---

# Mitomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Mitomycin：從胰腺腺癌到胰臟固態偽乳突癌
{: .text-alpha }

## 一句話總結

Mitomycin 是一種細胞毒性抗腫瘤藥物，知識圖譜中記錄的相關疾病為胰腺腺癌 (pancreatic adenocarcinoma)。
TxGNN 模型預測它可能對**胰臟固態偽乳突癌 (solid pseudopapillary carcinoma of pancreas)** 有效，
但目前**沒有臨床試驗與直接相關文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胰腺腺癌（知識圖譜中記錄的關聯；香港許可證未提供核准適應症文字） |
| 預測新適應症 | 胰臟固態偽乳突癌 |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Mitomycin 一般被歸類為具 DNA 交聯作用的烷化類細胞毒性藥物，這是通用的藥理背景，並非本次資料中提供的 MOA 內容。

TxGNN 模型（深度學習）預測的前 10 名新適應症幾乎都是胰臟腫瘤的不同組織亞型，這些分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

就本預測而言，固態偽乳突腫瘤通常以手術處理，惡性潛能低，因此細胞毒性化療的理論基礎偏弱。這類預測應視為假說，而非可直接採用的新適應症。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

首位預測疾病（固態偽乳突癌）目前無相關文獻。

以下為同一批預測中其他胰臟腫瘤亞型的間接文獻，皆**未直接證實 mitomycin 對該疾病有效**：

| PMID | 年份 | 類型 | 期刊 | 關聯疾病與主要發現 |
|------|-----|------|------|---------|
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Case report | Pancreatology | 胰臟 IPMN 合併腹膜假黏液瘤，以腹腔內溫熱化療灌流處理；未顯示 mitomycin 用於胰臟病灶 |
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Review | Strahlenther Onkol | 導管型胰臟癌的輔助與術前放化療，屬原適應症相關，非針對 IPMN |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | 臨床研究（間接） | Nihon Geka Gakkai Zasshi | 胰臟癌切除後在免疫化療（含 mitomycin）基礎上加用 tamoxifen；重點在 tamoxifen，非 mitomycin 本身 |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Review | Bulletin du Cancer | 原發部位不明腫瘤的診斷與治療，屬間接資料 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67642 | ACCORD MITOMYCIN 2 POWDER FOR SOLUTION FOR INJECTION/INFUSION OR INTRAVESICAL USE 2MG | 未提供 | 未提供 |
| HK-67641 | ACCORD MITOMYCIN 10 POWDER FOR SOLUTION FOR INJECTION/INFUSION OR INTRAVESICAL USE 10MG | 未提供 | 未提供 |
| HK-66821 | MITONCO POWDER FOR SOLUTION FOR INJECTION 10MG | 未提供 | 未提供 |
| HK-67651 | MITOMYCIN FOR INJECTION USP 10MG | 未提供 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA 交聯烷化類） |
| 骨髓抑制風險 | 請參考原廠仿單；知識圖譜記錄的禁忌關聯包含血小板減少、白血球減少、貧血 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 一般應包含 CBC（含血小板）、腎功能；詳細項目請參考原廠仿單 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：腎臟疾病、膿尿輸尿管 (pyoureter)、血小板減少、凝血疾病、貧血、巨球性貧血、白血球減少、溶血性尿毒症候群（含典型型）、充血性心衰竭、心臟衰竭、口腔炎。
- **藥物交互作用**：共查得 100 筆，以下為已標示等級者：
  - 嚴重 (Major)：Deferiprone、Samarium (153Sm) lexidronam
  - 中度 (Moderate)：Palifermin、Strontium chloride Sr-89、Fostamatinib
  - 輕微 (Minor)：Levofloxacin
  - 其餘（如 Warfarin、Dexamethasone、Ondansetron 等）等級未定

正式的警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測，無任何直接針對固態偽乳突癌的臨床試驗或文獻，證據等級為 L5。
- 此腫瘤通常以手術處理且惡性潛能低，化療的理論基礎薄弱。

**若要推進需要：**
- 補齊 mitomycin 的作用機轉資料
- 取得香港仿單的核准適應症、警語與禁忌症
- 針對該腫瘤亞型的病例系列或臨床研究證據
- 評估是否應優先聚焦於與原適應症更接近的亞型（如胰臟印戒細胞腺癌，預測分數 0.9984），但同樣需先補充直接證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

