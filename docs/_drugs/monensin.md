---
layout: default
title: Monensin
parent: 僅模型預測 (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
---

# Monensin
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

# Monensin：原適應症資料缺乏，預測可能適用於胃食道逆流症

## 一句話總結

Monensin（DrugBank ID: DB11430）目前無原始適應症與作用機轉資料可查，且未在香港取得任何藥品許可證。
TxGNN 模型列出的 10 個候選適應症中，排名最高者為**胃食道逆流症 (Gastroesophageal Reflux Disease)**，
但 TxGNN 分數僅 **50%**（接近隨機基線，全域排名約第 209 萬名），且**無任何臨床試驗或文獻支持**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（未記錄原始適應症） |
| 預測新適應症 | 胃食道逆流症 (Gastroesophageal Reflux Disease) |
| TxGNN 預測分數 | 50.00%（全域排名約 2,091,003） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Monensin 詳細的作用機轉資料，無法從藥理路徑驗證其與胃食道逆流症的關聯性。

Evidence Pack 中對此預測的機轉評估本身已明確標示為推測性質：Monensin 為 Na+/H+ 離子載體，
理論上可能影響上皮細胞的離子梯度，但**沒有任何體內或體外實驗資料**支持其對胃食道逆流症有效，
且該藥物已知具有心臟毒性風險，人體給藥安全性堪慮。這個連結純屬知識圖譜的統計性推論，
尚未有機轉層級的實證支持。

此外，本次列出的其他 9 個候選適應症（如 primary biliary cholangitis、Behcet disease 等）機轉關聯性同樣薄弱；
其中部分候選（如「beta-amino acids, renal transport of」「B-cell growth factor」「primary basilar invagination」）
實際上是生理現象或生長因子，而非疾病實體，疑似知識圖譜節點映射錯誤，不具臨床評估意義。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Monensin 目前**未在香港取得任何藥品許可證**（許可證數：0），無核准適應症或劑型資料可提供。

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語與禁忌資料缺失，已列為 Blocking 等級資料缺口，
在補齊前無法進入 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，10 個候選適應症均無臨床試驗或文獻支持，TxGNN 分數接近隨機基線（50%，排名約第 209 萬）。
- 藥物層級關鍵資料（MOA、仿單警語/禁忌）均缺失，其中安全性資料缺口已被標記為 Blocking，無法進行初步安全性評估。
- 該藥物未在香港上市，且候選清單中多筆疑似為知識圖譜節點映射錯誤（非真實疾病實體），整體清單品質有疑慮。

**若要推進需要：**
- 向 DrugBank 補查 Monensin 的作用機轉（MOA）資料
- 取得 TFDA／HK 相關仿單警語與禁忌症資料，解除 Blocking 缺口
- 針對排名第 1 的胃食道逆流症預測，另行搜尋是否有動物實驗或體外機轉研究可佐證
- 檢視並剔除候選清單中非疾病實體的節點映射錯誤項目
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

