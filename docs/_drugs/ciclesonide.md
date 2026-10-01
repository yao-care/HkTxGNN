---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ciclesonide：從吸入／鼻用類固醇到異位性皮膚炎

## 一句話總結

Ciclesonide 是一種糖皮質激素類藥物，香港目前有吸入劑（ALVESCO）與鼻噴劑（OMNARIS）上市。
TxGNN 模型預測它可能對**異位性皮膚炎 (Atopic Eczema)** 有效，分數很高。
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未提供適應症文字 |
| 預測新適應症 | 異位性皮膚炎 (Atopic Eczema) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Ciclesonide 是糖皮質激素前驅藥，經酯酶活化為 des-ciclesonide，再作用於糖皮質激素受體，產生抗發炎效果。

異位性皮膚炎屬於 Th2 主導的皮膚發炎，糖皮質激素的抗發炎作用在機轉上可能適用。這個推論只來自一般藥理，沒有本案的直接證據。

要注意的是，模型同時列出「atopic eczema」與「dermatitis, atopic」兩個節點（排名 1 與 3），指的是同一疾病，應合併，避免把同一訊號重複計算。另外，目前上市的劑型是吸入與鼻用，能否用於皮膚仍待確認。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症的參考資訊

| 預測適應症 | TxGNN 分數 | 證據 | 評估 |
|-----------|-----------|------|------|
| 2-hydroxyethyl methacrylate sensitization | 99.76% | 無 | 屬過敏原暴露狀態而非可治療疾病，治療理由薄弱 |
| bronchitis | 99.70% | 1 篇芬蘭 COPD 指引（[25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/)，2015） | 只涵蓋穩定期 COPD，屬間接證據 |
| contact dermatitis | 99.25% | 1 篇病例報告（[22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)，2012） | 屬過敏安全性訊號，不是療效證據 |
| asthma-related traits, susceptibility to | 99.13% | 無 | 屬遺傳易感性，需先對應到臨床氣喘適應症 |

## 香港上市資訊

| 許可證號 | 品名 | 持證商 |
|---------|------|--------|
| HK-53034 | ALVESCO 80 INHALER 80MCG/ACTUATION | DKSH HONG KONG LIMITED |
| HK-53035 | ALVESCO 160 INHALER 160MCG/ACTUATION | DKSH HONG KONG LIMITED |
| HK-59322 | OMNARIS NASAL SPRAY 50MCG | DKSH HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中有一篇病例報告：吸入 budesonide 引發系統性過敏性皮膚炎，貼膚試驗顯示與 ciclesonide 有交叉反應。對已知有糖皮質激素接觸過敏的患者，需留意交叉過敏風險。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測適應症沒有任何臨床試驗或文獻，證據等級僅 L5，分數再高也只是模型預測。
- 目前上市劑型（吸入、鼻噴）與皮膚適應症所需的給藥途徑可能不符，安全性資料也不完整。

**若要推進需要：**
- 補齊作用機轉資料（DrugBank）
- 取得香港衛生署仿單，完成警語與禁忌症審查
- 合併重複的疾病節點（atopic eczema 與 dermatitis, atopic）
- 檢索 ClinicalTrials.gov 與 PubMed，確認是否有 ciclesonide 用於異位性皮膚炎的研究
- 評估給藥途徑的可行性（是否需要外用劑型）

本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

