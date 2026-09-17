---
layout: default
title: Ozanimod
parent: 中證據等級 (L3-L4)
nav_order: 551
evidence_level: L3
indication_count: 1
---

# Ozanimod
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Ozanimod：從多發性硬化症（復發型）到多發性硬化症（進行性復發型）

## 一句話總結

Ozanimod 是一種口服 S1P1/S1P5 受體調節劑，國際藥證資料顯示其原本核准用於**復發型多發性硬化症**（RRMS、有活動性證據的次發進行性 MS、臨床孤立症候群）。
TxGNN 模型預測它可能對**進行性復發型多發性硬化症 (Progressive Relapsing Multiple Sclerosis, PRMS)** 有效，
目前有 **8 個臨床試驗**與 **18 篇文獻**可供參考，但均非針對 PRMS 族群的直接療效驗證。

> 註：Ozanimod 目前於**香港未上市**，故無本地許可證上之核准適應症資料；上述「原適應症」係依 Evidence Pack 中文獻（PMID 32385738）所載之國際藥證核准範圍。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 多發性硬化症復發型（RRMS／活動性 SPMS／CIS，依國際藥證文獻） |
| 預測新適應症 | 進行性復發型多發性硬化症 (Progressive Relapsing Multiple Sclerosis) |
| TxGNN 預測分數 | 99.34%（原始分數 0.9934，模型內排名第 10971 位） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Ozanimod 屬於 S1P1/S1P5 受體調節劑，透過抑制淋巴球從淋巴結釋出，減少自體反應性 T/B 細胞進入中樞神經系統，是一種免疫調節機轉，對「發炎／復發驅動」的 MS 病程有理論基礎。

然而，PRMS 是 2013 年前的舊分類，特徵是自發病起即呈進行性病程並伴隨偶發復發，其病理主要由神經退化驅動，而非單純周邊免疫細胞浸潤——這與 ozanimod 樞紐試驗（SUNBEAM/RADIANCE）鎖定的「復發型 MS」族群並不完全相同。

更值得注意的是，同類 S1P 調節劑中，fingolimod 在原發進行性 MS 的 INFORMS 試驗已證實無效，siponimod 也僅對「有活動性證據的次發進行性 MS」有限度有效。這顯示此藥物類別對「進行性」成分的效果本身有限，機轉外推到 PRMS 存在明確的不確定性，需要專門的族群驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | 已完成 | 2494 | SUNBEAM 樞紐試驗，RPC1063(ozanimod) 口服治療復發型 MS 之療效與安全性（雙盲雙模擬、活性對照），為核准之關鍵證據，但未特異針對 PRMS |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | 進行中（暫停招募） | 800 | DELIVER-MS：比較早期積極 vs. 升階治療策略於復發型 MS 之長期預後，涉及疾病進展控制議題 |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | 招募中 | 60 | 觀察性研究，預測 S1P 受體調節劑（含 ozanimod）治療下 MS 疾病活性與停藥反彈風險，與機轉直接相關但樣本小 |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | 進行中（暫停招募） | 84 | 中國族群單臂開放標籤研究，評估口服 ozanimod 用於復發型 MS 之有效性與安全性，缺乏對照組 |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | 進行中（暫停招募） | 900 | 實用性試驗比較早期積極 vs. 升階治療策略對長期失能之影響，非藥物本身療效之直接驗證 |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | 進行中（暫停招募） | 9000 | ORION：上市後真實世界安全性登錄研究，比較 ozanimod 與其他 S1P 調節劑之不良事件發生率，僅涉及安全性監測 |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | 邀請招募 | 323 | STATURE：口服 DMT（含 ozanimod）治療負擔與遵從性之觀察性研究，與 PRMS 療效無直接關聯 |
| [NCT05688436](https://clinicaltrials.gov/study/NCT05688436) | N/A | 招募中 | 1178 | 研究對象為 diroximel fumarate（非 ozanimod）暴露孕婦之妊娠結果，藥物錯配，僅具背景參考價值 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | 統合分析 (NMA) | Cochrane Database Syst Rev | 進行性 MS 免疫調節/免疫抑制治療之網絡統合分析，直接對應 PRMS 相關族群 |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | 統合分析 (NMA) | Cochrane Database Syst Rev | RRMS 免疫調節/免疫抑制治療之網絡統合分析更新版 |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | 法規審查 | Drugs | Ozanimod 首次核准回顧，確認美國 FDA 核准範圍為「復發型 MS」（CIS、RRMS、活動性次發進行性） |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | 回顧 | Neurology International | Ozanimod 治療復發型 MS 之完整回顧，涵蓋疾病、藥效與副作用 |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | 回顧 | Ther Adv Neurol Disord | 進行性 MS 最新治療發展與未來方向，討論進行性病程之致病機轉 |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | 回顧 | Expert Opin Pharmacother | S1P 受體調節劑用於復發型 MS 治療之最新進展 |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | 回顧 | Front Immunol | 中樞神經系統可及性 DMT 回顧，指出多數藥物在進行性 MS 中療效有限或未充分驗證 |
| [32059809](https://pubmed.ncbi.nlm.nih.gov/32059809/) | 2020 | 回顧 | Lancet Neurol | 復發型 MS 口服免疫調節療法進展，涵蓋 fingolimod、DMF、teriflunomide、cladribine |
| [35805142](https://pubmed.ncbi.nlm.nih.gov/35805142/) | 2022 | 回顧（機轉） | Cells | S1P 及 S1P 訊號路徑調節劑機轉回顧，說明其在自體免疫疾病致病機轉中角色尚未完全釐清 |
| [28812220](https://pubmed.ncbi.nlm.nih.gov/28812220/) | 2017 | 回顧 | Neurotherapeutics | S1P 受體調節劑用於 MS 治療之機轉回顧，說明淋巴球隔離之作用原理 |

---

## 香港上市資訊

Ozanimod 目前於香港**未上市**，無許可證登記資料，故無法提供核准適應症範圍。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 現有最相關的樞紐證據（SUNBEAM Phase 3, NCT02576717）與大型安全性登錄（ORION）均聚焦「復發型 MS」，而非 PRMS 這個以神經退化為主的特殊表型；機轉論證明確指出同類 S1P 調節劑（fingolimod INFORMS 試驗失敗、siponimod 效果有限）對「進行性」成分效果不佳，證據等級僅 L3，決策階段仍屬 S1 研究問題。
- 藥物在香港未上市、缺乏完整 MOA 與安全性仿單資料（DG001 為 Blocking 缺口），現階段不具備進入下一階段評估之條件。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking）
- 取得完整作用機轉（MOA）詳細資料（DG002，High）
- 尋找或設計針對 PRMS 特異族群的療效驗證研究（現有試驗多為 RRMS 療效或上市後安全性登錄）
- 評估藥廠是否有意在香港申請上市許可
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

