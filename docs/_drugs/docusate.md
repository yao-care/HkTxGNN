---
layout: default
title: Docusate
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 2
---

# Docusate
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

# Docusate：從便秘（糞便軟化劑）到 Plummer-Vinson 症候群

## 一句話總結

Docusate 是一種陰離子界面活性劑類的糞便軟化劑，一般用於緩解便秘。
TxGNN 模型預測它可能對 **Plummer-Vinson 症候群 (Plummer-Vinson syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | Plummer-Vinson 症候群 (Plummer-Vinson syndrome) |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Docusate 一般被認為是界面活性劑型的糞便軟化劑。
但提供的資料中，沒有任何內容能把它連到 Plummer-Vinson 症候群。

Plummer-Vinson 症候群的特徵是缺鐵性貧血、吞嚥困難與食道蹼。
Docusate 與鐵代謝或食道病變之間，目前查不到已知的關聯。
唯一可推測的接點是：口服鐵劑常引起便秘，臨床上有時會搭配 docusate 使用。
這屬於支持性照護，不是針對疾病本身的治療，且尚未經任何資料驗證。

TxGNN 的高分（99.18%）只是知識圖譜的計算結果，可能反映圖譜的拓撲結構，而非真實的生物學關聯。
排名第 2 的預測是「不依賴維生素 B12 與葉酸的體質性巨母紅血球性貧血」（分數 99.15%），同樣沒有機轉依據或研究佐證，應視為可能的圖譜假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 10 張含 docusate 的許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-40969 | SOFLAX CAP 100MG | TRENTON-BOMA LTD |
| HK-01672 | EAR-SOL EAR DROPS | JEAN-MARIE PHARMACAL CO LTD |
| HK-39379 | PMS-DOCUSATE SODIUM CAP 100MG | TRENTON-BOMA LTD |
| HK-15102 | WYRUTIN HAEMORRHOID CAP | NATIONAL PHARMACEUTICAL CO LTD |
| HK-65563 | COLOXYL WITH SENNA TABLETS | ASPEN PHARMACARE ASIA LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症都只有模型分數，沒有臨床試驗、文獻或可辨識的作用機轉，證據等級為 L5。
- 香港仿單的警語與禁忌資料尚未取得，無法進行安全性初篩。

**若要推進需要：**
- 取得香港衞生署的仿單，補齊警語、禁忌與核准適應症。
- 補充 docusate 的作用機轉與藥物標靶資料（如透過 DrugBank）。
- 檢索是否有 docusate 與缺鐵性貧血、食道蹼或吞嚥困難相關的研究。
- 若找不到合理的機轉連結，建議將此預測視為圖譜假象，不再投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

