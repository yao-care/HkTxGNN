---
layout: default
title: Metyrapone
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 5
---

# Metyrapone
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

# Metyrapone：原適應症資料缺乏，預測用於運動誘發型惡性高熱

## 一句話總結

Metyrapone（DrugBank ID: DB01011）目前缺乏原適應症與作用機轉的完整記錄。
TxGNN 模型預測它可能對**運動誘發型惡性高熱 (Exercise-Induced Malignant Hyperthermia)** 有效，
但目前**無任何臨床試驗或文獻**支持，且證據包本身標註此關聯缺乏機轉基礎。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尚無資料 |
| 預測新適應症 | 運動誘發型惡性高熱 (Exercise-Induced Malignant Hyperthermia) |
| TxGNN 預測分數 | 99.95%（排名第 1363） |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據證據包內附的機轉分析，Metyrapone 是 **11β-hydroxylase (CYP11B1) 抑制劑**，作用於腎上腺皮質的類固醇合成路徑，抑制皮質醇生成。這是目前唯一可取得的機轉線索（正式的 `original_moa` 欄位本身缺資料）。

運動誘發型惡性高熱屬於骨骼肌 **ryanodine receptor 1 (RYR1)** 或 **CACNA1S** 相關的鈣離子通道病變，與腎上腺皮質類固醇合成軸之間**沒有已知的直接機轉聯繫**。證據包中同時列出的另外 4 個預測適應症——惡性高熱易感性、King-Denborough 症候群、central core myopathy、multiminicore disease——全部同屬 RYR1 相關先天性肌病譜系，且皆給出相同結論：藥理標的不重疊，缺乏機轉支持。

這種「同一藥物對一整組病理機轉相近但與藥物標的無關的疾病都給出高分」的模式，較可能反映知識圖譜中「肌肉/代謝壓力反應」節點的間接統計關聯，而非真實可用的藥理學路徑。換言之，此預測目前應視為假說產生（hypothesis-generating），而非有機轉支持的候選。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

此藥物目前未在香港取得上市許可證，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測適應症（及其餘 4 個同群組候選）均無臨床試驗或文獻支持，證據等級僅 L5，決策階段停留在 S0。
- 證據包內的機轉分析明確指出，Metyrapone 的 CYP11B1/皮質醇抑制作用與 RYR1/CACNA1S 相關惡性高熱、先天性肌病之間無已知分子路徑重疊，預測分數高可能是知識圖譜的間接統計關聯而非真實藥理訊號。

**若要推進需要：**
- 補齊 TFDA（或當地藥監局）仿單警語與禁忌症（目前為 Blocking 等級資料缺口，無法進入 S1 安全性初評）
- 補齊 Metyrapone 完整作用機轉資料（DrugBank API 查詢）
- 尋找是否有獨立於 TxGNN 之外的藥理學或病例報告佐證此關聯，否則建議不投入進一步資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

