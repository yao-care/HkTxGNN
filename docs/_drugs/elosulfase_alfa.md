---
layout: default
title: Elosulfase Alfa
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 9
---

# Elosulfase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Elosulfase Alfa：從黏多糖儲積症 IVA（Morquio A）到骨骼型溶酶體儲積症

## 一句話總結

Elosulfase alfa（Vimizim®）是唯一核准用於治療黏多糖儲積症 IVA（MPS IVA，Morquio A 症候群）的酵素補充療法，透過補充 N-acetylgalactosamine-6-sulfatase（GALNS）以清除溶酶體內堆積的 keratan sulfate 及 chondroitin-6-sulfate，目前在香港**尚未上市**。TxGNN 模型共預測 9 個新適應症：排名第 1 的 **Scheie 症候群**因酵素路徑完全不符而缺乏機轉支持（Hold）；排名第 2 的**骨骼型溶酶體儲積症（Lysosomal Storage Disease with Skeletal Involvement）**直接涵蓋 MPS IVA 核心適應症，有 Phase 3 RCT 確立療效，為 **L1 等級證據**，建議 Proceed with Guardrails；其餘 7 個預測因機轉不符或無證據支持，均建議 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | MPS IVA（Morquio A syndrome）— 美國/歐洲/日本已核准，香港尚未上市 |
| TxGNN 排名第 1 預測 | Scheie syndrome（MPS IS） |
| TxGNN 分數（排名第 1） | 99.90% |
| 排名第 1 證據等級 | L5（無機轉支持，演算法偽陽性） |
| TxGNN 排名第 2 預測 | Lysosomal storage disease with skeletal involvement |
| TxGNN 分數（排名第 2） | 99.59% |
| 排名第 2 證據等級 | L1（Phase 3 RCT 已確立） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails（排名第 2） |

---

## 為什麼這個預測合理？

### 排名第 2（骨骼型 LSD）：機轉完全吻合

Elosulfase alfa 是重組人類 GALNS，以靜脈注射每週 2.0 mg/kg 方式給藥。GALNS 缺乏導致 keratan sulfate 及 chondroitin-6-sulfate 無法正常降解，於溶酶體中大量堆積，造成 MPS IVA 的特徵性骨骼表現——短軀幹型矮小、脊椎側彎後凸、韌帶鬆弛及呼吸功能受限。「骨骼型溶酶體儲積症」此大類別在疾病定義上直接涵蓋 MPS IVA（Morquio A），TxGNN 此一預測本質上反映的是藥物的已核准適應症，並非新用途。Phase 3 樞紐試驗（MOR-004）及長達 120 週的延伸研究（MOR-005）已確立療效；若該類別延伸至其他骨骼型 LSD（如 MPS VI），則需個別評估酵素特異性。

### 排名第 1（Scheie 症候群）：機轉不符，屬偽陽性

Scheie syndrome（MPS IS）為 MPS I 輕型，由 **alpha-L-iduronidase（IDUA）**缺乏所致，堆積 dermatan sulfate 及 heparan sulfate，其核准 ERT 為 laronidase（Aldurazyme®）。Elosulfase alfa 補充的是 **GALNS**，與 IDUA 路徑完全不同，底物亦無重疊，在酵素補充療法的邏輯下無法治療 MPS IS。TxGNN 高分（99.90%）可能源自知識圖譜中 MPS 大家族節點的高度拓撲相近性，屬演算法偽陽性。

---

## 臨床試驗證據（排名第 2：骨骼型 LSD）

針對「lysosomal storage disease with skeletal involvement」適應症無直接登記的臨床試驗。以下為相關 LSD 查詢中檢索到的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | 招募中 | 10 | PEARL 研究：探索多種 LSD（含 MPS IVA）產前酵素補充療法的母胎安全性與可行性，預計完成日期 2032 年 7 月 |

> ⚠️ 此試驗對「elosulfase alfa 用於 Hurler 症候群」的支持性極低；若 elosulfase alfa 納入，對應 MPS IVA 胎兒，而非 Hurler（MPS IH）。Phase 3 MOR-004 / MOR-005 試驗結果請見下方文獻。

---

## 文獻證據（排名第 2：骨骼型 LSD）

以下文獻直接涉及 elosulfase alfa 治療 MPS IVA（Morquio A）的療效與安全性。

> ⚠️ **資料品質說明**：排名第 4（Sanfilippo syndrome）文獻清單中的 19 篇文獻，逐一核查後均屬 elosulfase alfa 用於 MPS IVA 的研究（含 Phase 3 RCT 及長期延伸試驗），係系統比對誤判，已整合至本節呈現。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [24810369](https://pubmed.ncbi.nlm.nih.gov/24810369/) | 2014 | RCT（Phase 3） | J Inherit Metab Dis | 樞紐試驗 MOR-004：elosulfase alfa 2 mg/kg/週顯著改善 MPS IVA 患者 6 分鐘步行距離（主要終點）及呼吸功能 |
| [27380995](https://pubmed.ncbi.nlm.nih.gov/27380995/) | 2016 | 開放標籤延伸 RCT | Mol Genet Metab | MOR-005（96 週延伸）：確認長期療效與安全性，每週給藥（2.0 mg/kg/週）為建議劑量 |
| [29248359](https://pubmed.ncbi.nlm.nih.gov/29248359/) | 2018 | 長期延伸研究 | Mol Genet Metab | MOR-005（n=173，120 週）：ERT 改善移動能力、自我照護及日常活動能力 |
| [28535791](https://pubmed.ncbi.nlm.nih.gov/28535791/) | 2017 | 開放標籤延伸 | Orphanet J Rare Dis | 成人 MPS IVA 亞族群（≥18 歲，n=32）：120 週 ERT 相較自然史有顯著功能改善 |
| [25284089](https://pubmed.ncbi.nlm.nih.gov/25284089/) | 2015 | Phase 3 多維分析 | Mol Genet Metab | MOR-004 多域次要終點：步行耐力、尿 keratan sulfate 及生活品質多項指標改善 |
| [27553181](https://pubmed.ncbi.nlm.nih.gov/27553181/) | 2016 | 臨床研究 | J Inherit Metab Dis | MOR-005 呼吸功能子分析：長期 ERT 對 FVC 及呼吸功能的影響 |
| [25234648](https://pubmed.ncbi.nlm.nih.gov/25234648/) | 2014 | PK/PD 研究 | Clin Pharmacokinet | Phase 3 中 elosulfase alfa 的藥物動力學及藥效學評估，支持每週給藥方案 |
| [41088244](https://pubmed.ncbi.nlm.nih.gov/41088244/) | 2025 | 敘述性回顧 | Orphanet J Rare Dis | MPS IVA 治療進展回顧：ERT 為目前唯一核准療法，對骨骼發育病變療效仍有侷限 |
| [25496828](https://pubmed.ncbi.nlm.nih.gov/25496828/) | 2015 | 臨床指引 | Mol Genet Metab | Morquio 症候群脊髓壓迫的診斷評估、監測及圍手術期管理共識指引 |
| [39541578](https://pubmed.ncbi.nlm.nih.gov/39541578/) | 2024 | 系統性回顧計畫書 | JMIR Res Protoc | Morquio A 症候群基因型—表現型相關性薈萃分析計畫書 |

---

## 香港上市資訊

Elosulfase alfa 在香港**尚未取得藥品許可證**（許可證數：0），目前無任何已核准的適應症。

全球主要核准狀態如下：

| 監管機構 | 核准年份 | 商品名 | 核准適應症 |
|---------|---------|-------|-----------|
| 美國 FDA | 2014 | Vimizim® | MPS IVA（Morquio A syndrome） |
| 歐洲 EMA | 2014 | Vimizim® | MPS IVA（Morquio A syndrome） |
| 日本 PMDA | 2015 | ビミジム® | MPS IVA（Morquio A syndrome） |

---

## 全部預測摘要

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 機轉說明 |
|-----|-----------|-----------|---------|------|---------|
| 1 | Scheie syndrome | 99.90% | L5 | Hold | IDUA 缺乏，非 GALNS；酵素路徑完全不同 |
| 2 | Lysosomal storage disease with skeletal involvement | 99.59% | L1 | **Proceed with Guardrails** | 直接涵蓋 MPS IVA，Phase 3 RCT 已確立 |
| 3 | Hurler syndrome | 99.43% | L3 | Research Question | IDUA 缺乏，非 GALNS；PEARL 試驗低相關性 |
| 4 | Sanfilippo syndrome | 99.42% | L5 | Hold | ⚠️ 文獻均為 MPS IVA 研究，系統性誤判；MPS III 酵素路徑不同 |
| 5 | Camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye | 99.09% | L5 | Hold | 無機轉關聯，知識圖譜拓撲偽陽性 |
| 6 | Ptosis-vocal cord paralysis syndrome | 99.06% | L5 | Hold | 無機轉關聯，神經肌肉發育異常與 GALNS 無關 |
| 7 | Ptosis-strabismus-ectopic pupils syndrome | 99.03% | L5 | Hold | 無機轉關聯，眼部結構先天異常 |
| 8 | Ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome | 99.03% | L5 | Hold | 無機轉關聯，解剖結構發育異常 |
| 9 | Congenital Horner syndrome | 99.02% | L5 | Hold | 無機轉關聯（MPS IVA 頸脊髓壓迫為疾病併發症，非 ERT 適應方向） |

---

## 安全性考量

安全性資訊請參考原廠仿單（Vimizim® 美國仿單）。

根據 Phase 3 試驗文獻已記錄的安全性訊號：

- **免疫原性**：多數患者會產生抗藥抗體（ADA），但中和抗體（NAb）不影響臨床療效或藥物攝入（PMID [25487082](https://pubmed.ncbi.nlm.nih.gov/25487082/)、[27955919](https://pubmed.ncbi.nlm.nih.gov/27955919/)、[27789297](https://pubmed.ncbi.nlm.nih.gov/27789297/)）
- **輸注相關反應**：臨床試驗中已記錄，建議輸注前預防性給藥
- **TFDA 仿單警語/禁忌**：資料缺口（Data Gap DG001），建議補充

---

## 結論與下一步

**決策：Proceed with Guardrails（排名第 2：骨骼型溶酶體儲積症 / MPS IVA）**

**理由：**
Elosulfase alfa 治療 MPS IVA 已有 Phase 3 RCT（MOR-004）及長達 120 週的延伸研究（MOR-005，n=173）支持，並在美國、歐洲、日本取得核准，具備 L1 等級實證基礎。TxGNN 排名第 1 的 Scheie syndrome 預測因酵素路徑不符為演算法偽陽性，可過濾。

**若要推進需要：**
- 補充 MOA 詳細資料（Data Gap DG002）：確認 GALNS 機轉說明及 CI-M6PR 受體標靶機制
- 補充香港本地仿單警語與禁忌（Data Gap DG001）：下載 FDA/EMA 仿單解析
- 評估香港 MPS IVA 患者人數（極罕見疾病，需罕見疾病用藥申請途徑）
- 建立輸注反應防護計畫及免疫原性長期監測方案
- 確認衛生署罕見疾病用藥免審或特殊申請途徑（如個案進口許可）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

