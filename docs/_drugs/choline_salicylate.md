---
layout: default
title: Choline Salicylate
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 9
monitor_inn: "Choline salicylate"
predicted_indications: ["Prinzmetal angina", "hypertensive disorder", "migraine disorder", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "malignant renovascular hypertension", "Raynaud disease", "pulmonary hypertension"]
last_modified_at: 2026-11-24
description: "Choline Salicylate：預測新適應症為變異型心絞痛 (Prinzmetal angina)（證據等級 L5）。香港藥劑製品註冊：8 張（有效 8 張）"
---

# Choline Salicylate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Choline salicylate：水楊酸類消炎鎮痛藥 → 變異型心絞痛 (Prinzmetal angina)
{: .text-alpha }

## 一句話總結

Choline salicylate 是一種非乙醯化的水楊酸類藥物，具有抑制環氧合酶（COX）的消炎止痛作用。
TxGNN 模型預測它可能對**變異型心絞痛 (Prinzmetal angina)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 0.9984 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Choline salicylate 屬於水楊酸類藥物，一般認為透過抑制 COX 而產生消炎與止痛作用。

變異型心絞痛的主要成因是冠狀動脈痙攣。COX 抑制並非此疾病公認的治療機轉，NSAID 類藥物甚至可能對血管張力產生不利影響。因此，這個高分預測目前只能視為模型的關聯推測，在機轉上並沒有明確的支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-32005 | DERMOJELA GEL | 單一成分 | JEAN-MARIE PHARMACAL CO LTD | 有效 |
| HK-32406 | OROJEL ORAL GEL | 單一成分 | MARCHING PHARMACEUTICAL LIMITED | 有效 |
| HK-37437 | BONJELA GEL | 複方 | RECKITT BENCKISER HONG KONG LTD | 有效 |
| HK-35703 | ORO-SEP GEL | 複方 | MARCHING PHARMACEUTICAL LIMITED | 有效 |
| HK-30925 | ORIS-GEL | 複方 | MARCHING PHARMACEUTICAL LIMITED | 有效 |

上表列出其中 5 張（共 8 張）。

<!-- licenses:end -->

目前含本藥成分的許可證包括單一成分與複方製劑（張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表）。

<!-- review:begin hk-lic-20261124b-choline_salicylate-1 -->

> **查核更正（2026-11-24）**：原文為「目前 8 張許可證皆為有效的單一成分製劑。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-choline_salicylate-1 -->

## 安全性考量

- **藥物交互作用**：已查詢到多筆交互作用，主要包括：
  - 中度：皮質類固醇（Hydrocortisone、Triamcinolone、Dexamethasone、Betamethasone、Budesonide）
  - 中度：磺醯脲類降血糖藥（Chlorpropamide、Acetohexamide、Glimepiride、Glipizide、Glyburide）及胰島素
  - 中度：制酸劑與吸附劑（Aluminum hydroxide、Calcium carbonate、Activated charcoal）
  - 中度：Fenfluramine、Dexfenfluramine
  - 輕度：質子幫浦抑制劑（Rabeprazole、Dexlansoprazole）
- 水楊酸類藥物可能影響腎臟前列腺素與血壓，用於心血管相關適應症時需特別留意。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有臨床試驗或文獻支持，證據等級為 L5。
- 變異型心絞痛由血管痙攣所致，COX 抑制並非已知的治療機轉，機轉上缺乏合理性。

**若要推進需要：**
- 取得 Choline salicylate 的詳細作用機轉資料，並評估與冠狀動脈痙攣的關聯
- 進行針對變異型心絞痛的文獻與臨床試驗系統性搜尋
- 取得香港原廠仿單的警語與禁忌症資料，完成安全性評估
- 若有初步機轉或前臨床證據，再重新評估是否進入下一階段

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「目前 8 張許可證皆為有效的單一成分製劑。」→「目前含本藥成分的許可證包括單一成分與複方製劑（張數與有效張數」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

