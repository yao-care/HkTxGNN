---
layout: default
title: Cytarabine
parent: 高證據等級 (L1-L2)
nav_order: 202
evidence_level: L2
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **9** 個
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

# Cytarabine（阿糖胞苷）：從急性白血病到多種腫瘤適應症（9 項預測）

## 一句話總結

Cytarabine（阿糖胞苷，Ara-C）是一種 S 期特異性嘧啶拮抗劑，長期作為急性髓系白血病（AML）的核心治療藥物，目前在香港未有已登記許可證。TxGNN 模型為 Cytarabine 預測了 **9 項新適應症**，其中以**原發性肺淋巴瘤（Primary Pulmonary Lymphoma）** 的臨床依據最為充分（L2 級，Proceed with Guardrails），另有**小細胞肺癌**、**神經母細胞瘤** 及**腹膜後腫瘤（髓系肉瘤亞型）** 具備可研究性支持（L3 級），其餘適應症目前建議暫緩（Hold）。

---

## 快速總覽 — 全部預測適應症

| 排名 | 疾病 | TxGNN 分數 | 臨床試驗數 | 文獻數 | 證據等級 | 決策 |
|------|------|-----------|-----------|--------|---------|------|
| 1 | 小細胞肺癌 | 99.78% | 3 | 20 | L3 | Research Question |
| **2** | **原發性肺淋巴瘤** | **99.78%** | **7** | **20** | **L2** | **Proceed with Guardrails** |
| 3 | 分化良好胎兒型肺腺癌 | 99.76% | 0 | 0 | L5 | Hold |
| 4 | 肺胚瘤 | 99.76% | 0 | 0 | L5 | Hold |
| 5 | 上呼吸消化道腫瘤 | 99.49% | 0 | 20 | L4 | Hold |
| 6 | 節細胞神經母細胞瘤 | 99.36% | 0 | 0 | L5 | Hold |
| 7 | 脊椎異常伴內分泌/T 細胞功能障礙 | 99.32% | 0 | 0 | L5 | Hold（疑假陽性）|
| 8 | 腹膜後腫瘤 | 99.23% | 1 | 14 | L3* | Research Question |
| 9 | 神經母細胞瘤 | 99.19% | 5 | 20 | L3 | Research Question |

> \* L3 僅適用於髓系肉瘤（Myeloid Sarcoma）亞型；其他組織學亞型降至 L5，不具直接依據。

---

## 關於 Cytarabine 的基礎認識

目前 Evidence Pack 缺乏詳細的作用機轉資料。根據文獻中的描述，Cytarabine（Ara-C，胞嘧啶阿拉伯糖苷）是一種結構類似去氧胞苷的核苷類似物，進入細胞後被磷酸化為活性代謝物 Ara-CTP，透過競爭性抑制 DNA 聚合酶干擾 DNA 合成。它屬於 **S 期特異性（phase-specific）** 藥物，對增殖指數高的腫瘤（如白血病、高惡性度淋巴瘤、小細胞癌）作用最顯著；對分裂緩慢的分化良好型固態腫瘤效益相對有限。相關衍生物（如 Gemcitabine）已廣泛用於實體腫瘤，提示嘧啶拮抗劑類別效應在實體瘤中具有一定空間。

> **香港上市狀態**：Cytarabine 在香港**未上市**，無已登記許可證。若考慮用於研究或特殊用途，需透過香港衛生署進口特許藥物申請途徑處理。

---

## 適應症一（最高優先）：原發性肺淋巴瘤（Primary Pulmonary Lymphoma）

### 快速概覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 原發性肺淋巴瘤（Primary Pulmonary Lymphoma） |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

### 為什麼這個預測合理？

原發性肺淋巴瘤主要分為兩大亞型：(1) **MALT 淋巴瘤**（低惡性度，多數不需化療，預後良好）；(2) **瀰漫性大 B 細胞淋巴瘤（DLBCL）**（高惡性度，治療等同系統性 DLBCL，需積極化療）。

Cytarabine 在侵襲性 B 細胞淋巴瘤中已確立核心地位，具體體現在三個層面：

第一，**BEAM 預處理方案**（BCNU + Etoposide + **Ara-C** + Melphalan）是淋巴瘤自體幹細胞移植（ASCT）的黃金標準，在 NCT00345865（n=473）等大型試驗中充分驗證了安全性與療效。第二，**OFAR 方案**（Oxaliplatin + Fludarabine + **Ara-C** + Rituximab）在 Richter 症候群（CLL 轉化為 DLBCL）的 Phase 1/2 試驗（NCT00452374, n=48）中直接展示 Cytarabine 對侵襲性 B 細胞淋巴瘤的療效。第三，**高劑量 MTX + Cytarabine** 已是原發性 CNS 淋巴瘤的標準一線方案（PMID 12241119）。

肺部 DLBCL 的生物學行為與系統性 DLBCL 高度一致，上述方案具強烈的生物學外推依據，支持 L2 評級。

⚠️ **重要警示**：MALT 淋巴瘤亞型通常不需要高強度化療，治療前組織病理學分型（MALT vs. DLBCL）至關重要，不可省略。

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00452374](https://clinicaltrials.gov/study/NCT00452374) | Phase 1/2 | 完成 | 48 | OFAR 方案（含 Cytarabine）用於 Richter 症候群（CLL→DLBCL 轉化），為 Cytarabine 用於侵襲性 B 細胞淋巴瘤最直接的臨床依據 |
| [NCT00345865](https://clinicaltrials.gov/study/NCT00345865) | Phase 2 | 完成 | 473 | 淋巴瘤自體幹細胞移植（含 BEAM 預處理），迄今最大規模 BEAM 淋巴瘤試驗，安全性資料豐富 |
| [NCT02443077](https://clinicaltrials.gov/study/NCT02443077) | Phase 3 | 進行中（不再招募） | 94 | ibrutinib vs. 安慰劑於 ASCT 後維持治療（含 BEAM 預處理），大型 DLBCL 移植試驗 |
| [NCT01476839](https://clinicaltrials.gov/study/NCT01476839) | Phase 1 | 完成 | 25 | Y-90 抗 CD25 + BEAM 用於難治型 Hodgkin 淋巴瘤 ASCT，Cytarabine 安全性資料 |
| [NCT02356159](https://clinicaltrials.gov/study/NCT02356159) | Phase 1/2 | 完成 | 34 | Palifermin 支持性治療於 HLA 配對異體 HSCT，提供 HSCT 背景毒性管理框架 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [41117344](https://pubmed.ncbi.nlm.nih.gov/41117344/) | 2025 | Phase II RCT | Hematol Oncol | BV + BeEAM（含 Cytarabine）vs. BeEAM 用於 CD30+ 淋巴瘤大劑量化療，隨機試驗 |
| [38024477](https://pubmed.ncbi.nlm.nih.gov/38024477/) | 2023 | RCT | EClinicalMedicine | BendaEAM vs. BEAM 用於復發淋巴瘤 ASCT 的首個隨機對照試驗 |
| [38555923](https://pubmed.ncbi.nlm.nih.gov/38555923/) | 2024 | Phase I | Lancet Haematol | 抗 CD30 CAR-T + ASCT 鞏固治療高危 CD30+ 淋巴瘤，Phase I 安全性確認 |
| [12241119](https://pubmed.ncbi.nlm.nih.gov/12241119/) | 2002 | Phase II | J Neuro-Oncol | 高劑量 MTX + Cytarabine 治療原發性 CNS 淋巴瘤（n=14），支持 Cytarabine 用於淋巴瘤腦部侵犯 |
| [29217775](https://pubmed.ncbi.nlm.nih.gov/29217775/) | 2018 | 機制研究 | Haematologica | Cytarabine 在不同 B 細胞淋巴瘤中的差異性細胞週期阻滯機制，探討 Wee1 抑制劑協同潛力 |
| [7804123](https://pubmed.ncbi.nlm.nih.gov/7804123/) | 1994 | 臨床試驗 | Stem Cells | CBV/BEAM 大劑量化療於 Hodgkin 病的 ASCT，長期無病存活達 50% |
| [27165090](https://pubmed.ncbi.nlm.nih.gov/27165090/) | 2016 | Phase I/II | Ann Hematol | 三次 ASCT + 改良 BEAM（不同劑量）用於復發侵襲性 NHL，可行性評估 |

### 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Cytarabine 已作為 BEAM 方案核心成分廣泛用於淋巴瘤 ASCT，OFAR 方案在侵襲性 B 細胞淋巴瘤（Richter 症候群）中直接展示療效，且高劑量 MTX + Cytarabine 為 CNS 淋巴瘤標準方案；生物學外推至肺部 DLBCL 依據充分，達 L2 證據等級。

**若要推進需要：**
- 組織病理學確認亞型（DLBCL vs. MALT），方可決定是否適用高強度化療
- 啟動原發性肺 DLBCL 的前瞻性病例系列研究或回顧性分析
- 向香港衛生署申請 Cytarabine 進口特許（研究用途）
- 制定骨髓抑制及感染性併發症的系統性監測方案

---

## 適應症二：小細胞肺癌（Small Cell Lung Carcinoma）

### 快速概覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 小細胞肺癌（Small Cell Lung Carcinoma, SCLC） |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 建議決策 | Research Question |

### 為什麼這個預測合理？

SCLC 具有極高的腫瘤增殖指數（Ki-67 常 > 80%），理論上是 S 期特異性藥物 Cytarabine 的最佳靶點。歷史文獻（1979 年，PMID 232239）記載 Ara-C + 環磷醯胺 + Adriamycin 聯合放療治療 20 例初診 SCLC，取得 78% 緩解率（中位存活 49+ 週完全緩解）。1988 年的 VP-16 + 持續輸注 Ara-C 研究（PMID 2841844）及 1984 年的 CAV + Ara-C 研究（PMID 6095640）進一步補充了 SCLC 的歷史證據。腦膜轉移場景下，有個案報告記錄鞘內 Cytarabine 於 SCLC 腦膜轉移的使用（PMID 28223673）。

然而，現行 SCLC 標準方案（EP/EC + Atezolizumab 免疫化療）已高度確立，上述歷史試驗均屬小樣本老年研究，缺乏近代對照試驗支持。Cytarabine 的再利用空間主要限於**復發難治性 SCLC** 或**腦膜轉移亞族群**。

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | 已終止 | 34 | NSCLC 輔助化療試驗（疾病類型不符 SCLC，且已終止，無有效數據） |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | 完成 | 13 | 鞘內 Pemetrexed 用於 NSCLC 腦膜轉移；提供鞘內化療路徑參考 |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | 完成 | 34 | 鞘內 Pemetrexed + 涉野放療用於腦膜轉移（含 NSCLC），間接支持 CNS 化療路徑 |

> 注意：以上試驗與 SCLC 直接相關性有限，主要提供腦膜轉移治療路徑的間接參考。

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | 臨床試驗 | Med Pediatr Oncol | Ara-C + 環磷醯胺 + Adriamycin + 放療治療 SCLC（n=20），緩解率 78% |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | 臨床試驗 | Am J Clin Oncol | VP-16 + 持續輸注 Ara-C 用於難治性 SCLC（n=17），探討耐藥後挽救治療 |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | 臨床試驗 | Am J Clin Oncol | Ara-C 持續輸注單藥及 CAV + Ara-C 組合用於 SCLC（n=35），含廣泛期患者 |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | J Clin Oncol | CALGB 隨機試驗：限制期 SCLC 化療 ± 華法林（含 Cytarabine 方案），評估抗凝治療影響 |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | 病例報告 | Gan to Kagaku Ryoho | SCLC 腦膜轉移個案，鞘內 Cytarabine 多學科治療，提供 CNS 治療場景參考 |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | 基礎研究 | Biochem Pharmacol | 耐藥（拓撲異構酶抑制劑）SCLC 細胞株對 Cytarabine 呈旁系敏感性，提示耐藥後再利用潛力 |

### 結論與下一步

**決策：Research Question**

**理由：**
歷史臨床試驗支持 Cytarabine 用於 SCLC，但均為 1980-1990 年代小樣本研究，缺乏近代免疫治療時代的對照試驗；現行標準方案已確立，再利用空間限於特定亞族群。

**若要推進需要：**
- 明確鎖定靶向族群：復發難治性 SCLC 或 SCLC 腦膜轉移
- 考慮設計 Pilot 研究評估鞘內 Cytarabine 於 SCLC 腦膜轉移
- 需先完成現代化劑量安全性評估（結合現行支持療法標準）

---

## 適應症三：神經母細胞瘤（Neuroblastoma）

### 快速概覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 神經母細胞瘤（Neuroblastoma） |
| TxGNN 預測分數 | 99.19% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 建議決策 | Research Question |

### 為什麼這個預測合理？

Cytarabine 對神經母細胞瘤具有多重、獨特的機轉依據，且涵蓋細胞毒性與分化誘導兩個層面：

**（1）分化誘導機轉**：低劑量 Ara-C（低至 0.1 μg/ml，約臨床劑量的 1/1000）即可在 NB 細胞株中誘導形態學與表型的神經元分化（PMID 2917605），且與 Gamma-interferon、Retinoic Acid 作用機轉不同，具協同聯合潛力（PMID 1751963）。

**（2）直接細胞毒性**：多項 NB 細胞株體外研究證實 Ara-C 具有抗增殖活性（PMID 7529082, 7576981），且耐藥（拓撲異構酶抑制劑）的 SCLC 細胞株對 Cytarabine 呈現旁系敏感性，推測類似機制可能存在於 NB。

**（3）增敏策略**：CTP 合成酶抑制劑 Cyclopentenyl cytosine（CPEC）前處理可使 NB 細胞對 Cytarabine 的敏感性增加 2-8 倍（PMID 12471622），提供聯合方案設計依據。

**（4）新型遞藥系統**：Cytarabine 載入碳點奈米材料在 NB 細胞中展現協同光熱-化療效應（PMID 36688816），代表現代轉化研究的前沿方向。

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02130869](https://clinicaltrials.gov/study/NCT02130869) | Phase 1 | 完成 | 8 | 單倍體 NK 細胞 + CD133+ 自體幹細胞移植（含 Cytarabine 清骨髓預處理）用於高危 NB，提供安全性前驅數據 |
| [NCT06942039](https://clinicaltrials.gov/study/NCT06942039) | Early Phase 1 | 招募中 | 15 | 鞘內 Topotecan + 維持化療用於 < 6 歲 NB 鞏固後（2025 年啟動），現代 NB 鞏固後治療框架 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [2917605](https://pubmed.ncbi.nlm.nih.gov/2917605/) | 1989 | 基礎研究 | Exp Cell Res | 低劑量 Ara-C 誘導人類 NB 細胞株（GI-ME-N）形態分化，0.1 μg/ml 即有效 |
| [1751963](https://pubmed.ncbi.nlm.nih.gov/1751963/) | 1991 | 基礎研究 | Cell Mol Neurobiol | γ-IFN、Retinoic Acid、Ara-C 透過不同機轉誘導 LAN-1、GI-ME-N 分化，具協同潛力 |
| [1358448](https://pubmed.ncbi.nlm.nih.gov/1358448/) | 1992 | 基礎研究 | Cell Mol Neurobiol | Ara-C 等藥物誘導 LAN-5 NB 細胞的生化與形態分化，綜合評估 |
| [12471622](https://pubmed.ncbi.nlm.nih.gov/12471622/) | 2003 | 基礎研究 | Int J Cancer | CPEC 前處理增強 SK-N-BE(2)c NB 細胞對 Cytarabine 毒性 2-8 倍 |
| [7529082](https://pubmed.ncbi.nlm.nih.gov/7529082/) | 1993 | 臨床/體外 | Cancer Biother | NB 患者及親屬淋巴細胞對 Ara-C 及 Bleomycin 的染色體不穩定性分析 |
| [36688816](https://pubmed.ncbi.nlm.nih.gov/36688816/) | 2023 | 轉化研究 | ACS Appl Mater Interfaces | Cytarabine 載入碳點在 NB 細胞中展現光觸發協同光熱-化療效應 |
| [3316512](https://pubmed.ncbi.nlm.nih.gov/3316512/) | 1987 | 臨床試驗 | J Clin Oncol | N4SE 方案（含 Ara-C）用於 100 例進展期 NB，1 歲以下患者 CR/GPR 達 85% |

### 結論與下一步

**決策：Research Question**

**理由：**
多項體外研究證明 Cytarabine 對 NB 具分化誘導及細胞毒性雙重活性，N4SE 方案中的歷史臨床使用及小型移植試驗的間接使用記錄支持 L3 評級。

**若要推進需要：**
- 系統性體外劑量反應研究（低劑量分化誘導 vs. 高劑量細胞毒性策略比較）
- NB 異種移植動物模型體內療效評估
- 考慮低劑量 Ara-C + Retinoic Acid 聯合分化誘導方案設計

---

## 適應症四：腹膜後腫瘤（Retroperitoneal Neoplasm）—— 髓系肉瘤亞型

### 快速概覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 腹膜後腫瘤（Retroperitoneal Neoplasm） |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L3（限髓系肉瘤亞型） |
| 香港上市 | ✗ 未上市 |
| 建議決策 | Research Question |

### 為什麼這個預測合理？

腹膜後腫瘤為組織學高度異質性疾病群（脂肪肉瘤、平滑肌肉瘤、髓系肉瘤、生殖細胞腫瘤等）。文獻分析揭示一關鍵亞族群：**髓系肉瘤（Myeloid Sarcoma / Granulocytic Sarcoma）** 常以腹膜後腫瘤形式初次呈現（PMID 39588445, 34733617, 41366933, 12656749），其本質為 AML 的髓外表現，而 Cytarabine-based 誘導方案（如 7+3 方案）已是髓系肉瘤的 **L1 級標準治療**。

⚠️ **決策關鍵**：若組織病理為其他軟組織肉瘤亞型（脂肪肉瘤、平滑肌肉瘤等），Cytarabine 缺乏任何直接依據，此預測不適用。臨床決策必須以病理確認為前提。

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [39588445](https://pubmed.ncbi.nlm.nih.gov/39588445/) | 2024 | 病例報告 + 42 例回顧 | Cureus | 宮頸部髓系肉瘤（無白血病）：系列回顧確認髓系肉瘤可呈現為局部腫瘤 |
| [41366933](https://pubmed.ncbi.nlm.nih.gov/41366933/) | 2025 | 病例報告 | Medicine | 縱隔/腹膜後髓系肉瘤壓迫食道，Cytarabine-based AML 方案治療 |
| [34733617](https://pubmed.ncbi.nlm.nih.gov/34733617/) | 2021 | 病例報告 | World J Clin Oncol | 原發性胃髓系肉瘤：de novo 髓外 AML 呈現 |
| [12656749](https://pubmed.ncbi.nlm.nih.gov/12656749/) | 2003 | 病例報告 | Eur J Haematol | AML 以雙側睪丸腫塊 + 腹膜後腫瘤形式呈現，Cytarabine-based 誘導治療 |

### 結論與下一步

**決策：Research Question**

**理由：**
髓系肉瘤亞型的腹膜後腫瘤具備強烈 Cytarabine 使用依據（AML 標準方案），但整體「腹膜後腫瘤」診斷高度異質，決策完全取決於病理分型。

**若要推進需要：**
- 組織病理學 + 免疫組化 + 細胞遺傳學確認（髓系肉瘤需 CD34/CD117/MPO 陽性）
- 若確認為髓系肉瘤：直接採用標準 AML 誘導方案（7+3 或 CPX-351）
- 若為其他軟組織肉瘤亞型：此預測不適用，排除

---

## 低優先級適應症摘要

| 疾病 | 證據等級 | 決策 | 評估摘要 |
|------|---------|------|---------|
| 上呼吸消化道腫瘤 | L4 | Hold | 1989 年 Ara-C + Cisplatin 先導研究（n=16）有 38% 緩解率（PMID 2589230），2002 年高劑量 Ara-C + Cisplatin + 5-FU 隨機研究（PMID 12110494）；但現行頭頸鱗癌標準方案已轉向免疫檢查點抑制劑，缺乏 2000 年後對照試驗，口腔黏膜炎毒性在頭頸放化療場景需特別管理，暫不推進 |
| 節細胞神經母細胞瘤 | L5 | Hold | 源於神經母細胞瘤知識圖譜路徑延伸，理論上對未分化細胞群可能有效，但無任何直接臨床試驗或文獻支持，屬生物學合理的純預測階段 |
| 分化良好胎兒型肺腺癌 | L5 | Hold | 低增殖指數的分化良好型腫瘤與 S 期特異性機轉相悖，常見 CTNNB1 突變的生物學特性亦不支持；TxGNN 高分可能來自「肺癌→化療藥物」通用路徑，無直接臨床證據 |
| 肺胚瘤 | L5 | Hold | 極罕見腫瘤（< 0.5% 肺惡性腫瘤），原始間質細胞群理論上對 DNA 合成抑制敏感，但無任何臨床試驗或文獻，需先確認體外活性 |
| 脊椎異常伴內分泌/T 細胞功能障礙 | L5 | **Hold（疑假陽性）** | 此為先天性多系統發育異常（非增殖性惡性腫瘤），Cytarabine 作為細胞毒性藥物無任何治療機轉依據。⚠️ TxGNN 高分極可能源於「T 細胞功能異常→免疫調節藥物」路徑雜訊，應作為假陽性預測排除，**不應進入任何臨床評估流程** |

---

## 細胞毒性

Cytarabine 為傳統細胞毒性藥物（嘧啶拮抗劑），適用以下細胞毒性評估：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Pyrimidine Antagonist / Antimetabolite） |
| 骨髓抑制風險 | 高（劑量依賴性；嗜中性白血球減少、血小板減少、貧血均常見；高劑量方案骨髓抑制更嚴重） |
| 致吐性分級 | 低至中度（常規劑量）；高劑量方案（≥ 1 g/m²）可達中至高度 |
| 監測項目 | CBC（含分類計數）、肝功能、腎功能；高劑量方案需額外監測眼毒性（角膜炎）、小腦功能及神經毒性 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；鞘內給藥需由具專業資格的人員執行，並需特別注意防腐劑含量（需使用不含防腐劑製劑） |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 總體結論與下一步

**整體決策摘要：**

| 適應症 | 決策 | 優先等級 |
|--------|------|---------|
| 原發性肺淋巴瘤（DLBCL 亞型） | **Proceed with Guardrails** | 🟢 最優先 |
| 小細胞肺癌（復發難治 / 腦膜轉移） | Research Question | 🟡 中等 |
| 神經母細胞瘤 | Research Question | 🟡 中等 |
| 腹膜後腫瘤（髓系肉瘤確認亞型） | Research Question | 🟡 中等（需病理前置確認） |
| 上呼吸消化道腫瘤 | Hold | 🔴 低 |
| 節細胞神經母細胞瘤 / 分化良好胎兒型肺腺癌 / 肺胚瘤 | Hold | ⚫ 暫緩 |
| 脊椎異常伴 T 細胞功能障礙 | Hold（疑假陽性） | ❌ 排除 |

**跨適應症共同行動項目：**
- 向香港衛生署申請 Cytarabine 進口特許（研究及特殊用途），作為所有後續研究推進的前提
- 每個適應症均需在進入臨床評估前完成組織病理學確認
- 優先推進原發性肺 DLBCL 病例系列研究設計，作為最有臨床轉化價值的候選方向
- 建立統一的細胞毒性藥物安全監測方案（含骨髓功能、感染預防、神經毒性評估）
- 補充 Cytarabine 詳細藥物作用機轉（MOA）資料，以強化機轉關聯性分析

> ⚠️ 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過嚴格臨床驗證才能應用於患者。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

