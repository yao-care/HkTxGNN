---
layout: default
title: Nepafenac
parent: 高證據等級 (L1-L2)
nav_order: 518
evidence_level: L1
indication_count: 5
---

# Nepafenac
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Nepafenac：從白內障術後眼部發炎疼痛到廣泛眼科發炎相關疾病

## 一句話總結

Nepafenac 是外用非類固醇消炎止痛藥（NSAID）前驅藥，國際上核准用於白內障手術相關的眼部疼痛與發炎。
TxGNN 模型預測它對**廣義眼科疾病 (Eye Disease)** 具高度關聯性，
目前有 **41 個臨床試驗**和 **20 篇文獻**支持，其中多項為已完成的 Phase 3/4 隨機對照試驗。
需注意：此預測與其已知用途高度重疊，屬於既有適應症的證據延伸，而非全新的老藥新用假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 白內障手術後疼痛與發炎（國際仿單適應症；香港無核准許可證資料） |
| 預測新適應症 | 廣義眼科疾病 (Eye Disease) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Nepafenac 為外用 NSAID 前驅藥，經眼組織酯酶水解為活性代謝物 amfenac，抑制 COX-1/COX-2，阻斷前列腺素合成，藉此減少眼內發炎、疼痛與黃斑水腫。這個機轉已在白內障手術後、雷射虹膜切開術後、玻璃體內注射後等多種眼科發炎情境中被驗證。

TxGNN 預測的新適應症「eye disease」本質上與 nepafenac 已確立的核心用途高度重疊——多項 Phase 3/4 隨機對照試驗（如 NCT01109173, n=2120；NCT01853072, n=881）直接針對白內障手術後發炎與糖尿病患者黃斑水腫進行驗證，證據充分。

換句話說，這個預測更像是模型正確辨識出藥物既有的強項，而非發掘全新的治療方向。其價值在於系統性確認 nepafenac 在「廣義眼科發炎疾病」這個更大類別下的證據密度，可作為評估其在香港上市可行性的基礎。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01001806](https://clinicaltrials.gov/study/NCT01001806) | Phase 4 | 完成 | 126 | 比較 nepafenac 與其他 NSAID 眼用藥物之房水穿透濃度，支持其眼內抗發炎藥動學基礎 |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | 完成 | 40 | 直接驗證 nepafenac 降低黃斑前膜手術後黃斑體積/水腫 |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | 完成 | 260 | 安慰劑對照，證實 0.1% 懸液對中國成人白內障術後發炎與疼痛療效優於安慰劑 |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | 完成 | 448 | 學名藥與原廠 Ilevro 生體相等性研究，證實白內障術後止痛消炎療效一致 |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | 提前終止 | 175 | 評估糖尿病視網膜病變患者術後黃斑水腫發生率，因提前終止證據力打折 |
| [NCT02955641](https://clinicaltrials.gov/study/NCT02955641) | N/A | 狀態不明 | 100 | 評估雷射周邊虹膜切開術後是否需要抗發炎眼藥水 |
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | 完成 | 2120 | 大型試驗評估 0.3% 懸液對白內障術後發炎與疼痛之預防與治療效果 |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | 完成 | 881 | 證實 0.3% 每日一次劑量在糖尿病患者白內障術後臨床結果優於安慰劑 |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | 完成 | 819 | 同上設計之獨立試驗，再次驗證糖尿病患者術後療效優越性 |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | 完成 | 1342 | 比較 0.3% 與 0.1% 懸液及安慰劑，確立劑量反應關係 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review | Eur J Ophthalmol | 系統性回顧與統合分析：nepafenac 併用類固醇可減少白內障術後黃斑水腫、改善視力預後 |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | 回顧 nepafenac 於白內障手術中降低發炎、疼痛及囊樣黃斑水腫風險，穿透力佳、副作用低 |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | 微創白內障術後，0.1% nepafenac 與 1% prednisolone 消炎效果比較 |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmol Glaucoma | 雷射周邊虹膜切開術後，0.1% nepafenac 消炎效果與安全性不劣於 1% prednisolone |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | RCT | J Cataract Refract Surg | 預防性 nepafenac 對比 ketorolac 與安慰劑，評估白內障術後黃斑體積變化 |
| [35196591](https://pubmed.ncbi.nlm.nih.gov/35196591/) | 2022 | RCT | Ophthalmol Glaucoma | 雷射虹膜切開術後，0.1% nepafenac 與 0.09% bromfenac 消炎效果比較 |
| [24345317](https://pubmed.ncbi.nlm.nih.gov/24345317/) | 2014 | RCT | Am J Ophthalmol | 隨機前瞻性研究評估 nepafenac 眼藥水對白內障患者眼壓的影響 |
| [29199864](https://pubmed.ncbi.nlm.nih.gov/29199864/) | 2018 | Cohort/Interventional | Curr Eye Res | 前房內使用 nepafenac 之安全性與抑制前列腺素合成之療效驗證 |
| [25493620](https://pubmed.ncbi.nlm.nih.gov/25493620/) | 2016 | Interaction Study | J Glaucoma | 探討 nepafenac 與前列腺素類降眼壓藥物併用對原發性隅角開放性青光眼患者眼壓的影響 |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Comparative Study | Acta Ophthalmol | 比較 nepafenac 與不含防腐劑 diclofenac 於白內障術後之療效與耐受性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多個已完成的 Phase 2/3 隨機對照試驗（含大型試驗 n=2120、n=881、n=819）一致支持 nepafenac 於眼科發炎相關適應症的療效與安全性，證據等級達 L1。但此預測本質上是既有適應症的延伸驗證，而非全新老藥新用方向，實際效益在於支持其於香港申請上市或擴大適應症範圍。

**若要推進需要：**
- 取得 TFDA／香港衛生署仿單警語與禁忌症資料（目前為 Blocking 等級資料缺口，無法進入安全性初評）
- 補充 DrugBank 作用機轉（MOA）正式資料，目前僅能依文獻推論
- 若計畫於香港申請上市，需準備完整的許可證申請與在地臨床橋接資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

