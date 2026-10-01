---
layout: default
title: Flunarizine
parent: 高證據等級 (L1-L2)
nav_order: 379
evidence_level: L2
indication_count: 1
---

# Flunarizine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **1** 個
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

# Flunarizine：從（原適應症資料缺漏）到偏頭痛

## 一句話總結

Flunarizine 是一種鈣離子通道阻斷劑，在香港已有 9 張許可證，但本次資料中缺少原適應症與作用機轉。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **19 個臨床試驗**和 **20 篇文獻**支持這個方向，其中多項為與其他預防藥物的直接比較。
值得注意的是，Flunarizine 在多國本來就是偏頭痛預防用藥，這可能不是真正的「新用途」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證的核准適應症欄位皆為空白） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.12% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 記載的詳細作用機轉資料。根據一般藥理知識，Flunarizine 是非選擇性鈣離子通道阻斷劑（T 型與 L 型），另有鈉離子通道阻斷，以及抗組織胺與多巴胺 D2 拮抗作用。以下機轉說明來自通用藥理知識，並非本次資料紀錄。

這些作用可能降低皮質擴散性抑制（cortical spreading depression）與神經元過度興奮，而這兩者與偏頭痛的病理生理有關。因此機轉上支持 TxGNN 的高分預測。

另外，多項試驗與文獻把 Flunarizine 當成偏頭痛預防的標準用藥或對照組，歐洲頭痛聯盟（EHF）也有專門針對 Flunarizine 的統合分析。這顯示它可能早已是既有適應症，而非嚴格意義上的老藥新用。

---

## 臨床試驗證據

本次資料共 19 個試驗，以下列出與 Flunarizine 最相關的 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | 完成 | 62 | Flunarizine 10 mg/日 vs Topiramate 50 mg/日，用於慢性偏頭痛預防 |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | NA | 完成 | 120 | 比較枕大神經阻斷、Topiramate 與 Flunarizine 用於陣發性偏頭痛 |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | NA | 未知 | 84 | Flunarizine vs Amitriptyline 用於偏頭痛預防（巴基斯坦） |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | NA | 招募中 | 44 | Flunarizine vs Propranolol 用於兒童偏頭痛（PedMIDAS） |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | 尚未招募 | 460 | 基層醫療中比較 Amitriptyline、Flunarizine、Topiramate、Propranolol 的預防效果 |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | 完成 | 60 | 青少年偏頭痛預防，加上 α-硫辛酸的療效與安全性 |
| [NCT03828539](https://clinicaltrials.gov/study/NCT03828539) | Phase 4 | 完成 | 777 | Erenumab vs Topiramate；受試者需曾使用或不適用 Flunarizine 等預防藥 |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | NA | 進行中（不再招募） | 60 | 經皮脈衝射頻 vs 鈣離子通道阻斷劑，用於兒童偏頭痛 |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | 尚未招募 | 60 | 傅氏皮下針療法 vs Flunarizine，用於無先兆偏頭痛 |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | 完成 | 75 | Flunarizine 與 Topiramate 併用的藥物動力學交互作用研究 |

**說明：**
- 多數試驗為 Phase 4 或 NA，且缺乏已公布的結果，因此無法確認療效大小。
- 另有 NCT00740259（Flunarizine 用於思覺失調症）等試驗與偏頭痛無關，未列入。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | 統合分析 | J Headache Pain | 歐洲頭痛聯盟針對 Flunarizine 用於偏頭痛預防的系統性回顧與統合分析 |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | RCT | Acta Neurol Scand | Flunarizine 合併經皮眶上神經刺激，偏頭痛預防效果較單一療法佳 |
| [37563914](https://pubmed.ncbi.nlm.nih.gov/37563914/) | 2023 | RCT | J Clin Pharmacol | 60 名青少年隨機分為 Flunarizine 或 Flunarizine 加 α-硫辛酸 |
| [2404346](https://pubmed.ncbi.nlm.nih.gov/2404346/) | 1990 | RCT | S Afr Med J | Flunarizine 與 Propranolol 雙盲比較，用於偏頭痛預防（58 人） |
| [8349477](https://pubmed.ncbi.nlm.nih.gov/8349477/) | 1993 | 比較研究 | Headache | Flunarizine 與 Nifedipine 用於偏頭痛預防的療效比較 |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | 統合分析 | J Assoc Physicians India | Amitriptyline 與 Propranolol、Flunarizine 用於偏頭痛預防的比較 |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | 網絡統合分析 | JAMA Netw Open | 兒童偏頭痛預防藥物的療效與安全性比較 |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | 系統性回顧 | Health Technol Assess | 成人慢性偏頭痛預防藥物的系統性回顧與經濟模型 |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | 治療指引 | Neurology | 美國神經學會／頭痛學會兒童偏頭痛預防藥物指引更新 |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | 治療指引 | Can J Neurol Sci | 加拿大頭痛學會偏頭痛預防指引 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49233 | FURNAZM TAB 5MG | 未載明 | 未載明 |
| HK-41240 | SUZIN CAP 10MG | 未載明 | 未載明 |
| HK-21275 | FLUZINE TAB 5MG | 未載明 | 未載明 |
| HK-61872 | VANID CAPSULES 5MG | 未載明 | 未載明 |
| HK-42370 | SIBERID-5 TAB 5MG | 未載明 | 未載明 |

本表為 9 張許可證中的前 5 張。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多個直接比較試驗與統合分析，以及國際治療指引，都把 Flunarizine 作為偏頭痛預防選項，證據以 L2 為佳。
- 但原適應症、作用機轉與香港核准適應症資料都缺漏，且安全性資料尚未取得，無法確認這是新適應症還是既有適應症。

**若要推進需要：**
- 取得香港衛生署的仿單，確認 Flunarizine 目前核准的適應症，判斷偏頭痛是否已在標示內
- 查詢 DrugBank 補齊作用機轉與原適應症
- 取得仿單中的警語與禁忌症，完成安全性篩選
- 追蹤 NCT06499116、NCT07354126 等進行中試驗的結果
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

