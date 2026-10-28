---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 756
evidence_level: L5
indication_count: 9
monitor_inn: "RANIBIZUMAB"
predicted_indications: ["tetanic cataract", "immature cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "hemorrhagic disease of newborn"]
last_modified_at: 2026-10-23
description: "Ranibizumab：預測新適應症為手足搐搦性白內障 (tetanic cataract)（證據等級 L5）。原適應症：知識圖譜記錄的關聯疾病：糖尿病視網膜病變、黃斑部病變、糖尿病黃斑部水腫、視網膜動脈阻塞、早產兒視網膜病變等"
---

# Ranibizumab
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

## Ranibizumab：從視網膜血管疾病到白內障（tetanic cataract）
{: .text-alpha }

## 一句話總結

Ranibizumab 是一種眼內注射的抗 VEGF 藥物，知識圖譜記錄的相關疾病為糖尿病視網膜病變、黃斑部病變與糖尿病黃斑部水腫等眼底疾病。
TxGNN 模型預測它可能對**手足搐搦性白內障 (tetanic cataract)** 有效，但**沒有任何臨床試驗或文獻直接研究此疾病**，屬於僅有模型預測的階段（L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯疾病：糖尿病視網膜病變、黃斑部病變、糖尿病黃斑部水腫、視網膜動脈阻塞、早產兒視網膜病變等（香港許可證資料未提供核准適應症文字） |
| 預測新適應症 | 手足搐搦性白內障 (tetanic cataract) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ranibizumab 為抗 VEGF（血管內皮生長因子）藥物，臨床上用於視網膜血管與新生血管相關疾病。

手足搐搦性白內障繼發於低血鈣或副甲狀腺功能低下，並非 VEGF 驅動的病程，機轉上看不出合理的抗 VEGF 作用途徑。此高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病（如糖尿病白內障、視網膜疾病等已知眼科適應症）之間的相似性，而非生物學證據。

同一批高分預測還包括未成熟、成熟、皮質性、核性、老年性白內障等。這些預測分數幾乎相同（0.9999），多數同樣缺乏直接證據，顯示模型是以「眼科疾病鄰近性」判斷，解讀時須謹慎。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無直接針對手足搐搦性白內障的文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65166 | LUCENTIS SOLUTION FOR INJECTION 2.3MG/0.23ML (VIAL+FILTER NEEDLE PACK) | 注射液 | 資料未提供 |
| HK-68384 | LUCENTIS SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 10MG/ML | 預充填注射筒 | 資料未提供 |
| HK-63860 | LUCENTIS SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 10MG/ML | 預充填注射筒 | 資料未提供 |

三張許可證皆為單一成分製劑，持有者為 Novartis Pharmaceuticals (HK) Limited，狀態皆為有效。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：眼部感染性疾病、結膜炎。

其他安全性資訊（警語、禁忌、藥物交互作用）請參考原廠仿單。

另外，檢索到一則個案報告，描述玻璃體內注射 ranibizumab 後發生囊袋阻塞症候群（capsular block syndrome，PMID 38476863），屬不良事件，並非療效，但提示眼內注射在晶體相關疾病上需留意。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究手足搐搦性白內障，證據等級為 L5。
- 疾病成因（低血鈣）與抗 VEGF 機轉無明顯關聯，分數來自 TxGNN 模型（深度學習），可能只是反映模型學到的相關疾病之間的相似性，而非生物學證據。

**若要推進需要：**
- 取得 ranibizumab 的作用機轉資料，並釐清是否有任何晶體病變相關的 VEGF 路徑。
- 取得香港仿單的核准適應症、警語與禁忌資料。
- 若仍想探索，需先有前臨床或機轉研究，證明對晶體混濁有作用，再考慮臨床試驗。
- 其他白內障亞型（如糖尿病相關）目前的文獻都只涉及視網膜併發症處置，並非白內障本身的療效，也不建議以此作為推進依據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

