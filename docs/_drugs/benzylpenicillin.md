---
layout: default
title: Benzylpenicillin
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Benzylpenicillin：預測新適應症為冠周炎 (Pericoronitis)（證據等級 L5）。原適應症：鏈球菌感染、腦膜炎球菌感染、肺炎鏈球菌腦膜炎、炭疽、心內膜炎、金黃色葡萄球菌感染等"
---

# Benzylpenicillin
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

# Benzylpenicillin：從鏈球菌感染等細菌性感染到牙周炎（Pericoronitis）

## 一句話總結

Benzylpenicillin（青黴素 G）是經典的注射用 β-內醯胺類抗生素，原本用於鏈球菌感染、腦膜炎、心內膜炎、炭疽等多種細菌性感染。
TxGNN 模型預測它可能對**冠周炎 (Pericoronitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測的研究假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鏈球菌感染、腦膜炎球菌感染、肺炎鏈球菌腦膜炎、炭疽、心內膜炎、金黃色葡萄球菌感染等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 冠周炎 (Pericoronitis) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold（僅列為研究問題） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Benzylpenicillin 屬於青黴素類抗生素，一般認為其作用是抑制細菌細胞壁合成而產生殺菌效果，對鏈球菌等敏感菌有效。

冠周炎是由鏈球菌與厭氧菌等引起的多菌種牙源性感染，這些菌多半對青黴素敏感，因此在機轉上有合理性。不過，牙源性感染通常使用口服青黴素（如 penicillin V、amoxicillin），注射型 benzylpenicillin 主要可能用於嚴重病例。

需要注意的是，TxGNN 分數僅為模型預測，並無實際研究佐證。同一份預測清單中的其他口腔疾病（如牙齦萎縮、口瘡、白斑）與抗菌機轉關聯薄弱，顯示高分可能部分反映知識圖譜中與口腔疾病節點的鄰近性，而非真實療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43500 | PAN-PENICILLIN G SOD FOR INJ 1M IU | 注射劑 | 未提供 |
| HK-60173 | NORAPENY FOR IM/IV INJ 1000000IU | 注射劑（肌肉／靜脈） | 未提供 |
| HK-68195 | PENICILLIN G SODIUM SANDOZ POWDER FOR SOLUTION FOR INJECTION/INFUSION 1000000IU | 注射／輸注用粉末 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（非仿單文字，僅供參考）：腎臟疾病、輸尿管積膿、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、傳染性單核球增多症、慢性 Epstein-Barr 病毒感染症候群。
- **藥物交互作用**：共查得 21 項，主要如下：
  - **重大 (Major)**：Methotrexate（可能降低其排除而增加毒性，應謹慎）
  - **中度 (Moderate)**：Doxycycline、Minocycline、Tetracycline、Oxytetracycline、Demeclocycline（四環素類）、Chloramphenicol、Warfarin、Dicoumarol、Ethinylestradiol、Mycophenolic acid、Picosulfuric acid、Iodide I-123、Iodide I-131
  - 另有輕度（Clarithromycin、Erythromycin）及等級未明（Salbutamol、Acyclovir、Gentamicin、Levothyroxine）的交互作用。

主要警語與正式禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 冠周炎的預測僅有模型分數，無任何臨床試驗或文獻佐證（L5）。雖然抗菌機轉在牙源性感染上有合理性，但臨床上已有口服青黴素等標準選擇，注射型的新增價值有限。

**若要推進需要：**
- 補充作用機轉資料（MOA）及香港許可證的核准適應症與仿單警語、禁忌症
- 系統性檢索冠周炎抗生素治療的臨床試驗與文獻，並與現行標準療法（口服青黴素、amoxicillin 等）比較
- 釐清注射給藥是否適用於重症冠周炎的情境（給藥途徑相容性評估）
- 完成安全性篩選，特別是與 methotrexate 等藥物的交互作用，以及腎功能不全患者的使用考量
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

