---
layout: default
title: Laronidase
parent: 中證據等級 (L3-L4)
nav_order: 502
evidence_level: L4
indication_count: 2
---

# Laronidase
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# Laronidase：從黏多醣症 I 型（MPS I）到伴隨骨骼病變的溶小體儲積症

## 一句話總結

Laronidase 是重組人類 α-L-艾杜糖醛酸酶（alpha-L-iduronidase），用於酵素replacement療法（ERT），文獻顯示其主要用於黏多醣症 I 型（MPS I）。TxGNN 模型預測它可能對**伴隨骨骼病變的溶小體儲積症 (lysosomal storage disease with skeletal involvement)** 有效。目前**沒有臨床試驗**，只有 **4 篇文獻**，且多屬間接證據。這個預測很可能只是 MPS I 既有機轉的重新歸類，而不是真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明；依文獻推定為 MPS I（需對照核准仿單確認） |
| 預測新適應症 | 伴隨骨骼病變的溶小體儲積症 (lysosomal storage disease with skeletal involvement) |
| TxGNN 預測分數 | 99.31% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。根據文獻，Laronidase 是重組 α-L-艾杜糖醛酸酶，用來補充 MPS I 患者缺乏的酵素，分解溶小體內堆積的硫酸乙醯肝素（heparan sulfate）和硫酸皮膚素（dermatan sulfate）。

MPS I 本身就是一種伴隨骨骼病變（多發性骨發育不全，dysostosis multiplex）的溶小體儲積症。因此這個高分預測，最可能反映的是 MPS I 既有的機轉，而不是找到了新用途。體外研究顯示 Laronidase 可被培養的纖維母細胞與成骨細胞攝取（PMID 18758061），這支持它與骨骼組織有合理關聯。

不過「伴隨骨骼病變的溶小體儲積症」是很廣的分類。現有資料沒有骨骼專屬的療效數據，也無法比對它與已核准 MPS I 適應症的重疊程度。因此在確認核准仿單之前，不宜把它當成真正的老藥新用。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review（藥物專論） | BioDrugs | 介紹 Laronidase 作為 MPS I 酵素replacement療法的開發歷程，已獲美國與歐洲孤兒藥資格 |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | 說明 MPS I 因 α-L-艾杜糖醛酸酶缺乏導致 GAG 堆積，涵蓋 Hurler、Scheie 等表型與診斷 |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Case report | Pediatric Neurology | Scheie 症候群男童接受 6.5 年酵素replacement療法，追蹤後整體狀況下降、疾病仍進展 |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | 體外／前臨床 | Biological & Pharmaceutical Bulletin | Laronidase 主要經甘露糖-6-磷酸受體被纖維母細胞與成骨細胞攝取，並運送到溶小體 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56438 | ALDURAZYME CONC. SOLUTION FOR IV INFUSION 2.9MG/5ML（藥商：SANOFI HONG KONG LIMITED） | 靜脈輸注濃縮液（依品名） | 許可證資料未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測沒有任何臨床試驗支持，文獻也只有兩篇綜述、一篇體外研究和一篇個案報告，對此分類都只是間接證據。
- 預測很可能只是 MPS I 既有適應症的重新歸類。香港核准適應症與仿單安全資料也都缺漏，目前無法進入安全性篩選。

**若要推進需要：**
- 下載並解析香港衛生署核准仿單，確認正式適應症、警語與禁忌症，判斷這是否真的超出現有 MPS I 適應症。
- 補齊 DrugBank 的作用機轉資料。
- 找出骨骼病變的專屬療效指標，例如影像或關節活動度數據。

**補充：** 同一份資料中的第二個預測「Sanfilippo 症候群 (MPS III)」（TxGNN 分數 99.22%，證據等級 L4）同樣建議 **Hold**。MPS III 缺乏的是不同的酵素，Laronidase 無法補上，且靜脈酵素無法有效穿越血腦屏障，而 MPS III 以神經症狀為主。現有文獻全部是 MPS I 研究，機轉依據薄弱。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

