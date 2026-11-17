---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 7
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
last_modified_at: 2026-10-28
description: "Celecoxib：預測新適應症為肢中型發育不良，Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Celecoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Celecoxib：COX-2 選擇性非類固醇消炎藥 → 肢中型發育不良，Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## 一句話總結

Celecoxib 是一種 COX-2 選擇性非類固醇消炎藥（NSAID），在香港已有多張單一成分的藥品許可證。
TxGNN 模型預測它可能對**肢中型發育不良，Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 肢中型發育不良，Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 50 張／共 50 張） |
| 許可證數 | 50 張（有效 50 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，celecoxib 屬於 COX-2 選擇性抑制劑，主要作用是減少前列腺素生成，產生消炎與止痛效果。

Hunter-Thompson 型肢中型發育不良是一種罕見的遺傳性骨骼發育異常，成因為 CDMP1/GDF5 功能喪失，屬於結構性發育問題。COX-2 抑制並不預期能矯正這類先天性缺陷，因此在機轉上**找不到可信的關聯**。

這個高分僅來自模型的運算預測，並無試驗或文獻佐證，應視為假設產生的線索，而非有效的治療方向。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 50 張含本藥成分的許可證（全部有效；皆為單一成分）。主要許可證如下，其核准適應症文字在本地資料中未記錄。

<!-- review:begin hk-lic-20261117-celecoxib-1 -->

> **查核更正（2026-11-17）**：原文為「本地資料共有至少 20 張單一成分 celecoxib 許可證（清單可能不完整），皆為有效狀態。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 50 張含本藥成分的許可證（全部有效；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-celecoxib-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44731 | CELEBREX CAP 200MG | 未記錄 | 未記錄 |
| HK-61703 | CELECOXIB SANDOZ CAPSULES 200MG | 未記錄 | 未記錄 |
| HK-67848 | CELECOXIB CAPSULES 200MG | 未記錄 | 未記錄 |
| HK-67377 | HOVID CELECOXIB CAPSULES 200MG | 未記錄 | 未記錄 |
| HK-64176 | APO-CELECOXIB CAPSULES 100MG | 未記錄 | 未記錄 |

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，其中列為重大 (Major) 的有 **Eliglustat**；其餘多為中度，例如：
  - 降血糖藥物：Metformin、Glimepiride、Glipizide、Glyburide、Chlorpropamide、Nateglinide、Exenatide
  - 腸道消炎藥：Mesalazine、Balsalazide、Olsalazine
  - 其他：Hydrocortisone、Cimetidine、Levofloxacin、Metronidazole、Naltrexone、Kanamycin

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數，沒有臨床試驗或文獻，且疾病成因（GDF5 功能喪失的先天性骨骼發育異常）與 COX-2 抑制之間缺乏可信的機轉關聯。

**若要推進需要：**
- 提出具體的生物學假說，說明 COX-2 抑制如何影響 GDF5/CDMP1 相關的骨骼發育
- 前臨床研究（細胞或動物模型）驗證
- 補齊作用機轉資料與仿單的警語、禁忌症
- 評估此罕見病族群（多為兒童）使用 NSAID 的風險與效益

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本地資料共有至少 20 張單一成分 celecoxib 許可證（清單可能不完整）」→「香港共有 50 張含本藥成分的許可證（全部有效；皆為單一成分」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

