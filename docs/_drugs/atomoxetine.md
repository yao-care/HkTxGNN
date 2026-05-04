---
layout: default
title: Atomoxetine
parent: 高證據等級 (L1-L2)
nav_order: 68
evidence_level: L1
indication_count: 10
---

# Atomoxetine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Atomoxetine：從 ADHD 到特定發展障礙

## 一句話總結

Atomoxetine（阿托莫西汀）是一種選擇性去甲腎上腺素再攝取抑制劑（NRI），已在美國（2002 年）、歐洲及全球逾 97 個國家取得 ADHD 核准適應症，但**目前在香港尚未上市**。
TxGNN 模型預測它可能對**特定發展障礙 (Specific Developmental Disorder)** 有效，
目前有 **8 個臨床試驗**和 **15 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ADHD（注意力不足過動症，於美國/歐洲已核准；香港無上市記錄） |
| 預測新適應症 | 特定發展障礙 (Specific Developmental Disorder) |
| TxGNN 預測分數 | 99.9985% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

本 Evidence Pack 中的詳細作用機轉資料尚待補充。根據已知資訊，Atomoxetine 為選擇性去甲腎上腺素再攝取抑制劑，透過抑制突觸前去甲腎上腺素轉運體（NET，由 *SLC6A2* 基因編碼），提升前額葉皮質中的去甲腎上腺素濃度，從而改善注意力調節、執行功能與衝動抑制等核心症狀。與興奮劑（methylphenidate）不同，Atomoxetine 不作用於多巴胺轉運體，對成癮風險較低，且可於全天維持穩定血中濃度。

在分類上，ADHD 屬於 ICD-10 F80-F89「心理發展障礙」大類，而 TxGNN 預測的「特定發展障礙 (Specific Developmental Disorder)」正涵蓋此範疇，包括語言、學習、動作及混合型發展障礙，以及與 ADHD 高度共病的自閉症類群障礙（ASD）。現有臨床試驗已直接在 ASD 合併 ADHD 症狀的族群（Phase 3/4 RCT）中驗證其療效。

值得特別指出的是：**Atomoxetine 在香港的「再利用」本質上是市場准入機會，而非全新藥理假說**。其對 ADHD 及神經發展障礙族群的臨床實證已高度成熟，香港目前尚無核准商品，構成明確的未滿足醫療需求缺口。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00510276](https://clinicaltrials.gov/study/NCT00510276) | Phase 4 | 完成 | 445 | 雙盲 RCT，評估 Atomoxetine 在青年成人 ADHD 症狀療效與功能性結果，含網路自陳式社區樣本臂 |
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Phase 4 | 完成 | 396 | 多中心雙盲試驗，比較 Guanfacine-PR vs Atomoxetine vs 安慰劑於 6-17 歲 ADHD 兒童青少年的安全性與療效 |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | 完成 | 1398 | ADDUCE 大型觀察性研究，評估 methylphenidate 等 ADHD 藥物（含 Atomoxetine 對照）對生長、神經系統及心血管系統的兩年期影響 |
| [NCT00380692](https://clinicaltrials.gov/study/NCT00380692) | Phase 4 | 完成 | 97 | 隨機雙盲安慰劑對照試驗，評估 Atomoxetine 改善自閉症類群兒童青少年 ADHD 症狀的療效 |
| [NCT00498173](https://clinicaltrials.gov/study/NCT00498173) | Phase 3 | 完成 | 60 | 雙盲安慰劑對照試驗，評估 Atomoxetine 治療自閉症、亞斯伯格症及 PDD-NOS 合併 ADHD 症狀的療效 |
| [NCT00844753](https://clinicaltrials.gov/study/NCT00844753) | Phase 4 | 完成 | 128 | 平行雙盲設計，比較 Atomoxetine 合併/不合併家長管理訓練（PMT）在神經發展族群（ASD）的效果 |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | 完成 | 27 | 探索成人 ADHD 合併抽菸行為中 Atomoxetine 對尼古丁強化機制的影響（樣本小，次要相關） |
| [NCT05635318](https://clinicaltrials.gov/study/NCT05635318) | N/A | 不明 | 102 | 量化 EEG 神經回饋作為 ADHD 輔助療法的評估研究，Atomoxetine 作為比較組（試驗狀態不明）|

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Network Meta-analysis | The Lancet Psychiatry | 比較成人 ADHD 藥物、心理及神經刺激治療的相對療效與可接受性，為目前最高等級綜合分析 |
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Systematic Review + Meta-analysis | Autism Research | 統合 3 個 RCT（n=241），評估 Atomoxetine 在自閉症兒童合併 ADHD 症狀的療效（GRADE 評估）|
| [32946507](https://pubmed.ncbi.nlm.nih.gov/32946507/) | 2020 | Systematic Review | PLoS One | 系統性回顧 Atomoxetine 等 ADHD 藥物在女童/女性的處方率及療效性別差異 |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Clinical Review | Ther Adv Psychopharmacology | 回顧 Atomoxetine 在 ADHD 合併對立反抗症、情緒障礙、焦慮症及廣泛發展障礙共病族群的療效 |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Cohort Study | Neuropsychopharmacology Reports | 回溯性世代研究，識別 Atomoxetine 成人 ADHD 6 個月長期療效（約 40% 有效率）之影響因子 |
| [41332541](https://pubmed.ncbi.nlm.nih.gov/41332541/) | 2025 | Neuroimaging Study | bioRxiv | 白質結構連接偏差可預測 ADHD 青少年症狀發展軌跡與 Atomoxetine 治療結果（潛在生物標記）|
| [39514707](https://pubmed.ncbi.nlm.nih.gov/39514707/) | 2024 | Case Report + Review | JDBP | ADHD 合併焦慮、憂鬱及自殺意念患者之遠距醫療管理，Atomoxetine 在複雜共病情境下的應用 |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Observational | Clinical EEG & Neuroscience | 量化 EEG 在兒童 ADHD 及學習障礙中的臨床應用，支持個人化治療評估工具的發展 |
| [18030077](https://pubmed.ncbi.nlm.nih.gov/18030077/) | 2007 | Practice Guidelines | JAACAP | 學前兒童（<6 歲）精神藥物治療指引，含 Atomoxetine 在極幼年兒童的使用建議與風險評估 |
| [16232017](https://pubmed.ncbi.nlm.nih.gov/16232017/) | 2005 | Pharmacotherapy Study | Pharmacotherapy | 分析 ADHD 兒童初始選擇 Atomoxetine（而非傳統興奮劑）治療的臨床預測因子 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：根據 FDA 已知資訊，Atomoxetine 帶有**黑框警語**（警示兒童及青少年自殺意念風險），以及肝毒性、心血管效應等重要警語。在取得香港上市申請前，應完整評估原廠（Eli Lilly）仿單及 FDA/EMA 核准標籤中的所有安全性資訊。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Atomoxetine 對 ADHD 及相關神經發展障礙族群的臨床實證達 L1 等級（多個已完成 Phase 3/4 RCT，超過 1,500 篇發表文獻），TxGNN 預測的「特定發展障礙」與其全球核准適應症高度吻合。香港目前無核准商品，構成清晰的市場准入缺口，而非需大量前期驗證的全新再利用假說。

**若要推進需要：**
- 補充完整作用機轉資料（MOA）：查詢 DrugBank API (DB00289)
- 取得原廠完整仿單，解析黑框警語、肝毒性及心血管監測要求
- 評估香港 ADHD 未滿足醫療需求與潛在患者規模
- 研究香港藥劑業及毒藥管理局（Pharmacy and Poisons Board）之本地上市申請流程
- 確認是否有現行香港進口管制或平行進口路徑可供使用
- 規劃上市後監測計畫，尤其針對兒童青少年自殺意念之主動監測機制
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

