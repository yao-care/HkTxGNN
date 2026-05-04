---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 5
---

# Etoposide
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

# Etoposide：五項腫瘤再利用適應症評估（以尤文肉瘤為主要推薦）

## 一句話總結

Etoposide（依托泊苷，DB00773）是一種拓撲異構酶 II 抑制劑，目前在香港尚無核准上市紀錄。TxGNN 模型預測其在 5 個腫瘤適應症具有再利用潛力，其中**尤文肉瘤 (Ewing Sarcoma)** 具備最高等級的臨床證據（**L1**），有多項大型 Phase 3 RCT 直接支持含 Etoposide 方案的療效，且機轉上對尤文肉瘤特有的 EWS-FLI1 融合蛋白所造成的 DNA 修復缺陷具有協同毒性；**原發性肺淋巴瘤 (Primary Pulmonary Lymphoma)** 亦有 L3 等級間接臨床支持；其餘 3 項適應症因缺乏充分直接證據，建議暫緩或作為研究方向。

---

## 所有預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗數 | 文獻數 | 證據等級 | 建議決策 |
|------|--------|-----------|-----------|--------|---------|---------|
| 1 | 高分化胎兒型肺腺癌 (WDFAC) | 99.94% | 0 | 1 | L4 | Hold |
| 2 | **原發性肺淋巴瘤 (PPL)** | 99.94% | 18 | 20 | L3 | **Proceed with Guardrails** |
| 3 | 肺母細胞瘤 (Pulmonary Blastoma) | 99.94% | 0 | 20 | L4 | Research Question |
| 4 | **尤文肉瘤 (Ewing Sarcoma)** | 99.85% | 47 | 20 | **L1** | **Proceed with Guardrails** |
| 5 | 陰道葡萄狀胚胎性橫紋肌肉瘤 | 99.80% | 0 | 0 | L5 | Hold |

---

## 快速總覽（主要推薦：尤文肉瘤）

| 項目 | 內容 |
|------|------|
| 香港核准適應症 | 香港未有核准上市紀錄 |
| 主要預測新適應症 | 尤文肉瘤 (Ewing Sarcoma) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L1（≥2 個已完成 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

### 作用機轉

根據 Evidence Pack 中的再利用機轉說明（repurposing_rationale）及相關文獻（PMID 29513652），Etoposide 是一種拓撲異構酶 II（Topo II）抑制劑。它透過穩定 Topo II-DNA 共價複合體，阻止拓撲異構酶 II 完成 DNA 的切割-重接循環，導致 DNA 雙股斷裂（DSB）累積，最終觸發細胞凋亡。此機轉對快速增殖腫瘤細胞（尤其是 S 期和 G2 期細胞）具有高度毒性。

### 尤文肉瘤的機轉關聯性

尤文肉瘤的分子特徵為 EWS-FLI1 融合蛋白（由 t(11;22)(q24:q12) 染色體易位產生）。此融合蛋白會在基因組中造成 R-loop 異常積累，並阻礙 BRCA1 介導的 DNA 雙股斷裂修復（PMID 29513652）。這使得尤文肉瘤細胞對 DNA 損傷性藥物異常敏感。Etoposide 正是尤文肉瘤一線標準化療方案 **VDC/IE**（vincristine/doxorubicin/cyclophosphamide 交替 ifosfamide/etoposide）的核心成分，已在多個大型 Phase 3 RCT（如 PMID 12594313，NEJM 2003）中獲得直接驗證，存活率從化療前的約 10% 提升至局限性疾病的約 75%（PMID 20152770）。

### 原發性肺淋巴瘤的機轉關聯性

原發性肺淋巴瘤（PPL）為結外淋巴瘤的罕見亞型，病理分型以 MALT、DLBCL 及 NK/T 細胞型為主。其系統性化療策略與其他部位非霍奇金淋巴瘤高度重疊，而 Etoposide 是 EPOCH（etoposide/prednisone/vincristine/cyclophosphamide/doxorubicin）和 ICE（ifosfamide/carboplatin/etoposide）等核心淋巴瘤化療方案的主要組成。Lymphomatoid granulomatosis（肺部 EBV 相關 B 細胞淋巴增生疾病）的 Phase 2 研究（NCT00001379）直接支持含 Etoposide 方案在肺部淋巴瘤的臨床可行性。

---

## 詳細評估：尤文肉瘤 (Ewing Sarcoma) — L1 等級

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 完成 | 642 | VDC/IE 為標準對照方案，含 Etoposide 的 IE 交替方案為非轉移性尤文肉瘤現行基準 |
| [NCT00876031](https://clinicaltrials.gov/study/NCT00876031) | Phase 3 | 完成 | 195 | 評估含 etoposide 口服維持化療（O-TIE）6 個月是否改善高風險肉瘤 EFS |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | 完成 | 155 | 高劑量化療合併放療及 cyclophosphamide 鞏固治療轉移性尤文肉瘤，直接評估含 etoposide 鞏固方案 |
| [NCT00001335](https://clinicaltrials.gov/study/NCT00001335) | Phase 2 | 完成 | 90 | NIH 研究尤文肉瘤家族腫瘤新治療策略，含 etoposide 強化方案，90 人完成 |
| [NCT01946529](https://clinicaltrials.gov/study/NCT01946529) | Phase 2 | 進行中 | 24 | 依風險分層直接針對尤文肉瘤家族腫瘤的含 etoposide 方案評估 |
| [NCT00003657](https://clinicaltrials.gov/study/NCT00003657) | Phase 2 | 完成 | 24 | 高劑量 ICE（含 etoposide）合併 amifostine 保護，直接評估劑量強化方案於尤文肉瘤 |
| [NCT07194044](https://clinicaltrials.gov/study/NCT07194044) | Phase 1 | 招募中 | 15 | 轉移性尤文肉瘤演化原則強化方案，反映 etoposide 方案最新優化研究動態 |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | 進行中 | 83 | 伊立替康+替莫唑胺加入 etoposide 骨幹方案（VDC/IE），評估新組合對新診斷尤文肉瘤 |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | 進行中 | 437 | VIrR 聯合 VDC/IE 對比 VDC/IE 標準方案治療轉移性尤文肉瘤，是目前規模最大的進行中試驗 |
| [NCT00617890](https://clinicaltrials.gov/study/NCT00617890) | Phase 2 | 已終止 | 219 | IGF-1R 抑制劑（robatumumab）合併 etoposide 背景化療於尤文肉瘤；已終止，但提供組合治療安全性資料 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | Phase 3 RCT | NEJM | 將 ifosfamide+etoposide 加入標準方案，顯著改善尤文肉瘤存活率；確立 IE 為標準組成 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | Phase 3 RCT | Lancet | EE2012 試驗比較歐洲（VIDE/VAI）與美國（VDC/IE）含 etoposide 標準方案，療效相當 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Phase 3 RCT | Trials | EURO EWING 2012 國際多中心 RCT 設計，含 etoposide 方案的直接頭對頭比較 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | 專家共識/指引 | Cancer | 國家尤文肉瘤腫瘤委員會共識：VDC/IE 仍為標準一線方案，etoposide 地位不可替代 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | Phase 3 RCT | JCO | AEWS1221：ganitumab 加入含 etoposide 間歇壓縮化療；確認含 etoposide 骨幹方案安全性 |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | Phase 3 RCT | JCO | Ewing 2008R3：高劑量鞏固 vs 含 etoposide 標準方案，高風險轉移性 ES |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | 系統性回顧 | Lancet Oncol | 尤文肉瘤治療進展回顧：多藥方案含 etoposide 使局限性疾病存活率提升至約 75% |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | 機轉研究 | Nature | EWS-FLI1 造成 R-loop 積累並阻礙 BRCA1 修復，解釋尤文肉瘤對 etoposide 的高敏感性 |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | 回顧性研究 | Sarcoma | 口服 etoposide 用於復發/難治尤文肉瘤（33 例，青少年/成人），顯示單藥活性 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | 系統性回顧 | JCO | 尤文肉瘤多模式治療現況與國際合作展望，含 etoposide 方案為全球核心 |

---

## 詳細評估：原發性肺淋巴瘤 (PPL) — L3 等級

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00001379](https://clinicaltrials.gov/study/NCT00001379) | Phase 2 | 完成 | 94 | Lymphomatoid granulomatosis（肺部 EBV 相關 B 細胞淋巴增生）評估 alpha 干擾素或含 etoposide 化療，與 PPL 解剖位置及免疫表現高度相關 |
| [NCT01092182](https://clinicaltrials.gov/study/NCT01092182) | Phase 2 | 完成 | 194 | DA-EPOCH-R（含 etoposide）治療 Burkitt 淋巴瘤及 c-MYC+ DLBCL，方案可外推至侵襲性 PPL |
| [NCT03077828](https://clinicaltrials.gov/study/NCT03077828) | Phase 2 | 未知 | 43 | Pembrolizumab + ICE（含 etoposide）治療復發/難治性霍奇金淋巴瘤；狀態 UNKNOWN 降低可信度 |
| [NCT00051311](https://clinicaltrials.gov/study/NCT00051311) | Phase 2 | 完成 | 62 | EPOCH 方案（含 etoposide）誘導治療難治性淋巴瘤，62 人完成，支持方案安全性 |
| [NCT01445535](https://clinicaltrials.gov/study/NCT01445535) | Phase 1 | 完成 | 15 | Siplizumab + DA-EPOCH-R 治療 T/NK 細胞淋巴瘤，與部分 PPL 亞型（ENKTL）相關 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27332902](https://pubmed.ncbi.nlm.nih.gov/27332902/) | 2016 | RCT | NEJM | PET-CT 導向治療進階霍奇金淋巴瘤，含 etoposide 強化方案（BEACOPPesc）應用 |
| [34350085](https://pubmed.ncbi.nlm.nih.gov/34350085/) | 2021 | 回顧性研究 | Cureus | R-CEOP（含 etoposide）治療原發性縱隔 B 細胞淋巴瘤，與侵襲性 PPL 分型具相關性 |
| [34329577](https://pubmed.ncbi.nlm.nih.gov/34329577/) | 2021 | 臨床試驗報告 | Lancet Haematology | BV-ICE（含 etoposide）二線治療復發/難治性霍奇金淋巴瘤，Phase 1/2 |
| [32590768](https://pubmed.ncbi.nlm.nih.gov/32590768/) | 2020 | 案例報告 | Medicine | 原發性肺 NK/T 細胞淋巴瘤（ENKTL，鼻型）2 例報告及文獻回顧，18 例累積 |
| [25527680](https://pubmed.ncbi.nlm.nih.gov/25527680/) | 2014 | 案例報告 | BMJ Case Reports | AIDS 相關 PPL 案例，說明 PPL 臨床特徵及化療挑戰 |

---

## 其他預測適應症（簡要說明）

### 肺母細胞瘤 (Pulmonary Blastoma) — L4 等級

**決策：Research Question**

肺母細胞瘤為極罕見的雙相性肺部惡性腫瘤（佔原發性肺癌不到 0.5%），目前無標準化療指引。現有 20 篇文獻以案例報告或小型系列為主，其中有紀錄顯示 cisplatin+etoposide 組合曾在個案中嘗試（PMID [11955657](https://pubmed.ncbi.nlm.nih.gov/11955657/)），並有 CCNU+vincristine+VP-16（即 etoposide）+cyclophosphamide 達完全緩解的 1984 年案例（PMID [6086368](https://pubmed.ncbi.nlm.nih.gov/6086368/)）。理論上有機轉活性，但缺乏對照研究，建議作為科學問題探索，不建議直接臨床推進。

### 高分化胎兒型肺腺癌 (WDFAC) — L4 等級

**決策：Hold**

WDFAC 是肺母細胞瘤的罕見亞型。唯一相關文獻（PMID [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/)）為雙相性肺母細胞瘤個案報告，與 WDFAC 僅有組織學相關性，無直接 etoposide 使用紀錄。無任何臨床試驗，暫不建議推進。

### 陰道葡萄狀胚胎性橫紋肌肉瘤 — L5 等級

**決策：Hold**

無任何臨床試驗或文獻支持此特定適應症。雖然 Etoposide 在 VAC/IE 方案中用於橫紋肌肉瘤，但此特定罕見亞型缺乏任何直接證據，不建議推進。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Epipodophyllotoxin 類，Topo II 抑制劑） |
| 骨髓抑制風險 | 高度（劑量限制性毒性：嗜中性白血球減少症、血小板減少症為主要毒性） |
| 致吐性分級 | 中度（口服劑型低至中度；靜脈劑型依劑量強度為中至高度） |
| 監測項目 | CBC（含分類計數）、血小板、肝功能（ALT/AST/膽紅素）、腎功能（Cr/eGFR） |
| 繼發性惡性腫瘤風險 | 蓄積劑量相關的繼發性 AML/MDS 風險，需納入長期隨訪計畫 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈劑型含 polysorbate 80，需注意過敏/低血壓反應 |

---

## 安全性考量

安全性資訊請參考原廠仿單。由於香港目前無已核准的 Etoposide 上市製品，建議參考 FDA、EMA 或其他國際認可機構核准的藥品仿單，以及現行臨床腫瘤學指引（如 NCCN、ESMO）中的劑量調整與毒性管理建議。

---

## 結論與下一步

### 🟢 尤文肉瘤（優先推薦）

**決策：Proceed with Guardrails**

**理由：**
Etoposide 是尤文肉瘤一線標準化療方案（VDC/IE）的核心成分，多項大型 Phase 3 RCT 直接驗證療效，機轉與 EWS-FLI1 相關 DNA 修復缺陷具協同效應，是本報告中唯一達到 L1 證據等級的再利用候選。

**若要推進需要：**
- 向香港衛生署申請特別用藥許可（Specific Drug Application）或引入 Etoposide 上市申請
- 建立本地腫瘤科使用規範及骨髓抑制監測計畫（含 G-CSF 預防性使用決策）
- 制定繼發性惡性腫瘤（AML/MDS）長期隨訪方案
- 補充完整的作用機轉（MOA）及香港仿單安全性資料

### 🟡 原發性肺淋巴瘤（有條件推進）

**決策：Proceed with Guardrails**

**理由：**
多個 Phase 2 試驗間接支持含 etoposide 方案（EPOCH、ICE）在各型淋巴瘤的療效，PPL 的病理生物學與系統性淋巴瘤高度重疊，具備合理外推基礎，但缺乏 PPL 專屬 RCT。

**若要推進需要：**
- 建立香港 PPL 病例登記，收集本地流行病學及治療數據
- 與國際罕見淋巴瘤研究網絡合作，探索納入含 etoposide 方案的前瞻性小型研究
- 取得完整安全性仿單資料

### 🔵 肺母細胞瘤（研究方向）

**決策：Research Question**

**若要推進需要：**
- 加入國際稀有肺腫瘤登記（如 EORTC 罕見癌症工作組）
- 開展基礎研究驗證 Topo II 在肺母細胞瘤的表達及 etoposide 體外敏感性

---

> **免責聲明：** 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過嚴格臨床驗證才能應用於實際患者治療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

