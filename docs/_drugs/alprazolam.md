---
layout: default
title: Alprazolam
parent: 中證據等級 (L3-L4)
nav_order: 40
evidence_level: L3
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L3** | 預測適應症: **3** 個
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

# Alprazolam：從焦慮症到失眠

## 一句話總結

Alprazolam（阿普唑侖）是苯二氮平類（benzodiazepine）藥物，臨床上主要用於焦慮與恐慌相關疾病。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效。
目前有 **7 個相關臨床試驗登記**和 **18 篇文獻**，但多為觀察性研究或間接證據，沒有直接測試 alprazolam 治療失眠的隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未提供適應症文字（文獻顯示為焦慮、恐慌症等） |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據已知的藥理分類，alprazolam 是 GABA-A 受體的正向異位調節劑，具有鎮靜與安眠作用。因此在機轉上，它可能適用於失眠，也與 TxGNN 的高分預測一致。

實務上，苯二氮平類藥物常被用來處理焦慮合併睡眠困難。文獻中也有 alprazolam 與褪黑激素在血液透析患者睡眠障礙的比較研究，以及合併冠心病與失眠患者的觀察性研究。不過，這些都不是針對失眠的確證性試驗。

需要特別留意的是，多篇文獻指出苯二氮平類有依賴、耐受、跌倒和認知影響等風險，長者尤其明顯。這代表即使療效上可行，安全性審查也必須先於任何推薦。

**另一個值得注意的預測：agoraphobia（懼曠症）。** TxGNN 對此預測分數為 99.56%，證據等級為 L1，有多項 RCT（如 PMID 3282478、3282479、8101126）支持。但恐慌症合併懼曠症本來就是 alprazolam 公認的使用範圍，屬於既有用途，並非真正的老藥新用。資料中原適應症欄位為空，只是資料缺口。

---

## 臨床試驗證據

以下 7 個試驗均與失眠有間接關聯，沒有任何一個直接測試 alprazolam 治療失眠。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | 不適用 | 未知 | 1400 | 台灣長者安眠藥風險與效益的前瞻性世代研究，屬觀察性研究，並非針對 alprazolam |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | 不適用 | 完成 | 170 | 以電子化自我管理介入協助退伍軍人停用苯二氮平類，探討減藥而非失眠療效 |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | 完成 | 418 | Niravam 合併 SSRI/SNRI 用於廣泛性焦慮或恐慌症的開放性試驗，無失眠終點 |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | 已終止 | 2 | Gabapentin 治療苯二氮平依賴，僅入組 2 人，僅與依賴風險背景相關 |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | 未知 | 128 | 催眠療法與 alprazolam 術前用藥比較，針對手術前焦慮，並非失眠 |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | 完成 | 26 | Clarithromycin 治療嗜睡症，屬不同睡眠疾病與不同藥物，可能是關鍵字誤配 |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | 完成 | 220 | AVP-923 治療阿茲海默症躁動的安慰劑對照試驗，未見涉及 alprazolam 或失眠 |

---

## 文獻證據

文獻相關性尚待人工審閱。以下為資料中提供的部分文獻（共 18 篇，僅提供 10 篇）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | 探討 eszopiclone 對阿茲海默症合併睡眠障礙長者的睡眠品質與認知功能影響（非 alprazolam） |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | 統合分析 | Acta Pharmaceutica | 評估各類鎮靜藥用於長者的劑量、療效與不良反應，以找出安全的鎮靜藥與劑量 |
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | 比較研究 | Cureus | 比較 alprazolam 與褪黑激素用於血液透析患者的睡眠障礙，是最直接的臨床訊號 |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | 回溯性觀察研究 | Medicine | 116 位冠心病合併失眠患者，對照組用 alprazolam，實驗組加用督脈灸與耳針，觀察心功能與神經傳導物質 |
| [7484706](https://pubmed.ncbi.nlm.nih.gov/7484706/) | 1995 | 回顧 | American Family Physician | 恐慌症的臨床概述，與失眠無直接關聯 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | 回顧 | Expert Opin Drug Metab Toxicol | 抗焦慮藥物的藥物動力學回顧 |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | 世代研究 | JHEP Reports | 肝硬化患者停用 zolpidem 可減少跌倒與骨折，提示鎮靜安眠藥的風險 |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | 前臨床（小鼠） | Aging | 小鼠重複給予 alprazolam 造成粒線體功能異常，削弱海馬迴依賴的記憶鞏固 |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | 模型研究 | Value in Health Regional Issues | 以 10 年預測模型分析苯二氮平類的使用趨勢與經濟負擔，並指出長期使用的風險 |
| [39295670](https://pubmed.ncbi.nlm.nih.gov/39295670/) | 2024 | 個案報告 | Cureus | 順勢療法用於持續性失眠合併廣泛性焦慮症的個案，與 alprazolam 關聯有限 |

---

## 香港上市資訊

本藥在香港共有 14 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-17668 | XANAX TAB 0.5MG（Viatris Healthcare Hong Kong） | — | — |
| HK-56775 | VICK-ALPRAZOLAM TAB 0.5MG（Vickmans Laboratories） | — | — |
| HK-55270 | ZOLARAM 1.0 TAB 1MG（Trenton-Boma） | — | — |
| HK-17669 | XANAX TAB 0.25MG（Viatris Healthcare Hong Kong） | — | — |
| HK-51649 | ALPRAX 2 TAB 2MG（Aspen Pharmacare Asia） | — | — |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 失眠適應症目前只有間接證據（證據等級 L3，屬於「研究問題」階段），沒有直接測試 alprazolam 治療失眠的 RCT，最接近的只是與褪黑激素的小型比較研究。
- 香港仿單的警語與禁忌症資料尚未取得，無法進行安全性初篩；而苯二氮平類的依賴、耐受、跌倒和認知風險在失眠族群（尤其長者）更受關注。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與藥物交互作用
- 取得 DrugBank 的作用機轉（MOA）資料
- 完成剩餘文獻的人工相關性審閱，確認 alprazolam 用於失眠的直接證據
- 與現行失眠治療（如認知行為治療、其他安眠藥）比較療效與風險
- 若持續評估，需訂定短期使用、停藥與長者用藥的風險控管計畫

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

