---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 829
evidence_level: L5
indication_count: 5
---

# Sunitinib
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

# Sunitinib：從腎細胞癌到脂肪肉瘤

## 一句話總結

Sunitinib 是多標的酪胺酸激酶抑制劑，已是腎細胞癌的認可療法（依證據包的機轉說明）。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效。
目前有 **3 個臨床試驗**和 **9 篇文獻**與這個方向相關，但都是混合型非 GIST 肉瘤的 Phase 2 研究，**沒有脂肪肉瘤專屬的療效數據**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；依證據包機轉說明為腎細胞癌 |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L2（證據包評定；但相關試驗為單臂 Phase 2，非隨機對照） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據證據包的推論，Sunitinib 是多標的受體酪胺酸激酶抑制劑，作用於 VEGFR、PDGFR 和 KIT，可能抑制軟組織肉瘤中的血管新生與 PDGFR 驅動的訊號。

Sunitinib 在腎細胞癌和對 imatinib 抗藥的 GIST 等實體瘤已有應用，而這些腫瘤帶有類似的訊號異常。軟組織肉瘤常被當成同一種疾病治療，因此模型把脂肪肉瘤列為可能的新適應症。

不過要注意，現有的 Phase 2 研究收的是混合組織型的非 GIST 肉瘤（含平滑肌肉瘤、脂肪肉瘤、MFH 等），沒有提供脂肪肉瘤亞型的結果。預測分數高，不等於脂肪肉瘤有直接證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | 完成 | 53 | 連續給藥 Sunitinib 治療非 GIST 肉瘤，族群包含脂肪肉瘤；未提供各組織型的反應數據 |
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | 完成 | 48 | 單中心開放標籤試驗，用於轉移性或無法切除的軟組織肉瘤（含脂肪肉瘤）；未提供亞型結果 |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | 完成 | 131 | 測試的是 regorafenib，不是 Sunitinib，只能作為同類藥物的間接佐證 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase 2 試驗 | Int J Cancer | 單一機構研究，評估 Sunitinib 用於復發或難治的平滑肌肉瘤、脂肪肉瘤和 MFH 的安全性與療效（可得摘要未含結果數據） |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | 整理脂肪肉瘤的基因、表觀遺傳與轉錄體變異，探討標靶治療的選擇 |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | 成人軟組織肉瘤的新興療法概述 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | 軟組織肉瘤的藥物治療越來越依組織亞型決定 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 以組織型為導向的治療；trabectedin 對脂肪肉瘤（尤其黏液型）活性高 |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case report | Anticancer Res | 一例多線治療後的轉移性脂肪肉瘤，使用 Sunitinib 獲得長期臨床效益 |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | 試驗計畫書 | BMC Cancer | REGOSARC：regorafenib 用於晚期軟組織肉瘤的隨機 Phase 2 試驗設計（非 Sunitinib） |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | 基因體研究 | Oncotarget | 骨外黏液樣軟骨肉瘤的定序，並評估 Sunitinib 獲益的預測因子（非脂肪肉瘤） |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Case series | Am J Surg Pathol | 黏液樣發炎性肌纖維母細胞肉瘤的病理分析，與本藥關聯性低 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55406 | SUTENT CAP 12.5MG | Pfizer Corporation Hong Kong Limited |
| HK-55405 | SUTENT CAP 50MG | Pfizer Corporation Hong Kong Limited |
| HK-67681 | ALSUNI CAPSULES 12.5MG | Lotus Pharmaceutical HK Limited |
| HK-68626 | SUNITINIB CAPSULES 12.5MG | Chemill Pharma Limited |
| HK-68627 | SUNITINIB CAPSULES 50MG | Chemill Pharma Limited |

共 6 張許可證，上表列出其中 5 張。各許可證的劑型與核准適應症在資料中均未載明。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標的酪胺酸激酶抑制劑，作用於 VEGFR、PDGFR、KIT） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據都是混合組織型非 GIST 肉瘤的 Phase 2 研究，脂肪肉瘤沒有獨立的療效數據，且 Phase 2 為單臂試驗，證據強度有限。
- 香港仿單的警語與禁忌資料缺口屬於阻斷性（Blocking），目前無法進入安全性篩選。

**若要推進需要：**
- 取得 Phase 2 試驗（NCT00474994、NCT00400569、PMID 21154746）中脂肪肉瘤亞型的療效與安全性數據
- 下載並解析衛生署（Department of Health）的仿單，補齊警語、禁忌與藥物交互作用
- 補充 DrugBank 的作用機轉資料
- 與脂肪肉瘤現行標準治療（如 doxorubicin、trabectedin）比較其定位
- 補齊香港許可證的劑型與核准適應症資料

**補充：**同一份證據包中，**未分類腎細胞癌 (Unclassified RCC)** 這項預測的證據較完整（L2，建議 Proceed with Guardrails），有多個 Phase 2 試驗和非透明細胞型腎癌的 Phase 2 與真實世界研究，可作為後續優先評估的候選。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

