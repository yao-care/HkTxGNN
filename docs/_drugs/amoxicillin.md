---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Amoxicillin：預測新適應症為多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)（證據等級 L5）。原適應症：泌尿道感染、感染性中耳炎、鏈球菌感染、細菌性肺炎、金黃色葡萄球菌感染、咽炎等"
monitor_inn: "AMOXICILLIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin：從細菌感染到多株性高黏滯症候群

## 一句話總結

Amoxicillin 是 β-內醯胺類抗生素，原本用於泌尿道感染、中耳炎、肺炎、咽炎等多種細菌感染。
TxGNN 模型預測它可能對**多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)** 有效，但目前**沒有任何臨床試驗與文獻**支持，僅為模型預測（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染、感染性中耳炎、鏈球菌感染、細菌性肺炎、金黃色葡萄球菌感染、咽炎等（依 TxGNN 知識圖譜） |
| 預測新適應症 | 多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Amoxicillin 是 β-內醯胺類抗菌藥物，透過抑制細菌細胞壁合成而殺菌。

多株性高黏滯症候群是由血清免疫球蛋白升高所致，並非感染性疾病。Amoxicillin 與此病之間**沒有可信的機轉關聯**。0.996 的高分較可能反映知識圖譜中與感染或免疫球蛋白相關節點的網路鄰近性，而非真實的治療效果。

其他排名前列的預測（高澱粉酶血症、先天性無白蛋白血症、血型不合、單株免疫球蛋白病變等）同樣缺乏機轉依據與實證支持。唯一生物學上較為合理的是**敗血性鼠疫**（排名第 8，僅有體外與動物研究，屬 L4），但 β-內醯胺並非鼠疫標準療法，對細胞內的鼠疫桿菌活性有限，不太可能優於現行的胺基糖苷類、氟喹諾酮類或四環素類。

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
| HK-52757 | PROMOX CAP 500MG | 膠囊 | — |
| HK-35653 | AMOXICAP 250 CAP | 膠囊 | — |
| HK-39546 | AMOXYCILLIN CAP 250MG (BRIGHT FUTURE) | 膠囊 | — |
| HK-55778 | AMOXICILLIN ORAL SUSPENSION BP 125MG/5ML | 口服懸液 | — |
| HK-56083 | T.V. MOX CAP 500MG | 膠囊 | — |

（共 20 張有效單方許可證，上表僅列出 5 張；本次資料未提供核准適應症文字。）

---

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容）**：長 QT 症候群、尖端扭轉型心律不整、肝衰竭、肝病、腎病、紫質症、困難梭狀芽孢桿菌結腸炎、重症肌無力、膽汁鬱積、心室頻脈、骨質疏鬆、骨折、傳染性單核球增多症等。此為模型圖譜資料，須與仿單核對後再採信。
- **藥物交互作用**（共 100 筆，列出主要者）：
  - **重大**：Methotrexate、霍亂活疫苗 (Vibrio cholerae CVD 103-HgR)
  - **中度**：Doxycycline、Minocycline、Demeclocycline、Ethinylestradiol、Estradiol、Anisindione、Dicoumarol、Balsalazide、Entecavir、Mycophenolate mofetil
  - **輕微**：Allopurinol、Amiloride、Azithromycin、Clarithromycin、Erythromycin

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但所有預測適應症皆無臨床試驗支持，也缺乏可信的機轉關聯，屬純模型預測（L5）。
- 少數檢索到的資料僅為感染併發症的個案報告或間接的試驗，不構成再利用證據。

**若要推進需要：**
- 補齊 Amoxicillin 的作用機轉資料與香港仿單的警語、禁忌資料
- 若要探索，優先考慮生物學上較合理的**敗血性鼠疫**，需先進行細胞內活性與動物模型的比較性前臨床驗證
- 其餘預測（多株性高黏滯症候群、高澱粉酶血症等）建議不投入資源，除非有新的機轉證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

