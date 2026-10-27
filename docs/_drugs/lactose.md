---
layout: default
title: Lactose
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lactose：預測新適應症為無出血的食道靜脈曲張 (esophageal varices without bleeding)（證據等級 L5）。原適應症：乳糖不耐症"
monitor_inn: "Lactose"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding", "varicose disease", "Steel syndrome", "cystinosis", "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Immunoerythromyeloid hypoplasia", "familial apolipoprotein C-II deficiency", "hypophosphatasia"]
---

# Lactose
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

## Lactose：從乳糖不耐症到食道靜脈曲張（無出血）
{: .text-alpha }

## 一句話總結

Lactose（乳糖）是一種雙醣，常作為膳食糖類與藥品賦形劑，原本的適應症為乳糖不耐症。
TxGNN 模型預測它可能對**無出血的食道靜脈曲張 (esophageal varices without bleeding)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乳糖不耐症（來自知識圖譜的適應症關聯；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 無出血的食道靜脈曲張 (esophageal varices without bleeding) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。乳糖是一種膳食雙醣，也是藥品常用的賦形劑；水解後產生葡萄糖與半乳糖，可作為能量來源。其原適應症乳糖不耐症與食道靜脈曲張在病理上沒有直接關聯。

目前找不到可信的機轉連結。乳糖對門脈壓力、靜脈曲張血管壁張力或止血功能都沒有已知作用。一個可能的解釋是：另一種合成雙醣「乳果糖 (lactulose)」被用於門脈高壓相關的肝性腦病變，因此模型的預測可能反映了糖類之間的相似性或名稱混淆。這只是推測，沒有資料支持。

同一組預測中，「有出血的食道靜脈曲張」分數完全相同，且排名前後相鄰，較可能是知識圖譜中相鄰疾病節點造成的計算結果，而非生物學上的證據。其他排名較前的預測（靜脈曲張疾病、Steel 症候群、胱胺酸症、低磷酸酶症等）同樣缺乏機轉依據與研究支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43329 | MICROGYNON 30 ED TAB | 未載明 | 未載明 |
| HK-56563 | YAZ TAB | 未載明 | 未載明 |
| HK-68562 | ALYSSA TABLETS | 未載明 | 未載明 |
| HK-65968 | MEDIAZ TABLETS | 未載明 | 未載明 |
| HK-59784 | QLAIRA TAB | 未載明 | 未載明 |

上述 5 張皆為有效的單一成分許可證，品項看來屬口服避孕藥製劑，乳糖在其中很可能是賦形劑，並非作為治療用的主成分。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型計算（證據等級 L5），沒有臨床試驗、文獻或機轉依據，且乳糖對門脈高壓或靜脈曲張沒有已知藥理作用。
- 香港上市的產品中，乳糖多半是賦形劑，不能作為支持新適應症的證據。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA），並檢視預測是否與乳果糖混淆
- 取得香港衛生署仿單的警語與禁忌資料
- 進行文獻與臨床試驗的系統性檢索，確認是否有任何支持證據
- 在有任何機轉或臨床訊號之前，不建議投入進一步的研發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

