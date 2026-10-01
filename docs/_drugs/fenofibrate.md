---
layout: default
title: Fenofibrate
parent: 中證據等級 (L3-L4)
nav_order: 363
evidence_level: L4
indication_count: 5
---

# Fenofibrate
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Fenofibrate：從血脂異常到同合子家族性高膽固醇血症

## 一句話總結

Fenofibrate 是一種降血脂藥，屬於 PPAR-alpha 促效劑（fibrate 類），主要用於降低三酸甘油酯。
TxGNN 模型預測它可能對**同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 有效，
但目前僅有 **1 個臨床試驗**（研究的是 alirocumab，不是 fenofibrate）和 **10 篇文獻**（多為綜述），沒有直接證據支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明；依藥理類別推論為血脂異常（高三酸甘油酯、混合型高脂血症） |
| 預測新適應症 | 同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知藥理，Fenofibrate 透過活化 PPAR-alpha，降低三酸甘油酯，並小幅降低 LDL-C。

HoFH 患者的 LDL 受體缺失或嚴重缺損。Fenofibrate 的降 LDL 效果主要靠增加 LDL 清除，在這類患者身上預期效果有限。
TxGNN 的高分（0.999）較可能來自藥物與整個高脂血症知識網路的關聯，而不是 HoFH 的特異機轉。
1984 年一項小型研究中，唯一的 HoFH 患者總膽固醇和 LDL-C 降幅最大，但只有 1 人，不足以支持結論。

目前 HoFH 的處置主要靠高強度降 LDL 治療，例如 PCSK9 抑制劑、lomitapide、LDL 血漿分離術，嚴重時考慮肝臟移植。Fenofibrate 即使有效，也只可能是輔助角色。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 完成 | 18 | 開放標籤試驗，評估 alirocumab 用於 8-17 歲 HoFH 兒童與青少年的 LDL-C 降幅。研究藥物不是 fenofibrate，無法提供直接證據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | 22 名 II 型高脂蛋白血症患者用 fenofibrate 4-12 個月，LDL-C 降 24%。其中 1 名 HoFH 患者降幅最大 |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Intern Med J | HoFH 的肝臟移植治療案例與新興降脂療法。標準降脂藥與 LDL 血漿分離術效果可能不足 |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | 兒童與青少年血脂異常的藥物與手術治療，提到 fenofibrate 等藥物在家族性高膽固醇血症中曾有降脂成效 |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | 非史他汀降脂藥綜述。Fenofibrate 單方最明確的適應症是空腹三酸甘油酯 >500 mg/dl，可降低急性胰臟炎風險 |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Curr Atheroscler Rep | 妊娠期血脂異常的處置，與 HoFH 關聯間接 |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart J | LDL 膽固醇、史他汀與 PCSK9 抑制劑綜述，重度高膽固醇血症以史他汀、ezetimibe 等為主 |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Ezetimibe 膽固醇吸收抑制劑的介紹，與 fenofibrate 無直接關係 |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin 藥理與治療潛力綜述，與 fenofibrate 無直接關係 |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE 血脂異常處置與心血管疾病預防指引 |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | 藥動學研究 | Pharmacotherapy | Lomitapide（HoFH 核准用藥）與 fenofibrate 等降脂藥的藥物動力學交互作用 |

## 香港上市資訊

香港共有 19 張許可證，以下列出 5 張主要許可證。資料中未記載劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-59427 | FENOGET CAP 200MG | CHARIOT PHARMA LIMITED |
| HK-50649 | LIPANTHYL SUPRA TAB 160MG | ABBOTT LAB LTD |
| HK-53289 | LEXEMIN CAP 100MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-59426 | FENOGET CAP 67MG | CHARIOT PHARMA LIMITED |
| HK-67885 | LIPANTHYL MICRO CAPSULES 267MG | ABBOTT LAB LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一的臨床試驗研究的是 alirocumab，不是 fenofibrate。文獻只有零星的小型早期研究和綜述。
- 機轉上，HoFH 的 LDL 受體缺失，fenofibrate 的降 LDL 途徑預期效果有限，高預測分數更可能反映模型的網路關聯。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料（目前為阻擋性缺口，無法進入安全性篩選）
- 補齊 DrugBank 的作用機轉資料
- 系統性檢索 fenofibrate 用於 HoFH 的臨床研究，確認是否有比 1984 年單一病例更直接的證據
- 若仍想探索血脂領域，同一份預測中的**高脂蛋白血症 (Hyperlipoproteinemia)** 有多個已完成的 Phase 3 RCT 支持（證據等級 L1，評估為 Proceed with Guardrails）。但這很可能是既有或已確立的用途，而非真正的老藥新用，且需先確認香港許可證核准的適應症

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

