---
layout: default
title: Bendamustine
parent: 高證據等級 (L1-L2)
nav_order: 100
evidence_level: L1
indication_count: 10
---

# Bendamustine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Bendamustine：預測新適應症為被套細胞淋巴瘤 (Mantle Cell Lymphoma)

## 一句話總結

Bendamustine 是一種烷化劑類的細胞毒性抗癌藥，香港已有 9 張許可證，但本次資料未提供原核准適應症文字。
TxGNN 模型預測它可能對**被套細胞淋巴瘤 (Mantle Cell Lymphoma, MCL)** 有效。
目前檢索到 **40 多個相關臨床試驗**，其中至少 **3 個已完成的 Phase 3 隨機試驗**，另有 **多篇 RCT 與治療指引文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 被套細胞淋巴瘤 (Mantle Cell Lymphoma) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。以下說明來自一般藥理知識：Bendamustine 是雙功能烷化劑，帶有類嘌呤的苯并咪唑環。它使 DNA 交叉連結並誘發細胞凋亡，對快速增生的 B 細胞淋巴瘤有效。它與 rituximab（抗 CD20 抗體）合用的化學免疫療法，已是常用的組合。

MCL 是 B 細胞非何杰金氏淋巴瘤的一種亞型，對烷化劑加抗 CD20 的治療有反應。多項研究已把 bendamustine + rituximab (BR) 用於 MCL 的第一線與復發/難治情境。
- 第一線：BRIGHT、StiL 等 Phase 3 試驗。
- 加入新標靶藥物：ibrutinib、acalabrutinib、venetoclax 等。

TxGNN 分數極高（99.63%），與臨床證據方向一致。
不過，原適應症欄位為空，這個用途在臨床上可能已是既有標準治療，未必是真正的「再利用」。建議先確認香港許可證是否已涵蓋此適應症。

---

## 臨床試驗證據

以下為最相關的 10 個試驗（共檢索到 40 多個）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Phase 3 | 完成 | 447 | BRIGHT 試驗：BR 對比 R-CHOP/R-CVP，用於晚期惰性 NHL 或 MCL 第一線，主要指標為完全緩解率 |
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | 完成 | 549 | 第一線 BR 對比 R-CHOP 用於低惡性度淋巴瘤與 MCL，檢驗無惡化存活期的非劣性 |
| [NCT01456351](https://clinicaltrials.gov/study/NCT01456351) | Phase 3 | 完成 | 230 | 復發性低惡性度 NHL 與 MCL：BR 對比 fludarabine + rituximab，檢驗事件無惡化存活期的非劣性 |
| [NCT00891839](https://clinicaltrials.gov/study/NCT00891839) | Phase 2 | 完成 | 45 | BR 用於復發/難治 MCL 的療效與安全性 |
| [NCT01737177](https://clinicaltrials.gov/study/NCT01737177) | Phase 2 | 完成 | 42 | Lenalidomide + BR (R2-B) 用於首次復發/難治 MCL，後續 lenalidomide 維持治療 |
| [NCT04115631](https://clinicaltrials.gov/study/NCT04115631) | Phase 2 | 進行中（不再招募） | 360 | 未治療 MCL（≤70 歲）三組隨機比較：BR/高劑量 cytarabine 加或不加 acalabrutinib，以及 BR + acalabrutinib |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | 招募中 | 476 | Orelabrutinib + BR 對比安慰劑 + BR，用於未治療 MCL（雙盲） |
| [NCT03567876](https://clinicaltrials.gov/study/NCT03567876) | Phase 2 | 完成 | 141 | 高風險年長 MCL：R-BAC 後接 venetoclax（V-RBAC） |
| [NCT01415752](https://clinicaltrials.gov/study/NCT01415752) | Phase 2 | 進行中（不再招募） | 373 | ≥60 歲未治療 MCL 四組隨機：RB 加或不加 bortezomib，並接 rituximab 或 lenalidomide + rituximab 鞏固 |
| [NCT01662050](https://clinicaltrials.gov/study/NCT01662050) | Phase 2 | 完成 | 57 | 年長 MCL 依年齡調整的 R-BAC 誘導治療；早期分析顯示活性佳，但血液毒性相當明顯 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | RCT | Lancet | Phase 3 非劣性試驗：BR 對比 R-CHOP，用於惰性淋巴瘤與 MCL 第一線 |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | RCT | Blood | BRIGHT 試驗：BR 對比 R-CHOP/R-CVP 的非劣性隨機試驗 |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | 世代（長期追蹤） | J Clin Oncol | BRIGHT 試驗 5 年長期追蹤 |
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | RCT | N Engl J Med | Ibrutinib 加 BR 及 rituximab 維持治療，用於未治療 MCL 年長患者 |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | RCT | J Clin Oncol | Acalabrutinib 加 BR 用於未治療 MCL；背景為 ibrutinib 加 BR 延長無惡化存活期，但可能因毒性未改善整體存活期 |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | RCT（試驗設計） | Future Oncol | Phase 3 設計：zanubrutinib + rituximab 對比 BR，用於不適合移植的未治療 MCL |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | RCT（Phase 2/3） | Lancet | ENRICH 試驗：ibrutinib + rituximab 對比免疫化療（R-CHOP 或 BR），用於 ≥60 歲未治療 MCL |
| [40975105](https://pubmed.ncbi.nlm.nih.gov/40975105/) | 2025 | Phase 2 單臂 | Lancet Haematol | FIL_V-RBAC：年長高風險 MCL 於 RBAC 後加 venetoclax；RBAC 為年長適合治療者的標準起始治療之一 |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Phase 2 合併分析 | Blood Adv | 可移植 MCL：3 週期 RB + 3 週期 rituximab/高劑量 cytarabine 誘導，後接自體幹細胞移植 |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | 指引 | HemaSphere | EHA-EU MCL network 診斷與治療指引 |

---

## 香港上市資訊

香港共登記 9 張許可證，以下列出 5 張主要許可證。本次資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66431 | ORIMUST POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | Orient Europharma |
| HK-59067 | TREANDA FOR INJ 100MG | Teva Pharmaceutical Hong Kong |
| HK-66891 | BENDAMUSTINE HYDROCHLORIDE POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | Fresenius Kabi Hong Kong |
| HK-66343 | BEMUNAT 100 POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | I & C (Hong Kong) |
| HK-62300 | TREANDA FOR INJECTION 25MG | Teva Pharmaceutical Hong Kong |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑） |
| 骨髓抑制風險 | 高（文獻指出與 cytarabine 合併的 R-BAC 有相當明顯的血液毒性；同時具 T 細胞淋巴球低下作用） |
| 致吐性分級 | 中度（依藥物類別判斷，請以仿單為準） |
| 監測項目 | CBC（含分類）、肝腎功能；並留意感染與次發性惡性腫瘤 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

本次資料無 DrugBank toxicity 內容。上述為依藥物類別與文獻的判斷，詳細警語請參考原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。本次資料未取得香港衛生署仿單的警語與禁忌症，也未查到藥物交互作用資料。

文獻另提示，bendamustine 的免疫抑制作用可能增加感染與次發性惡性腫瘤的風險（PMID 36792059）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有至少 3 個完成的 Phase 3 隨機試驗（BRIGHT 等）涵蓋 MCL，另有多個 Phase 2 與進行中的 Phase 3（如 orelabrutinib + BR），並有 NEJM、Lancet 等期刊發表的 RCT，證據等級為 L1。
- 這些 Phase 3 試驗多為「惰性 NHL 加 MCL」的混合族群，MCL 為其中一個子群，且香港仿單的警語與適應症資料尚缺，因此建議附帶條件推進。

**若要推進需要：**
- 取得香港衛生署各許可證的仿單，確認核准適應症是否已涵蓋 MCL（判斷是既有用途還是真正的再利用），並補齊警語與禁忌症。
- 補齊 DrugBank 作用機轉資料。
- 擬定血液學與感染監測計畫，特別針對年長患者及與 cytarabine 或標靶藥物的併用情境。
- 補充說明：同一份資料中，MALT 淋巴瘤（L2）也有 Phase 2 專屬試驗，決策為 Proceed with Guardrails，可另行評估。

**以上內容僅供研究參考，不構成醫療建議；預測與候選用途需經臨床驗證。**
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

