---
layout: default
title: Minoxidil
parent: 高證據等級 (L1-L2)
nav_order: 500
evidence_level: L2
indication_count: 5
---

# Minoxidil
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Minoxidil：原適應症資料缺失 → 預測新適應症以瀰漫性圓禿（Diffuse Alopecia Areata）證據最強

## 一句話總結

本次證據包中 Minoxidil 的原始核准適應症資料缺失（香港未上市，無許可證紀錄，作用機轉亦為 Data Gap）。TxGNN 針對 5 個候選適應症進行預測，其中證據最紮實的是**瀰漫性圓禿 (Diffuse Alopecia Areata)**，有 **3 個臨床試驗**與 **20 篇文獻**支持；其餘 4 項候選多半僅有模型預測分數、缺乏直接臨床證據，其中「Pseudopelade of Brocq」經文獻檢視判斷極可能為疾病標籤與文獻檢索錯配，不建議採信。

## 快速總覽（主要候選：瀰漫性圓禿）

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（香港未上市，無許可證紀錄） |
| 預測新適應症 | 瀰漫性圓禿 (Diffuse Alopecia Areata) |
| TxGNN 預測分數 | 99.9998%（KG 排名第 5） |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

### 全部候選一覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|--------|-----------|---------|---------|------|
| 1 | Hypotrichosis simplex of the scalp | 99.9999% | L4 | S1 | Research Question |
| 2 | Congenital hypotrichosis with milia | 99.9999% | L5 | S0 | Hold |
| 3 | **Diffuse alopecia areata** | 99.9998% | L2 | S2 | **Proceed with Guardrails** |
| 4 | Pseudopelade of Brocq | 99.92%（KG 排名第 2107） | L4 | S0 | Hold（疑似錯配） |
| 5 | Pulmonary arterial hypertension | 99.92%（KG 排名第 2266） | L4 | S1 | Research Question |

## 為什麼這個預測合理？

目前缺乏 Minoxidil 詳細的作用機轉資料（DrugBank MOA 為 Data Gap）。根據既有藥理學共識與文獻內容可知，Minoxidil 為 K+ channel opener，已廣泛用於雄性禿（androgenetic alopecia）及其他非疤痕性落髮，機轉為延長毛囊生長期（anagen phase）並促進毛囊周邊血流。

瀰漫性圓禿（AA）為自體免疫性、非疤痕性落髮，毛囊結構未遭破壞，這與 Minoxidil 促進「存活毛囊」再生的機轉方向一致；口服／外用 Minoxidil 已廣泛作為 AA 的臨床輔助治療（常與 JAK 抑制劑、皮質類固醇合併使用）。相對地，排名第 4 的 Pseudopelade of Brocq 屬原發性**疤痕性**落髮（毛囊已纖維化破壞），機轉上與 Minoxidil 不匹配——經檢視其 20 篇文獻全數為雄性禿相關研究，判斷為 TxGNN 疾病標籤與文獻檢索的錯配，非真實適應症證據，不建議採信。

## 臨床試驗證據（瀰漫性圓禿）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01900041](https://clinicaltrials.gov/study/NCT01900041) | Phase 2 | 完成 | 74 | Pantovigar 併用 2% minoxidil vs 單用 2% minoxidil，針對女性型落髮（含 AA）之多中心、開放標籤比較試驗（Grade B：與 minoxidil 直接相關，惟公開資料未確認 minoxidil 是否為比較臂之一） |
| [NCT06527729](https://clinicaltrials.gov/study/NCT06527729) | Early Phase 1 | 完成 | 28 | Sildenafil 脂質奈米載體治療 AA，介入藥物非 minoxidil，僅疾病相同（Grade C，關聯性低） |
| [NCT04011748](https://clinicaltrials.gov/study/NCT04011748) | Phase 2 | 狀態未知 | 20 | 幹細胞教育療法治療 AA，介入與 minoxidil 機轉無關（Grade C） |

## 文獻證據（瀰漫性圓禿，節錄 10 篇最相關）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35796224](https://pubmed.ncbi.nlm.nih.gov/35796224/) | 2022 | RCT | Dermatologic Therapy | Methotrexate 1% gel vs minoxidil 5% gel 治療局部性 AA 之隨機對照試驗（n=50） |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | RCT | Dermatologic Therapy | Latanoprost、minoxidil 5%、betamethasone 及組合方案治療 AA 之多組盲性隨機對照試驗 |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 網絡統合分析 | Cochrane Database Syst Rev | AA 各類治療（含 minoxidil）之網絡統合分析比較療效 |
| [36800063](https://pubmed.ncbi.nlm.nih.gov/36800063/) | 2023 | 系統性回顧 | Lasers Med Sci | 雷射光療合併外用 minoxidil 治療 AA 之系統性回顧與統合分析 |
| [33940103](https://pubmed.ncbi.nlm.nih.gov/33940103/) | 2022 | 系統性回顧 | J Am Acad Dermatol | 兒童 AA 治療之系統性回顧 |
| [38169088](https://pubmed.ncbi.nlm.nih.gov/38169088/) | 2024 | 專家共識 | J Eur Acad Dermatol Venereol | 歐洲 AA 全身性治療專家共識聲明 |
| [35244759](https://pubmed.ncbi.nlm.nih.gov/35244759/) | 2023 | 回顧 | Arch Dermatol Res | 口服 minoxidil 用於雄性禿與休止期落髮之回顧 |
| [31499158](https://pubmed.ncbi.nlm.nih.gov/31499158/) | 2021 | 病例系列 | J Am Acad Dermatol | Tofacitinib 併用口服 minoxidil 治療重度 AA |
| [38634160](https://pubmed.ncbi.nlm.nih.gov/38634160/) | 2024 | 待分類 | Skin Res Technol | 微針注射 minoxidil 併用 triamcinolone acetonide 治療 AA 之回溯性觀察 |
| [37024053](https://pubmed.ncbi.nlm.nih.gov/37024053/) | 2023 | 待分類 | J Am Acad Dermatol | AA 病人 tofacitinib 與 baricitinib 轉換治療之臨床反應回顧 |

## 香港上市資訊

目前 Minoxidil 於香港**未上市**，無許可證登記紀錄。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails（限瀰漫性圓禿此候選）；其餘 4 項候選維持 Hold / Research Question**

**理由：**
- 瀰漫性圓禿有 1 個 Phase 2 RCT（Grade B）及多篇 RCT／統合分析／專家共識文獻支持，機轉外推合理，證據等級達 L2。
- 其餘候選（hypotrichosis simplex、congenital hypotrichosis with milia、pulmonary arterial hypertension）僅有病例報告或 1970 年代非目標族群之血行動力學觀察，證據薄弱；Pseudopelade of Brocq 判斷為文獻檢索錯配，不建議採信。

**若要推進需要：**
- 補齊 TFDA／香港仿單警語與禁忌（DG001，Blocking，目前無法進入 S1 安全性初評）
- 補齊 DrugBank 作用機轉資料（DG002，High，影響機轉關聯性分析）
- 確認 NCT01900041 中 minoxidil 是否確實為比較臂之一，以提升該試驗證據等級
- 各候選之給藥途徑相容性（route_compatibility）與原適應症相似度（similarity_to_original）目前均為 pending，需補齊後才能完成完整評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

