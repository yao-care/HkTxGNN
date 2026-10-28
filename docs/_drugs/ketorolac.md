---
layout: default
title: Ketorolac
parent: 高證據等級 (L1-L2)
nav_order: 499
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "ketorolac"
predicted_indications: ["headache disorder", "rosacea conjunctivitis", "trigeminal autonomic cephalalgia"]
description: "Ketorolac：預測新適應症為頭痛疾患 (headache disorder)（證據等級 L1）。原適應症：本地許可證資料未記載適應症"
---

# Ketorolac
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Ketorolac: 頭痛疾患 (headache disorder)
{: .text-alpha }

## 一句話總結

Ketorolac 是一種非類固醇消炎止痛藥（NSAID），原適應症為過敏性、春季及乳突狀結膜炎。
TxGNN 模型預測它可能對**頭痛疾患 (Headache Disorder)** 有效，
目前有 **17 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含指引與系統性回顧。
這個用途更接近已確立的仿單外使用（off-label），而非全新的再利用方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 頭痛疾患 (headache disorder) |
| TxGNN 預測分數 | 0.9943 |
| 證據等級 | L1 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據 ketorolac 已知的藥理，它是非選擇性 COX-1/COX-2 抑制劑，
透過阻斷前列腺素合成，減少周邊與中樞敏感化以及神經源性發炎，而這些機制與偏頭痛和緊張型頭痛的疼痛有關。

原適應症（眼部過敏性結膜炎）同樣依賴 COX 抑制來降低前列腺素介導的發炎，因此兩者在機轉上有共通點。
需要說明的是，這段機轉連結是依據 ketorolac 的已知藥理推論，而非來自本次整理的 MOA 資料。

此外，指引層級的文獻已支持 ketorolac 用於急性偏頭痛。因此它較適合視為「已確立的仿單外使用」，而非新穎的再利用候選。

---

## 臨床試驗證據

以下列出 10 個最相關的試驗（共 17 個）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | 完成 | 56 | 靜脈注射 ketorolac 加 metoclopramide 用於兒童偏頭痛急診治療 |
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | 完成 | 72 | Ketorolac 鼻噴劑 vs sumatriptan 鼻噴劑 vs 安慰劑，用於急性偏頭痛 |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | 完成 | 123 | Metoclopramide/diphenhydramine vs 單用 ketorolac 治療緊張型頭痛 |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | 完成 | 173 | 雙盲、安慰劑對照，評估鼻用 ketorolac 治療急性偏頭痛的安全性與止痛效果 |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | 完成 | 330 | 靜脈注射 valproate、metoclopramide、ketorolac 三者比較治療急性偏頭痛 |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | 完成 | 59 | 鼻內 vs 靜脈注射 ketorolac 治療兒童偏頭痛的非劣性試驗 |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | 未知 | 60 | Ketamine vs ketorolac 治療緊張型頭痛（結果未確認） |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | 完成 | 80 | 鼻內 ketamine 與標準療法比較，用於急診原發性頭痛 |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | 提前終止 | 41 | 鼻用 ketorolac 組合 vs 靜脈注射 ketorolac 組合，用於兒童偏頭痛；提前終止，可解讀性有限 |
| [NCT05641363](https://clinicaltrials.gov/study/NCT05641363) | Phase 3 | 完成 | 171 | 三種劑量 ketorolac 用於兒童急性疼痛（非頭痛專屬） |

---

## 文獻證據

以下列出 10 篇最相關的文獻（共 20 篇），依指引與系統性回顧、RCT、其他綜述的順序排列：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | 指引 | Headache | 美國頭痛學會更新成人急診偏頭痛注射藥物治療指引 |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | 指引／證據評估 | Headache | 美國頭痛學會急性偏頭痛藥物治療證據評估 |
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | 系統性回顧／統合分析 | Acad Emerg Med | 評估注射型 ketorolac 治療急性偏頭痛的療效 |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | 系統性回顧／統合分析 | Adv Clin Exp Med | 成人偏頭痛靜脈注射 ketorolac 與 metoclopramide 的比較 |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | 系統性回顧 | Headache | 注射型 ketorolac 治療急性偏頭痛的療效，既有證據並不一致 |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | 系統性回顧 | Headache | 發作性緊張型頭痛的注射藥物治療 |
| [34822214](https://pubmed.ncbi.nlm.nih.gov/34822214/) | 2022 | RCT | Acad Emerg Med | 鼻內 vs 靜脈注射 ketorolac 治療兒童偏頭痛 |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | 兒童急診中 metoclopramide 加或不加 ketorolac 的比較 |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurol Sci | 比較 dexamethasone、metoclopramide、ketorolac、chlorpromazine 的止痛與預防復發效果 |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | 肌肉注射 ketorolac vs meperidine 加 hydroxyzine 治療急性偏頭痛 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49503 | KETO INJ 30MG/ML | 未載明 | 未載明 |
| HK-67719 | REMOPAIN SOLUTION FOR INJECTION 30MG/1ML | 未載明 | 未載明 |
| HK-35309 | TORADOL INJ 3% | 未載明 | 未載明 |
| HK-53935 | KETO ENTERIC-MICROENCAPSULATED CAP 10MG | 未載明 | 未載明 |
| HK-60656 | KETOROLAC TROMETAMOL NORMON INJ SOLN 30MG/ML | 未載明 | 未載明 |

香港目前登記的 5 張許可證均為有效的單方製劑，以注射劑為主，另有 1 張口服腸溶膠囊。

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（非仿單內容，僅供參考）：
  - 消化道：消化性潰瘍（含活動性）、胃潰瘍、發炎性腸道疾病
  - 心血管與腦血管：高血壓、心肌梗塞、冠狀動脈血栓、中風與腦血管疾病、腦梗塞、心臟病
  - 腎肝：腎功能不全、肝病、膽囊疾病
  - 出血與血液：凝血疾患、血友病、貧血、血紅素病變
  - 呼吸與免疫：氣喘（內因性、過敏性）、類風濕性關節炎
  - 代謝：糖尿病、糖尿病酮酸中毒
  - 眼部：乾眼症
- **藥物交互作用**：共查得 222 筆，以下為部分重點：
  - 重大 (Major)：Acetylsalicylic acid（阿斯匹靈）
  - 中度 (Moderate)：皮質類固醇（betamethasone、budesonide、dexamethasone、hydrocortisone）、磺醯脲類降血糖藥（glimepiride、glipizide、glyburide、chlorpropamide、acetohexamide）、kanamycin、levofloxacin、exenatide 等
  - 輕微 (Minor)：famotidine、ranitidine、cimetidine、linaclotide
- **其他提醒**：文獻中有 ketorolac 與鋰鹽併用導致鋰中毒的個案報告（見試驗與文獻之外的次要預測方向），併用鋰鹽的患者需特別留意。

香港仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 其他預測新適應症（附註）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|-----------|-----------|---------|------|------|
| 酒糟性結膜炎 (Rosacea Conjunctivitis) | 0.9940 | L5 | Hold | 僅有模型預測，無臨床試驗與文獻；機轉上 COX 抑制可能減輕眼表發炎，但僅屬假說 |
| 三叉自主神經性頭痛 (Trigeminal Autonomic Cephalalgia) | 0.9939 | L4 | Research Question | 機轉合理，但 NSAID 在叢集性頭痛的療效一般有限；唯一試驗已撤回（0 人），證據僅有間接文獻 |

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 頭痛疾患（特別是偏頭痛與緊張型頭痛）已有多個已完成的 Phase 3/4 試驗、多篇系統性回顧與統合分析，以及美國頭痛學會指引支持，證據等級為 L1。
- 但香港許可證缺乏適應症文字，且 ketorolac 有明確的腸胃道、心血管、腎臟與出血風險，需設置使用防護。

**若要推進需要：**
- 取得香港衛生署核准仿單，確認正式適應症、警語與禁忌，並釐清頭痛使用是否屬仿單外使用
- 補充詳細的作用機轉（MOA）資料
- 訂定使用防護：限制短期使用、排除高風險族群（消化性潰瘍、腎功能不全、心腦血管疾病、出血傾向），並審視與阿斯匹靈、類固醇等的交互作用
- 若考慮兒童或鼻用劑型，需確認香港是否有對應劑型與核准途徑（目前登記以注射劑為主）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

