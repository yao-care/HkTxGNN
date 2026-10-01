---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 7
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Ceftriaxone：從抗生素用途到高澱粉酶血症

## 一句話總結

Ceftriaxone 是第三代頭孢菌素類抗生素，香港已有多張許可證上市。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前**沒有臨床試驗**，3 篇檢索到的文獻也都不支持療效。這個高分預測很可能是知識圖譜的假象。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.39% |
| 證據等級 | L5（僅有模型預測；證據包自動標為 L4，但檢索到的文獻並無支持療效者） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ceftriaxone 是廣效的第三代頭孢菌素類抗生素，主要用於治療細菌感染，並不具備已知的降低血清澱粉酶的機轉。

高澱粉酶血症是一種檢驗數值異常，可由胰臟炎、頭部外傷、顱內出血等多種原因引起。藥物與這個病名的關聯，並沒有合理的治療機轉支持。相反地，Ceftriaxone 與膽泥 (biliary sludge) 有關，罕見時也與胰臟炎有關，方向與預測相反。

因此，0.994 的高分應視為知識圖譜的關聯假象，不應據此推動任何臨床決策。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | 臨床研究（設計未確認） | Bratislavske lekarske listy | 內視鏡乳頭括約肌切開術後，30 位患者預防性給予 Ceftriaxone 1 g，與未給藥的 30 位比較。膽汁培養菌對 Ceftriaxone 敏感。目標是預防感染併發症，並非治療高澱粉酶血症 |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | 觀察性研究（與 Ceftriaxone 無關） | Southern Medical Journal | 38 位顱內出血患者中，25 位脂肪酶升高、17 位澱粉酶也升高，且無胰臟炎。討論的是酵素升高的意義，未涉及 Ceftriaxone |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | 病例報告 | Revista espanola de enfermedades digestivas | 48 歲男性因胃潰瘍出血就診，診斷為 Weil 症候群（鉤端螺旋體病）。與 Ceftriaxone 治療高澱粉酶血症無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-52844 | ROCEPHIN POWDER & SOLVENT FOR INJ 250MG IV | ROCHE HONG KONG LIMITED |
| HK-61060 | CEFTRIAXONE POWDER FOR SOLUTION FOR INJ 1G | CEUTICAL TRADING COMPANY LIMITED |
| HK-58898 | UNOCEF INJ 1000MG | WINGS PHARMACEUTICAL LTD |
| HK-64249 | KORIXAL POWDER FOR SOLUTION FOR INJECTION 1G | LSB (HK) LIMITED |
| HK-49794 | MEDAXONUM FOR 1M INJ 500MG (W. SOLVENT) | STAR MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測沒有臨床試驗，文獻也沒有任何一篇顯示 Ceftriaxone 能改善高澱粉酶血症。
- 藥物本身與膽泥、罕見胰臟炎有關，安全性方向與預測相反。

**若要推進需要：**
- 目前不建議針對此適應症投入資源。
- 若要在此藥上找有價值的再利用方向，證據包中排名第 4 的**感染性中耳炎**較值得優先評估。該項有 2 篇比較療效的研究（1997 年 Ceftriaxone 對 TMP-SMZ，2000 年 1 天對 3 天療程），證據等級為 L2，建議為 Proceed with Guardrails。
- 補齊香港衛生署仿單的警語與禁忌資料，以及作用機轉（MOA）資料。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

