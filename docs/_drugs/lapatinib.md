---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 501
evidence_level: L5
indication_count: 1
---

# Lapatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Lapatinib：從 HER2 陽性乳癌到隆突性皮膚纖維肉瘤

## 一句話總結

Lapatinib 是一種可逆性 EGFR/HER2 雙重酪胺酸激酶抑制劑，屬於標靶抗癌藥（此為一般藥理知識，輸入資料未載明原適應症）。
TxGNN 模型預測它可能對**隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma Protuberans, DFSP)** 有效。
目前**沒有臨床試驗**，也**沒有文獻**支持這個方向，只有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明（依一般藥理知識，為 HER2 陽性乳癌） |
| 預測新適應症 | 隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma Protuberans) |
| TxGNN 預測分數 | 99.30% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，下列說明來自一般藥理知識，並非輸入資料所提供。Lapatinib 是可逆性的 EGFR/HER2 雙重酪胺酸激酶抑制劑。

DFSP 通常由 COL1A1-PDGFB 融合基因驅動，會造成 PDGFRB 的自分泌活化。已確立的標靶治療是 imatinib，它是 PDGFR 抑制劑。Lapatinib 並不是主要的 PDGFR 抑制劑，所以兩者之間即使有關聯也只是間接的，例如受體酪胺酸激酶訊號路徑之間的交叉對話。

TxGNN 分數很高（99.30%），但它只是知識圖譜的預測結果。本資料集中沒有任何臨床或文獻證據可以佐證，因此這個預測目前只能視為待驗證的假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-66822 | LAPATINIB TABLETS 250MG | CHEMILL PHARMA LIMITED |
| HK-67443 | TYKERB TABLETS 250MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-56194 | TYKERB TAB 250MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑，依一般藥理知識判斷） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有 TxGNN 模型預測，沒有任何臨床試驗或文獻支持。
- 作用機轉上，DFSP 的主要驅動因子是 PDGFRB，而 lapatinib 不是 PDGFR 抑制劑，兩者的關聯只是間接的。
- 香港安全性資料尚未取得，目前無法進入安全性篩選。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料（阻擋性缺口）。
- 從 DrugBank 取得 lapatinib 的作用機轉資料。
- 檢索 lapatinib 與 DFSP 的前臨床研究（如細胞株、動物模型）及臨床文獻，確認是否有實質證據。
- 評估與 imatinib 等已確立標靶療法相比，lapatinib 是否有潛在優勢。
- 補充適應症、劑型等香港許可證欄位。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

