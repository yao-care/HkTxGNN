---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic acid：從（原適應症資料缺失）到 Papillary Conjunctivitis

## 一句話總結

Salicylic acid（水楊酸）目前**未在香港上市**，原始適應症與作用機轉（MOA）資料均缺失。
TxGNN 模型預測乳頭狀結膜炎（Papillary Conjunctivitis）為最高分候選（**99.88%**），
但目前**無任何臨床試驗或文獻**支持這個方向，證據等級為 **L5（僅模型預測）**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（未上市，無許可證核准適應症紀錄） |
| 預測新適應症 | Papillary Conjunctivitis |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Salicylic acid 具有弱抗發炎與角質溶解作用，理論上可能緩解結膜表面發炎，
但由於藥物未上市、原始適應症與 MOA 資料均缺失，無法建立可信的機轉鏈。TxGNN 高分較可能反映知識圖譜中
「藥物—發炎相關節點」的一般性連結，而非針對該適應症的特異性療效證據。

值得注意的是，本次 TxGNN 排名前 10 的候選適應症中，多數（如 brachydactyly-syndactyly syndrome、
pseudoachondroplasia、acromesomelic dysplasia 等）為單基因遺傳性骨骼/發育異常症候群，
其病理機轉（BMP/FGF 訊息路徑、COMP/GDF5 基因突變等）與水楊酸已知藥理作用（COX 抑制、角質溶解）
完全無交集，Evidence Pack 本身也將這些候選標記為「知識圖譜偽陽性/預測雜訊」。這顯示此次預測結果的
整體訊號品質偏弱，Rank 1（papillary conjunctivitis）與 Rank 5、10 雖機轉上略具合理性，仍需視為
假說階段，不足以支持任何臨床推進。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

Salicylic acid 目前未在香港取得許可證，無上市品項紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA/香港仿單警語與禁忌症資料目前缺失（Data Gap，標記為 Blocking），已影響此候選進入下一階段安全性初評（S1）的可行性。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 藥物未上市、無 MOA 資料、無任何臨床試驗或文獻支持，僅有 TxGNN 模型分數（L5），證據強度不足以支持進一步評估。
- 排名前 10 的候選適應症中多數為與水楊酸機轉無關的罕見遺傳症候群，顯示此次預測結果訊號品質偏弱，需審慎看待。

**若要推進需要：**
- 補齊 Salicylic acid 的作用機轉（MOA）資料（DrugBank API 查詢）
- 取得原廠仿单警語與禁忌症（TFDA/香港衛生署），解除 Blocking 等級的資料缺口
- 針對 Rank 1（papillary conjunctivitis）與 Rank 5（rosacea conjunctivitis）等機轉相對合理的候選，優先搜尋是否有局部水楊酸用於眼周/結膜發炎的前臨床或個案報告證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

