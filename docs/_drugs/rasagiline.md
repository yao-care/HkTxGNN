---
layout: default
title: Rasagiline
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 5
---

# Rasagiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rasagiline：從原發性帕金森氏症到 PLA2G6-associated neurodegeneration

## 一句話總結

Rasagiline 是選擇性 MAO-B（單胺氧化酶 B）抑制劑，原用於治療原發性帕金森氏症。
TxGNN 模型預測它可能對 **PLA2G6-associated neurodegeneration** 有效，
但目前**無任何臨床試驗**、**無任何文獻**支持這個方向，純屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性帕金森氏症（Parkinson's Disease）※ |
| 預測新適應症 | PLA2G6-associated neurodegeneration |
| TxGNN 預測分數 | 99.71%（排名 6048） |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

※ 註：evidence pack 未提供正式的原適應症/MOA 欄位資料（皆為 Data Gap），此處引用自模型 rationale 內文。

## 為什麼這個預測合理？

正式的作用機轉（MOA）欄位缺乏資料。根據 TxGNN rationale 內文，Rasagiline 為選擇性 MAO-B 抑制劑，透過減少多巴胺分解、提升紋狀體多巴胺濃度，並具潛在神經保護作用，已核准用於成人原發性帕金森氏症。

PLA2G6 相關神經退化症（PLAN，含 INAD、NBIA2）部分亞型（如非典型神經軸索病變）可出現帕金森症樣運動症狀，理論上與多巴胺路徑退化有重疊，MAO-B 抑制在理論上可能有症狀緩解價值。

但該疾病的主要病理是磷脂代謝異常導致的軸索病變與鐵沉積，與 rasagiline 的作用機轉**無直接因果關聯**。此關聯僅屬 TxGNN 模型的間接預測，**目前無任何臨床或臨床前證據支持**，機轉合理性偏弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 安全性考量

安全性資訊請參考原廠仿單。

（註：TFDA/香港仿單警語與禁忌症資料缺失，屬 Blocking 等級資料缺口，已影響本案進入 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5，無任何臨床試驗或文獻支持此適應症關聯。
- 機轉關聯性薄弱，rationale 明確指出 PLA2G6 相關神經退化症與 rasagiline 機轉無直接因果關係，僅為模型間接預測。
- 藥品目前未在本地上市，無許可證資料可供交叉比對。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking，為進入 S1 安全性初評的必要條件）。
- 補齊正式 MOA 資料以強化機轉分析（DG002）。
- 尋找 PLA2G6-associated neurodegeneration 之直接臨床前或病例證據。

**備註：** 本次預測清單中，rank 4「paralysis agitans, juvenile, of Hunt」（青少年型帕金森症）證據等級較高（L4/S1，Research Question），機轉合理性也較 rank 1 為中度（黑質多巴胺神經元功能缺損為共同終點），可能是更值得優先探索的方向，建議另案評估。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

