---
layout: default
title: Uracil
parent: 僅模型預測 (L5)
nav_order: 903
evidence_level: L5
indication_count: 10
---

# Uracil
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

# Uracil：從 UFT 複方成分（原適應症未載明）到結腸腫瘤

## 一句話總結

Uracil（尿嘧啶）在香港以 UFT（tegafur-uracil）類複方上市，在複方中扮演調節劑角色，資料中未載明單獨的原適應症。
TxGNN 模型預測它可能對**結腸腫瘤 (Colonic Neoplasm)** 有效，資料庫收錄 **50 個相關臨床試驗**和 **20 篇文獻**。
但其中只有 1 個試驗實際使用 UFT，**沒有任何證據是單獨測試 uracil**，臨床療效主要來自 tegafur 與複方，不是 uracil 本身。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 結腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L4（證據多屬 UFT 複方或氟尿嘧啶類，無 uracil 單獨證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據證據包的推論，uracil 沒有單獨的抗腫瘤適應症。它的相關機轉來自 UFT（tegafur 與 uracil 以 4:1 組成）。Uracil 會競爭性抑制二氫嘧啶去氫酶（DPD），減少 5-FU 的降解，提高 tegafur 轉換出的 5-FU 暴露量。Uracil 也是嘧啶類物質，參與鹼基切除修復（uracil-DNA glycosylase）。

結腸癌的標準治療以 5-FU 為基礎，因此氟尿嘧啶類藥物與結腸腫瘤的關聯很強。我們推測，TxGNN 給出高分，主要是因為 uracil 在知識圖譜中與氟尿嘧啶類相鄰。

要特別注意：文獻中的 Phase 3 證據（如 NSABP C-06、ACTS-CC 02）是針對 **UFT/leucovorin 複方**，療效主要由 tegafur 提供。這些證據不能直接當作 uracil 單獨有效的證明。

## 臨床試驗證據

資料庫共收錄 50 個試驗，以下列出與氟尿嘧啶類關聯較高的 10 個。只有 NCT01225744 直接使用 UFT，其餘為氟尿嘧啶類骨幹，沒有任何試驗單獨測試 uracil。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | 完成 | 47 | cetuximab + irinotecan + oxaliplatin + UFT 用於轉移性結直腸癌第一線，主要指標為客觀反應率（唯一直接含 UFT 的試驗） |
| [NCT00217737](https://clinicaltrials.gov/study/NCT00217737) | Phase 3 | 進行中（不再招募） | 2431 | 高復發風險 II 期結腸癌，比較 5-FU/LV/oxaliplatin 加或不加 bevacizumab（僅氟尿嘧啶類層級關聯） |
| [NCT00182715](https://clinicaltrials.gov/study/NCT00182715) | Phase 3 | 未知 | 2421 | COIN 試驗：oxaliplatin 加氟尿嘧啶類的連續、間歇與加 cetuximab 策略比較 |
| [NCT02893540](https://clinicaltrials.gov/study/NCT02893540) | Phase 2/3 | 未知 | 250 | 轉移性結直腸癌，capecitabine 節拍式與傳統化療維持治療比較 |
| [NCT00425152](https://clinicaltrials.gov/study/NCT00425152) | Phase 3 | 完成 | 2151 | Dukes B/C 結腸癌，比較 5-FU + LV、5-FU + levamisole 及三者合併 |
| [NCT00646607](https://clinicaltrials.gov/study/NCT00646607) | Phase 3 | 完成 | 3756 | II/III 期結腸癌輔助治療，FOLFOX-4 的 3 個月與 6 個月療程，及加 bevacizumab 的比較 |
| [NCT00145314](https://clinicaltrials.gov/study/NCT00145314) | Phase 3 | 完成 | 571 | 轉移性結直腸癌第一線，連續或間歇 FLOX 加 cetuximab |
| [NCT04269369](https://clinicaltrials.gov/study/NCT04269369) | Phase 4 | 未知 | 250 | 5-FU 或 capecitabine 治療前先做 DPD 基因與表型檢測，依結果減量以降低重度毒性 |
| [NCT05236972](https://clinicaltrials.gov/study/NCT05236972) | Phase 3 | 招募中 | 323 | dMMR/MSI-H III 期結腸癌，sintilimab 與 XELOX 比較（免疫治療，與 uracil 無關） |
| [NCT00101686](https://clinicaltrials.gov/study/NCT00101686) | Phase 3 | 完成 | 547 | 轉移性結直腸癌第一線，irinotecan 搭配三種氟尿嘧啶類給藥方式（輸注、單次、口服 capecitabine） |

## 文獻證據

文獻中有數篇直接涉及 UFT，但同樣不是 uracil 單獨使用。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06：比較口服 UFT + LV 與靜脈 5-FU + LV 作為 II/III 期結腸癌術後輔助治療，終點為無病存活與整體存活 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 五年更新：高風險 III 期結腸癌，S-1 + oxaliplatin 在無病存活上未優於 UFT/LV，並報告整體存活與病理分期的次族群分析 |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 Phase 3：驗證 SOX 是否優於 UFT/LV 作為高風險 III 期結腸癌輔助治療 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | 結直腸癌輔助治療：OK-432 免疫治療搭配口服嘧啶類（HCFU、UFT）不同組合的療效與安全性 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 世代研究與統合分析 | Medicine | 台灣健保資料庫：比較 UFT 與 5-FU 作為 II/III 期結腸癌術後輔助治療的無病存活與整體存活 |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | 前瞻性觀察研究 | BMC Cancer | JFMC46-1201：高風險 II 期結腸癌，以傾向分數配對比較 UFT/LV 與單純手術 |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | 前瞻性對照研究 | Int J Clin Oncol | JFMC46-1201 最終分析：先前報告 UFT/LV 的 3 年無病存活顯著高於單純手術，本次補充 5 年整體存活與風險因子分析 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | 回顧 UFT 作為肺、胃、結直腸及乳癌術後輔助治療的臨床證據與機轉，指出毒性輪廓溫和、適合輔助治療 |
| [26722024](https://pubmed.ncbi.nlm.nih.gov/26722024/) | 2016 | Review | Anticancer Res | 回顧口服氟尿嘧啶類（S-1、UFT 等 DPD 抑制策略）與 TAS-102 在結腸癌的角色 |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Case report | Cancer Chemother Pharmacol | 轉移性結腸癌患者使用 UFT 後出現溶血性貧血的個案 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48265 | UNITORAL CAP（HEALTHCARE PHARMASCIENCE LIMITED） | 未載明 | 未載明 |
| HK-60904 | UFUR CAP（HIND WING CO LTD） | 未載明 | 未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | Uracil 本身是 DPD 抑制性調節劑，併用的 tegafur 屬傳統細胞毒性藥物（氟尿嘧啶類） |
| 監測項目 | 文獻有 UFT 引起溶血性貧血的個案，建議至少追蹤血液學參數（CBC）及肝腎功能 |
| 其他（骨髓抑制、致吐性、處置防護） | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

證據包中沒有 uracil 的警語、禁忌症與藥物交互作用資料，安全性資訊請參考原廠仿單。

補充兩點：
- Uracil 抑制 DPD 會提高 5-FU 暴露量，與其他氟尿嘧啶類併用時需特別留意毒性。
- DPD 基因與表型檢測（見 NCT04269369）可能有助於降低氟尿嘧啶類的重度毒性。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何證據單獨測試 uracil。臨床證據多來自 UFT/LV 複方，療效主要由 tegafur 驅動，而 TxGNN 高分很可能只反映它在知識圖譜中靠近氟尿嘧啶類。
- 香港仿單的警語與禁忌症資料尚缺，安全性篩選無法進行（此為阻斷性缺口）。
- 其餘預測適應症（胃癌、直腸乙狀結腸交界腫瘤等）同樣沒有 uracil 專屬證據，其中多項為良性病灶，缺乏合理機轉。

**若要推進需要：**
- 取得香港衛生署兩張許可證（HK-48265、HK-60904）的仿單與核准適應症，補齊警語、禁忌症及交互作用資料。
- 補充 DrugBank 的作用機轉資料。
- 釐清評估對象是 UFT 複方還是 uracil 單獨使用，並據此重新界定研究問題。
- 若評估 UFT 在結腸癌的用途，需納入 DPD 基因檢測與血液學監測的安全計畫。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

