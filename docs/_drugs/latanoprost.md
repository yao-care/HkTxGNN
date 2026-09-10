---
layout: default
title: Latanoprost
parent: 高證據等級 (L1-L2)
nav_order: 439
evidence_level: L2
indication_count: 5
---

# Latanoprost
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Latanoprost：從青光眼治療到原發性遺傳性青光眼（罕見亞型）

## 一句話總結

Latanoprost 是前列腺素 F2α 類似物，全球廣泛用於青光眼與高眼壓症治療，惟此藥物尚未在台灣完成許可證登記，故原始適應症與作用機轉資料目前缺失。TxGNN 模型預測它可能對**原發性遺傳性青光眼（Primary Hereditary Glaucoma）**——一種罕見亞型——有效，目前有 **1 個已完成的 Phase 2 臨床試驗**支持這個方向，文獻證據暫缺。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式登記記錄（台灣尚未上市，無許可證資料） |
| 預測新適應症 | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L2 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 Latanoprost 詳細的官方作用機轉資料（Data Gap）。但根據 TxGNN 證據包中的機轉關聯分析，Latanoprost 屬於前列腺素 F2α 類似物，經典藥理機轉為增加葡萄膜鞏膜房水外流以降低眼壓，是全球青光眼治療的一線藥物類別。

原發性遺傳性青光眼在病理生理上仍以眼壓調控異常為核心，與 Latanoprost 已知的降眼壓機轉高度一致。換句話說，此預測屬於**同類機轉延伸**（同一藥理作用機轉套用到同疾病大類下的罕見亞型），而非跨機轉的新適應症外推，合理性相對較高。唯一的限制是，現有臨床試驗證據（NCT01527682）測試的是前列腺素類似物合併碳酸酐酶抑制劑用於兒童青光眼族群，並未完全確認試驗中使用的是 Latanoprost 本體，需要進一步查證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | 完成 | 37 | 評估前列腺素類似物（latanoprost）合併 dorzolamide 對手術治療無效之原發性兒童青光眼患者的降眼壓效果與安全性 |

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。（台灣仿單警語、禁忌症與藥物交互作用資料目前缺失，屬 Blocking 等級資料缺口，需另行取得。）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的 Phase 2 RCT 直接測試該藥物類別於相關青光眼適應症，機轉關聯性合理（同類機轉延伸而非新機轉外推），達 L2 證據等級。
- 但關鍵安全性資料（仿單警語、禁忌症）與作用機轉正式記錄仍缺失，且台灣尚未取得許可證上市，須在補齊這些資料前設下防護關卡（Guardrails）才能繼續推進。

**若要推進需要：**
- 取得台灣仿單警語與禁忌症資料（DG001，Blocking，來源：TFDA 官網，需下載並解析仿單 PDF）
- 確認正式作用機轉（MOA）資料，以強化機轉關聯性分析（DG002，High，來源：DrugBank API）
- 確認 NCT01527682 試驗中是否明確使用 Latanoprost 本體（而非其他前列腺素類似物）
- 評估台灣上市登記可行性（目前為 0 張許可證，未上市狀態）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

