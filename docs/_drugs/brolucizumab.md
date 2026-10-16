---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Brolucizumab：預測新適應症為核 DNA 異常所致的粒線體氧化磷酸化疾患 (Mitochondrial oxidative phosphorylation disord…（證據等級 L5）。原適應症：黃斑部病變（macular degeneration）"
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices with bleeding", "esophageal varices without bleeding", "exocrine pancreatic insufficiency"]
---

# Brolucizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Brolucizumab：從黃斑部病變到粒線體氧化磷酸化疾患（核 DNA 異常所致）

## 一句話總結

Brolucizumab 是一種抗 VEGF-A 的單鏈抗體片段，原本用於黃斑部病變（新生血管性年齡相關黃斑部病變）的治療。
TxGNN 模型預測它可能對**核 DNA 異常所致的粒線體氧化磷酸化疾患**有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黃斑部病變（macular degeneration） |
| 預測新適應症 | 核 DNA 異常所致的粒線體氧化磷酸化疾患 (Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| TxGNN 預測分數 | 99.67% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Brolucizumab 是抗 VEGF-A 的單鏈抗體片段（scFv），其在新生血管性黃斑部病變中的療效已被證實。

然而，目前沒有資料顯示 VEGF-A 抑制與核 DNA 異常導致的粒線體氧化磷酸化功能障礙之間存在明確的機轉關聯。若要建立連結，也許可從粒線體疾病併發的視網膜血管問題著手，但這純屬推測。TxGNN 分數雖高，僅代表知識圖譜中的網路關聯，不能視為生物學上的證據。

**其他預測適應症（同樣僅為模型預測，無臨床試驗或文獻）：**

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|-----------|-----------|---------|------|
| 食道靜脈曲張伴出血 | 99.12% | L5 | VEGF 理論上與內臟血管新生和門脈高壓有關，但本藥為玻璃體內注射，且抗 VEGF 藥物有出血風險，對出血性疾病是安全疑慮 |
| 食道靜脈曲張未出血 | 99.12% | L5 | 理由同上，給藥途徑與目標組織皆不吻合 |
| 外分泌胰臟功能不全 | 99.07% | L5 | 未發現可信的機轉關聯，治療以胰酵素replacement為主 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67008 | BEOVU SOLUTION FOR INJECTION 6MG/0.05ML | 注射液 | 資料未提供 |
| HK-67009 | BEOVU SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 6MG/0.05ML | 預充填注射液 | 資料未提供 |

兩張許可證均為單一成分製劑、現行有效，持證商為 NOVARTIS PHARMACEUTICALS (HK) LIMITED。

## 安全性考量

- **知識圖譜中記載的禁忌相關疾病**：葡萄膜炎、虹膜疾病、睫狀體疾病、全葡萄膜炎、眼部感染性疾病、結膜炎。這些來自知識圖譜的藥物－疾病關聯，並非仿單原文，需對照原廠仿單確認。
- **推論的風險**：抗 VEGF 藥物若全身性使用，有出血風險，這對預測的食道靜脈曲張出血適應症特別值得注意。

其餘警語、禁忌症與藥物交互作用資料目前無法取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗、文獻或可驗證的機轉支持（證據等級 L5）。
- Brolucizumab 為玻璃體內注射的眼科用藥，與預測的全身性疾病在給藥途徑和目標組織上不符，且缺乏作用機轉與仿單安全性資料。

**若要推進需要：**
- 取得詳細的作用機轉資料，並驗證與預測適應症的生物學關聯
- 取得香港衛生署仿單的警語與禁忌症
- 進行文獻與臨床試驗檢索，確認是否存在任何前臨床或臨床證據
- 評估給藥途徑的可行性（玻璃體內注射與全身性疾病的落差）
- 優先評估各預測適應症中生物學合理性較高者，並完整評估出血相關安全風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

