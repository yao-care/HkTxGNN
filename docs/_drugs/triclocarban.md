---
layout: default
title: Triclocarban
parent: 僅模型預測 (L5)
nav_order: 906
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Triclocarban：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：許可證資料未載明核准適應症"
monitor_inn: "Triclocarban"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "ulerythema ophryogenesis", "atrophoderma vermiculata", "adrenal gland hyperfunction", "erectile dysfunction (disease)", "pulmonary hypertension", "leprosy", "sciatic neuropathy"]
---

# Triclocarban
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

# Triclocarban：從外用抗菌用途到偏頭痛（預測）

## 一句話總結

Triclocarban 是一種抗菌成分，歷史上常用於肥皂等外用產品，香港目前有 2 張單方許可證。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明核准適應症 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.27% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Triclocarban 是抗菌劑，主要對革蘭氏陽性菌有活性，歷史上用於肥皂與外用產品。

目前**無法建立**它與偏頭痛之間的機轉連結。它沒有已知作用於偏頭痛相關路徑（如 CGRP、血清素或三叉神經血管訊號）。體外研究曾提到它可能增強雄激素訊號並調節離子通道，但這些都未與偏頭痛連結。

0.993 的高分僅是知識圖譜的模型輸出，未經任何試驗或文獻驗證。排名較後的預測（如偏頭痛伴腦幹先兆、偏頭痛易感性）很可能只是因為本體論上與偏頭痛相近而得分偏高，並非獨立證據。

其他預測新適應症（皆為 L5、Hold）：

| 排名 | 預測疾病 | 分數 | 備註 |
|------|---------|------|------|
| 2 | 伴腦幹先兆的偏頭痛 | 99.06% | 與偏頭痛本體相近，無獨立證據 |
| 3 | 偏頭痛（易感性） | 98.63% | 屬基因易感性實體，非可治療的臨床適應症 |
| 4 | Ulerythema ophryogenesis | 98.36% | 罕見毛囊角化疾病，無合理機轉 |
| 5 | Atrophoderma vermiculata | 98.25% | 罕見皮膚病，無機轉依據 |
| 6 | 腎上腺功能亢進 | 97.86% | 體外雄激素訊號放大屬安全疑慮，不支持療效 |
| 7 | 勃起功能障礙 | 97.21% | 無療效證據，另有內分泌干擾疑慮 |
| 8 | 肺動脈高壓 | 96.32% | 無血管或肺部機轉 |
| 9 | 痲瘋病 (Leprosy) | 95.95% | 具抗菌活性，概念上較可想像，但無抗痲瘋分枝桿菌數據，仍屬推測 |
| 10 | 坐骨神經病變 | 95.86% | 無神經病變相關證據 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56733 | ST. LUKE'S PRICKLY HEAT LAVENDER POWDER | 未載明 | 未載明 |
| HK-01178 | POLIBABY CREAM | 未載明 | 未載明 |

## 安全性考量

- **內分泌相關疑慮**：體外研究曾報告 Triclocarban 可放大睪固酮誘導的雄激素受體訊號，若考慮系統性使用，需特別評估內分泌干擾風險。

其餘安全性資訊（警語、禁忌症、藥物交互作用）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測都只有模型分數，沒有臨床試驗、文獻或可辨識的作用機轉支持。
- 該藥主要為外用抗菌成分，且有內分泌干擾的疑慮，不適合在缺乏證據下推進系統性新適應症。

**若要推進需要：**
- 取得並解析香港衛生署的仿單，補齊警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 針對偏頭痛或抗感染方向（如痲瘋病）進行文獻與前臨床證據的系統性檢索
- 評估給藥途徑的可行性，以及系統性暴露的安全性（特別是內分泌影響）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

