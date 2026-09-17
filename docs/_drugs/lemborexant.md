---
layout: default
title: Lemborexant
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 1
---

# Lemborexant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Lemborexant：從國際核准之失眠治療到香港適應症評估

## 一句話總結

Lemborexant（DAYVIGO）是雙重食欲素受體拮抗劑（Dual Orexin Receptor Antagonist），已於美國、日本、加拿大等地核准用於成人失眠症治療，但目前**尚未在香港取得藥品許可證**。TxGNN 模型對其「失眠症－入睡與睡眠維持困難」適應症給出 **99.75%** 的極高預測分數，且有多個已完成的 Phase 3 RCT 及 20 篇文獻支持其療效，屬於**香港市場導入**而非全新機轉再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 失眠症（美國/日本/加拿大等已核准，來源：文獻摘要，非香港官方資料） |
| 預測新適應症 | 失眠症－入睡與睡眠維持困難 (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L1（≥2 個已完成的 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Evidence Pack 中的 `drug.original_moa` 欄位為空，但文獻證據本身已提供足夠線索：多篇摘要（PMID 32096020、33636648）指出 Lemborexant 是一款口服雙重食欲素受體拮抗劑（OXR1/OXR2），透過阻斷促醒訊號來幫助入睡與維持睡眠，並已在美國、日本、加拿大核准用於成人失眠症。

因此，TxGNN 預測的「新適應症」實際上與藥物在其他國家的既有核准適應症**高度重疊**——這不是機轉層面的全新再利用假說，而是反映該藥物在香港尚未上市、但海外已有大量療效證據的「市場導入」情境。模型給出接近 100% 的分數，正是因為知識圖譜中已存在大量藥物-疾病關聯證據支持這個連結。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | 尚未招募 | 15 | 評估 Eszopiclone 與 Lemborexant 對「低喚醒閾值」之阻塞性睡眠呼吸中止合併失眠（COMISA）患者的效果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Network Open | Lemborexant 對老年失眠患者療效優於安慰劑，與 Zolpidem 緩釋劑相當 |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Phase 3, SUNRISE 2) | Sleep | Lemborexant 長期（12個月）療效與耐受性優於安慰劑 |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | RCT (Phase 3, SUNRISE 2) | Sleep Medicine | 長達 12 個月連續使用之有效性與安全性數據 |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | RCT 事後分析 | Sleep Medicine | 輕度 OSA 合併失眠（COMISA）患者使用後睡眠結構（含 REM）之影響分析 |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | 系統性回顧/網絡統合分析 | Lancet | 比較各類失眠藥物急性期與長期治療的相對療效 |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | 系統性回顧/網絡統合分析 | Sleep Medicine Reviews | 針對 20 種失眠藥物療效與耐受性排名比較 |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | 系統性回顧/網絡統合分析 | Translational Psychiatry | Daridorexant、Lemborexant、Suvorexant 三種 DORA 藥物療效與安全性比較 |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | 網絡統合分析 | J Managed Care Spec Pharm | Lemborexant 與其他失眠治療藥物療效比較 |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | 藥物綜述（首次核准） | Drugs | Lemborexant 藥理特性、2019年美國首次核准經過與各國核准現況 |
| [41071053](https://pubmed.ncbi.nlm.nih.gov/41071053/) | 2025 | 綜述 | Expert Review of Clinical Pharmacology | Lemborexant 治療失眠的整體療效與臨床定位回顧 |

## 香港上市資訊

目前 Lemborexant 尚未在香港取得任何藥品許可證（0 張）。

## 安全性考量

安全性資訊請參考原廠仿單。（註：香港仿單警語與禁忌症資料尚未取得，屬 Blocking 等級資料缺口，見下方結論）

## 結論與下一步

**決策：Hold**

**理由：**
- 海外已有 ≥2 個完成的 Phase 3 RCT（SUNRISE 系列）及多篇統合分析支持療效，證據等級達 L1；
- 但香港仿單警語/禁忌症資料完全空白（DG001，Blocking），依規範無法進入 S1 安全性初評，且藥物在香港尚未上市（0 張許可證），故暫緩至資料補齊。

**若要推進需要：**
- 取得香港/原廠仿單警語與禁忌症資料（DG001）
- 補充 DrugBank 作用機轉資料以完善機轉關聯性分析（DG002）
- 評估香港藥品上市途徑（新藥申請或平行進口）並確認當地法規要求
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

