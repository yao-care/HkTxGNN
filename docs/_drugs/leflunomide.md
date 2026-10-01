---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 507
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Leflunomide：從（原適應症資料缺漏）到指趾短小併指症候群

## 一句話總結

Leflunomide 在香港已上市，但本次資料未載明原適應症。
TxGNN 模型預測它可能對**指趾短小併指症候群 (Brachydactyly-Syndactyly Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型分數。
這個預測更像是**潛在的安全性警訊**，不是療效訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 指趾短小併指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 99.93%（排名 1992） |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Hold |

另一個預測適應症是**眼缺損小眼畸形－根段肢體發育不良症候群 (Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome)**，分數 99.93%（排名 2049），同樣是 L5、Hold。

---

## 為什麼這個預測合理？

Leflunomide（其活性代謝物為 teriflunomide）會抑制 DHODH 酶，進而阻斷嘧啶的從頭合成，屬於免疫調節機轉。

指趾短小併指症候群是先天性肢體畸形，從這個機轉看不出合理的治療關聯。DHODH 功能喪失會造成 Miller 症候群（肢體與顏面畸形），而 leflunomide 是已知的致畸胎藥物。因此圖譜上的關聯，較可能反映兩者共享的發育路徑，而不是治療效果。

第二個預測（眼缺損小眼畸形－根段肢體發育不良症候群）也是罕見的先天發育異常。Leflunomide 的抗增生與免疫調節作用與其病理沒有已知關聯，這個連結很可能是知識圖譜中共同發育基因或表型鄰居造成的假象。

目前缺乏原適應症與詳細作用機轉的完整資料，機轉驗證並不完整。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

共 15 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67308 | LEFLUNOMIDE TABLETS 10MG | I & C (HONG KONG) LIMITED |
| HK-67309 | LEFLUNOMIDE TABLETS 20MG | I & C (HONG KONG) LIMITED |
| HK-54040 | APO-LEFLUNOMIDE TAB 20MG | HIND WING CO LTD |
| HK-58159 | PMS-LEFLUNOMIDE TAB 10MG | TRENTON-BOMA LTD |
| HK-46487 | ARAVA TAB 20MG | SANOFI HONG KONG LIMITED |

---

## 安全性考量

- **致畸胎風險（機轉推論）**：抑制嘧啶合成可能干擾胚胎發育，leflunomide 是已知致畸胎藥物。用於先天發育異常相關適應症時，這是首要顧慮。

其餘警語、禁忌症與藥物交互作用資料目前皆無。安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據只有模型分數，沒有臨床試驗或文獻，屬 L5。
- 機轉上找不到合理的治療關聯，反而有致畸胎的安全性顧慮，這個預測應視為警訊而非療效線索。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌症，這是進入安全性篩選的前提。
- 補齊 DrugBank 的作用機轉資料與原適應症。
- 用 DHODH 與相關發育基因的角度，檢視圖譜關聯是否為假象。
- 在出現實際臨床或前臨床證據之前，不建議投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

