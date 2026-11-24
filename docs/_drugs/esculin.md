---
layout: default
title: Esculin
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Esculin：預測新適應症為閉經 (Amenorrhea)（證據等級 L5）。原適應症：許可證資料未載明核准適應症（產品名稱為痔瘡軟膏類）"
monitor_inn: "ESCULIN"
predicted_indications: ["amenorrhea (disease)"]
---

# Esculin
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

## Esculin：從痔瘡外用製劑到閉經
{: .text-alpha }

## 一句話總結

Esculin（七葉苷）是一種香豆素類配糖體，萃取自七葉樹（馬栗），在香港以痔瘡軟膏（Hemo Ointment）產品上市。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明核准適應症（產品名稱為痔瘡軟膏類） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 0.9921 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 9 張／共 9 張） |
| 許可證數 | 9 張（有效 9 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Esculin 是來自七葉樹的香豆素配糖體，文獻上常被描述具有血管保護、抗發炎與抗氧化特性，這也與其以痔瘡軟膏形式上市的用途相符。

然而，這些特性並未被證實會作用於下視丘－腦下垂體－卵巢軸，也無法對應閉經的常見成因（如下視丘功能異常、多囊性卵巢症候群、高泌乳素血症、原發性卵巢功能不全或解剖構造問題）。

TxGNN 的高分（0.9921）來自 TxGNN 模型（深度學習）的計算推論，可能反映模型在相近疾病之間學到的相似性，不是生物學證據，也不是實驗或臨床證據。因此，痔瘡與閉經之間目前沒有可建立的機轉關聯，任何連結都屬推測，需要獨立驗證。

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
| HK-56046 | LONGS HEMO OINTMENT | 複方 | WILSON TRADING COMPANY LIMITED | 有效 |
| HK-56047 | REVCO HEMO OINTMENT "CHIAU SON" | 複方 | WILSON TRADING COMPANY LIMITED | 有效 |
| HK-56049 | XTRA HEMO OINTMENT "CHIAU SON" | 複方 | WILSON TRADING COMPANY LIMITED | 有效 |
| HK-55324 | ECKERD HEMO OINTMENT | 複方 | WILSON TRADING COMPANY LIMITED | 有效 |
| HK-54828 | HUDSON HEMO OINTMENT | 複方 | WILSON TRADING COMPANY LIMITED | 有效 |

上表列出其中 5 張（共 9 張）。

<!-- licenses:end -->

以上為其中部分許可證，皆為複方製劑，持證商皆為 Wilson Trading Company Limited；張數見本頁快速總覽與「香港上市資訊」的許可證表。

<!-- review:begin hk-lic-20261124b-esculin-1 -->

> **查核更正（2026-11-24）**：原文為「以上為 9 張有效許可證中的 5 張，均為單方製劑，持證商皆為 Wilson Trading Company Limited。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證皆為複方；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-esculin-1 -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗、文獻或明確的機轉支持（證據等級 L5）。
- 作用機轉、原適應症與安全性資料皆缺漏，目前無法進行安全性篩選。

**若要推進需要：**
- 補充 Esculin 的作用機轉資料（例如查詢 DrugBank）。
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌。
- 進行文獻與試驗檢索，確認 Esculin 與閉經成因（如下視丘－腦下垂體－卵巢軸）之間是否存在生物學連結。
- 評估給藥途徑的相容性：現有產品皆為外用軟膏，閉經若需全身性作用，需另行評估。
- 若有前臨床證據支持，再重新評估是否推進。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「以上為 9 張有效許可證中的 5 張，均為單方製劑，持證商皆為 Wilson T」→「以上為其中部分許可證，皆為複方製劑，持證商皆為 Wilson」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

