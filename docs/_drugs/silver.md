---
layout: default
title: Silver
parent: 僅模型預測 (L5)
nav_order: 687
evidence_level: L5
indication_count: 10
---

# Silver
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Silver：從未確立適應症到 Paget 氏骨病 (Bone Paget Disease)

## 一句話總結

> Silver（DB12965，元素態銀）在香港未上市，目前無任何核准適應症紀錄。
> TxGNN 模型預測其可能對**Paget 氏骨病 (Bone Paget Disease)** 有效，
> 但檢視支持證據後發現，這是「銀染色（silver staining）組織學技術」與「銀」藥物名稱混淆造成的**假陽性關聯**，並無真實藥理訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無（香港未上市，無核准適應症紀錄） |
| 預測新適應症 | Paget 氏骨病 (Bone Paget Disease) |
| TxGNN 預測分數 | 99.67% |
| 證據等級 | L5（僅模型預測，無實質研究支持） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

**結論：這個預測不合理，屬於關鍵字混淆造成的假陽性。**

目前缺乏 Silver 的作用機轉（MOA）資料。但更關鍵的問題是，支持此預測的文獻與臨床試驗經逐一檢視後，全部與「元素銀作為治療藥物」無關：

1. 文獻主體是「銀染色（silver staining / AgNOR）」——一種用於觀察蝕骨細胞核仁、定量類骨質的**組織學染色技術**，論文中的「silver」指的是染色試劑，而非治療藥物。
2. 臨床試驗（NCT01793168、NCT03573089）分別是罕見病通用註冊研究與腎病磷酸鹽控制試驗，內容與銀的治療用途完全無關，僅因 Paget disease 為罕見病被資料庫收錄。

換言之，TxGNN 的高分預測是知識圖譜中「Silver」一詞被組織學方法論文以及疾病名稱共同出現所誤導產生的雜訊，並非真實的藥物-疾病訊號。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01793168](https://clinicaltrials.gov/study/NCT01793168) | N/A | 招募中 | 20,000 | Sanford 罕見病協調註冊研究，通用型罕見病登記平台，非銀專屬試驗，僅因 Paget disease 屬罕見病被收錄 |
| [NCT03573089](https://clinicaltrials.gov/study/NCT03573089) | N/A | 招募中 | 3,600 | 探討透析患者血磷控制策略對心臟事件與生活品質的影響，與銀無關 |

**⚠️ 兩試驗均與銀之藥理治療無直接關聯，證據等級不足。**

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9836854](https://pubmed.ncbi.nlm.nih.gov/9836854/) | 1998 | 組織學 | Bone | 探討 Paget 氏骨病蝕骨細胞核之核仁組織區域數量增加，使用銀染色（AgNOR）技術觀察，與銀治療無關 |
| [3163726](https://pubmed.ncbi.nlm.nih.gov/3163726/) | 1988 | 組織學 | J Nucl Med | 鎵-67 於 Paget 氏骨病蝕骨細胞核之定位研究，與銀無關 |
| [4111887](https://pubmed.ncbi.nlm.nih.gov/4111887/) | 1972 | 方法學 | Stain Technology | 骨去鈣化前之銀染色方法，用於類骨質定量，屬染色技術論文 |
| [2420233](https://pubmed.ncbi.nlm.nih.gov/2420233/) | 1985 | 方法學 | Anat Anz | 骨組織銀浸染法，屬組織染色技術描述 |
| [9227338](https://pubmed.ncbi.nlm.nih.gov/9227338/) | 1997 | 基礎研究 | J Pathol | 組織切片中維生素 D 受體 mRNA 定量技術限制討論，與銀無直接關聯 |

**所有文獻均為 Tier 3 組織學/方法學論文，非治療性研究，無法作為適應症擴展證據。**

---

## 安全性考量

> 安全性資訊請參考原廠仿單。目前 TFDA/香港仿單警語與禁忌資料缺失（DG001，阻斷性缺口），無法進入 S1 安全性初評階段。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測為 TxGNN 知識圖譜中「Silver」關鍵字與「銀染色（silver staining）」組織學技術論文混淆所致的假陽性關聯，缺乏真實藥理機轉支持。
- 支持證據（臨床試驗、文獻）皆與銀之治療用途無直接關聯，證據等級僅達 L5。
- 藥物本身在香港未上市，且缺乏 MOA 與仿單安全性資料（DG001 屬阻斷性缺口），目前無法進入 S1 安全性初評。

**若要推進需要：**
- 若欲重新評估，應先排除 NER/關鍵字混淆問題，針對「元素銀」實際藥理應用（如抗菌敷料、外用製劑）重新檢索證據，而非依賴此批被污染的文獻集。
- 取得 TFDA/香港仿單警語與禁忌資料，補齊 DG001。
- 取得 DrugBank MOA 資料，補齊 DG002。
- 在證據源頭排除污染前，不建議投入後續資源。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

