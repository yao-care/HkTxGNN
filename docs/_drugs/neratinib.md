---
layout: default
title: Neratinib
parent: 僅模型預測 (L5)
nav_order: 613
evidence_level: L5
indication_count: 10
---

# Neratinib
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

# Neratinib：從 HER2 陽性乳癌到黃體素受體陽性乳癌

## 一句話總結

Neratinib 是不可逆的 pan-HER 酪胺酸激酶抑制劑，原本用於 HER2 陽性乳癌。
TxGNN 模型預測它可能對**黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)** 有效，
目前有 **2 個臨床試驗**（1 個進行中、1 個已撤回）和 **12 篇文獻**支持這個方向，但最強的證據仍屬於已核准的 HER2 陽性族群。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L2（依資料評分；見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：排名第 1 的預測為「normal breast-like subtype of breast carcinoma」（分數 99.68%），但該項僅有模型預測、無任何試驗或文獻（L5，Hold）。本報告改以證據最充分的排名第 2 項（黃體素受體陽性乳癌）為主軸。證據等級 L2 是資料評分結果；嚴格依本報告的判定規則，目前並無已完成的 Phase 2/3 試驗（唯一的 Phase 2 進行中，另一個已撤回），故此等級偏樂觀，應視為暫定。

## 為什麼這個預測合理？

目前缺乏經核准仿單的詳細作用機轉資料。根據已知資訊，Neratinib 是不可逆的 pan-HER（EGFR/HER2/HER4）酪胺酸激酶抑制劑，其在 HER2 陽性乳癌中的療效已被證實，機轉上也可能適用於荷爾蒙受體陽性的乳癌亞群。

在 HR+/HER2+ 乳癌中，HER2 與雌激素受體訊號之間存在交互作用（crosstalk），這是內分泌治療產生抗藥性的原因之一。因此將 Neratinib 與內分泌治療合併使用，在機轉上相當合理。延長輔助 Neratinib 治療（ExteNET 試驗）已在 HR+/HER2+ 族群中建立療效。

需注意：這部分證據與原本已核准的 HER2 陽性適應症高度重疊。真正屬於「再利用」的空間是 HR+/HER2 陰性但帶有 HER2 突變的族群（如 SUMMIT 試驗所探討），而針對此族群的 Phase 2 試驗已被撤回。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | 招募中 | 30 | 術前 Neratinib 併用內分泌治療與 Trastuzumab，用於 ER 陽性、HER2 陽性癌症；與合併治療理論直接相關，但族群與已核准適應症重疊且樣本小 |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Phase 2 | 已撤回 | 0 | Fulvestrant 併用 Neratinib，用於經治療的 HR 陽性、HER2 陰性轉移性乳癌；無受試者，未產生數據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncol | ExteNET：HER2 陽性早期乳癌在 Trastuzumab 輔助治療後，使用 12 個月 Neratinib 的 Phase 3 試驗 |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | RCT | N Engl J Med | I-SPY 2：高風險 II/III 期乳癌術前治療的適應性隨機 Phase 2 試驗，評估加入 Neratinib 的病理完全反應 |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | 指引 | J Natl Compr Canc Netw | NCCN 乳癌指引更新，CDK4/6 抑制劑改變 ER 陽性晚期乳癌的治療流程 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | 指引 | J Clin Oncol | ASCO 晚期 HER2 陽性乳癌全身性治療指引更新 |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Review | Clin Breast Cancer | HER2 陽性乳癌臨床進展與實務建議專家圓桌討論 |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncol | HR+/HER2+ 乳癌治療趨勢；荷爾蒙加抗 HER2 合併治療可使部分患者長期控制疾病 |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | 世代研究 | Breast Cancer Res Treat | HR+/HER2+ 早期乳癌輔助 Neratinib 的使用型態與耐受性；胃腸道副作用常導致停藥 |
| [41499317](https://pubmed.ncbi.nlm.nih.gov/41499317/) | 2026 | 世代研究 | Oncology | 現行臨床實務中輔助 Neratinib 的處方趨勢（ExteNET 進行時尚未使用 Pertuzumab 或 T-DM1） |
| [41886605](https://pubmed.ncbi.nlm.nih.gov/41886605/) | 2026 | 前臨床 | Cancer Res | 多體學分析發現 BRD8/EP400 是 HR+/HER2+ 乳癌抗 HER2 反應的關鍵染色質模組 |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | 回溯性分析 | Breast Cancer Res | ER 陽性、ERBB2 未擴增的浸潤性小葉癌中，可標靶的 ERBB2 突變與不良預後相關 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66416 | NERLYNX TABLETS 40MG | 錠劑 | 資料中未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（不可逆 pan-HER 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；文獻指出胃腸道副作用（腹瀉等）常導致停藥，須留意 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為主要項目：
  - **嚴重 (Major)**：Famotidine、Ranitidine、Cimetidine（H2 受體阻斷劑）；Omeprazole、Esomeprazole、Lansoprazole、Dexlansoprazole、Rabeprazole（質子幫浦抑制劑）；Aprepitant；Dexamethasone；Clarithromycin；Clotrimazole
  - **中度 (Moderate)**：Loperamide、Magnesium oxide、Aluminum hydroxide、Calcium carbonate、Empagliflozin、Naldemedine
  - **輕微 (Minor)**：Naloxegol、Fidaxomicin
  - 整體而言，降胃酸藥物與 CYP3A4 相關藥物是需要特別留意的類別。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 黃體素受體陽性乳癌有 Phase 3（ExteNET）、Phase 2 與多篇指引及文獻支持，機轉上合理；但這些證據主要來自已核准的 HER2 陽性族群，真正的新用途（HR+/HER2 陰性、HER2 突變）僅有 SUMMIT 等較早期的臨床資料，且唯一對應的 Phase 2 試驗已撤回。
- 其他排名較後的預測（如腱鞘巨細胞瘤、纖維母細胞瘤等）僅有模型預測，無試驗或文獻，建議維持 Hold。

**若要推進需要：**
- 以生物標記篩選族群（HER2 突變或擴增），避免用於 HER2 野生型的 Luminal A 腫瘤
- 取得香港仿單的警語、禁忌症與核准適應症，以完成安全性篩選
- 補充詳細作用機轉資料
- 制定腹瀉等胃腸道副作用的處置計畫，並審視與降胃酸藥物的併用
- 追蹤進行中的 NCT04886531 結果，並評估重新啟動 HR+/HER2 陰性族群試驗的可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

