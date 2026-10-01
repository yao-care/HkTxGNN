---
layout: default
title: Imiquimod
parent: 高證據等級 (L1-L2)
nav_order: 457
evidence_level: L2
indication_count: 10
---

# Imiquimod
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

# Imiquimod：從外用免疫調節治療到癌前腫瘤 (Pre-malignant Neoplasm)

## 一句話總結

Imiquimod 是外用的 TLR7 促效劑（免疫反應調節劑），目前在香港以乳膏形式上市。
TxGNN 模型預測它可能對**癌前腫瘤 (Pre-malignant Neoplasm)** 有效。
目前有 **19 個臨床試驗**和 **9 篇文獻**支持這個方向，但其中真正屬於癌前病變的試驗，多數樣本數很小或提前終止。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 癌前腫瘤 (Pre-malignant Neoplasm) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

> 證據等級說明：依判定規則，已完成且為隨機對照的試驗中，最明確的是 Phase 2 的子宮頸上皮內瘤變試驗（NCT03233412，n=90），因此判為 L2。Evidence Pack 原標示 L1，但 Phase 3 試驗中，已完成且適應症明確的並無 2 個：NCT01720407 的病變類型需再確認，NCT00175643 為單臂試驗，NCT02329171 則提前終止。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。以下根據一般藥理知識說明：Imiquimod 是 TLR7 促效劑，會在局部誘發 IFN-α、TNF-α 和 IL-12，活化先天與後天免疫，進而對抗腫瘤與病毒感染。

癌前病變（如子宮頸、外陰、肛門的上皮內瘤變，以及光化性角化症）多發生在上皮組織，且常與 HPV 感染有關。局部免疫活化有機會清除這些異常增生的上皮，這與 Imiquimod 的作用方式相符。文獻中也有多篇回顧與個案報告，描述外用 Imiquimod 用於外陰上皮內瘤變、鮑恩樣丘疹病等癌前病變。

但要注意，預測分數高不等於臨床有效。目前最直接的試驗（NCT02329171）只收了 9 人就提前終止，無法支持療效結論。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | 提前終止 | 9 | 外用 Imiquimod 治療高度子宮頸上皮內瘤變（CIN 2-3）的隨機對照試驗，樣本過少，無法下療效結論 |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | 完成 | 90 | 隨機試驗，評估外用 Imiquimod 治療高度子宮頸上皮內瘤變的療效 |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | 完成 | 259 | 以 Imiquimod 作為臉部惡性雀斑（原位病變）的術前輔助治療，目的是縮小切除範圍；病變類型仍需確認 |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | 完成 | 5 | 探討 HPV 相關病變的免疫逃避機轉，以及 Imiquimod 治療外陰上皮內瘤變的機轉；樣本太小 |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | 未知 | 20 | 冷凍治療後使用 3.75% Imiquimod 乳膏處理肥厚性光化性角化症 |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | 完成 | 20 | 開放標示試驗，5% Imiquimod 乳膏每週 3 次，用於頭部光化性角化症 |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | 提前終止 | 49 | 比較 5%、0.05% 及奈米包覆 0.05% Imiquimod 凝膠治療光化性唇炎 |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | 完成 | 16 | 早期口腔鱗狀細胞癌的術前 Imiquimod 免疫治療先導試驗，屬癌症而非癌前病變 |

另有 11 個試驗中，Imiquimod 僅為疫苗佐劑或組合治療成分（如神經膠質瘤、黑色素瘤疫苗），與癌前病變的直接關聯低，未列入。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 肛門上皮內瘤變（癌前病變）的介入治療回顧 |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 高度外陰上皮內瘤變的藥物治療回顧 |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | 非黑色素瘤皮膚癌的光動力療法及其合併治療 |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | 非黑色素瘤皮膚癌及癌前病變的外用治療，含 fluorouracil、diclofenac、imiquimod 與光動力療法 |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | 光化性角化症（癌前皮膚病變）的現行處置 |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | 前臨床（動物） | Urol Oncol | 兩種 TLR7 促效劑在大鼠膀胱內及靜脈給藥的藥動與藥效比較；TLR7 促效劑已用於（癌前）皮膚病變 |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | 個案報告 | Int J STD AIDS | 腎臟移植病人的高度外陰上皮內瘤變，以 5% Imiquimod 成功治療 |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | 個案報告 | Int J STD AIDS | 陰莖鮑恩樣丘疹病，以 5% Imiquimod 乳膏成功清除 |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | 影像診斷研究 | Hautarzt | 以光學同調斷層掃描診斷光化性汗孔角化症，僅為診斷報告，療效參考價值低 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-44090 | ALDARA CREAM 5% | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-68923 | IMIQUIMOD CREAM USP 5% W/W | HONG KONG MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多篇回顧、個案報告及數個完成的試驗，顯示 Imiquimod 用於上皮性癌前病變在機轉與臨床上都有依據。
- 最直接的 CIN 試驗有兩個，一個提前終止（n=9），另一個是 Phase 2（n=90），尚無大型確證性結果。
- 香港仿單的警語與禁忌資料缺失（Evidence Pack 標為阻斷性缺口 DG001），必須先補齊才能往下走。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與藥物交互作用。
- 取得 DrugBank 的作用機轉資料，並確認香港許可證的核准適應症。
- 詳讀 NCT03233412 與 NCT01720407 的結果，確認 NCT01720407 的病變類型，並釐清「癌前腫瘤」是否要縮小到特定病灶（如 CIN、VIN、光化性角化症）。
- 個案報告中曾出現不良事件（如口腔乳突瘤惡性轉變、多形性紅斑、扁平苔癬），黏膜部位使用時需特別留意。

**其他預測適應症（簡述）：**「口腔黏膜良性腫瘤」證據等級 L4，僅有回顧與動物實驗，列為研究問題。「奇形瘤」「內耳腫瘤」等其餘 8 項預測中，除口腔黏膜外的多數證據為 L4–L5，建議 Hold。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

