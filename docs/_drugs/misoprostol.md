---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 583
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Misoprostol：從（原適應症未提供）到閉經

## 一句話總結

Misoprostol 是前列腺素 E1 類似物，會引起子宮收縮與子宮頸軟化，但本次資料未載明其原適應症。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，目前**沒有相關臨床試驗**，檢索到的 **7 篇文獻**也**沒有一篇顯示它能治療閉經**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證與藥物資料均未載明 |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.64% |
| 證據等級 | L5（資料包標為 L4，但文獻並未直接支持此適應症，故依規則降為 L5） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Misoprostol 是前列腺素 E1 類似物，藥理作用是引起子宮收縮與子宮頸軟化（成熟）。本次輸入缺乏詳細的作用機轉與原適應症資料，因此無法獨立確認機轉上的關聯。

檢索到的文獻主要談 mifepristone 合併 misoprostol 用於早期妊娠終止，以及稽留流產的藥物處理。這些研究中的「閉經」只是**孕齡標準**（例如閉經 ≤35 天），並不是被治療的疾病。沒有任何論文顯示 misoprostol 能治療閉經本身。

因此 99.64% 的高分較可能反映知識圖譜中「妊娠」與「月經相關」術語之間的連結，而非真正的療效訊號。這個預測目前只能視為模型假說。

第二個預測適應症是「非典型主動脈縮窄」（分數 99.30%），完全沒有臨床試驗或文獻支持，同樣只有模型分數。前列腺素 E1（alprostadil）用於維持動脈導管開放，但那是不同的藥物與用途，不能作為 misoprostol 的證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | 744 位閉經 ≤35 天的超早期妊娠婦女，比較低劑量 mifepristone 加自行服用 misoprostol 與院內給藥，用於超早期藥物流產的療效、安全性與接受度。閉經僅為入組條件。 |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT（劑量範圍） | Reproductive Sciences | 2500 位超早期妊娠婦女，mifepristone 由 150 mg 遞減至 50 mg，24 小時後接 misoprostol 200 µg，評估終止妊娠效果。與治療閉經無關。 |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | 臨床研究 | Human Reproduction | 預期月經前使用低劑量 mifepristone 加 misoprostol，評估預防非預期妊娠的可行性與效果。 |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | 世代研究 | J Obstet Gynaecol Res | 自行服用 misoprostol 搭配低劑量 mifepristone 終止早期妊娠的安全性與療效。 |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | 臨床研究 | BMJ | 稽留流產與無胚胎妊娠的藥物處理（無摘要，依標題判斷）。 |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | 病例報告 | Cureus | 妊娠急性脂肪肝的診斷困難；病人以閉經等症狀就診，與 misoprostol 治療閉經無關。 |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | 回顧 | J Obstet Gynaecol Can | 子宮內膜燒灼術處理異常子宮出血；misoprostol 並非重點。 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-26808 | CYTOTEC TAB 200MCG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-56461 | APO-MISOPROSTOL TAB 200MCG | HIND WING CO LTD |
| HK-64599 | MEDABON TABLETS | HONG KONG MEDICAL SUPPLIES LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻中的「閉經」只是妊娠孕齡的描述，並非治療目標，高預測分數缺乏實質證據支撐。
- 香港仿單的警語與禁忌尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衞生署的仿單，補齊原適應症、警語與禁忌症。
- 補齊 DrugBank 的作用機轉，釐清 misoprostol 與閉經（如子宮內膜、荷爾蒙軸線）之間是否有機轉關聯。
- 重新檢索是否有直接以 misoprostol 治療閉經或月經異常的研究。若仍無，建議停止推進此適應症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

