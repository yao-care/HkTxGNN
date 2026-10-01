---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 920
evidence_level: L5
indication_count: 5
---

# Vildagliptin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Vildagliptin：從第 2 型糖尿病到僵人症候群

## 一句話總結

Vildagliptin 是 DPP-4 抑制劑，一般用於血糖控制。Evidence Pack 未載明原適應症，這是依藥理類別推定的。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效，但目前有 **0 個臨床試驗**和 **0 篇文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料包未提供（香港許可證的核准適應症欄位皆為空白） |
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Vildagliptin 屬於 DPP-4 抑制劑，這是從藥物類別得知的，資料包並未提供 DrugBank 的 MOA 內容。

一個推測性的連結是：僵人症候群屬自體免疫疾病（常見抗 GAD65 抗體），且常與第 1 型糖尿病並存，而 DPP-4 在免疫調節上可能扮演某些角色。**這只是假說層級的推論，沒有任何研究資料支持。** 高模型分數不等於療效證據。

此外，排名第 2 的「局部僵肢症候群 (Focal Stiff Limb Syndrome)」分數與僵人症候群完全相同（99.88%），很可能來自知識圖譜中的同一個鄰近區域，不能視為獨立的第二個訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

資料包列有 19 張許可證，以下列出 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68953 | VILDAGLIPTIN TABLETS 50MG（Chemill Pharma） | 錠劑（依品名） | 資料包未提供 |
| HK-68157 | VILDAGLIPTINA PENTAFARMA CAPSULES 50MG（Trenton-Boma） | 膠囊（依品名） | 資料包未提供 |
| HK-68917 | VILDAVITAE TABLETS 50MG（Hong Kong Medical Supplies） | 錠劑（依品名） | 資料包未提供 |
| HK-68118 | VILDAGUS TABLETS 50MG（APT Pharma） | 錠劑（依品名） | 資料包未提供 |
| HK-67559 | VIDASHINE TABLETS 50MG（Lotus Pharmaceutical HK） | 錠劑（依品名） | 資料包未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢結果為無資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測僅有 TxGNN 模型分數支持，沒有臨床試驗、文獻或明確機轉資料（證據等級 L5）。
- 香港仿單的警語與禁忌症資料缺失，屬阻擋性缺口，無法進入安全性篩選。
- 其餘 4 個預測（局部僵肢症候群、硫胺素反應性功能障礙症候群、Opsismodysplasia、藥物誘發局部脂肪營養不良）同為 L5、Hold，也都沒有支持證據。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與核准適應症。
- 從 DrugBank 補充 DPP-4 抑制劑的作用機轉資料。
- 文獻檢索：vildagliptin 或 DPP-4 抑制劑與僵人症候群、抗 GAD65 自體免疫的關聯。
- 若文獻支持，再評估是否需要設計探索性研究。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

