---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
---

# Imatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Imatinib：從原適應症（資料未提供）到心臟纖維肉瘤

## 一句話總結

Imatinib 是一種酪胺酸激酶抑制劑，在香港已有 18 張許可證，但本次資料未提供其原適應症。
TxGNN 模型預測它可能對**心臟纖維肉瘤 (Heart Fibrosarcoma)** 有效。
目前**沒有臨床試驗和文獻**支持，這只是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 心臟纖維肉瘤 (Heart Fibrosarcoma) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，DrugBank 資料中未收錄 Imatinib 的 MOA。
其他預測項目引用的文獻描述 Imatinib 為 KIT、PDGFR 與 ABL 等酪胺酸激酶的抑制劑。

這個預測的高分主要來自知識圖譜中，心臟纖維肉瘤與其他纖維肉瘤相關疾病的距離很近。
本次沒有檢索到任何試驗或文獻，無法證明 Imatinib 對這個疾病有效。
以現有資料來看，此預測不足以支持臨床使用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 18 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62351 | IMAKREBIN FILM-COATED TABLETS 400MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-65126 | IMATINIB-AFT CAPSULES 400MG | DKSH HONG KONG LIMITED |
| HK-64502 | PMS-IMATINIB TABLETS 100MG | TRENTON-BOMA LTD |
| HK-64829 | LEUKOVEC TABLETS 100MG | LSB (HK) LIMITED |
| HK-63407 | ACCORD IMATINIB TABLET 400MG | I & C (HONG KONG) LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑） |

其餘項目（骨髓抑制風險、致吐性、監測項目、處置防護）請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
心臟纖維肉瘤沒有任何臨床試驗或文獻支持，證據等級只有 L5。香港仿單的警語與禁忌症資料也尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與適應症資料
- 補充 DrugBank 的作用機轉資料
- 針對心臟纖維肉瘤重新檢索試驗與文獻，確認是否有直接證據
- 同一份資料中，「纖維母細胞腫瘤 (fibroblastic neoplasm)」的證據較充分，主要是隆突性皮膚纖維肉瘤 (DFSP) 的指引與綜述，證據等級為 L2。建議另行評估該適應症

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

