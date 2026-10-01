---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 598
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Naproxen：從消炎止痛到 Brachydactyly-Syndactyly 症候群

## 一句話總結

Naproxen 是非類固醇消炎止痛藥（NSAID），透過抑制 COX 酵素減少前列腺素造成的發炎與疼痛。
TxGNN 模型預測它可能對**短指併指症候群 (Brachydactyly-Syndactyly Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持，也找不到合理的機轉連結，僅屬模型推測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 短指併指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 99.35%（全體排名第 10,858） |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Naproxen 是非選擇性 COX-1/COX-2 抑制劑，主要作用是降低前列腺素介導的發炎與疼痛。

短指併指症候群是罕見的先天性肢體畸形，成因屬於基因與發育異常。抑制前列腺素合成，預期無法改變這類疾病的病程。

因此，**目前找不到合理的機轉連結**。0.9935 的高分只是知識圖譜的計算結果，缺乏生物學依據與臨床資料支持，不應把高分當成有效的證據。長期使用 NSAID 還有腸胃道、腎臟與心血管風險。

其他三個預測適應症同樣屬於罕見先天性或遺傳性骨骼發育異常，同樣找不到機轉連結，也沒有任何試驗或文獻：

| 排名 | 預測適應症 | TxGNN 分數 |
|------|-----------|-----------|
| 2 | 眼缺損小眼畸形-肢根型發育不良症候群 (Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome) | 99.22% |
| 3 | 肢中節發育不良 Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type) | 99.17% |
| 4 | 短軀幹-牙釉質發育不全症候群 (Brachyolmia-Amelogenesis Imperfecta Syndrome) | 99.06% |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Naproxen 在香港共有 20 張許可證，以下列出 5 張：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43951 | SOREN TAB 275MG | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-65797 | NAPROXEN TABLETS 250MG | PRUDENTLINK LIMITED |
| HK-56618 | SYN-NAPROXEN TAB 250MG | SYNCO (H.K.) LIMITED |
| HK-68279 | SELADIN TABLETS 250MG | YUNG SHIN CO LTD |
| HK-44905 | NAPXEN TAB 250MG | APT PHARMA LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數（L5），沒有任何臨床試驗或文獻，也找不到合理的機轉連結。
- 目標疾病是基因與發育起源的罕見畸形，COX 抑制無法針對其成因，而長期使用 NSAID 的風險反而確定存在。

**若要推進需要：**
- 找出 Naproxen（或 COX/前列腺素路徑）與該疾病之間的生物學關聯，例如相關基因或訊號路徑的機轉研究
- 前臨床或病例層級的證據，用以支持任何療效假設
- 補齊香港衛生署仿單的警語與禁忌資料，並完成完整的安全性評估
- 補充 DrugBank 的作用機轉資料

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

