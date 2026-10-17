---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 811
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sevoflurane：預測新適應症為變異型心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：許可證資料未記載（本藥為吸入式全身麻醉藥）"
monitor_inn: "SEVOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "myositis fibrosa"]
---

# Sevoflurane
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

# Sevoflurane：從（原適應症未記載）到 Prinzmetal 心絞痛

## 一句話總結

Sevoflurane（七氟烷）是一種吸入式全身麻醉藥，香港許可證資料中未記載其核准適應症文字。
TxGNN 模型預測它可能對 **變異型心絞痛 (Prinzmetal angina)** 有效，但目前**沒有臨床試驗，也沒有文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未記載（本藥為吸入式全身麻醉藥） |
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Sevoflurane 是吸入式全身麻醉藥，理論上揮發性麻醉藥具有血管擴張及調節鈣離子通道的作用，可能對抗冠狀動脈痙攣，而這正是變異型心絞痛的病理特徵。

不過，這只是未經驗證的推測。Sevoflurane 是需在麻醉環境下給藥的吸入劑，並不適合作為慢性抗心絞痛治療。原適應症與新適應症之間在臨床用途上差距很大，也沒有提供任何支持證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（備註：排名較後的預測適應症中，纖維肌痛症有 1 篇麻醉處置個案報告，肌腱炎有 9 篇與肌腱手術麻醉相關的文獻，但皆非針對疾病治療效果，且不屬於本報告主要預測適應症。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40147 | SEVORANE INHALATION LIQUID（AbbVie） | 吸入液 | 未記載 |
| HK-57565 | SEVOFLURANE INHALATION ANESTHETIC LIQUID（Baxter） | 吸入麻醉液 | 未記載 |
| HK-56752 | SOJOURN LIQUID FOR INHALATION（Hong Kong Medical Supplies） | 吸入液 | 未記載 |

---

## 安全性考量

- **知識圖譜標示的相關疾病（非仿單內容）**：癲癇、腎臟疾病、肝臟疾病、膽囊疾病、低血壓、惡性高熱（含運動誘發型）、顱內高壓、假性腦瘤、杜顯氏肌失養症及其他肌失養症、蛋白尿、膿輸尿管。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重（Major）：Epinephrine、Dolasetron、Cisapride
  - 中度（Moderate）：Morphine、Ondansetron、Palonosetron、Clarithromycin、Levofloxacin、Famotidine、Exenatide 等
  - 輕度（Minor）：Metronidazole

仿單的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗或文獻佐證（L5）。
- Sevoflurane 為吸入式麻醉藥，不適合長期治療變異型心絞痛。
- 知識圖譜顯示它與低血壓等疾病相關，需要特別留意心血管安全性。

**若要推進需要：**
- 取得詳細的作用機轉資料，分析對冠狀動脈血管的作用
- 取得香港仿單的警語與禁忌症
- 進行前臨床或機轉研究，評估對冠狀動脈痙攣的效果
- 評估給藥途徑與長期治療的可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

