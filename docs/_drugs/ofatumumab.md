---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ofatumumab：預測新適應症為慢性淋巴性白血病/小淋巴球淋巴瘤 (CLL/SLL)（證據等級 L5）。原適應症：急性淋巴性白血病、Richter 症候群"
monitor_inn: "OFATUMUMAB"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "follicular lymphoma", "leukemia, lymphocytic, susceptibility to"]
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Ofatumumab：從急性淋巴性白血病到慢性淋巴性白血病/小淋巴球淋巴瘤
{: .text-alpha }

## 一句話總結

Ofatumumab 是一種抗 CD20 單株抗體，原本的適應症包括急性淋巴性白血病與 Richter 症候群。
TxGNN 模型預測它可能對**慢性淋巴性白血病/小淋巴球淋巴瘤 (CLL/SLL)** 有效，目前有 **20 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過 ofatumumab 本身已用於 CLL，這個預測較接近既有用途的確認，而非全新的再利用發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴性白血病、Richter 症候群（取自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 慢性淋巴性白血病/小淋巴球淋巴瘤 (CLL/SLL)（TxGNN 排名第 5）；另一個證據較多的預測為濾泡性淋巴瘤 |
| TxGNN 預測分數 | 99.55%（CLL/SLL）；濾泡性淋巴瘤為 99.70% |
| 證據等級 | L1（CLL/SLL）；濾泡性淋巴瘤為 L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails（CLL/SLL） |

> 說明：預測清單中排名最前的兩項（pregerminal center CLL/SLL 與帶有 IGHV 體細胞突變的 CLL/SLL）為 CLL/SLL 的分子亞型，且沒有亞型專屬的試驗或文獻，分數相同，應是來自本體論的關聯。本報告以證據最完整的 CLL/SLL 為主軸，並補充濾泡性淋巴瘤。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄 MOA 欄位）。根據文獻，ofatumumab 是完全人源化的抗 CD20 單株抗體，結合 CD20 上與 rituximab 不同的近膜端表位。它能透過補體依賴性細胞毒性 (CDC) 與抗體依賴性細胞毒性 (ADCC) 殺死表達 CD20 的 B 細胞。

CLL/SLL 與急性淋巴性白血病同屬淋巴系惡性腫瘤，CLL/SLL 細胞表達 CD20，因此機轉上可直接適用。濾泡性淋巴瘤同樣表達 CD20，且 ofatumumab 對 rituximab 難治的患者有理論上的優勢。

需注意：ofatumumab 已在 CLL 取得核准，所以 CLL/SLL 屬於既有適應症。此外，BTK 與 BCL2 抑制劑已改變治療版圖，目前的指引定位需另行確認。

---

## 臨床試驗證據

### CLL/SLL（主要預測，列出 10 個最相關試驗）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02004522](https://clinicaltrials.gov/study/NCT02004522) | Phase 3 | 完成 | 319 | Duvelisib 對比 ofatumumab（對照組），用於復發/難治性 CLL/SLL |
| [NCT01578707](https://clinicaltrials.gov/study/NCT01578707) | Phase 3 | 完成 | 391 | Ibrutinib 對比 ofatumumab，用於復發/難治性 CLL/SLL |
| [NCT02049515](https://clinicaltrials.gov/study/NCT02049515) | Phase 3 | 完成 | 99 | Duvelisib 或 ofatumumab 治療進展後的延伸試驗 |
| [NCT01113632](https://clinicaltrials.gov/study/NCT01113632) | Phase 2 | 完成 | 77 | Ofatumumab 用於年長或拒絕 fludarabine 方案的未治療 CLL/SLL |
| [NCT01024010](https://clinicaltrials.gov/study/NCT01024010) | Phase 2 | 完成 | 82 | Pentostatin + cyclophosphamide + ofatumumab 用於未治療 CLL/SLL |
| [NCT03280160](https://clinicaltrials.gov/study/NCT03280160) | Phase 2 | 狀態未知 | 84 | Ibrutinib 後以 ofatumumab 鞏固，用於未治療 CLL/SLL |
| [NCT01496976](https://clinicaltrials.gov/study/NCT01496976) | Phase 2 | 完成 | 45 | Ofatumumab + 高劑量 methylprednisolone，後續 ofatumumab + lenalidomide 鞏固 |
| [NCT01243190](https://clinicaltrials.gov/study/NCT01243190) | Phase 2 | 完成 | 44 | Ofatumumab 用於高風險早期（0-II 期）未治療 CLL/SLL |
| [NCT01217749](https://clinicaltrials.gov/study/NCT01217749) | Phase 1/2 | 完成 | 71 | Ibrutinib (PCI-32765) + ofatumumab 用於復發/難治性 CLL/SLL |
| [NCT01010568](https://clinicaltrials.gov/study/NCT01010568) | Phase 2 | 提前終止 | 10 | Ofatumumab + bendamustine，因收案少而資料有限 |

此外尚有其他 Phase 1/2 試驗（如 NCT02135133、NCT01002755、NCT01515176 等），因篇幅未逐一列出。

### 濾泡性淋巴瘤（補充，列出 5 個代表性試驗）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | 提前終止 | 346 | Ofatumumab + bendamustine 對比 bendamustine，用於 rituximab 無效的惰性 B 細胞 NHL |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 | 完成 | 135 | Ofatumumab + bendamustine，加或不加 bortezomib，用於未治療濾泡性淋巴瘤 |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | 完成 | 116 | Ofatumumab 單藥用於 rituximab 難治濾泡性淋巴瘤 |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | 完成 | 110 | 局部放療加或不加 ofatumumab，用於 I/II 期濾泡性淋巴瘤 |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | 完成 | 59 | Ofatumumab 兩種劑量 + CHOP，用於未治療濾泡性淋巴瘤 |

---

## 文獻證據

### CLL/SLL

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37138022](https://pubmed.ncbi.nlm.nih.gov/37138022/) | 2023 | 統合分析 | Annals of Hematology | 彙整評估 ofatumumab 方案與非 ofatumumab 方案在 CLL 的療效 |
| [28580841](https://pubmed.ncbi.nlm.nih.gov/28580841/) | 2017 | 系統性回顧/統合分析 | Hematology | 納入 13 個臨床試驗，評估 ofatumumab 在 CLL 的療效與安全性 |
| [25736010](https://pubmed.ncbi.nlm.nih.gov/25736010/) | 2015 | 臨床指引 (NCCN) | JNCCN | 新型抗 CD20 抗體（ofatumumab、obinutuzumab）帶動化學免疫療法發展 |
| [24925211](https://pubmed.ncbi.nlm.nih.gov/24925211/) | 2015 | Phase 2 | Leukemia & Lymphoma | Ofatumumab + bendamustine 用於曾接受治療的 CLL/SLL |
| [26566719](https://pubmed.ncbi.nlm.nih.gov/26566719/) | 2015 | 安全性回顧 | Expert Opin Drug Saf | Ofatumumab 單用或併用，毒性特性良好 |
| [25828085](https://pubmed.ncbi.nlm.nih.gov/25828085/) | 2015 | Review | Haematologica | Ofatumumab 在 CLL 免疫治療中的角色 |
| [20481657](https://pubmed.ncbi.nlm.nih.gov/20481657/) | 2010 | 藥物回顧 | Drugs | 在氟達拉濱與 alemtuzumab 雙重難治 CLL 的關鍵性非對照研究中顯示活性 |
| [32482755](https://pubmed.ncbi.nlm.nih.gov/32482755/) | 2020 | Review | Haematologica | CD20 的調控與功能，CD20 表達量在不同患者間差異大 |
| [38174814](https://pubmed.ncbi.nlm.nih.gov/38174814/) | 2024 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | CLL 維持治療策略 |
| [23211638](https://pubmed.ncbi.nlm.nih.gov/23211638/) | 2013 | 前臨床/機轉 | mAbs | 抗 CD20 抗體表位交互作用與功能特性的關係 |

### 濾泡性淋巴瘤（補充）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT (Phase 2) | Cancer | Ofatumumab + bendamustine 與加 bortezomib 的比較（CALGB 50904） |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | 單臂多中心研究 | Blood | Rituximab 難治濾泡性淋巴瘤，116 位患者，整體反應率約 10–13% |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Phase 2 | Br J Haematol | Ofatumumab + CHOP 用於未治療濾泡性淋巴瘤 |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Phase 2 | Br J Haematol | 單藥 ofatumumab 用於未治療濾泡性淋巴瘤（CALGB 50901） |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Phase 2 | Lancet Haematol | 局部放療與 MRD 導向免疫治療，用於早期濾泡性淋巴瘤 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67210 | KESIMPTA SOLUTION FOR INJECTION IN PRE-FILLED PEN 20MG/0.4ML | 預充填注射筆（溶液） | 資料中未載明 |

> 此許可證為 Kesimpta 20 mg/0.4 mL 預充填注射筆（廠商：Novartis Pharmaceuticals (HK) Limited），為單一成分、有效狀態。此規格與腫瘤適應症使用的靜脈注射製劑不同，本地腫瘤適應症的核准狀況需另行確認。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 CD20 單株抗體），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單；併用化療時風險主要來自併用藥物 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單；抗 CD20 抗體一般需留意 B 型肝炎再活化、進行性多灶性白質腦病 (PML) |
| 處置防護 | 請參考原廠仿單 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 80 項交互作用，主要為免疫抑制相關。屬於 **Major** 的包括 Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib、Certolizumab pegol、Cladribine、Clozapine 等。屬於 **Moderate** 的包括 Alemtuzumab、Azathioprine、Anakinra、Canakinumab、Zidovudine、Chloramphenicol、Roflumilast，以及數種疫苗（破傷風類毒素、炭疽、霍亂活疫苗）。
- **類別警語**：抗 CD20 抗體需留意 B 型肝炎再活化與 PML。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（CLL/SLL）**；濾泡性淋巴瘤為研究性問題（Research Question），建議暫不推進；兩個 CLL/SLL 分子亞型與「易感性」項目建議 Hold。

**理由：**
- CLL/SLL 有多個 Phase 3 試驗與大量 Phase 2 試驗，但 Phase 3 中 ofatumumab 多為對照組，並非以它為主要受試藥的關鍵試驗。且 ofatumumab 已用於 CLL，屬既有用途。
- 濾泡性淋巴瘤雖有多個完成的 Phase 2 試驗，但缺乏完成的 Phase 3 證據，單藥在 rituximab 難治族群的反應率偏低，且不少試驗因收案不足而終止或撤回。

**若要推進需要：**
- 取得原廠仿單的警語與禁忌症（香港衛生署資料目前缺乏）
- 補充作用機轉資料（MOA）
- 確認香港本地腫瘤適應症的核准狀況與劑型（目前許可證為皮下注射筆劑）
- 對照目前 CLL 指引（BTK、BCL2 抑制劑）確認 ofatumumab 的定位
- 落實 B 型肝炎篩檢與 PML 監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

