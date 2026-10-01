---
layout: default
title: Vitamin A
parent: 僅模型預測 (L5)
nav_order: 924
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A：從營養補充（原適應症未登載）到先天性凝血酶原缺乏症

## 一句話總結

Vitamin A（維生素 A）在香港已有多張許可證，但資料中未登載原適應症。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，分數很高。
然而目前有 **5 個臨床試驗**，全部與 Vitamin A 無直接關聯，**文獻為 0 篇**，這個預測缺乏實際證據支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Vitamin A 是脂溶性維生素，在香港以單方、複方維生素（如 A&D 膠囊、靜脈注射脂溶性維生素）等多種形式上市。

從機轉上看，這個預測**難以成立**。凝血酶原（Prothrombin，凝血因子 II）缺乏症是遺傳性凝血因子缺乏，凝血酶原的合成與活化依賴維生素 K，與 Vitamin A 的視黃醇類（retinoid）訊號路徑沒有已知關聯。

TxGNN 分數雖高（99.97%），但這個分數沒有任何臨床試驗或文獻佐證。排名第 918 名，也只代表它在模型內的相對位置。以現有資料，較可能是模型在知識圖譜中的間接關聯所造成的假陽性。

## 臨床試驗證據

以下 5 個試驗皆由系統比對得到，經評估相關性均為 C 級（低相關），沒有任何一個直接測試 Vitamin A 治療凝血酶原缺乏症。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | 不適用 | 完成 | 25 | 複方營養補充品對輕中度高血壓患者血管內皮功能的影響，與凝血因子缺乏無關 |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | 完成 | 90 | Vitalliver 用於失代償性肝硬化的隨機對照試驗，無法確認與 Vitamin A 或凝血酶原缺乏的關聯 |
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | 不適用 | 招募中 | 480 | 血友病患者的骨質流失（PHILEOS 研究），屬不同出血疾病，無 Vitamin A 介入 |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | 完成 | 40 | Beriplex P/N（凝血酶原複合濃縮物）用於口服抗凝血劑造成的後天性凝血因子缺乏，不涉及 Vitamin A |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | 不適用 | 完成 | 220 | 瑞士法語區成人先天代謝異常的回溯性特徵描述，無 Vitamin A 介入 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 8 張許可證，以下列出 5 張。資料中未登載劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-61308 | VITAMIN A&D CAP | DCH Auriga (Hong Kong) Limited - Universal Division |
| HK-23024 | ADECON INJECTABLE SOLUTION (VET)（獸醫用） | Wai Lung Hong Agribusiness Ltd |
| HK-36206 | VITALIPID N ADULT INJ | Fresenius Kabi Hong Kong Limited |
| HK-36205 | VITALIPID N INFANT INJ | Fresenius Kabi Hong Kong Limited |
| HK-01178 | POLIBABY CREAM | Sato Pharmaceutical (HK) Co Ltd |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻支持。
- 凝血酶原缺乏症屬於維生素 K 依賴的凝血因子疾病，與 Vitamin A 沒有合理的機轉關聯。

**若要推進需要：**
- 補齊 Vitamin A 的作用機轉資料（DrugBank）。
- 取得香港衞生署的仿單，包括原適應症、警語與禁忌症，才能進入安全性初篩。
- 找出 Vitamin A 與凝血酶原缺乏之間的機轉或臨床證據；若找不到，建議放棄此適應症。

**其他預測適應症（超出本報告範圍，僅供參考）：** 同一份資料中，「周產期疾病」（有早產兒補充 Vitamin A 的 Cochrane 系統性回顧，證據等級 L2）和「輻射或化學誘發疾患」（局部視黃醇用於光老化，證據等級 L2）的證據明顯強於本預測，建議優先改以這兩個方向評估。但兩者都屬於範圍很廣的疾病分類，且證據多針對特定族群或局部劑型，需要再縮小適應症範圍。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

