---
layout: default
title: Colchicine
parent: 中證據等級 (L3-L4)
nav_order: 191
evidence_level: L4
indication_count: 3
---

# Colchicine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Colchicine：從痛風到惡性瘧疾

## 一句話總結

Colchicine 是源自秋水仙（*Colchicum autumnale*）的古老植物生物鹼，臨床上長期作為痛風急性發作的標準治療藥物，並廣泛用於家族性地中海熱（FMF）的長期預防。TxGNN 模型在本次評估中產出三項高分預測：最高分為**惡性瘧疾 (Plasmodium falciparum malaria)**（99.60%，L4，Hold）、次高分為**家族性地中海熱—體染色體顯性型（FMF autosomal dominant）**（99.38%，L1，Proceed with Guardrails）、第三為**隆突性皮膚纖維肉瘤（DFSP）**（99.37%，L5，Hold）。其中 FMF 有 **1 個臨床試驗**與 **20 篇文獻**強力支持，是本 Evidence Pack 中最具推進價值的方向。

---

## 快速總覽

| 項目 | 惡性瘧疾 | 家族性地中海熱 (FMF) | 隆突性皮膚纖維肉瘤 (DFSP) |
|------|---------|-------------------|------------------------|
| TxGNN 分數 | 99.60% | 99.38% | 99.37% |
| TxGNN 排名 | #7,735 | #10,457 | #10,653 |
| 臨床試驗數 | 0 | 1 | 0 |
| 文獻數 | 6 篇 | 20 篇 | 0 篇 |
| 證據等級 | L4 | L1 | L5 |
| 香港上市 | ✗ 未上市 | ✗ 未上市 | ✗ 未上市 |
| 許可證數 | 0 張 | 0 張 | 0 張 |
| 建議決策 | **Hold** | **Proceed with Guardrails** | **Hold** |

---

## 為什麼這些預測合理？

### 作用機轉

目前此 Evidence Pack 缺乏詳細的作用機轉資料（列為高優先度資料缺口）。根據現有文獻所揭示的資訊，Colchicine 主要透過以下機轉發揮作用：

1. **微管聚合抑制**：與 β-tubulin 結合，干擾微管聚合（polymerization），阻斷細胞有絲分裂，並抑制嗜中性球（neutrophil）的趨化移動與脫顆粒（degranulation）
2. **抗炎機轉**：抑制 NLRP3 inflammasome 活化，減少 IL-1β 的分泌，直接阻斷由 IL-1β 驅動的炎症反應

### 惡性瘧疾（Rank 1）的機轉關聯性

*Plasmodium falciparum* 含有與哺乳類同源的 α/β-tubulin 蛋白，理論上 colchicine 干擾微管聚合的機轉可抑制瘧原蟲的細胞骨架功能與分裂。體外研究顯示，tubulin 結合化合物（如 tubulozole）對 *P. falciparum* 有一定抑制活性，且 Colcemid（秋水仙素衍生物）對瘧原蟲蛋白合成有類似抑制效果，間接支持此機轉假說。然而，寄生蟲 tubulin 與哺乳類 tubulin 在分子層面存在顯著差異，colchicine 的治療選擇性（parasitic vs. host toxicity）尚未確立，目前完全缺乏臨床前動物實驗或人體試驗的直接驗證。

### 家族性地中海熱（Rank 2）的機轉關聯性

FMF 是由 MEFV 基因突變導致 pyrin 蛋白功能異常，進而引發 IL-1β 驅動週期性炎症發作的遺傳性自發炎疾病。Colchicine 透過雙重互補機轉直接對應 FMF 的病理核心：
- **IL-1β 路徑**：抑制 NLRP3/pyrin inflammasome 活化，降低 IL-1β 分泌
- **嗜中性球抑制**：透過微管干擾阻斷嗜中性球向漿膜腔的趨化聚集（即 FMF 發作的直接病理機制）

自 1977 年 *Lancet* 發表首篇報告以來，大量臨床證據確立 colchicine 為 FMF 的黃金標準治療，可顯著降低發作頻率並預防澱粉樣變性等嚴重長期併發症。

### 隆突性皮膚纖維肉瘤（Rank 3）的機轉關聯性

DFSP 以 COL1A1-PDGFB 融合基因為特徵，PDGFR 過度活化是其驅動機轉，標準標靶治療為 imatinib（PDGFR 抑制劑）。Colchicine 的抗微管機轉理論上可抑制任何增殖性細胞的有絲分裂，但此為高度非特異性機轉，且完全無 DFSP 的直接研究證據。此高分預測可能反映 TxGNN 模型對抗微管藥物在各類腫瘤中的系統性廣泛預測偏差。

---

## 適應症一：惡性瘧疾（Plasmodium falciparum Malaria）

**評估：Hold｜證據等級 L4（體外前臨床研究）**

### 臨床試驗證據

目前無相關臨床試驗登記。

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro 機轉 | Antimicrob Agents Chemother | Tubulozoles 對 *P. falciparum* 的作用機轉研究；Colcemid 對蛋白合成具類似抑制效果，支持微管為抗瘧靶點 |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro 篩選 | Cell Biol Int Rep | 9 種 tubulin 結合物對紅血球期 *P. falciparum* 的影響；寄生蟲 tubulin 與哺乳類蛋白在分子層面顯著不同 |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro 篩選 | Cell Biol Int Rep | 同上研究確認；Tubulozole-T 在哺乳類系統無活性但對瘧原蟲有效，顯示選擇性窗口存在的可能性 |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro 機轉 | PLoS One | Curcumin 干擾 *P. falciparum* 微管結構；與 HT-29、Caco-2 等癌細胞株的微管干擾機轉相似，支持微管作為抗瘧靶點的廣泛適用性 |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / 藥物抗性 | Mol Cell Biol | pfmdr1（ABC 轉運蛋白）在氯奎寧抗性中的角色；與 colchicine 的直接相關性有限，為抗性背景研究 |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | 血清學/觀察性 | Clin Exp Immunol | 82% 急性瘧疾患者血清中含抗中間絲（intermediate filaments）抗體，提示瘧疾感染與宿主細胞骨架自體免疫之關聯 |

---

## 適應症二：家族性地中海熱（Familial Mediterranean Fever, FMF）

**評估：Proceed with Guardrails｜證據等級 L1（多項系統性回顧 + 長期臨床使用）**

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | 觀察性（N/A） | 招募中 | 25 | 評估 Canakinumab（IL-1β 抗體）用於 **colchicine 抵抗型/不耐受型 FMF** 患者的安全性與有效性（REASSURE 研究）。試驗入組條件間接確認 colchicine 為 FMF 必嘗試的第一線標準治療 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [68234](https://pubmed.ncbi.nlm.nih.gov/68234/) | 1977 | 臨床報告 | Lancet | Colchicine 在 FMF 中應用的早期里程碑報告，奠定後續數十年臨床使用基礎 |
| [37298536](https://pubmed.ncbi.nlm.nih.gov/37298536/) | 2023 | Review / Update | Int J Mol Sci | FMF 最新文獻總覽；colchicine 為核心標準治療，可預防澱粉樣變性等長期嚴重併發症，並涵蓋治療抵抗與依從性議題 |
| [38354004](https://pubmed.ncbi.nlm.nih.gov/38354004/) | 2023 | Review | Rev Praticien | Colchicine 長期預防 FMF 發作，通常自幼年即開始使用；MEFV 基因（exon 10）突變確診 |
| [37903671](https://pubmed.ncbi.nlm.nih.gov/37903671/) | 2023 | 臨床診療指引 | Rev Med Interne | 法國 FMF 診斷與管理協定；colchicine 為治療核心，自幼年起長期使用 |
| [28413100](https://pubmed.ncbi.nlm.nih.gov/28413100/) | 2017 | Review | Semin Arthritis Rheum | Colchicine 黃金標準地位確立；約 5% 患者有抵抗性或不耐受，需 anakinra/canakinumab 等生物製劑作為二線治療 |
| [29526329](https://pubmed.ncbi.nlm.nih.gov/29526329/) | 2018 | Review | Rev Med Interne | FMF 最常見的單基因自發炎疾病；pyrin 活化促進 IL-1β 分泌，colchicine 阻斷此路徑 |
| [39404483](https://pubmed.ncbi.nlm.nih.gov/39404483/) | 2024 | 專家共識/會議 | Clin Exp Rheumatol | 第 2 屆 FMF 大會，涵蓋最新治療共識與未來研究方向 |
| [35789271](https://pubmed.ncbi.nlm.nih.gov/35789271/) | 2023 | 回溯性研究 | Mod Rheumatol | 探討 colchicine 抵抗的早期預測因子，有助於早期識別需升階治療的患者 |
| [35061158](https://pubmed.ncbi.nlm.nih.gov/35061158/) | 2022 | 回溯性世代研究 | Intern Emerg Med | 晚發型 FMF（40 歲後）的臨床與基因特徵比較，colchicine 為所有年齡層的標準治療 |
| [20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/) | 2010 | Review / 毒理學 | Clin Toxicol | Colchicine 治療指數窄，毒性與致死劑量界限不清；主要適應症為痛風與 FMF，需謹慎用藥 |

---

## 適應症三：隆突性皮膚纖維肉瘤（Dermatofibrosarcoma Protuberans, DFSP）

**評估：Hold｜證據等級 L5（僅模型預測，無任何研究支持）**

目前無任何臨床試驗登記或文獻支持 colchicine 用於 DFSP。DFSP 為罕見皮膚軟組織腫瘤，以 COL1A1-PDGFB 融合基因為特徵，imatinib（PDGFR 抑制劑）是目前標準標靶治療。在有更具特異性的標靶治療可選的情況下，colchicine 的非特異性抗有絲分裂機轉無實質優先推進的根據。

---

## 香港上市資訊

Colchicine 在香港目前**未取得任何藥物許可證**（0 張），尚未上市。

如需臨床使用，需透過香港衛生署特殊用藥申請（Special Drug Import）途徑，或考慮其他法規路徑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **重要提示**：根據文獻（PMID 20586571），Colchicine 治療指數（therapeutic index）極窄，無毒性、中毒與致死劑量之間的界限尚不明確，臨床上曾有嚴重的非刻意中毒案例。使用時應嚴格監控劑量，特別是合併使用 CYP3A4 或 P-glycoprotein 抑制劑時。

---

## 結論與下一步

### 適應症一：惡性瘧疾

**決策：Hold**

**理由：**
TxGNN 高分（99.60%）源自 colchicine 與 *P. falciparum* tubulin 之間的間接機轉相似性，但目前所有支持證據均為 1980–2013 年間的體外研究，缺乏動物模型及任何人體試驗數據，且抗瘧選擇性未被確立。

**若要推進需要：**
- 直接針對 colchicine 的 *P. falciparum* 體外 IC₅₀ 測定（而非間接引用微管結合物研究）
- 小鼠瘧疾感染模型的有效性與安全性驗證
- 人類與寄生蟲 tubulin 結合選擇性的結構生物學分析
- 與現有第一線抗瘧藥物（artemisinin、chloroquine）的比較實驗

---

### 適應症二：家族性地中海熱（FMF）

**決策：Proceed with Guardrails**

**理由：**
Colchicine 在 FMF 治療中已有近 50 年的臨床使用歷史（自 1977 年 Lancet 報告起），多項系統性回顧、臨床指引及觀察性研究均確認其為 FMF 的黃金標準第一線治療，FMF 實際上是 colchicine 的公認核心適應症，TxGNN 預測與現有醫學實踐高度吻合。

**若要推進需要：**
- 取得 Colchicine 完整 MOA 文件（補足資料缺口 DG002）
- 評估香港法規申請路徑（目前 0 張許可證，需特殊申請）
- 制定特殊患者族群（孕婦、兒童、腎功能不全者）安全性監測計畫
- 建立 colchicine 抵抗型 FMF 患者（約 5%）的升階治療銜接策略
- 取得 TFDA/香港 DoH 核准仿單以補足警語資料（補足資料缺口 DG001）

---

### 適應症三：隆突性皮膚纖維肉瘤（DFSP）

**決策：Hold**

**理由：**
無任何直接研究支持，DFSP 有成熟有效的標靶治療（imatinib），優先順位極低，建議不予推進。

---

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。所有老藥新用候選均需經過嚴格臨床驗證方可應用於臨床實踐。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

