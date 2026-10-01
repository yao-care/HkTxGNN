---
layout: default
title: Ketamine
parent: 中證據等級 (L3-L4)
nav_order: 488
evidence_level: L3
indication_count: 1
---

# Ketamine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Ketamine：從許可證未載明適應症到頭痛疾患 (Headache Disorder)

## 一句話總結

Ketamine 在香港有 4 張注射劑許可證，但許可證資料未載明原適應症。
TxGNN 模型預測它可能對**頭痛疾患 (Headache Disorder)** 有效。
檢索到 39 個臨床試驗和 19 篇文獻，其中直接針對頭痛的有 **9 個臨床試驗**和 **1 篇回溯性世代研究**，但多數規模小，且尚無已提供的療效結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 頭痛疾患 (Headache Disorder) |
| TxGNN 預測分數 | 99.33% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，資料庫中的 MOA 欄位是空白的。以下推論來自 Ketamine 的一般藥理知識，而非本次提供的紀錄：Ketamine 是 NMDA 受體拮抗劑。

偏頭痛、叢集性頭痛和難治性頭痛，都可能牽涉麩胺酸 (glutamate) 訊號傳遞和中樞敏感化 (central sensitization)。若 NMDA 拮抗能逆轉這種受體介導的敏感化，機轉上就有理由用於頑固型頭痛。部分臨床試驗（如 KetHead）正是以此為假說。

TxGNN 的 99.33% 分數只是計算預測，不是臨床證據。原適應症與新適應症之間的相似性分析，也因原適應症資料缺漏而無法進行。

## 臨床試驗證據

下表列出直接針對頭痛的試驗。其餘 30 個試驗涉及鐵鐮型貧血疼痛、憂鬱症、術後鎮痛等其他適應症，或並未測試 Ketamine，不列入。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | 完成 | 80 | THINK 試驗：急診原發性頭痛，鼻內亞麻醉劑量 Ketamine 對比標準治療，單盲、安慰劑對照（未提供結果） |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | 完成 | 54 | 急診頭痛，低劑量 Ketamine 對比 Compazine，雙盲隨機（未提供結果） |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | NA | 完成 | 34 | 急診急性偏頭痛型頭痛，亞麻醉劑量 Ketamine 對比安慰劑（未提供結果） |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | 未知 | 60 | 全身性緊張型頭痛，靜脈 Ketamine 對比 Ketorolac；狀態未知，無結果 |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | 招募中 | 56 | KetHead：慢性每日頭痛，高劑量靜脈 Ketamine 輸注對比安慰劑 |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | 招募中 | 90 | 難治性慢性叢集性頭痛，單次 Ketamine 併用硫酸鎂輸注 |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | 完成 | 23 | 慢性叢集性頭痛，Ketamine 鼻噴劑概念驗證（未提供結果） |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | 招募中 | 175 | 創傷性腦損傷相關頭痛與 PTSD，Ketamine、星狀神經節阻斷及合併治療對比假處置 |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | 完成 | 5 | 急診急性頭痛，口服 Ketamine + Aspirin 對比 Rimegepant，僅 5 人，屬可行性規模 |

**證據限制：**
- 已完成的試驗中，本次資料都沒有提供結果數據。
- 其中 NCT03081416 是唯一已完成、且直接針對頭痛的 Phase 3 隨機試驗，但只有 1 個。
- 目前尚無法確認 Ketamine 對頭痛有效。

## 文獻證據

19 篇文獻中，多數是憂鬱症（含 Esketamine）研究，與頭痛無關，不列入。下表為與頭痛或相關疼痛較相關的文獻。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | 回溯性世代研究 | Front Neurol | 評估 Lidocaine 與 Ketamine 輸注用於住院頭痛疾患的療效、持續時間與安全性；先前僅有小型病例系列支持（摘要未提供結果數值） |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | 叢集性頭痛急性與預防性藥物治療回顧；摘要未顯示 Ketamine 的具體結論 |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | 三叉神經痛藥物治療更新，指出 Ketamine 與大麻素類可能是有潛力的輔助或單一治療選項 |
| [37421541](https://pubmed.ncbi.nlm.nih.gov/37421541/) | 2023 | Review | Curr Pain Headache Rep | 複雜性區域疼痛症候群 (CRPS) 的證據回顧；屬相關疼痛，並非頭痛 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-07901 | KETALAR INJ 10MG/ML（輝瑞） | 未載明 | 未載明 |
| HK-07197 | KETALAR INJ 50MG/ML（輝瑞） | 未載明 | 未載明 |
| HK-61875 | KETAMINE-HAMELN SOLUTION FOR INJECTION 50MG/ML（MEKIM） | 未載明 | 未載明 |
| HK-37715 | KETAMINE INJ 10% (VET)（ALFAMEDIC） | 未載明 | 未載明 |

HK-37715 品名標示為獸醫用 (VET)，與人類用藥的評估無直接關係。四張許可證均為注射劑型。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 頭痛相關試驗規模小（5 至 175 人），已完成者均未提供結果，證據等級僅為 L3。
- 香港仿單的警語與禁忌資料缺漏，屬於阻斷性資料缺口 (DG001)，無法進入 S1 安全性篩選。目前定位是研究問題 (Research Question)。

**若要推進需要：**
- 取得香港衛生署 (Department of Health) 的仿單，補齊警語、禁忌與適應症資料。
- 補上 DrugBank 的作用機轉資料，強化機轉連結分析。
- 取得 NCT03081416、NCT02657031、NCT02697071 的結果或已發表論文，確認療效與安全性。
- 追蹤 KetHead (NCT05306899) 與 NCT04814381 的最終結果。
- 確認給藥途徑相容性：試驗使用靜脈、鼻內和口服，香港許可證均為注射劑型，此項目目前尚未評估。
- 由臨床專家審閱試驗與文獻的相關性，目前多筆仍待審。

本報告結果僅供研究參考，不構成醫療建議。預測的適應症需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

