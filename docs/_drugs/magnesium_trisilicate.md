---
layout: default
title: Magnesium Trisilicate
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 5
---

# Magnesium Trisilicate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Magnesium Trisilicate：從傳統制酸劑到消化性潰瘍相關適應症的再評估

## 一句話總結

Magnesium Trisilicate 是傳統制酸劑成分，目前在香港未有上市許可證，也缺乏正式登記的原適應症資料。
TxGNN 模型針對**5 個消化性潰瘍相關疾病**產生預測，其中證據較完整的是**胃空腸吻合口潰瘍 (Gastrojejunal Ulcer)**與**胃潰瘍 (Gastric Ulcer)**，
分別有 **20 篇**與**7 篇**文獻及 **1 個臨床試驗**支持，但多數證據屬於「抗酸劑」藥物類別的間接證據，而非本藥物專一的臨床試驗結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式登記資料；文獻脈絡顯示傳統作為制酸劑使用 |
| 預測新適應症 | 胃空腸吻合口潰瘍 (Gastrojejunal Ulcer)（證據最完整，詳見下方多適應症總表） |
| TxGNN 預測分數 | 99.81%（胃空腸吻合口潰瘍） |
| 證據等級 | L3（本候選藥物中最高等級） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question（部分適應症）／Hold（其餘適應症及整體上市決策） |

### 5 個預測適應症總表

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|------|-----------|---------|---------|------|
| 1 | Active Peptic Ulcer Disease | 99.86% | L4 | S1 | Hold |
| 2 | Peptic Ulcer Perforation | 99.81% | L5 | S0 | Hold |
| 3 | Gastrojejunal Ulcer | 99.81% | L3 | S2 | Research Question |
| 4 | Gastroduodenitis | 99.72% | L5 | S0 | Hold |
| 5 | Gastric Ulcer (disease) | 99.58% | L3 | S2 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 為資料缺口）。不過根據收集到的文獻脈絡，Magnesium Trisilicate 屬於**典型制酸劑（antacid）**，在胃內與胃酸反應生成氯化鎂與膠體矽酸，中和胃酸、提高胃內 pH、降低胃蛋白酶活性，並在潰瘍表面形成保護層。

這個中和胃酸、保護黏膜的機轉，與消化性潰瘍（含胃潰瘍、胃空腸吻合口潰瘍等酸相關疾病）的致病機轉直接相關——酸暴露是潰瘍形成與延遲癒合的關鍵因素。歷史上（1930-1980 年代）已有多篇臨床研究將 Magnesium Trisilicate 單獨或與氫氧化鋁複方用於消化性潰瘍治療。

但需注意：多數文獻描述的是「peptic ulcer」這個籠統類別，並未特異指向「胃空腸吻合口潰瘍（marginal ulcer，通常發生於胃空腸吻合術後）」這個較窄的臨床實體，屬於機轉可外推、但疾病顆粒度不完全吻合的情況。此外，rank 1、2、4 三個適應症（活動性潰瘍、潰瘍穿孔、胃十二指腸炎）缺乏藥物專一或機轉高度吻合的證據支持，尤其潰瘍穿孔屬外科結構性急症，制酸治療機轉關聯薄弱。

---

## 臨床試驗證據

僅「胃潰瘍 (Gastric Ulcer)」適應症有 1 個相關登記試驗，且相關性評級為 C（低）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | 招募中 | 140 | Alginate vs Sucralfate 併用 PPI 治療 GERD 症狀緩解；未使用 Magnesium Trisilicate，適應症也非胃潰瘍，僅同屬制酸/黏膜保護藥物類別，相關性低 |

其餘 4 個預測適應症（活動性潰瘍病、潰瘍穿孔、胃空腸吻合口潰瘍、胃十二指腸炎）**目前無相關臨床試驗登記**。

---

## 文獻證據

以下為「胃空腸吻合口潰瘍」與「胃潰瘍」兩項適應症中，與 Magnesium Trisilicate 直接相關或機轉高度相關的文獻（合併列出，最多 10 篇，優先列 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14248445](https://pubmed.ncbi.nlm.nih.gov/14248445/) | 1965 | RCT（雙盲） | British Medical Journal | 雙盲比較 bismuth aluminate 與 magnesium trisilicate 治療消化性潰瘍，併行胃酸分析 |
| [20321118](https://pubmed.ncbi.nlm.nih.gov/20321118/) | 1938 | Case series | Canadian Medical Association Journal | Magnesium Trisilicate 治療消化性潰瘍之早期臨床觀察 |
| [15425465](https://pubmed.ncbi.nlm.nih.gov/15425465/) | 1950 | Cohort | Am J Digestive Diseases | 氫氧化鋁+Magnesium Trisilicate+黏蛋白治療 125 例消化性潰瘍患者 |
| [20271751](https://pubmed.ncbi.nlm.nih.gov/20271751/) | 1947 | Cohort | Archives of Surgery | 同上複方之胃鏡與臨床追蹤研究 |
| [6328685](https://pubmed.ncbi.nlm.nih.gov/6328685/) | 1984 | Cohort/比較性研究 | S Afr Medical Journal | 含 Magnesium Trisilicate 之抗酸劑（Gelusil）vs Ranitidine，4 週潰瘍癒合率無顯著差異 |
| [4301560](https://pubmed.ncbi.nlm.nih.gov/4301560/) | 1968 | Cohort | Wiener Medizinische Wochenschrift | Magnesium Trisilicate-hyoscyamine 複方（Neoplex B）制酸效果之臨床功能分析 |
| [6547921](https://pubmed.ncbi.nlm.nih.gov/6547921/) | 1984 | Mechanistic/機轉研究 | Fortschritte der Medizin | Sucralfate、氫氧化鋁、Magnesium Trisilicate 對胃潰瘍局部電位差之影響 |
| [6091079](https://pubmed.ncbi.nlm.nih.gov/6091079/) | 1984 | 比較性研究 | Postgraduate Medical Journal | 四種抗酸劑之隨機雙盲比較（含 Magnesium Trisilicate 類製劑） |
| [6293043](https://pubmed.ncbi.nlm.nih.gov/6293043/) | 1982 | Cohort | Scand J Gastroenterol Suppl | 制酸劑療法對礦物質代謝之影響（安全性相關） |
| [4909818](https://pubmed.ncbi.nlm.nih.gov/4909818/) | 1970 | Cohort（對照組使用含 Mg trisilicate 安慰劑） | Gut | Duogastrone（carbenoxolone）治療十二指腸潰瘍試驗 |

---

## 香港上市資訊

目前香港無 Magnesium Trisilicate 相關許可證登記（`market_status`: 未上市，`total_licenses`: 0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 藥物在香港未上市、無登記許可證，且缺乏 TFDA/仿單警語、禁忌症與 MOA 等關鍵安全性資料（阻斷性資料缺口 DG001）。
- 雖然「胃空腸吻合口潰瘍」與「胃潰瘍」兩項適應症達到 L3 證據等級並標記為 Research Question，但現有文獻多為 1930-1980 年代的抗酸劑類別研究，僅 1 篇為雙盲 RCT，且多數研究對象是複方製劑而非單一成分，證據強度不足以支持直接推進。

**若要推進需要：**
- 補齊作用機轉（MOA）與仿單警語/禁忌資料（DG001、DG002）
- 確認香港上市/許可證登記可行性
- 若聚焦「胃空腸吻合口潰瘍」，需要針對此特定臨床實體（而非籠統消化性潰瘍）設計之對照試驗，以縮小疾病顆粒度落差
- 排除潰瘍穿孔、胃十二指腸炎等機轉關聯薄弱或無實證支持的適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

