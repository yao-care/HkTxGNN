---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Chlorpromazine：從抗精神病藥到視網膜失養症

## 一句話總結

Chlorpromazine（氯丙嗪）是第一代抗精神病藥，主要透過阻斷多巴胺 D2 受體發揮作用。
TxGNN 模型預測它可能對**視網膜失養症（Retinal Dystrophy，伴或不伴眼外異常）**有效，但目前有 **0 個臨床試驗**，14 篇文獻也沒有一篇直接支持這個方向。
這個預測較可能是知識圖譜結構造成的假象，並非真實的藥理訊號。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 視網膜失養症，伴或不伴眼外異常 (Retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 99.95%（模型排名第 1565 名） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

**這個預測在機轉上並不合理。** 目前缺乏詳細的作用機轉資料，但已知 Chlorpromazine 是 D2、5-HT2A、H1 及 alpha-1 受體拮抗劑。這些路徑都不是遺傳性視網膜失養症的已知致病驅動因子。

Chlorpromazine 本身還與眼部不良反應有關，包括水晶體與角膜沉積，以及高累積劑量下的色素性視網膜病變。安全性訊號和預測方向相反。文獻中唯一貼近的是 1968 年的〈Phenothiazine-retinopathy〉，談的是藥物造成視網膜病變，而不是治療它。

0.9995 的高分最可能來自圖譜拓樸的偽影（graph-topology artefact），不代表生物學上的關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

TxGNN 取回 14 篇文獻，大多只是因主題關鍵字（眼外肌、先天性眼部異常）被比對到，與 Chlorpromazine 的治療效果無關。下表列出 10 篇，型別以文獻自帶分類為準。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [5647013](https://pubmed.ncbi.nlm.nih.gov/5647013/) | 1968 | 未分類（無摘要） | Ophthalmologica | 依標題為吩噻嗪類藥物引起的視網膜病變，屬安全性訊號 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | 複視的問診與檢查流程，與 Chlorpromazine 無關 |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | 眼眶感染的成因與影像表現，與 Chlorpromazine 無關 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblatter fur Augenheilkunde | 先天性上眼瞼下垂的臨床特徵，與 Chlorpromazine 無關 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | 水晶體形狀的先天異常，與 Chlorpromazine 無關 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | 兒童眼部病變的鑑別診斷與影像特徵，與 Chlorpromazine 無關 |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | 先天性顱神經失神經支配疾病中的眼肌麻痺，與 Chlorpromazine 無關 |
| [31359131](https://pubmed.ncbi.nlm.nih.gov/31359131/) | 2019 | 未分類 | Human Genetics | 視黃酸訊號相關的眼部發育缺陷之遺傳架構，與 Chlorpromazine 無關 |
| [10192514](https://pubmed.ncbi.nlm.nih.gov/10192514/) | 1999 | Review | Progress in Retinal and Eye Research | 眼外肌本體感覺的作用，與 Chlorpromazine 無關 |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Cohort | Neuroradiology | 眼肌麻痺的神經影像與臨床特徵，與 Chlorpromazine 無關 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-53900 | CHLOZINE EXTRA TAB 100MG | APT PHARMA LIMITED |
| HK-44623 | CHLOZINE PLUS TAB 50MG | APT PHARMA LIMITED |
| HK-44714 | CHLOZINE TAB 25MG | APT PHARMA LIMITED |

## 安全性考量

- **與此預測相關的安全訊號**：Chlorpromazine 與水晶體與角膜沉積、高累積劑量下的色素性視網膜病變有關。若用於視網膜疾病，風險方向與預期相反。

其他警語、禁忌症與藥物交互作用資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有臨床試驗，也沒有支持性文獻，而且機轉上找不到合理連結。
- 藥物本身的視網膜毒性訊號還與預期方向相反。

**若要推進需要：**
- 找出視網膜失養症與 D2/5-HT2A/H1/alpha-1 路徑之間任何可驗證的機轉假說；若找不到，建議直接排除。
- 取得香港衛生署仿單的警語與禁忌症，補齊安全性資料。
- 補齊 DrugBank 的作用機轉資料。

**其他候選提醒：** 同一藥物的排名第 10 名預測「早發性精神分裂症 (Early-onset schizophrenia)」是本次唯一有實質證據的候選。它有 1 個觀察性試驗登記（NCT06128408，僅間接相關）和 8 篇觀察性或藥物基因學文獻，證據等級為 L3，目前無 RCT。這其實是成人適應症向兒童與青少年族群的延伸。若要推進，建議另行評估這個候選，並特別檢視兒童的錐體外症狀、鎮靜與代謝風險。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

