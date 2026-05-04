---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine：從免疫調節劑到炎症性腸病維持治療

## 一句話總結

Azathioprine (AZA) 是嘌呤類免疫調節劑，本數據包中原適應症資料缺乏（台灣無上市許可），但其作為免疫抑制劑的臨床應用已逾 60 年。TxGNN 模型在前 10 項預測中，**炎症性腸病 (Inflammatory Bowel Disease, IBD)** 為最具臨床意義的預測（TxGNN 分數 99.52%，全局排名第 5），目前有逾 **50 個臨床試驗** 及 **20 篇高品質文獻**（含多份 Cochrane 系統性回顧）支持，證據等級達 **L1**。

> ⚠️ **TxGNN 分數最高的前 4 項預測**（colobomatous microphthalmia-rhizomelic dysplasia、brachydactyly-syndactyly、osteoarthritis susceptibility、WHIM syndrome）均為罕見遺傳性發育疾病或原發性免疫缺陷，機轉分析確認為**已知假陽性**（圖譜稀疏節點效應或反適應症），建議全數排除，不列入本報告主體。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未見於本數據包（台灣無上市許可，需補充仿單資料） |
| 最具臨床意義預測 | 炎症性腸病 (Inflammatory Bowel Disease) |
| TxGNN 預測分數 | 99.52%（全局排名第 5；潰瘍性結腸炎另列排名第 9） |
| 證據等級 | L1（多項已完成 Phase 3 RCT 及 Cochrane 系統性回顧） |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

本數據包的作用機轉（MOA）資料缺乏（DG002 數據缺口）。根據已知藥理學資訊，Azathioprine 為嘌呤類抗代謝藥物，體內代謝為 6-巰嘌呤（6-MP），進一步轉化為 6-硫鳥嘌呤核苷酸（6-TGN）。其主要機轉為競爭性抑制嘌呤合成，選擇性抑制 T/B 淋巴球增殖；同時透過 Rac1 GTPase 途徑誘導活化 T 細胞凋亡，降低腸道黏膜促炎細胞激素（IL-2、TNF-α）水平。

炎症性腸病（IBD，包含克隆氏症 Crohn's Disease 及潰瘍性結腸炎 UC）的核心病理機制為腸道黏膜免疫系統異常活化（Th1/Th17/Th2 介導），導致慢性、反覆發作的腸道炎症。AZA 的免疫調節機轉與 IBD 的病理生理機制具有**直接且高度對應**的關聯性，這也是 TxGNN 能準確預測此適應症的根本原因。

潰瘍性結腸炎（UC，預測排名第 9）作為 IBD 的主要亞型，同屬 Th2/Th17 介導的腸道黏膜免疫失調。兩項預測（IBD 排名第 5、UC 排名第 9）在機轉和臨床上高度重疊，共同構成超過 45 年的國際臨床實踐基礎，並獲多份 Cochrane 系統性回顧反覆確認，是本數據包中唯二達 L1 等級的預測。

---

## 臨床試驗證據

（選取 IBD/UC 相關最具代表性的 10 項試驗，優先選取 Grade A 及 Phase 3 已完成者）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | 招募中 | 300 | MIRACLE 試驗：Mirikizumab vs **AZA 標準治療**用於新診斷中重度 UC（52 週多中心 RCT），直接確立 AZA 在 UC 標準治療地位 |
| [NCT05507216](https://clinicaltrials.gov/study/NCT05507216) | Phase 3 | 已完成 | 636 | ABX464 vs 安慰劑在中重度 UC 誘導緩解，AZA 為標準療法失敗之定義門檻，大型已完成 RCT |
| [NCT03464136](https://clinicaltrials.gov/study/NCT03464136) | Phase 3b | 已完成 | 386 | Ustekinumab vs Adalimumab 在生物製劑初治 Crohn's Disease，含 AZA 等免疫調節劑預治失敗族群，直接評估療效與安全性 |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | 已完成 | 78 | **AZA vs Mesalazine** 防止術後 Crohn's Disease 復發，雙盲雙模擬設計，直接比較 AZA 療效 |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | 已完成 | 211 | SPARE 研究：IFX + 抗代謝物（含 AZA）vs 單藥在 Crohn's Disease 維持緩解，評估 AZA 組合治療策略 |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Phase 3 | 招募中 | 166 | **AZA vs MTX** 聯合 Adalimumab 在 Crohn's Disease 的直接頭對頭比較，釐清最佳聯合治療方案 |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | 未知 | 84 | 低劑量 **AZA + Allopurinol** vs 標準 AZA 單藥在 UC，評估優化給藥策略之多中心 RCT |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | 已終止 | 242 | IFX 單藥 vs IFX+AZA vs **AZA 單藥**在中重度 UC，直接評估 AZA 單藥療效（因納入不足終止） |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | 已完成 | 83 | **AZA vs Mesalazine** 防止術後 Crohn's Disease 復發多中心開放標籤 RCT |
| [NCT01235689](https://clinicaltrials.gov/study/NCT01235689) | Phase 3 | 已完成 | 252 | 緊密控制 vs 常規管理策略在 Crohn's Disease（CALM 研究），評估黏膜癒合率，AZA 為骨幹免疫調節藥 |

---

## 文獻證據

（優先選取 Tier 1 高品質文獻：Cochrane 回顧 > Meta-analysis > RCT > Review）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane 系統性回顧 | Cochrane Database | **AZA/6-MP 在 UC 維持緩解**最新更新版 Cochrane 回顧，確認長期緩解維持療效 |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE 試驗：Top-down IFX+AZA vs **AZA 單藥**在類固醇反應性急性重度 UC 的維持治療 |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane 系統性回顧 | Cochrane Database | **AZA/6-MP 在 UC 維持緩解** Cochrane 回顧（2016 版），確認統計學顯著優勢 |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Cochrane 系統性回顧 | Cochrane Database | **AZA/6-MP 在 UC 維持緩解** Cochrane 回顧（2012 版），確立 IBD 療效 |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | AZA/6-MP 在 **UC 療效**統合分析，釐清此類藥物在 UC 相較 Crohn's Disease 的效果差異 |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's & Colitis | **Thiopurines 在 IBD** 最新臨床回顧：涵蓋 AZA、6-MP、thioguanine 的適應症、療效與安全性 |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Review | World J Gastroenterol | **優化 AZA/6-MP 在 IBD 的給藥策略**：6-TGN/6-MMP 代謝物監測與個人化用藥 |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol | **AZA 在 IBD 的分子機轉新見解**：Rac1 GTPase 凋亡路徑與 45 年臨床應用總結 |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | **AZA/6-MP 在 IBD 的藥物基因組學**：TPMT 多型性與代謝物監測的臨床應用 |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Systematic Review | Scand J Gastroenterol Suppl | **AZA 在 IBD 臨床療效與安全性**更新：荷蘭 Crohn's Disease 長期治療核准基礎文件 |

---

## 台灣上市資訊

台灣目前**無** Azathioprine 的上市許可（共 0 張藥品許可證），本藥物在台灣屬未上市狀態。如需使用，須透過**特殊藥品輸入申請**（食藥署專案核准進口）途徑辦理。

---

## 安全性考量

安全性資訊請參考原廠仿單。

本數據包的 TFDA 仿單警語與禁忌資料缺乏（DG001，屬 **Blocking 等級**數據缺口，影響 S1 安全性初評），需另行下載並解析台灣 FDA 仿單 PDF 方可完成安全性評估。藥物交互作用資料庫查詢亦未獲結果（query_status: not_found）。

根據藥物已知特性，Azathioprine 的主要安全注意事項包括：骨髓抑制（嗜中性球低下、血小板低下）、感染易感性增加、TPMT 基因多型性相關嚴重毒性（高達 10% 患者因不良反應停藥），以及長期使用相關惡性腫瘤風險（尤其是淋巴瘤及非黑色素瘤皮膚癌）。建議使用前進行 TPMT 基因型或酶活性篩檢。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
AZA 用於炎症性腸病（Crohn's Disease 及潰瘍性結腸炎）具有 L1 等級最高水準證據——多項已完成的 Phase 3 RCT 及每隔數年持續更新的 Cochrane 系統性回顧（最新至 2025 年）均確認其在維持緩解期的療效，全球主要 IBD 治療指引（ECCO、ACG、BSG）均已將 AZA 納入標準治療方案。台灣目前雖無上市許可為當前主要阻礙，但藥物本身具備充分的有效性與安全性數據基礎。

**若要推進需要：**
- 補充台灣 FDA 仿單警語與禁忌資料（**DG001 Blocking 缺口**，必須優先解決）
- 補充完整 MOA 資料（DG002，查詢 DrugBank API 取得 DB00993 詳細機轉）
- 評估台灣 IBD 患者族群的臨床未滿足需求，研擬特殊藥品輸入申請策略
- 制定包含 **TPMT 基因型篩檢**前置條件的安全監測計畫
- 明確排除 TxGNN 第 1–4 項預測（罕見遺傳性發育疾病及原發性免疫缺陷，確認為假陽性），並標記第 4 項（WHIM syndrome）及第 6、8 項（CGD 相關）為**機轉反適應症**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

