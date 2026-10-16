---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Carbimazole：預測新適應症為新生兒甲狀腺毒症 (Neonatal Thyrotoxicosis)（證據等級 L5）。原適應症：甲狀腺機能亢進、葛瑞夫茲氏症、甲狀腺毒症"
---

# Carbimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Carbimazole：從甲狀腺機能亢進到新生兒甲狀腺毒症

## 一句話總結

Carbimazole 是抗甲狀腺藥物，原本用於治療甲狀腺機能亢進、葛瑞夫茲氏症（Graves disease）與甲狀腺毒症。
TxGNN 模型預測它可能對**新生兒甲狀腺毒症 (Neonatal Thyrotoxicosis)** 有效（預測分數最高者為「甲狀腺素抗性症」，但依證據與機轉合理性，本報告以新生兒甲狀腺毒症為主要評估方向）。
目前**無已登記的臨床試驗**，但有 **13 篇文獻**（以綜述、世代研究與病例報告為主）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲狀腺機能亢進、葛瑞夫茲氏症、甲狀腺毒症（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 新生兒甲狀腺毒症 (Neonatal Thyrotoxicosis)（TxGNN 排名第 2） |
| TxGNN 預測分數 | 99.41%（排名第 1 的甲狀腺素抗性症為 99.71%，但機轉不支持；第 3 為高甲狀腺素血症 99.21%） |
| 證據等級 | L3（僅有觀察性研究、綜述與病例報告） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Carbimazole 是甲巴唑（methimazole）的前驅藥物，會抑制甲狀腺過氧化酶，減少甲狀腺素合成。這個機轉與其在葛瑞夫茲氏症的已核准用途相同。

新生兒甲狀腺毒症多由母體的 TSH 受體刺激性抗體經胎盤傳給胎兒所致，本質上是葛瑞夫茲氏症的延伸。因此阻斷甲狀腺素合成在機轉上直接適用，文獻中也有以 carbimazole 治療新生兒甲狀腺毒症，以及子宮內治療胎兒甲狀腺機能亢進的報告。

另外兩個預測值得注意：
- **甲狀腺素抗性症（RTH-β）**：此病的周邊組織對甲狀腺素不敏感，TSH 不被抑制。降低激素濃度可能進一步提高 TSH、加重甲狀腺腫，機轉薄弱且可能有害。唯一相關文獻討論的是鑑別診斷，不是治療。高分很可能只是反映網絡鄰近性。
- **高甲狀腺素血症**：這只是檢驗結果，成因多元。Carbimazole 僅在真正的甲狀腺過度分泌（如葛瑞夫茲氏症）時有效，與原適應症重疊。對家族性白蛋白異常高甲狀腺素血症或 TSH 分泌型腺瘤則不適用，甚至可能有害。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為新生兒甲狀腺毒症的主要文獻（依證據類型排序）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24251220](https://pubmed.ncbi.nlm.nih.gov/24251220/) | 2013 | Review | Indian J Endocrinol Metab | 胎兒/新生兒甲狀腺毒症罕見，死亡率 12–20%，由母體刺激性抗體經胎盤傳遞造成 |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | 妊娠期甲狀腺機能亢進須與生理變化區分，母嬰皆可能出現不良結果 |
| [7523202](https://pubmed.ncbi.nlm.nih.gov/7523202/) | 1994 | Cohort | Eur J Obstet Gynecol Reprod Biol | 32 例妊娠合併甲亢，使用 carbimazole 或 PTU 控制，僅 28% 能在孕晚期減藥或停藥 |
| [1971773](https://pubmed.ncbi.nlm.nih.gov/1971773/) | 1990 | Cohort | Clin Endocrinol | 44 位葛瑞夫茲氏症孕婦與其嬰兒，探討 TBII、抗甲狀腺藥劑量與新生兒甲狀腺功能的關係 |
| [11298090](https://pubmed.ncbi.nlm.nih.gov/11298090/) | 2001 | Case series | Clin Endocrinol | 早產兒先天性甲狀腺毒症，死亡率可高達 25%，母體 TBII 可預測不良結果 |
| [41191399](https://pubmed.ncbi.nlm.nih.gov/41191399/) | 2025 | Case report | Endocrinol Diabetes Metab Case Rep | 新生兒甲狀腺毒症引起嚴重高血鈣，對 carbimazole 治療有反應 |
| [25952662](https://pubmed.ncbi.nlm.nih.gov/25952662/) | 2015 | Case report | Indian J Pediatr | 兩位手足的胎兒甲亢，以 carbimazole 進行子宮內治療 |
| [12124735](https://pubmed.ncbi.nlm.nih.gov/12124735/) | 2002 | Case report | Am J Med Genet | 母體使用 carbimazole 後出現後鼻孔閉鎖（第 4 例報告） |
| [27747714](https://pubmed.ncbi.nlm.nih.gov/27747714/) | 2015 | Case report | Drug Saf Case Rep | 新生兒以 carbimazole 與 propranolol 治療，後續使用 amlodipine 出現嚴重低血壓 |
| [41018437](https://pubmed.ncbi.nlm.nih.gov/41018437/) | 2025 | Case report | Cureus | 散發性非自體免疫性先天性甲亢（TSHR 活化突變）的延遲表現 |
| [2315685](https://pubmed.ncbi.nlm.nih.gov/2315685/) | 1990 | 未分類 | Scott Med J | 新生兒甲狀腺毒症對 carbimazole 治療有反應 |
| [29494342](https://pubmed.ncbi.nlm.nih.gov/29494342/) | 2018 | 未分類 | J Pediatr Endocrinol Metab | 自體免疫性甲狀腺功能低下母親所生嬰兒，因 TRAb 出現嚴重甲亢 |
| [6689398](https://pubmed.ncbi.nlm.nih.gov/6689398/) | 1983 | 未分類 | Arch Fr Pediatr | 新生兒葛瑞夫茲氏症合併顱縫早閉，以 carbimazole 治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52760 | CARBIMAZOLE 5 TAB 5MG (REMEDICA) | — | — |
| HK-60955 | SYN-CARBIMAZOLE TAB 5MG | — | — |
| HK-35972 | CARBIROID TAB 5MG | — | — |
| HK-26101 | CARBIMAZOLE TAB 5MG | — | — |
| HK-65516 | CAMAZOL TABLETS 5MG | — | — |

另有 HK-05069（CARBIMAZOLE TAB 5MG，SYNCO）為第 6 張有效許可證。6 張皆為單方、有效狀態。

---

## 安全性考量

- **致畸胎風險**：文獻報告胎兒期暴露於 carbimazole 與先天性畸形（如後鼻孔閉鎖）有關（PMID 12124735），孕期使用需審慎權衡。
- **新生兒併用藥物**：有報告顯示新生兒在 carbimazole 與 propranolol 治療期間使用 amlodipine 出現嚴重低血壓（PMID 27747714），併用降壓藥須特別小心。
- **其他預測適應症的風險**：用於甲狀腺素抗性症或 TSH 分泌型腺瘤可能提高 TSH 刺激，並非適當用途。

其餘警語、禁忌與藥物交互作用資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對新生兒甲狀腺毒症）

**理由：**
- 新生兒甲狀腺毒症的機轉與 carbimazole 已核准的葛瑞夫茲氏症用途一致，文獻也有臨床使用報告，但證據以觀察性研究與病例報告為主，沒有已登記的臨床試驗。這在臨床上已屬既有做法，與原適應症的區別不明確，不算嚴格意義上的藥物再利用。
- 甲狀腺素抗性症（排名第 1）和高甲狀腺素血症（排名第 3）機轉不支持，建議 **Hold**。

**若要推進需要：**
- 取得香港衛生署仿單的警語、禁忌與核准適應症內容，完成安全性篩選
- 補充詳細的作用機轉資料（MOA）
- 針對新生兒與孕期使用，建立劑量、致畸胎風險與血液學（如顆粒球缺乏）的監測計畫
- 蒐集或設計前瞻性研究，與現行標準處置（如 methimazole、PTU）比較
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

