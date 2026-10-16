---
layout: default
title: Ceftriaxone
parent: 高證據等級 (L1-L2)
nav_order: 176
evidence_level: L2
indication_count: 7
last_modified_at: 2026-10-14
description: "Ceftriaxone：預測新適應症為感染性中耳炎 (Infectious Otitis Media)（證據等級 L2）。原適應症：鏈球菌感染、細菌性肺炎、細菌性腦膜炎、淋病等"
monitor_inn: "CEFTRIAXONE"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **7** 個
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

# Ceftriaxone：從細菌感染到感染性中耳炎

## 一句話總結

Ceftriaxone 是第三代頭孢菌素類抗生素，原本用於鏈球菌感染、細菌性肺炎、細菌性腦膜炎、淋病等多種細菌感染。
TxGNN 模型預測它可能對**感染性中耳炎 (Infectious Otitis Media)** 有效，
目前有 **1 個臨床試驗**（但未直接測試 ceftriaxone）和 **18 篇文獻**支持這個方向，其中包含 1 篇隨機對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鏈球菌感染、細菌性肺炎、細菌性腦膜炎、淋病等（香港許可證未提供核准適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 感染性中耳炎 (Infectious Otitis Media) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：本報告以排名第 4 的「感染性中耳炎」為主要評估對象，因為它是目前證據最完整的預測適應症。排名第 1 至 3 名（高澱粉酶血症、多株性高黏滯症候群、先天性無白蛋白血症）以及第 5 名（血型不相容）缺乏合理機轉與臨床證據，詳見文末附註。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ceftriaxone 是第三代頭孢菌素，對中耳炎的主要致病菌（肺炎鏈球菌、流感嗜血桿菌、卡他莫拉菌）具有抗菌活性。

原適應症本身就是呼吸道與腦膜等細菌感染，而中耳炎同樣屬於細菌感染，病原體與原適應症高度重疊。因此這個預測與其說是全新用途，不如說更接近既有適應症的延伸。實務上，對無法口服用藥的兒童，常使用單次肌肉注射 ceftriaxone，並有與 trimethoprim-sulfamethoxazole 比較的隨機對照試驗支持（PMID 8989332）。

使用上需留意抗藥性與抗生素管理：宜保留給口服治療失敗或無法耐受的情況。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | NA | 完成 | 250 | 評估鼓膜置管對復發性急性中耳炎兒童的效果；並未測試 ceftriaxone，僅提供疾病背景 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | Pediatrics | 單次肌肉注射 ceftriaxone 與 10 天口服 TMP-SMZ 治療急性中耳炎的療效比較 |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | 共識指引 | Clinical Pediatrics | 急性中耳炎處置的共識建議 |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | 世代研究 | Int J Pediatr Otorhinolaryngol | 美國基層醫療中 ceftriaxone 用於急性中耳炎的相關因素，使用增加可能反映抗藥性問題 |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | Clinical Therapeutics | 整合急性中耳炎抗生素治療建議 |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Review | JAMA Network Open | 兒童門診抗生素處方的適當性 |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | Otol Neurotol | 人工耳蝸兒童中耳炎與腦膜炎的預防與治療 |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | 臨床研究 | Pediatr Infect Dis J | 1 天與 3 天肌肉注射 ceftriaxone 治療無反應性急性中耳炎的細菌學與臨床療效比較 |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | 臨床研究 | Pediatr Infect Dis J | 3 天肌肉注射 ceftriaxone 對無反應性急性中耳炎的細菌學療效 |
| [6301365](https://pubmed.ncbi.nlm.nih.gov/6301365/) | 1983 | 臨床研究 | Antimicrob Agents Chemother | 50 位成人嚴重細菌感染使用 ceftriaxone，多數感染有良好反應 |
| [33172868](https://pubmed.ncbi.nlm.nih.gov/33172868/) | 2022 | Case report | Arch Dis Child Educ Pract Ed | 2 歲兒童耳漏合併耳後腫脹，使用靜脈注射 ceftriaxone |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52844 | ROCEPHIN POWDER & SOLVENT FOR INJ 250MG IV | 注射劑 | 未提供 |
| HK-20195 | ROCEPHIN FOR INJ 2G STERILE PDR FOR INF | 注射劑 | 未提供 |
| HK-20190 | ROCEPHIN FOR INJ 1G IV STERILE POWDER | 注射劑 | 未提供 |
| HK-20192 | ROCEPHIN FOR INJ 1G IM STERILE POWDER | 注射劑 | 未提供 |
| HK-20188 | ROCEPHIN FOR INJ 500MG IV STERILE POWDER | 注射劑 | 未提供 |

香港共有 20 張有效單方許可證，上表僅列出 5 張主要許可證（原廠 ROCEPHIN 系列）。

## 安全性考量

- **知識圖譜標示之禁忌疾病**：肝臟疾病、膽囊疾病、新生兒黃疸、困難梭菌結腸炎、周產期壞死性腸炎、溶血性貧血。
- **藥物交互作用**：共查得 100 筆，主要包括：
  - **嚴重 (Major)**：氯化鈣、葡庚糖酸鈣、葡萄糖酸鈣（含鈣製劑與 ceftriaxone 併用有沉澱風險，尤其在新生兒）
  - **中度 (Moderate)**：Kanamycin、Neomycin、Streptomycin（胺基糖苷類）、Picosulfuric acid

其他警語與禁忌的仿單資料目前缺乏，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 感染性中耳炎的病原體在 ceftriaxone 抗菌譜內，且有 1 篇 RCT 與多篇臨床研究、指引支持其使用，生物學合理性強。但已登記的臨床試驗並未測試 ceftriaxone，因此證據等級定為 L2 而非更高。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌，確認中耳炎是否已在標示範圍內
- 補充作用機轉資料
- 限定使用情境（口服治療失敗或無法耐受的兒童），並配合抗生素管理與當地抗藥性資料
- 避免與含鈣製劑併用，並留意肝膽疾病與新生兒黃疸族群

## 附註：其他預測適應症的評估

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|-----------|-----------|---------|------|------|
| 高澱粉酶血症 | 99.39% | L4 | Hold | 無明確機轉；ceftriaxone 可引起膽泥與假性膽石，反而可能升高胰酶 |
| 多株性高黏滯症候群 | 99.39% | L5 | Hold | 無合理機轉，無試驗與文獻 |
| 先天性無白蛋白血症 | 99.37% | L5 | Hold | 無治療機轉；僅涉及藥動學（高蛋白結合率） |
| 化膿性中耳炎 | 99.02% | L3 | 研究問題 | 有 1989 年臨床研究支持急性期；慢性期病原體（如綠膿桿菌、生物膜）不利 |
| 慢性中耳炎 | 99.01% | L3 | 研究問題 | 僅有舊研究涵蓋急性惡化，其餘多為微生物調查；需限定亞群 |
| 血型不相容 | 99.12% | L5 | Hold | 無治療機轉；溶血性貧血與膽假性膽石屬不良反應 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

