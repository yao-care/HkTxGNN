---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 734
evidence_level: L5
indication_count: 5
---

# Quetiapine
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

# Quetiapine：從精神科用藥到視網膜失養症

## 一句話總結

Quetiapine 是一種非典型抗精神病藥，在香港已有多張上市許可證。
TxGNN 模型預測它可能對**視網膜失養症（伴或不伴眼外異常，Retinal Dystrophy）**有效，但目前**沒有任何臨床試驗**，檢索到的 15 篇文獻也都與 quetiapine 無關，證據僅來自模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（藥物屬非典型抗精神病藥） |
| 預測新適應症 | 視網膜失養症，伴或不伴眼外異常 (Retinal Dystrophy) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 欄位未提供）。根據已知資訊，quetiapine 是非典型抗精神病藥，主要作用在 D2 與 5-HT2A 受體拮抗，另有 H1 與 alpha-1 活性。

視網膜失養症多為遺傳性疾病，成因是光受體或視網膜色素上皮細胞功能異常。目前沒有受體層級的理由能把 quetiapine 與這類疾病連起來。

因此，這個預測的 99.57% 高分只代表知識圖譜上的關聯，**不代表有機轉或臨床依據**。現階段不宜把它視為合理的老藥新用候選。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

檢索到的文獻都是一般眼科或眼眶先天異常的主題，標題與摘要均未提及 quetiapine 或任何藥物治療。研究類型皆未能判定，以下列出 10 篇。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | 未分類 | Taiwan J Ophthalmol | 水晶體形狀的先天異常概述，與 quetiapine 無關 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | 未分類 | Pediatr Radiol | 兒童眼眶病變的影像鑑別診斷 |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | 未分類 | Int J Mol Sci | 先天性眼外肌纖維化合併視神經盤與視網膜異常 |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | 未分類 | Am J Ophthalmol | 空洞性視神經盤異常相關黃斑病變的致病機轉與處置 |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | 未分類 | J Binocul Vis Ocul Motil | 先天性顱神經失神經支配疾病與眼肌麻痺 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | 病例報告 | J Neuroophthalmol | 一例先天性滑車神經與動眼神經聯動 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | 病例報告 | Optom Vis Sci | 一例先天性眼外肌纖維化的協同性外斜 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | 病例系列 | Arch Ophthalmol | 眼眶動靜脈畸形的臨床特徵與處置 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | 未分類 | Semin Neurol | 複視的系統性評估方法 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | 未分類 | Doc Ophthalmol | Wagner-Stickler 症候群的玻璃體視網膜病變 |

## 香港上市資訊

許可證資料未載明劑型與核准適應症。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65854 | QUETIAPINE TABLETS 100MG | 未載明 | 未載明 |
| HK-58567 | QUETIAPINE-TEVA TAB 25MG | 未載明 | 未載明 |
| HK-64304 | ACCORD QUETIAPINE EXTENDED RELEASE TABLETS 200MG | 未載明 | 未載明 |
| HK-65348 | QUESERO EXTENDED RELEASE TABLETS 200MG | 未載明 | 未載明 |
| HK-52580 | SEROQUEL TAB 300MG | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻也與 quetiapine 無關，證據等級只有 L5。
- 機轉上沒有可說明的連結，高分只來自圖譜預測。
- 其餘四個預測適應症同樣只有模型分數，沒有試驗或文獻，也都沒有機轉依據：
  - 岩藻糖化缺陷的先天性糖基化異常
  - 無腦迴畸形（水腦無腦症）
  - 17p13.3 遠端微缺失症候群
  - 多小腦迴畸形合併小腦發育不全與關節攣縮

**若要推進需要：**
- 補齊 quetiapine 的作用機轉資料，並分析它與視網膜失養症病理的關聯。
- 以 quetiapine 與視網膜疾病（含前臨床模型）為關鍵字重新檢索，確認是否有直接證據。
- 取得香港衛生署仿單，補上警語、禁忌與交互作用資料，才能進入安全性初篩。
- 若無上述直接證據，不建議繼續投入資源。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

