---
layout: default
title: Stannous Fluoride
parent: 僅模型預測 (L5)
nav_order: 833
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Stannous Fluoride：預測新適應症為腦膜炎球菌感染 (Meningococcal Infection)（證據等級 L5）。原適應症：未載明"
monitor_inn: "STANNOUS FLUORIDE"
predicted_indications: ["meningococcal infection"]
---

# Stannous Fluoride
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

# Stannous Fluoride：從（原適應症未載明）到腦膜炎球菌感染

## 一句話總結

Stannous Fluoride（氟化亞錫）在香港有一張上市許可證，但目前資料中未記錄其核准適應症。
TxGNN 模型預測它可能對**腦膜炎球菌感染 (Meningococcal Infection)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未載明 |
| 預測新適應症 | 腦膜炎球菌感染 (Meningococcal Infection) |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，也沒有記錄原適應症。唯一的支持是 TxGNN 給出的高預測分數（0.997），這是圖譜模型的輸出，尚未經過實驗或臨床驗證。

一個合理但未經證實的假設是：亞錫離子與氟離子具有抗菌活性（例如干擾細菌酶與細胞膜，如口腔生物膜控制所見）。然而，這是否能延伸到腦膜炎球菌（*Neisseria meningitidis*，一種侵襲性全身性病原體）並無證據支持。

此外，氟化亞錫在牙科上以局部使用為主，全身暴露量極低，若無相關證據，很難在侵襲性腦膜炎球菌疾病中達到治療濃度。現有治療（如第三代頭孢菌素、青黴素）與預防措施（疫苗、化學預防）已相當有效，因此對局部用藥再利用的未滿足需求偏低。

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
| HK-59808 | KIT FOR THE PREPARATION OF TECHNETIUM TC99M MEBROFENIN | 未載明 | 未載明 |

此許可證為含氟化亞錫成分的鎝-99m Mebrofenin 製備套組（診斷用放射性藥物配套），製造商為 Global Medical Solutions Hong Kong Limited。氟化亞錫在此套組中可能作為配方成分，並非作為治療腦膜炎球菌感染之用。

---

## 安全性考量

- **知識圖譜標示之禁忌疾病**：牙齒氟斑症 (dental fluorosis)（來自 TxGNN 知識圖譜的藥物－疾病禁忌關係，並非仿單內容）

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。藥物交互作用查詢未找到相關資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測分數，缺乏任何臨床試驗、文獻或機轉資料支持（證據等級 L5）。
- 氟化亞錫主要為局部使用、全身暴露有限，難以用於侵襲性感染；且現有標準治療與預防措施已相當有效。

**若要推進需要：**
- 補充 DrugBank 作用機轉（MOA）資料
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症
- 進行體外抗 *N. meningitidis* 活性試驗，並評估全身藥動學與可達濃度
- 確認路徑相容性（目前尚待評估）
- 在上述證據出現前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

