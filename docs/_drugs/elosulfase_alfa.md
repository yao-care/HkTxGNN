---
layout: default
title: Elosulfase Alfa
parent: 僅模型預測 (L5)
nav_order: 313
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

# Elosulfase alfa：從黏多醣症到 Scheie 症候群

## 一句話總結

Elosulfase alfa 是重組 N-乙醯半乳糖胺-6-硫酸酯酶（GALNS）酵素替代療法，原本用於黏多醣症（Morquio A，MPS IVA）。
TxGNN 模型預測它可能對 **Scheie 症候群 (Scheie syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持此預測，僅屬模型推論，且機轉上關聯薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黏多醣症（Mucopolysaccharidosis） |
| 預測新適應症 | Scheie 症候群 (Scheie syndrome) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Elosulfase alfa 是 GALNS 重組酵素，用來分解硫酸角質素（keratan sulfate）與硫酸軟骨素-6（chondroitin-6-sulfate），在 Morquio A 中的療效已被證實。

Scheie 症候群（MPS I 的較輕型）則是 α-L-艾杜糖醛酸酶（alpha-L-iduronidase）缺乏，累積的是硫酸皮膚素與硫酸乙醯肝素。這是不同的受質，Elosulfase alfa 無法補足 MPS I 缺少的酵素，**機轉上的關聯很弱**。高分可能只反映兩者同屬黏多醣症類別，而非真正的酵素作用重疊。此外，MPS I 已有核准療法（laronidase）。

其他預測疾病的情況：

- **溶小體儲積症伴骨骼病變**（分數 99.59%）：此類別涵蓋 Morquio A，也就是現有核准適應症，相關文獻支持的是現有標示，並非新適應症的獨立證據。
- **Hurler 症候群**（99.43%）與 **Sanfilippo 症候群**（99.42%）：受質不同，且重組酵素通常無法穿越血腦屏障，對以神經病變為主的 Sanfilippo 尤其不利。
- **其餘五項**（眼瞼下垂相關症候群、先天性 Horner 症候群等，分數約 99.0–99.1%）：與 GALNS 代謝途徑無已知關聯，僅為運算預測。

---

## 臨床試驗證據

針對排名第一的預測（Scheie 症候群），目前無相關臨床試驗登記。

作為參考，排名第三的 Hurler 症候群有一項間接相關的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | 招募中 | 10 | PEARL：溶小體儲積症的產前酵素替代療法安全性與可行性研究；無證據顯示使用 elosulfase alfa，相關性屬間接 |

---

## 文獻證據

針對排名第一的預測（Scheie 症候群），目前無相關文獻。

以下為排名第四（Sanfilippo 症候群）所檢索到的文獻。這些文獻幾乎全部討論 Morquio A，**並未證明對 Sanfilippo 症候群有效**，僅反映現有適應症的證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24810369](https://pubmed.ncbi.nlm.nih.gov/24810369/) | 2014 | RCT | J Inherit Metab Dis | 第 3 期隨機安慰劑對照試驗，評估 elosulfase alfa 治療 Morquio A 的療效與安全性 |
| [25284089](https://pubmed.ncbi.nlm.nih.gov/25284089/) | 2015 | RCT | Mol Genet Metab | 24 週關鍵第 3 期試驗中，多面向次要與複合終點的影響 |
| [27380995](https://pubmed.ncbi.nlm.nih.gov/27380995/) | 2016 | Cohort | Mol Genet Metab | 96 週延伸研究（累計 120 週）的長期耐力與安全性 |
| [27553181](https://pubmed.ncbi.nlm.nih.gov/27553181/) | 2016 | Cohort | J Inherit Metab Dis | 長期治療對呼吸功能的影響 |
| [28535791](https://pubmed.ncbi.nlm.nih.gov/28535791/) | 2017 | Cohort | Orphanet J Rare Dis | 成人 Morquio A 亞群在長期延伸研究中的臨床結果 |
| [27955919](https://pubmed.ncbi.nlm.nih.gov/27955919/) | 2017 | Cohort | Clin Ther | MOR-005 延伸研究的長期免疫原性 |
| [25487082](https://pubmed.ncbi.nlm.nih.gov/25487082/) | 2015 | 其他 | Clin Ther | MOR-004 第 3 期試驗的免疫原性分析 |
| [25234648](https://pubmed.ncbi.nlm.nih.gov/25234648/) | 2014 | 其他 | Clin Pharmacokinet | 第 3 期試驗的藥動學與藥效學評估 |
| [30289033](https://pubmed.ncbi.nlm.nih.gov/30289033/) | 2015 | Review | Expert Rev Endocrinol Metab | Elosulfase alfa 治療 MPS IVA 的回顧 |
| [32014045](https://pubmed.ncbi.nlm.nih.gov/32014045/) | 2020 | Cohort | Orphanet J Rare Dis | 7 萬名新生兒的 Morquio 與其他溶小體疾病篩檢結果，非治療證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63775 | VIMIZIM CONCENTRATE FOR SOLUTION FOR INFUSION 1MG/ML | 未提供 | 未提供 |

製造商為 BioMarin Pharmaceutical Inc.，為有效單方製劑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Scheie 症候群的預測僅來自模型分數，沒有任何臨床試驗或文獻支持，證據等級為 L5。
- GALNS 的受質與 MPS I 缺乏的酵素不同，機轉上缺乏合理性，且 MPS I 已有核准療法。其他預測疾病也同樣沒有獨立的新適應症證據。

**若要推進需要：**
- 取得詳細的作用機轉資料，並以體外或動物模型驗證 GALNS 是否能影響 MPS I 的受質累積
- 取得香港衛生署核准仿單，補齊警語、禁忌症與交互作用資訊
- 與現有 MPS I 標準療法（laronidase）比較其潛在附加價值
- 在有任何生物學證據前，不建議啟動臨床開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

