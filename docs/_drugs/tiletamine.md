---
layout: default
title: Tiletamine
parent: 僅模型預測 (L5)
nav_order: 879
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Tiletamine：預測新適應症為失眠 (Insomnia)（證據等級 L5）。原適應症：許可證未載明（依藥物類別，為獸醫用解離性麻醉）"
monitor_inn: "TILETAMINE"
predicted_indications: ["insomnia (disease)"]
---

# Tiletamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Tiletamine：從獸醫用解離性麻醉到失眠
{: .text-alpha }

## 一句話總結

Tiletamine 目前在香港僅以獸醫用注射劑（Zoletil）形式上市，原適應症資料未載明。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（依藥物類別，為獸醫用解離性麻醉） |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 0.9983 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依藥物類別推論，Tiletamine 屬於芳基環己胺類 (arylcyclohexylamine) 的 NMDA 受體拮抗劑，與 ketamine、phencyclidine 相近。在獸醫領域，它與 zolazepam 組成複方，用作解離性麻醉劑。以上說明是根據藥物類別推論，並非來自本次彙整的資料。

從機轉角度看，NMDA 拮抗作用可能影響睡眠與覺醒相關的神經迴路，這是模型預測可能成立的一個方向。

不過需要謹慎：ketamine 等解離性藥物已知會干擾睡眠結構，並可能引起類精神病反應，因此對失眠是否真有淨效益並不確定。0.9983 的 TxGNN 分數只是計算預測，沒有實際研究佐證或反駁。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-47383 | ZOLETIL 100 FOR INJECTION (VET) | 複方 | VIRBAC H.K. TRADING LIMITED | 有效 |
| HK-43831 | ZOLETIL 50 FOR INJ (VET) | 複方 | VIRBAC H.K. TRADING LIMITED | 有效 |

<!-- licenses:end -->

上表許可證皆為複方（tiletamine 與 zolazepam），持證商為 VIRBAC H.K. TRADING LIMITED，且皆為獸醫用產品；狀態見表中「狀態」欄。

<!-- review:begin hk-lic-20261124b-tiletamine-1 -->

> **查核更正（2026-11-24）**：原文為「兩張許可證均為單方、有效，持證商為 VIRBAC H.K. TRADING LIMITED，且皆為獸醫用產品。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證皆為複方；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-tiletamine-1 -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有模型預測，沒有任何臨床試驗或文獻。
- 香港現有產品僅為獸醫用，且同類藥物可能擾亂睡眠並引起精神症狀，對失眠的淨效益不確定。

**若要推進需要：**
- 取得詳細的作用機轉資料，釐清 NMDA 拮抗與睡眠調節的關係
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 進行文獻與臨床試驗檢索，確認是否有支持或反駁的證據
- 評估人用劑型與給藥途徑的可行性（目前僅有獸醫用注射劑）
- 前臨床研究評估對睡眠結構的影響與精神副作用風險

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「兩張許可證均為單方、有效，持證商為 VIRBAC H.K. TRADING LI」→「上表許可證皆為複方（tiletamine 與 zolazep」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

