---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 754
evidence_level: L5
indication_count: 9
monitor_inn: "RAMIPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis", "cerebral artery occlusion"]
last_modified_at: 2026-10-28
description: "Ramipril：預測新適應症為Pulmonary hypertension owing to lung disease and/or hypoxia（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ramipril
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

## Ramipril: Pulmonary hypertension owing to lung disease and/or hypoxia
{: .text-alpha }

## 一句話總結

Ramipril 是一種 ACE 抑制劑，知識圖譜中記錄的原有關聯包括高血壓、中風與腦血管疾病。
TxGNN 模型預測它可能對**肺高壓（因肺部疾病和/或缺氧所致）**有效。
目前**沒有臨床試驗**，只有 **1 篇**直接相關的動物研究，其餘文獻僅提供間接支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5（僅有一篇直接研究此疾病的動物實驗） |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ramipril 屬於 ACE 抑制劑類別，一般認為它透過抑制血管張力素轉換酶，降低血管張力素 II 生成，進而影響血管張力與血管重塑。

慢性缺氧會啟動腎素-血管張力素系統（RAS），促使肺血管重塑。一項大鼠研究（PMID 9200213）顯示，在慢性缺氧期間給予 ramipril，可降低基線灌流壓，並減輕缺氧對肺血管的影響。這是本預測最直接的機轉依據。

但這項證據僅限動物實驗，沒有人體臨床試驗。此外，全身性血管擴張可能惡化缺氧性肺病的通氣灌流匹配，臨床上需特別謹慎。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下表列出與此預測相關性較高的文獻，其餘檢索到的文獻（如心肌梗塞、子宮內膜異位症、庫欣氏病個案等）與肺高壓無直接關係，不予列出。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | 動物研究 | Physiological Research | 大鼠暴露於慢性缺氧 3 週並給予 ramipril，肺血管灌流壓較低，減輕缺氧對肺血管的影響 |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | 動物研究 | Am J Physiol Regul Integr Comp Physiol | 轉基因大鼠研究 RAS 與心肌缺氧再灌注，屬心臟而非肺部，僅提供間接參考 |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | 大鼠與人體組織 | Eur Heart J | 心肌梗塞後 ACE2 表現增加，與肺高壓無直接關係 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55957 | APT-RAMIPRIL TAB 2.5MG | 未載明 | 未載明 |
| HK-57336 | APO-RAMIPRIL CAP 5MG | 未載明 | 未載明 |
| HK-36855 | TRITACE 2.5MG TAB | 未載明 | 未載明 |
| HK-36856 | TRITACE 5MG TAB | 未載明 | 未載明 |
| HK-55956 | APT-RAMIPRIL TAB 5MG | 未載明 | 未載明 |

另有 1 張許可證（HK-57478，APO-RAMIPRIL CAP 2.5MG）未列於上表。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：腎臟疾病、肝臟疾病、膽囊疾病、全身性紅斑性狼瘡、嗜中性白血球低下、顆粒球缺乏症、遺傳性血管性水腫、低血壓、結締組織疾病、腎動脈阻塞、硬皮病／系統性硬化症等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重（Major）：檸檬酸鉀、碳酸氫鉀（高血鉀風險需注意）
  - 中度（Moderate）：阿斯匹靈、嗎啡、二甲雙胍、格列美脲、達格列淨、恩格列淨、卡格列淨、氫皮質酮、地塞米松、貝他米松、布地奈德等

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有單一動物實驗支持，沒有任何臨床試驗，且 ACE 抑制劑造成的血管擴張可能不利於缺氧性肺病，目前不宜推進。
- 同一預測分數下的「機轉不明的多因性肺高壓」更是僅有模型分數，沒有任何研究。

**若要推進需要：**
- 補充 ramipril 的作用機轉資料
- 取得香港仿單的核准適應症、警語與禁忌
- 進行人體研究，驗證對肺高壓血行動力學的影響及對通氣灌流匹配的安全性
- 評估與 PDE5 抑制劑、內皮素受體拮抗劑等現有肺高壓治療的定位與合併安全性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

