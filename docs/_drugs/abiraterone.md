---
layout: default
title: Abiraterone
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Abiraterone：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：許可證資料未載明"
monitor_inn: "Abiraterone"
predicted_indications: ["migraine disorder", "migraine with or without aura, susceptibility to", "migraine with brainstem aura", "leprosy", "pulmonary hypertension", "nephrogenic syndrome of inappropriate antidiuresis", "rheumatoid arthritis", "kyphoscoliotic heart disease", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Abiraterone
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

# Abiraterone：從前列腺癌相關用途到偏頭痛

## 一句話總結

Abiraterone 是 CYP17A1 抑制劑，在香港已有多張許可證上市，但本次資料未提供原適應症文字。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前**沒有任何臨床試驗或直接相關文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（本次資料缺少核准適應症文字） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 98.81% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Abiraterone 是 CYP17A1 抑制劑，可抑制雄性素與雌性素的合成。

偏頭痛的發作與性荷爾蒙波動有一定關聯，因此從「調節性荷爾蒙」的角度，理論上可以推想兩者有關。但這只是推測，沒有臨床或文獻證據支持。

此外，排名前三的預測都是偏頭痛相關名稱（偏頭痛、偏頭痛易感性、腦幹先兆偏頭痛），分數可能受到疾病本體論（ontology）相近性影響而偏高，解讀時需保守。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無針對偏頭痛的相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65540 | ZYTIGA TABLETS 500MG | 錠劑 | 未載明 |
| HK-61370 | ZYTIGA TABLETS 250MG | 錠劑 | 未載明 |
| HK-68295 | AKEEGA TABLETS 50MG/500MG | 錠劑 | 未載明 |
| HK-68296 | AKEEGA TABLETS 100MG/500MG | 錠劑 | 未載明 |
| HK-67871 | APO-ABIRATERONE TABLETS 500MG | 錠劑 | 未載明 |

> 共 16 張有效許可證（皆為單方），上表僅列出 5 張主要許可證。劑型欄位依品名判斷為錠劑。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶／荷爾蒙治療藥物（CYP17A1 抑制劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下為部分範例：
  - **嚴重 (Major)**：Cisapride、Dolasetron、Eliglustat、Loperamide
  - **中度 (Moderate)**：Clarithromycin、Levofloxacin、Metoclopramide、Granisetron、Famotidine 等
  - **輕微 (Minor)**：Metronidazole

其他警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛預測僅來自圖譜模型（證據等級 L5），沒有臨床試驗與直接相關文獻，機轉連結也只是推測。
- 其他九項預測（含痲瘋病、類風濕性關節炎、肺高壓等）同樣缺乏證據。肺高壓項下檢索到的 5 篇文獻都是前列腺癌研究，與該適應症無關，不能視為支持證據。

**若要推進需要：**
- 補齊 Abiraterone 的作用機轉資料與原廠仿單（警語、禁忌症、核准適應症）。
- 進行偏頭痛與性荷爾蒙／CYP17A1 路徑的文獻回顧，並評估前臨床或機轉研究的可行性。
- 評估安全性：Abiraterone 可能造成鹽皮質素過多（高血壓、水腫），需審慎評估用於非癌症族群的風險效益。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

