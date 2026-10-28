---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 815
evidence_level: L5
indication_count: 5
monitor_inn: "SIMVASTATIN"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Simvastatin：預測新適應症為腦幹梗塞 (brain stem infarction)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Simvastatin: 腦幹梗塞 (brain stem infarction)
{: .text-alpha }

## 一句話總結

Simvastatin 是 HMG-CoA 還原酶抑制劑（他汀類）藥物，知識圖譜中記錄的原有關聯包括高脂血症、動脈粥樣硬化與腦血管疾病。
TxGNN 模型預測它可能對**腦幹梗塞 (Brain Stem Infarction)** 有效，但目前**沒有直接研究此疾病的臨床試驗或文獻**，僅有 1 篇間接相關的文獻，因此證據等級為 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 腦幹梗塞 (brain stem infarction) |
| TxGNN 預測分數 | 0.9941 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Simvastatin 屬於他汀類藥物，一般認為它透過抑制 HMG-CoA 還原酶降低膽固醇，並可能具有穩定斑塊、抗發炎及改善血管內皮功能等多效性作用。這些說明屬於藥物類別的一般知識，並非本報告所整理資料的直接內容。

知識圖譜中，Simvastatin 與中風、腦血管疾病、腦梗塞及動脈粥樣硬化有關聯記錄。腦幹梗塞是缺血性中風的一種亞型，因此模型給出高分在生物學上可以理解。

不過，唯一檢索到的文獻（PMID 27465579）研究的是阿魏酸鈉與正丁烯基苯酞合併骨髓基質細胞，並非 Simvastatin，與本預測僅間接相關。此預測目前主要來自模型推論，尚無直接證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27465579](https://pubmed.ncbi.nlm.nih.gov/27465579/) | 2016 | 前臨床（間接相關） | Journal of Translational Medicine | 大鼠局部腦缺血模型中，阿魏酸鈉與正丁烯基苯酞合併骨髓基質細胞可促進血管新生與神經新生；未以 Simvastatin 為介入 |

## 香港上市資訊

資料顯示共有至少 20 張單一成分許可證，狀態皆為有效，但清單可能不完整。以下列出 5 張，許可證資料未提供核准適應症與劑型文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34337 | ZOCOR TAB 10MG | 未提供 | 未提供 |
| HK-58993 | SIMPLAQOR TAB 10MG | 未提供 | 未提供 |
| HK-58991 | SIMPLAQOR TAB 40MG | 未提供 | 未提供 |
| HK-51048 | SIMVASTATIN-TEVA TAB 20MG | 未提供 | 未提供 |
| HK-51793 | APO-SIMVASTATIN TAB 40MG | 未提供 | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單文字）**：胰臟炎、肝臟疾病、膽囊疾病、血小板減少、肌病變、橫紋肌溶解症、痛風、糖尿病、糖尿病酮酸中毒、凝血疾病、急性冠心症等。
- **藥物交互作用**（共 100 筆，列出部分主要者）：
  - 重大：Amiodarone、Amlodipine、Fenofibrate
  - 中度：Paclitaxel、Nifedipine、Omeprazole、Zidovudine、Aprepitant 等

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 腦幹梗塞的預測沒有任何直接研究支持，僅有一篇間接相關的前臨床文獻，證據停留在模型預測層級（L5）。
- Simvastatin 在缺血性中風相關領域的分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，並非生物學證據；這不等同於已證實對腦幹梗塞有額外療效，也不能視為已核准適應症。

**若要推進需要：**
- 檢索直接評估他汀類藥物於腦幹梗塞或後循環缺血性中風的臨床研究與觀察性資料
- 補充作用機轉資料與香港仿單的警語、禁忌與核准適應症
- 評估與現有中風二級預防用藥的重複性及藥物交互作用風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

