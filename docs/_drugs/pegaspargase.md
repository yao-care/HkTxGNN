---
layout: default
title: Pegaspargase
parent: 高證據等級 (L1-L2)
nav_order: 657
evidence_level: L1
indication_count: 5
---

# Pegaspargase
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Pegaspargase：從（原適應症未登載）到前驅淋巴芽細胞淋巴瘤/白血病

## 一句話總結

Pegaspargase 是聚乙二醇修飾的 L-天門冬醯胺酶（Oncaspar），已在香港上市，但輸入資料沒有登載原適應症。
TxGNN 模型預測它可能對**前驅淋巴芽細胞淋巴瘤/白血病 (Precursor Lymphoblastic Lymphoma/Leukemia)** 有效，
目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向。這很可能是已核准的標準用途，而非真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 前驅淋巴芽細胞淋巴瘤/白血病 (Precursor Lymphoblastic Lymphoma/Leukemia) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Pegaspargase 是 E. coli 來源 L-天門冬醯胺酶的 PEG 化版本，作用是耗竭血中的天門冬醯胺 (asparagine)。淋巴芽細胞的天門冬醯胺合成酶 (ASNS) 表現低，無法自行合成足夠的天門冬醯胺。血中濃度下降後，白血病細胞的蛋白質合成受阻而死亡。DrugBank 的機轉欄位沒有資料，以上說明取自預測報告中的機轉推論。

這個機轉與淋巴芽細胞惡性腫瘤高度吻合。多項 Phase 3 試驗和 COG 的 Phase III 論文，已把 pegaspargase 放進兒童與成人急性淋巴芽細胞白血病 (ALL) 及淋巴芽細胞淋巴瘤的標準多藥化療架構。

輸入資料中的原適應症和作用機轉都是空白。依現有證據判斷，這比較像已核准的標準用途，而非新用途。建議先對照香港仿單，確認核准範圍後，再決定是否視為老藥新用候選。

## 臨床試驗證據

共 50 個試驗，以下列出 10 個最相關者。多數試驗把 pegaspargase 當作多藥化療的一環，療效歸因屬間接證據。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | 完成 | 166 | 直接比較 SC-PEG 與靜脈注射 Oncaspar（pegaspargase）用於高風險 ALL，pegaspargase 為對照組 |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | 完成 | 600 | Total Therapy XVI：比較高劑量與常規劑量 PEG-天門冬醯胺酶的臨床效益與藥動學 |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | 完成 | 650 | NOPHO 方案：比較間歇與持續給予 PEG-天門冬醯胺酶的無事件存活率 |
| [NCT01574274](https://clinicaltrials.gov/study/NCT01574274) | Phase 2 | 進行中（不再招募） | 240 | 隨機比較 Calaspargase pegol 與靜脈注射 Oncaspar，用於兒童與青少年 ALL/淋巴芽細胞淋巴瘤 |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | 進行中（不再招募） | 9,350 | COG 標準風險 B-ALL/局限性 B 淋巴芽細胞淋巴瘤的風險適應化療；pegaspargase 為骨幹成分，屬間接證據 |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | 完成 | 6,136 | 兒童與青少年 ALL 的國際合作方案，含天門冬醯胺酶的化療組合 |
| [NCT00866307](https://clinicaltrials.gov/study/NCT00866307) | Phase 1 | 完成 | 104 | 強化 pegaspargase 併用化療，用於新診斷高風險 ALL 的安全性試驗 |
| [NCT01005914](https://clinicaltrials.gov/study/NCT01005914) | Phase 2 | 提前終止 | 11 | 在 Hyper-CVAD 加入 PEG-天門冬醯胺酶，用於成人新診斷 ALL；樣本數過少 |
| [NCT00439296](https://clinicaltrials.gov/study/NCT00439296) | Phase 1/2 | 提前終止 | 9 | ABT-751 併用 PEG-天門冬醯胺酶等藥物，用於復發 ALL；樣本數過少 |
| [NCT04843150](https://clinicaltrials.gov/study/NCT04843150) | N/A | 完成 | 320 | ALLTogether 先導研究：PEG-天門冬醯胺酶初始劑量的藥動學與免疫原性 |

## 文獻證據

共 20 篇，以下列出 10 篇最相關者。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231：Bortezomib 用於新診斷 T-ALL/淋巴芽細胞淋巴瘤的 Phase III 試驗 |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232：Dexamethasone 與高劑量 Methotrexate 改善高風險 B-ALL 預後 |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434：Nelarabine 用於新診斷 T-ALL 的 Phase III 隨機試驗 |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001：比較 Calaspargase 與 Pegaspargase 的療效與毒性 |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Phase 2 | Blood Adv | GIMEMA LAL1913：成人 ALL 在化療中加入 Pegaspargase 的風險導向方案 |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Phase 2 | Int J Hematol | 日本新診斷 ALL 病人使用凍晶 Pegaspargase 的療效、安全性與藥動學 |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 追蹤 | Leukemia | Venetoclax 加入 Hyper-CVAD、Nelarabine 與 PEG 化天門冬醯胺酶，用於 T-ALL/淋巴芽細胞淋巴瘤的長期追蹤 |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | 專家共識：成人 ALL 使用天門冬醯胺酶/Pegaspargase 不良事件的辨識、預防與處置 |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Review | Blood | 成人 ALL 使用 Pegasparaginase 的毒性處置經驗 |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Pegaspargase 在 ALL 的整體回顧，已獲美國與歐盟核准用於 ALL 多藥化療 |

## 香港上市資訊

| 許可證號 | 品名 | 持有廠商 |
|---------|------|---------|
| HK-67823 | ONCASPAR POWDER FOR SOLUTION FOR INJECTION/INFUSION 3750 UNITS | SERVIER HONG KONG LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 酵素類抗腫瘤藥物（天門冬醯胺酶，PEG 化），機轉為耗竭天門冬醯胺，不直接損傷 DNA |
| 骨髓抑制風險 | 低（依藥物類別判斷，常與其他骨髓抑制藥物併用，需綜合評估） |
| 致吐性分級 | 低（依藥物類別判斷） |
| 監測項目 | 過敏反應、肝功能、胰臟酵素（胰臟炎）、三酸甘油酯、血糖、凝血功能（血栓風險）、血清天門冬醯胺酶活性 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

目前沒有仿單警語、禁忌症與藥物交互作用的資料，請參考原廠仿單。

文獻與試驗中反覆提到的天門冬醯胺酶類毒性如下：
- 過敏反應與沉默性失活（抗體使藥效消失）
- 胰臟炎
- 血栓
- 肝毒性
- 高三酸甘油酯血症
- 高血糖

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
針對急性淋巴芽細胞白血病/淋巴芽細胞淋巴瘤，有多個已完成的 Phase 3 試驗，且 pegaspargase 是標準化療架構中的成分，證據等級為 L1。不過，多數試驗並非單獨檢驗 pegaspargase，輸入資料也沒有原適應症和仿單，不能把它當成確定的老藥新用。

**若要推進需要：**
- 確認香港 HK-67823 的核准適應症，判斷這是已核准用途還是新增適應症
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩選
- 補充 DrugBank 的作用機轉資料
- 限定在有規範的多藥化療方案內使用，並監測過敏、胰臟炎、血栓、肝毒性與高三酸甘油酯血症
- 補齊其餘試驗與文獻的相關性評估，目前多數仍為待評估

另有兩類預測目前不建議推進：
- 慢性淋巴球性白血病/小淋巴球淋巴瘤（含兩個亞型）及濾泡性淋巴瘤，僅有模型分數，沒有臨床試驗或文獻，為 L5，建議 Hold。
- 「急性淋巴芽細胞白血病」（排名第 5）證據與本篇相同，同為 L1。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

