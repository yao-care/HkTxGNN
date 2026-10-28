---
layout: default
title: Ceftolozane
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceftolozane：預測新適應症為淋球菌性尿道炎 (Gonococcal Urethritis)（證據等級 L5）。原適應症：泌尿道感染"
monitor_inn: "CEFTOLOZANE"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ceftolozane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Ceftolozane：從泌尿道感染到淋球菌性尿道炎
{: .text-alpha }

## 一句話總結

Ceftolozane 是一種頭孢菌素類（cephalosporin）抗生素，原本用於治療泌尿道感染。
TxGNN 模型預測它可能對**淋球菌性尿道炎 (Gonococcal Urethritis)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染 |
| 預測新適應症 | 淋球菌性尿道炎 (Gonococcal Urethritis) |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ceftolozane 屬於 beta-lactam 類的頭孢菌素，
一般認為其作用是抑制細菌的青黴素結合蛋白（penicillin-binding proteins），
進而干擾細胞壁合成。其在泌尿道感染中的療效已被證實。

TxGNN 給出高分，可能反映的是與其他用於淋病奈瑟菌（*Neisseria gonorrhoeae*）的頭孢菌素在類別上相似，
以及模型從尿道炎與泌尿生殖道感染等相關疾病之間學到的相似性；分數來自 TxGNN 模型（深度學習），並非生物學證據。

不過需要審慎看待：Ceftolozane 主要是針對革蘭氏陰性菌（如綠膿桿菌與腸內菌科）開發，
目前沒有資料顯示它對淋病奈瑟菌具有活性。因此這個預測目前只能視為假設，尚無實證支持。

**其他預測適應症的簡要評估**（均為 L5，除另有說明）：

| 預測適應症 | TxGNN 分數 | 合理性評估 |
|-----------|-----------|-----------|
| Ureaplasma 尿道炎 | 0.9989 | 該菌無細胞壁，beta-lactam 機轉上預期無效，生物學上不合理 |
| 子宮發炎性疾病 | 0.9988 | 僅有間接依據（Ceftolozane/tazobactam 已核准用於複雜性腹腔內感染），證據薄弱 |
| 黃色肉芽腫性腎盂腎炎 | 0.9988 | 有間接依據（已核准用於複雜性泌尿道感染含腎盂腎炎），但此病通常需手術處置，抗生素療效未確立；證據等級 L4 |
| 泌尿生殖道結核 | 0.9950 | 結核菌對多數 beta-lactam 天然抗藥，不合理 |
| 高澱粉酶血症、多形性高黏滯症候群、先天性無白蛋白血症、血型不合、癌前期血液系統疾病 | 0.9911–0.9952 | 非感染性疾病，無抗菌標靶；分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首位預測（淋球菌性尿道炎）目前無相關文獻。

以下為排名第 4 的預測適應症（黃色肉芽腫性腎盂腎炎）所附的唯一一篇文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Review | Current Opinion in Infectious Diseases | 回顧複雜性泌尿道感染（含腎盂腎炎與泌尿道敗血症）的文獻進展，並未直接評估 Ceftolozane |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65156 | ZERBAXA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1G/0.5G | 未提供 | 未提供 |

## 安全性考量

- **藥物交互作用**：共查得 11 項中度（Moderate）交互作用，包括：
  - 胺基糖苷類抗生素：Kanamycin、Neomycin、Streptomycin、Amikacin（含脂質體劑型）、Gentamicin
  - 抗凝血劑：Warfarin、Dicoumarol
  - 其他：Chloramphenicol、Ethinylestradiol、Mycophenolic acid

其餘警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（淋球菌性尿道炎）僅有模型分數，沒有臨床試驗與文獻，且缺乏 Ceftolozane 對淋病奈瑟菌有活性的資料。
- 排名前 10 的預測中，多數在機轉上不合理，或屬非感染性疾病；僅有黃色肉芽腫性腎盂腎炎具間接依據（L4），但療效仍未確立。

**若要推進需要：**
- 取得 Ceftolozane 對淋病奈瑟菌的體外藥敏（MIC）資料
- 補充詳細的作用機轉（MOA）資料
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 系統性檢索相關臨床前與臨床研究，再重新評估證據等級
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

