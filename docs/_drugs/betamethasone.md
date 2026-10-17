---
layout: default
title: Betamethasone
parent: 高證據等級 (L1-L2)
nav_order: 115
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Betamethasone：預測新適應症為圓形禿 (Alopecia Areata)（證據等級 L2）。原適應症：資料庫未提供許可證層級的核准適應症文字"
monitor_inn: "BETAMETHASONE"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions"]
---

# Betamethasone
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

# Betamethasone：從自體免疫與發炎性疾病到圓形禿

## 一句話總結

Betamethasone（倍他米松）是一種強效糖皮質類固醇，原本用於自體免疫疾病、發炎性腸道疾病、腎上腺皮質功能不足及部分血液腫瘤等。
TxGNN 模型預測它可能對**圓形禿 (Alopecia Areata)** 有效，
目前有 **6 個臨床試驗**和 **20 篇文獻**支持這個方向，其中 1 項 Phase 2 試驗已完成。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未提供許可證層級的核准適應症文字；知識圖譜列出自體免疫疾病、克隆氏症、發炎性腸道疾病、腎上腺皮質功能不足、急性淋巴性白血病、足癬、皮疹等 |
| 預測新適應症 | 圓形禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

圓形禿是 T 細胞介導的自體免疫疾病，毛囊的免疫豁免狀態被破壞，導致非疤痕性掉髮。
Betamethasone 是強效糖皮質類固醇，能抑制 T 細胞活化與促發炎細胞激素，直接針對這個免疫病理。
目前缺乏 DrugBank 詳細的作用機轉資料，以上機轉說明來自類固醇的已知藥理特性。

Betamethasone 原本就用於多種自體免疫與發炎性疾病，圓形禿同屬自體免疫範疇，因此預測在機轉上合理。
臨床上外用、病灶內注射與口服小劑量脈衝（mini-pulse）等給藥方式皆已被使用。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | 完成 | 60 | 每週 azathioprine 脈衝 vs 口服 betamethasone 小劑量脈衝，用於中重度圓形禿 |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | 完成 | 50 | 外用 latanoprost vs 外用類固醇（betamethasone），用於局部圓形禿 |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | 未知 | 59 | 外用 cetirizine 1% vs betamethasone valerate 0.1%，用於局部圓形禿 |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | 未知 | 60 | 外用 pentoxifylline、metformin vs betamethasone valerate 乳膏，用於斑塊狀圓形禿 |
| [NCT07696585](https://clinicaltrials.gov/study/NCT07696585) | N/A | 尚未招募 | 60 | Metformin、simvastatin 與 betamethasone valerate 外用治療，betamethasone 的貢獻無法單獨區分 |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | 招募中 | 250 | 中央離心性疤痕性禿髮的多治療組比較，與圓形禿屬不同疾病，僅間接相關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 網絡統合分析 | Cochrane Database Syst Rev | 比較圓形禿的免疫抑制劑、促毛髮生長藥物與接觸免疫療法等治療 |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | 微針經皮遞送複方 betamethasone，探討減輕病灶內注射疼痛 |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | 口服 cyclosporine 與 betamethasone 小劑量脈衝比較（60 位患者） |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iran J Pharm Res | 口服脈衝 betamethasone、methotrexate 及合併治療，雙盲安慰劑對照（36 位重度患者） |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | RCT | Dermatol Ther | Latanoprost 與 minoxidil、betamethasone 及合併療法比較 |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | J Dermatolog Treat | 病灶內 betamethasone vs triamcinolone，個體內隨機對照 |
| [27746635](https://pubmed.ncbi.nlm.nih.gov/27746635/) | 2016 | 比較研究 | Ann Dermatol | 口服 cyclosporine 與 betamethasone 小劑量脈衝比較 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | 類固醇脈衝治療圓形禿的療效、復發率與副作用 |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | 臨床研究 | Cureus | 口服 betamethasone 小劑量脈衝用於中重度圓形禿的療效與安全性 |
| [17642661](https://pubmed.ncbi.nlm.nih.gov/17642661/) | 2004 | 開放性無對照研究 | Indian J Dermatol Venereol Leprol | 口服 betamethasone 小劑量脈衝治療廣泛性圓形禿 |

## 香港上市資訊

香港共有 20 張有效許可證，皆為單方製劑，以下列出 5 張。資料庫未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-02807 | BETNOVATE CREAM 0.1%（GlaxoSmithKline） | 乳膏（依品名） | 未提供 |
| HK-02811 | BETNOVATE OINT 0.1%（GlaxoSmithKline） | 軟膏（依品名） | 未提供 |
| HK-06910 | BETNOVATE SCALP APPLICATION 0.1%（GlaxoSmithKline） | 頭皮外用製劑（依品名） | 未提供 |
| HK-34326 | SYNMETHASONE FORTE SYRUP 0.5MG/5ML（Marching Pharmaceutical） | 糖漿（依品名） | 未提供 |
| HK-35263 | BETAMETHASONE SYRUP 1MG/5ML（Quality Pharm Lab） | 糖漿（依品名） | 未提供 |

## 安全性考量

- **主要風險（依藥理特性與預測分析）**：長期或高劑量使用可能造成皮膚萎縮與下視丘-腦下垂體-腎上腺軸（HPA 軸）抑制，停藥後也可能復發。
- **知識圖譜標示的禁忌相關疾病**（非仿單內容）：高血壓、癲癇、高血糖、充血性心衰竭、單純疱疹病毒角膜炎、麻疹，以及腦下垂體功能低下相關疾病等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 重大（Major）：Adalimumab
  - 中度（Moderate）：Zidovudine、Isotretinoin、Acarbose、Ketorolac、Ibuprofen、Nifedipine、Ethinylestradiol、Fluvoxamine、Fosamprenavir 等
  - 輕微（Minor）：Formoterol、Salbutamol

香港仿單的警語與禁忌尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 項完成的 Phase 2 試驗，並有多項 RCT 與比較研究支持 betamethasone（外用、病灶內、口服小劑量脈衝）用於圓形禿，機轉合理且香港已有多種劑型上市。
- 但多數研究規模小、betamethasone 常作為對照組，且缺乏香港仿單安全性資料，需設置安全防護。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料
- 取得 DrugBank 的詳細作用機轉資料
- 確認給藥途徑（外用、病灶內、口服小劑量脈衝）與香港現有劑型的對應
- 建立長期使用的 HPA 軸抑制、皮膚萎縮與復發的監測計畫
- 評估與 adalimumab 等重大交互作用藥物併用時的風險

**其他預測適應症（供參考）：**
- 特發性類固醇敏感型腎病症候群：僅有 1981 年的小兒脈衝療法報告（L3），列為研究問題，尚無法推進。
- 毛囊黏蛋白症（alopecia mucinosa）：僅有 1964 年病例系列（L4）。建議暫緩，並需先排除皮膚 T 細胞淋巴瘤。
- 休止期落髮：機轉薄弱，證據不足（L4），建議暫緩。
- 禿髮性毛囊炎：僅有間接證據（L4），建議暫緩。
- 其餘 5 項預測（如類固醇抗性腎病症候群、多種遺傳性稀毛症候群等）僅有模型預測（L5），建議暫緩；其中抗體缺乏相關禿髮使用類固醇可能有害，類固醇抗性腎病症候群則與疾病定義矛盾。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

