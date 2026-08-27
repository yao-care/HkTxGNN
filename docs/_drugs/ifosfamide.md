---
layout: default
title: Ifosfamide
parent: 高證據等級 (L1-L2)
nav_order: 388
evidence_level: L1
indication_count: 5
---

# Ifosfamide
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

# Ifosfamide（異環磷醯胺）：原適應症資料缺失 → 女性乳癌 (Female Breast Carcinoma)

## 一句話總結

IFOSFAMIDE 是一種烷化劑類化學治療藥物（DrugBank ID: DB01181），目前**香港未上市**，且原始核准適應症與作用機轉（MOA）資料皆缺失。TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **8 個臨床試驗**支持這個方向，但相關文獻證據目前掛零。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（原廠仿單與 DrugBank 適應症資料尚未取得） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.91%（排名第 2436） |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料（DrugBank 查詢待補），但根據現有證據描述與已知藥理學分類，Ifosfamide 為烷化劑前驅藥（oxazaphosphorine prodrug），經肝臟代謝活化後產生 isophosphoramide mustard，可與 DNA 形成股間交聯（interstrand cross-link），抑制 DNA 複製與轉錄，對快速增殖的腫瘤細胞（包括乳癌細胞）具直接細胞毒殺作用。

現有證據顯示，Ifosfamide 早已被納入多種轉移性乳癌合併化療方案（常與 paclitaxel、docetaxel 併用），臨床實務上已有一定使用基礎——這代表此項預測並非全新推論，而是有長期臨床操作經驗支持的機轉延伸。

**需要留意的重要提醒**：本評估中唯一的 Phase 3 隨機對照試驗（NCT00954174）實際收案族群為「子宮/輸卵管/腹膜/卵巢之癌肉瘤（Carcinosarcoma）」，並非乳癌患者，與「女性乳癌」適應症的直接關聯性可能有限；且多數其餘試驗狀態為 UNKNOWN 或已終止（TERMINATED），未有明確療效結論。因此本項預測應被解讀為「Ifosfamide 作為合併化療方案組成藥物」的延伸應用，而非具獨立適應症地位的確立新用途，證據等級雖標示為 L1，實際解讀時應審慎看待。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | 未知 (UNKNOWN) | 637 | 比較 Paclitaxel+Carboplatin vs Ifosfamide+Paclitaxel，用於新診斷/持續性/復發性子宮、輸卵管、腹膜或卵巢癌肉瘤；⚠️收案族群為婦科癌肉瘤，非乳癌 |
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | 未知 (UNKNOWN) | 42 | Docetaxel + Ifosfamide 作為轉移性乳癌一線化療 |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | 未知 (UNKNOWN) | N/A | 比較多週期高劑量化療 vs 常規劑量化療於轉移性乳癌 |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | 已完成 | 33 | 序貫高劑量 Cisplatin/Cyclophosphamide/Etoposide/Ifosfamide/Carboplatin/Taxol 併自體幹細胞移植，用於晚期癌症（未特指乳癌） |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | 已終止 | N/A | Topotecan+Ifosfamide/Mesna+Etoposide（TIME 方案）併自體幹細胞救援，用於轉移性乳癌 |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | 已終止 | 12 | 雙重（序貫）自體骨髓移植併 Samarium 153，用於第四期乳癌 |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | 已終止 | 7 | 周邊血幹細胞移植後以活化 T 細胞治療第四期乳癌，Ifosfamide 為前導化療 |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | 不適用 | 未知 (UNKNOWN) | 35 | 以患者衍生類器官（organoid）高通量藥物篩選選擇化療藥物，用於難治性實體瘤（非乳癌專屬，屬體外篩選研究） |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

目前 Ifosfamide **未在香港上市**，無許可證資料（總許可證數：0）。

---

## 細胞毒性

Ifosfamide 屬於已知的細胞毒性化療藥物類別（Oxazaphosphorine 烷化劑），故列出以下資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Oxazaphosphorine 類烷化劑前驅藥，需經肝臟活化為 isophosphoramide mustard） |
| 骨髓抑制風險 | 高。本評估其他候選適應症分析亦指出，Ifosfamide 等烷化劑本身是治療相關性骨髓發育不良症候群（t-MDS）的已知致病因子，顯示其骨髓抑制/基因毒性風險顯著 |
| 致吐性分級 | 中至高（Oxazaphosphorine 類藥物常見特性；確切分級建議參照原廠仿單） |
| 監測項目 | 全血球計數（CBC，含白血球分類）、腎功能（BUN/Creatinine）、尿液常規（監測出血性膀胱炎，需併用 Mesna 保護）、意識狀態評估（監測 Ifosfamide 相關腦病變風險） |
| 處置防護 | 屬細胞毒性抗腫瘤藥物，調配與給藥需依醫療院所危害性藥物（Hazardous Drug）處置規範操作，並使用適當個人防護裝備 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本評估之 TFDA/香港仿單警語、禁忌症與藥物交互作用資料目前皆為缺失狀態，屬 Blocking 等級資料缺口，需優先補齊後方可進入安全性初評。）

---

## 其他預測適應症（不建議推進）

本次評估另預測 4 項適應症，均因缺乏臨床證據且存在機轉矛盾，建議不予推進：

- **未分類骨髓發育不良症候群**、**5q 染色體長臂部分缺失（5q- 症候群）**、**先天性環形鐵芽細胞貧血**：均為 L5（僅模型預測，無實際研究），且更關鍵的是——Ifosfamide 等烷化劑本身是這類骨髓疾病的**已知致病/惡化因子**，機轉方向與「治療」目的相反，應視為安全性警示訊號而非再利用機會。
- **兒童難治性血球低下症**：L4，僅有 1 篇病例對照文獻與 1 個 Phase 1 試驗，且該試驗實際評估的是 Ifosfamide 化療所致血小板低下的支持性治療，並非以 Ifosfamide 治療此病本身，相關性低。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 個 Phase 3 RCT 及多個 Phase 1/2 試驗涉及 Ifosfamide 於乳癌相關化療方案，證據等級達 L1，具一定臨床實務基礎。
- 但關鍵的 Phase 3 試驗（NCT00954174）實際收案族群為婦科癌肉瘤而非乳癌，且多數試驗狀態為 UNKNOWN/TERMINATED，實際支持「女性乳癌」這一具體適應症的證據強度可能被高估，須審慎解讀後再決定是否進一步投入資源。

**若要推進需要：**
- 補齊 TFDA/香港衛生署仿單安全性資料（警語、禁忌症）—— DG001，Blocking 等級，為進入 S1 安全性初評的必要條件
- 查詢 DrugBank API 取得完整作用機轉（MOA）資料 —— DG002，High 等級
- 重新檢視 NCT00954174 實際收案族群是否確實包含乳癌患者，避免將婦科癌肉瘤證據誤判為乳癌證據
- 確認 Ifosfamide 於乳癌其他已完成/已發表 Phase 2/3 試驗結果，以補足目前「已完成試驗僅 1 筆 Phase 1」的證據缺口
- 確認香港上市規劃與許可證申請狀態（目前為未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

