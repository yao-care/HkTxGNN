---
layout: default
title: Imidacloprid
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 5
---

# Imidacloprid
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

# Imidacloprid：從獸用外寄生蟲藥（無人類適應症）到脊髓馬尾症候群

## 一句話總結

Imidacloprid 是新煙鹼類（neonicotinoid）殺蟲劑，在香港以獸用外寄生蟲產品上市，沒有登記的人類適應症。
TxGNN 模型預測它可能對**脊髓馬尾症候群 (Cauda Equina Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型分數，很可能是知識圖譜的假象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症；品名皆標示為獸用 (VET)，無人類適應症 |
| 預測新適應症 | 脊髓馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市（獸用產品） |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。就已知資訊，Imidacloprid 是作用於昆蟲菸鹼型乙醯膽鹼受體 (nAChR) 的殺蟲劑，對哺乳動物受體的親和力相對較低，在香港僅作為貓狗用的外寄生蟲滴劑。

脊髓馬尾症候群是馬尾神經根受壓迫造成的神經系統疾病。目前找不到 Imidacloprid 與這類壓迫性神經病變之間的藥理關聯，也沒有人類治療開發史。

因此，這個預測**缺乏可查證的機轉支持**。99.99% 的高分僅反映圖譜中的統計關聯，不代表藥理上合理，應視為知識圖譜假象，不宜當作研究線索。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

以下為獸用產品，許可證資料未載明劑型與適應症，共 6 張，列出其中 5 張：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-55111 | ADVANTAGE 400 SOLN 400MG/4ML (VET) | UNIPET HOUSE COMPANY LIMITED |
| HK-55109 | ADVANTAGE 250 SOLN 250MG/2.5ML (VET) | UNIPET HOUSE COMPANY LIMITED |
| HK-57257 | ADVANTAGE 40 FOR CATS SOLUTION 40MG/0.4ML (VET) | UNIPET HOUSE COMPANY LIMITED |
| HK-57256 | ADVANTAGE 80 FOR CATS SOLUTION 80MG/0.8ML (VET) | UNIPET HOUSE COMPANY LIMITED |
| HK-55110 | ADVANTAGE 100 SOLN 100MG/ML (VET) | UNIPET HOUSE COMPANY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，沒有任何臨床試驗或文獻，也沒有合理的機轉連結。
- 藥物在香港僅有獸用許可證，無人類使用史與人類安全性資料。
- 同一份預測清單的其他候選也都是 L5 / Hold。腸躁症（3 個試驗）與食道疾病（39 個試驗）的檢索結果，只是疾病關鍵字比對，沒有任何試驗測試 Imidacloprid。食道疾病唯一的文獻是獸用 Advocate（imidacloprid 加 moxidectin）滴劑治療犬食道旋尾線蟲病，不屬於人類證據。

**若要推進需要：**
- 取得香港衞生署仿單的警語與禁忌資料（目前為阻擋性缺口）。
- 補齊 DrugBank 的作用機轉資料，再重新評估與馬尾症候群的機轉關聯。
- 先有前臨床或機轉研究，才值得重新評估；沒有的話，不建議投入資源。
- 評估哺乳動物毒理學風險，確認人類使用是否可行。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

