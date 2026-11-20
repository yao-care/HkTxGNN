---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "infectious bovine rhinotracheitis", "malignant catarrh"]
description: "Enfortumab Vedotin：預測新適應症為痲瘋病 (leprosy)（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Enfortumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Enfortumab Vedotin: 痲瘋病 (leprosy)
{: .text-alpha }

## 一句話總結

Enfortumab vedotin 是一款以 Nectin-4 為標的、搭載 MMAE 細胞毒性藥物的抗體藥物複合體（ADC），香港已核准上市，但本報告所編整的資料中未載明其核准適應症。
TxGNN 模型預測排名第一的新適應症為**痲瘋病 (Leprosy)**，但目前**沒有任何臨床試驗或文獻**支持，屬於純計算預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 痲瘋病 (leprosy) |
| TxGNN 預測分數 | 0.9953 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Enfortumab Vedotin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Enfortumab vedotin-ejfv 為一種 ADC。其抗體為針對 Nectin-4 的人類 IgG1 kappa 抗體，Nectin-4 為一種位於細胞表面的黏附蛋白。小分子 MMAE 為一種微管破壞劑，經由可被蛋白酶切割的連接子與抗體相連。」英文原文："Enfortumab vedotin-ejfv is an ADC. The antibody is a human IgG1 kappa directed against Nectin-4, an adhesion protein located on the surface of cells. The small molecule, MMAE, is a microtubule-disrupting agent, attached to the antibody via a protease-cleavable linker."（[DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed)，版本日期 2026-08-04；查閱日期 2026-11-19）。根據已知資訊，Enfortumab vedotin 是 Nectin-4 導向的抗體藥物複合體，透過抗體將 MMAE 細胞毒性藥物送入表現 Nectin-4 的腫瘤細胞。

**痲瘋病的預測缺乏合理的機轉連結。** 痲瘋病由麻風分枝桿菌 (Mycobacterium leprae) 感染引起，Nectin-4 標的治療與此感染之間沒有已知關聯。高分數僅是計算模型的輸出，沒有試驗或文獻佐證，不宜視為有效訊號。

其他排名前列的預測（多發性內分泌腫瘤、巨細胞病毒感染、念珠菌症、腦梗塞、HIV、同型接合子家族性高膽固醇血症等）同樣缺乏機轉依據。巨細胞病毒感染與念珠菌症各有一篇文獻，但內容分別是食道炎病例報告與藥物不良反應通報分析，反映的是安全性訊號，並非療效證據。

---

## 臨床試驗證據

針對排名第一的痲瘋病：目前無相關臨床試驗登記。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | 進行中（不再招募） | 329 | EV-202 試驗：開放標示、多組別，評估 Enfortumab vedotin 用於局部晚期或轉移性實體腫瘤的客觀緩解率；非專為 HER2 陽性乳癌設計，未提供結果數據 |

---

## 文獻證據

針對排名第一的痲瘋病：目前無相關文獻。

作為參考，其他預測適應症的文獻如下：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | Histopathology | 膀胱癌分子病理學回顧（HER2 陽性乳癌預測項下） |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Review | ASCO Educational Book | ADC 的新標的與藥物載荷的發展回顧 |
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Review | Crit Rev Oncol Hematol | 近五年核准的 10 種腫瘤藥物之真實世界證據整合 |
| [42480966](https://pubmed.ncbi.nlm.nih.gov/42480966/) | 2026 | Review | Cancer Letters | ADC 對抗多重抗藥性癌症的生物標記、載荷與旁觀者效應 |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | 前臨床 | Cancer Letters | 多倍體巨型癌細胞介導對 HER2 標的 ADC 的抗藥性 |
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Case report | Reports (MDPI) | EV 併用 pembrolizumab 後發生嚴重潰瘍性食道炎（巨細胞病毒感染預測項下，屬不良反應） |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | 藥物警訊分析 | Clinical Epidemiology | 膀胱癌 ADC 的 FAERS 真實世界風險訊號（念珠菌症預測項下，屬安全性訊號） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67888 | PADCEV 凍乾濃縮輸注液 20mg | 未載明 | 未載明 |
| HK-67889 | PADCEV 凍乾濃縮輸注液 30mg | 未載明 | 未載明 |

兩張許可證均為單方、有效，持有人為 Astellas Pharma Hong Kong Company Limited。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體（ADC），以 MMAE（微管蛋白抑制劑）為細胞毒性載荷 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單（一般需監測血液學參數、肝腎功能與血糖） |
| 處置防護 | 屬細胞毒性藥物，應依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下為部分範例：
  - **嚴重 (Major)**：Clarithromycin
  - **中等 (Moderate)**：多為降血糖藥物，包括 Metformin、Pioglitazone、Acarbose、Glimepiride、Glipizide、Glyburide、Empagliflozin、Dapagliflozin、Canagliflozin、Exenatide、Dulaglutide、Linagliptin、Saxagliptin 等；另有 Aprepitant

其餘主要警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的痲瘋病預測分數雖高（0.9953），但沒有任何臨床試驗或文獻，也缺乏機轉依據，屬證據等級 L5 的純計算預測。

**若要推進需要：**
- 取得香港衛生署許可證的核准適應症與仿單（警語、禁忌症），以釐清原適應症與安全性。
- 補充 DrugBank 的作用機轉資料。
- 痲瘋病、病毒及獸醫疾病等預測，除非有新的生物學證據，否則不建議投入資源。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

