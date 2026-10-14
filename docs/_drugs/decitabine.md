---
layout: default
title: Decitabine
parent: 中證據等級 (L3-L4)
nav_order: 250
evidence_level: L4
indication_count: 1
---

# Decitabine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Decitabine：從急性骨髓性白血病到兒童難治性血球減少症

## 一句話總結

Decitabine 是一種去甲基化藥物，原本用於急性骨髓性白血病（AML）及相關骨髓疾病的治療。
TxGNN 模型預測它可能對**兒童難治性血球減少症 (Refractory Cytopenia of Childhood, RCC)** 有效，
目前**沒有登記的臨床試驗**，僅有 **2 篇文獻**（1 篇世代研究、1 篇病例報告）支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性骨髓性白血病（AML）及相關骨髓性疾病（香港許可證未列出核准適應症文字） |
| 預測新適應症 | 兒童難治性血球減少症 (Refractory Cytopenia of Childhood) |
| TxGNN 預測分數 | 99.03% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位未提供）。根據藥理學既有知識，Decitabine 是一種去甲基化核苷類似物，可抑制 DNA 甲基轉移酶，已用於骨髓性惡性腫瘤，包括 AML 與骨髓增生異常症候群（MDS）。以下機轉推論來自一般藥理知識，而非所提供的資料。

RCC 是兒童 MDS 最常見的亞型。AML 與 MDS 都涉及異常 DNA 甲基化與骨髓系殖株功能失調，因此機轉上有合理關聯。

需要注意：0.99 的 TxGNN 分數是電腦模型預測，並非臨床證據。目前支持性資料僅有一項單中心世代研究與一則病例報告。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | 世代研究 | BMC Pediatrics | 單中心 10 年經驗，探討 Decitabine 合併低骨髓抑制方案作為橋接，再接受異體造血幹細胞移植，用於兒童 MDS |
| [42125547](https://pubmed.ncbi.nlm.nih.gov/42125547/) | 2026 | 病例報告 | Experimental and Therapeutic Medicine | 一名 8 歲兒童 RCC 病患不適合接受移植或免疫抑制治療，以 Decitabine 單藥治療的病例 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67129 | DACOGEN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 50MG（Johnson & Johnson (Hong Kong) Ltd.） | 輸注濃縮液用粉末（依品名） | 未提供 |
| HK-68634 | DECITABINE POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 50MG（Chemill Pharma Limited） | 輸注濃縮液用粉末（依品名） | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（去甲基化核苷類似物） |
| 骨髓抑制風險 | 高（知識圖譜將嗜中性白血球減少、血小板減少、顆粒球缺乏列為禁忌相關疾病） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

其餘細胞毒性細節請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜標示的相關疾病禁忌**（來自知識圖譜，非仿單內容）：腎臟疾病、膿輸尿管症、肝臟疾病、膽囊疾病、血小板減少症、糖尿病、糖尿病酮酸中毒、嗜中性白血球減少症、顆粒球缺乏症。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 重大（Major）：Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib
  - 中度（Moderate）：Palifermin、Mercaptopurine、Chloramphenicol、Zidovudine、Ganciclovir、Gemcitabine、Azathioprine、Alemtuzumab 等

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅有模型分數與極少量文獻（1 篇單中心世代研究、1 篇病例報告）支持，沒有登記的臨床試驗，證據等級為 L4。
- 仿單的警語與禁忌資料尚缺，無法進入安全性篩選；兒童族群的骨髓抑制風險也需要審慎評估。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症
- 補充 DrugBank 的作用機轉（MOA）資料
- 系統性回顧兒童 MDS/RCC 使用 Decitabine 的研究
- 評估兒童族群的劑量、骨髓抑制與感染風險
- 規劃前瞻性臨床研究，或先與血液專科討論個案使用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

