---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 5
monitor_inn: "CLARITHROMYCIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
last_modified_at: 2026-10-28
description: "Clarithromycin：預測新適應症為高澱粉酶血症 (Hyperamylasemia)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯包括中耳炎、鏈球菌感染、細菌性肺炎、上顎竇炎、黴漿菌肺炎等"
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Clarithromycin：從呼吸道與耳鼻喉細菌感染到高澱粉酶血症
{: .text-alpha }

## 一句話總結

Clarithromycin 是一種大環內酯類抗生素，在知識圖譜中記錄的用途為中耳炎、鏈球菌感染、細菌性肺炎、上顎竇炎等感染症。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前**沒有臨床試驗**，只有 **1 篇個案報告**，且該報告並未直接研究以 clarithromycin 治療此疾病，因此證據極為薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯包括中耳炎、鏈球菌感染、細菌性肺炎、上顎竇炎、黴漿菌肺炎等（香港許可證資料未提供適應症文字） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 0.9935 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 核准數 | 至少 20 張許可證（清單可能不完整） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Clarithromycin 屬於大環內酯類抗生素，一般認為其作用是抑制細菌蛋白質合成，並具有免疫調節特性，但這些內容並非來自本報告所彙整的機轉資料，僅供參考。

目前找不到合理的直接機轉，說明 clarithromycin 能治療高澱粉酶血症。唯一檢索到的文獻是 2004 年日本的個案報告，內容是脂膜分枝桿菌（M. abscessus）肺部感染合併原發性巨澱粉酶血症，高澱粉酶血症是病人的伴隨狀況，並非治療標的。大環內酯類相關的胰酵素上升也不是已知的治療效果。

因此，0.9935 的 TxGNN 模型（深度學習）分數僅屬計算預測，可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | 個案報告 | Nihon Kokyuki Gakkai zasshi | 一名 76 歲男性的 M. abscessus 肺部感染合併原發性巨澱粉酶血症；並非研究以 clarithromycin 治療高澱粉酶血症 |

---

## 香港上市資訊

以下為已列出的許可證（資料顯示至少 20 張，清單可能不完整，此處列出 5 張）。許可證資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-54399 | VICK-CLARCID TAB 250MG | VICKMANS LABORATORIES LTD |
| HK-67578 | CLACIN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | JACOBSON MARKETING LIMITED |
| HK-54294 | CLACIN PLUS TAB 500MG | APT PHARMA LIMITED |
| HK-67473 | CLARITHROPHIL TABLETS 250MG | CROSS WORLD PHARMA |
| HK-38306 | KLACID TAB 500MG | ABBOTT LAB LTD |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：長 QT 症候群、尖端扭轉型心律不整、心室頻脈、肝衰竭、肝病、膽汁鬱積、腎臟病、紫質症、重症肌無力、困難梭狀芽孢桿菌結腸炎、骨質疏鬆、傳染性單核球增多症等。
- **藥物交互作用**：資料庫共查得 100 筆交互作用，其中列出的重大 (Major) 等級包括 Abemaciclib、Fentanyl、Acalabrutinib；中度 (Moderate) 包括 Paclitaxel、Tramadol、Nifedipine、Ethinylestradiol、Hydrocortisone 等。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何直接研究此疾病的臨床試驗或文獻，證據等級為 L5；唯一的文獻是個案報告，並非評估療效。
- 機轉上看不出合理連結，高分僅反映模型的計算預測。

**若要推進需要：**
- 取得 clarithromycin 的作用機轉資料，並評估其與澱粉酶代謝的可能關聯。
- 找出直接針對高澱粉酶血症的臨床或前臨床研究。
- 補齊香港仿單的警語、禁忌與適應症文字。
- 若仍有興趣，優先考慮其他排名候選（如點狀上皮角結膜炎，目前亦僅屬間接證據，須進一步確認）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

