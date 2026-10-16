---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Clarithromycin：預測新適應症為多發性株高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)（證據等級 L5）。原適應症：感染性中耳炎、鏈球菌感染、細菌性肺炎、金黃色葡萄球菌感染、上顎竇炎、黴漿菌肺炎、披衣菌肺炎等"
monitor_inn: "CLARITHROMYCIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
---

# Clarithromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Clarithromycin：從呼吸道與耳鼻喉細菌感染到多發性株高黏滯症候群

## 一句話總結

Clarithromycin 是巨環內酯類（macrolide）抗生素，原本用於中耳炎、肺炎、鼻竇炎等細菌感染。
TxGNN 模型預測它可能對**多發性株高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)** 有效，
但目前**沒有臨床試驗與文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 感染性中耳炎、鏈球菌感染、細菌性肺炎、金黃色葡萄球菌感染、上顎竇炎、黴漿菌肺炎、披衣菌肺炎等 |
| 預測新適應症 | 多發性株高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.35% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Clarithromycin 屬於巨環內酯類抗生素，在細菌感染的療效已被證實。巨環內酯類另有免疫調節與抗發炎作用（影響細胞激素產生）。

不過，目前沒有證據把這些作用與多株性丙種球蛋白病所致的血液高黏滯症連結起來。原適應症是細菌感染，與高黏滯症候群在病理上並無明顯關聯。0.993 的分數僅是知識圖譜上的預測，不能視為機轉或臨床支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

> 補充：預測排名第 2 的「高澱粉酶血症」僅有 1 篇 2004 年病例報告（PMID 15228140），內容為脫膿分枝桿菌肺部感染合併原發性巨澱粉酶血症，clarithromycin 在其中是用於治療感染，並非治療高澱粉酶血症，可能只是共同出現的假關聯。排名第 4 的「點狀上皮角膜結膜炎」有 1 篇 2024 年研究（PMID 38472959），探討瞼板腺炎相關角膜結膜炎的治療，可作為巨環內酯類的間接線索，但是否使用 clarithromycin 及研究設計仍待確認。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-38306 | KLACID TAB 500MG | 錠劑（500mg） | 未提供 |
| HK-35866 | KLACID TAB 250MG | 錠劑（250mg） | 未提供 |
| HK-43890 | KLACID FORTE TAB 500MG | 錠劑（500mg） | 未提供 |
| HK-54264 | CLACIN POWDER FOR ORAL SUSPENSION 125MG/5ML | 口服懸液用粉劑 | 未提供 |
| HK-67578 | CLACIN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 輸注濃縮液用粉劑 | 未提供 |

目前共 20 張有效單方許可證，皆為上市中，無已註銷者。

---

## 安全性考量

- **禁忌症（來自知識圖譜關聯，非仿單內容）**：
  - 心臟節律：長 QT 症候群、尖端扭轉型心室頻脈 (Torsades de pointes)、心室頻脈
  - 肝臟：肝衰竭、肝病、膽汁鬱積
  - 代謝：紫質症
  - 腎臟與其他：腎臟疾病、膽囊疾病、骨質疏鬆、骨折
  - 神經肌肉：重症肌無力
  - 腸道與感染：困難梭狀芽孢桿菌結腸炎、嬰兒壞死性腸炎、傳染性單核球增多症
- **藥物交互作用**：資料庫共查得 100 筆，以下為其中列出的較重要者：
  - 嚴重 (Major)：Abemaciclib、Fentanyl、Acalabrutinib
  - 中度 (Moderate)：Paclitaxel、Tramadol、Nifedipine、Ethinylestradiol、Hydrocortisone、Abiraterone、Afatinib 等
  - 輕度 (Minor)：Dolutegravir、Zidovudine、Loratadine

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測疾病無任何臨床試驗或文獻，也沒有機轉連結，僅有 TxGNN 圖譜分數，證據等級為 L5。
- 其他前幾名預測（高澱粉酶血症、先天性無白蛋白血症、血型不合）同樣缺乏可信的治療依據；僅「點狀上皮角膜結膜炎」有間接的類別層級線索（L4）。

**若要推進需要：**
- 補充 clarithromycin 的作用機轉資料
- 釐清預測疾病的臨床意義，並做系統性文獻檢索
- 確認 PMID 38472959 是否實際研究 clarithromycin 及其研究設計，可作為轉向角膜結膜炎方向的研究問題
- 取得香港衛生署仿單的警語與禁忌症，完成安全性評估
- 因 QT 延長與多種藥物交互作用風險，任何新適應症評估都需納入心電圖與併用藥物的監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

