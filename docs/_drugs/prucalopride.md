---
layout: default
title: Prucalopride
parent: 僅模型預測 (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride：原適應症資料缺口 → TxGNN 預測低α脂蛋白血症（Hypoalphalipoproteinemia）

## 一句話總結

Prucalopride（DrugBank ID: DB06480）目前未在香港上市，原始核准適應症與完整作用機轉資料尚未補齊（列為 Blocking / High 等級資料缺口）。
TxGNN 對此藥物共產出 **10 個預測適應症**，分數最高的是**低α脂蛋白血症 (Hypoalphalipoproteinemia)**（99.82%），
但機轉分析判斷此為知識圖譜嵌入雜訊，**無任何臨床試驗或文獻支持**；10 個候選中僅 1 個（原發性澱粉樣變性）有文獻佐證。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（無許可證紀錄，亦無原始適應症資料） |
| 預測新適應症 | 低α脂蛋白血症 (Hypoalphalipoproteinemia) |
| TxGNN 預測分數 | 99.82%（模型排名第 4183 位） |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式登錄的作用機轉 (MOA) 資料（原始欄位標記為資料缺口，屬 High severity）。根據 TxGNN 預測理由文字中附帶的背景描述，Prucalopride 為高選擇性 **5-HT4 受體促效劑**，主要作用於腸道神經叢以促進腸蠕動——這類機轉一般對應腸胃動力相關適應症，而非血脂代謝疾病。

低α脂蛋白血症的病理核心在於 HDL／脂蛋白代謝路徑（如 ABCA1、LCAT），這與 5-HT4 受體訊息傳導**沒有已知交集**。模型評估文字本身也明確指出：「TxGNN 分數極高但缺乏任何生物學合理性，判斷為知識圖譜嵌入雜訊（embedding artifact）」。也就是說，這個高分預測**不應被解讀為真實的藥理訊號**，而是模型層面的雜訊。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Prucalopride 目前**未在香港上市**，無許可證紀錄可列出。

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他預測候選適應症一覽

TxGNN 針對此藥物共產出 10 個候選，多數與排名第一者同樣缺乏機轉合理性與實證支持，僅原發性澱粉樣變性有文獻佐證：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 | 備註 |
|------|-----------|-----------|---------|---------|------|------|
| 1 | Hypoalphalipoproteinemia | 99.82% | L5 | S0 | Hold | 判定為知識圖譜嵌入雜訊 |
| 2 | Homozygous familial hypercholesterolemia | 99.67% | L5 | S0 | Hold | 與脂蛋白代謝路徑無關聯 |
| 3 | Duodenal ulcer | 99.65% | L5 | S0 | Hold | 促動力機轉方向與潰瘍治療相悖 |
| 4 | Oral candidiasis | 99.64% | L5 | S0 | Hold | 無抗真菌活性 |
| 5 | Familial combined hyperlipidemia（已列為過時分類） | 99.62% | L5 | S0 | Hold | 疾病分類已過時，不建議投入資源 |
| 6 | Amyloidosis | 99.62% | L5 | S0 | Hold | 理論上具症狀緩解合理性，但無實證 |
| 7 | Strongyloidiasis | 99.60% | L5 | S0 | Hold | 無抗寄生蟲活性 |
| 8 | HIV infectious disease | 99.60% | L5 | S0 | Hold | 無抗病毒活性 |
| **9** | **Primary amyloidosis** | 99.56% | **L4** | **S1** | **Research Question** | 唯一有文獻佐證；澱粉樣變性侵犯腸道自主神經可能導致動力障礙，機轉具中等合理性，但僅有間接流行病學文獻（[PMID 34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/)），無介入性證據 |
| 10 | Acquired amyloid peripheral neuropathy | 99.55% | L5 | S0 | Hold | 與 #9 機轉假說類似，但完全無實證 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名最高的低α脂蛋白血症預測分數雖高，但機轉與實證雙缺，模型自評即判定為雜訊，不具推進價值。
- 全部 10 個候選中僅原發性澱粉樣變性達到 L4／S1（Research Question）等級，其餘皆為 L5（僅模型預測），證據強度不足以支持任何投資決策。

**若要推進需要：**
- 補齊 TFDA／香港仿單警語與禁忌症資料（DG001，Blocking，目前無法進入安全性初評）
- 補齊完整作用機轉 (MOA) 資料（DG002，High）
- 若聚焦原發性澱粉樣變性方向：需取得該族群腸道動力障礙之介入性研究（病例系列或前瞻性試驗），目前僅有診斷型文獻佐證
- 若考慮於香港上市，需完成當地藥證申請流程（目前 0 張許可證）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

