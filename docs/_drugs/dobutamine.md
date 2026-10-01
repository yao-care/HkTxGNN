---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine：從心臟收縮無力／低心輸出量狀態到落髮（Alopecia）

## 一句話總結

Dobutamine 是一種靜脈注射用的 beta-1 受體促效劑（強心劑）。原適應症資料在本次 Evidence Pack 中缺漏。
TxGNN 模型預測它可能對**落髮 (Alopecia)** 有效，但目前**沒有任何臨床試驗**，相關文獻也僅有 2 篇無關的個案報告（貓與兒童的中毒案例），實質證據等同於零。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未登載核准適應症文字 |
| 預測新適應症 | 落髮 (Alopecia) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dobutamine 是短效靜脈注射的 beta-1 促效劑型強心劑，只有輕微的 beta-2 血管擴張作用。

**這個預測在機轉上並不合理。** 分析顯示，高分很可能來自知識圖譜中與 minoxidil 等血管擴張劑的鄰近關係，而非 Dobutamine 本身的藥理作用。Dobutamine 是急性靜脈輸注用藥，不適合用於慢性皮膚／毛髮疾病。

同一批預測中的其他適應症（毛髮稀少症、先天性稀毛症、圓禿、多毛症、青光眼、雷諾氏病、頭痛、偏頭痛）同樣缺乏機轉支持。其中開角型青光眼方向甚至可能與 beta 受體藥理相反（beta 阻斷劑才用於降眼壓）。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | 個案報告（獸醫） | Journal of Veterinary Cardiology | 一隻貓因 minoxidil 中毒引發心衰竭，住院初期因低血壓使用 dobutamine；與落髮治療無關 |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | 個案報告 | Pediatric Emergency Care | 兒童秋水仙鹼急性中毒，恢復期出現掉髮；未涉及 dobutamine |

兩篇文獻都只是與落髮擦邊的中毒個案，並未顯示 dobutamine 對落髮有任何療效。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68119 | DOBUTAMINE CONCENTRATE FOR SOLUTION FOR INFUSION 250MG/20ML | 輸注用濃縮液 | 未登載 |
| HK-40604 | DOBUTAMINE HCL INJ 250MG/20ML (HOSPIRA) | 注射劑 | 未登載 |
| HK-63922 | DOBUTEL CONCENTRATE FOR SOLUTION FOR INFUSION 250MG/5ML | 輸注用濃縮液 | 未登載 |
| HK-66677 | DOBUTAMINE-HAMELN CONCENTRATE FOR SOLUTION FOR INFUSION 250MG/20ML | 輸注用濃縮液 | 未登載 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗，文獻也未提供任何支持。
- 機轉上缺乏合理連結，且 Dobutamine 只能靜脈輸注，不適合慢性落髮治療。

**若要推進需要：**
- 建議不投入資源推進落髮適應症。若仍想探索，需先有明確的機轉假說與前臨床證據。
- 取得香港衛生署仿單，補齊原適應症與安全性資料（警語、禁忌症）。
- 補充 DrugBank 的作用機轉資料。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

