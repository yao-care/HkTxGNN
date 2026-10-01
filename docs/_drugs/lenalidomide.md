---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 509
evidence_level: L5
indication_count: 5
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lenalidomide：從多發性骨髓瘤／del(5q) 骨髓增生異常症候群到骨髓性白血病

## 一句話總結

Lenalidomide 是口服免疫調節藥物，原本用於多發性骨髓瘤，以及伴隨 del(5q) 的低風險骨髓增生異常症候群（MDS）輸血依賴性貧血。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效。
目前有 **50 筆臨床試驗紀錄**和 **20 篇文獻**，但多為 Phase 1/2 的小型試驗，**沒有 Phase 3 的 AML 證據**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；文獻指出核准用於多發性骨髓瘤（合併 dexamethasone）及 del(5q) 低風險 MDS 輸血依賴性貧血 |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.49% |
| 證據等級 | L2（有已完成的 Phase 2 隨機試驗，無 Phase 3 AML 試驗） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails（僅限研究性質） |

---

## 為什麼這個預測合理？

Lenalidomide 是 cereblon E3 連接酶調節劑，會促使 CK1α 等受質被降解。它同時具有免疫調節和直接抗白血病的作用。這個機轉在 del(5q) MDS 中最為確立。細胞研究也顯示，CRBN 蛋白量會影響 AML 細胞對 lenalidomide 的敏感度（PMID 39881283）。

MDS 與 AML 同屬骨髓性腫瘤，約三分之一的 MDS 患者會進展為 AML。因此已在 MDS 證實有效的藥物，延伸到高風險 MDS 及 AML 有其合理性。目前已有多項 Phase 2 試驗測試 lenalidomide 用於 AML 的單藥、合併 azacitidine、合併化療及維持治療。

需要注意的是，有研究指出 lenalidomide 可能促進 **TP53 突變型治療相關骨髓性腫瘤**的發生（PMID 35512188）。這是明確的安全訊號，若要研究此適應症，須以 TP53 狀態篩選病人。

---

## 臨床試驗證據

以下為 50 筆紀錄中最相關的 10 筆。資料庫僅提供試驗設計摘要，未提供療效結果。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要內容 |
|---------|------|------|------|---------|
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | 完成 | 88 | 隨機分組，比較高劑量 lenalidomide、azacitidine 序貫 lenalidomide 與 azacitidine 單用，對象為 ≥65 歲新診斷 AML |
| [NCT00957385](https://clinicaltrials.gov/study/NCT00957385) | Phase 2 | 完成 | 24 | 隨機分組，lenalidomide 維持治療，對象為緩解後的 AML 病人；樣本小 |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | 完成 | 27 | lenalidomide 單藥，對象為第 5 號染色體異常的復發／難治性 AML 或高風險 MDS |
| [NCT00885508](https://clinicaltrials.gov/study/NCT00885508) | Phase 2 | 未知 | 85 | lenalidomide 合併遞增劑量化療，對象為中高風險 MDS 及 del(5q) AML |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Phase 2 | 完成 | 48 | lenalidomide 用於 ≥60 歲、未治療且無 5q 異常的 AML |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Phase 2 | 完成 | 41 | lenalidomide 用於拒絕誘導化療、≥60 歲的 del(5q) AML |
| [NCT01743859](https://clinicaltrials.gov/study/NCT01743859) | Phase 2 | 完成 | 37 | azacitidine 序貫 lenalidomide，對象為復發／難治性 AML 及高風險 MDS，主要指標為 CR/CRi 率 |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | 完成 | 41 | MEC 化療合併 lenalidomide，對象為復發／難治性 AML |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | 未知 | 60 | azacitidine 合併 lenalidomide，依 MRD 監測做維持治療，對象為年長或不適合強化治療的 AML；狀態未知，非已完成 |
| [NCT01029262](https://clinicaltrials.gov/study/NCT01029262) | Phase 3 | 完成 | 239 | 雙盲安慰劑對照，對象為無 del(5q) 的低／中一風險 MDS 輸血依賴性貧血；屬 MDS，非 AML 本身 |

---

## 文獻證據

本適應症目前沒有 RCT 文獻，以下依系統性回顧、臨床研究、綜述的順序排列。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | 系統性回顧／統合分析 | Cancer Manag Res | 評估 lenalidomide 治療 AML 的療效與安全性；摘要指出其對 AML 的效果仍有爭議 |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | 系統性回顧／統合分析 | Hematology | 評估 azacitidine 合併 lenalidomide 用於 AML、高風險 MDS 與 CMML 的療效與不良事件 |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | 前瞻性臨床研究 | Haematologica | Azalena 試驗：azacitidine + lenalidomide + DLI，用於異體移植後復發的 MDS／AML／CMML |
| [37435080](https://pubmed.ncbi.nlm.nih.gov/37435080/) | 2023 | 前瞻性研究 | Front Immunol | azacitidine 合併低劑量 lenalidomide，用於 AML 異體移植後預防復發 |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Phase Ib | J Geriatr Oncol | lenalidomide 用於年長 AML 緩解後治療，評估安全性與老年功能面向 |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Phase I | Bone Marrow Transplant | 異體移植後 lenalidomide 維持治療，16 位高風險 MDS／AML 病人的劑量遞增研究 |
| [40250191](https://pubmed.ncbi.nlm.nih.gov/40250191/) | 2025 | Phase I | Leuk Res | lenalidomide 合併 bortezomib，用於異體移植後復發的 AML／MDS |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | 前臨床／世代研究（安全訊號） | Blood | 分析 416 位治療相關骨髓性腫瘤病人，指出 lenalidomide 會促進 TP53 突變型腫瘤發生 |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | 綜述 | Expert Opin Investig Drugs | 回顧 lenalidomide 用於高風險 MDS 及 AML 的試驗 |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | 前臨床 | Cell Mol Biol Lett | 組蛋白去甲基酶 KDM5C 穩定 cereblon，提高 AML 細胞對 lenalidomide 的敏感度 |

---

## 香港上市資訊

共 8 張許可證，以下列出 5 張。資料庫未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62181 | REVLIMID CAPSULES 15MG (SWITZERLAND) | Bristol-Myers Squibb Pharma (HK) Ltd |
| HK-62182 | REVLIMID CAPSULES 10MG (SWITZERLAND) | Bristol-Myers Squibb Pharma (HK) Ltd |
| HK-62183 | REVLIMID CAPSULES 5MG (SWITZERLAND) | Bristol-Myers Squibb Pharma (HK) Ltd |
| HK-68893 | LENALIDOMIDE SANDOZ CAPSULES 10MG | Sandoz Hong Kong Limited |
| HK-68895 | LENALIDOMIDE SANDOZ CAPSULES 25MG | Sandoz Hong Kong Limited |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫調節／cereblon E3 連接酶調節劑，非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 需重視。證據包中的用藥限制條件要求監測嗜中性白血球低下與血小板低下 |
| 致吐性分級 | 低（口服免疫調節劑，依藥物類別判斷） |
| 監測項目 | CBC（含分類）、血栓栓塞風險、肝腎功能；建議檢測 TP53 突變 |
| 處置防護 | 為沙利竇邁 (thalidomide) 衍生物，處置與使用請依原廠仿單及風險管控規範 |

---

## 安全性考量

- **TP53 突變風險**：有研究指出 lenalidomide 可能促進 TP53 突變型治療相關骨髓性腫瘤（PMID 35512188），用於白血病須先確認 TP53 狀態。
- **血液學毒性與血栓風險**：依證據包的用藥限制條件，應監測嗜中性白血球低下、血小板低下及血栓栓塞。

香港衛生署仿單的警語與禁忌症、藥物交互作用資料目前缺漏，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅限研究性質，屬「研究問題」階段）

**理由：**
- 有多項已完成的 Phase 2 試驗，包括隨機分組的 AML 試驗，顯示臨床上可行，也有明確的機轉基礎。
- 但樣本數都偏小，沒有 Phase 3 AML 證據，且存在 TP53 相關的安全訊號，因此不宜視為可直接推廣的適應症。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，這是目前的阻斷性缺口，缺少它無法進入安全性篩選。
- 補充機轉資料（DrugBank 的 MOA）。
- 判讀各 Phase 2 試驗的實際療效結果，並確認 NCT04490707 這項 Phase 3 試驗的進展。
- 制定病人選擇標準（TP53 篩檢），並規劃血液學與血栓監測。

**其他預測適應症的簡要判斷：**
- 「貧血（aregenerative anemia，實為 MDS 相關貧血）」證據為 L2，可在限縮於 del(5q) MDS 貧血、並有 TP53 篩檢與血液學與血栓監測的前提下推進。
- 「未分類 MDS」證據為 L3，證據有限。
- 「兒童難治性血球減少」與「先天性鐵粒幼細胞貧血」證據為 L4／L5，建議暫緩（Hold）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

