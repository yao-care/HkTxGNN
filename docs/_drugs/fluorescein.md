---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorescein：預測新適應症為Prinzmetal 心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：目前香港許可證資料未載明核准適應症（實際用途為眼科診斷染色與血管攝影）"
monitor_inn: "Fluorescein"
predicted_indications: ["Prinzmetal angina", "antithrombin deficiency type 2", "rheumatoid arthritis", "factor 5 excess with spontaneous thrombosis", "hemoglobinopathy", "heparin cofactor 2 deficiency", "thrombophilia", "hyperthyroidism", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
---

# Fluorescein
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

# Fluorescein：從診斷用螢光染劑到 Prinzmetal 心絞痛（變異型心絞痛）

## 一句話總結

Fluorescein 是一種診斷用螢光染劑，主要用於眼科血管攝影與角膜染色，並非治療藥物。
TxGNN 模型預測它可能對 **Prinzmetal 心絞痛 (Prinzmetal angina)** 有效，但目前**沒有任何臨床試驗，也沒有直接支持此預測的文獻**，僅為模型的圖譜推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前香港許可證資料未載明核准適應症（實際用途為眼科診斷染色與血管攝影） |
| 預測新適應症 | Prinzmetal 心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Fluorescein 是診斷用螢光染劑（用於血管攝影），目前沒有已知的血管擴張或抑制冠狀動脈痙攣的藥理活性。

因此，原用途（診斷顯影）與 Prinzmetal 心絞痛（冠狀動脈痙攣）之間找不到合理的機轉關聯。99.81% 的高分來自知識圖譜的關聯推論，沒有臨床或文獻佐證，應視為低可信度的假說。

其他預測中，類風濕性關節炎、血紅素病變、血栓傾向、甲狀腺機能亢進等所附文獻，多半是 fluorescein 作為眼部診斷工具（角膜染色、螢光血管攝影）的描述，並非治療效果，不構成再利用證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59383 | FLUORESCITE INJ 10%（Alcon Hong Kong） | 未載明 | 未載明 |
| HK-08618 | FLUORETS OPHTHALMIC STRIPS 1MG（Bausch & Lomb (HK)） | 未載明 | 未載明 |
| HK-49096 | FLUO STRIPS 1MG（E&E Optics o/b Dreimlens Optics） | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型推論（證據等級 L5），沒有臨床試驗與直接文獻，且 fluorescein 是診斷染劑，與冠狀動脈痙攣之間沒有可辨識的機轉關聯。
- 其餘 9 個預測適應症同樣缺乏試驗，相關文獻多反映診斷用途，不支持治療性再利用。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，確認是否存在任何藥理活性關聯
- 取得香港衛生署的仿單，以補齊核准適應症、警語與禁忌
- 以文獻或前臨床實驗找出 fluorescein 與冠狀動脈血管張力調節之間的任何生物學證據
- 在缺乏上述證據前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

