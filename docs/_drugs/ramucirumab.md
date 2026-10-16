---
layout: default
title: Ramucirumab
parent: 僅模型預測 (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ramucirumab：預測新適應症為子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma)（證據等級 L5）。原適應症：非小細胞肺癌、胃腺癌、肝細胞癌"
monitor_inn: "Ramucirumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Ramucirumab
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

# Ramucirumab：從肺癌／胃癌／肝癌到子宮韌帶腺癌

## 一句話總結

Ramucirumab 是一種 VEGFR2 拮抗型單株抗體，原本用於非小細胞肺癌、胃腺癌及肝細胞癌等腫瘤。
TxGNN 模型預測它可能對**子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、胃腺癌、肝細胞癌（依知識圖譜適應症；香港許可證未載明適應症文字） |
| 預測新適應症 | 子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位未提供）。依已知資訊，Ramucirumab 是 VEGFR2 拮抗型抗體，透過阻斷 VEGF 訊號來抑制腫瘤血管新生，其療效已在胃腺癌、肺癌、肝癌等適應症中被研究。

婦科腺癌中 VEGF 訊號通常相當活躍，因此抗血管新生策略在機轉上有合理性。例如，抗 VEGF-A 的 bevacizumab 在子宮頸癌已有明確角色，可提供間接的生物學依據。

不過，此預測缺乏針對這個罕見疾病的任何資料，高分（99.95%）屬於計算模型的結果，不等同臨床證據。

**其他高分預測（皆為 L5、Hold）：** 子宮頸內膜癌 (endocervical carcinoma)、子宮頸腺樣囊性癌、子宮韌帶漿液性／子宮內膜樣／透明細胞／黏液性腺癌、子宮頸印戒細胞型與腸型黏液腺癌、子宮頸腺鱗癌（毛玻璃細胞型）。這些預測同樣沒有臨床試驗或文獻佐證，多半反映本體論（ontology）上與子宮頸、腺癌相關術語的接近程度，而非疾病特異性的生物學。

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
| HK-64422 | CYRAMZA CONCENTRATE FOR SOLUTION FOR INFUSION 500MG/50ML（製造商：ELI LILLY ASIA, INC.） | 輸注用濃縮液 | 未提供 |
| HK-64421 | CYRAMZA CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/10ML（製造商：ELI LILLY ASIA, INC.） | 輸注用濃縮液 | 未提供 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（VEGFR2 單株抗體），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用：** 已查詢到 100 筆交互作用紀錄，以下為其中主要項目：
  - **Major（重大）：** Acetylsalicylic acid（阿斯匹靈）、Deferasirox、Ibritumomab tiuxetan、Tositumomab（含 I-131）；以及多種抗凝血／抗血小板／溶栓藥物，包括 Abciximab、Alteplase、Antithrombin III、Apixaban、Betrixaban、Bivalirudin、Cangrelor、Caplacizumab、Cilostazol、Clopidogrel、Dalteparin、Defibrotide。整體而言，需特別留意與影響凝血或血小板功能藥物併用時的出血風險。
  - **Moderate（中度）：** Dexfenfluramine、Fenfluramine、Sibutramine。

主要警語與禁忌症的資料目前缺漏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都僅有 TxGNN 模型分數，沒有臨床試驗、文獻或機轉研究支持，證據等級為 L5。
- 原始作用機轉與仿單安全性資料缺漏，尚無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌症與核准適應症），完成安全性篩選
- 補充 DrugBank 的作用機轉資料，進行機轉關聯分析
- 針對子宮頸／婦科腺癌系統性檢索 Ramucirumab 的臨床試驗、文獻與前臨床資料
- 評估這些罕見組織型別的實際可及病人族群，以及是否有更合適的已有證據之抗血管新生藥物（如 bevacizumab）可作為對照
- 在取得至少前臨床或觀察性證據後，再重新評估是否升級決策
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

