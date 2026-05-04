---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin：從廣效細菌感染到喉炎及多重耳鼻喉感染

## 一句話總結

Ampicillin 是一種廣效性 β-lactam 抗生素，對多種革蘭氏陽性及陰性菌具殺菌活性，長期用於各類細菌性感染的治療。TxGNN 模型預測其最高分適應症為**喉炎 (Laryngitis)**（99.97%），同時對**慢性鼻竇炎**、**淋球菌尿道炎**、**細菌性關節炎**等 10 項適應症給出高度預測分數；其中喉炎有 **1 個臨床試驗**及 **20 篇文獻**支持，慢性鼻竇炎有 **9 個臨床試驗**及 **20 篇文獻**，為整體最強證據方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效細菌感染（香港未有許可證，原始記錄缺乏詳細核准適應症） |
| TxGNN 最高分預測 | 喉炎 (Laryngitis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4（喉炎）；**L2**（慢性鼻竇炎，最強） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold（喉炎）；**Proceed with Guardrails**（慢性鼻竇炎、細菌性關節炎）；Hold（Ureaplasma 尿道炎、副鼻竇腫瘤—機轉矛盾） |

---

## 為什麼這個預測合理？

Ampicillin 屬廣效性氨苄青黴素，其作用機轉為與青黴素結合蛋白（PBPs）共價結合，抑制細菌細胞壁肽聚糖的交叉連接，導致細胞壁缺損與細菌裂解死亡。由於需要完整的細菌肽聚糖作為靶點，ampicillin 對缺乏細胞壁的微生物（如 Mycoplasma、Ureaplasma）先天無效。

TxGNN 模型預測 ampicillin 可用於喉炎，機轉上具有一定合理性——細菌性喉炎（如 *H. influenzae*、β-溶血性鏈球菌所致）的致病菌多屬 ampicillin 敏感菌。然而，喉炎 80–90% 為病毒性病因，細菌性病例僅佔少數，且現有臨床試驗均使用 amoxicillin/clavulanate 複方，而非單用 ampicillin。

在 10 項預測適應症中，**慢性鼻竇炎（Rank 4）**具最佳臨床證據（L2），ampicillin 及其衍生物（amoxicillin、amoxicillin-clavulanate）對 CRS 常見致病菌（*S. pneumoniae*、*H. influenzae* MSSA 菌株）有效，且有多個 Phase 4 RCT 支持。**細菌性關節炎（Rank 8）**亦有 Phase 4 RCT 與 2023 年兒科傳染病指引支持，屬另一具臨床價值方向。需排除 Ureaplasma 尿道炎與副鼻竇腫瘤，前者為機轉矛盾假陽性，後者為抗生素無法治療的腫瘤性疾病。

---

## 十大預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 | 備註 |
|-----|--------|-----------|---------|---------|------|
| 1 | 喉炎 (Laryngitis) | 99.97% | L4 | Research Question | 80-90% 為病毒性，細菌性僅少數；現有試驗非直接 ampicillin |
| 2 | Ureaplasma 尿道炎 | 99.36% | L5 | **Hold** | ⚠️ 機轉矛盾：缺乏細胞壁，β-lactam 先天耐藥 |
| 3 | 淋球菌尿道炎 | 99.36% | L3 | Hold | 歷史有效，現行 PPNG 耐藥率 >30–50%，非 WHO/CDC 建議選項 |
| 4 | **慢性鼻竇炎** | 99.34% | **L2** | **Proceed with Guardrails** | 最強證據，多個 Phase 4 RCT；ampicillin 有直接菌學研究 |
| 5 | 慢性篩竇炎 | 99.33% | L3 | Research Question | CRS 解剖亞型；有直接 ampicillin 術前使用文獻 |
| 6 | 牙齦炎 | 99.28% | L3 | Research Question | β-lactamase 陽性比例高，需搭配酶抑制劑 |
| 7 | 副鼻竇腫瘤 | 99.20% | L5 | **Hold** | ⚠️ 機轉矛盾：抗生素對腫瘤細胞無抗增殖活性 |
| 8 | **細菌性關節炎** | 99.11% | **L3** | **Proceed with Guardrails** | 有兒科骨關節感染 Phase 4 RCT（n=180）及 2023 指引支持 |
| 9 | 結膜炎 | 99.04% | L4 | Research Question | 系統給藥非眼表感染標準途徑；無直接 ampicillin 滴眼 RCT |
| 10 | 冠周炎 | 99.04% | L4 | Hold | β-lactamase 產酶菌盛行率 >30%；純 ampicillin 覆蓋不足 |

---

## 臨床試驗證據

### 喉炎（Rank 1）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A（上市後） | 完成 | 363 | CLAVAMOX®（amoxicillin/clavulanate）日本兒科感染含喉炎的上市後安全性及療效調查；藥物為 ampicillin 衍生物複方，非直接 ampicillin |

### 慢性鼻竇炎（Rank 4，最佳證據）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01825408](https://clinicaltrials.gov/study/NCT01825408) | Phase 4 | 完成 | 40 | 比較 3 週與 6 週抗生素療程作為 CRS 最大醫療治療一部分的效果差異 |
| [NCT01919411](https://clinicaltrials.gov/study/NCT01919411) | Phase 4 | 完成 | 134 | 鼻竇內視鏡手術後預防性抗生素 vs. 安慰劑的術後感染率與生活品質比較 |
| [NCT03809312](https://clinicaltrials.gov/study/NCT03809312) | Phase 4 | 未知 | 134 | 功能性鼻竇手術中預防性抗生素使用隨機雙盲臨床試驗（含有/無鼻息肉） |
| [NCT00335309](https://clinicaltrials.gov/study/NCT00335309) | N/A | 完成 | 50 | 系統性抗生素合併上頜竇鹽水沖洗 vs. 單純抗生素治療 CRS 的前瞻性 RCT |
| [NCT02712502](https://clinicaltrials.gov/study/NCT02712502) | N/A | 完成 | 100 | Levofloxacin vs. Amoxicillin-clavulanate 治療急性細菌性鼻竇炎療效與安全性比較 |
| [NCT00377403](https://clinicaltrials.gov/study/NCT00377403) | Phase 4 | 完成 | 172 | Amoxicillin（ampicillin 衍生物）vs. 安慰劑治療急性鼻竇炎的 Phase 4 指引評估研究 |
| [NCT03369717](https://clinicaltrials.gov/study/NCT03369717) | Phase 4 | 提早終止 | 24 | 鼻竇手術後抗生素使用的多機構前瞻性研究；因入組不足提早終止 |

### 細菌性關節炎（Rank 8）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04563325](https://clinicaltrials.gov/study/NCT04563325) | Phase 4 | 完成 | 180 | ⭐ 全國性多中心 RCT：兒童骨關節感染純口服抗生素是否不劣於靜脈後序貫口服療法，β-lactam 類為主要治療藥物 |

---

## 文獻證據

### 喉炎（Rank 1）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | 指引品質評估 | CoDAS | AGREE II 評估喉炎與咽炎臨床指引方法學品質，為管理標準提供依據 |
| [8651625](https://pubmed.ncbi.nlm.nih.gov/8651625/) | 1996 | 回顧性研究 | Ann Otol Rhinol Laryngol | 鼻硬化症喉氣管表現，早期病例以口服四環素有效；嚴重病例需手術 |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | 個案報告+文獻回顧 | Ann Otol Rhinol Laryngol | 現代抗生素時代自發性喉部膿腫：免疫抑制患者為高風險族群，抗生素治療為基礎 |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | 個案報告 | Auris Nasus Larynx | 骨髓移植後喉部放線菌症，延長 penicillin 類抗生素療程後完全緩解 |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | 回顧性世代 | Otolaryngol Head Neck Surg | 喉切除術圍術期抗生素選擇（含 ampicillin 類）與手術部位感染及傷口裂開的關聯性分析 |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | 病例系列 | Anaesth Intensive Care | 161 例兒童急性會厭炎（含 5 例死亡）管理，氣道管理與抗生素治療為核心策略 |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | 病例系列 | Acta Otorrinolaringol Esp | 2 例聲門旁喉部膿腫，需快速診斷與治療以避免氣道威脅 |

### 慢性鼻竇炎（Rank 4，最佳證據）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31838920](https://pubmed.ncbi.nlm.nih.gov/31838920/) | 2021 | RCT 10年追蹤 | Ear Nose Throat J | 10 年追蹤比較 CRSsNP 兩種長期醫療策略的疾病控制率及 GERD 在治療抗性中的角色 |
| [27610609](https://pubmed.ncbi.nlm.nih.gov/27610609/) | 2017 | RCT | Int Forum Allergy Rhinol | Amoxicillin-clavulanate（ampicillin 衍生物+酶抑制劑）治療 CRS 急性惡化的雙盲安慰劑對照試驗 |
| [9438060](https://pubmed.ncbi.nlm.nih.gov/9438060/) | 1997 | 臨床研究 | Am J Rhinol | **直接** ampicillin（500mg q6h，2 週）術前使用於 74 例 CRS 患者的細菌學研究，上頜竇與篩竇培養率約 46% |
| [29959565](https://pubmed.ncbi.nlm.nih.gov/29959565/) | 2018 | 臨床研究 | Eur Arch ORL | Amoxicillin-clavulanic acid 與 levofloxacin 對 CRSwNP 鼻竇組織細菌生物膜的體外抑制效果比較 |
| [11685965](https://pubmed.ncbi.nlm.nih.gov/11685965/) | 2001 | 藥物動力學 | Acta ORL Belgica | Amoxicillin/clavulanate 於 CRS 患者鼻竇組織與血清的藥物分布分析 |
| [20015730](https://pubmed.ncbi.nlm.nih.gov/20015730/) | 2010 | 回顧性世代 | Am J Otolaryngol | 兒童 CRS 6 年上頜竇穿刺培養細菌學與抗藥性分析，評估當前致病菌對 ampicillin 類敏感性 |
| [10209612](https://pubmed.ncbi.nlm.nih.gov/10209612/) | 1998 | 細菌學研究 | J Laryngol Otol | 533 例 CRS 患者膿性分泌物細菌學研究，定義主要致病菌種類與分布 |
| [11391261](https://pubmed.ncbi.nlm.nih.gov/11391261/) | 2001 | 臨床研究 | Otolaryngol Head Neck Surg | Amoxicillin-clavulanate 術前治療後 CRS 細菌學研究（90 例研究組 vs. 113 例對照組） |
| [41054784](https://pubmed.ncbi.nlm.nih.gov/41054784/) | 2025 | 綜述 | Minerva Medica | Amoxicillin/clavulanate 作為 WHO AWaRe Access 類抗生素的抗菌管理建議綜述 |
| [7805431](https://pubmed.ncbi.nlm.nih.gov/7805431/) | 1994 | RCT | Chemotherapy | 251 例成人慢性鼻竇炎雙盲多中心比較：ciprofloxacin vs. amoxycillin/clavulanic acid（主要致病菌含 S. aureus、H. influenzae） |

### 細菌性關節炎（Rank 8）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37741341](https://pubmed.ncbi.nlm.nih.gov/37741341/) | 2023 | 臨床指引 | Infect Dis Now | 兒科傳染病學組 2023 年骨關節感染抗生素治療指引，明確建議 β-lactam 類（含 ampicillin 衍生物）為兒童 S. aureus MSSA 及 Streptococcus 感染首選 |
| [27976670](https://pubmed.ncbi.nlm.nih.gov/27976670/) | 2016 | 綜述 | Nat Rev Dis Primers | 萊姆病（Borrelia 關節炎）完整綜述，penicillin 類抗生素（含 ampicillin）為一線治療 |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | 臨床研究 | Rev Infect Dis | 9 例兒童骨髓炎/感染性關節炎靜脈 sulbactam/ampicillin 序貫口服 sultamicillin 的療效與安全性評估 |
| [12787521](https://pubmed.ncbi.nlm.nih.gov/12787521/) | 2003 | 綜述 | Best Pract Clin Rheumatol | 淋球菌性關節炎（最常見急性感染性關節炎之一）臨床特徵與 penicillin 類抗生素治療策略 |
| [7899877](https://pubmed.ncbi.nlm.nih.gov/7899877/) | 1994 | 回顧性研究 | Semin Arthritis Rheum | 鐮刀型紅血球病 Salmonella 骨關節感染：ampicillin 為特定菌種治療選項之一 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **補充說明**：根據 Ampicillin（DrugBank DB00415）的已知臨床知識，需特別注意：
> - 青黴素過敏患者禁用（包括嚴重過敏反應、史蒂文斯–強生症候群）
> - 感染性單核球增多症（EBV 感染）患者使用 ampicillin/amoxicillin 易出現全身性皮疹，需謹慎
> - 腎功能不全患者需調整劑量
> 詳細藥物警語、禁忌及藥物交互作用，請查閱原廠仿單及 DrugBank DB00415 資料庫

---

## 結論與下一步

### 最高分預測：喉炎（Rank 1）

**決策：Hold（偏向 Research Question）**

**理由：**
喉炎 80–90% 為病毒性，細菌性喉炎僅佔少數案例；現有唯一臨床試驗使用的是 amoxicillin/clavulanate 複方（非單一 ampicillin），且為兒科廣效感染的上市後調查，缺乏直接針對喉炎的 ampicillin RCT。L4 證據等級不足以支持直接推進，但細菌性喉炎的機轉合理性值得進一步研究。

**若要推進需要：**
- 設計細菌性喉炎（經培養確認）的 ampicillin 前瞻性觀察研究
- 釐清抗菌譜覆蓋率（尤其是 β-lactamase 陽性菌株的比例）

---

### 最具臨床價值預測：慢性鼻竇炎（Rank 4）

**決策：Proceed with Guardrails**

**理由：**
Ampicillin 及其衍生物在 CRS 有多個 Phase 4 RCT 支持（L2 等級），且 PMID 9438060 提供直接 ampicillin 術前使用的菌學依據，藥理外推合理。主要限制在於部分致病菌（尤其是 β-lactamase 陽性 *S. aureus*、*H. influenzae*）對純 ampicillin 耐藥，臨床上更常考慮搭配 sulbactam 或選用 amoxicillin-clavulanate。

**若要推進需要：**
- 補充 TFDA 仿單警語與禁忌症（目前為資料缺口 DG001）
- 取得 DrugBank 詳細作用機轉資料（DG002）
- 確認香港未上市原因，評估法規路徑
- 釐清是否需要搭配 β-lactamase 抑制劑以提升臨床效果
- 建立特定族群（兒童、腎功能不全患者）的安全性監測計畫

---

### 細菌性關節炎（Rank 8）

**決策：Proceed with Guardrails**

**理由：**
有全國性 Phase 4 RCT（NCT04563325，n=180）支持兒童骨關節感染口服 β-lactam 療法，2023 年兒科傳染病指引（PMID 37741341）亦有明確建議。需注意，感染性關節炎常需積極靜脈給藥期，純口服 ampicillin 的定位應在序貫治療降階段。

---

### 建議排除的假陽性預測

| 適應症 | 排除理由 |
|--------|---------|
| Ureaplasma 尿道炎（Rank 2） | 機轉矛盾：Ureaplasma 缺乏細胞壁，對所有 β-lactam 先天性耐藥，TxGNN 高分為假陽性 |
| 副鼻竇腫瘤（Rank 7） | 機轉矛盾：ampicillin 為抗菌藥物，無任何直接抗腫瘤機轉，文獻涉及的是腫瘤合併細菌感染情境 |

---

> **免責聲明**：本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過嚴謹臨床驗證方可應用於臨床。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

