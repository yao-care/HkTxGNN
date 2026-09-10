---
layout: default
title: Norethisterone
parent: 高證據等級 (L1-L2)
nav_order: 530
evidence_level: L2
indication_count: 1
---

# Norethisterone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **1** 個
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

# Norethisterone：從黃體素療法到續發性閉經 (Amenorrhea)

## 一句話總結

Norethisterone 是一種合成黃體素（progestin），廣泛用於避孕與月經相關治療，但本次 Evidence Pack 未收錄其正式核准適應症與完整作用機轉資料。TxGNN 模型預測它可能對**續發性閉經 (Amenorrhea)** 有效，目前有 **8 個臨床試驗**（含 3 個已完成的 Phase 3 RCT）和 **20 篇文獻**支持這個方向，但多數證據來自它作為 GnRH 拮抗劑合併療法中的 add-back 成分，而非單方直接治療閉經的證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未收錄（原始適應症與 MOA 待查證，對應資料缺口 DG002） |
| 預測新適應症 | 續發性閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.60%（rank 7685） |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Evidence Pack 標記為資料缺口）。但根據已知臨床藥理學常識，norethisterone 是合成黃體素，可抑制下視丘-腦下垂體-卵巢軸並抑制子宮內膜增生，臨床上常作為誘導/調節閉經的黃體素成分使用。

本資料集中的關聯證據，主要並非測試 norethisterone 單方治療閉經，而是它在 GnRH 拮抗劑（relugolix、elagolix）合併療法中作為「add-back」成分，用於子宮肌瘤／大量經血治療，其中「誘導閉經 (amenorrhea induction)」是這些試驗的關鍵次要療效指標之一。這代表機轉關聯明確且成熟，但目前所附試驗多屬間接（合併療法脈絡），尚無 norethisterone 單方對閉經適應症的直接對照試驗。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) | Phase 3 | 完成 | 388 | LIBERTY 1：relugolix + estradiol + norethindrone acetate 對比安慰劑，治療子宮肌瘤相關大量經血，達成閉經為關鍵次要指標 |
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) | Phase 3 | 完成 | 382 | LIBERTY 2：與 LIBERTY 1 同設計、同藥物組合的重複驗證試驗 |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) | Phase 3 | 完成 | 477 | LIBERTY EXTENSION：長期開放性延伸試驗，驗證持續閉經效果與安全性 |
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) | N/A | 招募中 | 111 | Relugolix + estradiol + norethisterone 治療期間子宮肌瘤超音波影像變化觀察 |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Phase 3 | 完成 | 229 | Relugolix + estradiol + norethindrone acetate 停藥後隨機分組研究，評估長期療效安全性 |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2 | 完成 | 271 | Elagolix 治療子宮肌瘤大量經血之概念驗證研究，未提及 norethisterone，關聯性較弱 |
| [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) | Phase 3 | 未知 | 312 | BG2109 合併 add-back 療法治療子宮肌瘤大量經血，成分細節不明，追蹤已中斷 |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2 | 完成 | 571 | Elagolix 合併/不合併 add-back 療法治療子宮肌瘤大量經血，未見 norethisterone 成分 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37863160](https://pubmed.ncbi.nlm.nih.gov/37863160/) | 2024 | RCT（亞族群分析） | Am J Obstet Gynecol | Relugolix + estradiol + norethindrone acetate 合併療法在黑人/非裔美籍女性子宮肌瘤患者中顯著改善大量經血，療效持續 52 週 |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT | PLoS One | WHICH 試驗：NET-EN 與 DMPA-IM 注射避孕藥對雌二醇水平、月經型態及 HIV 風險相關指標的比較 |
| [6786825](https://pubmed.ncbi.nlm.nih.gov/6786825/) | 1981 | 臨床試驗（Phase I） | Contraception | Norethisterone enanthate 與 acetate 之 Phase I 試驗，觀察到治療後閉經、點狀出血等月經異常發生率 |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Review | Obstet Gynecol | 口服 GnRH 拮抗劑（合併賀爾蒙 add-back）治療子宮肌瘤的療效與安全性綜述 |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | 複方注射避孕藥（含 norethisterone 類成分）之避孕效果與可接受性系統性回顧 |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | 同上主題較早版本之系統性回顧 |
| [12335903](https://pubmed.ncbi.nlm.nih.gov/12335903/) | 1979 | Review | Contraception, fertilité, sexualité | 子宮內膜異位症與不孕症相關黃體素治療綜述 |
| [2660092](https://pubmed.ncbi.nlm.nih.gov/2660092/) | 1989 | Review | Pediatr Clin North Am | 賀爾蒙避孕原理綜述，涵蓋青少年應用情境 |
| [12317413](https://pubmed.ncbi.nlm.nih.gov/12317413/) | 1987 | Review | Current Therapeutics | 口服避孕藥綜述 |
| [3659794](https://pubmed.ncbi.nlm.nih.gov/3659794/) | 1987 | Review | La Revue du praticien | 黃體素類避孕法綜述（法文文獻） |

---

## 香港上市資訊

目前 norethisterone 在香港**未上市**，查無許可證登記（0 張）。無法提供品名、劑型與核准適應症資訊。

---

## 安全性考量

目前查無主要警語、禁忌症資料，DDI 查詢亦無結果（query_status: not_found）。此為 Blocking 等級資料缺口（DG001），需取得官方仿單資料後才能進行安全性初評（S1 階段）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 3 個已完成的 Phase 3 RCT（LIBERTY 1/2/EXTENSION）支持 norethisterone 作為 add-back 成分達成閉經療效指標，證據等級達 L2。
- 但證據多為合併療法脈絡（與 relugolix、estradiol 共同給藥），非 norethisterone 單方治療閉經的直接證據，且安全性資料（DG001，Blocking）與 MOA 資料（DG002，High）皆缺失，須補齊後才能推進至安全性初評。

**若要推進需要：**
- 取得 TFDA／香港衛生署官方仿單，解析警語與禁忌症（解決 DG001，Blocking）
- 透過 DrugBank API 補齊完整作用機轉資料（解決 DG002）
- 釐清 norethisterone 單方 vs. 合併療法（relugolix/estradiol add-back）在閉經適應症上的證據差異，評估是否需要額外單方試驗
- 確認香港上市現況（0 張許可證）之原因，評估是否需申請新藥證或以既有複方途徑切入
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

