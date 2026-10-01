---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 5
---

# Indacaterol
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

# Indacaterol：從長效 β2 支氣管擴張劑到腎因性抗利尿不適當症候群

## 一句話總結

Indacaterol 是長效 β2 腎上腺素受體促效劑（吸入型支氣管擴張劑），香港以 Onbrez Breezhaler 等品名上市。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (NSIAD)** 有效，但目前**沒有直接支持的臨床試驗或文獻**，僅有模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別，Indacaterol 是長效 β2 腎上腺素受體促效劑，透過 Gs/cAMP 訊號路徑作用。

從機轉來看，這個預測**缺乏可信的關聯**。NSIAD 的成因是 AVPR2 基因的功能增益突變，使腎臟的 cAMP 訊號已呈持續活化。再進一步活化 Gs 訊號，不太可能帶來幫助，理論上還可能加重水分滯留。0.995 的高分只是知識圖譜的推算結果，沒有任何試驗或文獻佐證。

同一份預測清單中的其他候選也是相同情況，均為 L5、建議 Hold：

| 排名 | 預測適應症 | TxGNN 分數 | 機轉評估 |
|------|-----------|-----------|---------|
| 2 | 頭痛疾患 (Headache disorder) | 99.53% | 頭痛是吸入型 β2 促效劑常見的不良反應，方向相反 |
| 3 | 三叉神經自主神經性頭痛 | 99.33% | 無已知機轉關聯 |
| 4 | 腱鞘周圍炎 (Paratenonitis) | 99.26% | 無已知機轉關聯，吸入劑在肌肉骨骼部位的全身暴露極低 |
| 5 | 鈣化性肌腱炎 | 99.25% | 無證據顯示 β2 促效作用影響肌腱鈣沉積 |

## 臨床試驗證據

針對 NSIAD 沒有任何臨床試驗。以下兩項試驗是連結到排名 2「頭痛疾患」的資料，相關性評級皆為 C（無關），僅供參考：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02576626](https://clinicaltrials.gov/study/NCT02576626) | Phase 4 | 完成 | 40 | 比較 Indacaterol/Glycopyrronium 乾粉吸入器與噴霧器對穩定期 COPD 的 FEV1 與呼吸困難的影響，與頭痛無關 |
| [NCT02165826](https://clinicaltrials.gov/study/NCT02165826) | Phase 3 | 完成 | 1,323 | 評估 Roflumilast 遞增劑量用於 COPD 的耐受性與藥動學，不是 Indacaterol 試驗，也與頭痛療效無關 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 13 張許可證，以下列出 5 張主要許可證，核准適應症文字在資料中未提供：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67628 | ONBREZ BREEZHALER INHALATION POWDER 150MCG/CAPSULE | Novartis Pharmaceuticals (HK) Limited |
| HK-67725 | ONBREZ BREEZHALER INHALATION POWDER 300MCG/CAPSULE | Novartis Pharmaceuticals (HK) Limited |
| HK-60180 | ONBREZ BREEZHALER INHALATION POWDER 150 MCG/CAPSULE | Novartis Pharmaceuticals (HK) Limited |
| HK-60179 | ONBREZ BREEZHALER INHALATION POWDER 300 MCG/CAPSULE | Novartis Pharmaceuticals (HK) Limited |
| HK-67120 | ATECTURA BREEZHALER INHALATION POWDER HARD CAPSULES 150MCG/160MCG | Novartis Pharmaceuticals (HK) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗或文獻支持（L5）。
- 首位的 NSIAD 在機轉上有反向風險，β2 促效可能加重 cAMP 訊號過度活化。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症。
- 補齊 DrugBank 的作用機轉資料，重新評估機轉關聯。
- 針對 NSIAD 做系統性文獻檢索，以及 AVPR2/cAMP 路徑的前臨床機轉研究。
- 在取得任何支持證據前，不建議進入後續評估階段。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

