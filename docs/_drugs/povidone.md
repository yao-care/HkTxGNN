---
layout: default
title: Povidone
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 1
---

# Povidone
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

# Povidone：從皮膚消毒到先天性魚鱗癬樣紅皮症

## 一句話總結

Povidone（聚維酮）本身並非具有明確藥理作用的活性藥物，而是常作為藥物製劑賦形劑，或與碘複合成 povidone-iodine 用於體表消毒殺菌。TxGNN 模型預測它可能對**先天性魚鱗癬樣紅皮症 (Congenital Ichthyosiform Erythroderma)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，證據等級僅為最低的 L5。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無明確適應症（作為賦形劑／體表消毒劑使用） |
| 預測新適應症 | 先天性魚鱗癬樣紅皮症 (Congenital Ichthyosiform Erythroderma) |
| TxGNN 預測分數 | 99.11%（排名第 14,108 位） |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Povidone 詳細的作用機轉資料（original_moa 標註為 [Data Gap]）。根據已知資訊，Povidone 本質上是一種惰性高分子賦形劑／黏合劑，臨床上多作為藥物製劑的載體，或與碘複合成 povidone-iodine 用於體表消毒殺菌，並沒有明確的藥理作用靶點或訊息傳遞路徑。

先天性魚鱗癬樣紅皮症屬體染色體隱性遺傳的角質化障礙，致病機轉為 ABCA12、TGM1 等角質形成相關基因突變導致表皮屏障功能異常。這與 Povidone 作為物理性賦形劑／消毒劑的定位之間，缺乏任何已知或可推論的分子機轉關聯。

換言之，TxGNN 給出的 0.9911 高分應被視為知識圖譜嵌入相似度的統計輸出，而非具生物學意義的因果訊號——尤其在完全沒有臨床試驗與文獻佐證、且藥物本身缺乏 MOA 資料的情況下，此預測關聯的可信度目前偏低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Povidone 目前於香港**未上市**，無獨立藥品許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：TFDA/香港仿單警語與禁忌資料目前缺失（DG001，Blocking），這是進入下一階段安全性初評（S1）前必須補足的項目。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測目前為 L5（僅有模型統計預測，無任何臨床試驗或文獻佐證），且機轉分析顯示 Povidone 的賦形劑／消毒劑特性與先天性魚鱗癬樣紅皮症的遺傳性角質化缺陷之間缺乏合理連結。
- 藥物本身缺乏 MOA 資料與仿單安全性資訊（Blocking Data Gap），尚不足以支持任何後續臨床評估。

**若要推進需要：**
- 補足 Povidone 的作用機轉（MOA）資料（DG002）
- 取得 TFDA／香港官方仿單警語與禁忌症資料（DG001，Blocking，目前無法進入 S1 安全性初評）
- 尋找是否有 Povidone 或 povidone-iodine 應用於皮膚屏障／角質化相關疾病的前臨床或個案研究，以驗證機轉合理性
- 在補齊上述資料前，不建議投入進一步資源於此候選適應症
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

