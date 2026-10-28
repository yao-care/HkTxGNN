---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 924
evidence_level: L5
indication_count: 6
monitor_inn: "VALSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
last_modified_at: 2026-10-28
description: "Valsartan：預測新適應症為惡性高血壓腎病變（證據等級 L5）。原適應症：高血壓"
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Valsartan：從高血壓到惡性高血壓腎病變
{: .text-alpha }

## 一句話總結

Valsartan 是血管張力素 II 第一型受體（AT1）阻斷劑，知識圖譜記錄的原適應症為高血壓。
TxGNN 模型預測它可能對**惡性高血壓腎病變 (malignant hypertensive renal disease)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇間接文獻**（內容為另一種藥物 avosentan 的前臨床研究），證據非常有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（知識圖譜記錄；本次整理的香港許可證資料未載明適應症文字） |
| 預測新適應症 | 惡性高血壓腎病變 |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Valsartan 屬於 AT1 受體阻斷劑（ARB）類別，可阻斷腎素-血管張力素系統對血管收縮的作用，用於高血壓治療。

惡性高血壓腎病變是嚴重高血壓造成的腎臟損傷，和原本的高血壓適應症在病理上相連。在機轉上，阻斷 AT1 受體可降低血壓，並可能減輕腎臟的血管與纖維化損傷，因此模型預測具有生物學上的合理性。

不過，這只是推論。唯一取得的文獻研究的是內皮素拮抗劑 avosentan，並非 valsartan，因此只能視為間接線索。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | 前臨床（不同藥物） | Pharmacological Research | 在過度表現人類腎素與血管張力素原基因的轉基因大鼠中，內皮素拮抗劑 avosentan 在不引起液體滯留的劑量下，對高血壓腎病變有保護作用；此研究未使用 valsartan |

---

## 香港上市資訊

以下為本次整理到的許可證（共列出 5 張，總數至少 20 張，清單可能不完整）。資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62376 | PMS-VALSARTAN TABLETS 320MG | 錠劑 | 未載明 |
| HK-60971 | VALSACOR FILM-COATED TABLETS 80MG | 膜衣錠 | 未載明 |
| HK-49137 | DIOVAN TAB 80MG | 錠劑 | 未載明 |
| HK-49138 | DIOVAN TAB 160MG | 錠劑 | 未載明 |
| HK-66401 | VALSARTAN TEVA TABLETS 80MG | 錠劑 | 未載明 |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，並非仿單內容）：肝衰竭、肝病、胰臟炎、膽囊疾病、血管性水腫（含遺傳性及腎素-血管張力素系統阻斷劑引起者）、全身性紅斑狼瘡、缺鉀、糖尿病及糖尿病酮酸中毒、高尿酸血症、痛風、嗜中性白血球低下、顆粒球缺乏症、低血壓、副甲狀腺機能亢進、高血鈣、腎鈣質沉著症、磷代謝異常、肝性昏迷與肝性腦病變、新生兒黃疸、無尿、腎動脈阻塞、腎功能不全。
- **藥物交互作用**（資料庫共 100 筆，以下為主要者）：
  - 重大：氯化鉀、碳酸氫鉀（有高血鉀風險）
  - 中度：多種胰島素製劑、Exenatide、Hydrocortisone、Eluxadoline、含電解質之聚乙二醇 3350

仿單警語與禁忌的正式內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高，但沒有臨床試驗，唯一文獻研究的是另一種藥物，直接證據不足，屬 L5。
- 知識圖譜中的禁忌關聯涵蓋腎功能不全、腎動脈阻塞與高血鉀風險，對腎病變族群需審慎評估。

**若要推進需要：**
- 搜尋 valsartan 或其他 ARB 用於惡性高血壓腎病變的臨床與觀察性研究
- 取得原廠仿單的警語與禁忌，以及作用機轉資料
- 設計針對腎功能與血鉀監測的安全計畫
- 釐清香港許可證實際核准的適應症文字
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

