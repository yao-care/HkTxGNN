---
layout: default
title: Trifluoperazine
parent: 中證據等級 (L3-L4)
nav_order: 773
evidence_level: L4
indication_count: 1
---

# Trifluoperazine
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

# Triflupromazine（Trifluoperazine）：從精神分裂症到躁鬱症（Manic Bipolar Affective Disorder）

## 一句話總結

Trifluoperazine 是典型 phenothiazine 類抗精神病藥，目前香港未上市，原始適應症與作用機轉資料均缺失。
TxGNN 模型預測它可能對**躁鬱症躁狂發作 (Manic Bipolar Affective Disorder)** 有效，
目前**無相關臨床試驗登記**，僅有 **20 篇文獻**（多為個案報告與回顧性文章）提供機轉層級的間接支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（香港未上市，原始適應症未記錄） |
| 預測新適應症 | 躁鬱症躁狂發作 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

本資料集中 `original_moa` 標記為缺失，無法從官方資料直接確認 Trifluoperazine 的作用機轉。不過根據文獻層級的機轉推論（PMID 970489），Trifluoperazine 屬於典型 phenothiazine 類抗精神病藥，主要藥理作用為 D2 多巴胺受體拮抗。

躁狂發作與中樞多巴胺功能亢進假說一致，這也是典型抗精神病藥被用於急性躁狂治療的經典機轉基礎。然而，這個關聯目前只建立在**藥物類別層級（class-level）**的推論上——文獻中提及 Trifluoperazine 多半是作為抗精神病藥類別的一員被討論（如躁狂管理、NMS 副作用案例），而非針對躁鬱症躁狂發作設計的 Trifluoperazine 專屬對照試驗。

換言之，機轉上「合理」，但目前缺乏藥物專一性（drug-specific）的直接臨床證據來驗證這個預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11279762](https://pubmed.ncbi.nlm.nih.gov/11279762/) | 2001 | RCT（不同藥物） | Cochrane Database Syst Rev | Clotiapine 用於急性精神病症狀之隨機對照試驗回顧，非 Trifluoperazine 直接證據 |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | 回顧典型與非典型抗精神病藥對躁鬱症合併焦慮症狀的療效 |
| [39202628](https://pubmed.ncbi.nlm.nih.gov/39202628/) | 2024 | Systematic Review | Medicina (Kaunas) | 抗精神病藥誘發「兔子症候群」口部運動障礙之系統性回顧 |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatr Practice | 懷孕期間抗精神病藥使用與安全性回顧 |
| [40926568](https://pubmed.ncbi.nlm.nih.gov/40926568/) | 2026 | Review（基礎研究） | J Appl Toxicol | Phenothiazine 衍生物對細胞凋亡機轉的影響回顧 |
| [970489](https://pubmed.ncbi.nlm.nih.gov/970489/) | 1976 | Review/Mechanistic | Am J Psychiatry | 探討躁狂發作的多巴胺機轉假說，為典型抗精神病藥治療躁狂的機轉基礎 |
| [30601177](https://pubmed.ncbi.nlm.nih.gov/30601177/) | 2021 | Review | Am J Ther | 哺乳期精神科用藥（含躁鬱症治療）安全性評分系統 |
| [24943390](https://pubmed.ncbi.nlm.nih.gov/24943390/) | 2014 | Cohort/處方模式 | J Clin Psychopharmacol | 烏干達精神科機構躁鬱症等診斷之抗精神病藥處方模式調查 |
| [20851282](https://pubmed.ncbi.nlm.nih.gov/20851282/) | 2010 | Case report | Gen Hosp Psychiatry | Risperidone 誘發口吃個案報告，提及 Trifluoperazine 等藥物曾有類似副作用文獻 |
| [19164500](https://pubmed.ncbi.nlm.nih.gov/19164500/) | 2010 | Case report | J Psychopharmacol | Ziprasidone 誘發自發性性高潮個案，提及 Trifluoperazine 曾有類似報告 |

**注意**：以上文獻多數為抗精神病藥「類別層級」討論，直接針對 Trifluoperazine 用於躁鬱症躁狂發作的研究極為有限，證據強度偏低。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 資料缺口提示：TFDA 仿單警語/禁忌資料缺失（Blocking），目前**無法進行 S1 安全性初評**。此為推進本候選前必須補齊的關鍵資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L4（機轉層級推論，無藥物專一性臨床試驗），且無任何臨床試驗登記支持。
- 安全性初評因 TFDA 仿單警語/禁忌資料缺失而無法執行（Blocking data gap）。
- 香港未上市，缺乏在地監管與上市資訊佐證。

**若要推進需要：**
- 取得 TFDA（或香港藥劑業及毒藥管理局）官方仿單，解析警語與禁忌症，解除 Blocking 缺口。
- 查詢 DrugBank API 補齊 Trifluoperazine 之作用機轉（MOA）原始資料。
- 檢索是否存在 Trifluoperazine 專屬（而非藥物類別層級）用於躁鬱症躁狂發作之對照試驗或觀察性研究。
- 確認香港上市狀態與潛在許可證途徑。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

