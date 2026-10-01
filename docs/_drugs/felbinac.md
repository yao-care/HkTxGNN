---
layout: default
title: Felbinac
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 5
---

# Felbinac
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

# Felbinac：從外用非類固醇消炎藥到 Brachyolmia-Amelogenesis Imperfecta 症候群

## 一句話總結

Felbinac 是外用非類固醇消炎藥（NSAID，COX 抑制劑），為 fenbufen 的活性代謝物，香港有 1 張上市許可證。
TxGNN 模型預測它可能對**Brachyolmia-Amelogenesis Imperfecta 症候群**有效，但目前**0 個臨床試驗、0 篇文獻**支持，僅有模型分數，機轉上也找不到合理的關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症（藥理上屬外用消炎止痛） |
| 預測新適應症 | Brachyolmia-Amelogenesis Imperfecta 症候群 |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Felbinac 已知是外用 NSAID，透過抑制 COX 酶減少前列腺素合成，用於局部疼痛與發炎。

這個預測的機轉關聯薄弱。Brachyolmia-Amelogenesis Imperfecta 症候群是罕見的遺傳性骨骼與牙齒發育疾病，病因在發育過程，不在 COX 介導的發炎。COX 抑制無法針對其病理機轉。99.99% 的分數只是知識圖譜的推論，沒有任何臨床或文獻佐證，應視為訊號待查，不能當成療效依據。

同一批預測中的其他候選也是如此：

| 排名 | 預測疾病 | 分數 | 評估 |
|------|---------|------|------|
| 2 | Acromesomelic dysplasia, Hunter-Thompson type | 99.99% | 罕見骨骼發育不良，無機轉關聯，最多能緩解肌肉骨骼疼痛 |
| 3 | Myosclerosis | 99.99% | 罕見遺傳性肌病，僅可能局部緩解疼痛，不會改變病程 |
| 4 | Brachyolmia | 99.99% | 罕見骨骼發育不良，無機轉關聯 |
| 5 | Pseudoachondroplasia | 99.99% | 早發關節痛可能有症狀緩解效果，屬症狀處理，不是疾病修飾 |

這些預測都屬 L5、Hold。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56207 | SUPER STRONG AMMELTZ FELBINA-ACE LIQUID | 未載明 | 未載明 |

持證商為小林製藥（香港）有限公司（Kobayashi Pharmaceutical (Hong Kong) Company Limited）。

## 安全性考量

安全性資訊請參考原廠仿單。DrugBank 查無藥物交互作用紀錄。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型分數，沒有任何臨床試驗或文獻支持，證據等級為 L5。
- 病因是發育異常，COX 抑制沒有合理的機轉關聯。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症。
- 補齊 DrugBank 的作用機轉資料。
- 有實際的機轉或前臨床證據，說明 Felbinac 與該疾病病理的關係。
- 確認給藥途徑是否相容（外用劑型與疾病所需途徑）。
- 若只是要緩解相關疾病的疼痛，應另立為症狀治療議題評估，不屬於老藥新用。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

