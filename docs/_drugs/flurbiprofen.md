---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 5
---

# Flurbiprofen
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

# Flurbiprofen：從 NSAID 類消炎止痛藥到肢端中段發育不良（Hunter-Thompson 型）

## 一句話總結

Flurbiprofen 是一種一般認為屬於非類固醇消炎止痛藥（NSAID）的成分，香港已有 3 張上市許可證。
TxGNN 模型預測它可能對**肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效。
目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.99%（全體排名第 497） |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Flurbiprofen 一般被認為是非選擇性 COX 抑制劑（NSAID），但這是通識性描述，並非本次輸入資料中的機轉。抑制 COX 會減少前列腺素合成，主要作用是消炎與止痛。

這個預測疾病是罕見的骨骼發育異常，一般認為與 BMP/CDMP1（GDF5）訊號傳遞缺陷有關。輸入資料中沒有任何內容把前列腺素合成抑制和這條路徑連起來。因此，**目前找不到有依據的機轉連結**。99.99% 的高分只代表模型輸出，沒有臨床或文獻佐證。

同批的前 5 名預測還包括指趾短小併指症候群、眼缺損小眼畸形併肢根型發育不良症候群、短軀幹併釉質發育不全症候群，以及肌硬化症 (myosclerosis)。這些預測也都沒有試驗或文獻支持。前四者是先天結構發育疾病，NSAID 不太可能改變其病程。肌硬化症頂多只能推測 NSAID 可緩解疼痛或發炎，那是症狀處理，並非疾病修飾。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68354 | SULAN TABLETS 100MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-64202 | FUKON TABLETS 50MG | HITPHARM PHARMACEUTICAL CO LTD |
| HK-61431 | STREPFEN HONEY & LEMON LOZENGE 8.75MG | RECKITT BENCKISER HONG KONG LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻支持，證據等級只有 L5，且找不到有依據的機轉連結。
- 原廠仿單的警語與禁忌症資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認原適應症、警語與禁忌症。
- 補齊 Flurbiprofen 的作用機轉資料，例如從 DrugBank 查詢。
- 釐清 COX 抑制與 BMP/GDF5 訊號或骨骼發育之間是否有機轉關聯，可先做前臨床或機轉文獻回顧。
- 若機轉找不到關聯，建議不再往此適應症推進，改看其他預測。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

