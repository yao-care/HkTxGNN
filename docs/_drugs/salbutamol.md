---
layout: default
title: Salbutamol
parent: 高證據等級 (L1-L2)
nav_order: 672
evidence_level: L2
indication_count: 5
---

# Salbutamol
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

# Salbutamol：從氣喘/COPD 支氣管痙攣到支氣管炎（Bronchitis）

## 一句話總結

Salbutamol 為選擇性 β2-腎上腺素受體促效劑，臨床上已廣泛用於氣喘與慢性阻塞性肺病（COPD）等可逆性支氣管痙攣的緩解治療。TxGNN 模型針對本藥產出 **5 項**預測適應症，其中僅**支氣管炎 (Bronchitis)** 具備扎實證據——有多個已完成的隨機對照試驗及 **Cochrane 系統性回顧**支持；其餘 4 項候選（結膜乳頭增生、鼻腔疾病、咽炎、急性喉咽炎）證據薄弱，機轉上多屬 TxGNN 知識圖譜的間接連結，非真實藥理標靶關係。

---

## 快速總覽（以證據最強候選——支氣管炎為主）

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料集無正式許可證記錄；依機轉描述屬氣喘/COPD 相關可逆性支氣管痙攣 |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

### 候選適應症總覽（5 項比較）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗數 | 文獻數 | Pipeline 建議 |
|---|---|---|---|---|---|---|
| 1 | 結膜乳頭增生 (Papillary Conjunctivitis) | 99.996% | L5 | 0 | 0 | Hold |
| 2 | 鼻腔疾病 (Nasal Cavity Disease) | 99.994% | L4 | 2 | 2 | Hold |
| 3 | 咽炎 (Pharyngitis) | 99.994% | L4 | 10 | 10 | Hold |
| 4 | **支氣管炎 (Bronchitis)** | 99.992% | **L2** | **50** | **20** | **Research Question** |
| 5 | 急性喉咽炎 (Acute Laryngopharyngitis) | 99.991% | L5 | 0 | 0 | Hold |

支氣管炎是唯一有大量直接臨床證據支持的候選，以下章節聚焦於此。

---

## 為什麼這個預測合理？

Salbutamol 為選擇性 β2-腎上腺素受體促效劑，主要作用於呼吸道與支氣管平滑肌，透過活化 cAMP 路徑鬆弛平滑肌、緩解支氣管痙攣（此描述來自證據包各候選適應症之機轉註記；DrugBank 正式 MOA 欄位目前為高優先級資料缺口，需另行查證）。

氣喘/COPD 相關可逆性支氣管痙攣與支氣管炎——尤其是嬰幼兒喘鳴性/毛細支氣管炎——在病理生理上高度重疊，臨床上 salbutamol 早已廣泛用於此類族群的支氣管擴張治療，因此是五項候選中唯一具備直接、大量臨床使用證據支持的適應症。惟多個 Cochrane 系統性回顧顯示其在嬰幼兒毛細支氣管炎的療效證據不一致，國際指引未將其列為常規建議治療，須視個別喘鳴表型判斷。

相對地，其餘四項候選（結膜乳頭增生、鼻腔疾病、咽炎、急性喉咽炎）在機轉上缺乏 β2 受體促效作用的直接關聯——證據包本身即標註這些連結多源於 TxGNN 知識圖譜中「過敏/發炎」節點的間接路徑，而非真實藥理標靶關係，故證據等級僅 L4-L5，建議維持 Hold。

---

## 臨床試驗證據（支氣管炎，精選 10 項）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02233985](https://clinicaltrials.gov/study/NCT02233985) | Phase 4 | 完成 | 64 | 霧化 3% 高滲食鹽水併用 salbutamol 治療中重度毛細支氣管炎之療效評估 |
| [NCT00667797](https://clinicaltrials.gov/study/NCT00667797) | Phase 4 | 完成 | 486 | Levalbuterol vs racemic albuterol 於住院霧化治療之藥物經濟學比較 |
| [NCT01238445](https://clinicaltrials.gov/study/NCT01238445) | N/A | 完成 | 29 | 評估 albuterol 對毛細支氣管炎患者的支氣管擴張反應性 |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Phase 4 | 完成 | 17 | 評估 albuterol 及 tiotropium 於幹細胞移植後阻塞性細支氣管炎之急性支氣管擴張反應性 |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | 未知 | 600 | Epinephrine vs albuterol 治療毛細支氣管炎之隨機對照試驗 |
| [NCT02760719](https://clinicaltrials.gov/study/NCT02760719) | Phase 2 | 終止 | 100 | 霧化 3% 高滲食鹽水併用 salbutamol 治療住院兒童急性毛細支氣管炎 |
| [NCT00696540](https://clinicaltrials.gov/study/NCT00696540) | Phase 2 | 未知 | 74 | 以高滲食鹽水或生理食鹽水稀釋 salbutamol 治療毛細支氣管炎之安全性/療效比較 |
| [NCT03199976](https://clinicaltrials.gov/study/NCT03199976) | Phase 4 | 終止 | 80 | 間歇性 tiotropium 併用 salbutamol vs 單用 salbutamol 治療幼兒反覆喘鳴 |
| [NCT01065272](https://clinicaltrials.gov/study/NCT01065272) | Phase 1 | 完成 | 200 | 口服 dexamethasone 併用霧化 salbutamol 治療病毒性毛細支氣管炎 |
| [NCT01302587](https://clinicaltrials.gov/study/NCT01302587) | N/A | 完成 | 306 | 評估內建劑量計數器之 albuterol HFA 定量吸入劑於氣喘/COPD 患者之效果 |

---

## 文獻證據（支氣管炎，精選 10 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33843971](https://pubmed.ncbi.nlm.nih.gov/33843971/) | 2021 | RCT | JAMA Pediatrics | 針對性去導入措施可減少毛細支氣管炎住院患者的非證據導向治療（含支氣管擴張劑）使用 |
| [35383741](https://pubmed.ncbi.nlm.nih.gov/35383741/) | 2022 | RCT | Mymensingh Med J | 霧化 3% 高滲食鹽水併用 salbutamol vs 一般食鹽水於急性毛細支氣管炎之療效比較 |
| [24937099](https://pubmed.ncbi.nlm.nih.gov/24937099/) | 2014 | Cochrane Review | Cochrane Database Syst Rev | 「Bronchodilators for bronchiolitis」— 支氣管擴張劑於毛細支氣管炎之系統性證據總結 |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Review | Cochrane Database Syst Rev | Epinephrine 於毛細支氣管炎顯示短期中度效益，支氣管擴張劑類藥物整體效果有限 |
| [26833493](https://pubmed.ncbi.nlm.nih.gov/26833493/) | 2016 | Systematic Review | Cochrane Database Syst Rev | 胸腔物理治療於急性毛細支氣管炎（0-24月）之證據回顧 |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | 毛細支氣管炎整體治療證據總覽，支持性治療為主流 |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clinical Evidence | 毛細支氣管炎治療證據回顧（早期版本） |
| [36765418](https://pubmed.ncbi.nlm.nih.gov/36765418/) | 2023 | Guideline | Italian J Pediatrics | 2022 義大利毛細支氣管炎管理指引更新 |
| [9531910](https://pubmed.ncbi.nlm.nih.gov/9531910/) | 1998 | Review | American Family Physician | 急性支氣管炎多為病毒感染，少數小型研究顯示 albuterol 可緩解部分症狀 |
| [1829865](https://pubmed.ncbi.nlm.nih.gov/1829865/) | 1991 | Comparative Study | Thorax | 過敏與年齡對 salbutamol/ipratropium 支氣管擴張反應之影響（氣喘與慢性支氣管炎族群） |

---

## 香港上市資訊

目前無香港許可證記錄（市場狀態：未上市，登記數 0 張）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 資料缺口提示：TFDA 仿單警語/禁忌資料缺失（Blocking），目前**無法進入安全性初評（S1）**；DrugBank 作用機轉（MOA）資料亦缺失（High）。兩者皆須補齊才能進行完整風險評估。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 五項候選中僅支氣管炎（L2、Research Question）具備實質臨床證據，但國際指引對嬰幼兒毛細支氣管炎並未常規建議使用支氣管擴張劑，臨床效益證據不一致；其餘 4 項候選證據等級僅 L4-L5，機轉關聯性存疑。
- 本藥於香港未上市（0 張許可證），且 TFDA 仿单警語/禁忌資料為 Blocking 等級缺口，安全性初評（S1）目前無法啟動，構成推進的硬性障礙。

**若要推進需要：**
- 補齊 TFDA/原廠仿單之警語、禁忌與 DDI 資料（DG001，Blocking）
- 補齊 DrugBank 正式作用機轉資料（DG002，High）
- 若考慮支氣管炎方向，需針對特定族群（如毛細支氣管炎兒童）重新評估现行指引與療效爭議
- 評估香港上市/引進之法規路徑，因目前 0 張許可證為基本前提缺口
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

