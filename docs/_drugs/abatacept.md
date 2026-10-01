---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# Abatacept：從類風濕性關節炎到類風濕性血管炎

## 一句話總結

Abatacept 是 CTLA4-Ig 融合蛋白，用於類風濕性關節炎等自體免疫疾病（原適應症依文獻判斷，香港許可證資料未載明）。
TxGNN 模型預測它可能對**類風濕性血管炎 (Rheumatoid Vasculitis)** 有效。
目前只有 **1 個不相關的臨床試驗**和 **約 10 篇相關文獻**（多為病例報告），證據不足，且結果互相矛盾。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎（依文獻判斷；香港許可證未載明適應症文字） |
| 預測新適應症 | 類風濕性血管炎 (Rheumatoid Vasculitis) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4（僅有病例報告與機轉推論，無 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Abatacept 是 CTLA4-Ig 融合蛋白，會阻斷 CD80/86 與 CD28 的 T 細胞共刺激訊號。DrugBank 的 MOA 欄位目前缺漏，以上機轉描述來自本次分析的機轉推論。

類風濕性血管炎是類風濕性關節炎的關節外併發症，由 T 細胞與免疫複合物驅動。阻斷 T 細胞共刺激在機轉上說得通，這也是模型給出高分的合理原因。

但臨床訊號並不一致。有 2 篇病例報告描述使用 abatacept 後改善，也有多篇報告描述在 abatacept 治療期間新發血管炎或 ANCA 相關腎炎。目前沒有任何前瞻性資料。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 尚未招募 | 80 | 風濕科患者接受全肩關節置換術時，比較術前免疫抑制劑停藥時間長短對疾病復發與術後併發症的影響。並非血管炎專屬研究，也未測試 abatacept 的療效，相關性低 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33595833](https://pubmed.ncbi.nlm.nih.gov/33595833/) | 2021 | 系統性回顧 | BioDrugs | 生物製劑與標靶合成藥物可能誘發風濕病患者的免疫性腎絲球疾病 |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | J Clin Med | 類風濕性關節炎相關上鞏膜炎與鞏膜炎的診斷與治療更新 |
| [31174819](https://pubmed.ncbi.nlm.nih.gov/31174819/) | 2018 | Review | Best Pract Res Clin Rheumatol | 類風濕性關節炎的中樞神經侵犯（含腦血管炎）及使用生物製劑的意涵 |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | 世代研究 | Ann Rheum Dis | 單中心資料，探討例行 ANA 檢測能否預測生物製劑相關的狼瘡與血管炎 |
| [22124545](https://pubmed.ncbi.nlm.nih.gov/22124545/) | 2012 | 病例報告 | Mod Rheumatol | 38 歲女性，對 MTX、TNF 抑制劑、類固醇、血漿置換及 IL-6 抑制劑反應不佳，使用 abatacept 後症狀迅速改善 |
| [29930884](https://pubmed.ncbi.nlm.nih.gov/29930884/) | 2018 | 病例報告 | Cureus | 合併常見變異型免疫缺乏症的類風濕性血管炎患者，abatacept 被提出作為可行的治療選項 |
| [27052429](https://pubmed.ncbi.nlm.nih.gov/27052429/) | 2016 | 病例報告 | Joint Bone Spine | abatacept 治療期間新發類風濕性血管炎，改用 rituximab 後改善（無摘要） |
| [30119075](https://pubmed.ncbi.nlm.nih.gov/30119075/) | 2018 | 病例報告 | Ophthalmic Plast Reconstr Surg | 使用 abatacept 期間出現雙側眼眶血管炎，cyclophosphamide 初期有效但病灶後來惡化 |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | 病例報告 | Intern Med | abatacept 合併 adalimumab 治療期間出現 ANCA 相關腎炎，改用 tocilizumab 後緩解 |

## 香港上市資訊

許可證資料未載明核准適應症與劑型欄位，劑型依品名整理。

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-58513 | ORENCIA LYOPHILIZED POWDER FOR IV INFUSION 250MG/VIAL | 凍晶粉末（靜脈輸注） | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |
| HK-61905 | ORENCIA SOLUTION FOR SUBCUTANEOUS INJ IN PRE-FILLED SYRINGE WITH ULTRASAFE PASSIVE NEEDLE GUARD 125MG/ML | 預充填注射筒（皮下注射，附安全針護套） | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |
| HK-61501 | ORENCIA SOLUTION FOR SUBCUTANEOUS INJECTION IN PRE-FILLED SYRINGE 125MG/ML | 預充填注射筒（皮下注射） | BRISTOL-MYERS SQUIBB PHARMA (HK) LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中有多例在 abatacept 治療期間出現血管炎或 ANCA 相關腎炎的報告。用於此適應症前，需特別留意藥物本身可能誘發或加重血管炎的風險。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅限少數病例報告，方向互相矛盾（有改善也有新發血管炎），無前瞻性資料。
- 香港仿單的警語與禁忌資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩選
- 補充 DrugBank 作用機轉資料
- 系統性整理類風濕性血管炎的病例系列與登錄資料，釐清 abatacept 是有效、無效還是誘發因素
- 若證據轉為正面，再評估設計小型前瞻性研究

**其他預測適應症備註：** 多發性關節型幼年類風濕性關節炎已有多個完成的 Phase 3 試驗（證據等級 L1），很可能是既有標示用途，並非新的老藥新用。乾癬性關節炎與脊椎關節病變類（發炎性脊椎病變）的證據相對較多，但需先釐清具體亞型。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

