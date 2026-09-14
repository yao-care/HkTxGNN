---
layout: default
title: Siponimod
parent: 僅模型預測 (L5)
nav_order: 689
evidence_level: L5
indication_count: 10
---

# Siponimod
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

# Siponimod：從（原適應症資料缺）到 肺動脈高壓

## 一句話總結

> Siponimod（DrugBank ID: DB12371）目前在香港**未上市**，原始適應症與作用機轉資料均未收錄於本次證據包。
> TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，
> 但這僅是**純模型預測分數**，目前**無任何臨床試驗或文獻**直接支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺（原始適應症與 MOA 均未收錄於本次證據包） |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L5（僅有模型預測分數，無臨床試驗或文獻佐證） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Siponimod 正式的作用機轉（MOA）資料與原適應症紀錄。根據本證據包中預測適應症的機轉關聯分析（repurposing_rationale）所提供的資訊，Siponimod 為 **S1P1/S1P5（sphingosine-1-phosphate receptor 1 及 5）選擇性調節劑**。

S1P 訊號路徑在理論上與血管內皮及平滑肌張力調控有關，這是 TxGNN 將 Siponimod 與肺動脈高壓連結的機轉依據。但需明確指出：**這僅是理論上的機轉合理性，目前沒有任何直接文獻或臨床試驗支持 Siponimod 用於肺動脈高壓**，屬於純預測分數（L5），臨床證據等級最低。

值得一提的是，本證據包共列出 10 個預測適應症，其中**僅類風濕性關節炎（rheumatoid arthritis, rank 7）達到較高的決策階段（S1／Research Question）**，該候選有文獻（PMID 33983615）明確討論 S1P 受體調節劑類藥物於多發性硬化症以外自體免疫疾病的應用潛力，機轉論證較肺動脈高壓完整，但同樣缺乏 Siponimod 直接用於 RA 的臨床證據。其餘候選（如 kyphoscoliotic heart disease、atrophoderma vermiculata、myelodysplastic syndrome 等）經評估後判定為知識圖譜雜訊（false positive），無機轉或證據支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Siponimod 目前於香港**未上市**，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（註：TFDA/仿單警語與禁忌症資料為本評估的阻斷性資料缺口，缺乏此資料無法進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
肺動脈高壓的預測雖然 TxGNN 分數極高（99.68%），但證據等級僅 L5——完全沒有臨床試驗或文獻支持，且原始適應症、MOA、仿單安全性資料均缺失，尚不足以支持任何推進行動。

**若要推進需要：**
- 補齊 Siponimod 原始適應症與正式 MOA 資料（DrugBank/原廠仿單）
- 取得仿單警語與禁忌症資料，完成 S1 安全性初評（目前為阻斷性缺口）
- 若優先追蹤預測方向，建議轉向證據較完整的類風濕性關節炎候選（L4／S1），並補充 Siponimod 於自體免疫疾病的臨床前或個案研究資料
- 針對肺動脈高壓方向，需先有動物模型或機轉研究（達到 L4）才建議進一步評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

