---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 775
evidence_level: L5
indication_count: 5
monitor_inn: "RIMEGEPANT"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
last_modified_at: 2026-10-28
description: "Rimegepant：預測新適應症為萎縮性蠕蟲狀皮膚病 (Atrophoderma Vermiculata)（證據等級 L5）。原適應症：知識圖譜記錄的關聯為偏頭痛"
---

# Rimegepant
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

## Rimegepant：從偏頭痛到萎縮性蠕蟲狀皮膚病（Atrophoderma Vermiculata）
{: .text-alpha }

## 一句話總結

Rimegepant 在知識圖譜中記錄的用途為偏頭痛。
TxGNN 模型預測它可能對**萎縮性蠕蟲狀皮膚病 (Atrophoderma Vermiculata)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯為偏頭痛（香港許可證資料中未載明核准適應症文字） |
| 預測新適應症 | 萎縮性蠕蟲狀皮膚病 (Atrophoderma Vermiculata) |
| TxGNN 預測分數 | 0.9976 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Rimegepant 屬於 CGRP（降鈣素基因相關胜肽）受體拮抗劑類別，知識圖譜記錄其與偏頭痛相關。

萎縮性蠕蟲狀皮膚病是一種罕見的毛囊角化與皮膚萎縮性疾病，目前沒有已知的 CGRP 路徑參與。因此，本報告未找到合理的機轉連結。0.9976 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

其他排名靠前的預測（眉部毛囊萎縮性紅斑、肝素輔因子 2 缺乏、抗凝血酶缺乏第 2 型、第五因子過量伴自發性血栓）同樣沒有任何臨床或文獻證據，機轉上也缺乏連結。其中數項涉及血栓風險，若考慮探索應特別審慎評估心血管與血栓安全性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67735 | NURTEC ORAL LYOPHILISATES 75MG | 未載明 | 未載明 |
| HK-67734 | NURTEC ORAL LYOPHILISATES 75MG | 未載明 | 未載明 |

兩張許可證均為單一成分製劑，持有者為 PFIZER CORPORATION HONG KONG LIMITED，狀態皆為有效。

## 安全性考量

- **藥物交互作用**：資料庫共查得 57 筆交互作用，以下列出部分主要項目：
  - 重度：Dexamethasone、Lumacaftor、Apalutamide
  - 中度：Aprepitant、Clarithromycin、Rolapitant、Sulfasalazine、Cobicistat、Eltrombopag、Ivacaftor、Chloramphenicol、Erythromycin、Fluconazole、Ketoconazole、Tacrolimus 等

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻直接研究此疾病，證據等級為 L5。
- 機轉上沒有合理的連結（CGRP 路徑與此疾病無已知關聯），高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並釐清 CGRP 路徑與該皮膚疾病是否有任何生物學關聯
- 取得香港衛生署核准的仿單，確認適應症、警語與禁忌症
- 取得至少前臨床或病例層級的證據，直接針對此疾病
- 若考慮血栓相關的預測適應症，需先完成心血管與血栓安全性審查
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

