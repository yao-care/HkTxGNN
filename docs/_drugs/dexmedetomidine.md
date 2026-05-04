---
layout: default
title: Dexmedetomidine
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
---

# Dexmedetomidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Dexmedetomidine：從 ICU 鎮靜到頭痛疾患（硬脊膜穿刺後頭痛）

## 一句話總結

Dexmedetomidine（右美托咪定）是高度選擇性的 α2 腎上腺素受體激動劑，目前主要用於加護病房（ICU）鎮靜與程序性鎮靜。
TxGNN 模型共預測 5 項新適應症，其中**頭痛疾患（Headache Disorder）**具有最完整的臨床證據，核心應用集中於**硬脊膜穿刺後頭痛（PDPH）**，
目前有 **4 個相關臨床試驗**（含 1 個 Phase 3 RCT）和 **5 篇文獻**（含 2025 年系統性回顧）支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ICU 鎮靜、程序性鎮靜 |
| TxGNN 最高評分預測 | 腎原性抗利尿不當症候群（99.60%，暫無臨床證據）|
| 最佳證據預測新適應症 | 頭痛疾患（Headache Disorder）— 核心應用：PDPH |
| TxGNN 預測分數（頭痛疾患）| 99.30% |
| 證據等級 | L2（1 個已完成 Phase 3 RCT + 系統性回顧）|
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## TxGNN 預測總覽（本次 5 項）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 腎原性抗利尿不當症候群 | 99.60% | L5 | Hold |
| 2 | 偏頭痛（Migraine Disorder）| 99.49% | L4 | Hold |
| 3 | 基底型偏頭痛（Migraine with Brainstem Aura）| 99.35% | L5 | Hold |
| **4** | **頭痛疾患（Headache Disorder / PDPH）** | **99.30%** | **L2** | **Research Question** |
| 5 | 三叉神經自律性頭痛（TAC）| 99.09% | L5 | Hold |

> **注意**：排名 1 的腎原性抗利尿不當症候群雖 TxGNN 評分最高，但目前無任何臨床試驗或文獻支持，屬純模型預測（L5）。本報告聚焦於證據最完整的頭痛疾患群（排名 4）。

---

## 為什麼這個預測合理？

Dexmedetomidine 是一種高度選擇性的 α2 腎上腺素受體激動劑（α2:α1 選擇比 ≈ 1620:1），主要作用於腦幹藍斑核（locus coeruleus）及脊髓後角，產生鎮靜、抗焦慮與脊髓層面鎮痛效果。TxGNN 知識圖譜捕捉到其與頭痛疾患間的潛在關聯，機轉假說包括三個面向：

① **脊髓層面鎮痛**：α2 受體激動抑制脊髓後角 P 物質及麩胺酸釋放，減少上行痛覺傳遞；② **腦血管收縮效應**：DEX 輕度收縮腦血管，可能逆轉 PDPH 因腦脊液流失所誘發的代償性顱內靜脈擴張；③ **抗焦慮效果**：全身性鎮靜作用降低痛覺感知閾值，減少中樞痛覺敏化。

採用**霧化給藥（nebulized）**是目前臨床試驗的創新亮點，藥物透過上呼吸道黏膜 α2 受體吸收，提供非侵入性治療選項，相較於傳統靜脈輸注或硬膜外血斑（epidural blood patch）更易於臨床接受。需注意：PDPH（低 ICP 代償性靜脈擴張）與原發性偏頭痛（皮質擴散抑制/三叉神經活化）的病理機轉有根本差異，現有臨床證據特指 PDPH，**不能直接外推至原發性頭痛疾患**。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | 完成 | 90 | 三臂雙盲 RCT：霧化 DEX vs. Neostigmine/Atropine vs. 生理鹽水安慰劑，治療剖腹產後 PDPH |
| [NCT06514040](https://clinicaltrials.gov/study/NCT06514040) | NA | 完成 | 48 | 霧化 DEX vs. 口服 Sumatriptan 治療剖腹產後 PDPH，主動對照設計，提供比較效益數據 |
| [NCT04327726](https://clinicaltrials.gov/study/NCT04327726) | NA | 完成 | 43 | 霧化 DEX 治療脊椎麻醉後 PDPH 有效性及腦血流動力學研究（跨顱都卜勒），隨機對照 |
| [NCT06470854](https://clinicaltrials.gov/study/NCT06470854) | NA | 完成 | 50 | 霧化 DEX vs. 雙側枕大神經阻滯治療 PDPH，病例對照研究，增加外部效度 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41120897](https://pubmed.ncbi.nlm.nih.gov/41120897/) | 2025 | 系統性回顧 + Meta 分析 | BMC Anesthesiology | 系統性分析霧化 DEX 治療剖腹產後 PDPH 的整體療效與安全性 |
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT（主動對照）| Minerva Anestesiologica | 霧化 DEX vs. Neostigmine/Atropine 保守治療 PDPH 之療效比較 |
| [33993346](https://pubmed.ncbi.nlm.nih.gov/33993346/) | 2021 | 臨床試驗 | Journal of Anesthesia | 霧化 DEX 補充治療 PDPH 有效性評估，含跨顱都卜勒腦血流動力學分析 |
| [39799300](https://pubmed.ncbi.nlm.nih.gov/39799300/) | 2025 | 病例報告 | BMC Anesthesiology | 霧化 DEX 治療產科 PDPH 2 例成功案例，補充真實世界應用紀錄 |
| [31345663](https://pubmed.ncbi.nlm.nih.gov/31345663/) | 2019 | 先驅研究 / 評論 | Int J Obstetric Anesthesia | DEX 霧化用於 PDPH 治療的早期概念驗證，奠定後續 RCT 基礎 |

---

## 香港上市資訊

Dexmedetomidine 目前在香港**未取得任何藥品許可證**，無上市紀錄（total_licenses = 0）。如需在香港特別行政區使用，須向衛生署申請特殊情況使用許可（Special Authorization），並符合相關藥事法規要求。

---

## 安全性考量

安全性資訊請參考原廠仿單（如 Pfizer/Hospira Precedex® 或 Orion Pharma Dexdor® 產品說明書）。

> ⚠️ **資料缺口提醒**：本 Evidence Pack 的仿單警語（DG001）、禁忌症及藥物交互作用資料均屬資料缺口，建議優先取得正式仿單後再進行完整安全性評估，目前屬 **Blocking** 級別缺口，影響 S1 安全性初評進行。

基於一般藥理知識補充參考：
- **心血管效應**：低血壓、竇性心搏過緩為最常見不良反應，負荷劑量期間須嚴密監測
- **霧化給藥特殊考量**：系統性藥物動力學（PK）數據有限，霧化劑量換算尚無標準指引，需審慎評估

---

## 結論與下一步

**決策：Hold**

**理由：**
Dexmedetomidine 在香港目前未上市（0 張許可證），缺乏藥品基礎登記，無法直接進入商業化評估流程。針對 PDPH 的霧化給藥方式雖具初步臨床試驗支持（1 個 Phase 3 RCT + 2025 年系統性回顧），但樣本規模偏小（n = 43–90），且研究母群體特定於產科椎管內麻醉情境，外推至一般頭痛疾患的可信度有限。TxGNN 最高評分適應症（腎原性抗利尿不當症候群，Rank 1）目前完全無臨床證據支持，仍屬 L5。

**若要推進需要：**
1. **香港上市登記**：向衛生署申請藥品登記或特殊情況使用許可，建立合規基礎
2. **補充安全性資料（Blocking）**：取得完整仿單（DG001），確認警語、禁忌症及主要藥物交互作用
3. **補充 MOA 資料（High）**：透過 DrugBank API 補全作用機轉說明（DG002），支持機轉關聯性分析
4. **PDPH 擴大試驗**：設計 ≥200 人多中心 Phase 3 RCT，擴展至非產科 PDPH 族群（如神經外科、疼痛科），確立霧化標準劑量及系統性 PK 數據
5. **原發性頭痛探索**：設計 Proof-of-Concept 試驗，評估 DEX 對偏頭痛（Rank 2）或三叉神經自律性頭痛（Rank 5）的潛在療效
6. **Rank 1 機轉研究**：探討 DEX 與腎原性抗利尿不當症候群的機轉關聯性，評估是否值得啟動臨床前研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

