---
layout: default
title: Pentosan Polysulfate
parent: 僅模型預測 (L5)
nav_order: 678
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Pentosan Polysulfate：預測新適應症為血小板釋放功能異常 (primary release disorder of platelets)（證據等級 L5）。原適應症：間質性膀胱炎 (interstitial cystitis)"
monitor_inn: "Pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
---

# Pentosan Polysulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Pentosan polysulfate：從間質性膀胱炎到血小板釋放功能異常

## 一句話總結

Pentosan polysulfate 是一種半合成的類肝素硫酸多醣，原本用於治療間質性膀胱炎。
TxGNN 模型預測它可能對**血小板釋放功能異常 (primary release disorder of platelets)** 有效，
但目前**沒有臨床試驗與文獻**支持，僅屬於模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 間質性膀胱炎 (interstitial cystitis) |
| 預測新適應症 | 血小板釋放功能異常 (primary release disorder of platelets) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

其他排名較前的預測還包括 Glanzmann 血小板無力症（99.65%）與偽性血管性血友病（99.62%），證據同樣為 L5，建議同為 Hold。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pentosan polysulfate 是一種類肝素的硫酸多醣，具有較弱的抗凝血活性，並可能影響血小板相關的凝血路徑。

這與新適應症的需求方向並不一致。血小板釋放功能異常的患者本身就有血小板功能不良與出血傾向，而抗凝血活性理論上可能加重出血風險。因此，從機轉上看，這個預測目前只是模型的運算結果，缺乏生物學上的支持，應視為假說。

同樣的疑慮也適用於另外兩個預測：Glanzmann 血小板無力症是整合素 αIIbβ3 (GPIIb/IIIa) 缺陷，藥物不太可能矯正此缺陷，反而可能增加出血；偽性血管性血友病則是血小板 GPIbα 功能增強所致，雖然類肝素多醣理論上可能與 VWF 或 GPIb 結合有關，但方向與臨床效果都未知。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60563 | ANSO RECTAL OINTMENT | 未提供 | 未提供 |

此許可證為單方、有效狀態，製造商為 CNW (HK) LTD。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自模型知識圖譜，並非仿單內容）：肝臟疾病、膽囊疾病、血小板低下症、凝血疾病、血友病、肝素引起的血小板低下症。
- **藥物交互作用**：共查得 58 筆交互作用，以下列出的皆為中度等級，主要與增加出血風險的藥物有關：
  - 抗血小板藥物：Acetylsalicylic acid（阿斯匹靈）、Clopidogrel、Cilostazol、Dipyridamole、Abciximab、Cangrelor
  - 抗凝血藥物：Warfarin、Apixaban、Edoxaban、Betrixaban、Dalteparin、Bivalirudin、Antithrombin III
  - 溶栓藥物：Alteplase、Anistreplase
  - 其他：Caplacizumab、Defibrotide、Ibritumomab tiuxetan、Tositumomab

由於新適應症本身即為出血性疾病，上述禁忌與交互作用特別值得重視。香港仿單的警語與禁忌資料目前尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測適應症均無臨床試驗或文獻佐證（L5），且藥物的抗凝血特性與出血性疾病的治療需求方向相反，可能增加出血風險。
- 知識圖譜已將血液凝固疾病、血友病、血小板低下症列為禁忌，與預測方向有明顯衝突。

**若要推進需要：**
- 取得詳細的作用機轉（MOA）資料，檢驗與血小板功能的實際關聯
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 進行文獻與臨床試驗的系統性檢索，確認是否有任何支持或反對的證據
- 若有機轉上的合理依據，再考慮前臨床研究（如血小板功能與出血風險實驗）
- 確認香港已登記的劑型（目前為直腸用軟膏）與預期給藥途徑是否相容
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

