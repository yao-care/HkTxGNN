---
layout: default
title: Propylene Glycol
parent: 中證據等級 (L3-L4)
nav_order: 621
evidence_level: L4
indication_count: 5
---

# Propylene Glycol
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

# PROPYLENE GLYCOL（丙二醇）：從藥用賦形劑到支氣管炎（預測方向存疑）

## 一句話總結

PROPYLENE GLYCOL（丙二醇，DrugBank DB01839）本身並非以特定適應症核准的活性藥物成分，目前在台灣尚未上市，藥典上主要作為溶劑/賦形劑使用。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效（預測分數 99.90%），
但現有 **4 個臨床試驗**與 **3 篇文獻**檢視後發現，證據並不支持這個方向——試驗受試藥物實際上是另一種藥物（環孢素吸入液），文獻則指向丙二醇可能是氣道刺激的風險因子而非治療手段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無明確核准適應症（丙二醇為藥典常用賦形劑/溶劑，非以此身分核准之治療用藥） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.90%（rank 2736） |
| 證據等級 | L4 |
| 上市狀態 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏丙二醇的詳細作用機轉資料（MOA: Data Gap）。丙二醇是藥典中常見的溶劑/賦形劑成分，並非以獨立藥理作用治療特定疾病而核准使用，因此本身沒有已知支持治療支氣管炎的機轉假說。

檢視支持證據後發現關聯性薄弱：4 個臨床試驗的受試藥物實際上都是 **Cyclosporine Inhalation Solution（環孢素吸入液）**，用於治療肺移植/幹細胞移植後的閉塞性細支氣管炎症候群（Bronchiolitis Obliterans Syndrome），丙二醇最多只是吸入配方中的溶劑角色，並非受試的治療標的。

更值得注意的是，3 篇相關文獻中有 2 篇是電子煙（e-cigarette）健康影響的回顧文章，內容指出丙二醇作為霧化液主要成分之一，可能是造成氣道刺激、氣喘與慢性阻塞性肺病惡化的**潛在危險因子**，方向與「治療支氣管炎」相反，屬於安全疑慮訊號而非療效訊號。第三篇為 COPD 動物模型研究，探討的是槲皮素（quercetin）的抗發炎效果，與丙二醇無直接關聯。整體而言，TxGNN 預測的分數雖高，但目前蒐集到的證據並未支持這個方向，反而出現與預測相反的安全性訊號。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | 完成 | 25 | 環孢素吸入液用於肺移植/幹細胞移植後閉塞性細支氣管炎症候群，非丙二醇本體 |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | 已終止 | 17 | 環孢素吸入液延伸追蹤研究，用於預防肺移植後慢性排斥；已終止 |
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | 完成 | 284 | 環孢素吸入液用於改善肺移植後閉塞性細支氣管炎症候群無病存活率 |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | 完成 | 7 | 環孢素吸入液擴大使用研究，用於治療閉塞性細支氣管炎 |

> 以上 4 個試驗的受試藥物皆為環孢素吸入液，丙二醇非治療標的，相關性均評為 C 級（低度相關）。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | 探討電子煙慢性使用是否導致肺病；丙二醇為霧化液常見成分之一 |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | 電子煙成分與氣喘潛在關聯之回顧，指出霧化液可能含氣道刺激物 |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Animal model study (mice) | Respiratory Research | 槲皮素於彈性蛋白酶/LPS 誘發 COPD 小鼠模型中的抗發炎效果；與丙二醇無直接關聯 |

## 安全性考量

安全性資訊請參考原廠仿單。目前台灣藥監局仿單警語、禁忌症與藥物交互作用資料均為資料缺口（見證據包 DG001，屬 Blocking 等級，尚無法進行 S1 安全性初評）。

## 結論與下一步

**決策：Hold**

**理由：**
- 臨床試驗證據皆指向另一藥物（環孢素吸入液），與丙二醇本體無直接因果關聯；文獻證據方向甚至與預測相反（丙二醇可能是氣道刺激/氣喘風險因子而非治療手段），機轉假說不成立。
- 藥物本身缺乏 MOA 資料，且台灣未上市、無核准適應症基礎可供比對，證據等級僅 L4 且方向矛盾。

**其他預測候選（同一藥物）：**
- 糖尿病視網膜病變（diabetic retinopathy，分數 99.68%）證據等級 L4、決策階段 S1（Research Question），為 5 個候選中相對最值得後續追蹤者，但關鍵文獻探討的是丙二醇的衍生酯類（丙二醇甘露酸硫酸酯），非丙二醇本體，藥理活性不可直接外推。
- 重度非增殖性糖尿病視網膜病變、皮質性白內障、核性老年白內障三項僅有 TxGNN 分數（L5），無任何臨床試驗或文獻支持，同為 Hold。

**若要推進需要：**
- 補齊 TFDA 仿單警語/禁忌症資料，解除 S1 安全性初評的 Blocking 缺口（DG001）
- 取得 DrugBank 或其他來源的丙二醇作用機轉資料（DG002）
- 針對丙二醇本體（而非衍生物或作為賦形劑角色）在支氣管炎/糖尿病視網膜病變的直接體外或機轉研究，以釐清是否存在真實治療潛力
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

