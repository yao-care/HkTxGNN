---
layout: default
title: Pimecrolimus
parent: 高證據等級 (L1-L2)
nav_order: 683
evidence_level: L2
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

# Pimecrolimus：從異位性皮膚炎到脂漏性皮膚炎

## 一句話總結

Pimecrolimus 是局部外用的鈣調神經磷酸酶抑制劑，市售品 Elidel 主要用於異位性皮膚炎。
TxGNN 模型預測它可能對**脂漏性皮膚炎 (Seborrheic Dermatitis)** 有效，
目前有 **1 個臨床試驗**和 **18 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未記載；依文獻與試驗資料為異位性皮膚炎 |
| 預測新適應症 | 脂漏性皮膚炎 (Seborrheic Dermatitis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據文獻，pimecrolimus 是外用鈣調神經磷酸酶抑制劑，會抑制 T 細胞活化，並減少 IL-2、IL-4、干擾素-γ、TNF-α 等發炎細胞激素的釋放，也會抑制肥胖細胞脫顆粒（PMID 16033622）。

脂漏性皮膚炎是慢性、反覆發作的發炎性皮膚病，好發於皮脂腺豐富的部位。發炎反應與皮膚共生黴菌 Malassezia 有關。T 細胞介導的皮膚發炎在機轉上可被鈣調神經磷酸酶抑制劑抑制，另有報告指 pimecrolimus 可能具有部分抗黴菌活性。因此，把它從異位性皮膚炎延伸到臉部脂漏性皮膚炎，在藥理上合理。

臨床上，它常被視為外用皮質類固醇以外的替代選擇，可避免長期使用類固醇的副作用。不過這個連結是依據已知藥理與文獻，並非來自本次提供的 MOA 記錄。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | 完成 | 113 | 4 週隨機雙盲、活性藥對照試驗，探索 Elidel 治療脂漏性皮膚炎的療效 |

目前沒有 Phase 3 RCT，這是證據停在 L2 的原因。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clin Exp Dermatol | 比較 pimecrolimus 1% 與 sertaconazole 2% 治療臉部脂漏性皮膚炎（摘要未提供結果） |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT | Ir J Med Sci | 比較 sertaconazole 2% 與 pimecrolimus 1% 乳膏治療脂漏性皮膚炎的療效（摘要未提供結果） |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | 系統性回顧（RCT） | Expert Rev Clin Pharmacol | Pimecrolimus 1% 乳膏耐受性良好且有效，與對照藥物的療效相當 |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | 系統性回顧（RCT） | Cureus | 回顧 pimecrolimus 治療臉部脂漏性皮膚炎的療效與安全性 |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | 開放性隨機對照 | J Dermatolog Treat | 比較 pimecrolimus 1% 與 ketoconazole 2% 乳膏 |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | 開放性研究 | Am J Clin Dermatol | 用於頑固性臉部脂漏性皮膚炎，有效且耐受良好 |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | 未分類研究 | J Cosmet Dermatol | 比較 pimecrolimus 1% 不同用藥療程治療臉部脂漏性皮膚炎 |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | 未分類研究 | Drugs Exp Clin Res | 評估對臉部與上軀幹脂漏性皮膚炎的療效、耐受性與安全性 |
| [19255921](https://pubmed.ncbi.nlm.nih.gov/19255921/) | 2009 | 未分類研究 | J Dermatolog Treat | 密切追蹤治癒與緩解時間及副作用，說明其仿單外使用日益增加 |
| [19391059](https://pubmed.ncbi.nlm.nih.gov/19391059/) | 2010 | 未分類研究 | J Dermatolog Treat | 探討反覆使用於復發性脂漏性皮膚炎的有效性與安全性 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51217 | ELIDEL CREAM 1% | VIATRIS HEALTHCARE HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

目前香港衛生署仿單的警語與禁忌資料尚未取得，藥物交互作用查詢也無結果。不過，外用鈣調神經磷酸酶抑制劑屬類別性的黑框警語（惡性腫瘤風險）。這個議題已有觀察性研究與統合分析（如 PMID 36370744）可供參考。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有 1 個完成的 Phase 2 活性藥對照 RCT（n=113），加上多項 RCT 與兩篇 RCT 系統性回顧，支持臉部脂漏性皮膚炎的療效。但缺乏 Phase 3 證據，且香港仿單的安全資料仍缺漏，因此需加上防護條件。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料（目前為阻擋性缺口，無法進入安全性篩選）
- 補齊 DrugBank 的作用機轉資料
- 限定使用範圍：僅限臉部、短療程，並排除誤診的黴菌感染（如 tinea incognito，PMID 20347654）
- 納入惡性腫瘤風險的追蹤與年齡、療程限制
- 若要提高證據等級，需要針對脂漏性皮膚炎的 Phase 3 RCT

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

