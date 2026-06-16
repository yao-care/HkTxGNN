---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 1
---

# Caspofungin
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

# Caspofungin：從侵襲性黴菌感染到 Gastrin 分泌異常

## 一句話總結

Caspofungin 是 echinocandin 類抗黴菌藥，透過抑制真菌細胞壁合成酶發揮殺菌作用，臨床上用於侵襲性念珠菌症與麴菌感染的治療。TxGNN 模型預測它可能對 **Gastrin 分泌異常 (Gastrin Secretion Abnormality)** 有效，然而目前**沒有任何臨床試驗或文獻**支持這一方向，此預測的生物學合理性存疑。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 侵襲性念珠菌症、麴菌感染（echinocandin 類抗黴菌治療） |
| 預測新適應症 | Gastrin 分泌異常 (Gastrin Secretion Abnormality) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Caspofungin 屬 echinocandin 類抗黴菌藥，作用機轉為抑制真菌細胞壁合成所需的 **β-(1,3)-D-glucan synthase**（FKS1 基因編碼），破壞真菌細胞壁完整性而導致細胞死亡。此機轉高度針對真菌特異性靶點，與人類細胞無對應酶，故毒性相對低。

Gastrin 分泌異常涉及胃竇 G 細胞透過 **GPCR／cAMP 信號路徑**調控 gastrin 的釋放，與 Caspofungin 的直接作用靶點無任何交集。唯一可推測的**間接機轉**是：腸道 *Candida* 過度增生時，可能透過 Toll-like receptor 或腸道菌-宿主信號軸干擾 gastrin 分泌節律；理論上，抗黴治療可恢復正常分泌。

然而，此間接假說目前**尚無任何實驗或臨床資料支撐**。TxGNN 預測分數 0.9944 極可能源自知識圖譜中疾病節點的間接共現（即兩者在圖譜上距離近，但非真正的生物學關聯），而非具有轉化潛力的再利用訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Caspofungin 在香港目前**未取得上市許可**，無相關藥品登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測缺乏任何直接生物學機轉支撐，Caspofungin 的靶點（真菌 β-glucan synthase）與 gastrin 分泌調控路徑（G 細胞 GPCR/cAMP）無已知交集；加之證據等級僅為 L5（純模型預測，零臨床試驗、零文獻），且藥物在香港未上市，目前不具推進條件。

**若要推進需要：**

- 補充 Caspofungin 完整作用機轉資料（DrugBank API 或原廠仿單），釐清是否存在任何腸道-胃軸相關的次要作用
- 搜尋腸道念珠菌感染與 gastrin 異常分泌相關的基礎研究或病例報告，評估間接機轉假說的可信度
- 若間接機轉假說獲得初步支持，再規劃前臨床（動物模型）驗證實驗
- 補充香港上市路徑評估（目前未上市，需考量藥物可及性問題）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

