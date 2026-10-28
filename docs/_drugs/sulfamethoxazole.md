---
layout: default
title: Sulfamethoxazole
parent: 僅模型預測 (L5)
nav_order: 839
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "SULFAMETHOXAZOLE"
predicted_indications: ["acute contagious conjunctivitis"]
description: "Sulfamethoxazole：預測新適應症為急性傳染性結膜炎 (acute contagious conjunctivitis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Sulfamethoxazole
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

## Sulfamethoxazole: 急性傳染性結膜炎 (acute contagious conjunctivitis)
{: .text-alpha }

## 一句話總結

Sulfamethoxazole（磺胺甲噁唑）是一種磺胺類抗菌藥，原本用於中耳炎、奴卡菌症、弓形蟲症、肺囊蟲症、志賀氏菌症等感染，原適應症清單中已包含結膜炎。
TxGNN 模型預測它可能對**急性傳染性結膜炎 (Acute Contagious Conjunctivitis)** 有效，
目前有 **0 個臨床試驗**和 **1 篇文獻**（回顧性世代研究）支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 急性傳染性結膜炎 (acute contagious conjunctivitis) |
| TxGNN 預測分數 | 0.9963 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 10 張／共 10 張） |
| 許可證數 | 10 張（有效 10 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Sulfamethoxazole 是磺胺類抗菌藥，抑制細菌的二氫蝶酸合成酶 (dihydropteroate synthase)，阻斷細菌葉酸合成；與 trimethoprim 合用時，可在連續兩個步驟上同時阻斷，產生協同效果。以上機轉說明來自一般藥理學，並非來自本報告所整理的資料。

急性傳染性結膜炎常由細菌引起（如流感嗜血桿菌、肺炎鏈球菌、金黃色葡萄球菌），因此抗菌機轉在生物學上合理。

需要注意：原適應症清單已包含「結膜炎」，所以這個預測更像是與既有用途重疊，而非真正的新適應症再利用。0.9963 的 TxGNN 分數僅是計算預測，不等於臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | 世代研究（回顧性） | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | 分析希臘西部兒童急性細菌性結膜炎的細菌學與抗生素感受性型態；該病通常以廣譜局部抗生素經驗性治療 |

此文獻為流行病學與感受性分析，摘要中未見直接評估 Sulfamethoxazole 療效的結論。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43066 | CO-SEPTIC TAB | 未載明 | 未載明 |
| HK-21598 | TRIMETRIN CAP | 未載明 | 未載明 |
| HK-09295 | APO-SULFATRIM 400-80MG TAB | 未載明 | 未載明 |
| HK-59021 | COBACIDE TAB | 未載明 | 未載明 |
| HK-65292 | DBL SULFAMETHOXAZOLE AND TRIMETHOPRIM CONCENTRATE FOR SOLUTION FOR INFUSION 400MG/80MG | 未載明（品名顯示為輸注用濃縮液） | 未載明 |

以上為 10 張有效許可證中的 5 張，均為單方許可證，無已註銷者。

## 安全性考量

- **禁忌症（來自知識圖譜的藥物－疾病禁忌關聯，非仿單文字）**：
  - 血液系統：血小板低下、嗜中性白血球低下、顆粒球缺乏症、葉酸缺乏性貧血、G6PD 缺乏症
  - 腎臟：腎臟疾病、腎衰竭、尿毒症、腎絲球腎炎
  - 肝膽：肝臟疾病、膽囊疾病
  - 代謝：紫質症（含遺傳性紫質症）、胱胺酸尿症、半乳糖血症、肝醣儲積症
  - 腸道：困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎
  - 其他：輸尿管積膿
- **藥物交互作用**：共查詢到 100 筆。列出的樣本中，中度交互作用主要涉及：
  - 降血糖藥（Chlorpropamide、Glimepiride、Acetohexamide、Glipizide、Glyburide）
  - 各類胰島素（human、aspart、degludec、detemir、glargine、glulisine）
  - Balsalazide、Picosulfuric acid
  
  輕度交互作用包括 Famotidine、Clarithromycin、Dolasetron、Palonosetron、Cisapride、Granisetron。

其餘警語請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的適應症與原適應症清單中的「結膜炎」重疊，並非真正的新用途，且目前沒有任何臨床試驗，僅有 1 篇與療效無直接關聯的流行病學文獻。
- TxGNN 高分只是模型預測；香港許可證缺少核准適應症文字，仿單安全性資料也尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌症
- 補充作用機轉資料（如 DrugBank）
- 確認眼科局部給藥的劑型與途徑是否可行（目前許可證劑型多未載明，且路徑相容性尚未評估）
- 蒐集 Sulfamethoxazole 用於結膜炎的直接療效證據（臨床試驗或感受性研究）
- 評估當地結膜炎病原菌對磺胺類藥物的抗藥性情形
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

