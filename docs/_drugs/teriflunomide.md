---
layout: default
title: Teriflunomide
parent: 高證據等級 (L1-L2)
nav_order: 849
evidence_level: L1
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Teriflunomide：從多發性硬化症到復發緩解型多發性硬化症

## 一句話總結

Teriflunomide 是一種口服免疫調節藥物，在香港已上市。
TxGNN 模型預測它對**復發緩解型多發性硬化症 (Relapsing-Remitting Multiple Sclerosis)** 有效，
目前有 **25 個臨床試驗**和 **19 篇文獻**支持，其中包含 2 個已完成的 Phase 3 試驗。
這其實是既有的核准用途，並非真正的新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未記載（香港許可證的適應症欄位為空） |
| 預測新適應症 | 復發緩解型多發性硬化症 (Relapsing-Remitting Multiple Sclerosis) |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Teriflunomide 的活性代謝物會抑制二氫乳清酸脫氫酶 (DHODH)，阻斷嘧啶的從頭合成。
活化的 T 細胞和 B 細胞增殖需要大量嘧啶，因此這個機轉可減少淋巴球增殖，
而這些細胞正是復發緩解型多發性硬化症病理的主要推手。

需說明的是，Evidence Pack 的 DrugBank 作用機轉欄位是空的，上述機轉說明來自文獻（如 PMID 31098896）與預測推論。
此外，Evidence Pack 中原適應症也為空白，應視為資料不完整。
文獻與臨床試驗皆顯示，teriflunomide 已是復發型多發性硬化症的既有疾病修飾治療，
因此這項預測屬於既有適應症的確認。TxGNN 的高分（99.24%）與已知的藥物—疾病知識圖譜關聯相符。

## 臨床試驗證據

以下依相關性挑選 10 項（共 25 項）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | 完成 | 1088 | 隨機、雙盲、安慰劑對照，評估 teriflunomide 降低復發頻率與延緩失能累積 |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | 完成 | 742 | 上述試驗的長期延伸，記錄 7 mg 與 14 mg 的長期安全性與療效 |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | 完成 | 324 | Teriflunomide 與干擾素 beta-1a 的評估者盲性比較 |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | 完成 | 147 | Phase 2 試驗的延伸，評估長期安全性與療效 |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | 完成 | 106 | 真實世界觀察性研究，評估至少兩年的療效 |
| [NCT02776072](https://clinicaltrials.gov/study/NCT02776072) | N/A | 完成 | 2978 | 回溯性真實世界研究，比較 DMF、GA、teriflunomide、fingolimod |
| [NCT03302442](https://clinicaltrials.gov/study/NCT03302442) | N/A | 完成 | 3000 | 法國 MS 世代中比較 DMF 與 teriflunomide 的臨床與 MRI 結果 |
| [NCT03561402](https://clinicaltrials.gov/study/NCT03561402) | N/A | 完成 | 24 | 以生物標記探討 teriflunomide 治療者的疾病活動度 |
| [NCT01881191](https://clinicaltrials.gov/study/NCT01881191) | N/A | 完成 | 50 | 以 MRI 評估 teriflunomide 對灰質病變的影響 |
| [NCT06843382](https://clinicaltrials.gov/study/NCT06843382) | N/A | 尚未招募 | 100 | 比較 teriflunomide 與 DMF 對疲勞耐受度的影響 |

## 文獻證據

以下依證據層級挑選 10 篇（共 19 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | N Engl J Med | Ofatumumab 對比 teriflunomide（對照組）用於多發性硬化症 |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | N Engl J Med | Ublituximab 對比 teriflunomide（對照組）用於復發型 MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | N Engl J Med | Tolebrutinib 對比 teriflunomide（對照組）用於復發型 MS |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurol | Evobrutinib 對比 teriflunomide（活性對照）的兩項 Phase 3 試驗 |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurol | OPTIMUM 試驗：ponesimod 對比 teriflunomide |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | 網絡統合分析 | Cochrane Database Syst Rev | 比較免疫調節與免疫抑制治療用於 RRMS |
| [37528262](https://pubmed.ncbi.nlm.nih.gov/37528262/) | 2023 | 統合分析 | Neurotherapeutics | 上市後真實世界研究中 DMF 與 teriflunomide 的比較 |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide 治療 RRMS 的回顧，抑制 DHODH 與嘧啶合成 |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | Review | CNS Drugs | 依歐盟仿單回顧 teriflunomide 的療效、安全性與處方考量 |
| [38619037](https://pubmed.ncbi.nlm.nih.gov/38619037/) | 2024 | 開放標籤延伸 | Mult Scler | TERIKIDS 延伸研究：teriflunomide 用於兒童復發型 MS |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63504 | AUBAGIO TAB 14MG | 錠劑（資料未載明） | 資料未載明 |
| HK-68466 | EPSYRAM TABLETS 14MG | 錠劑（資料未載明） | 資料未載明 |

## 安全性考量

- **藥物交互作用**：資料庫查無相關交互作用紀錄。
- 一般需留意肝毒性與致畸胎性，並依標準流程使用加速排除（washout）程序。此為依臨床常規提出的提醒，Evidence Pack 未包含香港仿單的警語與禁忌資料，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有 2 個已完成的 Phase 3 試驗（NCT00134563、NCT00803049）直接支持療效與長期安全性，
另有多項 RCT 以 teriflunomide 作為活性對照，證據等級為 L1。
這是既有的核准用途，不是真正的老藥新用，但香港仿單的安全性資料與適應症紀錄仍缺漏。

**若要推進需要：**
- 從香港衛生署取得兩張許可證的核准適應症與仿單，確認警語與禁忌
- 補齊 DrugBank 的作用機轉與原適應症資料
- 維持標準安全監測（肝功能、育齡族群避孕與 washout 程序）

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

