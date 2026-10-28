---
layout: default
title: Cetuximab
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
monitor_inn: "Cetuximab"
predicted_indications: ["non-seminomatous lesion", "ductal or ductular proliferation", "bronchial adenomas/carcinoids childhood", "chondroid hamartoma", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "cystic neoplasm", "epiglottis neoplasm", "pre-malignant neoplasm"]
last_modified_at: 2026-10-28
description: "Cetuximab：預測新適應症為非精原細胞瘤病灶 (Non-seminomatous Lesion)（證據等級 L5）。原適應症：香港許可證資料未提供核准適應症文字。知識圖譜記錄的關聯為大腸直腸癌、頭頸部鱗狀細胞癌等"
---

# Cetuximab
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

## Cetuximab：從大腸直腸癌與頭頸部鱗狀細胞癌，到非精原細胞瘤病灶 (Non-seminomatous Lesion)
{: .text-alpha }

## 一句話總結

Cetuximab 是一種 EGFR 單株抗體，知識圖譜記錄它與大腸直腸癌、頭頸部鱗狀細胞癌等疾病有關聯。
TxGNN 模型預測它可能對**非精原細胞瘤病灶 (Non-seminomatous Lesion)** 有效。
但本報告彙整的資料中**沒有臨床試驗，也沒有文獻**直接支持這個方向，目前只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未提供核准適應症文字。知識圖譜記錄的關聯為大腸直腸癌、頭頸部鱗狀細胞癌等（僅為知識圖譜關聯，不等同核准適應症） |
| 預測新適應症 | 非精原細胞瘤病灶 (Non-seminomatous Lesion) |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料，Cetuximab 是結合表皮生長因子受體 (EGFR) 的抗體。它用於 EGFR 表現的轉移性大腸直腸癌，也與放射線治療併用於鱗狀細胞來源的頭頸癌。

模型預測的新適應症是非精原細胞瘤（非精原細胞生殖細胞）病灶。目前沒有資料顯示這類病灶依賴 EGFR 訊號，因此無法建立機轉上的合理連結。

這個預測目前只是模型分數，沒有任何試驗或文獻佐證，應視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57484 | ERBITUX 輸注液 5mg/ml（Merck Pharmaceutical (HK) Limited） | 未提供 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 EGFR 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單。相關文獻提到須留意嚴重輸注反應與皮膚disorders |
| 處置防護 | 請參考原廠仿單與院內抗腫瘤藥物處置規範 |

## 安全性考量

- **藥物交互作用**：資料庫共記錄 19 筆藥物交互作用（另有 1 筆為 EGFR 標靶資訊，非交互作用）。
  - **嚴重 (Major)**：Aminolevulinic acid、Thalidomide。
  - **中度 (Moderate)**：質子幫浦抑制劑（Rabeprazole、Omeprazole、Esomeprazole、Lansoprazole、Dexlansoprazole、Pantoprazole）。
  - **中度 (Moderate)**：化療藥物（Capecitabine、Fluorouracil、Cisplatin、Carboplatin、Oxaliplatin）。
  - **中度 (Moderate)**：其他藥物（Idelalisib、Methoxsalen、Verteporfin 等）。

其他警語與禁忌症請參考原廠仿單。

## 其他預測適應症概覽

同一份資料中還有其他預測，其中少數有部分證據。以下證據等級採保守判定：只有直接研究該疾病本身的研究才算數，只涉及相關疾病的一律視為 L5。

| 預測適應症 | TxGNN 分數 | 證據狀況 | 證據等級 |
|-----------|-----------|---------|---------|
| 導管或小導管增生 | 0.9995 | 文獻以胰臟癌的綜述與前臨床研究為主，並未直接研究此疾病。KRAS 突變可能導致抗 EGFR 抗體抗藥 | L5 |
| 囊性腫瘤 | 0.9995 | 有腺樣囊性癌與唾液腺癌的 Phase I/II 試驗與單臂 Phase II 研究（PMID 18804410），屬相關但不同的腫瘤，並非囊性腫瘤本身 | L5 |
| 癌前期腫瘤 | 0.9995 | NCT00524017 為已完成的 Phase II 單藥試驗（35 人），對象為高風險上呼吸消化道癌前病灶。結果未提供，規模小 | L2（僅限該部位，結果待確認） |
| 牙源性囊腫 | 0.9995 | 僅有 2 篇原發性骨內癌的病例報告，屬間接證據 | L5 |
| 睪丸腫瘤、支氣管腺瘤/類癌（兒童）、軟骨樣錯構瘤、甲狀舌管囊腫、會厭腫瘤 | 約 0.9995 | 無試驗或文獻。會厭鱗狀細胞癌可能已落在頭頸癌既有用途範圍內 | L5 |

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測「非精原細胞瘤病灶」沒有任何臨床試驗或文獻，機轉上也看不出與 EGFR 的關聯，只有模型分數。
- 在其他預測中，只有「高風險上呼吸消化道癌前病灶」有直接的 Phase II 試驗，其餘大多只有間接證據。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌症。
- 補充詳細的作用機轉資料。
- 確認非精原細胞瘤病灶是否有 EGFR 表現，並檢索相關前臨床或臨床研究。
- 若考慮其他候選，優先取得 NCT00524017 的結果，並確認其研究設計。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

