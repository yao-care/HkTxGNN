---
layout: default
title: Desvenlafaxine
parent: 中證據等級 (L3-L4)
nav_order: 192
evidence_level: L4
indication_count: 10
---

# Desvenlafaxine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Desvenlafaxine：從重鬱症到強迫症

## 一句話總結

Desvenlafaxine 是 Venlafaxine 的活性代謝物，屬血清素-正腎上腺素再回收抑制劑（SNRI），原為重鬱症（Major Depressive Disorder）的治療藥物。
TxGNN 模型預測它可能對**強迫症（Obsessive-Compulsive Disorder, OCD）** 有效，
目前有 **2 個相關臨床試驗**和 **4 篇文獻**可供參考，惟多屬間接或類別效應依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 重鬱症（Major Depressive Disorder） |
| 預測新適應症 | 強迫症（Obsessive-Compulsive Disorder） |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏 Desvenlafaxine 的詳細作用機轉登錄資料。根據其藥物類別（SNRI）及現有文獻，Desvenlafaxine 透過**同時抑制血清素轉運體（SERT）與正腎上腺素轉運體（NET）**，提升突觸間隙中 5-HT 和 NE 的濃度，發揮抗憂鬱效果。其作用與母藥 Venlafaxine 在機制上高度一致。

OCD 的核心病理機制涉及眶額皮質－紋狀體迴路（orbitofrontal-striatal circuit）的過度活化，與血清素（5-HT）系統功能異常密切相關。SSRI 是目前 OCD 的一線藥物，而 SNRI 透過 SERT 抑制同樣作用於 5-HT 系統，機轉上具備治療 OCD 的合理基礎。

最關鍵的間接證據來自母藥研究：Venlafaxine 已有直接針對 OCD 的隨機雙盲對照試驗（PMID 14624187），顯示其療效可與 SSRI 相當（n=150）。Desvenlafaxine 作為活性代謝物可繼承此機轉效應，但目前**完全缺乏直接以 Desvenlafaxine 治療 OCD 的臨床試驗**，為本預測的主要侷限。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | 已完成 | 426 | 評估 Troriluzole（麩胺酸調節劑）輔助治療 OCD，入選條件為對 SSRI、Clomipramine、Venlafaxine 或 **Desvenlafaxine** 反應不佳者；Desvenlafaxine 為背景用藥，非試驗主角，屬間接相關 |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | 已完成 | 25 | **Desvenlafaxine** 用於產後憂鬱症（PPD）的功能恢復評估；適應症為 PPD 而非 OCD，僅提供 Desvenlafaxine 在情感疾患的安全性參考 |

> ⚠️ 注意：以上 2 個試驗均非直接驗證 Desvenlafaxine 用於 OCD，證據等級有限。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | Journal of Clinical Psychopharmacology | **母藥 Venlafaxine 對比 Paroxetine 治療 OCD（n=150）**，兩者療效相當，為 SNRI 機轉用於 OCD 的核心類別效應依據 |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Narrative Review | Expert Opinion on Pharmacotherapy | 回顧雙盲試驗數據，確認 5-HT 系統在 OCD 病理中的關鍵角色，支持含 SERT 抑制機轉之藥物的理論基礎 |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Clinical Report | Psychiatry and Clinical Psychopharmacology | Risperidone 增強抗憂鬱藥治療頑固性 OCD 之臨床報告，顯示抗憂鬱藥單藥治療 OCD 的侷限及增強策略 |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | 產後憂鬱症綜合回顧，提及 PPD 患者後期可能發展為 OCD，提供情感疾患與 OCD 共病的病理連結背景 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Research Question（研究問題階段）**

**理由：**
雖然 SNRI 機轉在理論上對 OCD 具合理性，且母藥 Venlafaxine 有直接 RCT 支持（PMID 14624187），但目前完全缺乏 Desvenlafaxine 本身用於 OCD 的臨床試驗資料，TxGNN 預測尚停留於知識圖譜推斷層次（L4），無法進入安全性初評（S1）。

**若要推進需要：**
- 補充完整作用機轉（MOA）資料（建議查詢 DrugBank API，DB06700）
- 取得仿單安全性警語與禁忌症資料（TFDA 官網下載仿單 PDF 解析）
- 系統性文獻搜尋：擴大至 Desvenlafaxine + anxiety spectrum disorders
- 評估是否設計以 Desvenlafaxine 為主藥的 OCD PoC（概念驗證）小型試驗
- 釐清與現有一線 OCD 藥物（Fluvoxamine、Fluoxetine、Clomipramine）的定位差異

---

> **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用於實際治療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

