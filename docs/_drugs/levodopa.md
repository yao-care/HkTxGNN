---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# Levodopa：從多巴胺補充治療到 Rasmussen 亞急性腦炎

## 一句話總結

Levodopa 是多巴胺前驅物，臨床機轉為補充紋狀體多巴胺不足（常見於帕金森氏症相關治療），但本評估包中並未正式登錄其原適應症與 MOA 資料。TxGNN 模型預測它可能對**Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)** 有效，預測分數高達 **99.06%**，但目前**沒有任何臨床試驗、ICTRP 登記或文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（DrugBank 未提供正式登錄適應症；機轉敘述僅提及多巴胺補充相關用途） |
| 預測新適應症 | Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis) |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 標記為資料缺口）。根據評估包中提供的機轉敘述，Levodopa 經 AADC 酵素轉化為多巴胺，用於補充紋狀體多巴胺不足。

Rasmussen 亞急性腦炎屬於罕見的自體免疫／慢性發炎性單側腦炎，病理機轉為 T 細胞介導的神經元破壞與難治性癲癇，與多巴胺路徑**目前沒有已知的病理生理關聯**。

TxGNN 給出的高分（0.99）在完全缺乏試驗與文獻佐證的情況下，較可能反映知識圖譜中的間接連結（例如神經科共病節點）或資料稀疏造成的雜訊，而非真實的生物合理性。加上原適應症與 MOA 資料本身缺失，無法交叉驗證此藥物的資料完整性，此預測的可信度偏低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Levodopa 目前在香港**未上市**，無任何許可證登記，無法評估在地臨床可及性。

## 安全性考量

安全性資訊請參考原廠仿單。（本評估包中之仿單警語、禁忌症與藥物交互作用資料均未取得，屬於待補齊的關鍵缺口。）

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5（純模型預測，無任何臨床試驗或文獻佐證）
- 機轉關聯性薄弱，Rasmussen 腦炎的自體免疫病理與多巴胺路徑無已知連結
- 藥物未在香港上市，且原適應症、MOA、仿單警語與禁忌症等關鍵資料皆缺失（其中仿單安全性資料為 Blocking 等級缺口）

**若要推進需要：**
- 取得 TFDA／原廠仿單警語與禁忌症資料，完成 S1 安全性初評
- 補齊 Levodopa 的作用機轉（MOA）與正式登錄適應症資料
- 尋找 Rasmussen 腦炎相關的臨床前或機轉研究，以驗證生物合理性後再考慮是否進入下一階段
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

