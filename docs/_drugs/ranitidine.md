---
layout: default
title: Ranitidine
parent: 高證據等級 (L1-L2)
nav_order: 633
evidence_level: L1
indication_count: 5
---

# Ranitidine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# RANITIDINE：從消化性潰瘍（原適應症疑似同義）到活動性消化性潰瘍等 5 項預測適應症

## 一句話總結

> Ranitidine（雷尼替丁）是經典的 H2 受體拮抗劑，原本即用於消化性潰瘍相關疾病治療，但本資料庫的 `original_indications` 欄位缺失，未正式登錄原適應症。
> TxGNN 模型將其排名最高的預測適應症列為**活動性消化性潰瘍 (Active Peptic Ulcer Disease)**，但這實際上很可能就是本藥的**原始核心適應症**，並非真正的老藥新用；其餘 4 項預測（胃空腸吻合口潰瘍、消化性潰瘍穿孔、十二指腸胃逆流、十二指腸阻塞）才是機轉延伸性較強的候選方向。
> 目前僅有 **1 個臨床試驗**（且與 ranitidine 非直接相關）與**約 20 篇文獻**支持第一名預測，證據強度標示為 L1，但需留意此為既有適應症的證據累積，而非新方向的驗證。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未登錄（`original_indications` 為空）；依藥理與文獻推斷應為消化性潰瘍/十二指腸潰瘍相關疾病 |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策（系統） | Proceed with Guardrails |

---

## 為什麼這個預測合理？

**⚠️ 重要提醒**：本資料庫缺少 `original_moa` 與 `original_indications` 兩項欄位（DG002, High severity），但從證據文獻可清楚重建 Ranitidine 的作用機轉——它是選擇性 H2（組織胺第二型受體）拮抗劑，透過阻斷壁細胞上的組織胺受體，抑制基礎與刺激性胃酸分泌，效力約為 cimetidine 的 4-10 倍。這正是消化性潰瘍治療的經典機轉。

排名第一的預測「活動性消化性潰瘍」與此機轉高度吻合——事實上多篇文獻（如 PMID 3909374、2491360、2877570）直接就是 ranitidine 用於治療活動性十二指腸/胃潰瘍的隨機對照試驗，證實其療效與 famotidine、omeprazole 相當。**這說明此項「預測」實質上是模型重新發現了藥物已知的核心適應症，而非發掘全新用途**，在解讀證據等級 L1 時應納入這層考量。

其餘 4 項預測適應症（胃空腸吻合口潰瘍、消化性潰瘍穿孔、十二指腸胃逆流、十二指腸阻塞）則屬於消化性潰瘍的解剖延伸或併發症，機轉關聯性遞減、證據強度也隨之下降（L4-L5），詳見下方「其他預測適應症」摘要。

### 其他預測適應症摘要（Rank 2-5）

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 系統建議 |
|------|------|-----------|---------|---------|---------|
| 2 | 胃空腸吻合口潰瘍 (Gastrojejunal Ulcer) | 99.88% | L4 | S1 | Research Question |
| 3 | 消化性潰瘍穿孔 (Peptic Ulcer Perforation) | 99.88% | L4 | S1 | Research Question |
| 4 | 十二指腸胃逆流 (Duodenogastric Reflux) | 99.84% | L4 | S1 | Research Question |
| 5 | 十二指腸阻塞 (Duodenal Obstruction) | 99.83% | L5 | S0 | Hold |

這 4 項均無直接臨床試驗支持，文獻多為個案報告、動物實驗或間接關聯研究，機轉上僅能視為「透過抑酸間接減少黏膜傷害」的延伸推論，而非直接治療機轉。

---

## 臨床試驗證據（活動性消化性潰瘍）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | 已完成 | 320 | 研究 PPI/statin 對 clopidogrel 抗血小板效果的影響；ranitidine 非研究焦點，相關性評級為 C（間接） |

**注意**：這是唯一登記到的相關試驗，且與 ranitidine 僅間接相關，並非直接驗證其於消化性潰瘍的療效。

---

## 文獻證據（活動性消化性潰瘍）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scand J Gastroenterol | Ranitidine 300mg/日治療潰瘍，4週癒合率：十二指腸潰瘍91%、幽門前潰瘍68%、胃體潰瘍81%；維持治療1年可降低復發 |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klinische Wochenschrift | Rioprostil 與 ranitidine 治療十二指腸潰瘍癒合效果比較 |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT（雙盲隨機） | J Gastroenterol Hepatol | 270名患者比較 omeprazole 與 ranitidine 治療十二指腸潰瘍及後續復發，每週內視鏡評估 |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT（多中心雙盲） | Am J Med | 1,031名患者跨19國多中心試驗，比較 famotidine 與 ranitidine 治療活動性十二指腸潰瘍 |
| [2092029](https://pubmed.ncbi.nlm.nih.gov/2092029/) | 1990 | RCT（雙盲隨機） | J Assoc Physicians India | famotidine 與 ranitidine 治療內視鏡確診消化性潰瘍之安全性與療效比較 |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | 前瞻對照研究 | Hepato-gastroenterology | Ranitidine 併用 ecabet 可獨立於 H. pylori 根除降低潰瘍復發 |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | 多中心研究 | Clin Ther | 160名患者比較 famotidine 與 ranitidine 治療活動性十二指腸潰瘍及6個月維持治療 |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intell Clin Pharm | Ranitidine 藥理綜述，效力約為 cimetidine 的4-10倍 |
| [6128216](https://pubmed.ncbi.nlm.nih.gov/6128216/) | 1982 | Review | Drugs | Ranitidine 藥理學與治療應用完整綜述 |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-gastroenterology | 消化性潰瘍發病機轉與抑酸治療綜述 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

**⚠️ 資料缺口提醒**：本評估缺少 TFDA/當地藥監局仿單警語與禁忌症資料（DG001，Blocking severity），依規則此缺口會阻擋進入 S1 安全性初評階段，須優先補齊後才能進行完整風險評估。此外，Ranitidine 已於 2020 年因原料藥可能含 NDMA（一種可能致癌物）雜質，遭全球多國廠商陸續下架回收，此為安全性考量的重要背景，而非療效問題。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 系統對排名第一預測（活動性消化性潰瘍）給出「Proceed with Guardrails」，但此項實質上並非新適應症，而是藥物原本已知且已上市多年的核心用途，不構成真正的老藥新用機會。
- 其餘 4 項具備新穎性的預測適應症證據等級僅 L4-L5，缺乏直接臨床試驗支持。
- 存在 Blocking 等級資料缺口（DG001：仿單警語/禁忌），依規則無法完成 S1 安全性初評。
- Ranitidine 目前香港未上市，且藥物本身因 NDMA 雜質疑慮已於全球下架，重新申請上市須先解決原料藥安全性問題，與適應症證據強弱無關。

**若要推進需要：**
- 補齊 TFDA/原廠仿單警語與禁忌症資料，解除 DG001 阻擋
- 補齊 DrugBank 完整 MOA 與 original_indications 欄位，釐清真正的「新」適應症基準線
- 針對胃空腸吻合口潰瘍、消化性潰瘍穿孔等真正具延伸性的候選方向，規劃前臨床或觀察性研究以補強證據
- 追蹤 NDMA 雜質風險是否已有解決方案（如替代合成製程），此為上市前提
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

