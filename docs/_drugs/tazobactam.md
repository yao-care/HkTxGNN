---
layout: default
title: Tazobactam
parent: 僅模型預測 (L5)
nav_order: 722
evidence_level: L5
indication_count: 2
---

# Tazobactam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Tazobactam：從「無獨立適應症」到肺炎、泌尿道感染複方佐劑角色

## 一句話總結

Tazobactam 本身不是可單獨使用的藥物——它是 β-lactamase 抑制劑，必須與 piperacillin 或 ceftolozane 等 β-lactam 類抗生素組成固定劑量複方使用。TxGNN 模型預測它對**肺炎 (Pneumonia)** 和**泌尿道感染 (Urinary Tract Infection)** 有效，目前分別有 **50 個臨床試驗 / 20 篇文獻**（肺炎）與 **13 個臨床試驗 / 18 篇文獻**（泌尿道感染）支持。

> ⚠️ **重要提醒**：根據證據包內的機轉分析，這兩個預測並非 TxGNN 發現的全新老藥新用機轉，而是重新確認了 piperacillin-tazobactam、ceftolozane-tazobactam 等複方藥物**既有的核准適應症**（HAP/VAP、cUTI 含腎盂腎炎）。屬於確效性證據彙整，非新穎候選。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無獨立適應症（僅作為 β-lactamase 抑制劑，須與 β-lactam 類藥物組成複方使用） |
| 預測新適應症（第一名） | 肺炎 (Pneumonia) |
| 預測新適應症（第二名） | 泌尿道感染 (Urinary Tract Infection) |
| TxGNN 預測分數 | 99.46%（肺炎）／99.12%（泌尿道感染） |
| 證據等級 | L1（兩者皆為 L1，具多個 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 DrugBank 未提供 Tazobactam 詳細的作用機轉描述（資料缺口）。根據公開藥理學共識，Tazobactam 是不可逆的 β-lactamase 抑制劑，本身幾乎沒有抗菌活性；必須與 β-lactam 類抗生素（如 piperacillin、ceftolozane）組成固定劑量複方，藉由抑制細菌產生的 β-lactamase（包括 ESBL），保護 β-lactam 藥物不被分解，進而恢復或增強其抗菌效力。

Tazobactam 沒有「原適應症」——它從未以單方形式獲得核准，而是作為 piperacillin-tazobactam、ceftolozane-tazobactam 等複方的組成成分。這兩個複方藥物在國際間早已核准用於醫院內肺炎（HAP）、呼吸器相關肺炎（VAP）及複雜性泌尿道感染（cUTI，含腎盂腎炎）。因此，TxGNN 預測 Tazobactam 對肺炎與泌尿道感染「有效」，實際上是模型重新發現了這兩個複方藥物既有的核准適應症，而非揭露全新的作用路徑。

這樣的結果雖非新穎老藥新用，但對於評估 Tazobactam（或其複方）在香港市場的定位仍有參考價值，尤其是在多重抗藥性（MDR）革蘭氏陰性菌感染日益嚴峻的背景下。

---

## 適應症一：肺炎 (Pneumonia)

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | 完成 | 726 | ASPECT-NP：ceftolozane/tazobactam 對比 meropenem 治療呼吸器相關院內肺炎，樞紐試驗 |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | 完成 | 537 | imipenem/relebactam 對比 piperacillin/tazobactam 治療 HABP/VABP |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | 完成 | 274 | 多國研究：IMI/REL 對比 PIP/TAZ 治療 HABP/VABP 非劣效性 |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | 完成 | 460 | Levofloxacin 對比 piperacillin/tazobactam 治療輕中度院內肺炎 |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | 招募中 | 20000 | REMAP-CAP：社區型肺炎多因子平台試驗，涵蓋多種抗生素 domain |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | 招募中 | 80 | 比較 ceftolozane-tazobactam 短輸注 vs 延長輸注治療 VAP |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | 完成 | 41 | 兒科族群 ceftolozane/tazobactam 之 PK/安全性研究（院內肺炎） |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Phase 2 | 完成 | 80 | 重症照護適當抗微生物治療前導試驗 |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | 招募中 | 42 | 老年肺炎患者 piperacillin-tazobactam 模型導引劑量優化研究 |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | 未知 | 50 | 院內肺炎（高 MIC 菌株）piperacillin/tazobactam 延長輸注 vs 常規輸注 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP：ceftolozane-tazobactam 對比 meropenem 治療院內肺炎，非劣效性確立 |
| [30208454](https://pubmed.ncbi.nlm.nih.gov/30208454/) | 2018 | RCT | JAMA | piperacillin-tazobactam 對比 meropenem 治療 ceftriaxone 抗藥菌血流感染之 30 天死亡率 |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2：imipenem/cilastatin/relebactam 對比 PIP/TAZ 治療 HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | IMI/REL 對比 PIP/TAZ 治療 HABP/VABP 之三期非劣效性試驗 |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohort | Clin Infect Dis | 比較 ceftazidime-avibactam 與 ceftolozane-tazobactam 治療後之抗藥性發生率 |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | Cohort | Lancet Infect Dis | CACTUS：ceftazidime-avibactam 對比 ceftolozane-tazobactam 於 MDR 綠膿桿菌感染之真實世界比較 |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Review | Int J Antimicrob Agents | 新型 β-lactam/β-lactamase 抑制劑複方於碳青黴烯抗藥革蘭氏陰性菌肺炎之 PK/PD 系統性回顧 |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Ceftolozane-tazobactam 治療院內肺炎之綜述 |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Review | Clin Microbiol Infect | 非呼吸器相關院內肺炎經驗性抗生素療法之網絡統合分析 |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Rev Esp Quimioter | Ceftolozane-tazobactam 於院內肺炎之應用綜述 |

---

## 適應症二：泌尿道感染 (Urinary Tract Infection)

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03687255](https://clinicaltrials.gov/study/NCT03687255) | Phase 3 | 完成 | 1043 | Cefepime-AAI101 對比 piperacillin/tazobactam 治療複雜性 UTI（含急性腎盂腎炎），最大規模試驗 |
| [NCT02728089](https://clinicaltrials.gov/study/NCT02728089) | Phase 3 | 完成 | 115 | 日本多中心研究：ceftolozane/tazobactam 治療複雜性 UTI 與腎盂腎炎之療效安全性 |
| [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) | Phase 2 | 完成 | 134 | Ceftolozane/tazobactam 對比 meropenem 治療兒科複雜性 UTI（含腎盂腎炎） |
| [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) | Phase 4 | 招募中止 | 198 | CAPITIS：piperacillin/tazobactam 對比 carbapenems 治療 ESBL 菌株非菌血症性 UTI |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) | 2018 | RCT | JAMA | TANGO I：meropenem-vaborbactam 對比 piperacillin-tazobactam 治療複雜性 UTI |
| [36194218](https://pubmed.ncbi.nlm.nih.gov/36194218/) | 2022 | RCT | JAMA | Cefepime/enmetazobactam 對比 piperacillin/tazobactam 治療複雜性 UTI 或急性腎盂腎炎 |
| [28592240](https://pubmed.ncbi.nlm.nih.gov/28592240/) | 2017 | RCT | BMC Infect Dis | Piperacillin-tazobactam、cefepime、ertapenem 治療 ESBL 大腸桿菌 UTI 之隨機對照試驗 |
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | RCT | Clin Infect Dis | ZEUS：Fosfomycin 注射劑對比 piperacillin-tazobactam 治療複雜性 UTI/急性腎盂腎炎 |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Review | J Comp Eff Res | 複雜性 UTI/急性腎盂腎炎治療選項之系統性回顧與網絡統合分析 |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | 治療 MDR 革蘭氏陰性菌感染新型抗生素之臨床數據綜述 |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Review | Int J Antimicrob Agents | 義大利/法國感染科學會 MDR 革蘭氏陰性桿菌感染治療實務指引 |
| [40007489](https://pubmed.ncbi.nlm.nih.gov/40007489/) | 2025 | — | Future Microbiol | Cefepime-enmetazobactam：首個核准用於 MDR 腸桿菌科之 cefepime-β-lactamase 抑制劑複方 |
| [36689671](https://pubmed.ncbi.nlm.nih.gov/36689671/) | 2023 | RCT | Pediatr Infect Dis J | Ceftolozane/tazobactam 對比 meropenem 治療新生兒與兒童複雜性 UTI（含腎盂腎炎） |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clin Infect Dis | 抗生素腎功能劑量調整之討論，含 ceftolozane/tazobactam 於 CrCl 30-50 mL/min 之療效疑慮 |

---

## 香港上市資訊

Tazobactam 目前**未在香港上市**，無許可證登記。

---

## 安全性考量

安全性資訊請參考原廠仿單。（藥物交互作用查詢無結果；主要警語與禁忌症目前缺乏資料，屬阻斷性資料缺口，需優先補齊才能進入安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 兩個預測適應症（肺炎、泌尿道感染）皆達 L1 證據等級，有多個已完成的 Phase 3 RCT 支持，但這些證據本質上是**複方藥物（piperacillin-tazobactam、ceftolozane-tazobactam）既有核准適應症的再確認**，而非 TxGNN 發現的新穎老藥新用機轉。
- Tazobactam 目前未在香港上市，且缺乏 MOA 與仿單安全性資料（阻斷性缺口），無法完成完整的安全性初評（S1）。

**若要推進需要：**
- 取得 Tazobactam（或其常見複方 piperacillin-tazobactam、ceftolozane-tazobactam）之官方藥品仿單，補齊警語、禁忌症與藥物交互作用資料
- 補充 DrugBank 或其他來源之詳細作用機轉（MOA）資料
- 確認香港是否已有相關複方藥物（piperacillin-tazobactam 等）以其他品名核准上市，避免與既有藥品重複評估
- 釐清此候選案是否應重新分類為「確效證據彙整」而非「老藥新用候選」，以免誤導決策流程
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

