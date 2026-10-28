---
layout: default
title: Chenodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 5
monitor_inn: "CHENODEOXYCHOLIC ACID"
predicted_indications: ["homozygous familial hypercholesterolemia", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "obsolete familial combined hyperlipidemia", "obsolete hyperuricemia (disease)"]
last_modified_at: 2026-10-28
description: "Chenodeoxycholic Acid：預測新適應症為同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Chenodeoxycholic Acid
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

## Chenodeoxycholic Acid：膽酸類藥物 → 同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia)
{: .text-alpha }

## 一句話總結

Chenodeoxycholic Acid（鵝去氧膽酸，CDCA）是一種膽酸類藥物。
TxGNN 模型預測它可能對**同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia)** 有效，
但目前**沒有直接研究此疾病的臨床試驗或文獻**，僅有 1 篇相關疾病（腦腱黃色瘤病）的綜論，證據屬於模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia) |
| TxGNN 預測分數 | 0.9957 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 CDCA 是膽酸，參與膽固醇與膽酸代謝的回饋調控。在腦腱黃色瘤病（CTX，一種 CYP27A1 缺陷導致的膽酸合成障礙）中，CDCA 被用來恢復對 CYP7A1 的負回饋，抑制異常膽固醇醇（cholestanol）與膽酸醇的生成。這顯示 CDCA 與脂質、固醇代謝有一定關聯。

然而，同合子家族性高膽固醇血症的核心問題是 LDL 受體缺陷造成的 LDL 清除受損，膽酸的回饋抑制機制並不能直接矯正這個缺陷，因此兩者的機轉連結是間接的。高分數較可能反映了模型中與固醇代謝相關疾病（如 CTX）的相鄰關係，而非經過驗證的機轉。

此外，臨床上 CDCA 曾被觀察到可能使 LDL 膽固醇上升，這對高膽固醇血症的使用情境是需要特別留意的疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻研究的是相關疾病（腦腱黃色瘤病），並非預測的同合子家族性高膽固醇血症本身：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Review | Orphanet J Rare Dis | 腦腱黃色瘤病的發病機轉、臨床表現、診斷與處置綜論；該病由 CYP27A1 突變造成膽酸合成減少與膽固醇醇堆積 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-39787 | SULISOU CAP 250MG (KOJAR) | 未記載 | 本地資料未記載 |

---

## 安全性考量

- **藥物交互作用**：共查得 56 項交互作用，以下為部分中度等級項目：
  - 雌激素類：Ethinylestradiol、Estradiol、Conjugated estrogens
  - 降血脂藥：Gemfibrozil、Fenofibrate、Clofibrate、Ezetimibe
  - 膽酸結合劑：Cholestyramine、Colesevelam、Colestipol
  - 含鋁制酸劑：Aluminum hydroxide
  - 其他：Asparaginase 類、Brentuximab vedotin、Cannabidiol、Bedaquiline、Clofarabine

其他警語與禁忌資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 CDCA 用於同合子家族性高膽固醇血症，僅有模型分數與相關疾病的間接線索。
- 此疾病的核心缺陷（LDL 受體功能不足）與 CDCA 的作用機轉並無直接對應，且 CDCA 可能升高 LDL 膽固醇。

**若要推進需要：**
- 補充 CDCA 作用機轉資料，並評估其對 LDL 清除路徑的實際影響
- 檢索直接針對同合子家族性高膽固醇血症的臨床或前臨床研究
- 取得原廠仿單的警語與禁忌資訊，進行安全性篩選
- 與現有標準治療（如他汀類、PCSK9 抑制劑等）比較，釐清潛在定位
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

