---
layout: default
title: Fluorometholone
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 5
---

# Fluorometholone
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

# Fluorometholone：從眼用局部類固醇到感染後血管炎

## 一句話總結

Fluorometholone 是局部用糖皮質類固醇，在香港以眼藥水劑型上市。
TxGNN 模型預測它可能對**感染後血管炎 (Postinfectious Vasculitis)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 感染後血管炎 (Postinfectious Vasculitis) |
| TxGNN 預測分數 | 99.91%（全體排名 2453） |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fluorometholone 屬於糖皮質類固醇類別，其抗發炎作用在眼科發炎性疾病中已被廣泛使用。從類別層級來看，全身性類固醇確實是免疫介導型血管炎的可能治療方向。

但這個推論有明顯限制。Fluorometholone 在香港僅有眼用劑型，全身暴露量極低，難以達到治療血管炎所需的藥物濃度。目前沒有任何針對此藥物與此疾病的專屬證據，路徑相容性（劑型與給藥途徑）也尚未評估。

因此，這個預測較適合視為研究線索，還不能作為臨床應用的依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症（供參考）

TxGNN 對此藥物另有 4 個預測結果。其中有試驗資料的是「感染後疾患 (Post-bacterial Disorder)」，證據等級為 L4，建議為「研究問題 (Research Question)」。

| 預測適應症 | 分數 | 證據等級 | 建議 | 說明 |
|-----------|------|---------|------|------|
| 細菌感染後疾患 (Post-bacterial Disorder) | 99.91% | L4 | Research Question | 有 2 個相關試驗，見下方 |
| 外耳炎 (Otitis Externa) | 99.90% | L5 | Hold | 僅有模型預測，無耳用劑型與安全性資料 |
| 感染性尿道狹窄 (Infective Urethral Stricture) | 99.90% | L5 | Hold | 僅有模型預測，無劑型與證據 |
| 感染後症候群 (Post-infectious Syndrome) | 99.90% | L4 | Hold | 詞彙過於籠統，可能來自本體論的寬鬆對應 |

「細菌感染後疾患」相關試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07308938](https://clinicaltrials.gov/study/NCT07308938) | Phase 2 | 尚未招募 | 174 | 評估局部 fluorometholone 作為細菌性角膜潰瘍輔助療法，3 個月時最佳矯正視力是否優於單用抗生素 |
| [NCT01949454](https://clinicaltrials.gov/study/NCT01949454) | 不適用 (NA) | 完成 | 154 | 沙眼性倒睫手術圍手術期使用 0.1% fluorometholone，觀察能否降低倒睫復發；未提供結果 |

這兩個試驗都僅能產生假說，尚無結果數據。細菌性角膜炎使用類固醇需審慎評估，風險包括延遲癒合與感染持續。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-34273 | FLUMETHOLON EYE DROPS 0.1% | Santen Pharmaceutical (Hong Kong) Limited |
| HK-34274 | FLUMETHOLON EYE DROPS 0.02% | Santen Pharmaceutical (Hong Kong) Limited |
| HK-54720 | TOLON EYE DROPS 0.1% | Lafarge Co., Limited |
| HK-64966 | FULUSON OPHTHALMIC SOLUTION 0.1% W/V | LSB (HK) Limited |
| HK-19538 | FML LIQUIFILM OPHTHALMIC SUSP 0.1% | Allergan Hong Kong Limited |

香港共登記 6 張許可證，上表列出其中 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（感染後血管炎）僅有模型分數，沒有試驗或文獻，證據等級為 L5。
- 藥物只有眼用劑型、全身暴露極低，與血管炎的治療需求有明顯落差。

**若要推進需要：**
- 補齊 Fluorometholone 的作用機轉資料（DrugBank）。
- 取得香港衛生署仿單，確認警語與禁忌症。
- 評估劑型與給藥途徑是否與血管炎相容。
- 若要優先探索，建議改看「細菌感染後疾患」（角膜潰瘍輔助治療）。可追蹤 NCT07308938 的進展，並先做類固醇安全性審查。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

