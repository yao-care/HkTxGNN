---
layout: default
title: Povidone
parent: 僅模型預測 (L5)
nav_order: 706
evidence_level: L5
indication_count: 1
---

# Povidone
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

# Povidone：從眼用滴劑到先天性魚鱗癬樣紅皮症

## 一句話總結

Povidone（聚維酮，PVP）在香港目前以眼藥水（人工淚液類）產品上市，許可證資料未載明原適應症文字。
TxGNN 模型預測它可能對**先天性魚鱗癬樣紅皮症 (Congenital Ichthyosiform Erythroderma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症文字（5 張許可證品名皆為眼藥水） |
| 預測新適應症 | 先天性魚鱗癬樣紅皮症 (Congenital Ichthyosiform Erythroderma) |
| TxGNN 預測分數 | 99.11% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Povidone 是親水性、可成膜的保濕高分子，常作為眼藥水的潤滑成分。香港的 5 張許可證品名皆為眼藥水，但許可證未載明適應症文字，原適應症無法確認。

先天性魚鱗癬樣紅皮症是遺傳性角化異常疾病（例如 TGM1、ALOXE3、ALOX12B 基因變異），特徵是皮膚鱗屑與角質增厚。理論上，Povidone 的保濕與成膜特性可能有助皮膚水合或屏障功能。若是含碘的 Povidone-iodine，也可能降低繼發性皮膚感染。這兩點都只是推測，尚未針對此疾病驗證過。

這個預測有明顯限制：
- 藥物並未作用於該疾病的致病路徑。
- 紅皮症患者的皮膚經皮吸收增加，含碘製劑理論上有碘吸收與甲狀腺影響的風險。
- 99.11% 的高分數可能反映知識圖譜中的鄰近關係或化合物的通用性質，不代表有特定療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

許可證資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-50769 | HANLIM POVIDONE EYE DROPS 20MG/ML | WELL FAVOURED LTD |
| HK-33056 | MURINE EYE DROPS NATURAL TEARS FORMULA | ZUELLIG PHARMA LIMITED |
| HK-50536 | SUMINE EYE DROPS | HITPHARM PHARMACEUTICAL CO LTD |
| HK-33055 | MURINE PLUS EYE DROPS NATURAL TEARS FORM | ZUELLIG PHARMA LIMITED |
| HK-42957 | FRESH TEARS EYE DROPS | JULIUS CHEN & COMPANY (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5，只有模型預測，沒有臨床試驗或文獻。
- 香港現有產品皆為眼藥水，與皮膚用途的劑型與給藥途徑不同。
- 作用機轉與疾病的致病路徑缺乏關聯，且紅皮症皮膚可能增加碘吸收的風險。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料。
- 取得香港衛生署仿單，確認警語與禁忌。
- 確認劑型與給藥途徑是否能用於皮膚，並釐清製劑是否含碘。
- 進行文獻與臨床試驗檢索，或先做前臨床（皮膚屏障、角質層水合）研究，以提升證據等級。
- 若進一步評估，需規劃甲狀腺功能監測（針對含碘製劑）。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

