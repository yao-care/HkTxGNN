---
layout: default
title: Solriamfetol
parent: 高證據等級 (L1-L2)
nav_order: 699
evidence_level: L1
indication_count: 5
---

# Solriamfetol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Solriamfetol：從嗜睡症相關嗜睡到注意力不足過動症 (ADHD)

## 一句話總結

Solriamfetol 是多巴胺/正腎上腺素再回收抑制劑 (DNRI)，於美國/歐盟核准用於嗜睡症 (narcolepsy) 及阻塞型睡眠呼吸中止症 (OSA) 相關的過度嗜睡（文獻提及，香港尚未上市）。
TxGNN 模型預測它可能對**成人注意力不足過動症 (ADHD)** 有效，
目前有 **2 個臨床試驗**（含 1 個已完成的大型 Phase 3 RCT，n=516）和 **6 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 嗜睡症/OSA 相關過度嗜睡（美國/歐盟核准，非香港核准；香港尚未上市） |
| 預測新適應症 | 注意力不足過動症 (Attention Deficit-Hyperactivity Disorder) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 查詢無結果）。根據現有文獻與試驗描述，Solriamfetol 為**多巴胺/正腎上腺素再回收抑制劑 (DNRI)**，此機轉與現行 ADHD 一線治療藥物（如 methylphenidate、atomoxetine、bupropion）作用的多巴胺/正腎上腺素路徑高度重疊，具有明確的生物學合理性。

Solriamfetol 原本用於治療嗜睡症與 OSA 患者的過度嗜睡，其促醒 (wake-promoting) 特性本質上即是透過強化中樞神經多巴胺/正腎上腺素訊號傳導達成——這與 ADHD 患者常見的注意力調節缺陷所涉及的神經傳導路徑相符，因此模型預測的機轉合理性強。

這個假設已進入實際臨床驗證階段：FOCUS 試驗（NCT05972044）為一項針對成人 ADHD 設計的大型 Phase 3 RCT（n=516，已完成），加上前導的 Phase 2/3 試驗（NCT04839562，n=66，已完成並發表於 *J Clin Psychiatry*），顯示此再利用方向已獲得業界與學術界的重視與投入。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05972044](https://clinicaltrials.gov/study/NCT05972044) | Phase 3 | 完成 | 516 | FOCUS 試驗：評估 solriamfetol 治療成人 ADHD 的療效與安全性，多中心、雙盲、安慰劑對照 |
| [NCT04839562](https://clinicaltrials.gov/study/NCT04839562) | Phase 2/3 | 完成 | 66 | 前導試驗：18-65 歲成人 ADHD 患者的雙盲安慰劑對照研究，為後續 Phase 3 設計基礎 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37819836](https://pubmed.ncbi.nlm.nih.gov/37819836/) | 2023 | RCT | J Clin Psychiatry | 6 週劑量優化試驗（75mg/150mg），60 名成人 ADHD 患者，顯示良好療效與耐受性型態 |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | Review | Expert Opin Pharmacother | 探討超越興奮劑之 ADHD 藥物治療新進展 |
| [40986064](https://pubmed.ncbi.nlm.nih.gov/40986064/) | 2025 | Review | Expert Opin Pharmacother | 聚焦 Phase 3 試驗的 ADHD 潛在治療藥物回顧 |
| [41621729](https://pubmed.ncbi.nlm.nih.gov/41621729/) | 2026 | Review | Pharmacol Ther | 成人 ADHD 複雜治療的藥理、神經調節與心理治療整合策略 |
| [33870884](https://pubmed.ncbi.nlm.nih.gov/33870884/) | 2022 | Perspective/Hypothesis | CNS Spectrums | 提出 solriamfetol 用於 ADHD 治療之假說 |
| [34534876](https://pubmed.ncbi.nlm.nih.gov/34534876/) | 2021 | Review | Epilepsy & Behavior | 癲癇患者合併過度嗜睡與注意力缺陷之藥物治療（背景相關文獻） |

---

## 香港上市資訊

目前 Solriamfetol 未在香港取得任何許可證，無上市藥品資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。（目前 TFDA/香港仿單警語、禁忌症與藥物交互作用資料均缺，列為 Blocking 等級資料缺口，需優先補齊才能進入 S1 安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的大型 Phase 3 RCT（NCT05972044, n=516）直接針對成人 ADHD 設計，加上前導 Phase 2/3 試驗與多篇同儕評審文獻支持，證據等級達 L1，機轉合理性強（DNRI 路徑與現行 ADHD 治療藥物重疊）。
- 但該藥目前在香港未上市（0 張許可證），且仿單安全性資料（警語、禁忌症）與詳細 MOA 資料均為 Blocking/High 等級缺口，尚不足以完成 S1 安全性初評，故需在防護機制下推進，而非直接 Go。

**若要推進需要：**
- 補齊 TFDA/原廠仿單警語與禁忌症資料（Blocking，DG001）
- 補齊 DrugBank 完整作用機轉描述（High，DG002）
- 若考慮香港上市途徑，需評估許可證申請與當地法規要求
- 追蹤 FOCUS 試驗（NCT05972044）正式發表結果，確認具體療效與安全性數據

---

## 附：其他 TxGNN 預測適應症（供參考，品質篩檢用）

| 排名 | 疾病 | 分數 | 證據等級 | 建議 | 備註 |
|-----|------|------|---------|------|------|
| 2 | Faciodigitogenital (Aarskog) syndrome | 99.99% | L5 | Hold | 罕見遺傳症候群，與 DNRI 機轉無已知連結，判斷為知識圖譜雜訊 |
| 3 | Insomnia | 99.97% | L2 | Research Question | 機轉矛盾：solriamfetol 為促醒藥物，理論上應加重而非治療失眠；現有試驗多針對共病嗜睡/疲勞，非典型失眠適應症，需人工釐清 |
| 4 | ADHD, inattentive type | 99.96% | L4 | Research Question | ADHD 亞型節點，機轉推論同主要 ADHD，但無獨立試驗/文獻佐證 |
| 5 | Chondromyxoid fibroma | 99.93% | L5 | Hold | 罕見良性骨腫瘤，與神經傳導再回收抑制機轉無已知路徑重疊，判斷為模型雜訊 |

上表顯示模型在高分區間仍存在明顯雜訊（rank 2、5）與機轉矛盾訊號（rank 3），凸顯僅依賴 TxGNN 分數不足以判斷再利用價值，須搭配機轉合理性與實證資料交叉驗證——這也是本報告優先聚焦 ADHD（rank 1）的主因。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

