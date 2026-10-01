---
layout: default
title: Cefazolin
parent: 中證據等級 (L3-L4)
nav_order: 166
evidence_level: L4
indication_count: 8
---

# Cefazolin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **8** 個
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

# Cefazolin：從細菌感染到感染性中耳炎

## 一句話總結

Cefazolin 是第一代頭孢菌素類注射抗生素，香港已有 3 張上市許可證。
TxGNN 模型預測它可能對**感染性中耳炎 (Infectious Otitis Media)** 有效。
目前有 **1 個相關臨床試驗登記**（未確認使用 cefazolin）和 **3 篇間接文獻**，尚無直接證據，建議先 Hold。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 感染性中耳炎 (Infectious Otitis Media) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Cefazolin 是第一代頭孢菌素，透過結合青黴素結合蛋白 (PBP) 來抑制細菌細胞壁合成。DrugBank 的作用機轉欄位目前缺資料，以上說明來自一般藥理知識。

中耳炎的急性化膿型多由細菌引起，所以作用於細胞壁的 β-內醯胺類抗生素在機轉上有合理性，鏈球菌與葡萄球菌也在 cefazolin 的涵蓋範圍內。

不過有幾個明顯限制：
- 對中耳炎常見的流感嗜血桿菌 (*H. influenzae*) 和卡他莫拉菌 (*M. catarrhalis*) 涵蓋有限。
- 只有注射劑型，不適合一般門診中耳炎的常規治療。

因此 0.9944 的高分較可能反映知識圖譜中與其他抗生素、中耳炎的關聯，不等於臨床有效性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | 已終止 | 520 | 比較 6–23 個月幼兒急性中耳炎的 5 天短療程與 10 天標準療程抗生素。未確認試驗藥物是 cefazolin，且無結果支持本藥，不能視為直接證據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | Southern Medical Journal | 回顧頭孢菌素在兒科感染的應用，特別是對青黴素過敏者，屬一般性背景資料 |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Stevens-Johnson 症候群的病例與文獻回顧，病童因中耳炎等感染用過抗生素，與 cefazolin 療效無直接關係 |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report | Annals of Otology, Rhinology, and Laryngology | 探討 ceftazidime + cefazolin 經驗性治療兒童 Gradenigo 症候群（急性中耳炎的罕見併發症），僅為病例報告 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64519 | STAZOLIN POWDER FOR SOLUTION FOR INJECTION 1G | KAI YUEN PHARMACEUTICAL CO |
| HK-34125 | CEFAZOLIN FOR INJ 1G (YUNG SHIN) | YUNG SHIN CO LTD |
| HK-47264 | CEFAZOLIN SODIUM FOR INJ 1G | THE UNITED LABORATORIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測目前只有模型分數和間接證據支持。唯一的試驗未確認使用 cefazolin，文獻多為回顧、病例報告或以 cefazolin 為對照藥。
- 藥物僅有注射劑型，且對中耳炎主要致病菌的涵蓋有限，臨床上難以取代現行口服首選藥物。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症。
- 補齊 DrugBank 的作用機轉資料。
- 確認 NCT01511107 的實際試驗藥物，並搜尋直接評估 cefazolin 的中耳炎臨床研究。
- 評估是否優先探討**化膿性中耳炎**：有一項 1982 年 cefmetazole 對 cefazolin 的人體對照研究，是目前最接近直接的臨床訊號，但設計與結果仍待查證。
- 其餘預測適應症（中耳疾病、慢性中耳炎、耳咽管炎、非化膿性與過敏性中耳炎）證據更弱或機轉不符，不建議優先投入。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

