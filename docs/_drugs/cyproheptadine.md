---
layout: default
title: Cyproheptadine
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Cyproheptadine：預測新適應症為過敏性蕁麻疹 (Allergic Urticaria)（證據等級 L5）。原適應症：過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、蕁麻疹、血管性水腫等"
---

# Cyproheptadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cyproheptadine：從過敏性鼻炎與蕁麻疹等過敏性疾病到寒冷性蕁麻疹

## 一句話總結

Cyproheptadine 是第一代 H1 抗組織胺藥物，原本用於過敏性鼻炎、蕁麻疹、血管性水腫等過敏性疾病。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效。
目前無已登記的臨床試驗，但有 **9 篇相關文獻**。其中預測排名第 2 的**寒冷性蕁麻疹 (Cold Urticaria)** 有 16 篇文獻，包含數項雙盲比較研究，證據相對較充分。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、蕁麻疹、血管性水腫等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4（過敏性蕁麻疹）；寒冷性蕁麻疹為 L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Hold（過敏性蕁麻疹）；寒冷性蕁麻疹列為研究問題 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位尚未取得）。依文獻與藥理常識，Cyproheptadine 是第一代 H1 抗組織胺藥物，同時具有血清素 (5-HT2) 拮抗與抗膽鹼作用。

蕁麻疹本來就屬於它的既有適應症（蕁麻疹、血管性水腫、過敏性皮膚病）。因此「過敏性蕁麻疹」較像既有適應症的子類型，不是全新的再利用標的。0.9996 的高分很可能反映這種重疊。H1 阻斷可直接對抗組織胺引起的風團與搔癢，機轉上相當吻合。

排名第 2 的**寒冷性蕁麻疹**涉及冷刺激誘發肥大細胞釋放組織胺。Cyproheptadine 長期被視為此病的標準或參考用藥。不過現行指引偏好第二代抗組織胺，且本藥有嗜睡與抗膽鹼副作用，限制了臨床使用。

排名第 3、4 的「鼻腔疾病」與「急性喉咽炎」缺乏任何直接證據。前者與既有的過敏性／血管運動性鼻炎適應症重疊；後者多為感染性，抗組織胺最多只能緩解症狀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下以預測排名第 1（過敏性蕁麻疹）與第 2（寒冷性蕁麻疹）的文獻為主，優先列出對照試驗。

**寒冷性蕁麻疹（排名 2，證據最完整）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | 雙盲比較試驗 | Arch Dermatol | 8 名原發性後天性寒冷性蕁麻疹患者，比較 cyproheptadine、chlorpheniramine 與安慰劑 |
| [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/) | 1984 | 隨機雙盲比較 | J Am Acad Dermatol | 比較 cinnarizine、cyproheptadine、doxepin、hydroxyzine；以冰塊試驗評估，doxepin 較受病人偏好 |
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | 雙盲交叉試驗 | Dermatologica | 18 名患者；acrivastine 與 cyproheptadine 皆顯著縮小風團面積，acrivastine 效果更佳 |
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | 雙盲交叉比較 | Asian Pac J Allergy Immunol | 6 名泰國兒童，比較 cyproheptadine 與 ketotifen |
| [6102102](https://pubmed.ncbi.nlm.nih.gov/6102102/) | 1980 | 臨床研究 | J Allergy Clin Immunol | 服藥期間患者無症狀，冰塊試驗恢復正常，6 人中僅 1 人在冰水浸泡後出現腫脹 |
| [1364168](https://pubmed.ncbi.nlm.nih.gov/1364168/) | 1992 | 隨機單盲交叉 | J Investig Allergol Clin Immunol | 7 名患者，比較 loratadine、cetirizine 與 cyproheptadine、ketotifen |
| [5287036](https://pubmed.ncbi.nlm.nih.gov/5287036/) | 1971 | 臨床研究 | J Allergy Clin Immunol | 以 cyproheptadine 治療寒冷性蕁麻疹 |
| [1305812](https://pubmed.ncbi.nlm.nih.gov/1305812/) | 1992 | 診斷研究 | Asian Pac J Allergy Immunol | 兒童冰塊試驗；cyproheptadine 治療 4 週後，3 分鐘冰塊試驗僅 17% 呈陽性 |

**過敏性蕁麻疹／過敏性皮膚病（排名 1）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [812662](https://pubmed.ncbi.nlm.nih.gov/812662/) | 1976 | 比較療效評估 | Curr Ther Res | 比較 cyproheptadine 與 hydroxyzine 對過敏性皮膚病搔癢的療效 |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | acrivastine 治療過敏性鼻炎與蕁麻疹的回顧（與 cyproheptadine 為間接關聯） |

**證據限制：** 多為 1960–1990 年代的小型研究，設計不一，沒有登記的臨床試驗。

---

## 香港上市資訊

香港共有 17 張有效許可證，皆為單方製劑，無已取消者。以下列出 5 張代表性許可證；資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-17900 | CYPROHEPTADINE TAB 4MG（NEOCHEM） | 錠劑（依品名） | 未載明 |
| HK-05079 | CYPROHEPTADINE TAB 4MG (SYNCO) | 錠劑（依品名） | 未載明 |
| HK-21862 | APPETIN SYRUP 2MG/5ML | 糖漿（依品名） | 未載明 |
| HK-11455 | CYPROHEPTADINE SYRUP 2MG/5ML | 糖漿（依品名） | 未載明 |
| HK-46023 | CYPRODIN TAB 4MG | 錠劑（依品名） | 未載明 |

---

## 安全性考量

- **知識圖譜標示的相關疾病禁忌（非仿單原文）：** 高血壓、消化性潰瘍、良性前列腺增生、高眼壓、隅角閉鎖型青光眼、甲狀腺機能亢進（含葛瑞夫茲氏病、甲狀腺毒症）、膀胱頸阻塞。這與其抗膽鹼作用相符。
- **藥物交互作用：** 共查得 100 筆，以下列出主要者。
  - **嚴重 (Major)：** 檸檬酸鉀 (Potassium citrate)、氯化鉀 (Potassium chloride)
  - **中度 (Moderate)：** 多為抗膽鹼藥物（hyoscyamine、atropine、scopolamine、glycopyrronium、dicyclomine、trospium 等），以及鴉片類（morphine、opium）、loperamide、dronabinol、nabilone、metoclopramide、fenfluramine 等，主要涉及疊加性的抗膽鹼或中樞神經抑制作用。
- 仿單的警語與禁忌尚未取得，請參考香港衛生署核准的原廠仿單。

---

## 結論與下一步

**決策：Hold（過敏性蕁麻疹）；寒冷性蕁麻疹列為研究問題**

**理由：**
- 過敏性蕁麻疹本屬既有適應症，不是新的再利用機會，且無臨床試驗，證據僅 L4。
- 寒冷性蕁麻疹有數項雙盲比較研究支持，但多為老舊小型研究，且現行指引偏好第二代抗組織胺，故停留在 L3，不足以直接推進。
- 鼻腔疾病與急性喉咽炎僅有模型預測（L5），暫不建議投入。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌。
- 補齊 DrugBank 的作用機轉資料。
- 針對寒冷性蕁麻疹，系統性回顧並與現行第二代抗組織胺（可能含加倍劑量）作比較，評估 cyproheptadine 的相對價值。
- 評估老年、前列腺肥大、青光眼等族群的抗膽鹼風險，以及與鉀製劑、抗膽鹼藥物併用的管理方案。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

