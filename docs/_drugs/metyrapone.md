---
layout: default
title: Metyrapone
parent: 僅模型預測 (L5)
nav_order: 580
evidence_level: L5
indication_count: 9
monitor_inn: "METYRAPONE"
predicted_indications: ["exercise-induced malignant hyperthermia", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
last_modified_at: 2026-10-23
description: "Metyrapone：預測新適應症為運動誘發性惡性高熱（證據等級 L5）。原適應症：香港許可證未載明核准適應症"
---

# Metyrapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Metyrapone：從庫欣氏症候群診斷與治療到運動誘發性惡性高熱
{: .text-alpha }

## 一句話總結

Metyrapone 是腎上腺皮質類固醇合成抑制劑，臨床上用於下視丘－腦下垂體功能診斷，也偶爾用於庫欣氏症候群的治療。
TxGNN 模型預測它可能對**運動誘發性惡性高熱 (exercise-induced malignant hyperthermia)** 有效。
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型的計算預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症；藥理資料顯示臨床用途為下視丘－腦下垂體功能診斷，以及偶爾用於庫欣氏症候群治療 |
| 預測新適應症 | 運動誘發性惡性高熱 |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料，Metyrapone 抑制 11-β-羥化酶（CYP11B1），並作用於 CYP11B2，進而降低皮質醇合成。

運動誘發性惡性高熱與骨骼肌鈣離子調控異常（如 ryanodine receptor，RYR1）相關，而 Metyrapone 對此路徑沒有已知作用。因此，原用途與預測的新適應症之間，並沒有已確立的機轉關聯。這個高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據，應視為待驗證的假說。

同一組預測中的其他疾病，包括 King-Denborough 症候群、中央核心肌病、多微核心病、中心核肌病與其他類型的惡性高熱，也都屬於肌肉鈣調控相關疾病。這些預測同樣缺乏臨床試驗與文獻支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無針對運動誘發性惡性高熱的相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-19150 | METOPIRONE CAP 250MG | 資料未載明 | 資料未載明 |

製造商為 ORIENT EUROPHARMA CO. LTD。

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：Addison 氏病、慢性原發性腎上腺功能不全、腎上腺功能不全、家族性腎上腺發育不全合併腦下垂體黃體生成素缺乏、家族性糖皮質激素缺乏症、X 連鎖先天性腎上腺發育不全、CYP11A1 部分缺乏所致遺傳性單純腎上腺功能不全、先天性腎上腺增生症、腎上腺皮質功能不全。
- **藥物交互作用**（共 12 筆，其中 10 筆為中度）：
  - 雌激素類：Ethinylestradiol、Estradiol、Conjugated estrogens、Mestranol、Esterified estrogens、Estrone sulfate 及其外用劑型，均為中度交互作用。
  - Cyproheptadine：中度交互作用。
  - 另有 CYP11B1、CYP11B2 兩個藥理作用標靶紀錄（非藥物交互作用分級）。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 Metyrapone 用於運動誘發性惡性高熱，證據等級為 L5。
- 機轉上沒有已知關聯，且藥物在腎上腺功能不全相關疾病上有安全性疑慮。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症，補齊安全性與適應症資料。
- 補充 DrugBank 的作用機轉資料。
- 進行前臨床研究，驗證 Metyrapone 與 RYR1 或骨骼肌鈣調控路徑的關聯。
- 若要探索其他預測疾病（例如家族性週期性麻痺），需先取得 1971 年文獻（PMID 4322666）的全文，確認其研究內容。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

