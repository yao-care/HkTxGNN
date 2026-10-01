---
layout: default
title: Deferasirox
parent: 中證據等級 (L3-L4)
nav_order: 246
evidence_level: L4
indication_count: 5
---

# Deferasirox
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Deferasirox：從鐵螯合治療到 HIV 感染

## 一句話總結

Deferasirox 是口服鐵螯合劑，臨床上用於治療慢性鐵過載（此為藥物類別的通用知識，香港許可證資料中未載明適應症）。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有效。
目前**沒有臨床試驗**，只有 **2 篇文獻**，且僅為前臨床機轉研究和藥物概述，另有跡象顯示作用方向可能相反。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | HIV 感染 (HIV infectious disease) |
| TxGNN 預測分數 | 99.40% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Deferasirox 屬於鐵螯合劑，其作用是結合體內過量的鐵。機轉上是否適用於 HIV 感染，目前無法從現有資料確認。

HIV 複製與宿主的鐵狀態有關。2021 年一篇前臨床研究（PMID 34550543）指出，內溶酶體中的鐵會提高 HIV-1 Tat 蛋白的寡聚化與 β-catenin 表現，進而**抑制** Tat 介導的 HIV-1 LTR 轉錄活化。這是根據標題推斷的內容。

這帶來一個方向上的疑慮。鐵螯合劑降低細胞內鐵，理論上可能解除這種抑制，反而增加病毒轉錄活性，與治療效果相反。作用方向尚未釐清，TxGNN 的高分（0.994）目前沒有任何臨床數據支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | 前臨床／體外機轉研究 | Journal of Neurovirology | 內溶酶體鐵可抑制 Tat 介導的 HIV-1 LTR 轉錄活化，作用方向與鐵螯合可能相反 |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | 新藥概述 | J Am Pharm Assoc | ramelteon、tipranavir、nepafenac 與 deferasirox 的新藥介紹，未針對 HIV 適應症 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68031 | JADENU TABLETS 90MG | Novartis Pharmaceuticals (HK) Limited |
| HK-68030 | JADENU TABLETS 360MG | Novartis Pharmaceuticals (HK) Limited |
| HK-66517 | PMS-DEFERASIROX DISPERSIBLE TABLETS 250MG | Trenton-Boma Ltd |
| HK-64787 | JADENU TABLETS 360MG | Novartis Pharmaceuticals (HK) Limited |
| HK-64785 | JADENU TABLETS 90MG | Novartis Pharmaceuticals (HK) Limited |

共 7 張許可證，以上列出 5 張。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻僅有前臨床機轉研究與一般藥物概述，證據等級為 L4。
- 現有機轉線索顯示鐵螯合可能促進而非抑制 HIV 轉錄，在方向釐清前不建議推進。

**若要推進需要：**
- 從 DrugBank 補齊作用機轉資料。
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩檢。
- 取得體外或動物實驗數據，確認鐵螯合對 HIV 複製的作用方向。
- 若後續要檢視其他預測（如慢性 C 型肝炎），需注意現有文獻多在 β-地中海貧血患者中討論鐵過載，並非 deferasirox 的抗病毒證據。

---

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

