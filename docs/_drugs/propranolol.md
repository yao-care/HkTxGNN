---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 740
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Propranolol"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
description: "Propranolol：預測新適應症為遠端肌病變，Tateyama 型 (distal myopathy, Tateyama type)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Propranolol: 遠端肌病變，Tateyama 型 (distal myopathy, Tateyama type)
{: .text-alpha }

## 一句話總結

Propranolol（普萘洛爾）是一種非選擇性 β 受體阻斷劑，原本用於高血壓、心房顫動、肥厚性心肌病變及血管瘤等。
TxGNN 模型預測它可能對**遠端肌病變，Tateyama 型 (distal myopathy, Tateyama type)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，這只是模型的計算預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 遠端肌病變，Tateyama 型 (distal myopathy, Tateyama type) |
| TxGNN 預測分數 | 0.9940 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 17 張／共 17 張） |
| 許可證數 | 17 張（有效 17 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Propranolol 屬於非選擇性 β 腎上腺素受體阻斷劑，透過降低心率、減少心肌耗氧量來發揮作用，在心血管疾病中的療效已被證實。

然而，Tateyama 型遠端肌病變是一種與 caveolin 相關的遠端肌病變。根據本報告彙整的資料，β 受體阻斷與這個疾病之間**看不出明確的機轉關聯**。高達 0.9940 的分數屬於模型的計算結果，不能視為療效證據。

另外，此藥在知識圖譜中還有多項肌肉相關疾病（如肌病變、骨骼肌疾病、重症肌無力）被列為禁忌，使這個預測在臨床上更需謹慎看待。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（備註：排名第 5、6 的預測適應症——肝硬化心肌病變與心肌病變——有少量文獻，但與本報告主要預測的疾病無關，故不列入。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50454 | BETAPRESS 10 FC TAB 10MG | 未載明 | 未載明 |
| HK-45677 | BECARDIN 40 TAB 40MG | 未載明 | 未載明 |
| HK-45676 | BECARDIN 10 TAB 10MG | 未載明 | 未載明 |
| HK-33813 | DERALIN 10 TAB 10MG | 未載明 | 未載明 |
| HK-16631 | PROPRANOLOL TAB 10MG | 未載明 | 未載明 |

（共 17 張有效許可證，皆為單一成分製劑；上表僅列出 5 張。）

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：支氣管炎、肝臟疾病、腎臟疾病、胰臟炎、糖尿病與糖尿病酮酸中毒、痛風、重症肌無力、肌病變與骨骼肌疾病、家族性週期性麻痺、全身性紅斑狼瘡、肝性腦病變、無尿症、高血鈣症等。
- **藥物交互作用**（DDInter，共 100 筆，以下為部分）：
  - 重大 (Major)：Epinephrine（腎上腺素）
  - 中度 (Moderate)：Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone、Atropine、Morphine、Bupropion、Cimetidine、Canagliflozin、Chlorpropamide 等
  - 輕微 (Minor)：Ascorbic acid、Acetylsalicylic acid、Magnesium oxide

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型計算（L5），沒有臨床試驗或文獻佐證，機轉上也看不出合理關聯。
- 知識圖譜將多種肌肉疾病列為此藥的禁忌，臨床上有潛在安全疑慮。

**若要推進需要：**
- 取得 Propranolol 的作用機轉資料，並評估其與 caveolin 相關肌病變的機轉關聯
- 進行文獻與臨床試驗登記的系統性檢索
- 取得香港衛生署核准的仿單，確認警語與禁忌
- 若有前臨床（細胞或動物模型）證據，再重新評估；目前建議優先研究其他排名較高證據的預測（例如肝硬化心肌病變、心肌病變，兩者皆為 L4 的研究問題）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

