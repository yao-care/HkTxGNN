---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
monitor_inn: "CIPROFLOXACIN"
predicted_indications: ["diffuse scleroderma", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-28
description: "Ciprofloxacin：預測新適應症為瀰漫性硬皮症 (diffuse scleroderma)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ciprofloxacin
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

## Ciprofloxacin：氟喹諾酮類抗菌藥 → 瀰漫性硬皮症 (diffuse scleroderma)
{: .text-alpha }

## 一句話總結

Ciprofloxacin 是氟喹諾酮類抗菌藥，在香港已有多張單方許可證上市。
TxGNN 模型預測它可能對**瀰漫性硬皮症 (diffuse scleroderma)** 有效，
目前**無已登記的臨床試驗**，僅有 **2 篇文獻**與此疾病相關，且均非對照性的確證研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 瀰漫性硬皮症 (diffuse scleroderma) |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ciprofloxacin 屬氟喹諾酮類抗菌藥，一般認為是透過抑制細菌 DNA 複製相關酵素而發揮抗菌作用，但這不是本次資料中直接記載的機轉。

就瀰漫性硬皮症而言，資料顯示有兩條可能的關聯路徑：
1. 有研究提出 ciprofloxacin 可能對皮膚具抗纖維化作用（PMID 20507401）。
2. 系統性硬化症常併發小腸細菌過度增生，ciprofloxacin 可用於處理此併發症（PMID 7728404）。

然而，抗纖維化機轉尚未獲得證實；腸道細菌過度增生的改善屬於症狀處理，並非改變疾病本身的療法。因此高預測分數並未得到對照臨床資料的支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | 探索性研究（對照、雙盲隨機試驗設計） | The Journal of Dermatology | 評估口服 ciprofloxacin 對硬皮症皮膚的抗纖維化作用；可取得的摘要內容不完整，結果須查閱全文 |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | 診斷／觀察性研究 | British Journal of Rheumatology | 24 位有吸收不良症狀的系統性硬化症患者，探討小腸細菌過度增生的偵測方法與治療結果 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52577 | VIPROLOX 250 TAB 250MG | 未記載 | 未記載 |
| HK-53688 | LOXIN TAB 250MG | 未記載 | 未記載 |
| HK-51940 | ZOXAN-250 TAB 250MG | 未記載 | 未記載 |
| HK-47031 | POLI-CIFLOXIN 250 TAB 250MG | 未記載 | 未記載 |
| HK-50313 | INTERFLOX 500 TAB 500MG | 未記載 | 未記載 |

本表僅列出部分許可證，完整清單可能不止於此（本次資料可能不完整）。

## 安全性考量

- **藥物交互作用**：本次資料顯示共有 100 筆交互作用記錄。其中列為嚴重 (Major) 的包括 hydrocortisone、bupropion、triamcinolone、dexamethasone、betamethasone；列為中度 (Moderate) 的包括 acarbose、famotidine、metformin、pioglitazone、loperamide、aspirin 等。糖皮質素類與氟喹諾酮併用，需特別留意肌腱相關風險。

其餘警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高，但目前沒有任何已登記的臨床試驗，僅有的兩篇文獻並未提供對照性的療效證據。抗纖維化作用仍屬假說，腸道細菌過度增生的處理也只是症狀性獲益。

**若要推進需要：**
- 取得 PMID 20507401 的全文與完整結果，確認其對照試驗的療效與安全性數據
- 補充詳細的作用機轉資料，驗證抗纖維化假說
- 取得原廠仿單中的警語與禁忌症，並評估長期使用氟喹諾酮於慢性病族群的安全性（含肌腱、周邊神經與 QT 延長風險）
- 如要進一步研究，需設計針對瀰漫性硬皮症的前瞻性對照試驗
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

