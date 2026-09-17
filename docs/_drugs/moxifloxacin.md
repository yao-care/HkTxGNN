---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 510
evidence_level: L5
indication_count: 5
---

# Moxifloxacin
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

# Moxifloxacin：原適應症資料缺失 → 預測新適應症 Hyperamylasemia（高澱粉酶血症）

## 一句話總結

本 Evidence Pack 未提供 Moxifloxacin 的原適應症登記資訊與作用機轉（MOA）資料。
TxGNN 模型預測它可能對 **Hyperamylasemia（高澱粉酶血症）** 有效，
但目前查無任何**臨床試驗**或**文獻**佐證這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供核准適應症文字；香港無許可證登記） |
| 預測新適應症 | Hyperamylasemia (高澱粉酶血症) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻佐證） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA），本 Evidence Pack 也未提供 Moxifloxacin 的原適應症登記資訊，因此無法就「原適應症 → 預測新適應症」進行實質的機轉關聯性分析。

以國際通用藥品分類而言，Moxifloxacin 為第四代氟喹諾酮類抗生素，臨床上主要用於細菌感染治療（此為藥品通用分類常識，非本 Evidence Pack 提供的資料）。其藥理機轉一般為抑制細菌 DNA gyrase / topoisomerase IV，與 Hyperamylasemia（通常與胰臟發炎、唾液腺疾病或腎功能異常相關）之間並無已知的直接病理生理連結。

值得注意的是，本批預測中 rank 799（hyperamylasemia）與 rank 800（polyclonal hyperviscosity syndrome）的 TxGNN 分數完全相同（0.9997972846031188），顯示此排序區間可能落在模型信心邊界附近，需要更多獨立證據才能判斷預測是否具實質意義。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測新適應症 Hyperamylasemia 目前沒有任何臨床試驗或文獻證據支持（evidence level L5，僅為模型預測）。
- 藥物層級的關鍵安全性資料（仿單警語、禁忌）屬於 Blocking 等級的資料缺口（DG001），且作用機轉未知（DG002），目前無法進行安全性初評或機轉合理性分析。
- 該藥物目前未於香港上市，無許可證資訊可供參照。

**若要推進需要：**
- 取得仿單警語與禁忌症資料（DG001，Blocking：下載仿單 PDF 並解析）
- 查詢 DrugBank API 取得完整作用機轉資料（DG002，High）
- 針對 Hyperamylasemia 補做文獻／臨床試驗檢索，確認是否有近期未收錄的證據
- 若證據持續缺口，建議改評估同批候選中證據相對較多者（如 rank 3 congenital analbuminemia，雖僅 1 篇 case report，仍優於 rank 1/2 的零證據狀態）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

