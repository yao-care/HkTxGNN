---
layout: default
title: Vernakalant
parent: 中證據等級 (L3-L4)
nav_order: 932
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Vernakalant：預測新適應症為中風 (Stroke Disorder)（證據等級 L4）。原適應症：心房顫動（atrial fibrillation）"
monitor_inn: "Vernakalant"
predicted_indications: ["stroke disorder", "sick sinus syndrome 2, autosomal dominant", "obsolete susceptibility to ischemic stroke", "sarcoglycanopathy", "Wildervanck syndrome", "ABri amyloidosis"]
---

# Vernakalant
{: .fs-9 }

證據等級: **L4** | 預測適應症: **6** 個
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

# Vernakalant：從心房顫動到中風

## 一句話總結

Vernakalant 是一種心房選擇性抗心律不整藥物，原本用於心房顫動（atrial fibrillation）。
TxGNN 模型預測它可能對**中風 (Stroke Disorder)** 有效，但目前**沒有臨床試驗**，僅有 **7 篇文獻**（多為心房顫動的綜述，並非直接證明本藥可預防中風）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房顫動（atrial fibrillation） |
| 預測新適應症 | 中風 (Stroke Disorder) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Vernakalant 是心房選擇性抗心律不整藥物，一般認為它阻斷心房較具優勢的鉀電流（如 IKur、IK,ACh），並對鈉通道有頻率依賴性的阻斷作用，用於復發性心房顫動的藥物性心律轉換。

心房顫動是心源性栓塞中風的重要成因，因此兩者之間存在**間接**的關聯：若能恢復並維持竇性心律，理論上有可能降低中風風險。

不過，目前沒有證據顯示 Vernakalant 本身能降低中風發生率。心律轉換過程也可能帶來血栓栓塞風險，因此這個關聯不能視為已確立的益處。0.998 的高預測分數，較可能反映知識圖譜中「心房顫動—中風」的關聯，而非藥物的直接作用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27292602](https://pubmed.ncbi.nlm.nih.gov/27292602/) | 2016 | Cohort | Am J Emerg Med | 單center研究，評估急診近期發作心房顫動藥物性心律轉換的安全性與療效，並追蹤 30 天血栓栓塞或死亡 |
| [17371199](https://pubmed.ncbi.nlm.nih.gov/17371199/) | 2007 | Review | Expert Opin Investig Drugs | 介紹 Vernakalant (RSD1235) 的作用特性及用於急性轉換心房顫動的研發進展 |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | 心房顫動處置進展，包括口服抗凝血劑與中風風險分層 |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Review | J Manag Care Pharm | 心房顫動藥物治療的現有與新興選項 |
| [22576674](https://pubmed.ncbi.nlm.nih.gov/22576674/) | 2012 | Review | Curr Hypertens Rep | 高血壓患者心房顫動的近期臨床試驗，含 vernakalant 等新型抗心律不整藥 |
| [23553811](https://pubmed.ncbi.nlm.nih.gov/23553811/) | 2013 | Review | Pharmacotherapy | 心房顫動處置的臨床更新 |
| [25024989](https://pubmed.ncbi.nlm.nih.gov/25024989/) | 2014 | Review | Heart Lung Vessels | 2013 年心胸血管麻醉與重症照護重點，含心房顫動新藥與左心耳封堵預防中風 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61191 | BRINAVESS CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/ML | — | — |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 中風的預測僅來自模型與心房顫動的間接關聯，沒有任何臨床試驗，文獻也未顯示 Vernakalant 能降低中風發生率。
- 心律轉換本身可能帶來血栓栓塞風險，此方向的獲益尚未確立。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌症，完成安全性初篩
- 設計或蒐集以中風/血栓栓塞為終點的臨床證據，證明本藥相對於標準照護（如抗凝血治療）的附加價值

---

### 其他預測適應症（供參考）

其餘預測（家族性竇房結症候群、缺血性中風易感性（過時術語）、肌聚糖病、Wildervanck 症候群、ABri 類澱粉變性）皆無臨床試驗或文獻支持，證據等級為 L5，僅屬模型預測。其中竇房結症候群可能因心搏過緩與傳導風險而使病情惡化，不建議優先考慮。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

