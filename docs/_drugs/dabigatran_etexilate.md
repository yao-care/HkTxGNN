---
layout: default
title: Dabigatran Etexilate
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 5
---

# Dabigatran Etexilate
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

# Dabigatran Etexilate：從抗凝血治療到硬化性膽管炎

## 一句話總結

Dabigatran Etexilate（達比加群酯）是一種直接凝血酶抑制劑，屬口服抗凝血藥。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效。
目前**沒有臨床試驗**，僅有 **1 篇**間接相關的文獻（與 dabigatran 本身無直接關聯），證據只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未附適應症文字） |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Dabigatran 是直接凝血酶抑制劑，作用在凝血路徑，但資料中沒有原適應症與機轉的完整描述。

就現有資料來看，**找不到明確的機轉連結**。膽汁鬱積與纖維化路徑，和凝血酶抑制之間沒有資料支持的關聯。99.82% 的高分只是知識圖譜的推論，不能當作療效證據。

另外，TxGNN 對此藥的其他預測也同樣缺乏支持：
- 家族性複合型高脂血症（已被本體論標為過時術語）、低 α 脂蛋白血症、同型合子家族性高膽固醇血症：皆為 L5，無試驗、無文獻，也無機轉關聯。
- 血小板釋放障礙：證據等級 L4，只有間接的血栓相關文獻，且抗凝血藥用於血小板功能缺陷可能增加出血風險。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | 藥物交互作用研究 | Clinical Pharmacokinetics | 評估 FXR 促效劑 cilofexor（開發中，用於非酒精性脂肪肝炎與原發性硬化性膽管炎）作為受影響藥與影響藥的 CYP450 及轉運蛋白交互作用。**此研究未涉及 dabigatran**，不構成直接證據。 |

## 香港上市資訊

香港共有 6 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57315 | PRADAXA CAP 110MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-60516 | PRADAXA CAP 150MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-57316 | PRADAXA CAP 75MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-68583 | DABIGATRAN ETEXILATE SANDOZ CAPSULES 110MG | SANDOZ HONG KONG LIMITED |
| HK-68584 | DABIGATRAN ETEXILATE SANDOZ CAPSULES 150MG | SANDOZ HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測，沒有任何臨床試驗，唯一的文獻與 dabigatran 無關，證據等級為 L5。
- 機轉上找不到明確連結，且安全性資料（香港仿單的警語與禁忌）尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料（目前為阻擋項目）
- 補充 dabigatran 的作用機轉與原適應症資料（如查詢 DrugBank）
- 檢索凝血酶／PAR 訊號與膽道纖維化、發炎相關的前臨床研究，確認是否存在機轉假說
- 若找到前臨床或觀察性證據，再重新評估證據等級與決策

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

