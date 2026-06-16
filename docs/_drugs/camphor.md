---
layout: default
title: Camphor
parent: 中證據等級 (L3-L4)
nav_order: 129
evidence_level: L4
indication_count: 10
---

# Camphor
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Camphor（樟腦）：從局部外用鎮痛到偏頭痛

## 一句話總結

Camphor（樟腦）是歷史悠久的傳統外用藥物，以局部鎮痛、清涼消炎著稱，但目前在香港無正式藥品許可。
TxGNN 模型預測它可能對**偏頭痛 (migraine disorder)** 有效，
目前有 **0 個臨床試驗**和 **5 篇文獻**（多為間接或反向證據）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 傳統局部外用鎮痛／清涼消炎（香港無正式上市許可） |
| 預測新適應症 | 偏頭痛 (migraine disorder) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

樟腦（Camphor）是一種萜類化合物，藥理上為 **TRPV1 部分激動劑**，可調控三叉神經的痛覺傳導。偏頭痛的發作機制涉及三叉神經血管系統的活化，因此兩者在理論上存在生物學交集。

樟腦同時活化 **TRPM8（冷感受器）**，產生局部清涼感與鎮痛效果。此外，其對 Nav（電壓門控鈉離子通道）的輕微阻斷作用，理論上類似某些偏頭痛預防藥物的部分機轉。

然而，上述機轉目前缺乏直接的人體臨床研究驗證。更關鍵的是，樟腦全身性給藥（口服或系統性暴露）的**安全窗口極窄**，高劑量可引發中樞神經過度興奮乃至癲癇，使任何全身性用藥路徑面臨嚴重安全障礙。現有文獻亦出現**反向訊號**（見下方文獻表）。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case Report | BMJ Case Reports | ⚠️ **反向訊號**：含樟腦與桉油精牙膏與叢集性頭痛發作有時序關聯，提示樟腦可能誘發或加重頭痛 |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case Series | Headache | 五例因含促驚厥精油牙膏引發叢集性頭痛之案例系列，樟腦為可能致病成分之一 |
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | RCT | The Journal of Headache and Pain | Erenumab Phase 3 亞洲慢性偏頭痛研究（DRAGON study）；與樟腦無直接關聯，為背景對照文獻 |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Historical Review | Z Kinder Jugendpsychiatr Psychother | 1940–50 年代兒少神經精神藥理學歷史回顧；樟腦曾被用於多種神經症狀，但無偏頭痛特定療效數據 |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Historical/Case | Minerva Medica | 偏側頭痛（essential hemicrania）療法歷史案例；摘要不可取得，細節無從評估 |

---

## 香港上市資訊

Camphor 在香港目前無正式藥品上市許可（衛生署許可證數：0 張），無法從現有核准適應症推論監管可行性。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **文獻衍生安全警示（非仿單資料）：**
>
> - 樟腦為已知**促驚厥劑（convulsant）**，可降低癲癇閾值，對具偏頭痛與癲癇共病傾向之患者存在潛在危害
> - 口服急性毒性研究（PMID 27955803）顯示，口服樟腦可對多個器官造成氧化壓力及組織病理損傷
> - 外用含樟腦產品（如牙膏）已有誘發叢集性頭痛的案例報告（PMID 34373243、35856604）
> - 歷史上樟腦被視為**抗催情劑**（anti-aphrodisiac），全身性使用之安全性疑慮有據可查

---

## 結論與下一步

**決策：Hold**

**理由：**
樟腦對偏頭痛的機轉連結僅停留在理論層面（TRPV1/TRPM8 三叉神經調控），現有文獻多為間接證據，且出現**負向訊號**（樟腦可能誘發或加重頭痛），加上促驚厥毒性使全身性給藥路徑不可行，目前不具備進入臨床評估的條件。

**若要重新評估需要：**

- 建立樟腦在三叉神經 TRPV1/TRPM8 路徑上的動物模型驗證（前臨床必要步驟）
- 開發靶向局部給藥系統（如鼻腔凝膠、穴位貼片），以繞過全身毒性障礙並確立治療劑量窗口
- 排除「樟腦誘發頭痛」與「樟腦緩解偏頭痛」兩種相悖訊號的機轉差異
- 取得 MOA 完整數據（DrugBank API 查詢）及香港仿單安全性資料，以補齊 DG001/DG002 資料缺口後重新評分
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

