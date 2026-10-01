---
layout: default
title: Triprolidine
parent: 中證據等級 (L3-L4)
nav_order: 896
evidence_level: L4
indication_count: 7
---

# Triprolidine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **7** 個
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

# Triprolidine：從抗組織胺藥到過敏性蕁麻疹

## 一句話總結

Triprolidine 是第一代 H1 受體拮抗劑（抗組織胺藥），香港已有多張許可證，但資料中未載明核准適應症。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效。
目前**沒有臨床試驗**，只有 **6 篇文獻**，且多為其他抗組織胺藥的間接證據，沒有 triprolidine 本身的療效試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證的適應症欄位皆為空白） |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Triprolidine 是第一代 H1 受體拮抗劑。

過敏性蕁麻疹的風團與紅暈，主要來自肥大細胞釋放組織胺。阻斷 H1 受體在機轉上直接相關，這也符合模型給出的高分。

但這個合理性主要來自藥物類別，不是 Triprolidine 本身的臨床資料。檢索到的文獻多半是其他抗組織胺藥（如 acrivastine、非鎮靜型 H1 拮抗劑）的回顧。與 Triprolidine 直接相關的只有一篇 1965 年的皮膚反應研究，並非療效試驗。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7911009](https://pubmed.ncbi.nlm.nih.gov/7911009/) | 1994 | RCT（間接） | Allergy | 雙盲、安慰劑對照交叉試驗，10 位花粉過敏者。評估 acrivastine 抑制皮膚點刺試驗風團反應的起效時間；藥物為 acrivastine，與 triprolidine 為間接關係 |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | acrivastine 的藥理與療效回顧。雙盲試驗顯示對慢性蕁麻疹與過敏性鼻炎有效且耐受性佳 |
| [8094649](https://pubmed.ncbi.nlm.nih.gov/8094649/) | 1993 | Review | Dermatologic Clinics | 新型 H1 抗組織胺藥因鎮靜與抗膽鹼副作用少，為蕁麻疹與輕度血管性水腫的第一線治療 |
| [2568212](https://pubmed.ncbi.nlm.nih.gov/2568212/) | 1989 | Review | Clinical Pharmacy | 回顧非鎮靜型 H1 拮抗劑（terfenadine、astemizole、loratadine、acrivastine）；acrivastine 是 triprolidine 的側鏈縮減代謝物 |
| [1983393](https://pubmed.ncbi.nlm.nih.gov/1983393/) | 1990 | Review/評論 | Drug and Therapeutics Bulletin | 三種新型非鎮靜抗組織胺藥的評論（無摘要） |
| [14283425](https://pubmed.ncbi.nlm.nih.gov/14283425/) | 1965 | 藥效學研究 | British Journal of Dermatology | triprolidine 與皮膚對紫外線反應的研究（無摘要）；唯一與 triprolidine 直接相關，但不是蕁麻疹療效試驗 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-50191 | TRIPROLIDINE HYDROCHLORIDE | SUNRISE TRADING CO |
| HK-53400 | TRIPROLIDINE HYDROCHLORIDE | SUNRISE TRADING CO |
| HK-39992 | TRIPROLIDINE HCL CAP 2.5MG (UNITED LAB) | THE UNITED LABORATORIES LTD |
| HK-54211 | PHARMANIAGA PSEUDOEPHEDRINE T TAB | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-61804 | DUOFED TABLETS | NEOCHEM PHARMACEUTICAL LABORATORIES LTD. |

後兩者看起來是含 pseudoephedrine 的複方製劑。以上僅列 20 張許可證中的 5 張。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數很高，機轉上也合理，但沒有任何 triprolidine 專屬的蕁麻疹療效試驗，證據只是同類藥物的間接推論。
- 更好研究的抗組織胺藥已涵蓋此用途，且香港仿單的警語與禁忌資料缺失，無法進入安全性篩選。
- 目前只適合列為研究問題。
- 其他預測適應症（寒冷性蕁麻疹、鼻腔疾病、咽炎、急性喉咽炎、頑固性異位性皮膚炎、異位性 IgE 反應）證據更弱，同樣建議 Hold。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌資料，這是目前的阻斷項。
- 補充詳細的作用機轉資料（可查詢 DrugBank）。
- 搜尋 triprolidine 本身的蕁麻疹臨床資料，並與已上市的第二代抗組織胺藥比較其增益。
- 確認香港許可證的核准適應症，釐清原適應症與劑型。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

