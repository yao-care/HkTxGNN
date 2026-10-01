---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine：從原適應症（資料未載明）到先天性糖基化異常（岩藻糖基化缺陷）

## 一句話總結

Bromocriptine（溴隱亭）在香港已上市，但本次資料未載明其核准適應症。
TxGNN 模型預測它可能對**先天性糖基化異常，伴岩藻糖基化缺陷 (Congenital disorder of glycosylation with defective fucosylation)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個預測，只有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 先天性糖基化異常，伴岩藻糖基化缺陷 (Congenital disorder of glycosylation with defective fucosylation) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Bromocriptine 屬於多巴胺促效劑類藥物，主要作用於多巴胺 D2 類受體。本次資料並未提供其原適應症，因此無法比較原適應症與這個罕見遺傳性代謝疾病之間的關聯。

以現有資料，看不出多巴胺受體調控與岩藻糖基化缺陷之間有任何機轉連結。這個候選只依靠知識圖譜的預測分數（0.998），沒有試驗、文獻或機轉研究佐證。在補足機轉資料之前，這個預測只能視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測候選（供參考）

排名第 1 的候選沒有證據。以下兩個候選有一些檢索結果，但都不足以支持推進：

| 排名 | 預測適應症 | 分數 | 證據等級 | 說明 |
|------|-----------|------|---------|------|
| 3 | 視網膜失養症 (Retinal dystrophy) | 99.82% | L4 | 檢索到的多為先天性眼眶或眼部異常的綜述與病例報告，與 bromocriptine 無關。PMID [39009597](https://pubmed.ncbi.nlm.nih.gov/39009597/)（2024，Nature Communications）是藥物再利用的前臨床組合治療研究，其標題被截斷，無法確認是否涉及 bromocriptine，需人工查核。 |
| 9 | 思覺失調症 (Schizophrenia) | 99.73% | L3 | 有 3 個相關試驗，但都不是以 bromocriptine 直接治療思覺失調症症狀（見下）。 |

**思覺失調症的相關試驗：**
- [NCT03575000](https://clinicaltrials.gov/study/NCT03575000)：Phase 4、開放標籤、15 人、尚未招募。研究 bromocriptine 輔助改善抗精神病藥物造成的糖代謝異常。
- [NCT00315081](https://clinicaltrials.gov/study/NCT00315081)：Phase 3、20 人、狀態未知。研究 bromocriptine 治療 risperidone 引起的高泌乳素血症。

**機轉與安全性方面：**
- 多巴胺促效劑與抗精神病藥物的 D2 拮抗作用方向相反。
- 有病例報告顯示 bromocriptine 可能誘發精神病（PMID [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/)）。
- 較合理的用途是輔助處理藥物副作用，而不是作為主要療法。

## 香港上市資訊

資料中的劑型與核准適應症欄位皆為空白，以下僅列許可證號、品名與廠商：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-32888 | MEDOCRIPTINE TAB 2.5MG | STAR MEDICAL SUPPLIES LTD |
| HK-34468 | BROMOCRIPTIN TAB 2.5MG (RICHTER) | MEKIM LTD |
| HK-33542 | SYNTOCRIPTINE TAB 2.5MG | CNW FAR EAST LIMITED |
| HK-01595 | PARLODEL TAB 2.5MG | SKY UNITED TRADING LIMITED |
| HK-40461 | APO-BROMOCRIPTINE TAB 2.5MG | HIND WING CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢未找到資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗、文獻或機轉線索支持（L5）。
- 香港仿單的警語與禁忌資料缺口屬於阻擋等級，目前無法進入安全性篩選。

**若要推進需要：**
- 補齊 bromocriptine 的作用機轉資料（可查詢 DrugBank API）。
- 取得香港衛生署的仿單，補足警語與禁忌症。
- 釐清多巴胺受體調控與岩藻糖基化缺陷之間是否存在生物學連結。
- 人工查核 PMID 39009597 是否涉及 bromocriptine，並評估其他候選（如思覺失調症輔助用途）是否更值得優先研究。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

