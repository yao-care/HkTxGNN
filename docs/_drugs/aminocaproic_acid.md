---
layout: default
title: Aminocaproic Acid
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 1
---

# Aminocaproic Acid
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

# Aminocaproic Acid：從止血治療到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Aminocaproic Acid（ε-胺基己酸，EACA）是一種抗纖維蛋白溶解劑，臨床上用於控制異常出血。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變（Severe Nonproliferative Diabetic Retinopathy）** 有效，
預測分數高達 **99.27%**，但目前**無任何臨床試驗或文獻**支持此方向，屬於純模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 止血 / 抗纖維蛋白溶解（antifibrinolytic therapy） |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變（Severe Nonproliferative Diabetic Retinopathy） |
| TxGNN 預測分數 | 99.27% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

Aminocaproic Acid（EACA）屬於抗纖維蛋白溶解劑，作用機轉為抑制 plasminogen activator 及 plasmin 的活性，藉此阻止血栓被過早降解，達到止血效果。

理論上，視網膜微血管瘤（microaneurysm）破裂後造成的微出血，若合併纖維蛋白溶解過度活化，EACA 的抗纖溶機轉在理論上或可穩定局部凝血、減少視網膜出血的進展。TxGNN 的高分（0.9927）推測源於知識圖譜中「抗凝/凝血路徑 ↔ 糖尿病視網膜病變」節點間的拓撲連結。

然而，此推論高度間接，**需特別注意反向風險**：抗纖溶劑可能抑制微血栓的正常吸收，加速閉塞性微血管病變，理論上反而可能惡化 NPDR 缺血程度。在無任何臨床轉譯證據的情況下，此預測的臨床可行性仍高度不確定。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

Aminocaproic Acid 在台灣**尚未取得上市許可**，目前無任何登記之藥品許可證。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：抗纖維蛋白溶解劑用於眼科適應症時，需特別評估血栓栓塞風險（如深層靜脈栓塞、肺栓塞）及局部微循環影響，建議於推進前完整查閱相關安全資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測目前完全缺乏臨床轉譯證據（L5 等級），且存在理論上的反向風險——抗纖溶機轉可能惡化視網膜缺血。在無任何臨床試驗或文獻支持的情況下，不建議推進。

**若要推進需要：**
- 補充完整作用機轉（MOA）資料，確認 EACA 對視網膜微血管的實際作用方向
- 進行文獻回顧，確認是否有 EACA 用於眼科或視網膜疾病的前臨床研究
- 評估台灣 TFDA 仿單警語與禁忌，排除眼科用途的安全禁忌
- 取得台灣藥品許可前，需評估藥品可及性及引進路徑
- 如初步文獻支持，建議先進行 Phase 1 前臨床安全性評估（動物眼科模型）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

