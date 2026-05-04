---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Adalimumab：從類風濕性關節炎到類風濕血管炎

## 一句話總結

Adalimumab 是一種全人源化抗 TNF-α 單株抗體，全球已廣泛用於類風濕性關節炎（RA）、強直性脊椎炎及銀屑病關節炎等炎症性疾病，目前尚未在香港正式上市。
TxGNN 模型共預測 **6 個潛在適應症**，首要預測為**類風濕血管炎（Rheumatoid Vasculitis）**，目前有 **5 個臨床試驗**和 **20 篇文獻**提供間接支持；另有**炎性脊椎病**與**多關節型幼年特發性關節炎**兩個適應症具備 **L1 等級**的充分 Phase 3 RCT 證據，全球已屬獲批適應症，具高度臨床推進可行性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎（全球已批；香港未上市） |
| 首要預測適應症 | 類風濕血管炎 (Rheumatoid Vasculitis) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L3（類風濕血管炎） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question（類風濕血管炎） |

---

## 所有預測適應症一覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|---------|
| 1 | 類風濕血管炎 (Rheumatoid Vasculitis) | 99.80% | L3 | Research Question |
| 2 | 尾骨過度活動症 (Hypermobility of Coccyx) | 99.77% | L5 | **Hold** |
| 3 | 炎性脊椎病 (Inflammatory Spondylopathy) | 99.77% | L1 | **Proceed with Guardrails** |
| 4 | Kummell 病 (Kummell Disease) | 99.74% | L5 | **Hold** |
| 5 | 多關節型幼年特發性關節炎 (Polyarticular JIA) | 99.72% | L1 | **Proceed with Guardrails** |
| 6 | 椎體疾病 (Vertebral Disease) | 99.18% | L2 | Research Question |

> **排名 2（尾骨過度活動症）** 及 **排名 4（Kummell 病）** 為結構性/機械性病理，與 TNF-α 炎症通路無已知直接關聯，TxGNN 高分屬圖譜拓撲雜訊，不具臨床推進意義，以下不再詳述。

---

## 為什麼這個預測合理？

### 藥物作用機轉

Adalimumab 是全人源化 IgG1 單株抗體，可高親和力結合可溶性及膜結合型 TNF-α，阻斷其與受體（TNFR1、TNFR2）的交互作用，從而抑制下游 NF-κB 及 MAPK 等促炎信號通路。結果是降低血管細胞黏附分子（VCAM-1）表達、減少白血球穿越血管壁，以及抑制破骨細胞活化。

> 注：本 Evidence Pack 中詳細 MOA 資料（原廠仿單）缺失，以上描述基於已發表的 TNF-α 抑制劑藥理學文獻。

### 類風濕血管炎的關聯性（排名 1）

類風濕血管炎（RV）是 RA 最嚴重的關節外表現，以小至中型血管壁的免疫複合物沉積及補體活化為核心病理。TNF-α 在 RV 中驅動內皮活化、ICAM-1 上調及中性球浸潤，理論上 adalimumab 可抑制這些機轉。現有的系統性回顧（PMID 33058033）及個案報告（PMID 25133007）均有 adalimumab 在 RV 中發揮療效的直接紀錄。

**需特別警示**：多篇文獻（PMID 28719435、19482531、36418100）記錄 adalimumab 本身可誘發白血球碎裂性血管炎及 ANCA 相關腎炎，屬藥物不良事件。因此在 RV 患者中使用時，獲益風險平衡需個案審慎評估，並密切監測腎功能及 ANCA 指標。

### 炎性脊椎病的關聯性（排名 3）

炎性脊椎病（含 AS、axSpA、PsA 中軸型）的核心病理為 TNF-α 驅動的椎間盤旁及韌帶附著點（enthesis）炎症。Adalimumab 透過阻斷 TNF-α 降低 RANKL 表達、抑制破骨細胞活化，從而減少脊椎骨侵蝕與新骨形成。此機轉已獲多項 Phase 3 RCT 驗證，並被 EULAR/ACR 指引列為第一線 bDMARD 推薦——為本系列預測中證據最充分的適應症。

### 多關節型幼年特發性關節炎的關聯性（排名 5）

多關節型 JIA 的滑膜炎炎症機轉與成人 RA 高度相似，TNF-α 同為關鍵介質。FDA 於 2008 年批准 adalimumab 用於 2 歲以上多關節型 JIA（4mg/kg，每兩週皮下注射），並有完整兒科 PK/PD 資料及長達 10 年的 STRIVE 登記安全性追蹤。

---

## 臨床試驗證據（類風濕血管炎）

目前**無專屬針對 RV 設計的 RCT**；以下試驗提供間接相關資訊，僅保留 B 級以上。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 未知 | 750,000 | 大型資料庫研究，評估生物製劑使用者新發 IMID（含血管炎作為結局之一）風險，具流行病學背景參考價值 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | 已完成 | 184 | 多國觀察性研究，追蹤 tocilizumab 在 RA 患者療效，部分患者可能含 RV 亞群，可作間接對照 |

---

## 文獻證據（類風濕血管炎）

優先排列：Systematic Review > Cohort > Case Report

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | RV 生物製劑治療系統性回顧（PRISMA），涵蓋 adalimumab 等 TNF 抑制劑療效，為本適應症最直接的文獻 |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | J Clin Medicine | RA 相關鞏膜炎（血管炎亞型）診斷與管理更新，涵蓋生物製劑治療選擇 |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort / Pharmacovigilance | RMD Open | BSRBR-RA 大型隊列：比較 TNFi 與 nbDMARD 使用者發生狼瘡樣及血管炎樣事件的藥物特異性風險 |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Rep Rheumatol | RA 合併指端數字型血管炎個案使用 adalimumab 治療成功，提供直接療效個案依據 |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine | RV 患者減少 adalimumab 劑量後發生急性肺動脈高壓危象，強調維持治療的重要性 |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | Am J Dermatopathol | ⚠️ Adalimumab 誘發白血球碎裂性血管炎及皮膚血管旁噬血細胞症（不良事件報告，需納入風險評估） |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine | ⚠️ Adalimumab + abatacept 治療 RA 期間發生 MPO-ANCA 相關腎炎，tocilizumab 成功控制 |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Case Report | Nephrol Therapeutique | ⚠️ Adalimumab 治療 RA 期間誘發 ANCA 相關腎小球腎炎（壞死性腎炎），需停藥 |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | Case Report | Clin Exp Rheumatol | 多藥耐藥且 anti-TNF 無效的全身性 RV：改用抗 IL-6R 抗體（tocilizumab）治療成功，提示替代機轉 |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Observational | Ann Rheum Dis | ANA 常規檢測對預測生物製劑誘發狼瘡及血管炎的效用，對安全性監測有參考價值 |

---

## 臨床試驗證據（炎性脊椎病，排名 3 — L1 補充）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00085644](https://clinicaltrials.gov/study/NCT00085644) | Phase 3 | 已完成 | 315 | 多中心 RCT，adalimumab 40mg 每兩週用於活動性 AS，FDA 批准的關鍵樞紐試驗 |
| [NCT03259074](https://clinicaltrials.gov/study/NCT03259074) | Phase 3 | 已完成 | 859 | Secukinumab vs adalimumab 生物相似藥頭對頭比較，以 mSASSS 評估脊椎結構保護 |
| [NCT01083121](https://clinicaltrials.gov/study/NCT01083121) | N/A | 已完成 | 1,779 | 韓國上市後監測研究，真實世界 adalimumab 在炎性脊椎病患者的安全性與療效 |
| [NCT00427362](https://clinicaltrials.gov/study/NCT00427362) | Phase 3 | 已完成 | 127 | 加拿大開放標籤多中心研究，DMARD 反應不足之 PsA（炎性脊椎病亞型）患者使用 adalimumab |
| [NCT01474876](https://clinicaltrials.gov/study/NCT01474876) | N/A | 已完成 | 566 | 多國觀察性研究，評估 adalimumab 在 AS/PsA 患者 12 個月長期療效維持（中東歐真實世界） |
| [NCT01610947](https://clinicaltrials.gov/study/NCT01610947) | N/A | 已完成 | 398 | 隨機研究，AS 低疾病活動度患者 anti-TNF 注射間隔延長策略 |
| [NCT00195819](https://clinicaltrials.gov/study/NCT00195819) | Phase 3 | 已完成 | 82 | Adalimumab 在 AS 的多中心補充療效研究 |

---

## 臨床試驗證據（多關節型幼年特發性關節炎，排名 5 — L1 補充）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00048542](https://clinicaltrials.gov/study/NCT00048542) | Phase 3 | 已完成 | 171 | 核心樞紐試驗：多中心隨機雙盲安慰劑對照，評估 adalimumab 在 4–17 歲 polyJIA 兒童安全性、療效及 PK，FDA 批准的直接依據 |
| [NCT02840175](https://clinicaltrials.gov/study/NCT02840175) | Phase 3 | 已完成 | 62 | JIA 緩解後 adalimumab 停藥策略隨機對照研究，評估減藥安全性 |
| [NCT00690573](https://clinicaltrials.gov/study/NCT00690573) | Phase 3 | 已完成 | 25 | 日本多中心開放標籤研究，延伸評估 adalimumab 在亞洲 polyJIA 兒童的長期安全性 |
| [NCT00775437](https://clinicaltrials.gov/study/NCT00775437) | Phase 3 | 已完成 | 32 | 同情性用藥研究，擴展至 2–4 歲及體重 < 15 kg 的極幼齡 JIA 兒童安全性與 PK 數據 |
| [NCT06654882](https://clinicaltrials.gov/study/NCT06654882) | Phase 3 | 招募中 | 400 | 多中心 SMART 隨機設計試驗，評估 TNFi 失敗後序貫治療策略（含第二個 TNFi vs 非 TNFi 生物製劑） |

---

## 文獻證據（炎性脊椎病 / 多關節型 JIA 精選）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33789011](https://pubmed.ncbi.nlm.nih.gov/33789011/) | 2021 | Phase 3 RCT | NEJM | Upadacitinib vs adalimumab 治療 PsA（炎性脊椎病亞型）：直接頭對頭比較 |
| [32386593](https://pubmed.ncbi.nlm.nih.gov/32386593/) | 2020 | Phase 3 RCT | Lancet | EXCEED 研究：Secukinumab vs adalimumab 作為 PsA 第一線生物製劑單藥療法 52 週比較 |
| [38556921](https://pubmed.ncbi.nlm.nih.gov/38556921/) | 2024 | Phase 3 RCT | Arthritis Rheumatol | SURPASS 研究：Secukinumab vs adalimumab 生物相似藥在放射學 axSpA 脊椎影像學進展比較 |
| [30499246](https://pubmed.ncbi.nlm.nih.gov/30499246/) | 2019 | Clinical Guideline | Arthritis Rheumatol | ACR/NPF 2018 PsA 治療指引，adalimumab 列為一線 bDMARD 推薦 |
| [31421019](https://pubmed.ncbi.nlm.nih.gov/31421019/) | 2020 | Observational | Arthritis Care Res | STRIVE 登記七年中期報告：adalimumab 在 polyJIA 的長期安全性與療效 |
| [18716298](https://pubmed.ncbi.nlm.nih.gov/18716298/) | 2008 | Phase 3 RCT | NEJM | Adalimumab ± methotrexate 在多關節型 JIA 的隨機雙盲安慰劑對照研究（FDA 批准基礎研究） |
| [40148850](https://pubmed.ncbi.nlm.nih.gov/40148850/) | 2025 | RCT/Meta-analysis | BMC Pediatrics | Etanercept vs adalimumab 在 polyJIA 療效與安全性比較 meta 分析 |
| [30054164](https://pubmed.ncbi.nlm.nih.gov/30054164/) | 2018 | Observational | J Pediatrics | 兒科 adalimumab 安全性整合分析：涵蓋 polyJIA、ERA、銀屑病及克隆氏病兒童 |
| [31969328](https://pubmed.ncbi.nlm.nih.gov/31969328/) | 2020 | Clinical Guideline | Ann Rheum Dis | EULAR 2019 RA 管理建議更新，涵蓋 bDMARD（含 adalimumab）使用原則 |
| [22772328](https://pubmed.ncbi.nlm.nih.gov/22772328/) | 2013 | Phase 3 RCT | Ann Rheum Dis | ABILITY-1 研究：adalimumab 在非放射學 axSpA（nr-axSpA）的隨機安慰劑對照試驗 |

---

## 香港上市資訊

Adalimumab 目前在香港**尚未正式上市**，衛生署藥物辦公室（Department of Health）現無登記許可證（共 0 張）。

全球方面，Adalimumab（原廠品牌 Humira®）已獲 US FDA 及 EMA 批准之適應症包括：類風濕性關節炎、多關節型幼年特發性關節炎（≥ 2 歲）、強直性脊椎炎、非放射學中軸型脊椎關節炎、銀屑病關節炎、克隆氏病、潰瘍性結腸炎、銀屑病、葡萄膜炎等。若欲在香港使用，需向衛生署申請個別藥物許可或特別授權。

---

## 安全性考量

Adalimumab 仿單安全性資料未包含於本 Evidence Pack（資料缺口 DG001）。安全性資訊請參考原廠仿單。

根據現有文獻，在考慮本批預測適應症時，以下安全性風險值得特別關注：

- **感染風險**：TNF-α 抑制劑顯著增加機會性感染風險，包括結核病再活化、侵入性真菌感染及細菌性敗血症。使用前需強制篩查潛伏性結核（TST 或 IGRA）。
- **藥物誘發性自身免疫**：有個案報告顯示 adalimumab 可誘發 ANCA 相關性血管炎、白血球碎裂性血管炎及藥物誘發性 SLE，此點在評估類風濕血管炎適應症時需格外謹慎。
- **免疫原性**：抗藥抗體（ADA）形成可導致藥物濃度下降及療效喪失，需考慮治療藥物濃度監測（TDM）。
- **心血管事件**：中度至重度心衰竭（NYHA III/IV 級）為禁忌，使用前需評估心臟功能。

---

## 結論與下一步

### 適應症一：類風濕血管炎（排名 1）

**決策：Research Question**

**理由：**
RV 為 RA 罕見且嚴重的並發症，目前無專屬 RCT 設計（證據主要來自系統性回顧及個案報告，L3 等級）。更需關注的是 adalimumab 本身可誘發血管炎樣不良事件，在 RV 患者中的獲益風險平衡尚未經過系統性評估。

**若要推進需要：**
- 針對 RV 亞型設計前瞻性觀察性研究或全球多中心登記研究
- 制訂鑑別「治療性療效」與「藥物誘發血管炎」的診斷標準
- 必須建立腎功能（包括 ANCA 定期監測）及血管炎活動度的安全性監測計畫

---

### 適應症三：炎性脊椎病（排名 3）

**決策：Proceed with Guardrails**

**理由：**
具備多個已完成 Phase 3 RCT 及大規模真實世界研究（L1 等級），EULAR/ACR 指引已將 adalimumab 列為 AS/axSpA 第一線 bDMARD。全球已獲批准，香港未上市屬法規缺口而非療效缺口。

**若要推進需要：**
- 向香港衛生署申請藥物登記許可（可參考 FDA/EMA 已批准資料包）
- 制訂結核病強制篩查及潛伏感染預防性治療方案
- 長期追蹤感染風險、心血管事件及治療藥物濃度

---

### 適應症五：多關節型幼年特發性關節炎（排名 5）

**決策：Proceed with Guardrails**

**理由：**
FDA 於 2008 年批准 adalimumab 用於 2 歲以上多關節型 JIA，且有長達 10 年的 STRIVE 登記安全性追蹤數據（L1 等級）。兒科劑量（4 mg/kg，最大 40 mg，每兩週皮下注射）及 PK/PD 資料完整，是本次預測中證據最充分且最具臨床推進可行性的適應症之一。

**若要推進需要：**
- 向香港衛生署申請兒科適應症許可證
- 制訂兒科體重分層劑量指引（含 < 15 kg 超低體重族群特別說明）
- 長期監測兒童生長發育、感染風險（包括 EBV 相關淋巴瘤）及免疫原性

---

> **免責聲明**：本報告僅供研究參考，不構成醫療建議。所有藥物再利用候選均需經過充分臨床驗證及法規核准，方可應用於實際患者治療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

