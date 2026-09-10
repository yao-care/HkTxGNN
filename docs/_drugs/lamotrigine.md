---
layout: default
title: Lamotrigine
parent: 高證據等級 (L1-L2)
nav_order: 432
evidence_level: L2
indication_count: 5
---

# Lamotrigine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Lamotrigine：從癲癇治療到三叉神經痛

## 一句話總結

Lamotrigine 是一款抗癲癇藥物（本評估未取得完整的原適應症與作用機轉資料，但由臨床試驗描述可知其為 anticonvulsant）。TxGNN 模型針對此藥產生了 **5 個候選新適應症**，其中證據最強的是**三叉神經痛 (Trigeminal Neuralgia)**，目前有 **4 個臨床試驗**（含 1 個 lamotrigine vs carbamazepine 的頭對頭研究）與 **19 篇文獻**支持。另一個高分預測「三叉神經腫瘤 (Trigeminal Nerve Neoplasm)」經檢視後，證據不支持——很可能是知識圖譜將「neuralgia（神經痛）」與「neoplasm（腫瘤）」節點搞混所致的假訊號。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（未提供；試驗描述顯示屬抗癲癇藥物類別） |
| 預測新適應症（最強證據） | 三叉神經痛 (Trigeminal Neuralgia) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails（僅限三叉神經痛；其餘 4 項為 Hold） |

**五項候選預測總覽**

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|------|-----------|---------|---------|------|
| 1 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) | 99.97% | L4 | S0 | Hold（疑似 KG 節點混淆） |
| 2 | 三叉神經痛 (Trigeminal Neuralgia) | 99.89% | L2 | S2 | Proceed with Guardrails |
| 3 | 聲源性癲癇 (Audiogenic Seizures) | 99.38% | L4 | S1 | Research Question |
| 4 | 進食性癲癇 (Eating Seizures) | 99.38% | L4 | S0 | Hold |
| 5 | 性高潮誘發癲癇 (Orgasm-induced Seizures) | 99.38% | L5 | S0 | Hold |

## 為什麼這個預測合理？

目前缺乏 lamotrigine 完整的作用機轉資料庫紀錄，但根據試驗與文獻描述，其核心機轉為**抑制電壓依賴性鈉離子通道並減少麩胺酸釋放**，藉此穩定神經元異常放電——這與三叉神經痛現行一線用藥 carbamazepine、oxcarbazepine 屬同一藥理類別。

三叉神經痛的病理特徵是三叉神經根因血管壓迫導致局部脫髓鞘與異常神經放電，而 lamotrigine 的鈉通道阻斷機轉理論上能直接抑制這類陣發性放電，這也是為什麼已有頭對頭 RCT（NCT00913107）直接比較 lamotrigine 與 carbamazepine 的療效與安全性。

至於排名第 1 的「三叉神經腫瘤」，兩篇支持文獻實際內容討論的都是三叉神經**痛**（含一例由海綿狀血管畸形引起、以加馬刀放射手術治療），並非腫瘤本身的藥物治療證據。這與三叉神經痛高度相似的分數（99.97% vs 99.89%）進一步佐證此為知識圖譜節點混淆的假陽性，不建議採信。另外 3 項反射性癲癇亞型（聲源性、進食性、性高潮誘發癲癇）雖與 lamotrigine 廣譜抗癲癇機轉具生物學合理性，但目前僅有動物模型或零星個案報告，證據強度不足。

## 臨床試驗證據

以下為三叉神經痛（證據最強之預測適應症）相關試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | 完成 | 21 | Lamotrigine 與 carbamazepine 頭對頭比較療效與安全性，為最直接證據，但樣本小 |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | NA | 完成 | 20 | 雙盲安慰劑對照 add-on 研究，評估 lamotrigine 對三叉神經痛發作頻率與安全性的效果 |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | NA | 完成 | 6 | 以 fMRI 探討 lamotrigine 對神經病變性顏面疼痛的機轉，屬支持性研究 |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | 未知 | 132 | 比較 carbamazepine 與 oxcarbazepine，未納入 lamotrigine，僅作同類藥物間接佐證 |

其餘 4 項候選適應症目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | 歐洲神經學會三叉神經痛治療指引 |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | 系統性回顧三叉神經痛各類藥物療效與副作用 |
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | 臨床研究 | J Chinese Medical Association | Lamotrigine 與 carbamazepine 於三叉神經痛療效及安全性直接比較 |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case Report | Multiple Sclerosis Related Disorders | Pregabalin + lamotrigine 併用成功治療難治性三叉神經痛 |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | 三叉神經痛現行與新興藥物治療選項回顧 |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | 三叉神經痛實務診療指南 |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | 三叉神經痛病理生理學至藥物治療總論 |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | 三叉神經痛藥物治療最新進展 |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | 三叉神經痛病理機轉與治療總覽 |
| [21493636](https://pubmed.ncbi.nlm.nih.gov/21493636/) | 2011 | Review | Postgraduate Medical Journal | 三叉神經痛診斷與治療管理 |

## 香港上市資訊

Lamotrigine 目前於香港**未上市**，無許可證登記資料，無法列出核准適應症與劑型。

## 安全性考量

安全性資訊請參考原廠仿單。目前 TFDA/藥監局仿單警語與禁忌症資料尚未取得（此為 Blocking 等級資料缺口，直接影響安全性初評 S1 階段）。

## 結論與下一步

**決策：Proceed with Guardrails**（僅限三叉神經痛 (Trigeminal Neuralgia) 這一項預測；其餘 4 項維持 Hold）

**理由：**
- 三叉神經痛已有 1 個 Phase 2/3 頭對頭 RCT（lamotrigine vs carbamazepine）及多篇高品質指引/系統性回顧支持，機轉合理，證據等級達 L2。
- 「三叉神經腫瘤」預測高度疑似知識圖譜節點混淆所致假陽性，不建議採信；聲源性/進食性/性高潮誘發癲癇僅有動物模型或零星個案，證據不足以推進。
- 該藥物目前於香港未上市，需先解決上市與安全性資料缺口才能進入下一階段。

**若要推進需要：**
- 補齊 lamotrigine 完整作用機轉（MOA）與 TFDA/香港仿單警語、禁忌症資料（目前為 Blocking 缺口）
- 向知識圖譜維護方回報並校正「trigeminal nerve neoplasm」與「trigeminal neuralgia」節點混淆問題
- 若考慮於香港申請三叉神經痛適應症，需規劃當地上市申請與族群安全性監測計畫
- 針對聲源性癲癇等反射性癲癇亞型，若要繼續研究需先進行前臨床/概念驗證研究，注意 lamotrigine 於部分肌躍型癲癇可能有惡化風險
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

