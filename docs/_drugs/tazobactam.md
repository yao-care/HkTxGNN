---
layout: default
title: Tazobactam
parent: 高證據等級 (L1-L2)
nav_order: 851
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-14
description: "Tazobactam：預測新適應症為肺炎 (Pneumonia)（證據等級 L1）。原適應症：細菌性肺炎、腹膜炎、闌尾炎、金黃色葡萄球菌感染"
---

# Tazobactam
{: .fs-9 }

證據等級: **L1** | 預測適應症: **2** 個
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

# Tazobactam：從細菌性肺炎到肺炎（含尿路感染延伸）

## 一句話總結

Tazobactam 是 β-內醯胺酶抑制劑，必須與 piperacillin、ceftolozane 等抗生素合併使用，原本用於細菌性肺炎、腹膜炎、闌尾炎及葡萄球菌感染。
TxGNN 模型預測它對**肺炎 (Pneumonia)** 有效，另預測可延伸至**尿路感染 (Urinary Tract Infection)**。
肺炎方面有 **20 個臨床試驗**和 **20 篇文獻**，尿路感染方面有 **5 個臨床試驗**和 **20 篇文獻**。
肺炎與原適應症高度重疊，屬於標示內或接近標示內的使用，並非全新的再利用方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性肺炎、腹膜炎、闌尾炎、金黃色葡萄球菌感染（香港許可證未登載適應症文字，此為模型知識圖譜資料） |
| 預測新適應症 | 肺炎 (Pneumonia)；次要預測：尿路感染 (Urinary Tract Infection) |
| TxGNN 預測分數 | 肺炎 99.46%；尿路感染 99.12% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張（皆為有效的單方許可證） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏經核實的詳細作用機轉資料。依據本報告整理的資料，tazobactam 是不可逆的 β-內醯胺酶抑制劑，能保護搭配的 β-內醯胺類抗生素（piperacillin、ceftolozane）不被細菌酵素水解，包括 ESBL（如 TEM、SHV、CTX-M）。本身沒有抗菌活性，因此所有臨床證據都是針對複方組合。

**肺炎：** 社區型、院內型和呼吸器相關肺炎的常見致病菌包含產 β-內醯胺酶的革蘭氏陰性菌。肺炎與原適應症「細菌性肺炎」幾乎相同，所以這項預測較屬於標示內或接近標示內的使用。

**尿路感染：** 這項屬於延伸適應症，不在原適應症清單內。引起複雜性尿路感染和腎盂腎炎的腸內菌常產 ESBL，而 piperacillin-tazobactam 經尿液排泄，尿中藥物濃度高，機轉上合理。但對 ESBL 菌株的療效仍有爭議，碳青黴烯類仍是 ESBL 菌血症的首選。

---

## 臨床試驗證據

### 肺炎（共 20 個登記，列出最相關者）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | 完成 | 726 | Ceftolozane/tazobactam 對比 meropenem，用於呼吸器相關院內肺炎，主要終點為第 28 天全因死亡率（非劣性） |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | 完成 | 537 | Imipenem/relebactam 對比 piperacillin/tazobactam，用於院內或呼吸器相關細菌性肺炎，主要終點為全因死亡率（非劣性） |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | 完成 | 460 | Levofloxacin 對比 piperacillin/tazobactam，用於輕中度院內肺炎的非劣性試驗 |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | 提前終止 | 4 | Ceftolozane/tazobactam 對比 piperacillin/tazobactam 用於呼吸器相關肺炎，僅收 4 人，無法評估療效 |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Phase 2 | 完成 | 80 | 重症加護適當抗生素治療的隨機先導試驗，tazobactam 的個別貢獻不明 |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | 完成 | 41 | Ceftolozane/tazobactam 用於兒童院內肺炎的安全性與藥動學 |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Phase 1 | 完成 | 37 | 重症患者使用 ceftolozane/tazobactam 的血漿藥動學與肺部穿透性 |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | 不適用 | 招募中 | 42 | 模型導引與經驗劑量的 piperacillin-tazobactam 比較，用於老年肺炎，尚無結果 |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | 不適用 | 尚未招募 | 100 | 嚴重社區型肺炎中，piperacillin/tazobactam 單用對比合併 fluoroquinolone |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | 不適用 | 完成 | 179 | 加護病房肺炎的個別化抗生素劑量方案 |

### 尿路感染（共 5 個登記）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03687255](https://clinicaltrials.gov/study/NCT03687255) | Phase 3 | 完成 | 1043 | Cefepime-enmetazobactam 對比 piperacillin/tazobactam，用於複雜性尿路感染及急性腎盂腎炎（piperacillin/tazobactam 為對照組） |
| [NCT02728089](https://clinicaltrials.gov/study/NCT02728089) | Phase 3 | 完成 | 115 | 日本人使用 ceftolozane/tazobactam 的開放性非對照試驗，用於腎盂腎炎和複雜性尿路感染 |
| [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) | Phase 2 | 完成 | 134 | 兒童複雜性尿路感染，ceftolozane/tazobactam 對比 meropenem |
| [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) | Phase 4 | 暫停 | 198 | Piperacillin/tazobactam 對比碳青黴烯類，用於產 ESBL 菌所致非菌血症尿路感染，尚無結果 |
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | 不適用 | 完成 | 3520 | 兒童標準治療下的藥動學研究，非尿路感染專屬 |

---

## 文獻證據

### 肺炎

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP：ceftolozane-tazobactam 對比 meropenem 用於院內肺炎的 Phase 3 非劣性試驗 |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2：imipenem/relebactam 對比 piperacillin/tazobactam 用於院內或呼吸器相關肺炎 |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Imipenem/relebactam 對比 piperacillin/tazobactam 的 Phase 3 非劣性試驗 |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | 系統性回顧與網絡統合分析 | Clin Microbiol Infect | 非呼吸器相關院內肺炎的經驗性抗生素方案比較 |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Review | Eur Respir Rev | 革蘭氏陰性菌肺炎的新抗生素概述 |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Review | Semin Respir Crit Care Med | 院內及呼吸器相關肺炎的新抗生素 |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Review | Crit Care | 加護病房院內肺炎治療更新 |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Review | Int J Antimicrob Agents | 新型 β-內醯胺類治療碳青黴烯抗藥菌肺炎的藥動學與藥效學系統性回顧 |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohort | Clin Infect Dis | 多重抗藥綠膿桿菌菌血症或肺炎：ceftolozane-tazobactam 的抗藥性產生率（10%）低於 ceftazidime-avibactam（40%） |
| [42129898](https://pubmed.ncbi.nlm.nih.gov/42129898/) | 2026 | 隨機藥動學試驗 | Crit Care | Ceftolozane/tazobactam 與 ceftazidime/avibactam 連續輸注的肺內穿透性比較 |

### 尿路感染

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36194218](https://pubmed.ncbi.nlm.nih.gov/36194218/) | 2022 | RCT | JAMA | Cefepime/enmetazobactam 對比 piperacillin/tazobactam，用於複雜性尿路感染或急性腎盂腎炎 |
| [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) | 2018 | RCT | JAMA | TANGO I：meropenem-vaborbactam 對比 piperacillin-tazobactam 用於複雜性尿路感染 |
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | RCT | Clin Infect Dis | ZEUS：fosfomycin 注射劑對比 piperacillin-tazobactam，Phase 2/3 |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | 統合分析 | J Comp Eff Res | 複雜性尿路感染治療選項的系統性回顧與網絡統合分析 |
| [40583996](https://pubmed.ncbi.nlm.nih.gov/40583996/) | 2025 | 系統性回顧 | JAC Antimicrob Resist | 新型 β-內醯胺/β-內醯胺酶抑制劑組合的療效、安全性與藥動學 |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | 新型抗生素治療多重抗藥革蘭氏陰性菌感染的臨床資料 |
| [29493397](https://pubmed.ncbi.nlm.nih.gov/29493397/) | 2018 | Review | Expert Rev Anti Infect Ther | Ceftolozane/tazobactam 的治療定位 |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clin Infect Dis | 抗生素腎功能劑量調整；ceftolozane/tazobactam 在肌酸酐清除率 30–50 mL/min 時有療效下降的警示 |

---

## 香港上市資訊

香港共有 14 張有效許可證，皆為單方，無已註銷者。資料中未登載劑型與核准適應症文字，以下列出主要 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58094 | TAZOCIN FOR INJ 4.5G（輝瑞） | 注射劑 | 未登載 |
| HK-49703 | TAZOCIN FOR INJ 4.5G（輝瑞） | 注射劑 | 未登載 |
| HK-65156 | ZERBAXA 1G/0.5G（默沙東，ceftolozane/tazobactam） | 輸注用濃縮液粉劑 | 未登載 |
| HK-65419 | PIPERACILLIN/TAZOBACTAM KABI 4G/0.5G（Fresenius Kabi） | 輸注用粉劑 | 未登載 |
| HK-64861 | PIPERACILLIN/TAZOBACTAM SANDOZ 4.5G（Sandoz） | 輸注用粉劑 | 未登載 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（僅供參考，並非仿單文字）：腎臟疾病、輸尿管積膿、嗜中性白血球低下、顆粒球缺乏症、凝血疾病、困難梭狀芽孢桿菌結腸炎、新生兒壞死性小腸結腸炎、傳染性單核球增多症、慢性 EB 病毒感染症候群。
- 文獻也提醒：ceftolozane/tazobactam 在基線肌酸酐清除率 30–50 mL/min 的患者，臨床反應可能下降，使用時須留意腎功能與劑量調整。

其他警語、禁忌症與藥物交互作用資料請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 肺炎方面有多個已完成的 Phase 3 RCT（含 ASPECT-NP 及以 piperacillin/tazobactam 為對照的試驗），證據達 L1。但這些試驗多以複方組合為研究對象，且肺炎本就接近原適應症，不屬全新再利用。
- 尿路感染為延伸適應症，有 Phase 3 試驗和多項 RCT 以 piperacillin/tazobactam 為對照，但對 ESBL 菌株的療效仍有爭議，碳青黴烯類仍是首選。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認各許可證的核准適應症、警語與禁忌症
- 補齊作用機轉的正式資料
- 釐清尿路感染（特別是 ESBL 菌株）的證據，等待 NCT03891433 等試驗結果
- 建立腎功能不全、嗜中性白血球低下、凝血異常等族群的使用與監測方案
- 依各產品的具體組合（piperacillin 或 ceftolozane）分別評估證據，不可直接推論到 tazobactam 單獨使用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

