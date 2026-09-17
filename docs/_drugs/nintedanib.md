---
layout: default
title: Nintedanib
parent: 中證據等級 (L3-L4)
nav_order: 525
evidence_level: L4
indication_count: 10
---

# Nintedanib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Nintedanib：從纖維化/抗血管新生治療到皮膚隆突性纖維肉瘤 (DFSP)

## 一句話總結

Nintedanib 是三重血管激酶抑制劑（VEGFR1-3、FGFR1-3、PDGFRα/β），全球已知用於特發性肺纖維化等間質性肺病及非小細胞肺癌合併治療（此為一般公開藥理學資訊，非本 Evidence Pack 提供）。
TxGNN 模型預測它可能對**皮膚隆突性纖維肉瘤 (Dermatofibrosarcoma Protuberans, DFSP)** 有效，
目前僅有 **1 篇相關文獻**（回顧性文章，非該藥物專屬臨床數據），無臨床試驗支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 此 Evidence Pack 未提供（`original_indications` 為空、無 MOA 資料）；一般已知用於間質性肺病、NSCLC |
| 預測新適應症 | 皮膚隆突性纖維肉瘤 (Dermatofibrosarcoma Protuberans) |
| TxGNN 預測分數 | 99.15% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏本藥物的正式 MOA 欄位資料（`original_moa` 為 Data Gap），但證據包中的機轉推論指出：Nintedanib 為三重血管激酶抑制劑，同時抑制 VEGFR1-3、FGFR1-3、PDGFRα/β。

DFSP 這類腫瘤常見 *COL1A1-PDGFB* 融合基因，會驅動 PDGFRB 持續活化——這正是 DFSP 現行標準治療 imatinib 的作用標的。Nintedanib 的 PDGFR 抑制活性因此在分子機轉上與 DFSP 有明確關聯。

但需注意：唯一支持文獻是一篇 2018 年的 PDGFR 抑制劑類別回顧性文章，並非針對 nintedanib 治療 DFSP 的專屬研究，屬於**間接的類別效應推論**，尚無 nintedanib 專屬的臨床前或臨床數據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | 回顧小分子 PDGFR 抑制劑於腫瘤治療中的角色，說明 PDGF/PDGFR 訊號路徑在多種腫瘤（含纖維母細胞性腫瘤）中的致病機轉 |

## 香港上市資訊

此藥物目前**未在香港上市**，查無許可證資料（`total_licenses = 0`）。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本 Evidence Pack 標記 TFDA/香港仿單警語與禁忌症資料為 **Blocking** 缺口（DG001），目前無法進行 S1 安全性初評。

## 其他預測適應症（低證據等級，僅供研究參考）

除 DFSP 外，TxGNN 同批預測了以下 9 個候選適應症，均**無臨床試驗或文獻證據**支持（證據等級 L5，僅為模型分數推論）：

| 排名 | 疾病 | TxGNN 分數 | 建議 |
|------|------|-----------|------|
| 2 | Liposarcoma | 99.13% | Hold |
| 3 | Ovarian myxoid liposarcoma | 99.12% | Hold |
| 4 | Heart fibrosarcoma | 98.88% | Hold |
| 5 | Axial spondylometaphyseal dysplasia | 98.87% | Hold（機轉不相關，疑似偽陽性） |
| 6 | Amyotrophic lateral sclerosis type 22 | 98.86% | Hold |
| 7 | Fibroblastic neoplasm | 98.84% | Hold |
| 8 | Kidney fibrosarcoma | 98.83% | Hold |
| 9 | Conventional fibrosarcoma | 98.81% | Hold |
| 10 | ALS, susceptibility to | 98.80% | Hold |

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一支持證據為類別回顧文獻，非 nintedanib 專屬數據，證據等級僅 L4；
- 安全性仿單資料缺失（Blocking），無法進入 S1 安全性初評；
- 藥物於香港未上市，無在地法規路徑可依循。

**若要推進需要：**
- 取得 TFDA/香港官方仿單警語與禁忌症資料（解除 DG001 Blocking 缺口）
- 透過 DrugBank API 補齊正式 MOA 資料（DG002）
- 尋找 nintedanib 專屬於 PDGFR 驅動腫瘤（如 DFSP）之臨床前或病例報告證據
- 評估劑型與給藥途徑相容性（目前無本地上市劑型資料）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

