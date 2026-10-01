---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 902
evidence_level: L5
indication_count: 2
---

# Upadacitinib
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

# Upadacitinib：從免疫介導疾病到眼缺損小眼畸形-肢根型骨發育不良症候群

## 一句話總結

Upadacitinib 是選擇性 JAK1 抑制劑，用於免疫介導的發炎性疾病。
TxGNN 模型預測它可能對**眼缺損小眼畸形-肢根型骨發育不良症候群 (Colobomatous microphthalmia-rhizomelic dysplasia syndrome)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測，且機轉上找不到合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 眼缺損小眼畸形-肢根型骨發育不良症候群 (Colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| TxGNN 預測分數 | 99.61%（排名 7549） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Upadacitinib 屬於 JAK 抑制劑，一般認為它透過抑制 JAK1 來減弱 JAK-STAT 細胞激素訊號，用於免疫介導的發炎性疾病。

這個預測在機轉上**不成立**。預測的疾病是極罕見的先天發育症候群，表現為眼部缺損／小眼症合併肢根型肢體發育不良。它被認為源自形態發生的基因缺陷，而不是持續進行的發炎。出生時已存在的結構性畸形，也不太可能靠出生後的免疫調節逆轉。

0.996 的高分只是模型輸出，很可能來自知識圖譜的連結特性（connectivity artifact），不能當作療效證據。藥物資料中缺少原適應症和 MOA，也無法拿已知藥理來交叉驗證。

模型的第二個預測是**短指－併指症候群 (Brachydactyly-syndactyly syndrome)**，分數 99.58%。它同樣是先天肢體畸形，同樣沒有機轉連結和任何證據，結論相同。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66872 | RINVOQ PROLONGED-RELEASE TABLETS 15MG | ABBVIE LIMITED |
| HK-67512 | RINVOQ PROLONGED-RELEASE TABLETS 30MG | ABBVIE LIMITED |
| HK-68084 | RINVOQ PROLONGED-RELEASE TABLETS 45MG | ABBVIE LIMITED |

資料庫未提供這些許可證的劑型和核准適應症文字。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有模型預測，沒有臨床試驗和文獻。
- 預測疾病是先天結構性畸形，與 JAK1 抑制的藥理作用沒有可辨識的關聯，高分很可能是模型假象。

**若要推進需要：**
- 從 DrugBank 補齊 Upadacitinib 的 MOA 與原適應症。
- 從香港衛生署取得仿單，補上警語與禁忌症。
- 提出此症候群與 JAK-STAT 發炎路徑相關的生物學依據。目前看不到，若無法提出，建議不再投入。
- 取得任何病例報告或前臨床資料，再重新評估。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

