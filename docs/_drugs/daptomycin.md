---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin：從革蘭氏陽性菌感染到退化性關節炎

## 一句話總結

Daptomycin 是一種環狀脂肽類抗生素，用於治療革蘭氏陽性菌感染。
TxGNN 模型預測它可能對**退化性關節炎 (Osteoarthritis)** 有效，但目前**沒有臨床試驗**，且 9 篇文獻幾乎都是骨關節*感染*的研究，並非針對退化性關節炎本身。這個高分較可能來自知識圖譜中與關節疾病的關鍵字鄰近，而非真正的療效訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（一般為革蘭氏陽性菌所致皮膚感染、菌血症等） |
| 預測新適應症 | 退化性關節炎 (Osteoarthritis) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L5（僅有模型預測；文獻皆為感染研究，不支持新適應症） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Daptomycin 是環狀脂肽類抗生素，以鈣依賴方式使革蘭氏陽性菌的細胞膜去極化而殺菌。目前缺乏更詳細的作用機轉資料。

原適應症是細菌感染，新適應症是退化性關節炎（非感染性的關節退化），兩者在病理上沒有直接關聯。檢索到的文獻主要是 daptomycin 治療骨關節感染、人工關節感染的經驗，支持的是**既有的抗菌用途**，並非退化性關節炎的療效。

因此，機轉上找不到可信的連結。高預測分數較可能反映知識圖譜中「關節疾病」節點的鄰近效應。相較之下，同一次預測中的**類風濕性關節炎**有兩篇 2025 年前臨床研究（見結論），比退化性關節炎更值得追蹤。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | Int Orthop | 評估高劑量 daptomycin 併用 rifampicin 治療革蘭氏陽性菌骨關節感染的安全性與療效 |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | daptomycin 治療髖、膝人工關節感染的臨床經驗 |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | 高劑量 daptomycin (>6 mg/kg) 用於複雜性骨關節與植入物相關感染的療效與安全性 |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | 比較 daptomycin 與標準療法治療金黃色葡萄球菌菌血症合併骨關節感染的預後 |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohort | Med Clin (Barc) | EU-CORE 資料庫中西班牙醫院使用 daptomycin 的病人特徵與結果 |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Cohort（調查） | Int J Antimicrob Agents | 傳染病醫師對人工關節感染處置的問卷調查，指出高品質證據不足 |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | 人工關節感染分離出的葡萄球菌之抗生素感受性 |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surg Infect | 骨關節感染葡萄球菌菌株十年間的抗藥性演變 |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Rep Orthop | 一名有退化性關節炎診斷的病人，實為慢性紋狀棒狀桿菌化膿性關節炎 |

以上文獻均與 daptomycin 治療退化性關節炎無關，僅涉及骨關節感染。

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57551 | CUBICIN FOR INJ 500MG | MERCK SHARP & DOHME (ASIA) LTD |
| HK-67114 | DAPTOMYCIN POWDER FOR SOLUTION FOR INJECTION/INFUSION 500MG | I & C (HONG KONG) LIMITED |
| HK-67646 | DAPTOMYCIN POWDER FOR SOLUTION FOR INJECTION/INFUSION 500MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-68014 | DAPTOMYCIN POWDER FOR SOLUTION FOR INJECTION/INFUSION 500MG | CHEMILL PHARMA LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中有一則值得注意的訊號：一篇個案報告（[PMID 36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/)）記載 daptomycin 引起橫紋肌溶解，並併發急性痛風性關節炎。橫紋肌溶解是 daptomycin 已知的不良反應。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，現有文獻談的是骨關節感染，不是退化性關節炎。機轉上也找不到可信的連結，高分很可能是圖譜鄰近效應。
- 同次預測的痛風等其他項目也無支持證據，其中痛風的個案報告反而是不良反應訊號。

**若要推進需要：**
- 先評估**類風濕性關節炎**方向：2025 年有兩篇前臨床研究（[PMID 39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/)、[40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/)），顯示 daptomycin 或其衍生物在膠原誘導關節炎小鼠模型中可降低發炎細胞激素與 NF-κB 訊號。這仍屬動物或體外證據，需獨立重複驗證，並比較動物實驗劑量與人體 daptomycin 暴露量。
- 評估長期使用抗生素的風險。
- 取得香港衛生署仿單，補齊警語與禁忌資料。
- 若仍要探討退化性關節炎，需先有機轉假說與前臨床資料，目前不建議投入資源。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

