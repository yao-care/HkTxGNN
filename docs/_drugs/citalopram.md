---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 5
---

# Citalopram
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

# Citalopram：從憂鬱症到強迫症

## 一句話總結

Citalopram 是選擇性血清素再吸收抑制劑（SSRI），香港已有多張許可證，但許可證資料未載明原適應症，一般用於憂鬱症。
TxGNN 模型預測它可能對**強迫症 (Obsessive-Compulsive Disorder, OCD)** 有效。
目前有 **28 個臨床試驗**和 **15 篇文獻**支持這個方向，但多數試驗測試的是其 S-鏡像異構物 escitalopram，citalopram 本身的 OCD 證據僅限於早期開放性研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（依藥理類別為 SSRI 抗憂鬱劑） |
| 預測新適應症 | 強迫症 (Obsessive-Compulsive Disorder) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L3（Evidence Pack 初判為 L2，但未找到以 citalopram 本身在 OCD 進行的已完成 Phase 2/3 RCT，故依規則降為 L3） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，citalopram 屬於 SSRI 類別，抑制血清素再吸收是這類藥物的共同作用。

OCD 對血清素再吸收抑制劑有反應，這是該疾病藥物治療的核心依據（PMID 12607204、10471169）。因此 citalopram 用於 OCD 在機轉上合理，也與 TxGNN 的高分預測一致。

有兩個限制需要注意：
- 多數已登記的 OCD 試驗測試的是 escitalopram，不是 citalopram，只能算旁證。
- OCD 常需要比憂鬱症更高的劑量（PMID 38703743），但 citalopram 有劑量相關的 QT 間期延長風險，劑量上限因此受限。

## 臨床試驗證據

以下列出最相關的 10 個試驗（全部 28 個中挑選）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | 完成 | 30 | Escitalopram 直接用於 OCD，評估療效與最適劑量（非 citalopram） |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | 完成 | 14 | Escitalopram 用於 OCD 的小型先導研究，支持力道弱 |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | 完成 | 100 | 高劑量 escitalopram（最高 50 mg/日）用於成人 OCD，開放標示、無對照，不算 RCT |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | 完成 | 176 | 雙盲隨機比較常規劑量（20 mg）與高劑量（40 mg）escitalopram 用於 OCD |
| [NCT00708240](https://clinicaltrials.gov/study/NCT00708240) | Phase 4 | 未知 | 40 | Escitalopram 用於青少年 OCD，並探討執行功能與腦區活化 |
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | 完成 | 149 | Citalopram 對比安慰劑，用於自閉症兒童的重複行為；疾病不同，僅供安全性與耐受性參考 |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | 完成 | 12 | 以功能性磁振造影研究 citalopram 對自閉症重複行為的影響，屬機轉性研究 |
| [NCT00115011](https://clinicaltrials.gov/study/NCT00115011) | Phase 4 | 完成 | 30 | Escitalopram 用於自傷性摳皮，屬 OCD 譜系疾病但非 OCD |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | 完成 | 158 | 團體認知行為治療 vs. fluoxetine 用於 OCD，提供 SSRI 類別背景 |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | 完成 | 124 | 認知行為治療合併血清素再吸收抑制劑，用於 SRI 部分反應的兒童 OCD |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | 系統性回顧/統合分析 | Comprehensive Psychiatry | 探討 OCD 使用仿單外高劑量血清素再吸收抑制劑的長期安全性與耐受性 |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | 統合分析 | Journal of Psychiatric Research | 網絡統合分析，比較藥物、心理治療及兩者合併對兒童青少年 OCD 的療效 |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | 統合回顧 | Frontiers in Psychiatry | 評估抗憂鬱劑在兒童青少年（含 OCD）急性治療的療效、耐受性與自殺風險 |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | 統合分析 | Journal of Affective Disorders | OCD 對安慰劑與抗憂鬱劑的反應皆低於其他焦慮症 |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | 開放性隨機試驗 | European Psychiatry | 16 位難治型 OCD 患者，比較 citalopram 單用與合併 clomipramine |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | 開放性研究 | Psychiatry and Clinical Neurosciences | 15 位兒童青少年 OCD 接受 citalopram 8 週治療的初步報告 |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | 回顧/評論 | International Clinical Psychopharmacology | 回顧 citalopram 用於 OCD 的證據及 OCD 的血清素神經生物學 |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | 回顧 | BMJ Clinical Evidence | OCD 的流行病學與治療證據回顧 |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | 回顧 | World Journal of Biological Psychiatry | 說明 OCD 對血清素類藥物有反應，及其神經解剖基礎 |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | 研究 | CNS Spectrums | 探討 BDNF Val66Met 基因多型對 escitalopram 或 paroxetine 治療 OCD 反應的影響 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62273 | LOPRAXER TABLETS 40MG | 未載明 | 未載明 |
| HK-53122 | PMS-CITALOPRAM TAB 20MG | 未載明 | 未載明 |
| HK-61066 | AUROPRAM 20 TAB 20MG | 未載明 | 未載明 |
| HK-53084 | APO-CITALOPRAM TAB 20MG | 未載明 | 未載明 |
| HK-52953 | EUROPRAM TAB 20MG | 未載明 | 未載明 |

以上為 10 張許可證中的 5 張。

## 安全性考量

- **主要警語**：Citalopram 有劑量相關的 QT 間期延長警語。每日最高劑量為 40 mg，老年人及 CYP2C19 弱代謝者最高為 20 mg。這會限制 OCD 所需的高劑量策略。
- 香港衛生署仿單的警語、禁忌症及藥物交互作用資料尚未取得，需另行補充。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- OCD 對 SSRI 有反應，機轉合理，TxGNN 分數也很高（99.74%），且有多個 escitalopram 的 OCD 試驗與統合分析可作類別佐證。
- Citalopram 本身的 OCD 證據只有早期小型開放性研究，且高劑量受 QT 風險限制，因此需要設置安全防護。

**若要推進需要：**
- 取得 citalopram 在 OCD 的直接證據，例如以 citalopram 本身進行的隨機對照試驗。
- 取得香港衛生署仿單的警語與禁忌症，並補充作用機轉與藥物交互作用資料。
- 訂定 QT 風險管控計畫，包括劑量上限、心電圖監測，以及老年人與 CYP2C19 弱代謝者的減量原則。

**其他預測適應症：** 分裂型、妄想型、孤僻型及做作型人格障礙的預測，分數皆為 99.68%，幾乎相同，疑為知識圖譜傳播造成。這四項幾乎沒有直接證據，建議皆為 **Hold**。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

