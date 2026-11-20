---
layout: default
title: Carisoprodol
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Carisoprodol：預測新適應症為失眠 (Insomnia)（證據等級 L5）。原適應症：資料中未載明"
monitor_inn: "CARISOPRODOL"
predicted_indications: ["insomnia (disease)"]
---

# Carisoprodol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Carisoprodol：從肌肉骨骼疾病到失眠
{: .text-alpha }

## 一句話總結

Carisoprodol 是一種中樞作用型骨骼肌肉鬆弛劑，在香港已有上市許可證。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇間接相關文獻**，證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明 |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 0.9902 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Carisoprodol 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Carisoprodol 緩解急性疼痛性肌肉骨骼疾病相關不適的作用機轉尚未明確確立。在動物研究中，carisoprodol 誘發的肌肉鬆弛與脊髓及腦部下行網狀結構中的中間神經元活性改變有關。」英文原文："The mechanism of action of carisoprodol in relieving discomfort associated with acute painful musculoskeletal conditions has not been clearly identified. In animal studies, muscle relaxation induced by carisoprodol is associated with altered interneuronal activity in the spinal cord and in the descending reticular formation of the brain."（[DailyMed: Carisoprodol Tablets, Usp, 350 Mg (carisoprodol) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f08f4af-37c2-49b5-a4e3-284414f866fa)，版本日期 2026-11-03；查閱日期 2026-11-19）。根據一般藥理學知識，Carisoprodol 是中樞作用型骨骼肌肉鬆弛劑，其活性代謝物 meprobamate 具有類似巴比妥類的鎮靜與抗焦慮作用，推測是透過調節 GABA-A 受體產生。這種鎮靜活性為改善睡眠提供了合理但尚未證實的理論基礎。

唯一的支持文獻談的是夜間腿部抽筋，這是一種會干擾睡眠的肌肉骨骼問題，並非直接測試失眠治療。因此即使有睡眠上的益處，也較可能是間接的，例如緩解抽筋或肌肉緊繃，或來自鎮靜作用本身。

TxGNN 分數很高（0.9902），但這僅是計算模型的預測，不能取代實際研究。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Review | American Family Physician | 夜間腿部抽筋可造成嚴重失眠；此文獻討論抽筋的成因與處置，並未直接評估 Carisoprodol 對失眠的療效 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48198 | CARISOPRODOL TAB 125MG | 錠劑 | 未提供 |

---

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，其中較重要的包括：
  - 嚴重（Major）：Morphine、Morphine (liposomal)
  - 中度（Moderate）：Dronabinol、Metoclopramide、Nabilone、Opium、Sibutramine、Difenoxin、Diphenoxylate
  - 整體而言，與中樞神經抑制劑、鴉片類藥物及苯二氮平類合用時風險特別需要留意。
- **知識圖譜標示的疾病禁忌**（來自模型知識圖譜，並非仿單內容）：癲癇、腎臟疾病、肝臟疾病、膽囊疾病、血小板低下、貧血、消化性潰瘍、發炎性腸道疾病、攝護腺肥大、低血壓、痛風、血友病、呼吸衰竭、心臟傳導疾病、腎上腺功能不全（含 Addison 病）、甲狀腺低下、物質濫用/依賴等。
- **濫用與依賴風險**：Carisoprodol 具有明顯的濫用及依賴潛力，對於失眠這類可能需長期用藥的情況尤其是疑慮。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有臨床試驗，唯一文獻也只是間接相關，證據停留在 L4。
- 藥物有濫用與依賴風險，且交互作用負擔大，不適合在缺乏證據下用於失眠這類慢性病症。

**若要推進需要：**
- 補齊作用機轉資料（MOA）
- 取得香港仿單的警語、禁忌與核准適應症
- 收集直接針對失眠的臨床或前臨床研究
- 評估與其他睡眠藥物相比的效益風險，以及依賴風險的管控方式

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Carisoprodol Tablets, Usp, 350 Mg (carisoprodol) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f08f4af-37c2-49b5-a4e3-284414f866fa) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

