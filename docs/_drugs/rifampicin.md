---
layout: default
title: Rifampicin
parent: 中證據等級 (L3-L4)
nav_order: 647
evidence_level: L3
indication_count: 5
---

# Rifampicin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

Using the pharmacist-report skill implicit in this task: producing the Traditional Chinese repurposing evaluation report per v5 spec below, based strictly on the supplied Evidence Pack.

# Rifampicin：從結核病 (TB) 到結膜炎 (Conjunctivitis)

## 一句話總結

Rifampicin 是廣譜抗生素，文獻證據顯示其核心用途為結核病 (TB) 治療（正式仿單資料尚未取得）。
TxGNN 模型預測它可能對**結膜炎 (Conjunctivitis)** 有效，
目前**無註冊臨床試驗**，但有 **20 篇文獻**支持這個方向，其中包含 1975 年一項針對沙眼（trachoma）的人體對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尚無正式仿單登記資料（DG001）；文獻佐證顯示主要用於結核病 (TB) 合併治療 |
| 預測新適應症 | 結膜炎 (Conjunctivitis) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 的正式 MOA 欄位標記為資料缺口（DG002），但本證據包彙整的文獻明確指出，rifampicin 的作用機轉是抑制細菌 RNA 聚合酶，阻斷 mRNA 合成，因而具有廣譜殺菌活性，涵蓋分枝桿菌（結核桿菌）與披衣菌屬（*Chlamydia trachomatis*）等病原體。

結膜炎（尤其是沙眼／包涵體結膜炎）常由 *Chlamydia trachomatis* 引起，而多篇文獻（PMID 6635446、PMID 5411121）指出，rifampicin 按重量計算是對抗 *C. trachomatis* 活性最強的抗生素之一，機轉上與其抗結核作用同源。1970 年代已有局部眼用 rifampicin 藥膏治療沙眼的人體對照試驗（PMID 1096630），顯示這並非純粹的知識圖譜雜訊。

值得特別提醒的是，本證據包同批預測中的「多發性內分泌腫瘤 (MEN)」與「HIV 感染」兩項，已被明確標註為知識圖譜的間接雜訊訊號（機轉上無合理生物學路徑，詳見文末附註），不應與本項「結膜炎」預測混淆。相較之下，結膜炎預測有實際的體外實驗與歷史臨床證據支持，屬於證據基礎相對紮實的老藥新用方向，但仍以早期、小規模研究為主，缺乏現代註冊臨床試驗驗證。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | 對照試驗 | Am J Ophthalmol | 突尼西亞學童沙眼對照試驗：1% 四環素藥膏 vs. 1% rifampicin 藥膏 vs. 5% 硼酸藥膏，為早期人體對照研究 |
| [6635446](https://pubmed.ncbi.nlm.nih.gov/6635446/) | 1983 | Review | Rev Infect Dis | Rifampin 按重量計算是對 *C. trachomatis* 活性最強的抗生素，局部治療沙眼療效與四環素相當 |
| [5411121](https://pubmed.ncbi.nlm.nih.gov/5411121/) | 1970 | 體外實驗 | Nature | Rifampicin 及其衍生物具抗沙眼病原體（*C. trachomatis*）之體外活性證據 |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | 臨床報告 | Ann Ophthalmol | 早期眼科臨床使用 rifampicin 之報告（摘要未提供） |
| [15228931](https://pubmed.ncbi.nlm.nih.gov/15228931/) | 2004 | Review | An Pediatr | 細菌性結膜炎常見病原菌與抗生素敏感性回顧，支持經驗性抗生素治療策略 |
| [19941479](https://pubmed.ncbi.nlm.nih.gov/19941479/) | 2010 | Review | Curr Med Chem | 探討沙眼等被忽視細菌感染疾病，提及 rifampin 於相關治療方案中的角色 |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | 觀察性研究 | Adv Biomed Res | 伊朗中部結膜炎患者之細菌病原體與抗生素敏感性分析 |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | 觀察性研究 | J Ophthalmic Inflamm Infect | 奈及利亞拉哥斯結膜炎病原菌分布與質體分析 |
| [2483893](https://pubmed.ncbi.nlm.nih.gov/2483893/) | 1989 | Review | Ann Ig | 回顧 *Chlamydia trachomatis* 致病機轉，涵蓋沙眼與包涵體結膜炎 |
| [21191558](https://pubmed.ncbi.nlm.nih.gov/21191558/) | 2010 | 觀察性研究 | Rev Esp Quimioter | *Corynebacterium macginleyi* 引起結膜炎菌株之抗生素敏感性分析 |

## 香港上市資訊

目前查無香港上市許可證資料（市場狀態：未上市，總許可證數：0）。

## 安全性考量

安全性資訊請參考原廠仿單。目前 TFDA/香港官方仿單資料尚未取得（DG001，Blocking 等級），DDI 查詢亦無結果，故本階段**無法完成安全性初評 (S1)**。

## 結論與下一步

**決策：Hold**

**理由：**
- 藥物目前未在香港上市，缺乏當地正式仿單與警語資料（DG001 為 Blocking 等級缺口），無法完成安全性初評。
- 結膜炎適應症證據等級為 L3，主要來自 1970-80 年代的體外實驗與小規模對照試驗，缺乏現代註冊臨床試驗（ClinicalTrials.gov 上無相關登記）驗證其在當代治療角色。

**若要推進需要：**
- 取得官方仿單以完成 DG001 安全性初評
- 補齊 DrugBank 正式 MOA 資料（DG002）
- 檢索近 10 年眼科臨床證據，確認 rifampicin 是否已被新一代抗生素取代
- 若考慮開發，需評估眼用局部劑型（現有證據多為藥膏劑型，而非現行口服劑型）之可行性

---

### 附註：其他預測候選（本報告未採納）

本證據包同批尚有 3 項預測適應症，因證據品質或機轉合理性問題，未列入本報告主體，特此說明以避免誤用：

| 適應症 | TxGNN 分數 | 狀態 | 說明 |
|--------|-----------|------|------|
| 多發性內分泌腫瘤 (MEN) | 99.86% | Hold | 證據包明確標註為知識圖譜雜訊訊號，MEN 為 RET/MEN1 基因突變疾病，與 rifampicin 之 RNA 聚合酶抑制機轉無已知關聯 |
| 痤瘡 (acne，實際多指 hidradenitis suppurativa/acne inversa) | 99.74% | 未評分 | 文獻顯示 rifampicin + clindamycin 併用已是歐洲/北美指引中治療化膿性汗腺炎的**既有標準療法**，並非全新適應症；但 TxGNN 節點標記為「acne (disease)」易與尋常痤瘡混淆，需注意疾病定義差異 |
| HIV 感染 | 99.59% | Hold | ⚠️ 證據包明確警告此為假性訊號。所有相關試驗與文獻均為「rifampicin 治療結核病時與抗反轉錄病毒藥物之藥物交互作用（CYP3A4/UGT1A1 誘導）研究」，rifampicin 並無抗 HIV 病毒活性，誤讀恐導致嚴重臨床誤導 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

