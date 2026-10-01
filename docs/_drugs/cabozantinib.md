---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib：從原適應症（證據包未載明）到脂肪肉瘤

## 一句話總結

Cabozantinib 是口服多重激酶抑制劑，在香港以 CABOMETYX 錠劑上市，但證據包未載明原適應症。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，目前有 **1 個臨床試驗**和 **1 篇文獻**支持，且兩者都是針對整體軟組織肉瘤，並非脂肪肉瘤專屬。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 證據包未載明（香港許可證未附適應症文字） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L2（證據包標示；唯一的隨機 Phase 2 試驗尚未完成，依判定規則屬偏樂觀，保守看待） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。
不過依證據包中的機轉推論，Cabozantinib 可抑制 MET、VEGFR2 與 AXL，這些標的與肉瘤的血管新生和腫瘤進展有關。

軟組織肉瘤包含脂肪肉瘤在內的多種亞型，Cabozantinib 在多種軟組織肉瘤亞型中已有活性報告。
但現有試驗與論文都以軟組織肉瘤整體為對象，**尚未證實對脂肪肉瘤本身有效**。

另外，證據包中排名第 7 的「腎細胞癌」有多項已完成的 Phase 3 RCT（如 METEOR、CheckMate 9ER、CONTACT-03）。
這說明 Cabozantinib 的核心已知用途很可能是腎細胞癌，證據包的「原適應症」欄位為空，應視為資料缺漏。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | 進行中（不再招募） | 66 | 隨機比較 Ipilimumab + Nivolumab 單獨使用與加上 Cabozantinib，用於晚期軟組織肉瘤；尚無公布結果，且非脂肪肉瘤專屬 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 試驗 | American Journal of Clinical Oncology | 評估 Cabozantinib 併用放射治療作為四肢軟組織肉瘤術前治療的安全性；背景指出該藥在多種軟組織肉瘤亞型有活性，但曾擔心瘻管或穿孔風險 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 持證商 |
|---------|------|------|--------|
| HK-65656 | CABOMETYX TABLETS 20MG | 錠劑 | BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED |
| HK-65654 | CABOMETYX TABLETS 40MG | 錠劑 | BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED |
| HK-65655 | CABOMETYX TABLETS 60MG | 錠劑 | BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多重酪胺酸激酶抑制劑，靶點 MET、VEGFR2、AXL） |
| 其他項目（骨髓抑制風險、致吐性、監測項目、處置防護） | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 脂肪肉瘤缺乏專屬證據：僅有 1 個進行中的軟組織肉瘤 Phase 2 試驗（無結果）和 1 篇 Phase 1 安全性研究。
- 香港仿單的警語與禁忌資料尚未取得（阻擋性資料缺口），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症，並確認原適應症以釐清這是否屬於藥物再利用。
- 等待 NCT05836571 公布結果，並確認其中脂肪肉瘤亞群的療效資料。
- 補充 DrugBank 的作用機轉與交互作用資料。
- 評估併用放射治療時的瘻管或穿孔風險。

若團隊想優先推進 Cabozantinib 的其他方向，證據包中「非透明細胞型腎細胞癌」有多項 Phase 2 試驗支持（建議 Proceed with Guardrails，須先確認是否為既有核准適應症）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

