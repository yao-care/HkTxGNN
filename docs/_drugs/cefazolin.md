---
layout: default
title: Cefazolin
parent: 中證據等級 (L3-L4)
nav_order: 169
evidence_level: L4
indication_count: 8
---

# Cefazolin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **8** 個
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

# Cefazolin：從細菌性肺炎等感染症到感染性中耳炎

## 一句話總結

Cefazolin 是第一代頭孢菌素類抗生素，原本用於細菌性肺炎、心內膜炎、細菌性關節炎、膽管炎等感染症。
TxGNN 模型預測它可能對**感染性中耳炎 (Infectious Otitis Media)** 有效，
但目前**沒有臨床試驗登記**，僅有 **2 篇間接文獻**，證據以模型預測為主。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未提供適應症文字；依知識圖譜為細菌性肺炎、心內膜炎、細菌性關節炎、膽管炎等 |
| 預測新適應症 | 感染性中耳炎 (Infectious Otitis Media) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cefazolin 屬於第一代頭孢菌素，一般認為是透過結合青黴素結合蛋白 (PBP)、抑制細菌細胞壁合成而殺菌。它對鏈球菌及對甲氧西林敏感的金黃色葡萄球菌 (MSSA) 等革蘭氏陽性菌有效，而這些菌可引起中耳炎。

原適應症（肺炎、心內膜炎、細菌性關節炎等）與中耳炎同屬細菌感染，致病菌有部分重疊，這是模型預測的合理基礎。

但限制也很明顯：Cefazolin 對流感嗜血桿菌 (H. influenzae) 和卡他莫拉菌 (M. catarrhalis) 的涵蓋有限，且注射劑型並非中耳炎的常規用藥。

另外，其他排名較前的預測（如非化膿性中耳炎、過敏性中耳炎、耳咽管炎）多為非細菌性或僅由模型分數支持，應視為本體論相近所致的可能假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | 病例報告/系列 | Ann Otol Rhinol Laryngol | 兒童 Gradenigo 症候群（急性中耳炎併發症）以 ceftazidime 加 cefazolin 經驗性治療；為合併療法，無法單獨評估 cefazolin 的貢獻 |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Stevens-Johnson 症候群的處置回顧，病例曾因中耳炎用藥；與 cefazolin 治療中耳炎的關聯很弱 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64519 | STAZOLIN POWDER FOR SOLUTION FOR INJECTION 1G | 注射用粉劑（依品名） | 未提供 |
| HK-34125 | CEFAZOLIN FOR INJ 1G (YUNG SHIN) | 注射劑（依品名） | 未提供 |
| HK-47264 | CEFAZOLIN SODIUM FOR INJ 1G | 注射劑（依品名） | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**：凝血功能障礙 (blood coagulation disease)、困難梭狀芽孢桿菌結腸炎 (Clostridium difficile colitis)、周產期壞死性腸炎、先天性凝血酶原缺乏症。此資料來自知識圖譜，並非仿單內容。
- **藥物交互作用**：共查得 100 筆，以下為主要項目。
  - 中度：Kanamycin、Neomycin、Streptomycin（皆為胺基糖苷類）、Picosulfuric acid
  - 其餘多為等級未知，例如 Amphotericin B、Metformin、Omeprazole、Morphine 等

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 感染性中耳炎沒有臨床試驗，文獻僅有合併療法的病例報告和間接資料，證據等級為 L4，主要仰賴模型分數。
- Cefazolin 對中耳炎常見致病菌（尤其是 H. influenzae、M. catarrhalis）的涵蓋不足，注射劑型也不符常規治療模式。
- 在預測清單中，化膿性中耳炎 (suppurative otitis media) 有一項 1982 年的日本對照研究（以 cefazolin 為對照組），是較具研究價值的方向，但該研究年代久遠，且並非為證實 cefazolin 療效而設計。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語和禁忌
- 補充作用機轉資料（MOA）
- 針對化膿性中耳炎，重新檢視 1982 年對照研究，並對照目前的細菌抗藥性資料
- 評估 cefazolin 對中耳炎常見致病菌的敏感性，以及相對於現行標準療法（如口服 amoxicillin）的定位
- 若要進一步研究，需設計能單獨評估 cefazolin 療效的臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

