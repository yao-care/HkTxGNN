---
layout: default
title: Nonivamide
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Nonivamide：預測新適應症為肺動脈高壓 (Pulmonary Hypertension)（證據等級 L5）。原適應症：香港許可證未提供核准適應症文字"
monitor_inn: "Nonivamide"
predicted_indications: ["pulmonary hypertension", "peripheral arterial disease", "acute lymphoblastic leukemia (disease)", "kyphoscoliotic heart disease", "peripheral vascular disease", "ventricular tachycardia", "anaphylaxis", "migraine disorder", "catecholaminergic polymorphic ventricular tachycardia", "intermittent vascular claudication"]
---

# Nonivamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Nonivamide：從外用止痛（原適應症資料缺漏）到肺動脈高壓
{: .text-alpha }

## 一句話總結

Nonivamide 是合成的辣椒素類似物（TRPV1 促效劑），在香港以外用止痛類產品形式上市。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未提供核准適應症文字 |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 0.9981 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Nonivamide 是辣椒素類似物，作為 TRPV1 促效劑，會活化感覺神經並釋放 CGRP，外用時有血管擴張與局部刺激（發紅）效果。

TRPV1 在肺血管與感覺神經中有表現，也曾被研究用於血管張力調節。但對 Nonivamide 與肺高壓之間，目前並未建立直接關聯。0.9981 的高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，不等於有生物學或臨床證據。

其他預測適應症中，機轉上相對合理的是**偏頭痛**（TRPV1 與 CGRP 為三叉神經血管痛覺訊號的核心，辣椒素類藥物可使痛覺神經去敏感化），但同樣沒有 Nonivamide 專屬的研究資料。周邊動脈疾病、間歇性跛行等僅有「局部血管擴張」的推測；急性淋巴芽細胞白血病、過敏性休克、CPVT、脊柱後側彎性心臟病則缺乏合理的機轉連結。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下表為香港已登記的許可證（皆為複方製劑；張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表）。資料中未提供劑型與核准適應症。

<!-- review:begin hk-lic-20261124b-nonivamide-1 -->

> **查核更正（2026-11-24）**：原文為「下表為香港已登記的 12 張許可證（皆為有效單一成分製劑）。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證皆為複方；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-nonivamide-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-66440 | TIGER BALM LOTION | 複方 | HAW PAR BROTHERS INTERNATIONAL (H K) LTD | 有效 |
| HK-66526 | NEW AMMELTZ YOKO YOKO EXTRA STRENGTH LIQUID | 複方 | KOBAYASHI PHARMACEUTICAL (HONG KONG) COMPANY LIMITED | 有效 |
| HK-62002 | SALONPAS LOTION | 複方 | HISAMITSU PHARMACEUTICAL (HONG KONG) CO., LIMITED | 有效 |
| HK-00349 | AMMELTZ LOTION | 複方 | KOBAYASHI PHARMACEUTICAL (HONG KONG) COMPANY LIMITED | 有效 |
| HK-42348 | NEW AMMELTZ YOKO YOKO LIQUID | 複方 | KOBAYASHI PHARMACEUTICAL (HONG KONG) COMPANY LIMITED | 有效 |

上表列出其中 5 張（共 12 張）。

<!-- licenses:end -->

另有 7 張許可證（如 PANOPAS SOLUTION、STRONG MAITREE-PAS PLASTER、WIDE PASS E PLASTER 等）未在此列出。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆只有模型分數，無臨床試驗與文獻佐證（L5），且 Nonivamide 與肺動脈高壓的機轉連結屬推測。
- 作用機轉與仿單安全性資料皆缺漏，無法進行安全性篩選。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉（MOA）資料，並取得香港衛生署仿單的警語與禁忌資料
- 確認各許可證的劑型與核准適應症
- 進行系統性文獻回顧與前臨床研究，評估 TRPV1 促效劑對肺血管的作用
- 評估外用劑型是否適用於全身性疾病（給藥途徑相容性尚待確認）
- 若要探索替代方向，可優先評估機轉較合理的偏頭痛，並先檢視其安全性風險

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「下表為香港已登記的 12 張許可證（皆為有效單一成分製劑）。」→「下表為香港已登記的許可證（皆為複方製劑；張數與有效張數見本頁」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

