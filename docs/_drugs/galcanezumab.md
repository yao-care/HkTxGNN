---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 3
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

# Galcanezumab：從偏頭痛預防到 Heparin Cofactor 2 缺乏症

## 一句話總結

Galcanezumab（Emgality®）是一種抗 CGRP 單株抗體，全球核准用於偏頭痛預防治療，在香港尚未取得上市許可。TxGNN 模型預測它可能對 **Heparin Cofactor 2 缺乏症（Heparin Cofactor 2 Deficiency）** 有效，然而目前**無任何臨床試驗或文獻**支持這個方向，且機轉分析顯示兩者之間存在**方向性矛盾風險**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 偏頭痛預防（CGRP 拮抗單株抗體，全球核准適應症） |
| 預測新適應症 | Heparin Cofactor 2 缺乏症（Heparin Cofactor 2 Deficiency） |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L5（僅模型預測，無任何實際研究） |
| 香港上市 | ✗ 未上市（0 張許可證） |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（列為 Data Gap）。根據已知資訊，Galcanezumab 是一種人源化 IgG4 單株抗體，靶向 **CGRP（降鈣素基因相關肽）**，透過阻斷 CGRP 與其受體的結合，抑制偏頭痛發作期的三叉神經血管活化與神經源性發炎。

Heparin Cofactor 2 缺乏症（SERPIND1 基因缺陷）是一種遺傳性血栓傾向疾病，患者體內 HC-II 蛋白（絲胺酸蛋白酶抑制劑）缺乏，導致凝血酶抑制不足，靜脈血栓風險上升。此疾病的核心機轉在於**凝血瀑布調控障礙**，與 CGRP 神經肽信號路徑無已知交集。

機轉分析顯示，CGRP 雖有微弱的抗血小板效應（抑制 ADP 誘導的血小板聚集），但阻斷 CGRP（即 galcanezumab 的作用方向）在理論上反而可能**輕微促進血小板活化**，方向性與治療 HC-II 缺乏症的需求相悖。TxGNN 的高分預測最可能源於圖譜中「血管內皮 → 凝血瀑布 → 絲胺酸蛋白酶抑制劑」節點的間接關聯，而非真實的藥理機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Galcanezumab 目前在香港**尚未取得上市許可**，無任何有效許可證。

---

## 安全性考量

安全性資訊請參考原廠仿單（Emgality® Prescribing Information）。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測為純模型輸出（L5 等級），無任何臨床試驗或文獻支持；更重要的是，機轉分析顯示 CGRP 阻斷與 Heparin Cofactor 2 缺乏症的治療需求存在**方向性矛盾**，生物學合理性極低。同樣情形亦見於本次另外兩個預測適應症（抗凝血酶 II 型缺乏、因子 V 過量伴發血栓），三者 TxGNN 分數幾乎相同（0.9941–0.9950），高度疑似為圖譜中「thrombophilia」疾病節點群聚效應所驅動。

**若要重新評估，建議先確認：**
- 補齊 Galcanezumab 的正式 MOA 資料（DrugBank API，DG002）
- 補齊香港仿單警語與禁忌（DG001）
- 由藥理學專家評估 CGRP 信號路徑與凝血酶調控之間是否存在任何間接交互作用的最新文獻
- 確認 TxGNN 預測是否因「thrombophilia cluster」所致，若確認則應將此類疾病群整批降為低優先級
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

