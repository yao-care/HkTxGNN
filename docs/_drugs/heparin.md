---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 2
---

# Heparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Heparin：從抗凝治療到先天性蛋白C缺乏症（自體隱性）

## 一句話總結

Heparin 是臨床廣泛使用的抗凝劑，透過增強 Antithrombin III 活性來阻斷凝血瀑布。TxGNN 模型預測它可能對**先天性蛋白C缺乏症，自體隱性遺傳型（thrombophilia due to protein C deficiency, autosomal recessive）** 有效，惟目前資料集中**無相關臨床試驗或文獻**，推測為資料收集缺口，而非真實證據缺乏。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗凝治療（香港無許可證資料） |
| 預測新適應症 | 先天性蛋白C缺乏症，自體隱性 (thrombophilia due to protein C deficiency, autosomal recessive) |
| TxGNN 預測分數 | 99.29% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據已知資訊，Heparin 是臨床廣泛使用的抗凝劑，透過與 **Antithrombin III（AT-III）** 結合並大幅增強其活性，間接抑制 **Thrombin（Factor IIa）** 及 **Factor Xa**，從而阻斷凝血瀑布的關鍵節點。

**先天性蛋白C缺乏症（自體隱性、同合子型）** 是一種嚴重的遺傳性高凝狀態。Protein C 是重要的天然抗凝蛋白，正常情況下可分解並抑制活化的 Factor Va 及 Factor VIIIa；當 Protein C 嚴重缺乏時，這條負回饋被打斷，患者——尤其是新生兒——可能出現**新生兒紫癜性暴發症（purpura fulminans）** 等危及生命的廣泛性血栓事件。

在機轉上，Heparin 透過 AT-III 路徑提供**旁路抗凝補償**，能緩解 Protein C 缺乏所造成的高凝環境。臨床實務中，急性血栓發作時確有使用 Heparin 的依據。TxGNN 高預測分數（0.9929）很可能反映此機轉合理性；資料集中無收錄文獻可能屬收集缺口，建議針對性補充搜尋。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

本藥物目前在香港無已登記之許可證，無法提供核准適應症資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
雖然 Heparin 用於蛋白C缺乏症急性血栓事件具機轉合理性，臨床實務亦有零星使用依據，但本資料集中無任何臨床試驗或文獻支持，證據等級僅為 L5（純模型預測）；加上香港現無上市許可、MOA 及安全性資料均為缺口，目前不具備推進條件。

**若要推進需要：**
- 針對性補充文獻搜尋：以「protein C deficiency AND heparin」、「purpura fulminans AND anticoagulation」為關鍵字搜尋 PubMed，補充個案報告與病例系列
- 取得 MOA 詳細資料（DrugBank API 查詢 DB01109）
- 下載原廠仿單 PDF 解析主要警語及禁忌症（DG001 Blocking 缺口）
- 確認香港衛生署藥物辦公室是否有 Heparin 製品（注射劑）的上市登記
- 評估與蛋白C濃縮製劑（Protein C concentrate）及新鮮冷凍血漿（FFP）的聯合治療可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

