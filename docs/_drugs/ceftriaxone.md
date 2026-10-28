---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 7
monitor_inn: "CEFTRIAXONE"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
last_modified_at: 2026-10-28
description: "Ceftriaxone：預測新適應症為高澱粉酶血症 (hyperamylasemia)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Ceftriaxone：第三代頭孢菌素類抗生素 → 高澱粉酶血症 (hyperamylasemia)
{: .text-alpha }

## 一句話總結

Ceftriaxone 是第三代頭孢菌素類注射抗生素，在香港有多張有效許可證。
TxGNN 模型預測它可能對**高澱粉酶血症 (hyperamylasemia)** 有效，
但目前**沒有相關臨床試驗**，僅有 3 篇間接相關的文獻，且證據並未直接證實此用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 高澱粉酶血症 (hyperamylasemia) |
| TxGNN 預測分數 | 0.9939 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ceftriaxone 為廣譜抗菌藥物，其作用在於對抗感染性病原體，並無已知機轉可直接治療高澱粉酶血症。

事實上，ceftriaxone 已知可能造成膽泥與假性膽結石，進而使胰臟酵素上升，因此這項關聯較可能反映的是副作用，而非治療效益。

唯一稍有關聯的文獻（PMID 10458061）探討內視鏡乳頭括約肌切開術後預防性使用 ceftriaxone，其作用方式是預防感染性併發症（如膽管炎），並非直接治療高澱粉酶血症。因此，高預測分數目前缺乏機轉與臨床證據的支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | 臨床研究 | Bratislavske lekarske listy | 30 位內視鏡乳頭括約肌切開術後病人預防性給予 ceftriaxone 1 g，與未給藥組比較；膽汁培養細菌對 ceftriaxone 敏感，研究重點為預防感染 |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | 世代研究 | Southern Medical Journal | 顱內出血病人中，無胰臟炎也可出現胰臟酵素升高（38 人中 25 人脂肪酶升高），未涉及 ceftriaxone 治療 |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | 病例報告 | Revista espanola de enfermedades digestivas | Weil 症候群合併上消化道出血的個案，與 ceftriaxone 治療高澱粉酶血症無直接關聯 |

## 香港上市資訊

本次整理的資料顯示共有至少 20 張有效的單一成分許可證，清單可能不完整。以下列出主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52844 | ROCEPHIN POWDER & SOLVENT FOR INJ 250MG IV | 未記載 | 未記載 |
| HK-61060 | CEFTRIAXONE POWDER FOR SOLUTION FOR INJ 1G | 未記載 | 未記載 |
| HK-58898 | UNOCEF INJ 1000MG | 未記載 | 未記載 |
| HK-64249 | KORIXAL POWDER FOR SOLUTION FOR INJECTION 1G | 未記載 | 未記載 |
| HK-49794 | MEDAXONUM FOR 1M INJ 500MG (W. SOLVENT) | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，主要包括：
  - 重大（Major）：氯化鈣、葡萄糖庚酸鈣、葡萄糖酸鈣（含鈣製劑與 ceftriaxone 併用有沉澱風險）
  - 中度（Moderate）：卡那黴素、新黴素、鏈黴素、苦味酸鈉（picosulfuric acid）

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 ceftriaxone 治療高澱粉酶血症，證據等級僅為 L5。
- ceftriaxone 本身可能引起膽泥與胰臟酵素上升，此預測更可能反映副作用關聯，高分並無機轉或臨床支持。

**若要推進需要：**
- 確認 ceftriaxone 與澱粉酶升高之間的方向性（治療或誘發）
- 取得詳細的作用機轉資料
- 取得香港許可證的核准適應症與仿單警語、禁忌症
- 若有假說，需設計針對性的臨床研究，並評估膽道與胰臟相關安全性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

