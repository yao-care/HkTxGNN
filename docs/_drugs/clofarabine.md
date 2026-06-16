---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine：從急性淋巴母細胞白血病到骨髓性白血病（多適應症評估）

## 一句話總結

Clofarabine 是第二代嘌呤核苷類似物，已獲美國 FDA 核准用於兒科復發/難治性急性淋巴母細胞白血病（ALL），目前在香港**尚未上市**。TxGNN 模型在此背景下，預測其最主要再利用目標為**骨髓性白血病 (Myeloid Leukemia)**（預測分數 99.88%），同時對**前驅淋巴母細胞腫瘤**及**急性淋巴母細胞白血病**具備 L1 最高等級臨床證據。本多適應症報告共識別 10 項預測，其中 4 項達到 Proceed with Guardrails 決策門檻，6 項建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 已知適應症（FDA） | 兒科復發/難治性急性淋巴母細胞白血病（≥1 歲、≥2 線治療失敗後） |
| 首位預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數（首位） | 99.88% |
| 最高證據等級 | L1（急性淋巴母細胞白血病、前驅淋巴母細胞腫瘤） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 首位適應症建議決策 | Proceed with Guardrails |

### 多適應症預測總覽

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗數 | 文獻數 | 證據等級 | 建議決策 |
|------|--------|-----------|-----------|-------|---------|---------|
| 1 | 骨髓性白血病 (Myeloid Leukemia) | 99.88% | 50 | 20 | L2 | Proceed with Guardrails |
| 2 | 前驅淋巴母細胞淋巴瘤/白血病 | 99.57% | 50 | 20 | L1 | Proceed with Guardrails |
| 3 | 神經節母細胞瘤 (Ganglioneuroblastoma) | 99.53% | 0 | 0 | L5 | Hold |
| 4 | 神經母細胞瘤 (Neuroblastoma) | 99.52% | 1 | 2 | L4 | Research Question |
| 5 | 脊椎異常合併 T 細胞功能障礙症候群 | 99.46% | 0 | 0 | L5 | Hold |
| 6 | 腹膜後腫瘤 (Retroperitoneal Neoplasm) | 99.44% | 0 | 0 | L5 | Hold |
| 7 | 急變期慢性骨髓性白血病（BCR-ABL1+） | 99.43% | 8 | 4 | L2 | Proceed with Guardrails |
| 8 | 急性淋巴母細胞白血病 (ALL) | 99.31% | 50 | 18 | L1 | Proceed with Guardrails |
| 9 | 前生發中心型 CLL/SLL | 99.26% | 0 | 0 | L5 | Hold |
| 10 | IGHV 突變型 CLL/SLL | 99.26% | 0 | 0 | L5 | Hold |

---

## 為什麼這些預測合理？

### 藥物作用機轉

Clofarabine 是專為克服第一代嘌呤核苷類似物（Fludarabine、Cladribine）缺陷而設計的第二代藥物。其嘌呤環和核糖環均經鹵化修飾，對去氨基酶（ADA）和嘌呤核苷磷酸化酶（PNP）具備高度穩定性。三重抗腫瘤機轉如下：

1. **抑制核糖核苷酸還原酶（RNR）**：耗竭細胞內 dNTP 池，對靜止期與分裂期的骨髓性母細胞和淋巴母細胞均有效，優於傳統阿糖胞苷（僅針對分裂期）
2. **抑制 DNA 聚合酶 α/ε**：以 5'-三磷酸代謝物形式嵌入 DNA，阻斷複製叉前進與 DNA 修復
3. **誘導粒線體凋亡途徑**：促使細胞色素 C 釋放，啟動不依賴 p53 狀態的內源性凋亡，可克服多數常見化療抗性機制

此外，Clofarabine 不依賴 MDR1 外排泵，對多重耐藥腫瘤細胞仍保有療效。

### 骨髓性白血病（Rank 1）的預測合理性

急性骨髓性白血病（AML）及骨髓異生不良症候群（MDS）中的白血病母細胞增殖高度依賴快速 DNA 合成，對 dNTP 池耗竭特別敏感。Clofarabine 的 RNR 雙重抑制機轉恰好針對此弱點。多項 Phase 2 完成試驗（NCT01101880 [n=50]、NCT00778375 [n=122]）及兩項大型 Phase 3 隨機試驗（NCT02085408 [n=727]、NCT00317642 [n=326]）已在成人 AML 中系統驗證其療效。Clofarabine 於不耐蒽環類化療的老年 AML 患者（≥60 歲）及移植預處理方案（Clo/Bu4）中尤具臨床價值。

### 淋巴母細胞腫瘤（Ranks 2 & 8）的預測合理性

Clofarabine 在淋巴母細胞中的藥理活性尤為突出，機轉連結最為直接：ALL 細胞中 Deoxycytidine Kinase（DCK）高度表達，促進 Clofarabine 磷酸化活化，5'-三磷酸活性代謝物在 T-ALL 和 B-ALL 細胞中積累濃度為其他細胞類型的 10 倍以上，是生物學合理性最強的適應症之一。COALL 08-09 研究（NCT01228331，Phase 2/3，n=745）及患者個體層級薈萃分析（PMID 37819554，2023）共同確立了 L1 最高等級臨床證據。值得注意的是，Rank 2（前驅淋巴母細胞腫瘤）與 Rank 8（急性淋巴母細胞白血病）高度重疊，均涵蓋在 FDA 已核准的適應症範疇內，在香港屬藥物再利用情境。

### 急變期 CML BCR-ABL1+（Rank 7）的預測合理性

BCR-ABL1 陽性急變期 CML 在轉化後增殖極度活躍，且 TKI 單藥療效不佳。Clofarabine 透過 RNR 抑制與 DNA 聚合酶阻斷對 BCR-ABL1 下游增殖路徑產生平行殺傷效應，不依賴 BCR-ABL1 激酶活性，因此對 TKI 抗性患者理論上仍有效。PMID 20938169 直接報告 Clofarabine 方案作為 Imatinib/Dasatinib 抗性骨髓危象橋接異體移植的有效策略；NCT00098033（Phase 2，n=64）亦明確納入 CML 急變期患者進行評估。

---

## 臨床試驗證據

### 適應症一：骨髓性白血病

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02085408](https://clinicaltrials.gov/study/NCT02085408) | Phase 3 | 完成 | 727 | 隨機試驗：Clofarabine 誘導 vs 標準 Daunorubicin/Cytarabine，後接 Decitabine 維持或觀察，用於 ≥60 歲新診斷 AML |
| [NCT00317642](https://clinicaltrials.gov/study/NCT00317642) | Phase 3 | 完成 | 326 | 雙盲隨機試驗：Clofarabine+Cytarabine vs Cytarabine 單藥，用於 ≥55 歲復發/難治性 AML，評估聯合用藥優勢 |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | 完成 | 324 | AML08：Clofarabine+Cytarabine vs 標準誘導療法用於新診斷 AML，並評估 NK 細胞移植可行性 |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | 完成 | 50 | Clofarabine+高劑量 Cytarabine+G-CSF priming 用於 <65 歲新診斷 AML/高風險 MDS，提供核心 Phase 2 療效數據 |
| [NCT00778375](https://clinicaltrials.gov/study/NCT00778375) | Phase 2 | 完成 | 122 | Clofarabine+Cytarabine 交替 Decitabine 作為 ≥60 歲 AML/高風險 MDS 誘導及鞏固方案 |
| [NCT01534702](https://clinicaltrials.gov/study/NCT01534702) | Phase 1/2 | 不明 | 60 | Cytarabine+Idarubicin+遞增劑量 Clofarabine 作為高風險 AML 誘導治療（AMLSG 17-10），提供劑量最佳化資料 |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Phase 2 | 完成 | 95 | 隨機比較 Clofarabine 單藥 vs Clofarabine+Cytarabine，用於 ≥60 歲未治療 AML/高風險 MDS |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | 完成 | 86 | Clofarabine 搶救療法用於復發/難治性 AML，評估橋接異體造血幹細胞移植的可行性與比率 |
| [NCT00065143](https://clinicaltrials.gov/study/NCT00065143) | Phase 2 | 完成 | 60 | Clofarabine+Cytarabine 用於 ≥50 歲新診斷 AML 及高風險 MDS（骨髓母細胞≥10%），早期大型 Phase 2 |
| [NCT01188174](https://clinicaltrials.gov/study/NCT01188174) | Phase 2 | 完成 | 26 | Clofarabine/Ara-C 聯合低強度移植預處理，作為初次治療失敗 AML 的序貫策略 |

### 適應症二：前驅淋巴母細胞腫瘤及急性淋巴母細胞白血病

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01228331](https://clinicaltrials.gov/study/NCT01228331) | Phase 2/3 | 完成 | 745 | COALL 08-09：多中心隨機試驗比較 Clofarabine vs 高劑量 Cytarabine 用於兒童 ALL，為本適應症最高等級（L1）核心試驗 |
| [NCT00990249](https://clinicaltrials.gov/study/NCT00990249) | Phase 2 | 完成 | 120 | Busulfan+Clofarabine 移植預處理大型完成試驗，ALL 患者為主要入組族群，提供移植前橋接強力佐證 |
| [NCT00042341](https://clinicaltrials.gov/study/NCT00042341) | Phase 2 | 完成 | 60 | Clofarabine 單藥 52 mg/m² 用於兒科復發/難治性 ALL，為 FDA 2004 年核准的關鍵基礎研究 |
| [NCT01462253](https://clinicaltrials.gov/study/NCT01462253) | Phase 2 | 完成 | 35 | 多中心序貫 Clofarabine-Cyclophosphamide 方案，用於成人復發/難治性 ALL 搶救治療，前瞻性設計 |
| [NCT01700946](https://clinicaltrials.gov/study/NCT01700946) | Phase 2 | 完成 | 80 | 兒科復發/難治性前驅 B 細胞 ALL 及淋巴瘤之風險適應性治療，標準風險 vs 高風險分層策略 |
| [NCT00337168](https://clinicaltrials.gov/study/NCT00337168) | Phase 2 | 完成 | 36 | Cytarabine+Clofarabine 聯合方案用於成人復發/難治性 ALL，評估療效與毒性 |
| [NCT01385891](https://clinicaltrials.gov/study/NCT01385891) | Phase 2/3 | 完成 | 40 | CEA 方案（Clofarabine+Etoposide+Cyclophosphamide）用於兒科復發/難治性 ALL 及 AML，緩解誘導評估 |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | 完成 | 50 | Clofarabine+Etoposide+Cyclophosphamide 劑量遞增研究，建立 CEA 方案 MTD 及兒科安全性基礎 |
| [NCT03136146](https://clinicaltrials.gov/study/NCT03136146) | Phase 2 | 招募中 | 42 | CEC+脂質體 Vincristine+Dexamethasone+Bortezomib 用於復發/難治性 ALL 及淋巴母細胞淋巴瘤 |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | 完成 | 30 | 多中心非隨機：Clofarabine+Busulfan+Thymoglobulin 移植預處理，直接納入 ALL 患者並提供療效資料 |

### 適應症三：急變期慢性骨髓性白血病（BCR-ABL1+）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00098033](https://clinicaltrials.gov/study/NCT00098033) | Phase 2 | 完成 | 64 | Clofarabine 在急性白血病藥效學研究，**明確納入 CML 加速期及急變期患者**，提供最直接療效與安全性資料 |
| [NCT00334074](https://clinicaltrials.gov/study/NCT00334074) | Phase 2 | 完成 | 30 | Clofarabine+Cytarabine 用於復發 AML 及高風險 MDS，骨髓性惡性腫瘤療效資料可參考 |
| [NCT00293410](https://clinicaltrials.gov/study/NCT00293410) | Phase 1 | 完成 | 70 | Clofarabine+Cyclophosphamide 劑量遞增，**明確納入 CML 及骨髓增生性腫瘤**，建立 MTD 及安全性基礎 |
| [NCT00423514](https://clinicaltrials.gov/study/NCT00423514) | Phase 1/2 | 完成 | 38 | Clofarabine+Melphalan+Thiotepa 骨髓清除預處理，涵蓋 CML 急變期移植前橋接情境 |

---

## 文獻證據

### 適應症一：骨髓性白血病

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | 系統性回顧 | Lancet Oncology | Clofarabine+Cytarabine 用於 AML 的 Cochrane 等級回顧，確立聯合方案證據基礎 |
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT | J Clinical Oncology | AML08 Phase 3：Clofarabine 可取代蒽環類及 Etoposide 於兒童 AML 誘導治療，療效相當但降低心毒性 |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 研究 | Cancer Medicine | CLAM 方案（Clofarabine+Cytarabine+Mitoxantrone）用於復發/難治性 AML，緩解率高並有效橋接移植 |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | 回溯性研究 | Transplantation & Cellular Therapy | Clo/Bu4 骨髓清除預處理用於活動性骨髓性惡性腫瘤移植，≤70 歲患者抗白血病活性可接受 |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase IB | Haematologica | Clofarabine 取代 Fludarabine 用於兒科復發/難治性 AML 聯合化療，確立推薦 Phase 2 劑量 |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | 次級分析 | Cancers | CLARA 鞏固方案改善年輕 AML 微複雜核型（micro-complex karyotype）患者的無復發存活率 |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | 綜述 | Leukemia & Lymphoma | Clofarabine 於 AML 完整回顧：機轉特性、關鍵試驗結果及各線治療聯合策略 |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | 綜述 | Critical Reviews in Oncology | 成人 AML 中 Clofarabine 的角色：從單藥到第一/二線聯合方案的系統性文獻分析 |
| [18756533](https://pubmed.ncbi.nlm.nih.gov/18756533/) | 2008 | 回溯性研究 | Cancer | Clofarabine 聯合方案（+Cytarabine/Idarubicin）作為復發 AML 搶救策略，療效與毒性評估 |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | 綜述 | Future Oncology | Clofarabine 在成人 AML 的治療前景：單藥活性優異，未來成為誘導/鞏固骨架藥物 |

### 適應症二：前驅淋巴母細胞腫瘤及急性淋巴母細胞白血病

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37819554](https://pubmed.ncbi.nlm.nih.gov/37819554/) | 2023 | 個體資料薈萃分析 | Advances in Therapy | 患者個體層級 meta-analysis：確認 Clofarabine 52 mg/m² 於兒科 R/R ALL 的臨床受益，確立 L1 核心證據 |
| [38680089](https://pubmed.ncbi.nlm.nih.gov/38680089/) | 2024 | 系統性回顧 | Cancer Medicine | HOVON-100 試驗多狀態模型分析：Clofarabine 於成人 ALL 提高 MRD 陰性率，EFS 未顯著改善，效益/風險仍待精準化 |
| [34348455](https://pubmed.ncbi.nlm.nih.gov/34348455/) | 2022 | RCT 結果報告 | Haematologica | CoALL 08-09 RCT：Clofarabine 優於 HDAC 清除 B-ALL 微殘留病，但未轉化為整體存活改善 |
| [38643356](https://pubmed.ncbi.nlm.nih.gov/38643356/) | 2024 | 前瞻性觀察 | Jpn J Clinical Oncology | 日本上市後真實世界研究：日本兒科 R/R ALL 的安全性與療效確認，支持亞洲族群應用 |
| [26666536](https://pubmed.ncbi.nlm.nih.gov/26666536/) | 2016 | 回溯性研究 | Annals of Hematology | **香港中文兒科患者** CLO-218 方案（Clofarabine+Cyclophosphamide+Etoposide）橋接 HSCT，具直接本地參考價值 |
| [22431002](https://pubmed.ncbi.nlm.nih.gov/22431002/) | 2012 | 回溯性世代 | American J Hematology | 西班牙 PETHEMA 組 31 例成人 R/R ALL 及淋巴母細胞淋巴瘤：Clofarabine 方案 CR 率 31%，可見多種細胞遺傳學亞型反應 |
| [15962525](https://pubmed.ncbi.nlm.nih.gov/15962525/) | 2005 | 藥物評論 | Nature Reviews Drug Discovery | Clofarabine FDA 核准背景：首個先獲兒科批准的抗白血病新藥，Phase 2 關鍵數據回顧 |
| [16117562](https://pubmed.ncbi.nlm.nih.gov/16117562/) | 2005 | 藥物評論 | Paediatric Drugs | 61 例兒科 ALL 患者 Clofarabine 52 mg/m² 治療數據：完全緩解率、安全性及管理摘要 |
| [33421973](https://pubmed.ncbi.nlm.nih.gov/33421973/) | 2021 | 前瞻性觀察 | Cancer Research and Treatment | 韓國兒科 R/R ALL 真實世界研究：Clofarabine 單藥及聯合方案療效與安全性，東亞族群補充證據 |
| [17288522](https://pubmed.ncbi.nlm.nih.gov/17288522/) | 2007 | 綜述 | Expert Rev Anticancer Therapy | Clofarabine 治療 ALL 的完整評估：兒科 Phase 2 到成人擴展的系統性分析及未來展望 |

### 適應症三：急變期慢性骨髓性白血病

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20938169](https://pubmed.ncbi.nlm.nih.gov/20938169/) | 2010 | 回溯性研究 | Acta Haematologica | **直接相關**：Clofarabine 方案作為 Imatinib/Dasatinib 抗性 Ph+ CML 骨髓危象橋接異體移植的有效策略，報告緩解率與存活資料 |
| [18537755](https://pubmed.ncbi.nlm.nih.gov/18537755/) | 2008 | 綜述 | Recent Patents on Anti-Cancer Drug Discovery | 嘌呤核苷類似物（Clofarabine/Nelarabine/Forodesine）於血液惡性腫瘤的機轉、代謝及臨床活性比較 |
| [12563614](https://pubmed.ncbi.nlm.nih.gov/12563614/) | 2003 | 綜述 | Seminars in Hematology | 進展期 CML（加速期/急變期）臨床管理策略及新藥整合，提供 CML 急變期治療背景 |
| [15230627](https://pubmed.ncbi.nlm.nih.gov/15230627/) | 2004 | 藥物評論 | Drugs in R&D | Clofarabine 早期臨床開發：雙重抑制（DNA 聚合酶 + RNR）機轉說明，為急變期 CML 合理性提供藥理基礎 |

---

## 香港上市資訊

Clofarabine 目前在香港**尚未上市**，香港衛生署無任何藥物許可證記錄（共 0 張）。

如需臨床使用，需透過衛生署特殊用藥申請途徑（Unregistered Drug）獲得批准。可參考以下已核准市場的資料來源：

- **美國 FDA**：Clolar®（靜脈注射劑，20 mg/20 mL），核准用於兒科 R/R ALL（1-21 歲）
- **歐盟 EMA**：Evoltra®，核准適應症相同
- **日本 PMDA**：コロファール®，2014 年核准，上市後真實世界資料可參考（PMID 38643356）

---

## 細胞毒性

Clofarabine 為明確的細胞毒性抗腫瘤藥物（Purine Nucleoside Analog，屬 Antineoplastic 類別）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（第二代嘌呤核苷類似物） |
| 骨髓抑制風險 | 高（幾乎全部患者出現 Grade 3-4 嗜中性白血球減少及血小板減少；感染風險顯著） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）每 1-2 週、肝腎功能（含 bilirubin）、電解質、尿酸（腫瘤溶解症候群監測）、體液平衡及感染徵象 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈注射配製需具備化療藥房設施（Biological Safety Cabinet） |

特別注意：Clofarabine 已有**全身發炎反應症候群（SIRS）、毛細血管滲漏症候群（Capillary Leak Syndrome）及心包膜積液/心肌炎**的報告，建議治療期間密切監測生命徵象、體重及心肺功能。腫瘤溶解症候群（TLS）於血液腫瘤患者需預防性處理（水化、Allopurinol/Rasburicase）。

> 如需完整毒性資料，請參考 Clolar®（美國）或 Evoltra®（歐盟）原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單（Clolar®/Evoltra®/コロファール®）。

本評估的 TFDA 仿單警語及禁忌症資料均有缺口，藥物交互作用查詢亦無結果（DDI 資料未取得）。建議於推進臨床評估前，優先補充以下資料：
- 美國 FDA 核准說明書完整警語（含黑框警告）
- EMA EPAR 文件中的安全性評估報告
- 日本 PMDA 審查報告書（含亞洲族群安全性數據）

---

## 結論與下一步

### 骨髓性白血病（Rank 1）

**決策：Proceed with Guardrails**

**理由：**
已有兩項大型 Phase 3 隨機試驗（NCT02085408 [n=727]、NCT00317642 [n=326]）及多項 Phase 2 完成研究提供充分療效依據；Clofarabine 在老年 AML 及 Clo/Bu4 移植預處理方案中已建立明確臨床定位。

**若要推進需要：**
- 取得原廠仿單完整安全性警語及禁忌症
- 評估香港衛生署特殊藥物申請路徑及可行性
- 明確目標族群（老年新診斷 AML vs 復發/難治性 AML vs 移植預處理）
- 建立本地骨髓抑制、感染及 SIRS 毒性管理計畫

---

### 前驅淋巴母細胞腫瘤 / 急性淋巴母細胞白血病（Ranks 2 & 8）

**決策：Proceed with Guardrails**

**理由：**
Clofarabine 已獲 FDA 核准用於兒科 R/R ALL，COALL 08-09（Phase 2/3，n=745）及患者個體薈萃分析（2023）確立 L1 最高等級證據；香港兒科本地真實世界資料（PMID 26666536，香港中文大學）提供直接參考。

**若要推進需要：**
- 申請香港衛生署特殊/緊急用藥審批
- 確認目標族群（兒科 vs 成人、復發 vs 初治）及介入線別
- 建立本地毒性監測計畫，重點：骨髓抑制、感染、TLS、SIRS 及心肺功能監測
- 參考日本（PMID 38643356）和韓國（PMID 33421973）亞洲族群安全性資料

---

### 急變期 CML BCR-ABL1+（Rank 7）

**決策：Proceed with Guardrails**

**理由：**
Phase 2 試驗（NCT00098033，n=64）直接納入 CML 急變期患者；PMID 20938169 病例系列支持 Clofarabine 作為 TKI 抗性骨髓危象橋接移植的可行方案，具機轉合理性。

**若要推進需要：**
- 蒐集更多 CML 急變期（特別是 TKI 抗性患者）的 Clofarabine 療效及安全性資料
- 評估 Clofarabine + 第二/三代 TKI 聯合方案的設計可行性
- 考量 BCR-ABL1 突變類型（T315I 等）對療效預測的影響

---

### 其他適應症（建議暫緩 Hold）

- **神經節母細胞瘤（Rank 3）**、**腹膜後腫瘤（Rank 6）**、**脊椎異常 T 細胞功能障礙症候群（Rank 5）**、**CLL/SLL 亞型（Ranks 9-10）**：完全缺乏直接臨床前或臨床證據，TxGNN 預測可能反映知識圖譜拓樸假陽性，建議暫緩。
- **神經母細胞瘤（Rank 4，L4）**：理論上高風險/MYCN 擴增型神經母細胞瘤的快速增殖特性使其對 RNR 抑制敏感，但目前僅有間接移植研究（NCT00617929）及一篇基礎蛋白質體學研究，需先取得體外/體內臨床前驗證資料方可進入臨床開發評估。

> **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選需經嚴格臨床驗證方可應用於患者。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

