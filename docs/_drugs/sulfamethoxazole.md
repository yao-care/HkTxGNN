---
layout: default
title: Sulfamethoxazole
parent: 中證據等級 (L3-L4)
nav_order: 824
evidence_level: L4
indication_count: 1
---

# Sulfamethoxazole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Sulfamethoxazole：從磺胺類抗菌藥到急性傳染性結膜炎

## 一句話總結

Sulfamethoxazole 是磺胺類抗菌藥，在香港已有多張上市許可證。
TxGNN 模型預測它可能對**急性傳染性結膜炎 (Acute Contagious Conjunctivitis)** 有效，
但目前只有 **0 個臨床試驗**和 **1 篇文獻**，且該文獻並未直接評估此藥的療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 急性傳染性結膜炎 (Acute Contagious Conjunctivitis) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Sulfamethoxazole 屬於磺胺類抗菌藥，作用是抑制細菌的二氫蝶酸合成酶 (dihydropteroate synthase)，阻斷細菌葉酸合成。這個機轉說明來自一般藥理知識，並非 Evidence Pack 所提供的資料。DrugBank 的原作用機轉資料目前缺漏，也沒有原適應症紀錄。

急性傳染性結膜炎多為細菌感染，常見菌種包括金黃色葡萄球菌、肺炎鏈球菌與流感嗜血桿菌。因此從抗菌角度來看，預測有一定合理性。TxGNN 分數很高 (99.63%)，但這只是計算模型的預測，不等於臨床證據。

這個預測仍有幾項限制：
- 病毒性與過敏性結膜炎不會對抗菌藥有反應。
- 磺胺類藥物的抗藥性是已知問題。
- 眼部組織的藥物穿透性與給藥途徑（全身性或局部）尚未被評估。香港現有許可證的品項中，至少有一項是輸注用濃縮液，並非眼用劑型。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | 觀察性研究（橫斷面微生物研究，依標題推斷） | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | 回溯分析希臘西部兒童急性細菌性結膜炎的病原菌與抗生素感受性；摘要不完整，未見此藥的直接療效資料 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43066 | CO-SEPTIC TAB | JEAN-MARIE PHARMACAL CO LTD |
| HK-21598 | TRIMETRIN CAP | VICKMANS LABORATORIES LTD |
| HK-09295 | APO-SULFATRIM 400-80MG TAB | HIND WING CO LTD |
| HK-59021 | COBACIDE TAB | VAST RESOURCES PHARMACEUTICAL LTD |
| HK-65292 | DBL SULFAMETHOXAZOLE AND TRIMETHOPRIM CONCENTRATE FOR SOLUTION FOR INFUSION 400MG/80MG | PFIZER CORPORATION HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測，加上一篇討論結膜炎病原菌的觀察性文獻，沒有任何研究直接測試 sulfamethoxazole 對結膜炎的療效。
- 安全性資料缺漏，且香港許可證的核准適應症與劑型資料也不完整，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌與核准適應症（此項為阻斷性缺口）
- 補齊 DrugBank 的作用機轉資料
- 查找結膜炎常見致病菌對磺胺類（含 trimethoprim 複方）的感受性資料
- 評估給藥途徑的可行性，包括全身性給藥是否能達到眼部有效濃度，或是否需要眼用劑型
- 更廣泛搜尋臨床試驗與比較性研究，確認是否有實際療效證據

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

