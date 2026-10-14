---
layout: default
title: Teriflunomide
parent: 高證據等級 (L1-L2)
nav_order: 864
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

Teriflunomide 原本用於治療多發性硬化症 (Multiple Sclerosis)。
TxGNN 模型預測它對**復發緩解型多發性硬化症 (Relapsing-Remitting Multiple Sclerosis)** 有效，
目前有 **12 個臨床試驗**和 **20 篇文獻**支持。需要說明的是，這其實是已核准的適應症（屬原適應症的亞型），並非嚴格意義上的新用途，因此預測結果主要用來驗證模型，而不是提供新的證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 多發性硬化症 (Multiple Sclerosis) |
| 預測新適應症 | 復發緩解型多發性硬化症 (Relapsing-Remitting Multiple Sclerosis) |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏資料庫中詳細的作用機轉記載。依據已知藥理，teriflunomide 的活性代謝物會抑制二氫乳清酸脫氫酶 (DHODH)，阻斷嘧啶的從頭合成，進而限制活化 T 細胞與 B 細胞的增生，因此能減少復發次數與病灶活動。

復發緩解型多發性硬化症是多發性硬化症最常見的病程型態，teriflunomide 已被核准用於復發型多發性硬化症。因此這項預測與既有適應症高度一致，0.992 的高分反映的是模型能重現已知事實，並不代表發現了新的治療機會。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | 完成 | 1088 | 雙盲、安慰劑對照，評估 teriflunomide 降低復發頻率與延緩失能累積 |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | 完成 | 324 | Teriflunomide 兩種劑量與干擾素 β-1a 的療效與安全性比較 |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | 完成 | 742 | 7 mg 與 14 mg 的長期延伸研究，記錄長期安全性與耐受性 |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | 完成 | 147 | Phase 2 延伸研究，評估長期安全性與療效 |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | 完成 | 185 | Ofatumumab 與第一線 DMT（醫師選擇）比較，開放標示、評估者盲性 |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | 完成 | 106 | Teriflunomide 的真實世界觀察性療效研究 |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | 進行中（不再招募） | 800 | DELIVER-MS：早期高效治療與升階治療策略比較 |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | 完成 | 900 | 早期積極治療與升階治療的實用性試驗 |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | 完成 | 30 | 探討調節性 B 細胞在 teriflunomide 作用機轉中的角色 |
| [NCT07189325](https://clinicaltrials.gov/study/NCT07189325) | Phase 3 | 招募中 | 250 | 抗 CD20 維持與降階策略的非劣性試驗，與 teriflunomide 僅間接相關 |

注：其中直接評估 teriflunomide 的 Phase 3 試驗為 NCT00134563、NCT00883337 與 NCT00803049。其餘多屬策略比較或間接相關研究。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | N Engl J Med | Ofatumumab 與 teriflunomide 在多發性硬化症的比較 |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurol | OPTIMUM：ponesimod 與 teriflunomide 的 Phase 3 比較 |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | N Engl J Med | Ublituximab 與 teriflunomide 在復發型多發性硬化症的比較 |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurol | Evobrutinib 與 teriflunomide（活性對照）的兩項 Phase 3 試驗 |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | N Engl J Med | Tolebrutinib 與 teriflunomide 在復發型多發性硬化症的比較 |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | 網絡統合分析 | Cochrane Database Syst Rev | 復發緩解型多發性硬化症免疫調節與免疫抑制治療的比較 |
| [38032059](https://pubmed.ncbi.nlm.nih.gov/38032059/) | 2023 | 網絡統合分析 | Cochrane Database Syst Rev | 多發性硬化症免疫治療不良反應的比較 |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide 在復發緩解型多發性硬化症的綜述，指出其為有效且耐受性良好的口服藥 |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | 多發性硬化症的診斷與治療綜述 |
| [37578431](https://pubmed.ncbi.nlm.nih.gov/37578431/) | 2023 | 觀察性研究 | Eur J Neurol | 真實世界中 dimethyl fumarate 與 teriflunomide 的療效比較 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63504 | AUBAGIO TAB 14MG（賽諾菲） | 錠劑（14 mg） | 資料未載明 |
| HK-68466 | EPSYRAM TABLETS 14MG（I & C (Hong Kong) Limited） | 錠劑（14 mg） | 資料未載明 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分列舉：
  - 嚴重 (Major)：acarbose、hydrocortisone、pioglitazone、bupropion、triamcinolone、acetylsalicylic acid、dexamethasone、betamethasone、budesonide、clarithromycin、minocycline 等
  - 中度 (Moderate)：alosetron、cimetidine、empagliflozin、sitagliptin
  - 輕微 (Minor)：zinc sulfate、zinc acetate

警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Teriflunomide 已有 Phase 3 安慰劑對照及主動對照試驗支持，且多項大型 RCT 以它作為活性對照藥，並已在香港上市。證據等級為 L1。
- 這是既有適應症，而非新的再利用方向；加上仿單的警語與禁忌症資料目前缺漏，因此需附帶安全性防護條件。

**若要推進需要：**
- 取得香港衛生署核准仿單，補齊警語與禁忌症，並確認核准適應症文字（目前許可證資料中為空白）
- 補充詳細的作用機轉資料（DrugBank MOA）
- 針對高風險交互作用（例如糖皮質素類及部分降血糖藥）制定用藥審查與監測計畫
- 若要主張真正的新用途，需另行評估其他適應症，而非以本預測作為依據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

