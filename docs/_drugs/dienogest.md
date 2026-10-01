---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest：從子宮內膜異位症到閉經

## 一句話總結

Dienogest 是一種黃體素類藥物，臨床上主要用於子宮內膜異位症。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，但閉經其實是 dienogest 已知的藥理作用（出血型態改變），並非治療目標。
目前有 4 個相關臨床試驗和 6 篇文獻，但**全部都在研究子宮內膜異位症，沒有任何一項直接針對閉經的療效**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 子宮內膜異位症（依相關試驗與 Visanne 產品推斷；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5（無任何研究以閉經為治療標的；系統自動標示為 L4，但沒有機轉或前臨床研究支持） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，dienogest 是選擇性黃體素類藥物，會抑制子宮內膜增生與排卵，因此使用者常出現月經停止或出血型態改變。

這正是預測分數偏高的可能原因：知識圖譜中「藥物－閉經」的關聯，很可能反映的是這個**藥物副作用或藥理效應**，而不是治療效益。閉經在子宮內膜異位症治療中，最多只是達到症狀控制的手段之一，不是需要被治療的疾病。

其餘 9 個預測適應症（如原發性卵巢衰竭、乳房纖維囊腫、生長激素缺乏症、染色體異常症候群等）證據同樣薄弱，均為 L5 或間接證據，建議一律 Hold。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | 完成 | 968 | 真實世界使用 Visanne 治療子宮內膜異位症；可能記錄出血結果，但未以閉經為主題 |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | 進行中（不再招募） | 138 | 比較經皮雌二醇加 dienogest 與 drospirenone 治療子宮內膜異位症的病人滿意度 |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | 招募中 | 290 | Indinol Forto 與 Visanne 2 mg 的非劣性隨機試驗；標題被截斷，目標疾病應為子宮內膜異位症，需回原登記頁確認 |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | 完成 | 895 | 亞洲女性使用 Visanne 治療子宮內膜異位症的生活品質觀察性世代研究 |

以上試驗都不是以閉經為適應症，只能算間接證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | 系統性回顧/統合分析 | BMC Pharmacol Toxicol | 彙整 dienogest 的不良反應與發生率（子宮內膜異位症、子宮腺肌症） |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | 說明子宮內膜異位症荷爾蒙治療的內分泌基礎 |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | 世代研究 | Reprod Sci | 514 位卵巢子宮內膜瘤患者長期使用 dienogest 的療效、安全性與復發率 |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | 藥效學研究 | Eur J Contracept Reprod Health Care | 2 mg dienogest 抑制率與轉化指數高；提及子宮內膜異位症治療的目標包含誘導閉經 |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review | J Pediatr Adolesc Gynecol | 苗勒氏管異常的進階影像視覺化；與 dienogest 關聯低 |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | 個案報告 | Medicine | 多囊卵巢症候群患者的卵巢顆粒細胞瘤；與 dienogest 關聯低 |

沒有 RCT，也沒有以閉經為治療目標的文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60781 | VISANNE TAB 2MG | BAYER HEALTHCARE LIMITED |
| HK-68772 | ENDOSAFE TABLETS 2MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-67958 | DIENOGEST TEVA TABLETS 2MG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-68699 | DIENOPIL TABLETS 2MG | DKSH HONG KONG LIMITED |
| HK-59784 | QLAIRA TAB | BAYER HEALTHCARE LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 閉經是 dienogest 的已知藥理效應（出血型態改變），高預測分數很可能只反映這層關聯，不代表治療效益。所有連結試驗都在研究子宮內膜異位症，沒有任何直接證據。
- 其餘預測適應症也都缺乏證據，目前沒有值得推進的候選。

**若要推進需要：**
- 重新定義臨床問題：若目標是「出血控制」或「月經抑制」，需要另設適應症與療效指標，而不是閉經本身。
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選。
- 補齊作用機轉資料（可查詢 DrugBank）。
- 確認 NCT07164183 的實際目標疾病，並確認各試驗是否有閉經相關的次要結果。

---

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

