---
layout: default
title: Piperacillin
parent: 僅模型預測 (L5)
nav_order: 689
evidence_level: L5
indication_count: 5
---

# Piperacillin
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

# Piperacillin：從細菌感染到類風濕性關節炎

## 一句話總結

Piperacillin 是一種注射用 β-內醯胺類抗生素，目前在香港有多張上市許可證。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
但目前**沒有臨床試驗**，檢索到的 17 篇文獻多為感染或藥物不良反應的個案報告，並不支持療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供 |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5（僅模型預測；系統內部標註為 L4，但文獻未提供機轉或前臨床研究，故依判定規則歸為 L5） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Piperacillin 屬於青黴素類（penicillin）抗生素，一般認為是透過抑制細菌細胞壁合成而殺菌。

類風濕性關節炎是自體免疫疾病，治療核心是免疫調節與抗發炎。Piperacillin 沒有已知的免疫調節或抗發炎活性，機轉上看不出與類風濕性關節炎的關聯。0.999 的高分很可能是知識圖譜的人為結果，而非生物學上的真實訊號。

檢索到的文獻中，類風濕性關節炎只是病人的背景疾病。這些報告描述的是病人因免疫抑制而感染、使用 piperacillin/tazobactam 治療感染，並不是在治療類風濕性關節炎本身。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為檢索到的主要文獻，均無法支持 piperacillin 對類風濕性關節炎的療效：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | 世代研究 | Ann Transl Med | 抗生素相關藥物性肝損傷的盛行率與臨床特徵 |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2025 | 回溯性世代／預測模型 | Br J Clin Pharmacol | 建立使用 ampicillin/sulbactam 或 piperacillin/tazobactam 者嗜酸性球增多的預測模型 |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | 個案報告 | Orthopadie | 類風濕性關節炎病人人工膝關節的流感嗜血桿菌感染，曾使用 piperacillin/tazobactam 治療肺炎 |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | 個案報告 | BMJ Case Rep | 使用 etanercept 的類風濕性關節炎病人發生化膿性心包膜炎，經驗性使用 piperacillin/tazobactam |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | 個案報告＋文獻回顧 | BMC Infect Dis | 抗藥性 Edwardsiella tarda 造成敗血性休克 |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | 個案報告 | Front Immunol | 長期免疫抑制的類風濕性關節炎病人發生大腸桿菌引起的非典型丹毒 |
| [30371923](https://pubmed.ncbi.nlm.nih.gov/30371923/) | 2019 | 個案報告 | Orthopedics | 類風濕性關節炎病人股骨氣腫性骨髓炎，以髓內抗生素骨水泥治療 |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | 個案報告 | Proc (Bayl Univ Med Cent) | 低劑量 methotrexate 毒性導致全血球減少，以 leucovorin 解救 |

另有數篇個案報告（如 methotrexate 毒性、Sjögren 症候群、Felty 症候群感染等）與 piperacillin 對類風濕性關節炎的療效無關，此處不逐一列出。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56958 | PIPERACILLIN SODIUM FOR INJ. 4G | 注射劑 | 資料未提供 |
| HK-66929 | PIPERACILLIN AND TAZOBACTAM POWDER FOR SOLUTION FOR INFUSION 4.5G | 輸注用粉劑 | 資料未提供 |
| HK-65419 | PIPERACILLIN/TAZOBACTAM KABI POWDER FOR SOLUTION FOR INFUSION 4G/0.5G | 輸注用粉劑 | 資料未提供 |
| HK-60314 | PYBACTAM 4.5G POWDER FOR SOLN FOR INJ/INF | 注射／輸注用粉劑 | 資料未提供 |
| HK-52054 | TAZOBACTAM/PIPERACILLIN SOD F/ INJ 2.25G (ZHUHAI UNITED LAB) | 注射劑 | 資料未提供 |

## 安全性考量

- **肝損傷**：文獻顯示 piperacillin 類抗生素與藥物性肝損傷有關（PMID 33987340）。
- **嗜酸性球增多**：使用 piperacillin/tazobactam 的病人有發生嗜酸性球增多的風險（PMID 41257433）。

其餘安全性資訊請參考原廠仿單。

## 其他預測適應症

以下預測全部只有模型分數，沒有臨床試驗，也沒有支持性文獻：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|------|-----------|-----------|---------|------|
| 2 | 眼缺損性小眼症-肢根型發育不良症候群 | 99.89% | L5 | 罕見發育遺傳疾病，抗菌藥物沒有可辨識的作用標的 |
| 3 | 短指-併指症候群 | 99.86% | L5 | 先天性肢體畸形，與抗菌機轉無關 |
| 4 | 硬化性膽管炎 | 99.82% | L5 | 僅有間接關聯（抗生素曾用於研究，piperacillin 經膽汁排泄），但也與藥物性肝損傷有關 |
| 5 | 骨關節炎易感性 | 99.56% | L5 | 指遺傳易感性，非抗菌藥物標的；唯一文獻是 linezolid 與 vancomycin 的比較，與 piperacillin 無關 |

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻只是類風濕性關節炎病人的感染或不良反應報告，機轉上也沒有合理的關聯。
- 五個預測適應症都沒有實質證據，TxGNN 的高分應視為知識圖譜的人為結果。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌症（目前為阻擋性資料缺口）
- 補齊作用機轉資料（可查詢 DrugBank）
- 找到具體的免疫調節或抗發炎機轉假說與前臨床證據，否則不建議投入資源

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

