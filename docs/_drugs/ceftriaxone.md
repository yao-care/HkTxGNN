---
layout: default
title: Ceftriaxone
parent: 中證據等級 (L3-L4)
nav_order: 152
evidence_level: L4
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L4** | 預測適應症: **7** 個
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

# Ceftriaxone：從細菌感染到高澱粉酶血症

## 一句話總結

Ceftriaxone 是廣效的第三代頭孢菌素類抗生素，臨床上廣泛用於嚴重細菌性感染（腦膜炎、肺炎、敗血症等）的治療。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，
目前有 **0 個臨床試驗**和 **3 篇文獻**涉及此方向，所有證據均為間接情境關聯，實際支持度十分有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性感染（依通用藥理知識；香港無上市記錄） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.39% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Ceftriaxone 的核心作用機轉是**抑制細菌細胞壁合成**：透過不可逆結合青黴素結合蛋白（PBPs），阻斷肽聚糖（peptidoglycan）交聯，導致細菌溶裂死亡。對革蘭氏陽性球菌（肺炎球菌、鏈球菌）及革蘭氏陰性桿菌（大腸桿菌、克雷伯菌、奈瑟菌）均具廣譜殺菌活性，血漿蛋白結合率高（85–95%），半衰期長達 8 小時，可單日給藥。

**高澱粉酶血症本身並非獨立疾病**，而是血清澱粉酶升高的實驗室發現，通常繼發於胰臟炎、腮腺炎、腸道穿孔、腎衰竭或全身性感染等。Ceftriaxone 的作用機轉僅限於殺菌，對胰臟酵素的分泌調節或清除路徑沒有任何已知影響。

現有 3 篇文獻的情境均與直接降低澱粉酶無關：1 篇為 ERCP 術後預防性使用 Ceftriaxone（澱粉酶僅為合併觀察項目），2 篇為感染性疾病或顱內出血合併高澱粉酶的病例描述。**這個預測很可能反映了模型從「感染情境下伴隨高澱粉酶」這一共現信號中提取到的假性關聯，而非真實的治療機轉。**

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | RCT/Prospective | Bratislavske lekarske listy | 30 例 ERCP 術後患者預防性使用 Ceftriaxone 1g，評估膽汁培養與臨床生化指標；澱粉酶為合併觀察項目，非主要終點 |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Observational | Southern Medical Journal | 38 例顱內出血患者觀察胰臟酵素升高現象（25 例 lipase 升高，17 例同時有 amylase 升高），與 Ceftriaxone 無直接關聯 |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Case Report | Rev Esp Enferm Dig | Weil 症候群（鉤端螺旋體病）合併上消化道出血病例，高澱粉酶血症為感染合併症；Ceftriaxone 用於治療原發感染，非用於降低澱粉酶 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
高澱粉酶血症為繼發性實驗室異常，而非可獨立治療的疾病實體。無任何生物機轉支持 Ceftriaxone 可直接改善此狀態；現有 3 篇文獻均屬感染情境下的間接共現，不構成再利用開發依據。

**若要推進需要：**
- 建立明確的分子層面作用假說（目前完全缺乏）
- 補充香港地區藥品上市許可及仿單安全性資料
- 建議優先評估有實質臨床證據支持的方向：**感染性中耳炎（Rank #4，L2 等級，建議 Proceed with Guardrails）** 具備 3 項臨床試驗與 19 篇文獻，且 Ceftriaxone 對主要致病菌（肺炎球菌、流感嗜血桿菌）具直接殺菌機轉，更值得優先推進
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

