---
layout: default
title: Bendamustine
parent: 高證據等級 (L1-L2)
nav_order: 102
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Bendamustine：預測新適應症為被套細胞淋巴瘤 (Mantle Cell Lymphoma)（證據等級 L1）。原適應症：濾泡性淋巴瘤、成熟 B 細胞腫瘤、急性淋巴母細胞白血病、Richter 症候群"
monitor_inn: "Bendamustine"
predicted_indications: ["mantle cell lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Hodgkins lymphoma", "small intestinal Burkitt lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "relapsing-remitting multiple sclerosis"]
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

# Bendamustine：從濾泡性淋巴瘤到被套細胞淋巴瘤

## 一句話總結

Bendamustine 是一種烷化劑化療藥物，原本用於濾泡性淋巴瘤、成熟 B 細胞腫瘤、急性淋巴母細胞白血病及 Richter 症候群。
TxGNN 模型預測它可能對**被套細胞淋巴瘤 (Mantle Cell Lymphoma)** 有效，
目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多個 Phase 3 隨機試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 濾泡性淋巴瘤、成熟 B 細胞腫瘤、急性淋巴母細胞白血病、Richter 症候群（取自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 被套細胞淋巴瘤 (Mantle Cell Lymphoma) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未提供）。依已知資訊，Bendamustine 是具有類嘌呤結構的烷化劑，可造成 DNA 交聯並誘導 B 細胞惡性腫瘤細胞凋亡。

被套細胞淋巴瘤同屬成熟 B 細胞腫瘤，與濾泡性淋巴瘤等原適應症在生物學上相近，因此機轉上可能適用。實際臨床上，Bendamustine 併用 Rituximab（BR）已是被套細胞淋巴瘤的既有治療骨幹，也是多項大型隨機試驗中與 BTK 抑制劑搭配或比較的方案。

## 臨床試驗證據

以下列出最相關的 10 個試驗（資料中共有 40 個登記）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | 完成 | 549 | BR 對比 R-CHOP 作為惰性及被套細胞淋巴瘤第一線治療的非劣性試驗 |
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Phase 3 | 完成 | 447 | BRIGHT 試驗：BR 對比 R-CVP/R-CHOP 用於惰性 NHL 或被套細胞淋巴瘤 |
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Phase 3 | 完成 | 523 | Ibrutinib 併用 BR 用於 65 歲以上新診斷被套細胞淋巴瘤 |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | 進行中（不再招募） | 635 | Acalabrutinib 併用 BR 對比安慰劑併用 BR，用於未治療被套細胞淋巴瘤 |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | 招募中 | 476 | Orelabrutinib 併用 BR 對比 BR，用於初治被套細胞淋巴瘤 |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Phase 3 | 招募中 | 182 | Glofitamab 單藥對比研究者選擇（BR 或 R-Len），用於復發/難治被套細胞淋巴瘤 |
| [NCT00891839](https://clinicaltrials.gov/study/NCT00891839) | Phase 2 | 完成 | 45 | BR 用於復發/難治被套細胞淋巴瘤 |
| [NCT00612183](https://clinicaltrials.gov/study/NCT00612183) | Phase 2 | 完成 | 56 | 日本 SyB L-0501（Bendamustine）用於惰性 B 細胞 NHL 或被套細胞淋巴瘤 |
| [NCT03834688](https://clinicaltrials.gov/study/NCT03834688) | Phase 2 | 完成 | 33 | Venetoclax 併用 BR 用於 60 歲以上未治療被套細胞淋巴瘤 |
| [NCT04115631](https://clinicaltrials.gov/study/NCT04115631) | Phase 2 | 進行中（不再招募） | 360 | BR 搭配高劑量 cytarabine 與 acalabrutinib 的三組隨機比較，用於 70 歲以下未治療被套細胞淋巴瘤 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | RCT | Lancet | BR 在惰性及被套細胞淋巴瘤第一線治療中，無進展存活不劣於 R-CHOP |
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | RCT | N Engl J Med | Ibrutinib 併用 BR 於未治療被套細胞淋巴瘤（SHINE 試驗） |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | RCT | J Clin Oncol | Acalabrutinib 併用 BR 於未治療被套細胞淋巴瘤；先前 ibrutinib 併用 BR 延長無進展存活但總存活未改善，可能與毒性有關 |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | RCT | Lancet | ENRICH 試驗：Ibrutinib + Rituximab 對比標準免疫化療（R-CHOP 或 BR），用於 60 歲以上患者 |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | RCT（試驗設計） | Future Oncol | Zanubrutinib + Rituximab 對比 BR，用於不適合移植的未治療被套細胞淋巴瘤 |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | RCT | Blood | BRIGHT 研究：BR 對比 R-CHOP/R-CVP 的非劣性第三期試驗 |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | 長期追蹤 | J Clin Oncol | BRIGHT 研究 5 年追蹤結果 |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Phase 2 合併分析 | Blood Adv | RB 與 R-cytarabine 誘導治療用於可移植被套細胞淋巴瘤 |
| [40975105](https://pubmed.ncbi.nlm.nih.gov/40975105/) | 2025 | Phase 2 | Lancet Haematol | R-BAC 後接 venetoclax 用於高風險老年被套細胞淋巴瘤 |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | 指引 | HemaSphere | EHA-EU MCL 網絡被套細胞淋巴瘤診斷與治療指引 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66431 | ORIMUST POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | 輸注用濃縮粉劑 | 資料未載明 |
| HK-59067 | TREANDA FOR INJ 100MG | 注射劑 | 資料未載明 |
| HK-66891 | BENDAMUSTINE HYDROCHLORIDE POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG（Fresenius Kabi） | 輸注用濃縮粉劑 | 資料未載明 |
| HK-66343 | BEMUNAT 100 POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | 輸注用濃縮粉劑 | 資料未載明 |
| HK-62300 | TREANDA FOR INJECTION 25MG | 注射劑 | 資料未載明 |

另有 4 張有效許可證（HK-68531、HK-68463、HK-66432、HK-68462），共 9 張，皆為單方、有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑） |
| 骨髓抑制風險 | 高。知識圖譜列出血小板減少、嗜中性白血球減少、顆粒球缺乏症、貧血為禁忌相關疾病；R-BAC 試驗亦提到明顯血液毒性 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（非仿單文字）：肝衰竭、腎臟疾病、膿輸尿管、肝病、膽囊疾病、血小板減少、嗜中性白血球減少、顆粒球缺乏症、貧血、巨球性貧血。
- **藥物交互作用**：共查得 100 筆，以下為主要者。
  - 重大（Major）：Deferiprone、Samarium (153Sm) lexidronam
  - 中度（Moderate）：Omeprazole、Esomeprazole、Cimetidine、Caffeine、Mercaptopurine、Chloramphenicol、Ticlopidine、Deferasirox 等

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的 Phase 3 隨機試驗（NCT00991211、NCT00877006、NCT01776840）及頂級期刊 RCT 支持 BR 用於被套細胞淋巴瘤，證據等級為 L1。
- 因缺乏 MOA 與香港仿單安全性資料，且藥物有明確的骨髓抑制風險，需在防護措施下推進。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認警語、禁忌及核准適應症是否已涵蓋被套細胞淋巴瘤
- 補充詳細的作用機轉（MOA）資料
- 建立血液學監測與感染預防計畫，並評估老年及腎肝功能不全族群的劑量
- 審視 DDI 清單，特別留意 Deferiprone 等重大交互作用

---

**其他預測適應症簡述**（供後續研究參考）：

| 預測適應症 | 證據等級 | 建議 |
|-----------|---------|------|
| MALT 淋巴瘤 | L2 | Proceed with Guardrails（有 Phase 2 BR 試驗，但 Phase 3 試驗多已終止或撤回） |
| 何杰金氏淋巴瘤 | L3 | Research Question（僅小型 Phase 1/2 及兒童組合方案資料） |
| 小腸 MALT 淋巴瘤 | L3 | Research Question（證據多來自一般 MALT 或混合淋巴瘤） |
| 小腸 Burkitt 淋巴瘤 | L3 | Hold（試驗皆為泛淋巴瘤研究，無文獻） |
| 慢性骨髓性白血病 | L4 | Hold（機轉上不支持，TxGNN 高分未獲臨床資料印證） |
| 扁桃腺淋巴瘤 | L4 | Hold（僅有病例報告） |
| 甲狀腺 / 乳房 MALT 淋巴瘤 | L5 | Hold（無直接證據） |
| 復發緩解型多發性硬化症 | L5 | Hold（僅模型預測，且骨髓抑制與感染風險不利） |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

