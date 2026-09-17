---
layout: default
title: Sofosbuvir
parent: 中證據等級 (L3-L4)
nav_order: 698
evidence_level: L4
indication_count: 5
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Sofosbuvir：從C型肝炎到B型肝炎病毒感染

## 一句話總結

Sofosbuvir 是 HCV NS5B RNA 聚合酶抑制劑，原本用於治療慢性C型肝炎（此為根據證據包內多數臨床試驗上下文推斷，非官方許可證資料）。
TxGNN 模型預測它可能對**B型肝炎病毒感染 (Hepatitis B Virus Infection)** 有效，
目前有 **50 個臨床試驗**和 **19 篇文獻**與此標籤關聯，但證據包本身的機轉分析指出，這些研究多屬「HCV/HBV 共感染治療」或「HCV 治療後 HBV 再活化」安全性訊號，**並非直接針對 HBV 的抗病毒療效證據**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性C型肝炎（Hepatitis C）— 依證據包內多數試驗/文獻上下文推斷，非取自官方許可證，因香港無上市紀錄 |
| 預測新適應症 | B型肝炎病毒感染 (Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.77%（rank 5074） |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（drug-level MOA 標記為 Data Gap）。但根據證據包中各筆預測的 `repurposing_rationale` 內容，Sofosbuvir 抑制的是 HCV（Flaviviridae/Hepacivirus）的 **NS5B RNA 依賴型 RNA 聚合酶**，這是其抗 HCV 療效的核心機轉。

然而 HBV 屬於 Hepadnaviridae，是以**反轉錄酶**複製的 DNA 病毒，並非 Sofosbuvir 的作用標的。證據包中的機轉分析明確指出：「**直接抗 HBV 機轉不成立**」。

列出的 50 個臨床試驗與 19 篇文獻，絕大多數的研究情境是「HCV/HBV 共感染病人接受抗 HCV 治療」或「DAA 治療 HCV 後觀察到的 HBV 再活化（reactivation）安全性訊號」，而非證實 Sofosbuvir 對 HBV 本身具抗病毒活性。TxGNN 給出的高分，較可能來自知識圖譜中「Sofosbuvir」與「HBV」在共感染/共病文獻中的高度共現（co-occurrence），而非真實的藥理學關聯。這也是本案評為 **L4 / Hold** 的核心原因。

---

## 臨床試驗證據

> 說明：以下僅列出與 HBV 直接相關（HBV 單純感染或 HCV/HBV 共感染／再活化研究）的試驗；證據包中其餘 40+ 筆多為單純 HCV 治療試驗，經人工判讀為不相關（grade C）或標題與 HBV 無關，故不納入。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | 完成 | 21 | Ledipasvir/Sofosbuvir 治療**HBV單純感染**病人12週，評估 HBsAg 及 HBV DNA 下降情形——是本清單中唯一直接針對 HBV（非共感染）的試驗 |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | 完成 | 111 | LDV/SOF 複方於台灣 HCV genotype 1/2 合併 HBV 共感染病人之抗病毒療效與安全性 |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 完成 | 23 | 前瞻性研究 HCV/HBV 共感染病人接受抗 HCV DAA 治療時 **HBV 再活化**之發生率與危險因子 |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | 未知 | 21 | HARVONI (LDV/SOF) 用於 HCV 相關（可能含 HBV/HDV 共感染族群）indolent B 細胞淋巴瘤之 Pilot 研究，標題截斷需人工核實確切病毒標的 |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | SOF/VEL 合併預防性 TAF，用於 HCV/HBV 共感染病人，評估治療期間 **HBV 再活化預防**效果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Cohort (Tier 2) | J Med Virol | LDV/SOF 用於 **HBV 單純感染**病人之 Phase 2 開放性研究，評估 HBsAg/HBV DNA 於第12週之下降幅度 |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | pending | Clin Infect Dis | 台灣 HCV/HBV 共感染病人接受 LDV/SOF 治療後，108週追蹤 HBV 再活化情形 |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort (Tier 2) | Trans R Soc Trop Med Hyg | Sofosbuvir/Daclatasvir 治療埃及 HCV 及 HCV/HBV 共感染病人之療效 |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | pending | J Clin Gastroenterol | 檢視接受 LDV/SOF 治療 HCV 的病人中，**HBV 再活化**風險 |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | pending | Infect Drug Resist | HCV-HBV 共感染病人於 DAA 治療後 HBV 再活化之處置策略 |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report (Tier 3, 安全性訊號) | Medicine | SOF+ribavirin 成功治療 HCV 後發生 **HBV 再活化**之病例報告 |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | pending | J Viral Hepat | 癌症病人接受 DAA 治療 HCV 時 HBV 再活化風險之前瞻性觀察研究 |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | pending | Lancet Gastroenterol Hepatol | 2022年全球 HBV 盛行率、照護級聯與預防涵蓋率建模研究（背景流行病學資料，非治療性證據） |

---

## 香港上市資訊

目前無許可證資料——Sofosbuvir **尚未在香港上市**（`market_status: 未上市`，許可證數：0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充：本案 TFDA/HK 仿單警語與禁忌症資料屬 **Blocking 等級資料缺口 (DG001)**，在補齊前無法進行 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據包自身的機轉分析已明確否定 Sofosbuvir 對 HBV 的直接抗病毒機轉（NS5B 聚合酶抑制劑 vs. HBV 反轉錄酶複製機制不匹配）。
- 現有 50 筆試驗與 19 篇文獻中，具直接相關性者僅個位數，且多為「共感染治療」或「HBV 再活化安全性訊號」研究，**並非 HBV 療效證據**；TxGNN 高分可能源自知識圖譜中的共現詞彙混淆。
- 藥品尚未在香港上市，且缺乏仿單警語/禁忌（Blocking data gap）與正式 MOA 資料，無法通過 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking）。
- 取得正式 DrugBank MOA 確認資料（DG002，High）。
- 針對 NCT03312023（唯一 HBV 單純感染試驗，N=21）進行結果人工核實，確認是否有陽性訊號可支持後續假說。
- 若欲深入評估，建議同時關注 TxGNN 預測清單中 rank 2「E型肝炎病毒感染」——該項具體外抑制實驗與個案系列支持（L3 / Research Question），機轉合理性（同屬 RdRp 結構相似之 RNA 病毒）較 HBV 更具說服力。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

