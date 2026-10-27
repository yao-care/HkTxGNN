---
layout: default
title: Enoxaparin
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Enoxaparin：預測新適應症為體染色體隱性蛋白 C 缺乏所致血栓形成傾向（證據等級 L5）。原適應症：肺栓塞、瀰漫性血管內凝血、猛爆性紫斑、後天性猛爆性紫斑"
monitor_inn: "Enoxaparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive"]
---

# Enoxaparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Enoxaparin：從肺栓塞與瀰漫性血管內凝血到蛋白 C 缺乏所致血栓形成傾向
{: .text-alpha }

## 一句話總結

Enoxaparin 是低分子量肝素，原本用於肺栓塞、瀰漫性血管內凝血 (DIC) 與猛爆性紫斑等凝血相關疾病。
TxGNN 模型預測它可能對**體染色體隱性蛋白 C 缺乏所致血栓形成傾向 (Thrombophilia due to protein C deficiency, autosomal recessive)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持，僅有模型預測與機轉推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺栓塞、瀰漫性血管內凝血、猛爆性紫斑、後天性猛爆性紫斑（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 體染色體隱性蛋白 C 缺乏所致血栓形成傾向 |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L5（僅有模型預測，無實際研究；系統內部標註為 L4） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Enoxaparin 是低分子量肝素，透過增強抗凝血酶 III 的活性，抑制第 Xa 因子（對凝血酶的抑制較弱），產生抗凝血作用。

蛋白 C 缺乏時，蛋白 C 抗凝血路徑（使第 Va、VIIIa 因子失活）失去作用，凝血酶生成不受控制，造成高凝血狀態。Enoxaparin 的抗凝血作用可以抵銷這種狀態。

原適應症中的猛爆性紫斑與後天性猛爆性紫斑，常由嚴重蛋白 C 缺乏引起，DIC 也屬於相近的凝血異常，這可能是 TxGNN 給出高分的原因。不過實務上，先天性蛋白 C 缺乏通常以蛋白 C 濃縮液和／或 warfarin 治療，肝素多作為急性期或銜接（bridging）用藥。Warfarin 可能暫時降低蛋白 C 而造成皮膚壞死，因此肝素銜接在臨床上是需要特別留意的環節。

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
| HK-38403 | CLEXANE INJ 20MG/0.2ML | 未載明 | 未載明 |
| HK-38404 | CLEXANE INJ 40MG | 未載明 | 未載明 |

兩張許可證皆由 Sanofi Hong Kong Limited 持有，狀態為有效。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單原文）：
  - 出血與凝血相關：血液疾病、血小板低下、肝素引起的血小板低下、凝血疾病、血友病、抗凝血酶 III 缺乏、Glanzmann 血小板無力症、血小板功能質性缺陷、顱內出血、腦內出血、胎盤早期剝離
  - 消化道與肝膽：肝衰竭、潰瘍性結腸炎、發炎性腸道疾病、活動性消化性潰瘍、膽道疾病、阻塞性黃疸
  - 眼部與心內膜：視網膜疾病、視網膜炎、糖尿病視網膜病變、糖尿病白內障、高血壓視網膜病變、感染性心內膜炎、心內膜炎、亞急性細菌性心內膜炎
  - 其他：骨質疏鬆、停經後骨質疏鬆、閉塞性動脈硬化
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重（Major）：Acetylsalicylic acid（阿斯匹靈）、Ibuprofen、Ketorolac、Abciximab、Alteplase、Acalabrutinib、Deferasirox、Trastuzumab emtansine、Ibritumomab tiuxetan、Tositumomab
  - 中度（Moderate）：Fenfluramine、Dexfenfluramine、Sibutramine、Aliskiren、Sugammadex、Iodide I-131 / I-123

其餘仿單警語與禁忌，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有針對此適應症的臨床試驗或文獻，僅憑模型高分與機轉推論，證據不足以推進。
- 先天性蛋白 C 缺乏已有蛋白 C 濃縮液與 warfarin 等標準處置，Enoxaparin 較可能僅是急性期或銜接用途。此外，仿單層級的安全性資料尚未取得。

**若要推進需要：**
- 進行系統性文獻回顧，確認 Enoxaparin 在先天性蛋白 C 缺乏（含猛爆性紫斑）的使用經驗。
- 取得香港衛生署仿單的警語、禁忌與核准適應症內容。
- 補齊 Enoxaparin 的作用機轉資料（如從 DrugBank 取得）。
- 評估與現行標準治療（蛋白 C 濃縮液、warfarin）的定位與銜接方案。
- 針對出血風險與知識圖譜標示的禁忌族群，擬定安全性監測計畫。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

