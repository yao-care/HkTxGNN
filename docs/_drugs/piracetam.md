---
layout: default
title: Piracetam
parent: 僅模型預測 (L5)
nav_order: 591
evidence_level: L5
indication_count: 10
---

# Piracetam
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

# Piracetam：原適應症資料缺失，TxGNN 預測骨關節炎 (Osteoarthritis)

## 一句話總結

Piracetam（DB09210）目前在本 Evidence Pack 中沒有原適應症與作用機轉（MOA）紀錄，且尚未在市場上市。
TxGNN 模型預測其可能對**骨關節炎 (Osteoarthritis)** 有效，分數高達 98.45%，
但目前**沒有臨床試驗、沒有文獻**支持這個方向，僅為知識圖譜嵌入相似性的預測結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（未提供原適應症紀錄） |
| 預測新適應症 | Osteoarthritis（骨關節炎） |
| TxGNN 預測分數 | 98.45%（圖譜排名 22,518） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，也沒有原適應症紀錄可供比對，因此無法從機轉角度驗證這個預測。
根據 Evidence Pack 本身附帶的分析，此預測「Piracetam 無已知抗發炎或軟骨保護機轉紀錄，純為 TxGNN 圖譜預測」，
換言之這個分數反映的是藥物與疾病在知識圖譜嵌入空間中的相似性，而非真實的生物學關聯。

值得注意的是，本次列出的前 10 個候選適應症中，有多筆為罕見骨骼遺傳疾病
（如 pseudoachondroplasia、brachyolmia、acromesomelic dysplasia、myosclerosis），
Evidence Pack 已標註這些候選「疑似圖譜鄰近節點聚集造成的預測偏誤」。
這種聚集現象進一步降低了整體候選名單（含排名第一的骨關節炎）的可信度，
建議在缺乏機轉與人體資料的情況下，將此類預測視為探索性訊號，而非可推進的候選。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

> 補充說明：本次查詢的 10 個候選適應症中，僅「hepatic porphyria」（排名第 5，分數 97.55%）查得 4 篇文獻，
> 但皆為 Levetiracetam（另一藥物）於卟啉症患者的癲癇治療案例報告，與 Piracetam 或骨關節炎無直接關聯，
> Evidence Pack 也註記「無法建立機轉連結」。

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語/禁忌尚未取得，列為 Blocking 資料缺口）

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的骨關節炎預測缺乏機轉、臨床試驗與文獻三方支持，證據等級僅 L5。
- 候選名單中多筆罕見骨骼遺傳疾病同群出現，顯示可能為圖譜嵌入偏誤而非真實訊號。
- 藥物本身缺乏 MOA 與原適應症資料，且尚未上市，無法進行安全性初評（S1）。

**若要推進需要：**
- 取得 TFDA/原廠仿單警語與禁忌資料（DG001，Blocking）
- 補齊 DrugBank 作用機轉（MOA）資料（DG002，High）
- 針對骨關節炎方向補做機轉文獻搜尋或前臨床研究，確認是否有生物學基礎
- 若持續無機轉或人體資料佐證，建議將此候選降低優先序，不投入後續資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

