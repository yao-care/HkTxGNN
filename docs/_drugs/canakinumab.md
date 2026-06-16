---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Canakinumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Canakinumab：從冷焰相關週期性症候群（CAPS）到家族性地中海熱（FMF）

## 一句話總結

Canakinumab（Ilaris，DB06168）是一種全人源抗 IL-1β 單株抗體，原核准用於冷焰相關週期性症候群（CAPS：FCAS / MWS / NOMID）及全身型幼年特發性關節炎（sJIA）等自身炎症性疾病。
TxGNN 模型共預測 10 項潛在新適應症；其中**家族性地中海熱（Familial Mediterranean Fever, autosomal dominant）**（TxGNN 排名第 6）具備最高臨床轉譯價值，目前有 **7 個臨床試驗**（含 5 項 Phase 3 已完成）和 **20 篇文獻**支持。
Canakinumab 在 FMF 方面已獲 EMA（2016）及 FDA 核准，惟**香港尚未正式上市**，本報告聚焦此最高證據優先適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 冷焰相關週期性症候群（CAPS：FCAS / MWS / NOMID），sJIA（依全球核准，HK 仿單資料缺失） |
| 預測新適應症（最高證據） | 家族性地中海熱（Familial Mediterranean Fever, autosomal dominant） |
| TxGNN 預測分數 | 99.41%（TxGNN 排名 #10,024） |
| 證據等級 | L1（≥2 項已完成 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Canakinumab 是一種全人源 IgG1/κ 型單株抗體，能高度選擇性地中和 IL-1β，阻斷其與受體（IL-1R1）結合，從根本上抑制 IL-1β 介導的炎症瀑布反應。其血清半衰期長達約 26 天，適合每 4–8 週一次的皮下注射給藥，有別於半衰期僅數小時的 anakinra，大幅提升患者用藥依從性。

家族性地中海熱（FMF）的核心致病機轉為：**MEFV 基因突變（Pyrin 蛋白功能異常）→ Pyrin 炎症體異常活化 → Caspase-1 活化 → IL-1β 大量成熟分泌 → 週期性發燒、漿膜炎、關節炎，長期可導致繼發性 AA 澱粉樣變腎損傷**。Canakinumab 直接中和終效應分子 IL-1β，相當於切斷此致病路徑最關鍵的一環，機轉合理性極高。

在臨床轉譯層面，秋水仙鹼（Colchicine）為 FMF 一線治療，但約 5–10% 患者完全無效、另有 40% 反應不足。針對此「colchicine 難治性或不耐受」族群，EMA 於 2016 年批准 Canakinumab（≥2 歲），FDA 同年批准，Phase 3 試驗（PMID 29768139，NEJM 2018）提供了最高等級直接證據，香港引入門檻明確，可循特殊藥物進口途徑申請。

---

## 所有預測適應症摘要

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|--------|-----------|---------|------|
| 1 | Hepatic infarction（肝梗塞） | 99.86% | L5 | Hold |
| 2 | Hepatic veno-occlusive disease（肝靜脈閉塞病） | 99.82% | L5 | Hold |
| 3 | Peliosis hepatis（紫癜肝） | 99.78% | L5 | Hold |
| 4 | Syndrome with combined immunodeficiency | 99.71% | L4 | Hold |
| 5 | Periodic fever-infantile enterocolitis-autoinflammatory syndrome | 99.57% | L3 | Research Question |
| **6** | **Familial Mediterranean fever, autosomal dominant ★** | **99.41%** | **L1** | **Proceed with Guardrails** |
| 7 | Extracutaneous mastocytoma（皮膚外肥大細胞瘤） | 99.35% | L5 | Hold |
| 8 | Blau syndrome | 99.34% | L4 | Research Question |
| 9 | Monosomy X（Turner 症候群） | 99.31% | L5 | Hold |
| 10 | Liver angiosarcoma（肝血管肉瘤） | 99.30% | L5 | Hold |

> **注意**：TxGNN 高分不等於臨床可行性。排名 1–4、7、9–10 因機轉關聯弱或無臨床數據，建議 Hold；排名 5、8 具備機轉合理性，可作為後續研究方向。

---

## 臨床試驗證據（家族性地中海熱 / CAPS）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | 完成 | 166 | 長期開放標籤安全性與療效研究，CAPS（FCAS/MWS/NOMID）患者，為本清單最大規模 Phase 3 試驗 |
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Phase 3 | 完成 | 35 | 隨機雙盲安慰劑對照撤藥設計（金標準），Muckle-Wells 症候群，直接評估療效維持與復發 |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Phase 3 | 完成 | 17 | 開放標籤多中心研究，≤4 歲 CAPS 幼兒，評估安全性、耐受性與疫苗接種相容性 |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | 完成 | 17 | Phase 3 開放標籤延伸研究，評估 CAPS 患者長期維持療效與安全性 |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | 完成 | 19 | 日本 CAPS 患者開放標籤療效安全性研究，延伸至商業化前持續供藥，補充亞洲族群數據 |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Phase 2 | 完成 | 20 | TRAPS 患者開放標籤研究，4 個月治療期後 6 個月撤藥設計，探索性補充數據 |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | 觀察性 | 招募中 | 25 | 真實世界非干預性研究（REASSURE），評估 Ilaris 在 CAPS/crFMF/TRAPS/HIDS-MKD/sJIA 患者的安全性與有效性，預計 2028 年完成 |

---

## 文獻證據（家族性地中海熱）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Clinical Review | NEJM | FMF、HIDS/MKD、TRAPS 三種單基因自身炎症疾病的 Canakinumab Phase 3 療效數據，奠定 EMA 核准基礎 |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic Review | Front Immunology | IL-1 靶向生物製劑（anakinra、canakinumab、rilonacept）在自身炎症疾病的系統性安全性與療效回顧 |
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Meta-analysis | Rheumatology | 抗 IL-1 治療在 FMF 的療效與安全性系統回顧暨統合分析，提供定量合併效果量 |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohort Study | Int J Rheum Dis | 比較 Canakinumab 合併/不合併秋水仙鹼治療 FMF 的發作特性、急性期反應物及腎臟結果 |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Clinical Review | Clin Exp Rheumatol | FMF 中 IL-1 抑制的臨床結果分析，探討秋水仙鹼難治患者改用 anti-IL-1 的時機與預期 |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Cohort Study | Rheumatology | 膠原蛋白抵抗 FMF 兒童患者 Canakinumab 停藥可行性，建立治療管理與停藥協議 |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Review | Expert Rev Clin Immunol | Canakinumab 用於 FMF 的完整治療回顧：IL-1β 阻斷機轉、適應症與臨床應用 |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Review | Turkish J Med Sci | FMF 從發病機轉到治療的現代綜述，涵蓋 IL-1 靶向治療新進展與遺傳學更新 |
| [31365342](https://pubmed.ncbi.nlm.nih.gov/31365342/) | 2019 | Case Series | Eur J Rheumatol | 秋水仙鹼無效 FMF 患者接受 Canakinumab 治療的療效與安全性個案系列報告 |
| [34684086](https://pubmed.ncbi.nlm.nih.gov/34684086/) | 2021 | Review | Medicina | FMF 相關澱粉樣變與腎小球疾病，IL-1 抑制的長期腎臟保護潛力 |

---

## 香港上市資訊

Canakinumab（Ilaris）在香港**未有核准登記許可證**，衛生署藥劑業及毒藥管理局資料庫中無相關記錄（許可證數：0）。

如需在香港取得此藥，須依香港《藥劑業及毒藥條例》申請「未登記藥物」進口許可，或透過醫院管理局同情用藥（Compassionate Use）途徑申請。

---

## 安全性考量

安全性資訊請參考原廠仿單（Novartis Ilaris SmPC/PI）。

> **資料缺口說明**：本 Evidence Pack 缺乏 TFDA 仿單警語/禁忌資料（Data Gap DG001，Blocking 級別）及完整作用機轉資料（DG002）。根據 Canakinumab 的藥理分類（IL-1β 拮抗劑，免疫抑制性生物製劑），使用前應特別注意：**感染風險評估（含結核病篩查）**、活性疫苗禁忌、免疫低下族群慎用，以及長期使用的感染監測計畫。

---

## 結論與下一步

**決策：Proceed with Guardrails**（適用於家族性地中海熱 colchicine 難治性或不耐受族群）

**理由：**
Canakinumab 在家族性地中海熱方面已具備最高等級臨床證據（L1），5 項已完成 Phase 3 試驗（最大規模 n=166）搭配 NEJM 主論文（PMID 29768139），以及 EMA/FDA 雙邊批准的監管背書，轉譯基礎扎實。香港未上市屬行政障礙而非科學障礙，可循特殊進口途徑引入，服務膠原蛋白難治 FMF 罕見病患者。

**若要推進需要：**
- 取得 Novartis Ilaris 原廠仿單（歐洲 SmPC 或美國 PI），補充完整警語、禁忌症及藥物交互作用，解除 DG001 Blocking 缺口
- 評估香港 FMF 患者人數（FMF 在亞洲族群發生率低於地中海族群，需確認市場規模）
- 向衛生署申請「第 21 條令」未登記藥物使用許可，或向醫院管理局申請罕見病藥物引入
- 建立感染監測計畫（結核病基線篩查、感染事件回報機制）
- 將**排名第 5（週期性發燒-嬰兒腸炎-自身炎症症候群，L3）** 及**排名第 8（Blau 症候群，L4）** 列為後續研究問題，考慮設計病例系列或前導性 RCT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

