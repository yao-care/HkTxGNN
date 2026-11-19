---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 5
monitor_inn: "CEFTRIAXONE"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
last_modified_at: 2026-11-17
description: "Ceftriaxone：預測新適應症為高澱粉酶血症 (hyperamylasemia)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Ceftriaxone: 高澱粉酶血症 (hyperamylasemia)
{: .text-alpha }

## 一句話總結

Ceftriaxone 是第三代頭孢菌素類注射抗生素，在香港已有多張有效許可證。
TxGNN 模型預測它可能對**高澱粉酶血症 (hyperamylasemia)** 有效，
但目前**沒有臨床試驗**，僅有 **3 篇**間接相關文獻，且無法直接支持此預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 高澱粉酶血症 (hyperamylasemia) |
| TxGNN 預測分數 | 0.9939 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 28 張／共 28 張） |
| 許可證數 | 28 張（有效 28 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ceftriaxone 屬於頭孢菌素類抗生素，一般是以抑制細菌細胞壁合成來發揮抗菌作用。

就現有資料而言，找不到抗菌作用與高澱粉酶血症之間的明確機轉連結。高澱粉酶血症是胰臟酵素升高的狀態，並非單純由細菌感染造成。相反地，ceftriaxone 已知可能引起膽汁淤積（biliary sludge）與假性膽結石，這本身可能使胰臟酵素升高，因此兩者的關聯較可能反映藥物不良反應，而非治療效益。

唯一稍有關聯的文獻（PMID 10458061）探討內視鏡乳頭括約肌切開術後預防性使用 ceftriaxone，其作用是預防感染性併發症（如膽管炎），而不是直接治療高澱粉酶血症。TxGNN 的高分預測缺乏機轉與臨床證據的支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

這些文獻皆未直接以高澱粉酶血症為治療目標研究 ceftriaxone，僅供參考。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | 臨床研究 | Bratislavske lekarske listy | 30 位內視鏡乳頭括約肌切開術後病人預防性給予 ceftriaxone 1 g，與未給藥組比較；所分離細菌皆對 ceftriaxone 敏感，重點為預防感染 |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | 世代研究 | Southern Medical Journal | 顱內出血病人在無胰臟炎下可出現胰臟酵素升高；未涉及 ceftriaxone 治療 |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | 病例報告 | Rev Esp Enferm Dig | 鉤端螺旋體病（Weil 症候群）合併上消化道出血的病例，非針對高澱粉酶血症之治療證據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52844 | ROCEPHIN POWDER & SOLVENT FOR INJ 250MG IV | 未記載 | 未記載 |
| HK-61060 | CEFTRIAXONE POWDER FOR SOLUTION FOR INJ 1G | 未記載 | 未記載 |
| HK-58898 | UNOCEF INJ 1000MG | 未記載 | 未記載 |
| HK-64249 | KORIXAL POWDER FOR SOLUTION FOR INJECTION 1G | 未記載 | 未記載 |
| HK-49794 | MEDAXONUM FOR 1M INJ 500MG (W. SOLVENT) | 未記載 | 未記載 |

香港共有 28 張含本藥成分的許可證（全部有效；單一成分 18 張、複方 10 張），以上僅列出其中 5 張主要許可證。

<!-- review:begin hk-lic-20261117-ceftriaxone-1 -->

> **查核更正（2026-11-17）**：原文為「目前共 20 張有效單方許可證，無已註銷者；以上僅列出其中 5 張主要許可證，清單可能不完整。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 28 張含本藥成分的許可證（全部有效；單一成分 18 張、複方 10 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-ceftriaxone-1 -->

## 安全性考量

- **藥物交互作用**（共查得 100 筆，以下列出主要者）：
  - 重大（Major）：氯化鈣（Calcium chloride）、葡庚糖酸鈣（Calcium glucoheptonate）、葡萄糖酸鈣（Calcium gluconate）
  - 中度（Moderate）：卡那黴素（Kanamycin）、新黴素（Neomycin）、鏈黴素（Streptomycin）、苦味酸鈉（Picosulfuric acid）

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 本預測沒有任何臨床試驗，文獻也未直接研究 ceftriaxone 對高澱粉酶血症的治療效果，證據等級僅為 L5。
- Ceftriaxone 本身可能引起膽汁淤積與假性膽結石而升高胰臟酵素，故此預測反而可能反映不良反應，不建議推進。

**若要推進需要：**
- 釐清 ceftriaxone 與胰臟酵素變化之間的因果方向（治療效果或藥物不良反應）
- 提出可驗證的作用機轉假說
- 取得直接以高澱粉酶血症為對象的臨床或回溯性研究資料
- 取得香港原廠仿單，完成警語與禁忌症的安全性審查

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「目前共 20 張有效單方許可證，無已註銷者；以上僅列出其中 5 張主要許可證，清」→「香港共有 28 張含本藥成分的許可證（全部有效；單一成分 1」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

