---
layout: default
title: Elosulfase Alfa
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 9
---

# Elosulfase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Elosulfase alfa：從 Morquio A 症候群 (MPS IVA) 到 Scheie 症候群

## 一句話總結

Elosulfase alfa 是重組 GALNS 酵素，用於 Morquio A 症候群 (MPS IVA) 的酵素替代療法。
TxGNN 模型預測它可能對 **Scheie 症候群 (Scheie syndrome)** 有效，
但目前**沒有臨床試驗**，只有 **2 篇** MPS 族群的世代研究，且未測試本藥。機轉上的關聯也偏弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明；文獻顯示為 Morquio A 症候群 (MPS IVA) |
| 預測新適應症 | Scheie 症候群 (Scheie syndrome) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5（Evidence Pack 標為 L4，但現有文獻未檢驗本藥，故保守判定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。Elosulfase alfa 是重組 N-乙醯半乳糖胺-6-硫酸酯酶 (GALNS)，
負責分解硫酸角質素 (keratan sulfate) 與軟骨素-6-硫酸 (chondroitin-6-sulfate)，用來補足 Morquio A 患者缺乏的 GALNS。

Scheie 症候群是輕型 MPS I，成因是 IDUA（α-L-艾杜糖醛酸酶）缺乏。
兩者同屬黏多醣症 (MPS)，但缺乏的酵素和堆積的受質不同。
Elosulfase alfa 不會補足 IDUA，預期無法矯正 Scheie 症候群的糖胺聚醣堆積。

高分較可能來自知識圖譜中 MPS 類疾病的鄰近關係，而非以機轉為基礎的關聯。
因此這個預測的合理性有限。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Cohort | Human Mutation | 伊朗 302 位 MPS 患者（289 個家庭）的分子特徵與地理來源分析，屬診斷與基因研究，未涉及 elosulfase alfa 療效 |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Cohort | Pathologie-Biologie | 突尼西亞 MPS I 與 IVA 的臨床特徵及近親婚配情形，未涉及 elosulfase alfa 療效 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-63775 | VIMIZIM CONCENTRATE FOR SOLUTION FOR INFUSION 1MG/ML | 輸注用濃縮液（依品名） | BIOMARIN PHARMACEUTICAL INC. |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻也只是 MPS 族群的世代研究，並未檢驗本藥用於 Scheie 症候群。
- Elosulfase alfa 補的是 GALNS，Scheie 症候群缺的是 IDUA，機轉上不相符。MPS I 已有專屬的酵素替代療法（laronidase）。

**其他預測結果的判讀：**
- 「伴骨骼病變的溶小體儲積症」(rank 2) 的證據實際上指向 Morquio A，是既有適應症而非新用途，應將疾病標籤縮窄為 MPS IVA。
- Sanfilippo 症候群 (rank 4) 底下的 19 篇文獻全部是 Morquio A 研究，疑為疾病對應錯誤，應改歸入 MPS IVA 的證據。
- Hurler 症候群 (rank 3) 只有一個 Phase 1 產前酵素替代試驗（NCT04532047），且無法確認其中是否含本藥。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症（DG001，為阻斷性缺口）。
- 補齊 DrugBank 的作用機轉資料（DG002）。
- 修正疾病對應，把 Morquio A 的證據重新歸入 MPS IVA。
- 提出 Scheie 症候群的機轉或前臨床證據，例如 elosulfase alfa 對 IDUA 相關糖胺聚醣堆積是否有任何作用。若沒有，就不建議繼續評估此適應症。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

