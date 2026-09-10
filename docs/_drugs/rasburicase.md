---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 5
---

# Rasburicase
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

# RASBURICASE：原適應症資料缺失 → 腎性低尿酸血症（預測）

## 一句話總結

RASBURICASE（DrugBank ID: DB00049）目前原適應症與作用機轉資料在本次 Evidence Pack 中均缺失。
TxGNN 模型預測它可能對**腎性低尿酸血症（Hypouricemia, Renal）**有效，
但目前**無臨床試驗、無文獻**支持這個方向，僅為模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未收錄，`original_indications` 為空） |
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, Renal) |
| TxGNN 預測分數 | 99.99%（rank 538） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 RASBURICASE 詳細的作用機轉（MOA）資料，Evidence Pack 中已標記為 Data Gap（DG002，嚴重度 High）。同時原適應症欄位也是空的，因此無法就「原適應症 → 預測新適應症」進行機轉關聯性分析。

由於 MOA 與原適應症兩項基礎資料同時缺失，本報告無法對此預測方向給出機轉層面的合理性論證，僅能呈現 TxGNN 模型輸出的分數與排名。建議先補齊 DrugBank MOA 查詢，再重新評估機轉關聯性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前無香港許可證資料（`market_status`：未上市，`total_licenses`：0）。

## 安全性考量

安全性資訊請參考原廠仿單。

（`key_warnings`、`contraindications`、DDI 查詢均無資料；且 DG001 標記為 Blocking，缺乏 TFDA/香港藥品仿單警語與禁忌資料，尚無法進行 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- DG001 為 Blocking 等級缺口（仿單警語/禁忌資料缺失），依規則無法進入 S1 安全性初評。
- 5 個預測適應症皆無任何臨床試驗或文獻佐證（`evidence_level` 均為 pending，實質為 L5），且藥物尚未在香港上市，證據強度不足以支持推進。

**若要推進需要：**
- 補齊 DG001：取得仿單警語/禁忌資料（來源：TFDA 官網，下載仿單 PDF 並解析）
- 補齊 DG002：查詢 DrugBank API 取得作用機轉（MOA）
- 補齊原適應症資料，以利機轉關聯性分析
- 針對排名前列的預測適應症（含下方其他候選）擴大臨床試驗與文獻檢索

---

**其他預測適應症（同批候選，僅供參考，證據狀況相同）：**
- Rank 2：HGPRT 部分缺乏症（99.97%，rank 990）
- Rank 3：肝性紫質症（99.97%，rank 1114）
- Rank 4：早發性家族性非肝硬化門靜脈高壓（99.97%，rank 1137）
- Rank 5：原發性門靜脈血栓形成（99.97%，rank 1138）

以上皆無臨床試驗或文獻資料，證據等級同為 L5。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

