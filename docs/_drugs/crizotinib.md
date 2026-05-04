---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib：從 ALK+/ROS1+ 非小細胞肺癌 到 肺部良性腫瘤（10 候選多適應症評估）

## 一句話總結

Crizotinib 是 ALK/ROS1/MET 受體酪胺酸激酶的 ATP 競爭性小分子抑制劑，已在多個市場核准用於攜帶 **ALK 融合基因或 ROS1 重排**的晚期非小細胞肺癌（NSCLC），目前在香港**未取得許可**。TxGNN 模型針對本藥提出 **10 項新適應症預測**，TxGNN 分數最高的候選為**牙齦纖維瘤病（99.81%）**，但缺乏機轉及臨床支持；最具臨床推進價值的候選為**肺部良性腫瘤（含 ALK+ 炎性肌纖維母細胞瘤）**，有 **20 篇文獻**（含 Phase 2/3 RCT 及 Meta 分析）支持，建議為 **Proceed with Guardrails（限分子標記確認亞群）**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ALK+/ROS1+ 晚期非小細胞肺癌（基於文獻推斷；香港無核准許可） |
| TxGNN 首位預測 | 牙齦纖維瘤病 (Gingival Fibromatosis) |
| TxGNN 首位分數 | 99.81% |
| 首位預測證據等級 | L5（無任何臨床或機轉支持） |
| 最佳候選適應症 | 肺部良性腫瘤 (Lung Benign Neoplasm)，限 ALK+ 炎性肌纖維母細胞瘤亞群 |
| 最佳候選證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 首位預測建議決策 | Hold |
| 最佳候選建議決策 | **Proceed with Guardrails** |

---

## 全候選適應症概覽

| 排名 | 適應症（中文） | 適應症（英文） | TxGNN 分數 | 證據等級 | 試驗 | 文獻 | 建議 |
|------|--------------|--------------|-----------|---------|:---:|:---:|------|
| 1 | 牙齦纖維瘤病 | Gingival Fibromatosis | 99.81% | L5 | 0 | 0 | Hold |
| 2 | 肺纖維瘤 | Fibroma of Lung | 99.75% | L5 | 0 | 0 | Hold |
| 3 | 肺錯構瘤 | Hamartoma of Lung | 99.75% | L4 | 0 | 1 | Hold |
| 4 | 肺門癌 | Lung Hilum Carcinoma | 99.73% | L4 | 0 | 2 | Research Question |
| **5** ⭐ | **肺部良性腫瘤** | **Lung Benign Neoplasm** | **99.73%** | **L3** | **0** | **20** | **Proceed with Guardrails** |
| 6 | 肺溝腫瘤 | Pulmonary Sulcus Neoplasm | 99.73% | L5 | 0 | 0 | Hold |
| 7 | 肺部生殖細胞腫瘤 | Lung Germ Cell Tumor | 99.73% | L3 | 4 | 20 | Research Question |
| 8 | IBMPFD（含體肌病／骨 Paget 病／額顳葉失智症） | Inclusion Body Myopathy w/ Paget / FTD | 99.72% | L5 | 0 | 20† | Hold |
| 9 | 接合性大皰性表皮鬆解症 | Junctional Epidermolysis Bullosa | 99.70% | L5 | 0 | 0 | Hold |
| 10 | 白斑黑皮症-發育遲滯-智障-牙發育不全-少毛症候群 | Leukomelanoderma-infantilism-ID-hypodontia-hypotrichosis | 99.69% | L4 | 0 | 20† | Hold |

> ⭐ 最具臨床推進價值的候選
>
> † 文獻為誤配（false-positive matching）：Rank #8 的 20 篇文獻均為額顳葉失智症一般性綜述，與 Crizotinib 靶向 VCP 路徑無任何生物學交叉點；Rank #10 的文獻為 Crizotinib 藥理學、MET/HGF 或不相關疾病資料，均不計入有效支持。

---

## 為什麼這個預測合理？

> 本節聚焦最佳候選：**肺部良性腫瘤（Lung Benign Neoplasm，含 ALK+ 炎性肌纖維母細胞瘤，Rank #5）**

目前缺乏 Crizotinib 詳細作用機轉的完整文件。根據已知文獻資訊，Crizotinib 是 **ALK（間變性淋巴瘤激酶）、ROS1（c-ros 原癌基因 1）及 MET（肝細胞生長因子受體）** 的 ATP 競爭性小分子抑制劑，其核心機轉為阻斷 ALK 融合基因或 ROS1/MET 異常活化所驅動的腫瘤增殖訊號。多項 Phase 2/3 RCT（PMID 29596029、30902613）已確立其為 ALK+/ROS1+ NSCLC 的一線治療標準，Phase 3 ALEX 試驗最終分析（PMID 41110693）進一步確認了長期整體存活率效益。

「肺部良性腫瘤」在 MeSH 疾病分類中涵蓋多種組織學亞型，其中最具臨床關聯性的為**炎性肌纖維母細胞瘤（Inflammatory Myofibroblastic Tumor, IMT）**。IMT 雖傳統歸類為良性至中間型間葉腫瘤，但約 **50–60% 攜帶 ALK 融合基因**（如 TPM3-ALK、TPM4-ALK、CLTC-ALK），其致病機制與 NSCLC 中的 EML4-ALK 融合相同——均造成 ALK 激酶持續異常活化。這一共同的分子病理基礎使 Crizotinib 的靶向機轉在 ALK+ IMT 中具備直接且充分的理論適用性，PMID 34011083 亦已記錄 Crizotinib 對 ALK+ IMT 的臨床活性。

需特別指出的是，若「肺部良性腫瘤」被嚴格解讀為**真正的良性病變**（錯構瘤、軟骨瘤、脂肪瘤），則與 Crizotinib 靶點毫無生物學關聯，TxGNN 的高分預測可能源於知識圖譜中「肺部腫瘤」大類的廣泛連結。因此，**任何臨床應用必須嚴格限定於分子病理學確認 ALK 融合陽性（或 ROS1+/MET 擴增確認）的 IMT 病例**，不可類推至整個「肺部良性腫瘤」分類。

---

## 臨床試驗證據

> 肺部良性腫瘤（Rank #5）目前無直接登記的臨床試驗。以下為 ALK+ 非 NSCLC 腫瘤的機轉相關試驗（來源：Rank #7 肺部生殖細胞腫瘤，相關性等級 B–C）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|:----:|---------|
| [NCT02568267](https://clinicaltrials.gov/study/NCT02568267) | Phase 2 | 進行中（不再招募） | 534 | Entrectinib（ALK/ROS1/NTRK 抑制劑，機轉類似 Crizotinib）籃型試驗，針對 ALK/ROS1/NTRK 融合陽性實體腫瘤，驗證分子標記驅動的跨瘤種治療策略 |
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | 進行中（不再招募） | 6,452 | NCI-MATCH 超大型籃型試驗，依基因組標記（含 ALK/MET 異常）配對靶向藥物，廣泛支持跨瘤種分子驅動治療框架 |
| [NCT01121588](https://clinicaltrials.gov/study/NCT01121588) | Phase 1b | 已終止 | 44 | Crizotinib 直接用於 ALK 融合陽性非 NSCLC 腫瘤的概念驗證試驗，提供 NSCLC 以外 ALK+ 腫瘤的早期安全性與活性資料 |
| [NCT02223819](https://clinicaltrials.gov/study/NCT02223819) | Phase 2 | 已完成 | 34 | Crizotinib 輔助治療高風險葡萄膜黑色素瘤（c-Met 驅動），確認 Crizotinib 在非 NSCLC 惡性腫瘤中的安全性與可行性 |

---

## 文獻證據

> 以下 10 篇選自 Rank #5（肺部良性腫瘤）的 20 篇文獻，優先呈現最高研究等級：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [29596029](https://pubmed.ncbi.nlm.nih.gov/29596029/) | 2018 | Phase 2 RCT | J Clin Oncol | 最大型 ROS1+ 晚期 NSCLC 東亞患者佇列，確立 Crizotinib 顯著抗腫瘤活性（ORR 71.7%）與安全性 |
| [30902613](https://pubmed.ncbi.nlm.nih.gov/30902613/) | 2019 | Phase 3 RCT | J Thorac Oncol | ALEX 試驗更新：ALK+ NSCLC 中 Alectinib 優於 Crizotinib（PFS HR=0.47），同時確立 ALK 靶向治療整體框架 |
| [41110693](https://pubmed.ncbi.nlm.nih.gov/41110693/) | 2026 | Meta-analysis | Ann Oncol | ALEX 試驗最終 OS 分析，提供 ALK+ NSCLC 成熟的長期整體存活率資料 |
| [37530142](https://pubmed.ncbi.nlm.nih.gov/37530142/) | 2023 | Systematic Review/Meta-analysis | Pak J Pharm Sci | 3 項 RCT 彙整（HR=0.33）：Alectinib vs Crizotinib 於 ALK+ NSCLC 療效與毒性的系統性比較 |
| [38749072](https://pubmed.ncbi.nlm.nih.gov/38749072/) | 2024 | Systematic Review/Meta-analysis | Lung Cancer | ROS1 融合晚期 NSCLC 中 Crizotinib 真實世界療效（ORR、PFS、OS）Meta 分析 |
| [25239305](https://pubmed.ncbi.nlm.nih.gov/25239305/) | 2014 | Meta-analysis | BMC Cancer | ALK+ NSCLC 中 Crizotinib 療效與安全性的早期臨床試驗彙整，FDA 加速核准的奠基研究 |
| [35232230](https://pubmed.ncbi.nlm.nih.gov/35232230/) | 2022 | 真實世界比較研究 | Future Oncol | ROS1+ NSCLC 中 Crizotinib vs Entrectinib 臨床試驗與真實世界結果的模擬治療比較 |
| [32949827](https://pubmed.ncbi.nlm.nih.gov/32949827/) | 2020 | 回顧性佇列 | Lung Cancer | MET 擴增肺癌對 Crizotinib 的臨床反應特徵，支持 MET 驅動亞群的靶向治療可行性 |
| [31313100](https://pubmed.ncbi.nlm.nih.gov/31313100/) | 2019 | 綜述 | Drugs | ROS1 重排 NSCLC 靶向治療全面綜述，確立 Crizotinib 為一線標準並分析後續世代藥物 |
| [41617059](https://pubmed.ncbi.nlm.nih.gov/41617059/) | 2026 | 綜述 | Toxicol Lett | Crizotinib 多系統毒性（肝毒性、心毒性、間質性肺炎）的機制與臨床管理策略 |

---

## 香港上市資訊

Crizotinib 在香港目前**未取得任何藥品許可**（許可證數：0），無上市資訊可列出。如需臨床使用，須透過特殊渠道（如緊急用藥申請、同情用藥或臨床試驗框架）取得。

---

## 細胞毒性

Crizotinib 的原核准適應症為惡性腫瘤（NSCLC），屬**抗腫瘤標靶治療藥物**（DrugBank 類別含 Antineoplastic Agent）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物—受體酪胺酸激酶抑制劑（非傳統細胞毒性化療；口服小分子 ALK/ROS1/MET 抑制劑） |
| 骨髓抑制風險 | 低至中（非傳統骨髓毒性；可能有中性球減少及淋巴球減少，需監測全血計數） |
| 致吐性分級 | 低至中度 |
| 監測項目 | 肝功能（ALT/AST/Bilirubin，建議每月監測；嚴重肝毒性含致死性肝衰竭案例）、心電圖（QT 間期延長、心跳過緩）、胸部影像（間質性肺炎）、視力評估（視覺障礙為常見不良反應）、腎功能 |
| 處置防護 | 口服劑型，依口服抗腫瘤藥物標準規範操作；具嚴重肝毒性（含致死性肝衰竭，PMID 26898609）及多重同時心臟毒性（PMID 29717400）的高風險警示，需建立結構性安全監測計畫 |

---

## 安全性考量

安全性資訊請參考原廠仿單（香港未上市，建議參閱 FDA／EMA 核准版本）。

根據已有文獻記錄的主要安全顧慮：

- **嚴重肝毒性**：包含致死性肝衰竭案例（PMID 26898609），使用期間需定期監測肝功能；出現顯著肝酶異常（>3×ULN）時應考慮停藥
- **心臟毒性**：QT 延長、心跳過緩、心室性心律不整及心包膜炎可**同時**發生（PMID 29717400），建議用藥前後進行心電圖監測，避免與其他 QT 延長藥物併用
- **間質性肺炎 / 藥物性肺損傷**：ROS1+ NSCLC 患者使用後出現藥物性組織性肺炎（PMID 37062732），需與原發性肺部疾病進展鑑別診斷

---

## 結論與下一步

**決策：Hold（TxGNN Rank #1 牙齦纖維瘤病）；Proceed with Guardrails（Rank #5 肺部良性腫瘤—ALK+ IMT 亞群）**

**理由：**
- TxGNN Rank #1（牙齦纖維瘤病，99.81%）儘管 TxGNN 分數最高，但與 Crizotinib 的 ALK/ROS1/MET 靶點缺乏任何已知生物學關聯，無臨床試驗或文獻支持，判定為知識圖譜遠端連結產生的假陽性預測，不建議投入資源。
- Rank #5（肺部良性腫瘤，ALK+ IMT 亞群）具直接且充分的機轉相關性（ALK 融合共享相同致病機制），有多項 Phase 2/3 RCT 及 Meta 分析確立 ALK+/ROS1+ 腫瘤靶向治療的療效基礎，具備在嚴格分子標記限定條件下推進的條件。

**若要推進（針對 ALK+ 炎性肌纖維母細胞瘤亞群）需要：**

1. **疾病精確定義**：適應症限定為**組織學及分子病理學確認的 ALK 融合陽性炎性肌纖維母細胞瘤（IMT）**，明確排除真正的良性肺部腫瘤（錯構瘤、脂肪瘤等）
2. **監管狀態補充**：確認 Crizotinib 在香港的監管路徑（同情用藥、特殊患者計畫或臨床試驗申請可行性）
3. **MOA 資料補充**：取得 Crizotinib 完整作用機轉文件及 IMT 特異性 ALK 融合亞型的藥效動力學資料
4. **安全性監測計畫**：制定涵蓋肝功能、心電圖、肺功能及視力的結構性分期監測方案
5. **試驗設計建議**：優先考慮**籃型試驗（Basket Trial）**設計，將 ALK+ IMT 作為以分子標記定義的獨立亞群納入，可參考 NCT02568267 及 NCT02465060 的框架

---

> ⚠️ **研究聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選須經嚴格臨床驗證後方可應用於實際患者。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

