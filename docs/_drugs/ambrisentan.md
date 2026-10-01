---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Ambrisentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ambrisentan：從肺動脈高壓到肺動脈靜脈畸形

## 一句話總結

Ambrisentan 是內皮素受體拮抗劑，原本用於治療肺動脈高壓（PAH）。
TxGNN 模型預測它可能對**肺動脈靜脈畸形 (Pulmonary Arteriovenous Malformation)** 有效，
但目前只有 **0 個臨床試驗**和 **1 篇文獻**（個案報告，且未使用 ambrisentan 治療），證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺動脈高壓（依證據包內的機轉描述推斷，香港許可證資料未載明適應症） |
| 預測新適應症 | 肺動脈靜脈畸形 (Pulmonary Arteriovenous Malformation) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L5（僅有模型預測；唯一文獻為個案報告，未測試 ambrisentan。證據包自動評為 L4，此處依判定規則下修） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 機轉欄位為空）。
從證據包其他描述可知，Ambrisentan 是選擇性內皮素 A 型（ETA）受體拮抗劑，
其療效在 PAH 中已被證實。

這個預測的關聯性偏弱。唯一找到的文獻，是一例遺傳性出血性毛細血管擴張症（HHT）合併 PAH 的病例。
即使 ambrisentan 有益，也是作用在合併的 PAH 上（已核准的用途），而非動靜脈畸形本身。
0.994 的高分是知識圖譜的推論結果，不是臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case report | World J Clin Cases | 報告一例 HHT 合併 PAH 的病例並分析家族基因，目的是提高對此共病的認識，未涉及 ambrisentan 治療 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-63502 | VOLIBRIS TABLETS 5MG | GLAXOSMITHKLINE LIMITED |
| HK-63503 | VOLIBRIS TABLETS 10MG | GLAXOSMITHKLINE LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，唯一文獻是未使用 ambrisentan 的個案報告，也找不到明確的機轉連結，高分只反映圖譜預測。
- 同一份 Evidence Pack 中，「先天性心臟病相關 PAH」和「結締組織病相關 PAH」兩個預測都是 L2、建議 Proceed with Guardrails。它們屬於已核准 PAH 的亞型，比本預測更值得優先評估。

**若要推進需要：**
- 找到 ambrisentan 用於肺動脈靜脈畸形或 HHT 的直接臨床或機轉研究。
- 釐清可能的獲益是否只限於合併的 PAH。
- 補齊香港衛生署仿單的警語與禁忌資料，特別是胚胎胎兒毒性（致畸胎性）與避孕管控。
- 補齊作用機轉（MOA）資料。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

