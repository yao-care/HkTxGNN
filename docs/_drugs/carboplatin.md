---
layout: default
title: Carboplatin
parent: 高證據等級 (L1-L2)
nav_order: 160
evidence_level: L2
indication_count: 10
---

# Carboplatin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Carboplatin：從鉑類化療藥物到女性乳癌 (Female Breast Carcinoma)

## 一句話總結

Carboplatin 是鉑類細胞毒性化療藥物，在香港已有 10 張許可證上市，但本次資料未載明原適應症。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，尤其是三陰性與 BRCA 缺陷型乳癌。
目前檢索到 **50 個臨床試驗登記**和 **20 篇文獻**，其中含 1 個已完成的 Phase 2/3 隨機試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：DrugBank 未列原適應症，香港許可證資料也沒有核准適應症文字，所以無法列出「原適應症」。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。但 carboplatin 屬鉑類藥物，一般認為它會與 DNA 形成加成物和交聯，阻斷快速分裂細胞的複製。

三陰性乳癌和 BRCA 缺陷型腫瘤的同源重組修復（homologous recombination repair）有缺陷，對鉑類 DNA 損傷特別敏感。這是模型預測合理的主要生物學依據。TxGNN 分數只是預測，不計入臨床證據。

臨床上已有隨機 Phase 2 資料支持在三陰性乳癌的新輔助治療加入 carboplatin，例如 GeparSixto 與 NeoSTOP。不過 DrugBank 沒有列出原適應症，「新穎性」是否成立，需要對照香港現行仿單確認。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | 完成 | 595 | 在三陰性與 HER2 陽性早期乳癌的新輔助治療中加入 carboplatin，隨機比較（GeparSixto） |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | 完成 | 961 | 高風險早期乳癌新輔助治療，比較兩種劑量密集方案（ETC 與含 carboplatin 的 PM(Cb)）（GeparOcto） |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | 完成 | 3222 | HER2 陽性乳癌輔助治療，比較 AC-T、AC-TH 與含 carboplatin 的 TCH |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | 進行中（不再招募） | 720 | 三陰性乳癌新輔助治療，每週 paclitaxel 對比 paclitaxel 加 carboplatin |
| [NCT01881230](https://clinicaltrials.gov/study/NCT01881230) | Phase 2/3 | 完成 | 191 | 轉移性三陰性乳癌一線治療，nab-paclitaxel 加 gemcitabine 或 carboplatin，對比 gemcitabine/carboplatin |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | 完成 | 148 | 轉移性遺傳性（BRCA）乳癌，carboplatin 對比 docetaxel |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | 完成 | 101 | Stage I-III 三陰性乳癌，carboplatin 加 docetaxel 或 paclitaxel，之後接 AC |
| [NCT00589238](https://clinicaltrials.gov/study/NCT00589238) | Phase 2 | 提前終止 | 16 | 基底樣乳癌，paclitaxel 加或不加 carboplatin；因提前終止，證據力有限 |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | 完成 | 45 | 三陰性乳癌新輔助 bevacizumab、docetaxel 加 carboplatin，單組試驗 |
| [NCT03639948](https://clinicaltrials.gov/study/NCT03639948) | Phase 2 | 進行中（不再招募） | 120 | 三陰性乳癌新輔助 pembrolizumab 加 carboplatin 與 docetaxel |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT（Phase 2） | Lancet Oncol | GeparSixto：在三陰性與 HER2 陽性早期乳癌的新輔助治療中加入 carboplatin，評估其療效 |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT（Phase 2） | Clin Cancer Res | NeoSTOP：比較含與不含 anthracycline 的 carboplatin 新輔助方案在 Stage I-III 三陰性乳癌的療效 |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT（Phase 3） | Eur J Cancer | BROCADE3：BRCA 突變晚期乳癌，veliparib 加 carboplatin/paclitaxel 的最終整體存活結果 |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | RCT（Phase 2） | Breast Cancer Res Treat | 晚期三陰性乳癌，比較單用 carboplatin 與 carboplatin 加 everolimus |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief：在含鉑的新輔助化療上加 camrelizumab 或安慰劑（carboplatin 為背景藥） |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | 統合分析 | PLoS One | 三陰性乳癌新輔助治療中，carboplatin 與 bevacizumab 均可提高病理完全緩解率 |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | 晚期乳癌中 paclitaxel 與 carboplatin 合併使用，其協同性、療效與安全性的累積證據 |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | 臨床試驗（Phase 2） | Breast Cancer Res | 乳癌腦轉移患者使用 carboplatin 加 bevacizumab 的安全性與療效 |
| [35837812](https://pubmed.ncbi.nlm.nih.gov/35837812/) | 2023 | 回溯性研究 | Cancer Med | HER2 陽性乳癌新輔助 TCHP，依 carboplatin 劑量比較貧血與病理完全緩解率（294 例） |
| [39944694](https://pubmed.ncbi.nlm.nih.gov/39944694/) | 2025 | 生物資訊學 | Front Immunol | 乳癌 carboplatin 抗藥性相關的 DNA 修復基因特徵與免疫浸潤的關聯 |

## 香港上市資訊

香港許可證資料未提供劑型與核准適應症文字，以下只列有資料的欄位（共 10 張，列出 5 張）。

| 許可證號 | 品名 | 持證商 |
|---------|------|--------|
| HK-35025 | PARAPLATIN INJ 10MG/ML | DKSH HONG KONG LIMITED |
| HK-61610 | CARBOPLATIN CONCENTRATE FOR SOLUTION FOR INFUSION 450MG/45ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-60146 | KEMOCARB INJ 450MG/45ML | FRESENIUS KABI HONG KONG LIMITED |
| HK-66515 | CARBOPLATIN-TRANET CONCENTRATE FOR SOLUTION FOR INFUSION 450MG/45ML | THE INTERNATIONAL MEDICAL COMPANY LIMITED |
| HK-65993 | CARBOPLATIN MYLAN CONCENTRATE FOR SOLUTION FOR INFUSION 150MG/15ML | VIATRIS HEALTHCARE HONG KONG LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（鉑類） |
| 骨髓抑制風險 | 高（以血小板減少為主，也常見嗜中性白血球減少與貧血；文獻 PMID 35837812 顯示合併 TCHP 時 3/4 級貧血常見） |
| 致吐性分級 | 中至高（依劑量而定，AUC ≥ 4 時通常視為高） |
| 監測項目 | CBC（含分類與血小板）、腎功能（劑量依腎功能計算）、肝功能、電解質；高劑量使用時需追蹤聽力（PMID 37715631 報告高劑量 carboplatin 的耳毒性） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

以上分級依藥物類別與已檢索文獻歸納，實際警語與注意事項請以原廠仿單為準。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
女性乳癌，特別是三陰性乳癌，有已完成的 Phase 2/3 隨機試驗（NCT01426880）與多個 Phase 2 隨機試驗支持 carboplatin 的貢獻，因此證據等級為 L2。但多數 Phase 3 試驗中 carboplatin 只是方案的一部分，不是被單獨檢驗的變項。目前也缺乏香港仿單的警語與禁忌資料，所以只能附帶條件推進。

**若要推進需要：**
- 取得香港衛生署的仿單，確認警語、禁忌症與現有核准適應症，判斷此適應症是否真的是新用途
- 補充 DrugBank 的作用機轉資料
- 把適用範圍限定在三陰性或 BRCA 缺陷型等明確亞型
- 建立骨髓抑制與嘔吐的監測及支持性治療計畫
- 評估 Phase 3 證據中 carboplatin 的獨立貢獻，例如針對 GeparOcto、NCT03168880 等試驗的後續結果

**其他預測適應症：** 成人生殖細胞腫瘤（L2，Proceed with Guardrails）在證據上與乳癌相當；子宮內膜混合型腺癌（L2，Proceed with Guardrails）也有 L2 證據，但組織學定義不一，需限縮在明確亞群。黏液性腺癌類預測（直腸、大腸、膽囊、膽管等）目前幾乎沒有專屬證據，建議 Hold。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

