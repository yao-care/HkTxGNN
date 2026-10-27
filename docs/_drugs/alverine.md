---
layout: default
title: Alverine
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Alverine：預測新適應症為輕度慢性憂鬱症 (Dysthymic Disorder)（證據等級 L5）。原適應症：本報告彙整的香港許可證資料未載明核准適應症"
monitor_inn: "Alverine"
predicted_indications: ["dysthymic disorder", "neurotic disorder", "anxiety disorder", "migraine disorder", "neurotic depression", "melancholia", "benign paroxysmal torticollis of infancy", "agoraphobia", "congenital isolated adrenocorticotropic hormone deficiency (disease)"]
---

# Alverine
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

## Alverine：從腸胃道平滑肌痙攣到構音情緒障礙（Dysthymic Disorder）
{: .text-alpha }

## 一句話總結

Alverine 是一種平滑肌鬆弛劑，在香港已有多張許可證上市，臨床上常用於腸胃道平滑肌痙攣的症狀緩解。
TxGNN 模型預測它可能對**輕度慢性憂鬱症（Dysthymic Disorder）**有效，但目前**沒有臨床試驗**，也**沒有直接文獻**支持，僅是模型預測。
在所有預測適應症中，證據最多的是**焦慮症（Anxiety Disorder）**，目前僅有 1 篇動物實驗文獻。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告彙整的香港許可證資料未載明核准適應症（藥理資料顯示用於腸胃道平滑肌痙攣的症狀緩解） |
| 預測新適應症 | 輕度慢性憂鬱症 (Dysthymic Disorder) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料庫的描述，Alverine 在部分國家用於緩解平滑肌痙攣引起的腸胃道不適，也可能用於減輕痛經相關的絞痛。另有資料指出它可能具有 5-HT1A 拮抗作用，這與情緒調節有潛在關聯。

針對輕度慢性憂鬱症，目前沒有任何直接證據。血清素系統與憂鬱、焦慮的病理有關，因此在機轉上有一定的推測空間，但這僅是假說，尚未有臨床或前臨床資料驗證。

值得注意的是，在其他預測適應症中，**焦慮症**有一篇 2014 年的小鼠研究，顯示 Alverine citrate 具有類抗焦慮效果，與 5-HT1A 拮抗機轉一致。憂鬱相關適應症（神經質憂鬱、憂鬱型情緒障礙）則僅有一篇網路式藥物再定位的計算研究，屬間接證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測適應症（輕度慢性憂鬱症）目前無相關文獻。

以下為其他預測適應症中的相關文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25199966](https://pubmed.ncbi.nlm.nih.gov/25199966/) | 2014 | 前臨床（動物模型） | European Journal of Pharmacology | Alverine citrate 在小鼠焦慮模型中顯示類抗焦慮效果，與 5-HT1A 受體拮抗相關（適應症：焦慮症） |
| [30087074](https://pubmed.ncbi.nlm.nih.gov/30087074/) | 2018 | 計算／網路式藥物再定位 | European Neuropsychopharmacology | 以網路方法預測並驗證潛在抗憂鬱藥物；Alverine 的具體角色尚無法確認（適應症：神經質憂鬱、憂鬱症狀） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-26461 | SPASMONAL CAP 60MG（Viatris Healthcare Hong Kong） | 膠囊 | 未提供 |
| HK-54718 | ALMETIN SOFT CAP（Lafarge） | 軟膠囊 | 未提供 |
| HK-35395 | METEOSPASMYL CAP（DCH Auriga） | 膠囊 | 未提供 |
| HK-62910 | AVARIN CAPSULES（Zuellig Pharma） | 膠囊 | 未提供 |
| HK-68438 | ALBISTA CAPSULES（LSB (HK)） | 膠囊 | 未提供 |

---

## 安全性考量

- **藥物交互作用**：藥理資料庫記錄 1 筆與 Alverine 相關的作用標的資料（肝細胞核因子 4-α，HNF4A），屬藥理標的層級資訊，並未分級，臨床意義尚不明確。

其他警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（輕度慢性憂鬱症）僅有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 在所有預測適應症中，只有焦慮症具有動物實驗支持（L4），且尚無人體資料，仍屬研究假說階段。

**若要推進需要：**
- 取得香港衛生署的仿單資料，確認核准適應症、警語與禁忌症
- 補充 Alverine 的作用機轉資料（特別是 5-HT1A 拮抗作用的證據強度）
- 針對焦慮症優先進行文獻深入回顧，並評估是否有設計探索性臨床研究的可行性
- 確認憂鬱相關預測在 2018 年網路式研究中是否真的涵蓋 Alverine
- 評估精神科用藥的劑量、療程與現行上市劑型是否相容
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

