---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
monitor_inn: "INDOMETHACIN"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
last_modified_at: 2026-10-31
description: "Indomethacin：預測新適應症為短指併指症候群 (brachydactyly-syndactyly syndrome)（證據等級 L5）。原適應症：本報告彙整的許可證資料未提供核准適應症文字。知識圖譜記錄的相關疾病包括滑囊炎、類風濕性關節炎、僵直性脊椎炎、痛風、骨關節炎、動脈導管未閉等"
---

# Indomethacin
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

## Indomethacin：從關節發炎類疾病到短指併指症候群
{: .text-alpha }

## 一句話總結

Indomethacin（吲哚美辛）是一種非類固醇消炎藥。知識圖譜記錄它與滑囊炎、類風濕性關節炎、僵直性脊椎炎、痛風、骨關節炎等疾病有關。TxGNN 模型預測它可能對**短指併指症候群 (brachydactyly-syndactyly syndrome)** 有效。目前**沒有任何臨床試驗或文獻**直接研究這個組合，只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告彙整的許可證資料未提供核准適應症文字。知識圖譜記錄的相關疾病包括滑囊炎、類風濕性關節炎、僵直性脊椎炎、痛風、骨關節炎、動脈導管未閉等（僅為知識圖譜關聯，不等同核准適應症） |
| 預測新適應症 | 短指併指症候群 (brachydactyly-syndactyly syndrome) |
| TxGNN 預測分數 | 0.9997（全體排名第 1093） |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，Indomethacin 是環氧合酶（COX-1 與 COX-2）抑制劑，透過減少前列腺素生成來發揮消炎與止痛作用，這也是它用於關節發炎類疾病的基礎。

短指併指症候群是罕見的先天性肢體發育畸形。這類疾病的成因是發育過程的基因或訊號異常，而不是前列腺素介導的發炎。消炎止痛作用沒有已知的途徑可以矯正骨骼發育缺陷，所以**目前無法建立合理的機轉連結**。

這個高分預測來自 TxGNN 模型（深度學習），分數可能反映模型從相關疾病之間學到的相似性，並非生物學證據，也沒有臨床或文獻佐證。在實際研究支持前，不宜當作有效的線索。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

本報告彙整的資料中，許可證的劑型與核准適應症欄位皆為空白，無法列出。以下為部分主要許可證，完整清單可能不止於此。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-67282 | TOSPAN INDOMETHACIN CAPSULES 25MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-67566 | KECENTIN CAPSULES 25MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-15122 | INDOMETHACIN CAP 25MG | NATIONAL PHARMACEUTICAL CO LTD |
| HK-46461 | RHEUMAXIN CAP 50MG | VICKMANS LABORATORIES LTD |
| HK-01934 | INDOCID CAP 25MG | ASPEN PHARMACARE ASIA LIMITED |

另有 INDECIN CREAM 1% W/W（HK-62726）為外用乳膏劑型。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，並非仿單文字）：高血壓、癲癇、胃潰瘍、十二指腸潰瘍、活動性消化性潰瘍、腎臟疾病、肝臟疾病、血小板低下、凝血異常、氣喘、心肌梗塞、心血管疾病、潰瘍性結腸炎、發炎性腸道疾病、壞死性腸炎、腦內出血等。
- **藥物交互作用**：資料庫共有 100 筆記錄，以下為部分中度交互作用：
  - 類固醇類：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide
  - 其他消炎藥：Acetylsalicylic acid、Mesalazine、Balsalazide
  - 降血糖藥：Metformin、Chlorpropamide、Glimepiride
  - 其他：Aprepitant、鉀鹽類（Potassium citrate、Potassium bicarbonate）、瀉劑類

仿單的警語與禁忌資料尚未取得，詳細安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻直接支持，機轉上也找不到合理的連結，證據等級為 L5。
- 疾病屬於先天性發育異常，消炎藥沒有已知的矯正作用。

**若要推進需要：**
- 找到具體的生物學假說，說明 COX 抑制如何影響此疾病的發育或病理途徑
- 取得 DrugBank 的作用機轉資料，並補齊香港仿單的警語與禁忌
- 在文獻與試驗登記庫中，針對此疾病進行直接檢索與確認

**補充：**同一份預測清單中，排名第 8 的**幼年特發性關節炎**有 19 篇文獻，以回顧和一項 1978 年的雙盲交叉試驗為主，證據較完整，也比較貼近 Indomethacin 的既有用途。若要選擇值得優先評估的方向，建議以該疾病為主要標的另行評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

