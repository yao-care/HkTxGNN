---
layout: default
title: Methotrexate
parent: 高證據等級 (L1-L2)
nav_order: 487
evidence_level: L2
indication_count: 5
---

# Methotrexate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Methotrexate：老藥新用評估——鎖定何杰金氏淋巴瘤

## 一句話總結

Methotrexate（MTX）為抗葉酸類（DHFR 抑制劑）廣效藥物，本次查詢未取得其原始適應症與香港上市資料。
TxGNN 模型針對 MTX 產生 **5 個預測新適應症**，其中證據最紮實的是**何杰金氏淋巴瘤 (Hodgkin's Lymphoma)**，
目前有 **50 個臨床試驗**登記與 **20 篇文獻**佐證，證據等級達 **L2**，是本批候選中唯一具備「Proceed with Guardrails」建議的項目。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（本次查詢未取得；香港未上市，無本地許可證可比對） |
| 預測新適應症 | 何杰金氏淋巴瘤 (Hodgkin's Lymphoma) |
| TxGNN 預測分數 | 99.32%（排名 11,294） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA: Data Gap）。根據證據包內的佐證資訊，Methotrexate 是抗葉酸類（DHFR 抑制劑）廣效藥物，其成分在淋巴瘤化療與異體移植後 GVHD 預防中的療效已被廣泛驗證（例如 Tac/MTX 用於 GVHD 預防的多個 Phase 3 試驗），機轉上可能適用於何杰金氏淋巴瘤。

MTX 為歷史上 **VBM（vinblastine, bleomycin, methotrexate）方案**的核心藥物之一，曾用於早期何杰金氏淋巴瘤治療；文獻中亦有 Phase 3 劑量強化試驗直接針對 Hodgkin 相關族群。抗葉酸機轉能抑制快速增殖的淋巴母細胞，與何杰金氏淋巴瘤的病理生理高度吻合。

需注意：現行第一線標準治療已為 ABVD 方案，MTX 的定位應限於復發/難治病例、特定禁忌症患者，或作為移植情境下的支持性用藥，而非取代現行標準。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00005977](https://clinicaltrials.gov/study/NCT00005977) | Phase 3 | 完成 | 83 | MTX 劑量強化方案用於晚期（III/IV）淋巴瘤族群 |
| [NCT00003632](https://clinicaltrials.gov/study/NCT00003632) | Phase 2 | 完成 | 30 | 高劑量 MTX + Ara-C 續接 BEAM 自體移植，用於新診斷淋巴瘤 |
| [NCT02631239](https://clinicaltrials.gov/study/NCT02631239) | Phase 3 | 未知 | 256 | MTX 為方案組成之一，用於第 I-II 期結外 NK/T 細胞淋巴瘤 |
| [NCT00734773](https://clinicaltrials.gov/study/NCT00734773) | Early Phase 1 | 撤回 | 0 | 高劑量 MTX 為基礎方案加入 motexafin gadolinium，用於原發性 CNS 淋巴瘤（因故撤回） |
| [NCT00003056](https://clinicaltrials.gov/study/NCT00003056) | Phase 3 | 終止 | 105 | Cyclosporine/MTX vs T 細胞剔除，用於異體移植 GVHD 預防 |
| [NCT01230983](https://clinicaltrials.gov/study/NCT01230983) | Phase 3 | 完成 | 573 | 高劑量 MTX 併用/不併用於 T 細胞 ALL 及晚期淋巴母細胞非何杰金氏淋巴瘤 |
| [NCT00000658](https://clinicaltrials.gov/study/NCT00000658) | Phase 3 | 完成 | 250 | 低劑量 vs 標準劑量 mBACOD（含 MTX）用於 AIDS 相關非何杰金氏淋巴瘤 |
| [NCT00003650](https://clinicaltrials.gov/study/NCT00003650) | Phase 3 | 完成 | 179 | 併用化療（含 MTX）用於兒童 T 細胞及前 B 細胞非何杰金氏淋巴瘤 |
| [NCT03602898](https://clinicaltrials.gov/study/NCT03602898) | Phase 2 | 撤回 | 0 | ATG / PTCy vs CNI-MTX 三方比較，用於移植後 GVHD 預防 |
| [NCT05421299](https://clinicaltrials.gov/study/NCT05421299) | N/A | 完成 | 378 | Abatacept 併用 CNI + MTX 於 HSCT 患者存活率之 CIBMTR 資料庫分析 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Review/Cohort | Crit Rev Oncol Hematol | VBM（含 MTX）併放療於早期何杰金氏淋巴瘤，完全緩解率 94-100%，5 年無惡化存活 75-95% |
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | Cohort | Cancer | GISL 經驗：VBM 化療併放療用於早期預後良好何杰金氏淋巴瘤 |
| [7509382](https://pubmed.ncbi.nlm.nih.gov/7509382/) | 1994 | Pilot study | J Clin Oncol | BNLI 試驗：VBM 併局部放療用於 IA/IIA 期何杰金氏病之療效與毒性 |
| [28380678](https://pubmed.ncbi.nlm.nih.gov/28380678/) | 2017 | Cohort | Cancer Science | MTX 相關淋巴增殖疾患：比較 DLBCL 型與典型何杰金氏淋巴瘤型之臨床病理特徵 |
| [8635099](https://pubmed.ncbi.nlm.nih.gov/8635099/) | 1996 | Cohort | Cancer | IVAM（含 MTX）作為復發/難治侵襲性非何杰金氏淋巴瘤之挽救性化療 |
| [2363941](https://pubmed.ncbi.nlm.nih.gov/2363941/) | 1990 | Cohort | Acta Oncol | MIME（含 MTX）用於復發/難治何杰金氏病與非何杰金氏淋巴瘤之挽救治療 |
| [35848760](https://pubmed.ncbi.nlm.nih.gov/35848760/) | 2022 | Cohort | Am J Surg Pathol | 比較 de novo 與 MTX 相關 EBV 陽性典型何杰金氏淋巴瘤之 9p24.1／PD-L1 表現 |
| [16467107](https://pubmed.ncbi.nlm.nih.gov/16467107/) | 2006 | 基礎研究 | Clin Cancer Res | 新型抗葉酸藥 pralatrexate/gemcitabine 對比 MTX/ara-C 於淋巴瘤模型之效果 |
| [16443552](https://pubmed.ncbi.nlm.nih.gov/16443552/) | 2006 | Case report | Int J Hematol | 長期低劑量 MTX 治療 RA 患者出現 EBV 陰性何杰金氏淋巴瘤，停藥後自發緩解 |
| [24246254](https://pubmed.ncbi.nlm.nih.gov/24246254/) | 2014 | Case report | J Oral Maxillofac Surg | MTX 治療患者出現模擬何杰金氏淋巴瘤之 EBV 陽性口腔潰瘍 |

---

## 香港上市資訊

Methotrexate 目前尚未在香港取得任何許可證（`total_licenses: 0`），無本地上市品項或核准適應症資料可供比對。

---

## 其他候選適應症一覽

TxGNN 本次共針對 MTX 產生 5 個預測適應症，證據強度差異極大，僅何杰金氏淋巴瘤達到可行動等級：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|-----------|-----------|---------|---------|
| 1 | 肺母細胞瘤 (Pulmonary Blastoma) | 99.45% | L5 | Hold（無臨床試驗/文獻） |
| 2 | 原發性肺淋巴瘤 (Primary Pulmonary Lymphoma) | 99.45% | L3 | Research Question |
| 3 | 小細胞肺癌 (Small Cell Lung Carcinoma) | 99.43% | L3 | Research Question（現行標準已為 platinum-etoposide，MTX 屬歷史用藥） |
| 4 | 分化良好胎兒型肺腺癌 | 99.42% | L5 | Hold（無臨床試驗/文獻） |
| **5** | **何杰金氏淋巴瘤（本報告主軸）** | **99.32%** | **L2** | **Proceed with Guardrails** |

---

## 細胞毒性

**判定依據**：本藥物涉及的預測適應症均屬腫瘤（淋巴瘤、肺癌），且證據內文明確描述 MTX 為「DHFR 抑制劑/抗葉酸廣效抗腫瘤藥」，屬傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗葉酸類 / DHFR 抑制劑） |
| 骨髓抑制風險 | 高（文獻多次描述骨髓抑制，高劑量方案需併用 leucovorin rescue 以降低毒性） |
| 致吐性分級 | 中度（依劑量與給藥途徑而異，低劑量口服致吐性低，高劑量靜脈/鞘內致吐性中高） |
| 監測項目 | CBC（含分類）、肝腎功能、MTX 血中濃度監測（尤其高劑量方案）、口腔黏膜炎評估 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；高劑量方案需搭配 leucovorin rescue 及水化保腎 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（限何杰金氏淋巴瘤候選；其餘 4 個候選維持 Hold）

**理由：**
- 何杰金氏淋巴瘤候選有多篇世代研究（VBM 方案）與 Phase 2/3 試驗支持 MTX 之歷史治療角色，證據等級達 L2，但現行第一線標準已為 ABVD，MTX 定位需限縮於特定次族群（復發/難治、ABVD 禁忌患者）。
- 其餘 4 個候選（肺母細胞瘤、原發性肺淋巴瘤、小細胞肺癌、分化良好胎兒型肺腺癌）證據強度僅達 L3 或 L5，暫不具行動基礎。

**若要推進需要：**
- 補齊 TFDA/HK 仿單警語與禁忌症資料（DG001，Blocking，目前無法進入 S1 安全性初評）
- 補充 MOA 詳細資料（DG002）
- 確認香港/台灣在地上市與許可證現況（目前查無資料）
- 針對何杰金氏淋巴瘤界定明確次族群使用情境（如復發/難治族群）並補充最新 RCT 資料
- 其餘 4 個候選需待更多臨床試驗/文獻資料累積後再重新評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

