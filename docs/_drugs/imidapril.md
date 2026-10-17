---
layout: default
title: Imidapril
parent: 僅模型預測 (L5)
nav_order: 461
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Imidapril：預測新適應症為原因不明的多因素肺高壓（pulmonary hypertension with unclear multifactorial mechan…（證據等級 L5）。原適應症：高血壓（hypertension）"
monitor_inn: "Imidapril"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease"]
---

# Imidapril
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

# Imidapril：從高血壓到肺高壓（肺動脈高壓）

## 一句話總結

Imidapril 是一種 ACE 抑制劑（血管收縮素轉換酶抑制劑），原本用於治療高血壓。
TxGNN 模型預測它可能對**肺高壓（pulmonary hypertension with unclear multifactorial mechanism）**有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬於模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（hypertension）；香港許可證未載明核准適應症文字，此處依知識圖譜的適應症資料 |
| 預測新適應症 | 原因不明的多因素肺高壓（pulmonary hypertension with unclear multifactorial mechanism） |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Imidapril 是 ACE 抑制劑前驅藥，在體內轉換為活性代謝物 imidaprilat，
可減少血管收縮素 II 的生成並降低血管阻力。這與肺血管張力及血管重塑之間存在合理的生物學關聯。
不過，目前缺乏詳細的作用機轉資料，且 ACE 抑制劑在肺高壓中整體上並未顯示一致的療效。

TxGNN 其他排名較高的預測還包括：

| 排名 | 預測疾病 | 分數 | 評析 |
|------|---------|------|------|
| 2 | 缺氧或肺部疾病所致肺高壓 | 99.78% | 高分可能來自共用的「高血壓」本體詞彙，而非已驗證的肺部機轉；全身性降壓藥也可能惡化缺氧肺病患者的氣體交換或血行動力學，需謹慎 |
| 3 | 惡性高血壓性腎病 | 99.76% | ACE 抑制對高血壓腎病在類別層級合理，且與原適應症接近；但惡性高血壓屬急症，通常使用注射藥物處理 |
| 4 | 惡性腎血管性高血壓 | 99.76% | 此病與腎素高度相關，機轉上合理；但雙側腎動脈狹窄或單一腎臟時，ACE 抑制劑可能誘發急性腎衰竭 |
| 5 | Braddock 症候群 | 99.70% | 無法從現有資料建立明確機轉連結，高分疑為知識圖譜的人為產物 |

整體而言，這些預測都只是計算結果與藥物類別層級的推論，並無 imidapril 專屬的臨床資料。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51394 | TANATRIL TAB 5MG | 未載明 | 未載明 |
| HK-51393 | TANATRIL TAB 10MG | 未載明 | 未載明 |

兩張許可證均為單一成分製劑，狀態有效，持有者為 PRIMAL CHEMICAL CO LTD。

## 安全性考量

- **藥物交互作用**：目前資料僅顯示 imidapril 的藥理靶點為 ACE（血管收縮素轉換酶），未列出具體的藥物間交互作用等級。
- **類別層級提醒**：ACE 抑制劑在雙側腎動脈狹窄或單一腎臟的患者，可能誘發急性腎衰竭；用於缺氧性肺病患者時，也需留意血行動力學變化。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗或文獻支持（證據等級 L5）。
- ACE 抑制劑在肺高壓中並未顯示一致的療效，且部分情境（缺氧性肺病、腎血管性疾病）存在安全疑慮。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉（MOA）資料
- 進行系統性文獻與臨床試驗檢索，確認 imidapril 或同類 ACE 抑制劑在肺高壓中的證據
- 優先評估與原適應症較接近的預測（如高血壓性腎病），並釐清肺高壓的亞型與目標族群
- 建立前臨床或小型探索性研究，驗證肺血管層面的機轉假說
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

