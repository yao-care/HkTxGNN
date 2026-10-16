---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Galcanezumab：預測新適應症為肝素輔因子 II 缺乏症 (Heparin Cofactor 2 Deficiency)（證據等級 L5）。原適應症：偏頭痛（migraine disorder）"
---

# Galcanezumab
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

# Galcanezumab：從偏頭痛到肝素輔因子 II 缺乏症

## 一句話總結

Galcanezumab 是一種針對 CGRP（降鈣素基因相關胜肽）的單株抗體，原本用於預防偏頭痛。
TxGNN 模型預測它可能對**肝素輔因子 II 缺乏症 (Heparin Cofactor 2 Deficiency)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 偏頭痛（migraine disorder） |
| 預測新適應症 | 肝素輔因子 II 缺乏症 (Heparin Cofactor 2 Deficiency) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

> 備註：香港許可證資料中未載明核准適應症文字，上表「原適應症」係依藥物知識圖譜的適應症資料列出。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Galcanezumab 是人源化單株抗體，可中和 CGRP，用於偏頭痛預防。

肝素輔因子 II 缺乏症是一種血栓傾向疾病，起因是絲胺酸蛋白酶抑制劑 SERPIND1 的活性下降，導致抑制凝血酶的能力不足。CGRP 訊號傳遞並不已知會調控肝素輔因子 II 或凝血酶抑制，因此**目前找不到可信的機轉連結**。

TxGNN 的高分（0.995）較可能來自知識圖譜中與凝血相關節點的網路鄰近性，而非生物學上的理由。同一藥物排名前三的預測（肝素輔因子 II 缺乏症、抗凝血酶缺乏症第 2 型、因子 V 過量伴自發性血栓）都屬於血栓傾向疾病，顯示這可能是知識圖譜的系統性假象，而非各自獨立的生物訊號。CGRP 雖有血管擴張作用，但與凝血抑制因子缺乏無關。

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
| HK-66579 | EMGALITY SOLUTION FOR INJECTION IN PREFILLED PEN 120MG/1ML | 注射液（預充填筆） | 資料中未載明 |
| HK-66580 | EMGALITY SOLUTION FOR INJECTION IN PREFILLED SYRINGE 120MG/1ML | 注射液（預充填注射器） | 資料中未載明 |

兩張許可證皆為單一成分、有效狀態，持有者為 ELI LILLY ASIA, INC.。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型計算（證據等級 L5），沒有任何臨床試驗或文獻佐證，且機轉上找不到合理連結。
- 三個預測適應症都屬血栓傾向疾病，高分很可能是知識圖譜的假象。

**若要推進需要：**
- 取得 Galcanezumab 的作用機轉資料（MOA）與香港仿單的警語、禁忌症
- 提出 CGRP 路徑與 SERPIND1／凝血抑制功能之間的機轉假說，並進行前臨床驗證
- 在有可信的生物學依據之前，不建議投入臨床開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

