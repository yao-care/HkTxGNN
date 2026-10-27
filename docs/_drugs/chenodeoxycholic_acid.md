---
layout: default
title: Chenodeoxycholic Acid
parent: 中證據等級 (L3-L4)
nav_order: 183
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Chenodeoxycholic Acid：預測新適應症為同型合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia)（證據等級 L4）。原適應症：膽結石、膽囊結石、膽總管結石"
monitor_inn: "CHENODEOXYCHOLIC ACID"
predicted_indications: ["homozygous familial hypercholesterolemia", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "obsolete familial combined hyperlipidemia", "obsolete hyperuricemia (disease)"]
---

# Chenodeoxycholic Acid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

## Chenodeoxycholic Acid：從膽結石到同型合子家族性高膽固醇血症
{: .text-alpha }

## 一句話總結

Chenodeoxycholic Acid（CDCA，鵝去氧膽酸）是一種膽酸，原本用於膽結石（膽囊結石、膽總管結石）的治療。
TxGNN 模型預測它可能對**同型合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇間接相關的文獻**（腦腱黃瘤症的綜述），證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 膽結石、膽囊結石、膽總管結石（資料來源為知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 同型合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，CDCA 是一種膽酸，已用於膽結石的治療，也是腦腱黃瘤症 (CTX) 的既有療法。CTX 是 CYP27A1 缺損造成的膽酸合成異常疾病，會使膽固醇烷醇（cholestanol）及膽固醇在組織中堆積。CDCA 可恢復對 CYP7A1 的負回饋，抑制異常膽醇與膽固醇烷醇的生成。這顯示 CDCA 與脂質及固醇代謝有一定關聯。

但是，HoFH 的核心問題是 LDL 受體缺損導致 LDL 清除受損，膽酸的回饋抑制並不能直接矯正這個缺陷。因此兩者的連結是間接的。TxGNN 的高分很可能來自知識圖譜中共享的固醇代謝相鄰節點（例如 CTX 與黃色瘤），而非經過驗證的 HoFH 作用機轉。

另外，CDCA 在臨床使用中曾與 LDL 膽固醇上升有關，這對高膽固醇血症的情境反而是疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Review | Orphanet J Rare Dis | 腦腱黃瘤症 (CTX) 的綜合回顧：CYP27A1 突變導致膽酸合成下降及膽固醇烷醇堆積。此文獻探討的是 CTX，並非 HoFH，僅為間接相關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-39787 | SULISOU CAP 250MG (KOJAR) | 膠囊（品名標示為 CAP） | 許可證資料未載明 |

製造商：JULIUS CHEN & COMPANY (HK) LIMITED；狀態：有效（單方）。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關係資料，並非仿單文字）：肝病、膽囊疾病、腹瀉性疾病、膽汁淤積、良性復發性肝內膽汁淤積、家族性肝內膽汁淤積、硬化性膽管炎、原發性膽汁性膽管炎、Reynolds 症候群。
- **藥物交互作用**：共查得 56 筆，以下為其中中度（Moderate）者的主要例子：
  - 雌激素類：Ethinylestradiol、Estradiol、Conjugated estrogens
  - 降脂藥：Gemfibrozil、Fenofibrate、Clofibrate、Ezetimibe
  - 膽酸結合劑：Cholestyramine、Colesevelam、Colestipol
  - 其他：Aluminum hydroxide、Asparaginase 類、Brentuximab vedotin、Cannabidiol、Bedaquiline、Clofarabine、Anisindione

警語及正式禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何針對 HoFH 的臨床試驗或直接文獻，唯一的文獻談的是 CTX。TxGNN 高分很可能反映知識圖譜的鄰近關係，而非實際療效。
- CDCA 可能提高 LDL 膽固醇，與 HoFH 的治療目標相衝突；且知識圖譜顯示它對肝病、膽汁淤積等族群有禁忌風險。

**若要推進需要：**
- 補齊 CDCA 的作用機轉資料（如 DrugBank）。
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症。
- 評估 CDCA 對 LDL 膽固醇的影響，以及其用於 HoFH 的機轉合理性；必要時先做前臨床或小規模探索性研究。
- 其他預測（COL4A1 相關疾病、已過時的家族性複合型高脂血症及高尿酸血症術語）皆僅有模型預測（L5）、無機轉依據，且部分疾病術語已過時，需先對應到現行術語再評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

