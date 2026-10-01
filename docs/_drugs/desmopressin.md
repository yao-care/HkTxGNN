---
layout: default
title: Desmopressin
parent: 中證據等級 (L3-L4)
nav_order: 254
evidence_level: L4
indication_count: 10
---

# Desmopressin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Desmopressin：從現有用途到先天性凝血酶原缺乏症

## 一句話總結

Desmopressin 是一種已在香港上市的合成抗利尿激素類似物，有錠劑、口溶錠和注射劑等劑型。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，但目前**沒有直接支持的臨床試驗或文獻**，高分較可能來自知識圖譜中與其他先天性凝血因子疾病的相近性。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Desmopressin 透過刺激內皮細胞釋放，提高血漿中的第八凝血因子 (FVIII) 與血管性血友病因子 (VWF)，因此臨床上常用於輕度 A 型血友病與部分類型的血管性血友病。

不過，先天性凝血酶原缺乏症是第二凝血因子 (FII) 不足，Desmopressin **不會提高凝血酶原**，機轉上沒有直接支持它有效的理由。相關文獻中最接近的，是 1989 年一例先天性第五、第八因子合併缺乏的個案報告，其中的 FVIII 部分可能對 Desmopressin 有反應，但這並不能推論到 FII 缺乏。

因此這個高分預測比較像是圖譜上「同屬先天性凝血因子疾病」的相近性，而非有藥理依據的關聯。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | 招募中 | 20 | 單臂、開放標籤，評估 Emicizumab 用於輕度 A 型血友病的止血特性。試驗未使用 Desmopressin，疾病也不同，與本適應症無關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | 先天性出血性疾病的治療選擇，涵蓋 A 型血友病與血管性血友病，屬一般性回顧 |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | 後天性血友病 A 的診斷、病因與治療，並非先天性凝血酶原缺乏症 |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | 1 例先天性第五、第八因子合併缺乏者使用 DDAVP，是本組最相關的一篇，但缺乏的因子不同 |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | 1 例第五、第八因子合併缺乏的孕婦，以第八因子濃縮劑支持剖腹產，並未使用 Desmopressin |

## 香港上市資訊

香港共有 14 張許可證，以下列出 5 張主要許可證（資料未載明核准適應症與劑型，劑型可由品名判斷）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-37371 | MINIRIN TAB 0.1MG | FERRING PHARMACEUTICALS LTD |
| HK-67930 | NURITAN TABLETS 0.1MG | STAR MEDICAL SUPPLIES LTD |
| HK-68708 | MINIS TABLETS 0.1MG | SB PHARMA LIMITED |
| HK-54452 | MINIRIN MELT ORAL LYOPHILISATE 60MCG | FERRING PHARMACEUTICALS LTD |
| HK-32872 | MINIRIN INJ 4MCG/ML | FERRING PHARMACEUTICALS LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，2023 年的一篇回顧 ([PMID 36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/)) 指出，Desmopressin 的使用可能併發低血鈉，並偶有動脈血栓事件。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測沒有任何直接證據支持。唯一的臨床試驗與 Desmopressin 無關，文獻僅有一般性回顧與不同因子缺乏的個案報告。
- 機轉上 Desmopressin 不提高凝血酶原，且香港仿單的警語與禁忌尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症
- 補充 Desmopressin 的作用機轉資料（如查詢 DrugBank）
- 尋找 Desmopressin 用於凝血酶原缺乏症的直接臨床或機轉證據，目前沒有

**其他預測適應症（供參考）：**
- 「血小板釋放障礙 (primary release disorder of platelets)」是這組預測中機轉最合理的一項，有兒童 aspirin-like defect 的研究 ([PMID 21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/)) 與 2023 年回顧支持，建議列為優先研究問題，但仍缺乏前瞻性對照數據。
- 「遺傳性血栓形成傾向」「假性血管性血友病」「血栓性血小板減少性紫癜」的預測方向與 Desmopressin 的促止血作用相反，較可能是安全性警訊，而非治療機會。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

