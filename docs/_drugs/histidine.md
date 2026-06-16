---
layout: default
title: Histidine
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 2
---

# Histidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Histidine：從必需胺基酸到胃輕癱與硬化性膽管炎

## 一句話總結

Histidine（L-組胺酸）是人體必需胺基酸，目前在香港無核准藥物適應症。
TxGNN 模型預測兩個潛在新用途：**胃輕癱 (Gastroparesis)**（Rank 1，分數 99.55%）與**硬化性膽管炎 (Sclerosing Cholangitis)**（Rank 2，分數 99.27%）。
前者完全缺乏臨床前及臨床證據（L5，Hold）；後者有 **8 篇機轉研究文獻**支持，但機轉方向存在根本矛盾，需動物實驗釐清淨效應（L4，Research Question）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無（必需胺基酸，無核准治療適應症） |
| 預測新適應症（Rank 1） | 胃輕癱 (Gastroparesis) |
| TxGNN 預測分數（Rank 1） | 99.55% |
| 預測新適應症（Rank 2） | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數（Rank 2） | 99.27% |
| 證據等級 | L5（胃輕癱）／L4（硬化性膽管炎） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold（胃輕癱）／Research Question（硬化性膽管炎） |

---

## 為什麼這個預測合理？

目前缺乏 Histidine 的詳細作用機轉（MOA）資料。Histidine 是人體無法自行合成的必需胺基酸，其已知的生化功能主要包括三個面向：**組織胺前驅物**（經 L-組胺酸脫羧酶 HDC 催化轉化為組織胺）、**抗氧化特性**（自由基清除、過渡金屬螯合），以及**免疫調節**（蛋白質合成與炎症調控）。

**Rank 1 ─ 胃輕癱（Gastroparesis）**

Histidine 作為組織胺前驅物，理論上可能透過 H2 受體路徑影響胃酸分泌，但此路徑與胃腸道動力障礙（胃輕癱的核心病理）之間的連結極為薄弱，且缺乏方向性支持。TxGNN 高分（0.9955）極可能反映知識圖譜中胃腸代謝節點的間接拓樸連結，而非有效的生物學機轉假說。目前無任何臨床前或臨床研究支持此適應症。

**Rank 2 ─ 硬化性膽管炎（Primary Sclerosing Cholangitis, PSC）**

Histidine 是組織胺的**直接生化前驅物**（Histidine →[HDC]→ 組織胺），此路徑在 PSC 中具有明確的文獻基礎。現有 8 篇文獻揭示一個重要的機轉矛盾：組織胺在 PSC 中扮演**促纖維化、促膽管增殖**的有害角色。HDC 基因敲除（無法將 Histidine 轉化為組織胺）的 Mdr2−/− PSC 小鼠膽管損傷與肝纖維化顯著改善，且阻斷 H1/H2 受體可抑制 PSC 模型中的損傷進展。

這意味著補充 Histidine（增加底物）可能**提升組織胺生成，從而加重疾病**。然而，Histidine 本身的抗氧化特性與免疫調節作用或許部分抵消上述不利影響，淨效應方向目前不明，需要直接動物實驗驗證。

---

## 臨床試驗證據

### 胃輕癱（Rank 1）

目前無相關臨床試驗登記。

### 硬化性膽管炎（Rank 2）

目前無相關臨床試驗登記。

---

## 文獻證據

### 胃輕癱（Rank 1）

目前無相關文獻。

### 硬化性膽管炎（Rank 2）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [32054995](https://pubmed.ncbi.nlm.nih.gov/32054995/) | 2020 | 動物模型（HDC-KO 小鼠） | Laboratory Investigation | HDC 基因敲除（無 Histidine→組織胺轉化）的 Mdr2−/− 雙基因敲除小鼠膽管損傷與肝纖維化顯著改善，直接揭示 Histidine 代謝路徑在 PSC 的核心作用 |
| [29601088](https://pubmed.ncbi.nlm.nih.gov/29601088/) | 2018 | 動物模型 + 體外 | Hepatology | 慢性阻斷 H1/H2 組織胺受體可抑制 Mdr2−/− 小鼠 PSC 相關膽管損傷及後續膽管癌形成 |
| [27351144](https://pubmed.ncbi.nlm.nih.gov/27351144/) | 2016 | 體外／機轉 | Hepatology | 抑制肥大細胞來源組織胺（cromolyn sodium）可減少 PSC 模型中膽管增殖與肝纖維化 |
| [35799467](https://pubmed.ncbi.nlm.nih.gov/35799467/) | 2022 | 細胞生物學／機轉 | Hepatology Communications | 肥大細胞透過 H2HR/cAMP/pERK1/2 訊號選擇性作用於大膽管細胞，揭示組織胺在 PSC 膽道損傷中的訊號機轉 |
| [30325540](https://pubmed.ncbi.nlm.nih.gov/30325540/) | 2019 | 代謝組學／橫斷面 | Hepatology | 血清代謝物分析可區分膽管癌、HCC 與 PSC，支持 PSC 具有獨特代謝特徵（含胺基酸代謝異常） |
| [8020893](https://pubmed.ncbi.nlm.nih.gov/8020893/) | 1994 | 回顧 | Hepatology | HLA-DR 分子特定胺基酸取代與自體免疫肝病（含 PSC）易感性相關，揭示胺基酸層面的疾病遺傳基礎 |
| [23928409](https://pubmed.ncbi.nlm.nih.gov/23928409/) | 2013 | 臨床觀察（世代） | Journal of Hepatology | 肝臟移植保存液中 microRNA 可預測移植後缺血性膽道病變（ITBL），揭示膽管上皮損傷的生物標誌物 |
| [19691661](https://pubmed.ncbi.nlm.nih.gov/19691661/) | 2010 | 臨床觀察（回溯性世代） | Transplant International | 分析 1,843 例肝臟移植患者 ITBL 危險因子，PSC 患者已排除，提供膽道損傷對照數據 |

---

## 香港上市資訊

Histidine 目前在香港無任何上市藥品許可證（總計 0 張），屬未上市狀態。如需推進臨床應用，須另行評估藥品申請途徑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

### Rank 1 — 胃輕癱

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.55%），但與胃輕癱的機轉連結薄弱，且完全缺乏臨床前與臨床研究支持，不具備推進依據。

**若要推進需要：**
- 前臨床機轉研究，確認 Histidine 是否能改善胃腸道動力
- 至少一篇與胃輕癱相關的文獻或臨床前數據

---

### Rank 2 — 硬化性膽管炎

**決策：Research Question（研究問題，暫緩推進）**

**理由：**
機轉路徑（Histidine → 組織胺）在 PSC 中具有文獻支撐，但現有證據顯示組織胺**加重** PSC 病情，補充 Histidine 的淨效應方向存在根本不確定性，無法在缺乏動物實驗直接數據的情況下推進。

**若要推進需要：**
- 在 Mdr2−/− PSC 小鼠模型中直接測試 Histidine 給藥（補充 vs. 安慰劑），量化膽管損傷與纖維化指標，釐清淨效應方向與劑量依賴性
- 補充 Histidine 的 MOA 資料（查詢 DrugBank API，DG002）
- 評估 Histidine 的抗氧化/免疫調節特性是否足以抵消組織胺促纖維化效應
- 確認香港藥品監管申請途徑（目前未上市，臨床試驗前需 IND 評估）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

