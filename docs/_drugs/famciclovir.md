---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Famciclovir：預測新適應症為感染後神經痛 (post-infectious neuralgia)（證據等級 L5）。原適應症：帶狀疱疹 (herpes zoster)"
---

# Famciclovir
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

# Famciclovir：從帶狀疱疹到帶狀疱疹後神經痛

## 一句話總結

Famciclovir 是口服抗疱疹病毒藥物，原本用於治療帶狀疱疹。
TxGNN 模型預測它可能對**感染後神經痛 (post-infectious neuralgia)** 有效，
但目前僅有 **1 個臨床試驗**（且該試驗並非直接測試 famciclovir）、**0 篇直接相關文獻**，證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 帶狀疱疹 (herpes zoster)（來源為知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 感染後神經痛 (post-infectious neuralgia) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，famciclovir 是抗疱疹病毒核苷類似物的前驅藥，其成分在帶狀疱疹中的療效已被證實，機轉上可能與帶狀疱疹後神經痛有關。

從疾病關聯來看，帶狀疱疹後神經痛 (PHN) 是帶狀疱疹最常見的併發症。合理的假設是：在急性期及早抗病毒，縮短病毒複製與神經發炎，或有機會降低後續神經痛的發生。這是臨床推論，並非本次資料所證實。

需要特別留意：本次資料中唯一的臨床試驗，是研究急性期早期使用 oxycodone 預防 PHN，並非測試 famciclovir。因此模型的高分主要反映疾病間的關聯，尚不能視為藥物有效的證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | 不適用 (NA) | 未知 | 140 | 評估帶狀疱疹急性期早期使用 oxycodone 能否預防帶狀疱疹後神經痛（試驗藥物非 famciclovir） |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66386 | FAMICOL TABLETS 250MG | 錠劑 | 未載明 |
| HK-39905 | FAMVIR TAB 125MG | 錠劑 | 未載明 |
| HK-57504 | PMS-FAMCICLOVIR TAB 250MG | 錠劑 | 未載明 |
| HK-39023 | FAMVIR TAB 250MG | 錠劑 | 未載明 |
| HK-58557 | APO-FAMCICLOVIR TAB 125MG | 錠劑 | 未載明 |

（共 8 張有效單方許可證，此處列出 5 張。品名後的 TAB 推定為錠劑。）

---

## 安全性考量

- **知識圖譜標示的相關疾病禁忌**：腎臟疾病 (kidney disease)、輸尿管積膿 (pyoureter)。此為知識圖譜的關聯，並非仿單原文。
- **藥物交互作用**：資料庫共收錄 84 筆交互作用，但嚴重程度皆為「未知」。例如 calcitriol、doxycycline、metformin、omeprazole、morphine、prednisone、simvastatin 等，臨床意義需另行查證。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何直接測試 famciclovir 用於 PHN 的臨床試驗或文獻，僅有模型預測（L5）。
- 唯一的試驗測試的是另一種藥物，且狀態不明。

**若要推進需要：**
- 搜尋並評估 famciclovir（或同類藥物 valacyclovir）預防 PHN 的既有研究與系統性回顧
- 補齊作用機轉資料與香港仿單的警語、禁忌
- 若有進一步價值，設計急性期抗病毒治療對 PHN 發生率影響的比較研究
- 針對腎功能不全族群，確認劑量調整與安全性監測方案
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

