---
layout: default
title: Dexmedetomidine
parent: 僅模型預測 (L5)
nav_order: 263
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

# Dexmedetomidine：從鎮靜到腎因性抗利尿不適當症候群

## 一句話總結

Dexmedetomidine 是 α2 腎上腺素受體促效劑，臨床試驗登記資料描述其核准用於成人 ICU 與處置性鎮靜。
TxGNN 預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，但**目前沒有任何臨床試驗或文獻支持**，且機轉上有明顯疑慮。
在其他預測適應症中，證據最多的是**頭痛疾患 (Headache Disorder)**，有 12 個相關登記試驗與 7 篇文獻，但集中在硬脊膜穿刺後頭痛 (PDPH)。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未列適應症文字；依試驗登記描述為 ICU 與處置性鎮靜 |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。已知 Dexmedetomidine 是 α2 腎上腺素受體促效劑，可降低血管加壓素釋放並促進利尿。

這正是此預測的問題所在。NSIAD 由血管加壓素 V2 受體 (AVPR2) 的活化型突變引起，與 ADH 無關。抑制上游血管加壓素分泌，理論上無法改善受體本身持續活化的狀況。

因此，0.996 的高分目前缺乏機轉支持，未經驗證，不宜視為有效訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症的證據概況

以下為同一批預測中的其他適應症，其中頭痛疾患是唯一有實質證據的方向。

| 預測適應症 | TxGNN 分數 | 證據等級 | 決策 | 說明 |
|-----------|-----------|---------|------|------|
| 偏頭痛 (Migraine Disorder) | 99.49% | L4 | Hold | 僅有 1 個 PDPH 試驗，屬繼發性頭痛，為間接證據 |
| 腦幹型先兆偏頭痛 | 99.35% | L5 | Hold | 無試驗與文獻 |
| **頭痛疾患 (Headache Disorder)** | 99.30% | L3 | Research Question | 證據集中於 PDPH，詳見下方 |
| 三叉自主神經性頭痛 | 99.09% | L5 | Hold | 無試驗與文獻，機轉推論屬臆測 |

### 頭痛疾患：臨床試驗（僅列與 PDPH 直接相關者）

12 個計入的試驗中，有數個是以麻醉為主的試驗，頭痛只是結果指標或關鍵字，故不列出。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04327726](https://clinicaltrials.gov/study/NCT04327726) | 未分期 | 完成 | 43 | 霧化 Dexmedetomidine 治療剖腹產後 PDPH 的隨機對照試驗 |
| [NCT06514040](https://clinicaltrials.gov/study/NCT06514040) | 未分期 | 完成 | 48 | 霧化 Dexmedetomidine 對比口服 Sumatriptan 治療 PDPH |
| [NCT06470854](https://clinicaltrials.gov/study/NCT06470854) | 未分期 | 完成 | 50 | 霧化 Dexmedetomidine 對比雙側枕大神經阻斷（病例對照設計） |
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | 完成 | 90 | 霧化 Dexmedetomidine 對比 Neostigmine/Atropine 與生理食鹽水安慰劑，雙盲隨機 |
| [NCT06824025](https://clinicaltrials.gov/study/NCT06824025) | Early Phase 1 | 尚未招募 | 111 | 霧化 Neostigmine/Atropine 對比 Lignocaine 治療 PDPH；Dexmedetomidine 非明確試驗組，僅作疾病脈絡參考 |

### 頭痛疾患：文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT（雙盲） | Minerva Anestesiologica | 比較霧化 Dexmedetomidine 與 Neostigmine/Atropine 對剖腹產後 PDPH 的保守治療效果 |
| [33993346](https://pubmed.ncbi.nlm.nih.gov/33993346/) | 2021 | RCT | Journal of Anesthesia | 在 PDPH 保守治療中加入霧化 Dexmedetomidine，並以經顱都卜勒評估腦血流動力學效應 |
| [41120897](https://pubmed.ncbi.nlm.nih.gov/41120897/) | 2025 | 系統性回顧與統合分析 | BMC Anesthesiology | 評估霧化 Dexmedetomidine 治療剖腹產後 PDPH 的療效與安全性 |
| [39799300](https://pubmed.ncbi.nlm.nih.gov/39799300/) | 2025 | 病例報告 | BMC Anesthesiology | 兩例產科 PDPH 使用霧化 Dexmedetomidine 的經驗 |
| [31345663](https://pubmed.ncbi.nlm.nih.gov/31345663/) | 2019 | 評論／短報 | Int J Obstet Anesth | 提出霧化 Dexmedetomidine 可能作為 PDPH 的解方（假說層級） |

證據多為小型、以產科為主的研究，沒有 Phase 2/3 標示的試驗，也沒有原發性頭痛（如偏頭痛）的試驗。結論不應外推到 PDPH 以外的頭痛。

## 香港上市資訊

共 10 張許可證，以下列出 5 張。資料庫未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66810 | DEXMEDETOMIDINE SANDOZ CONCENTRATE FOR SOLUTION FOR INFUSION 200MCG/2ML | Sandoz Hong Kong Limited |
| HK-67869 | DEXMEDETOMIDINE FRESENIUS CONCENTRATE FOR SOLUTION FOR INFUSION 0.2MG/2ML | Fresenius Kabi Hong Kong Limited |
| HK-68011 | DEXMEDETOMIDINE B. BRAUN CONCENTRATE FOR SOLUTION FOR INFUSION 200MCG/2ML | B. Braun Medical (HK) Ltd |
| HK-68375 | DEXMEDETOMIDINE KABI CONCENTRATE FOR SOLUTION FOR INFUSION 0.2MG/2ML | Fresenius Kabi Hong Kong Limited |
| HK-63931 | DEXMEDETOMIDINE CONCENTRATE FOR SOLUTION FOR INFUSION 0.2MG/2ML | Jindun Pharma (H.K.) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。DrugBank 查無藥物交互作用資料。

若未來在頭痛方向推進，需特別監測心搏過緩、低血壓與鎮靜。

## 結論與下一步

**決策：Hold**（首要預測：NSIAD）

**理由：**
- NSIAD 預測僅有模型分數，沒有任何試驗或文獻，而且機轉上與 AVPR2 活化型突變相矛盾，高分未經驗證。
- 頭痛疾患方向有小型 PDPH 研究支持（Research Question 階段），但屬繼發性頭痛，不能代表原發性頭痛或偏頭痛。

**若要推進需要：**
- NSIAD：確認是否有任何機轉或個案證據，否則不建議投入資源。
- 頭痛／PDPH：取得更大型、多中心的隨機對照試驗，確認霧化劑型的劑量與安全性。
- 偏頭痛等原發性頭痛：需要專屬的臨床試驗，PDPH 資料無法替代。
- 補齊香港衛生署仿單的警語與禁忌資料，以及 DrugBank 的作用機轉。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

