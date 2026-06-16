---
layout: default
title: Glycyrrhizic Acid
parent: 中證據等級 (L3-L4)
nav_order: 357
evidence_level: L3
indication_count: 10
---

# Glycyrrhizic Acid
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Glycyrrhizic acid：從傳統抗炎成分到類風濕性關節炎

## 一句話總結

Glycyrrhizic acid（甘草酸）是甘草根的主要活性三萜皂苷，在傳統醫學中廣泛用於抗炎、抗病毒及肝臟保護，目前香港無正式核准藥品登記。TxGNN 模型針對甘草酸共預測了 **10 個潛在新適應症**，其中**類風濕性關節炎（Rheumatoid Arthritis）**的臨床轉化可行性最高，目前有 **1 個臨床試驗**和 **20 篇文獻**支持，建議評級為 **Proceed with Guardrails**；肺動脈高壓（L4）、巨細胞病毒感染與痤瘡（均 L3）亦有初步前臨床/臨床信號，值得追蹤。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式核准適應症（傳統草藥活性成分） |
| 最佳預測適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 97.82%（TxGNN 排名第 30,159） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 所有預測適應症概覽

| 排名 | 疾病 | TxGNN 分數 | 臨床試驗 | 文獻 | 證據等級 | 建議 |
|------|------|-----------|---------|------|---------|------|
| 1 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) | 99.28% | 0 | 0 | L5 | Hold |
| 2 | 閉經 (Amenorrhea) | 98.87% | 0 | 0 | L5 | Hold |
| 3 | 低高密度脂蛋白血症 (Hypoalphalipoproteinemia) | 98.48% | 0 | 0 | L5 | Hold |
| 4 | 惡性卡他熱 (Malignant Catarrh) ⚠️ 獸醫疾病 | 98.39% | 0 | 0 | L5 | Hold |
| 5 | 牛傳染性鼻氣管炎 (Infectious Bovine Rhinotracheitis) ⚠️ 獸醫疾病 | 98.39% | 0 | 0 | L5 | Hold |
| 6 | 巨細胞病毒感染 (CMV Infection) | 98.24% | 0 | 5 | L3 | Research Question |
| 7 | 痤瘡 (Acne) | 98.18% | 0 | 3 | L3 | Research Question |
| 8 | 脊柱後側彎性心臟病 (Kyphoscoliotic Heart Disease) | 97.96% | 0 | 0 | L5 | Hold |
| 9 | 肺動脈高壓 (Pulmonary Hypertension) | 97.91% | 0 | 7 | L4 | Research Question |
| **10** | **類風濕性關節炎 (Rheumatoid Arthritis)** | **97.82%** | **1** | **20** | **L3** | **Proceed with Guardrails** |

> 排名 4、5 為純獸醫疾病，無人類適應症轉化價值，後續分析不納入。

---

## 為什麼這個預測合理？

目前缺乏甘草酸的正式作用機轉（MOA）資料。根據現有文獻，Glycyrrhizic acid 是甘草根（Glycyrrhiza glabra/uralensis）提取的五環三萜皂苷，其代謝物 18β-甘草次酸（glycyrrhetinic acid, GA）同具高度生物活性。甘草酸已知的藥理特性包括：NF-κB 抑制、HMGB1 拮抗、11β-HSD 酶抑制（影響皮質醇代謝）、抗病毒膜融合，以及廣泛的抗炎免疫調節作用。

**針對類風濕性關節炎的機轉關聯性**：RA 是以慢性滑膜炎症與軟骨骨質破壞為特徵的自體免疫疾病。甘草酸透過以下多重路徑干預 RA 病理：(1) **NF-κB 抑制**，降低 TNF-α、IL-1β、IL-6 等促炎細胞激素；(2) **JAK/STAT 路徑拮抗**，機轉與 tofacitinib 等已核准 JAK 抑制劑類似；(3) **HMGB1 抑制**，減少滑膜炎症驅動因子；(4) **COX-2/TxA2 路徑調節**及 Th17/Treg 免疫平衡。

甘草酸同時作為藥物遞送載體（自組裝兩親性奈米結構），已被用於增強 sinomenine、芒果苷、薑黃素等抗 RA 藥物的生物利用度，顯示其在 RA 組合療法中的獨特潛力。傳統中醫方劑「芍藥甘草附子湯」數千年用於關節痹症的歷史，亦為其臨床應用提供了安全性背景。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05788705](https://clinicaltrials.gov/study/NCT05788705) | Phase NA | 不明 | 75 | 評估天然 JAK/STAT 路徑抑制劑（含甘草酸相關成分）輔助治療 RA；2023 年 7 月啟動，預計 2025 年 12 月完成 |

> ⚠️ 限制說明：此試驗分期為 Phase NA（非標準分期，可能為先導性研究），狀態 UNKNOWN 表示試驗資訊不完整或進度不明，且甘草酸是否為唯一干預藥物尚不確定，需直接聯繫試驗負責人確認現況。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26498361](https://pubmed.ncbi.nlm.nih.gov/26498361/) | 2016 | Review | Oncotarget | 甘草酸與甘草次酸可透過 COX-2/TxA2 路徑干預 RA 治療，系統性文獻回顧 |
| [40220871](https://pubmed.ncbi.nlm.nih.gov/40220871/) | 2025 | 前臨床（體外＋體內） | J Controlled Release | 甘草酸-sinomenine 自組裝奈米凝膠增強 RA 抗炎療效，延長半衰期 |
| [38037139](https://pubmed.ncbi.nlm.nih.gov/38037139/) | 2023 | 前臨床 | Chinese Medicine | 芒果苷與甘草酸組合廣泛抑制 RA 滑膜新生血管形成 |
| [35749826](https://pubmed.ncbi.nlm.nih.gov/35749826/) | 2022 | 前臨床 | Phytomedicine | 芒果苷＋甘草酸組合透過逆轉產熱/能量代謝紊亂改善 RA 嚴重程度 |
| [31476301](https://pubmed.ncbi.nlm.nih.gov/31476301/) | 2019 | 前臨床（動物） | Arch Biochem Biophys | 甘草酸聯合 PRP 透過自噬機制改善膠原誘導性關節炎大鼠 |
| [37288078](https://pubmed.ncbi.nlm.nih.gov/37288078/) | 2023 | 前臨床（藥物遞送） | Frontiers in Chemistry | 甘草酸修飾碳點微針系統用於甲氨蝶呤經皮遞送，改善 RA 局部治療 |
| [33593531](https://pubmed.ncbi.nlm.nih.gov/33593531/) | 2021 | 前臨床 | Carbohydrate Polymers | 甘草酸/布地奈德核殼奈米載體共遞送，改善 RA 生物利用度 |
| [38373664](https://pubmed.ncbi.nlm.nih.gov/38373664/) | 2024 | 代謝組學 | J Ethnopharmacology | 芍藥甘草附子湯代謝組學研究，揭示甘草酸為關鍵活性物質 |
| [35667582](https://pubmed.ncbi.nlm.nih.gov/35667582/) | 2022 | 藥物交互作用研究 | J Ethnopharmacology | 芍藥甘草附子湯與 tofacitinib 的 CYP450 酶交互作用，需注意聯用安全 |
| [12761187](https://pubmed.ncbi.nlm.nih.gov/12761187/) | 2003 | 機制研究（體外） | J Biochemistry | 甘草酸與補體 C3 結合並抑制 CK-2 磷酸化，揭示補體調節機轉 |

---

## 其他值得關注的適應症

### 肺動脈高壓（Rank 9，L4，Research Question）

強效機轉連結：HMGB1 是肺動脈高壓（PAH）血管重塑的關鍵促炎介質，而甘草酸是已知最具活性的 HMGB1 拮抗劑之一。目前無臨床試驗，但有 7 篇前臨床/機制研究支持。

| PMID | 年份 | 類型 | 主要發現 |
|------|-----|------|---------|
| [25420924](https://pubmed.ncbi.nlm.nih.gov/25420924/) | 2014 | 動物研究（MCT-PAH 模型） | 甘草酸透過 HMGB1 抑制顯著減緩肺動脈高壓進展及血管重塑 |
| [30517029](https://pubmed.ncbi.nlm.nih.gov/30517029/) | 2019 | 機制研究（動物） | HMGB1 在慢性缺氧及 MCT 誘導肺高壓中機制上不可或缺 |
| [34419454](https://pubmed.ncbi.nlm.nih.gov/34419454/) | 2021 | 動物研究（高原 PAH 模型） | 18β-甘草次酸對高原性肺動脈高壓大鼠具保護作用（NMR 代謝組學） |
| [7613529](https://pubmed.ncbi.nlm.nih.gov/7613529/) | 1995 | 動物研究（血動力學） | 甘草酸影響大鼠右房壓及肺血管壓力（劑量相關效應） |
| [39284704](https://pubmed.ncbi.nlm.nih.gov/39284704/) | 2024 | 藥動/代謝研究 | 甘草酸代謝物個體差異與假性醛固酮增多症（安全性警示） |

> 主要限制：甘草酸的 11β-HSD 抑制可能升高血壓，與 PAH 治療目標存在潛在矛盾，需進一步區分甘草酸 vs. 甘草次酸的血管效應方向。

---

### 巨細胞病毒感染（Rank 6，L3，Research Question）

甘草酸可干擾 CMV 病毒顆粒的膜融合與細胞入侵，體外研究（U-937、MRC-5 細胞株）及嬰幼兒 CMV 相關肝功能不全的小型前瞻性病例系列提供了早期臨床信號。

| PMID | 年份 | 類型 | 主要發現 |
|------|-----|------|---------|
| [8073426](https://pubmed.ncbi.nlm.nih.gov/8073426/) | 1994 | 前瞻性病例系列 | SNMC（甘草酸製劑）靜脈注射改善嬰兒 CMV 相關肝功能異常 |
| [8193264](https://pubmed.ncbi.nlm.nih.gov/8193264/) | 1993 | 前瞻性病例系列 | 口服甘草酸改善 CMV 相關嬰兒肝功能及體重成長 |
| [20416218](https://pubmed.ncbi.nlm.nih.gov/20416218/) | 2010 | 回顧性臨床觀察 | 複方甘草酸治療兒童 CMV 肝炎，改善 D-dimer 及 vWF 凝血指標 |
| [8283138](https://pubmed.ncbi.nlm.nih.gov/8283138/) | 1994 | 體外研究 | 甘草酸抑制 U-937 及 MRC-5 細胞株中 HCMV 病毒抗原表達 |

---

### 痤瘡（Rank 7，L3，Research Question）

甘草酸具抗炎（NF-κB 抑制）、抗痤瘡桿菌及皮脂腺調節潛力；局部或介入性（mesotherapy）給藥可繞過系統性安全疑慮，為最具可行性的給藥方式。

| PMID | 年份 | 類型 | 主要發現 |
|------|-----|------|---------|
| [37036158](https://pubmed.ncbi.nlm.nih.gov/37036158/) | 2023 | 臨床介入研究（中療法） | 複方甘草酸皮內注射治療中重度痤瘡，療效顯著且耐受性良好 |
| [40020947](https://pubmed.ncbi.nlm.nih.gov/40020947/) | 2025 | 前臨床（奈米製劑） | 隱丹參酮-甘草酸自組裝微膠束增強皮膚穿透與抗炎療效 |
| [37183468](https://pubmed.ncbi.nlm.nih.gov/37183468/) | 2024 | Review | 甘草酸等植物抗炎成分在皮膚藥妝品的應用回顧 |

---

## 香港上市資訊

Glycyrrhizic acid 目前在香港**無任何藥品許可證**，未以獨立藥品形式上市。

> 備注：甘草酸製劑（如 SNMC，Stronger Neo-Minophagen C）在日本已核准用於慢性肝炎治療，可作為參考比較對象。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **已知安全性警示**：甘草酸長期或高劑量使用可能導致**假性醛固酮增多症**（低血鉀、高血壓、水腫、低血漿醛固酮），機轉為代謝物甘草次酸抑制腎臟 11β-HSD2 酶，使皮質醇過度活化礦物皮質素受體。此副作用存在**顯著個體差異**（與代謝物生成速率相關，見 PMID 39284704）。臨床使用前應評估血鉀、血壓及腎功能，特別是在肺動脈高壓等心血管適應症的評估中需審慎權衡。此外，甘草酸對 CYP450 酶有潛在影響（見 PMID 35667582），與 tofacitinib 等免疫調節藥物聯用時需注意藥物交互作用。

---

## 結論與下一步

**決策：Proceed with Guardrails（類風濕性關節炎）**

**理由：**
甘草酸對 RA 的多重免疫調節機轉（NF-κB、JAK/STAT、HMGB1 抑制、COX-2/TxA2 路徑）有紮實的前臨床研究支持，20 篇文獻涵蓋機制研究、藥物遞送創新及傳統方劑科學化佐證，並有 1 個相關臨床試驗登記，加上傳統醫學千年安全使用背景，整體推進障礙相對低。

**若要推進需要：**
- 確認 NCT05788705 試驗的最新狀態，釐清甘草酸的角色（單獨或組合用藥）
- 補充正式 MOA 資料（建議查詢 DrugBank API，彌補 DG002 資料缺口）
- 評估甘草酸單獨用藥 vs. 組合療法（如與 sinomenine 或芒果苷）的最佳策略
- 制定系統性安全監測計畫：血鉀、血壓、腎功能（假性醛固酮增多症防護）
- 探索局部/介入性給藥途徑，以降低系統性副作用（對痤瘡適應症尤具潛力）
- 針對肺動脈高壓適應症，需先釐清甘草酸對肺血管張力的淨效應方向（升壓 vs. 降壓）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

