---
layout: default
title: Imatinib
parent: 高證據等級 (L1-L2)
nav_order: 390
evidence_level: L2
indication_count: 10
---

# Imatinib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Imatinib：從原適應症資料缺口到纖維肉瘤家族腫瘤（Fibrosarcoma Spectrum）

## 一句話總結

> Imatinib（DrugBank ID: DB00619）之原始適應症與作用機轉資料在本次 Evidence Pack 中皆為缺口（Data Gap DG001／DG002），香港目前也**未上市**（0 張許可證）。
> TxGNN 模型針對此藥物產出 **10 個潛在新適應症**，全部集中於**纖維肉瘤／軟組織肉瘤譜系**，其中證據最堅實的是 **Conventional Fibrosarcoma（含 Dermatofibrosarcoma Protuberans, DFSP）**，已有 **1 個已完成的 Phase II 臨床試驗**與 **9 篇相關文獻**支持；其餘多數預測（如 heart fibrosarcoma、familial Mediterranean fever 等）目前**完全無臨床試驗或文獻佐證**，屬於模型分數外推。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（Evidence Pack 未提供 original_indications／original_moa；DG001、DG002） |
| 預測新適應症（主候選） | Conventional Fibrosarcoma（含 DFSP） |
| TxGNN 預測分數 | 99.93%（全體疾病節點排名第 1898 位） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Proceed with Guardrails**（僅限 Conventional Fibrosarcoma／DFSP 亞群；其餘 9 項預測多屬 Hold，詳見下表） |

### 10 項預測適應症全覽（依 TxGNN 分數排序）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Heart Fibrosarcoma | 99.94% | L5 | S0 | Hold |
| 2 | Fibroblastic Neoplasm（含 DFSP） | 99.94% | L3 | S1 | Research Question |
| 3 | **Conventional Fibrosarcoma** | 99.93% | **L2** | **S2** | **Proceed with Guardrails** |
| 4 | Kidney Fibrosarcoma | 99.93% | L4 | S0 | Research Question |
| 5 | Low Grade Fibromyxoid Sarcoma | 99.93% | L5 | S0 | Hold |
| 6 | Liposarcoma | 99.88% | L2 | S1 | Research Question |
| 7 | Liver Fibrosarcoma | 99.86% | L4 | S0 | Hold |
| 8 | 家族性地中海熱 (FMF) | 99.86% | L5 | S0 | Hold |
| 9 | 卵巢黏液樣脂肪肉瘤 | 99.85% | L5 | S0 | Hold |
| 10 | 家族性橫紋肌樣腫瘤 | 99.83% | L5 | S0 | Hold |

> 注意：TxGNN 分數本身皆 >99.8%，區辨力有限；排名（rank）與實證資料量才是判斷候選優先順序的關鍵依據。

---

## 為什麼這個預測合理？

目前缺乏 Imatinib 詳細的原始適應症與正式作用機轉資料（Evidence Pack Data Gap DG001「TFDA 仿單警語/禁忌」、DG002「作用機轉」皆列為待補項目）。

但根據本次收集之文獻內容可確認：Imatinib 是一種酪氨酸激酶抑制劑，標的包含 BCR-ABL、KIT 及**血小板衍生生長因子受體（PDGFR）**（PMID 15794712、18230575）。本次多項高分預測的共同分子基礎，正是 **PDGFB/PDGFRB 訊號路徑異常活化**：

- **Conventional Fibrosarcoma（含 DFSP）**：帶有 t(17;22)(q22;q13) 染色體易位，形成 **COL1A1-PDGFB 融合基因**，導致 PDGFRB 持續性活化（PMID 19635106、25852058）。此為 Imatinib 標的直接吻合的分子機轉，且已有真實世界文獻報告約 50% 病人對 Imatinib 有臨床反應（PMID 25852058），2025 年歐洲跨學科指引亦將 Imatinib 列為晚期/無法切除 DFSP 之治療選項（PMID 39904126）。
- **Liposarcoma**：部分亞型表現 c-KIT，理論上可能對 Imatinib 有反應（PMID 12702540），但也有陰性報告顯示 Imatinib 對部分 KIT+ 腹膜後脂肪肉瘤無效（PMID 17708241），顯示此適應症異質性高、需以生物標記篩選病人。
- 其餘 7 項預測（heart/kidney/liver fibrosarcoma、FMF、卵巢黏液樣脂肪肉瘤、家族性橫紋肌樣腫瘤等）**缺乏對應部位或病理亞型的臨床/文獻證據**，部分（如 FMF 為 pyrin inflammasome 過度活化、家族性橫紋肌樣腫瘤為 SMARCB1/SMARCA4 缺失）機轉上與 Imatinib 標的**無直接關聯**，較可能是知識圖譜鄰近節點產生的假陽性。

---

## 臨床試驗證據

以下為與 Imatinib 直接相關、已完成之試驗（排除以 Sunitinib、Regorafenib 為研究藥物之對照/延伸試驗 NCT00400569、NCT02048371，該兩者僅供同類藥物間接參考）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | 完成 | 17 | Glivec (Imatinib) 用於帶有 COL1A1/PDGFB 融合基因之局部晚期/轉移性 DFSP 及巨細胞纖維母細胞瘤 |
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase 2 | 完成 | N/A | Gleevec (Imatinib) 用於轉移性/無法切除之軟組織及骨肉瘤（North American Sarcoma Study Group 多中心試驗） |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase 1/2 | 完成 | 91 | STI571 (Imatinib) 劑量摸索及療效評估，用於復發/難治性軟組織肉瘤（含 liposarcoma 等亞型，籃式設計） |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | 完成 | 185 | Imatinib 用於多種危及生命之罕見惡性疾病，探討 PDGFR/KIT 等酪氨酸激酶相關疾病之反應性（籃式試驗，非部位專一） |

> 上述試驗均為軟組織肉瘤廣泛族群之籃式設計，對 conventional fibrosarcoma 以外的部位專一亞型（heart/kidney/liver fibrosarcoma 等）**無專一性數據**。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline | Eur J Cancer | 歐洲跨學科指引更新：DFSP 診斷與治療，將 Imatinib 列為晚期/不可切除病例之藥物選項 |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Cohort/Mechanistic | Mol Cancer Ther | Imatinib 對約 50% 無法切除/轉移性 DFSP 病人有臨床效益；亦提出 CDK4 為 Imatinib 抗藥性 DFSP 之潛在標的 |
| [19635106](https://pubmed.ncbi.nlm.nih.gov/19635106/) | 2009 | Cohort | Histopathology | 20 例 DFSP 之 COL1A1-PDGFB 轉錄本分析，闡明治療意涵 |
| [33449152](https://pubmed.ncbi.nlm.nih.gov/33449152/) | 2021 | Mechanistic Review | Cell Mol Life Sci | PDGFRA/PDGFRB 突變與人類疾病的關聯總覽，PDGFRB 驅動肌纖維瘤發生 |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Review | J Surg Oncol | DFSP 手術治療現況，提及 Imatinib 用於晚期/無法切除病例之藥物治療 |
| [26027711](https://pubmed.ncbi.nlm.nih.gov/26027711/) | 2015 | Review | Expert Rev Anticancer Ther | DFSP 現行治療選項回顧，PDGFB 自分泌/旁分泌刺激為核心致病機轉 |
| [12702540](https://pubmed.ncbi.nlm.nih.gov/12702540/) | 2003 | Case Series/Mechanistic | Ann Oncol | 表現 c-KIT (CD117) 之眼部黑色素瘤與脂肪肉瘤，探討 Imatinib 潛在應用 |
| [17708241](https://pubmed.ncbi.nlm.nih.gov/17708241/) | 2007 | Case Report（陰性結果） | Hepatogastroenterology | 2 例 KIT+ 腹膜後脂肪肉瘤對 Imatinib **無治療反應** |
| [15794712](https://pubmed.ncbi.nlm.nih.gov/15794712/) | 2005 | Review | Expert Opin Drug Saf | Imatinib 開發與臨床應用綜述，酪氨酸激酶抑制劑作用機轉說明 |
| [18230575](https://pubmed.ncbi.nlm.nih.gov/18230575/) | 2008 | Review | Bull Cancer | Imatinib 於實體腫瘤之應用，涵蓋 c-abl、c-kit、PDGFR 抑制活性 |

> 已刻意納入 1 篇陰性結果文獻（PMID 17708241），提醒 liposarcoma 適應症之療效並非一致，需以生物標記篩選病人。

---

## 香港上市資訊

Imatinib 目前於香港**未有任何許可證登記**（market_status：未上市，total_licenses：0），故無法提供核准適應症或劑型資訊。

---

## 細胞毒性

Imatinib 屬抗腫瘤藥物（廣泛用於 CML、GIST 等腫瘤，且本次多項預測適應症皆為腫瘤），故列出以下資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪氨酸激酶抑制劑：BCR-ABL / KIT / PDGFR 抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項（Evidence Pack 無 toxicity 資料） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。（本次 Evidence Pack 之主要警語、禁忌症、DDI 查詢均為資料缺口，其中 TFDA/香港仿單警語與禁忌屬 **Blocking** 等級缺口，須優先補齊才能進入 S1 安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅限 Conventional Fibrosarcoma／DFSP 亞群；其餘 9 項預測適應症建議 **Hold**）

**理由：**
- Conventional Fibrosarcoma（含 DFSP）具備 L2 等級證據：1 個已完成之 Phase II 臨床試驗（NCT00085475，n=17）、COL1A1-PDGFB 融合基因之明確分子機轉，以及 2025 年歐洲跨學科指引已將 Imatinib 列為治療選項，決策階段達 S2。
- 其餘預測（heart/kidney/liver fibrosarcoma、低度惡性纖維黏液樣肉瘤、FMF、卵巢黏液樣脂肪肉瘤、家族性橫紋肌樣腫瘤）皆無部位專一之臨床試驗或文獻證據（0/0），且部分機轉上與 Imatinib 標的（BCR-ABL/KIT/PDGFR）並無直接關聯，判定為模型分數外推之假陽性可能性高。
- 安全性資料（TFDA 仿單警語、禁忌症）為 **Blocking** 等級缺口，在補齊前無法完成任何適應症之 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA／香港衛生署官方仿單警語與禁忌症資料（解決 DG001 Blocking 缺口）
- 取得完整 DrugBank MOA 與毒理資料，強化機轉論述與骨髓抑制/致吐性風險評估（解決 DG002）
- 針對 Conventional Fibrosarcoma／DFSP，補充是否有更新（近5年）之前瞻性試驗數據，並確認香港/亞太地區是否已有註冊案例
- 若欲推進 Liposarcoma 適應症，建議先以 c-KIT/PDGFR 免疫組織化學表現作為病人篩選條件，並正視現有陰性案例報告（PMID 17708241）
- 其餘 7 項低證據等級預測，暫緩投入資源，待未來新增臨床試驗或文獻證據後再重新評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

