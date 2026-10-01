---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Cabazitaxel：從（原適應症未載明）到女性乳癌

## 一句話總結

Cabazitaxel 是一種紫杉烷（taxane）類微管穩定劑，目前輸入資料未載明其原適應症。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，
目前**無臨床試驗登記**，但有 **20 篇文獻**（本報告列出其中 18 篇）支持這個方向，其中包含 1 項 Phase 2 隨機對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證的核准適應症欄位皆為空白） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2（有 1 項 Phase 2 RCT，但輸入資料無法確認其完成狀態與結果） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails（僅限研究層級，見結論） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為資料缺口）。根據文獻，Cabazitaxel 屬於紫杉烷類微管穩定劑，與 paclitaxel、docetaxel 同類。乳癌是對紫杉烷類有反應的腫瘤，因此 TxGNN 的預測在生物學上相當一致。

文獻另提供兩項機轉層面的線索：
- 在 βIII-tubulin 高表現的情況下，Cabazitaxel 的療效優於 docetaxel（PMID 28567478）。
- 在三陰性乳癌中，Cabazitaxel 可能透過調節巨噬細胞，增強 CD47 標靶免疫治療的效果（PMID 33753567）。

需要注意：這些多屬前臨床研究。目前沒有 Phase 3 證據，也沒有確認的優越性。這是一個站得住腳的研究問題，並非用藥建議。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

輸入資料僅提供部分文獻，其中 PMID 28768217 的內容不完整，其結果無法從本輸入驗證。以下依 RCT > 臨床試驗 > 回顧 > 前臨床排序，列出最相關的 10 篇：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | RCT（Phase 2） | Eur J Cancer | GENEVIEVE 試驗：比較 Cabazitaxel 與每週 paclitaxel 作為新輔助治療，對象為 HER2 陰性乳癌；主要指標為病理完全緩解率（結果未提供） |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase 1/2 | Eur J Cancer | Cabazitaxel 併用 capecitabine，用於接受過 anthracycline 與 taxane 治療後惡化的轉移性乳癌，評估最大耐受劑量與安全性 |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase 2 劑量探索 | Clin Breast Cancer | Cabazitaxel 併用 lapatinib，用於 HER2 陽性且有顱內轉移的乳癌（NCT01934894） |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | Br J Clin Pharmacol | 紫杉烷類藥物的治療藥物監測與劑量調整回顧 |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | 機轉研究 | Mol Cancer Ther | Cabazitaxel 抗藥性機制；在 MCF-7 乳癌細胞株中，其交叉抗藥性低於 paclitaxel 與 docetaxel |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | 前臨床機轉 | Cancer Chemother Pharmacol | βIII-tubulin 表現使 Cabazitaxel 療效優於 docetaxel |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | 前臨床機轉 | J Immunother Cancer | Cabazitaxel 作用於巨噬細胞，改善三陰性乳癌 CD47 標靶免疫治療 |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | 前臨床 | J Control Release | 奈米粒子包覆的 Cabazitaxel 在病人來源乳癌異種移植模型中療效較游離藥物佳 |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | 前臨床 | Acta Pharmacol Sin | 高分子微胞包覆的 Cabazitaxel 用於抑制乳癌轉移 |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | 前臨床 | Int J Nanomedicine | 不同聚氰基丙烯酸酯奈米粒子變體包覆 Cabazitaxel 的前臨床療效 |

其餘文獻多為藥物遞送配方研究（脂質體、NLC、胜肽共軛等）與一般性回顧。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61193 | JEVTANA（Sanofi Hong Kong） | 輸注用濃縮液與溶劑 60mg | 資料未載明 |
| HK-68945 | CABAZITAXEL EVER PHARMA 45mg/4.5ml | 輸注用濃縮液 | 資料未載明 |
| HK-68946 | CABAZITAXEL EVER PHARMA 50mg/5ml | 輸注用濃縮液 | 資料未載明 |
| HK-68947 | CABAZITAXEL EVER PHARMA 60mg/6ml | 輸注用濃縮液 | 資料未載明 |
| HK-68385 | CABAZITAXEL（Chemill Pharma）60mg/1.5ml | 輸注用濃縮液與溶劑 | 資料未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（紫杉烷類微管抑制劑） |
| 骨髓抑制風險 | 高（文獻指出嗜中性白血球減少與神經病變為主要不良反應） |
| 致吐性分級 | 低至中度（依藥物類別判斷，輸入資料未提供） |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

其餘細節請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症（供參考）

TxGNN 另預測 9 項適應症，皆無臨床試驗與文獻，證據等級為 L5，建議 Hold：

| 預測適應症 | TxGNN 分數 | 評估 |
|-----------|-----------|------|
| 鐮刀型血球疾病相關 5 種變體（Hb D、β-地中海貧血、Hb C、Hb E、遺傳性胎兒血紅素持續存在症） | 99.89% | 無明確機轉；相同分數顯示可能是知識圖譜的共用假象 |
| HIV 感染 | 99.82% | 無抗病毒機轉；骨髓抑制性化療用於免疫低下族群風險高 |
| 甲狀腺機能亢進 | 99.77% | 微管穩定與甲狀腺激素過多之間無已知關聯 |
| 神經母細胞瘤 | 99.75% | 增生性實體瘤，機轉上可想像，但無任何證據，且為兒童族群 |
| 類風濕性關節炎 | 99.72% | 已有更安全的疾病修飾療法，風險效益比低 |

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
乳癌為對紫杉烷類有反應的腫瘤，且已有 Phase 2 RCT（GENEVIEVE）及多項機轉研究支持。但目前無臨床試驗登記、無 Phase 3 證據、無確認的優越性，因此僅能視為值得研究的問題，不是用藥建議。

**若要推進需要：**
- 取得 GENEVIEVE 試驗的完整結果（病理完全緩解率與安全性）
- 補齊 DrugBank 作用機轉資料（MOA）
- 下載並解析香港衛生署仿單，取得警語與禁忌症（此為阻斷性資料缺口，未補齊前無法進入安全性篩選）
- 確認原適應症與各許可證的核准適應症文字
- 評估是否有 Phase 3 或更大型的乳癌試驗，並與現有標準紫杉烷治療比較

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

