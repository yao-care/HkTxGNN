---
layout: default
title: Nepafenac
parent: 高證據等級 (L1-L2)
nav_order: 612
evidence_level: L1
indication_count: 10
monitor_inn: "NEPAFENAC"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
last_modified_at: 2026-10-23
description: "Nepafenac：預測新適應症為眼疾 (Eye Disease)（證據等級 L1）。原適應症：香港許可證資料未載明核准適應症文字"
---

# Nepafenac
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

## Nepafenac：從眼科術後發炎與疼痛到眼疾（Eye Disease）
{: .text-alpha }

## 一句話總結

Nepafenac 是一種眼用非類固醇消炎藥（NSAID）前驅藥，在香港以眼用懸浮液形式上市。
TxGNN 模型預測它可能對**眼疾 (Eye Disease)** 有效，但這個類別範圍很廣，且與既有的眼科用途高度重疊，實際上更接近「確認既有用途」，而非全新的藥物再利用。
目前資料中有**多項已完成的臨床試驗**（含數個 Phase 3）和**多篇文獻**，不過需先界定具體的次適應症，才適合推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症文字 |
| 預測新適應症 | 眼疾 (Eye Disease) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L1 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Proceed with Guardrails |

證據等級說明：「眼疾」為廣義類別，本報告所列試驗皆直接研究 nepafenac 在眼部疾病（白內障術後發炎與疼痛、術後黃斑部水腫、糖尿病視網膜病變相關黃斑水腫等）的表現。多個已完成的 Phase 3 隨機對照試驗（例如 NCT01109173、NCT01872611、NCT01853072、NCT01426854）符合 L1 條件。但這些試驗主要驗證的是已知的眼科用途。

---

## 為什麼這個預測合理？

目前資料中缺乏來自 DrugBank 的詳細作用機轉欄位。不過，依據文獻與試驗資料，nepafenac 是一種前驅藥，經眼組織水解酶轉換為 amfenac，後者是 COX-1/COX-2 抑制劑，可降低前列腺素合成。這能抑制眼部發炎、疼痛與血液-視網膜屏障破壞，與其用於術後發炎及黃斑部水腫的臨床方向一致。

「眼疾」是一個涵蓋範圍很廣的類別，與 nepafenac 已上市的眼科用途（白內障術後發炎與疼痛）重疊。因此這個預測較像是對既有用途的確認，而不是發掘全新適應症。在推進前，應先界定具體次適應症，例如術後黃斑部水腫預防、糖尿病視網膜病變相關黃斑水腫等。

藥動學研究顯示，局部點眼後 nepafenac 與 amfenac 可分布至眼後段，這支持其在視網膜相關疾病上的潛在應用；動物模型也顯示它能抑制眼部新生血管及糖尿病誘發的視網膜微血管病變。

---

## 臨床試驗證據

共有 40 項相關試驗，以下列出最相關的 10 項：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | 完成 | 2120 | Nepafenac 0.3% 用於預防與治療白內障術後眼部發炎與疼痛 |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | 完成 | 881 | Nepafenac 0.3% 對比賦形劑，用於糖尿病患者白內障術後臨床結果 |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | 完成 | 819 | 與上項設計相同的平行試驗，糖尿病患者白內障術後 |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | 完成 | 1342 | Nepafenac 0.3% 對比 0.1% 與賦形劑，預防與治療術後發炎與疼痛 |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | 完成 | 260 | Nepafenac 0.1% 對比賦形劑，中國受試者白內障術後發炎與疼痛 |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | 完成 | 263 | NEVANAC 0.1% 對比賦形劑，糖尿病視網膜病變患者白內障術後黃斑水腫 |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | 完成 | 227 | Nepafenac 0.1% 對比 ketorolac 與安慰劑，歐洲白內障術後 |
| [NCT00900887](https://clinicaltrials.gov/study/NCT00900887) | Phase 2 | 完成 | 84 | 局部抗發炎治療（nepafenac 或 ketorolac）用於糖尿病黃斑水腫光凝後中心厚度 |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Phase 4 | 完成 | 126 | 比較 Acuvail、Xibrom、Nevanac 對白內障手術患者 PGE2 的抑制 |
| [NCT07736690](https://clinicaltrials.gov/study/NCT07736690) | Phase 4 | 完成 | 60 | 圍手術期局部 nepafenac 用於視網膜前膜手術後的解剖與功能恢復 |

另有 NCT00939276（Phase 3，已終止，術後黃斑水腫）等多項試驗，此處不一一列出。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | 系統性回顧／網絡統合分析 | Eye | 比較各種局部 NSAID 對超音波乳化術後黃斑水腫與視力結果的影響 |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | 0.1% nepafenac 與 1% prednisolone 用於微切口白內障術後發炎控制的比較 |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | 雷射周邊虹膜切開術後，nepafenac 與 prednisolone 的安全性與療效比較 |
| [41039316](https://pubmed.ncbi.nlm.nih.gov/41039316/) | 2025 | 網絡統合／比較研究 | BMC Ophthalmology | 7 種局部 NSAID 對全視網膜光凝相關疼痛的止痛效果 |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Nepafenac 眼內穿透性高，在白內障手術中的角色 |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAID 在視網膜疾病治療中的應用 |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | 系統性回顧 | Cochrane Database Syst Rev | 局部 NSAID 用於糖尿病囊樣黃斑水腫 |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | 前臨床／藥動學 | Exp Eye Res | 局部給藥後 nepafenac 與 amfenac 分布至眼後段 |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | 動物研究 | Diabetes | 局部 nepafenac 抑制糖尿病大鼠視網膜微血管病變 |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | 病例報告 | J Cataract Refract Surg | Nepafenac 相關角膜融解（角膜穿孔）案例 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67972 | NEVANAC OPHTHALMIC SUSPENSION 0.1% W/V | 眼用懸浮液（品名所示） | 許可證資料未載明 |
| HK-57847 | NEVANAC OPHTHALMIC SUSP 0.1%W/V | 眼用懸浮液（品名所示） | 許可證資料未載明 |

兩張許可證皆為單一成分製劑，持有人為 Novartis Pharmaceuticals (HK) Limited，狀態有效。

---

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（來源為知識圖譜，並非仿單文字）：類風濕性關節炎、糖尿病、糖尿病酮酸中毒、凝血疾病、角膜炎、角結膜炎、乾眼症、乾眼症（眼球乾燥症）、角膜潰瘍。
- **文獻提示的風險**：已有 nepafenac 相關角膜融解、角膜穿孔的病例報告（PMID 17964407），提示在角膜上皮受損或有角膜疾病的患者應謹慎使用。
- **藥物交互作用**：查無相關資料。

完整的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的 Phase 3 隨機對照試驗，在眼科手術後發炎、疼痛及黃斑水腫等情境中支持 nepafenac。
- 「眼疾」類別過於廣泛，且與既有用途重疊，因此需設置護欄：先界定具體次適應症，並留意角膜相關安全性。

**若要推進需要：**
- 釐清具體次適應症（例如預防術後黃斑水腫、糖尿病視網膜病變相關黃斑水腫），並針對各項分別評估證據。
- 取得香港核准適應症文字與完整仿單（警語、禁忌症）。
- 補充詳細的作用機轉資料。
- 制訂角膜安全性監測計畫，特別針對有角膜疾病或乾眼症的族群。
- 確認哪些用途屬於新適應症，哪些僅是現有用途的延伸。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

