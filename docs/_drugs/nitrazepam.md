---
layout: default
title: Nitrazepam
parent: 中證據等級 (L3-L4)
nav_order: 527
evidence_level: L3
indication_count: 3
---

# Nitrazepam
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

# Nitrazepam：從已知安眠用途到失眠（入睡與睡眠維持困難）適應症驗證

## 一句話總結

Nitrazepam 為苯二氮平類（benzodiazepine）藥物，本次評估未取得其正式核准適應症紀錄。
TxGNN 模型預測其對**失眠（入睡與睡眠維持困難，Sleep Disorder, Initiating and Maintaining Sleep）**有效，
預測分數高達 **99.89%**，並有 **20 篇文獻**佐證——但這些文獻顯示 Nitrazepam 早自 1960、70 年代即已作為臨床安眠藥使用，
故此預測性質上較接近**驗證既有已知用途**，而非全新的老藥新用發現。目前無註冊臨床試驗，香港也尚未上市。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症紀錄（資料缺口）；依文獻已知為苯二氮平類鎮靜安眠藥 |
| 預測新適應症 | 失眠（入睡與睡眠維持困難，Sleep Disorder, Initiating and Maintaining Sleep） |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

正式的作用機轉（MOA）資料目前為缺口（DG002），但依本 Evidence Pack 中對同藥物其他候選適應症的機轉分析可知，Nitrazepam 屬於苯二氮平類藥物，透過增強 GABA-A 受體活性產生中樞神經抑制作用，是其鎮靜安眠效果的藥理基礎。

值得注意的是，文獻證據（如 1969 年 *Nitrazepam--a safe hypnotic*、1983 年與 Triazolam 的雙盲交叉比較試驗）顯示 Nitrazepam 長期以來就是臨床上用於治療失眠的標準安眠藥之一，並非新發現的適應症方向。TxGNN 的高分預測（99.89%）與大量既有文獻相互印證，說明模型正確捕捉到藥物已知的藥理定位，但也代表這條候選路徑的「新穎性」有限。

GABA-A 受體增強作用直接對應失眠的病理生理機轉（中樞過度覺醒、入睡困難、睡眠維持障礙），機轉上與預測適應症高度吻合。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | 安全性報告 | British Medical Journal | 27 名患者急性過量使用 Nitrazepam（最多 80 錠）僅出現嗜睡，未見嚴重不良反應；雙盲試驗顯示其安眠效果與 butobarbitone 相當 |
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | 比較試驗 | Acta Psychiatrica Scandinavica | 老年住院病患雙盲交叉試驗，Triazolam 與 Nitrazepam 對睡眠品質及精神運動表現效果相近 |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | 藥物動力學研究 | Clinical Pharmacokinetics | Nitrazepam 臨床藥物動力學特性回顧 |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | 安全性報告 | The British Journal of Psychiatry | 報告 Nitrazepam（Mogadon）依賴性案例 |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | 文獻回顧 | Drugs | Zolpidem 療效回顧，指出其安眠效果與 Nitrazepam 等苯二氮平類藥物相當 |
| [3281819](https://pubmed.ncbi.nlm.nih.gov/3281819/) | 1988 | 文獻回顧 | Drugs | Brotizolam 藥理及療效回顧，臨床試驗顯示其效果與 Nitrazepam 相近 |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | 文獻回顧 | CNS Drugs | 安眠藥殘留效應（隔日嗜睡、精神運動功能受損）之流行病學與臨床意義回顧 |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | 文獻回顧 | BMJ Clinical Evidence | 高齡族群失眠盛行率與危險因子回顧 |
| [10612270](https://pubmed.ncbi.nlm.nih.gov/10612270/) | 1999 | 文獻回顧 | Drug Safety | Zopiclone 15 年臨床經驗回顧，與多種短、中、長效安眠藥（含 Nitrazepam）比較風險效益 |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | 觀察性研究 | PLoS ONE | 基層醫療院所苯二氮平類藥物不當處方型態與相關因子分析 |

## 安全性考量

本地（香港）缺乏 TFDA／衛生署仿單警語與禁忌症資料，此為**阻斷級資料缺口（DG001）**，在取得前無法完成 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖有 20 篇文獻支持其藥理合理性，但這些證據多為佐證 Nitrazepam 既有已知的安眠用途，而非針對「老藥新用」的新證據；且無任何註冊臨床試驗直接驗證此適應症方向。
- 香港未上市（0 張許可證），且仿單安全性資料缺失屬阻斷級缺口，無法進入下一階段安全性初評。

**若要推進需要：**
- 取得正式仿單／藥品說明書（TFDA 或香港衛生署來源），解除 DG001 阻斷缺口
- 補齊 DrugBank 正式作用機轉紀錄（DG002）
- 釐清此候選是否具有實質新穎性，或應歸類為既有適應症確認而非老藥新用機會

**其他預測適應症（已評估，不建議推進）：**
- **Acute encephalopathy with biphasic seizures and late reduced diffusion**（L5・Hold）：機轉關聯僅為苯二氮平類藥理推論，無文獻或試驗支持。
- **Wernicke-Korsakoff syndrome**（L5・Hold）：本質為硫胺素缺乏症，與 GABA-A 調節無直接病理關聯，機轉關聯薄弱。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

