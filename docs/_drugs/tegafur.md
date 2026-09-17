---
layout: default
title: Tegafur
parent: 高證據等級 (L1-L2)
nav_order: 723
evidence_level: L1
indication_count: 5
---

# Tegafur
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

# Tegafur：從氟嘧啶類化療成分到大腸腫瘤（Colonic Neoplasm）

## 一句話總結

Tegafur 是 5-FU 的口服前驅藥，屬於氟嘧啶類抗代謝化療成分（UFT、S-1 複方皆含此成分）。
TxGNN 模型預測它對**大腸腫瘤 (Colonic Neoplasm)** 有效，
目前有 **31 個臨床試驗**和 **21 篇文獻**支持這個方向，其中多項為千人以上的完成 Phase 3 RCT。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港未上市，無核准適應症資料（成分屬氟嘧啶類抗代謝化療藥物） |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Tegafur 為 5-FU 的口服前驅藥（prodrug），經肝臟 CYP2A6 代謝活化為 5-fluorouracil，抑制胸苷酸合成酶（thymidylate synthase），阻斷 DNA 合成，屬經典氟嘧啶類抗代謝化療機轉。DrugBank 層級的正式 MOA 資料目前為 Data Gap，但此機轉描述可由多篇臨床文獻與試驗設計交叉驗證（如 NCT00197431 探討 CYP2A6/DPD 基因多型性對 S-1 藥效之影響）。

嚴格來說，這並非典型的「新」再利用假說：Tegafur 為成分之含 UFT（tegafur+uracil）與 S-1（tegafur+gimeracil+oteracil）複方，兩者皆已是日本與多國指引中大腸直腸癌標準輔助/轉移性治療用藥。本報告的證據本質上是既有標準治療證據的彙整，而非機轉外推。

香港目前無 Tegafur 單方或其複方製劑的許可證登記，代表此適應症若要落地，需透過 UFT 或 S-1 等複方途徑申請上市，而非單方 Tegafur。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | 完成 | 161 | S-1 vs Capecitabine 一線治療轉移性結直腸癌之隨機分派安全性評估 |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | 完成 | 2025 | UFT 輔助化療 vs 觀察，用於根治性切除後 Stage II 結腸癌 |
| [NCT02887365](https://clinicaltrials.gov/study/NCT02887365) | Phase 4 | 未知 | 300 | Tegafur-Uracil 作為 Stage II MSI-L/MSS 結腸癌維持化療之療效與安全性 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | UFT+LV vs S-1(TS-1) 輔助治療 Stage III 結腸癌，並分析基因表現預測因子 |
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | 完成 | 1608 | 口服 UFT+LV vs 靜脈 5-FU+LV 治療 Stage II/III 結腸癌 |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | 完成 | 900 | UFT 術後輔助化療 vs 單純手術，用於 Dukes C 結直腸癌（NSAS-CC） |
| [NCT00898846](https://clinicaltrials.gov/study/NCT00898846) | N/A | 完成 | 1111 | UFT 輔助化療於 Stage II 結腸癌患者之預後因子研究 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 未知 | 1191 | SOX（含 S-1）vs XELOX 輔助化療於 Stage III 結直腸癌之比較 |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | 完成 | 89 | Xeloda vs UFT+Folinic Acid 交叉試驗，晚期/轉移性結直腸癌患者偏好與安全性比較 |
| [NCT00439517](https://clinicaltrials.gov/study/NCT00439517) | Phase 2 | 完成 | 302 | FOLFOX-4+Cetuximab vs UFOX（含 UFT）+Cetuximab 一線治療轉移性結直腸癌 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC02 試驗更新 5 年總存活率，SOX vs UFT/LV 於高風險 Stage III 結腸癌輔助治療 |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC02 Phase III 優越性試驗，SOX 未證實優於 UFT/LV（DFS 無顯著差異） |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT | Medicine | 台灣全國性世代研究+統合分析，UFT vs 5-FU 作為 Stage II/III 結腸癌術後輔助化療比較 |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06 試驗，口服 UFT+LV 與靜脈 5-FU+LV 於 Stage II/III 結腸癌之 DFS/OS 比較 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | OK-432 免疫治療合併 UFT/HCFU 口服嘧啶類藥物之輔助化療隨機對照試驗 |
| [6402917](https://pubmed.ncbi.nlm.nih.gov/6402917/) | 1983 | RCT | Am J Clin Oncol | 口服 Tegafur 與靜脈 5-FU 於轉移性結直腸癌療效與毒性比較 |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT | Ann Oncol | JFMC33-0502 試驗，UFT/LV 輔助化療於 Stage IIB/III 結腸癌之治療期間比較（最終結果） |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT 作為肺/胃/結直腸/乳癌術後輔助化療之臨床證據、機轉與未來方向回顧 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | 亞洲轉移性結直腸癌治療共識，調整國際指引以符合亞洲人群 |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Observational | BMC Cancer | JFMC46-1201 前瞻性觀察研究，傾向分數配對評估 UFT/LV 於高復發風險 Stage II 結腸癌之療效 |

## 香港上市資訊

目前香港未上市，無許可證登記。Tegafur 單方及其複方（UFT、S-1）皆未在香港取得許可證。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類，5-FU 前驅藥，經 CYP2A6 代謝活化） |
| 骨髓抑制風險 | 資料不足，請參考原廠仿單的警語與注意事項（同類氟嘧啶藥物臨床上常見嗜中性白血球減少、血小板減少；文獻中亦見 UFT 誘發溶血性貧血個案報告 [PMID 11320674]） |
| 致吐性分級 | 資料不足，請參考原廠仿單的警語與注意事項 |
| 監測項目 | CBC（含分類）、肝腎功能；DPD/CYP2A6 基因型篩檢（見 NCT05266300、NCT00197431） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA/香港仿單警語與禁忌症資料為 Blocking 級資料缺口，尚未取得）

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多項大型已完成 Phase 3 RCT（ACTS-CC02、NSABP C-06、JFMC 系列）已證實含 Tegafur 之複方（UFT、S-1）為結直腸癌標準輔助/轉移性治療用藥，證據等級達 L1；但 Tegafur 在香港無任何許可證登記，且安全性仿單資料為 Blocking 缺口，須先補齊才可進入下一階段安全性初評。

**若要推進需要：**
- 取得 TFDA/香港仿單警語與禁忌症資料，解除 DG001（Blocking）
- 補充正式 DrugBank 作用機轉文件，解除 DG002
- 確認以 UFT 或 S-1 複方途徑申請香港上市（Tegafur 單方目前無許可證）
- 建立 DPD 缺乏症（DPYD 基因型）篩檢方案，因氟嘧啶類藥物毒性風險與代謝酶活性相關
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

