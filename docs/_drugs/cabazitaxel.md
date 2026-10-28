---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
monitor_inn: "Cabazitaxel"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin E disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "HIV infectious disease", "hyperthyroidism", "neuroblastoma", "rheumatoid arthritis"]
last_modified_at: 2026-10-28
description: "Cabazitaxel：預測新適應症為女性乳癌 (female breast carcinoma)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Cabazitaxel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Cabazitaxel：微管穩定型紫杉醇類抗腫瘤藥 → 女性乳癌 (female breast carcinoma)
{: .text-alpha }

## 一句話總結

Cabazitaxel 是一種半合成紫杉醇類（taxane）細胞毒性藥物。
TxGNN 模型預測它可能對**女性乳癌 (female breast carcinoma)** 有效。
目前沒有相關臨床試驗登記，文獻共 19 篇，多數為前臨床研究或綜述，另有 1 項直接針對乳癌的 Phase 2 研究（GENEVIEVE）及其長期追蹤報告，以及 1 項 Phase 1/2 研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 女性乳癌 (female breast carcinoma) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。依據已知藥理，Cabazitaxel 屬於半合成紫杉醇類藥物，能穩定微管、抑制有絲分裂紡錘體解聚，造成細胞有絲分裂停滯與死亡。

乳癌本身已有同類藥物（paclitaxel、docetaxel）作為標準治療，因此在機轉上具合理性。Cabazitaxel 對 P-醣蛋白（P-glycoprotein）外排幫浦的親和力較低，理論上可能對紫杉醇類抗藥的乳癌腫瘤仍有活性。文獻中的研究也顯示，它在部分抗藥細胞模型中的交叉抗藥性低於 paclitaxel 與 docetaxel。

不過，現有文獻大多是奈米載體、脂質載體等劑型的細胞與動物研究，或是紫杉醇類的一般性綜述。直接的人體研究僅有 GENEVIEVE（新輔助治療 Phase 2）與一項合併 capecitabine 的 Phase 1/2 研究。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | 隨機、開放性 Phase 2 | Eur J Cancer | GENEVIEVE：比較 cabazitaxel 與每週 paclitaxel 作為 HER2 陰性乳癌（三陰性或 luminal B）的新輔助治療，主要指標為病理完全緩解率 |
| [38663168](https://pubmed.ncbi.nlm.nih.gov/38663168/) | 2024 | Phase 2 長期追蹤 | ESMO Open | GENEVIEVE 長期結果，評估新輔助 cabazitaxel 與 paclitaxel 對長期預後的影響 |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase 1/2 | Eur J Cancer | Cabazitaxel 合併 capecitabine，用於已接受過蒽環類與紫杉醇類治療後惡化的轉移性乳癌，評估最大耐受劑量、安全性與活性 |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review／機轉研究 | Mol Cancer Ther | 在乳癌細胞模型中，cabazitaxel 的交叉抗藥性低於 paclitaxel 與 docetaxel |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs Today | Cabazitaxel 藥理與安全性概述，嗜中性白血球低下與神經病變為主要不良反應 |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | 前臨床 | J Immunother Cancer | Cabazitaxel 對巨噬細胞的作用可改善 CD47 標靶免疫治療於三陰性乳癌的效果 |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | 前臨床 | J Control Release | 載藥奈米粒子在病人來源乳癌異種移植模型中優於游離藥物 |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | 前臨床 | Acta Pharmacol Sin | 載藥高分子微胞用於治療乳癌轉移 |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | 前臨床 | Int J Nanomedicine | 載藥聚氰基丙烯酸酯奈米粒子變體的前臨床療效 |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | 前臨床 | Colloids Surf B | 載藥奈米結構脂質載體對乳癌細胞株的評估 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68945 | CABAZITAXEL EVER PHARMA CONCENTRATE FOR SOLUTION FOR INFUSION 45MG/4.5ML | 輸注濃縮液 | 本地資料未記錄 |
| HK-68946 | CABAZITAXEL EVER PHARMA CONCENTRATE FOR SOLUTION FOR INFUSION 50MG/5ML | 輸注濃縮液 | 本地資料未記錄 |
| HK-61193 | JEVTANA CONCENTRATE AND SOLVENT FOR SOLUTION FOR INFUSION 60MG | 輸注濃縮液 | 本地資料未記錄 |
| HK-68947 | CABAZITAXEL EVER PHARMA CONCENTRATE FOR SOLUTION FOR INFUSION 60MG/6ML | 輸注濃縮液 | 本地資料未記錄 |
| HK-68385 | CABAZITAXEL CONCENTRATE AND SOLVENT FOR SOLUTION FOR INFUSION 60MG/1.5ML | 輸注濃縮液 | 本地資料未記錄 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（紫杉醇類，微管抑制劑） |
| 骨髓抑制風險 | 高（文獻指出嗜中性白血球低下為主要不良反應） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 全血球計數（CBC，含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **藥物交互作用**：已查詢到多筆交互作用，其中屬重大等級者包括 deferiprone 與 samarium (153Sm) lexidronam；中度等級包括 aprepitant、clarithromycin、clotrimazole、metronidazole、miconazole、rosuvastatin、simvastatin、ticagrelor 等。
- 其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有直接針對乳癌的 Phase 2 隨機研究（GENEVIEVE）及其長期追蹤、以及 Phase 1/2 研究，加上機轉合理，支持進一步評估。但目前無已登記的臨床試驗，且 GENEVIEVE 結果細節未在資料中呈現，證據尚不足以直接推進臨床使用。
- 此藥骨髓抑制風險高，必須嚴密控管。

**若要推進需要：**
- 取得 GENEVIEVE 的完整療效與安全性數據，並與現行標準紫杉醇類療法比較
- 取得完整作用機轉資料與原廠仿單中的警語、禁忌症
- 規劃血液學監測與劑量調整方案
- 釐清適用的乳癌亞型（如三陰性乳癌、紫杉醇類抗藥者）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

