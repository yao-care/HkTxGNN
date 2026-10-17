---
layout: default
title: Ferric Sulfate
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ferric Sulfate：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L5）。原適應症：未載明"
monitor_inn: "Ferric sulfate"
predicted_indications: ["bronchitis", "bronchial neoplasm (disease)", "gastroduodenitis", "peptic ulcer disease", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "severe nonproliferative diabetic retinopathy", "Chagas cardiomyopathy", "infective urethral stricture"]
---

# Ferric Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ferric sulfate：從（原適應症未載明）到支氣管炎

## 一句話總結

Ferric sulfate（硫酸鐵）在香港有一張單方注射製劑許可證，但本報告編製的資料中未載明原適應症。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，但目前**沒有任何直接相關的臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未載明（許可證資料中核准適應症欄位為空） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 97.65% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ferric sulfate 是鐵鹽，已知可作為鐵質來源，並具有局部收斂與止血作用（透過蛋白質凝集）。

這些特性與支氣管炎（呼吸道發炎）之間沒有可信的機轉關聯。97.65% 的高分僅來自知識圖譜的圖形關係推論，並非來自藥理或臨床證據。

另外，與此預測連結的兩項試驗，其實是依「鐵化合物」關鍵字配對而來，並非針對支氣管炎。因此這項預測的合理性很低，應視為待驗證的假說，而非有依據的再利用方向。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00224055](https://clinicaltrials.gov/study/NCT00224055) | Phase 4 | 完成 | 89 | 比較靜脈鐵劑 Ferrlecit 與口服鐵劑，用於未使用紅血球生成素的慢性腎病缺鐵病人；化合物不同，與支氣管炎無關 |
| [NCT00224042](https://clinicaltrials.gov/study/NCT00224042) | Phase 4 | 完成 | 52 | 比較 Ferrlecit 與口服鐵劑，用於接受紅血球生成素治療的慢性腎病缺鐵病人；化合物不同，與支氣管炎無關 |

以上兩項試驗經評估均為不相關證據。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64379 | ADDAVEN CONCENTRATE FOR SOLUTION FOR INFUSION | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 支氣管炎的預測只有模型分數，沒有相關臨床試驗或文獻，且與藥物已知性質之間沒有可信的機轉關聯。
- 連結的兩項試驗為不同鐵化合物、不同適應症，不能作為支持證據。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並確認原適應症與核准用途
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 取得支氣管炎相關的前臨床或臨床證據；在此之前不建議投入資源
- 其他排名較後的預測（如支氣管腫瘤、消化性潰瘍等）同樣僅有模型預測，且部分機轉上與藥物性質相悖（例如鐵與腫瘤生長、口服鐵鹽刺激腸胃道），不建議優先考慮
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

