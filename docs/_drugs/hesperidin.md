---
layout: default
title: Hesperidin
parent: 中證據等級 (L3-L4)
nav_order: 428
evidence_level: L4
indication_count: 10
---

# Hesperidin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Hesperidin：從原適應症未登載到骨髓增生性腫瘤

## 一句話總結

Hesperidin（橙皮苷）是柑橘類黃酮，在香港已有 17 張許可證，但資料中沒有登載原適應症。
TxGNN 模型預測它可能對**骨髓增生性腫瘤 (Myeloproliferative Neoplasm)** 有效。
目前**沒有臨床試驗**，僅有 **2 篇前臨床文獻**（電腦模擬與細胞實驗），證據等級為 L4。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未登載 |
| 預測新適應症 | 骨髓增生性腫瘤 (Myeloproliferative Neoplasm) |
| TxGNN 預測分數 | 99.47% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，Hesperidin 原本的適應症也沒有登載。已知它是柑橘類黃酮糖苷，其配基（aglycone）為 hesperetin。以下的合理性只能從前臨床研究推得，並非來自已證實的臨床療效。

現有文獻集中在**慢性骨髓性白血病（CML，骨髓增生性腫瘤的一種）**：
- 一篇電腦模擬研究以藥物再利用方式，針對 CML 中 BCR-ABL 相關標的進行篩選。
- 一篇細胞實驗顯示 hesperetin 可提高人類骨髓性白血病細胞的膜黃體素受體表現，並降低活性氧（ROS）。

這些訊號只涉及 CML。其他類型的骨髓增生性腫瘤（例如 JAK2 驅動的疾病）沒有任何支持證據。

另有一個限制：兩篇研究中至少一篇使用的是 hesperetin，而非 hesperidin。Hesperidin 口服生物利用度偏低，能否達到有效濃度仍是未知數。因此這個預測目前主要靠模型分數支撐。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | 電腦模擬篩選 | Asian Pac J Cancer Prev | 以藥物再利用的電腦模擬方法，針對 CML 中 BCR-ABL 相關標的（Grb-2）尋找潛在藥物，藉此應對 TKI 抗藥性。 |
| [40751800](https://pubmed.ncbi.nlm.nih.gov/40751800/) | 2025 | 細胞實驗 | Med Oncol | Hesperetin 可提高人類骨髓性白血病細胞的膜黃體素受體表現，並降低 ROS。 |

兩篇皆屬前臨床研究，沒有 RCT、觀察性研究或系統性回顧。

---

## 香港上市資訊

香港共有 17 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-61727 | UNI-DAPHON TABLETS | VICKMANS LABORATORIES LTD |
| HK-68056 | AVENOR TABLETS 500MG | SB PHARMA LIMITED |
| HK-66397 | VEN-Q TABLETS | DELTAPHARM LIMITED |
| HK-60527 | HESMIN TAB | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-61118 | BF-DEPILE CAP | BRIGHT FUTURE PHARMACEUTICALS FACTORY O/B BRIGHT FUTURE PHARMACEUTICAL LABORATORIES LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢未找到資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，僅有 2 篇前臨床文獻，且只涉及 CML，無法延伸到整個骨髓增生性腫瘤類別。
- 作用機轉、原適應症與安全性資料都有缺口，暫時無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症。
- 補充 Hesperidin 的作用機轉資料（DrugBank）。
- 釐清 hesperidin 與 hesperetin 的差異，評估口服後實際可達到的血中濃度。
- 在動物模型中驗證 CML 或其他骨髓增生性腫瘤的療效。
- 評估其他預測適應症：排名第 8 的「骨髓性白血病」有 16 篇細胞與電腦模擬文獻，前臨床訊號比本項更完整，可優先研究。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

