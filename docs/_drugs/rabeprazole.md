---
layout: default
title: Rabeprazole
parent: 僅模型預測 (L5)
nav_order: 735
evidence_level: L5
indication_count: 2
---

# Rabeprazole
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

# Rabeprazole：從胃酸相關疾病到惰性全身性肥大細胞增生症

## 一句話總結

Rabeprazole（雷貝拉唑）是質子幫浦抑制劑，在香港已有 14 張許可證。
TxGNN 模型預測它可能對**惰性（冒煙型）全身性肥大細胞增生症 (Smouldering systemic mastocytosis)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測，因此建議暫緩（Hold）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明適應症文字（依藥理類別，質子幫浦抑制劑通常用於胃酸相關疾病） |
| 預測新適應症 | 惰性（冒煙型）全身性肥大細胞增生症 (Smouldering systemic mastocytosis) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Rabeprazole 是質子幫浦抑制劑，依一般藥理知識，這類藥物可抑制胃酸分泌。

肥大細胞增生症患者的肥大細胞會釋放大量介質（如組織胺），可能造成胃酸過度分泌。臨床上，質子幫浦抑制劑可用於控制這類消化道症狀。這屬於**症狀處理，不是改變疾病本身**，而且提供的資料中沒有任何內容支持這個推論。

TxGNN 另外還預測了「伴嗜酸性白血球增多的淋巴結病變型肥大細胞增生症」（分數 99.35%）。這是罕見且侵襲性的亞型，資料中沒有具體的機轉依據。這個預測很可能只是因為在知識圖譜中與其他肥大細胞增生症節點距離相近。模型分數高不等於臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 14 張許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-58509 | PROMTO TAB 20MG | CHARIOT PHARMA LIMITED |
| HK-61618 | APO-RABEPRAZOLE ENTERIC-COATED TABLETS 20MG | HIND WING CO LTD |
| HK-61506 | RABEPRAZOLE SANDOZ GASTRO-RESISTANT TABLETS 20MG | SANDOZ HONG KONG LIMITED |
| HK-61507 | RABEPRAZOLE SANDOZ GASTRO-RESISTANT TABLETS 10MG | SANDOZ HONG KONG LIMITED |
| HK-44936 | PARIET TAB 20MG (ENTERIC-COATED) | EISAI (HONG KONG) COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症都只有 TxGNN 模型分數，沒有臨床試驗或文獻，證據等級為 L5。
- 即使機轉上可能有幫助，也只是控制胃酸相關症狀，不是治療疾病本身。

**若要推進需要：**
- 取得香港衛生署（Department of Health）核准仿單，補齊警語、禁忌症與核准適應症。
- 補充 DrugBank 的作用機轉資料。
- 系統性搜尋 PPI 用於肥大細胞增生症的文獻與臨床試驗，確認是否有症狀控制的實證。
- 若要推進，應重新定位為「症狀支持治療」，而不是疾病治療。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

