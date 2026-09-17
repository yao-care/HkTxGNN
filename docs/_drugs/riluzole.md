---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 650
evidence_level: L5
indication_count: 5
---

# Riluzole
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

# Riluzole：適應症資料缺失 → bilateral parasagittal parieto-occipital polymicrogyria

## 一句話總結

Riluzole（DrugBank DB00740）目前在本證據包中缺乏原適應症與作用機轉資料。
TxGNN 模型將 **bilateral parasagittal parieto-occipital polymicrogyria**（雙側矢狀旁枕葉多小腦回畸形）列為排名第一的預測適應症（分數 99.99%），
但**沒有任何臨床試驗或文獻佐證**，且模型自身的機轉推論文字明確指出此預測與 riluzole 已知藥理作用**無病理連結**，屬於低可信度候選。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（DrugBank 未提供，香港無許可證可交叉核對） |
| 預測新適應症 | bilateral parasagittal parieto-occipital polymicrogyria |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 riluzole 的正式作用機轉（MOA）欄位資料（Data Gap DG002）。但本證據包中其他候選適應症的機轉推論文字有提及：riluzole 已知具有**麩胺酸釋放抑制**及**電位依賴型鈉離子通道阻斷**作用，是目前用於下運動神經元退化性疾病（如 ALS）的核心神經保護藥物。

然而，排名第一的預測 **bilateral parasagittal parieto-occipital polymicrogyria** 屬於大腦皮質發育畸形（神經元遷移異常），與上述麩胺酸調節/鈉通道阻斷機轉**沒有已知的病理連結**。模型自身的 `repurposing_rationale` 也明確指出，這個高分很可能反映知識圖譜中「神經系統疾病」的結構性相似，而非真正的機轉特異性——換句話說，這是一個**機轉薄弱、可能屬於嵌入空間偽相關**的候選。

值得注意的是，同一批預測中排名第 3（lower motor neuron syndrome with late-adult onset）與排名第 5（lethal arthrogryposis-anterior horn cell disease syndrome）雖然 TxGNN 分數略低，但機轉推論明確指向**下運動神經元退化**，與 riluzole 的已知藥理作用高度一致，機轉合理性遠優於排名第一的候選。

---

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

本藥物目前**未在香港取得藥品許可證**（許可證數：0），無可比對之核准適應症資料。

---

## 安全性考量

安全性資料存在關鍵缺口：

- **[DG001／Blocking]** 尚未取得當地藥監機關（原始資料標示為 TFDA）之仿單警語與禁忌症，此缺口已導致本候選**無法進入 S1 安全性初評**。
- **[DG002／High]** 作用機轉（MOA）資料缺失，影響機轉關聯性分析的完整度。
- 藥物交互作用查詢結果為「not_found」，無資料可供評估。

安全性資訊請待補齊上述缺口後再行評估，暫不建議以現有資料作臨床決策依據。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症在機轉層面明確缺乏合理性，且無任何臨床試驗或文獻支持（L5／S0）。
- 存在 Blocking 等級安全性資料缺口（DG001），本候選依規則已中斷於 S1 安全性初評之前。

**若要推進需要：**
- 補齊當地藥品監管機關之仿單警語與禁忌症資料，解除 DG001 Blocking 缺口
- 透過 DrugBank API 補齊作用機轉（MOA）資料（DG002）
- 若考慮繼續此藥物的老藥新用評估，建議優先轉向機轉合理性較高的候選——**rank 3（lower motor neuron syndrome with late-adult onset）**與**rank 5（lethal arthrogryposis-anterior horn cell disease syndrome）**，兩者皆與下運動神經元退化機轉直接相關，而非本報告標題所示、機轉薄弱的 rank 1 候選
- 需完成香港藥品許可證申請流程（現況：未上市，0 張許可證）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

