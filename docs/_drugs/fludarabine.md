---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fludarabine：預測新適應症為漿細胞骨髓瘤 (Plasma Cell Myeloma)（證據等級 L5）。原適應症：目前資料未載明"
monitor_inn: "Fludarabine"
predicted_indications: ["plasma cell myeloma", "hyperthyroidism", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "indolent plasma cell myeloma", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "brain small vessel disease 1 with or without ocular anomalies", "myelodysplastic syndrome", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "diabetic nephropathy"]
---

# Fludarabine
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

# Fludarabine：從（原適應症資料未載明）到漿細胞骨髓瘤

## 一句話總結

Fludarabine 是一種嘌呤核苷類似物（化療藥物），在香港已有 3 張有效許可證。
TxGNN 模型預測它可能對**漿細胞骨髓瘤 (Plasma Cell Myeloma)** 有效，目前有 **28 個臨床試驗**和 **19 篇文獻**與此方向相關。
但這些證據多數顯示 fludarabine 是移植預處理或 CAR-T 淋巴清除的**支持性成分**，而非單獨的抗骨髓瘤療法。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前資料未載明（香港許可證未列核准適應症文字） |
| 預測新適應症 | 漿細胞骨髓瘤 (Plasma Cell Myeloma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L1（但多為含 fludarabine 的組合方案，屬間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，fludarabine 是嘌呤核苷類似物，具淋巴清除（lymphodepletion）與免疫抑制作用。

在骨髓瘤領域，它主要有兩種角色：
1. **CAR-T 前的淋巴清除**：與 cyclophosphamide 併用，是 BCMA 導向 CAR-T 療法（如 idecabtagene vicleucel、ciltacabtagene autoleucel）的核心預處理方案。
2. **異體移植的減低強度預處理**：搭配 busulfan、melphalan、treosulfan 等，支持植入並促成移植物抗骨髓瘤效應。

此外，有一項前臨床研究（PMID 17976186）顯示 fludarabine 在體外與體內對骨髓瘤細胞株有抑制活性，但臨床上對其單藥療效仍有爭議。因此預測合理，但定位應是「治療流程中的支持成分」，而非獨立的抗骨髓瘤藥物。

---

## 臨床試驗證據

以下列出與漿細胞骨髓瘤最相關的試驗（資料中共 28 筆，此處依相關性評級選列 10 筆）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06045806](https://clinicaltrials.gov/study/NCT06045806) | Phase 3 | 進行中（不招募） | 79 | ide-cel 加 lenalidomide 維持 vs 單用 lenalidomide；fludarabine 屬淋巴清除方案，非受試變項 |
| [NCT07764978](https://clinicaltrials.gov/study/NCT07764978) | Phase 3 | 招募中 | 750 | AZD0120（BCMA/CD19 CAR-T）鞏固治療；預期使用含 fludarabine 的淋巴清除，尚無結果 |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | 完成 | 20 | fludarabine 併用 methoxyamine (TRC102)，用於復發/難治血液惡性腫瘤 |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | 完成 | 16 | 自體移植後接非清髓異體移植（含 fludarabine 方案），用於高風險淋巴瘤、骨髓瘤、CLL |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | 完成 | 213 | 臍帶血移植，採 cyclophosphamide/fludarabine/TBI 清髓預處理，族群混合 |
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | 提前終止 | 6 | busulfan、fludarabine 異體移植用於骨髓瘤或骨髓纖維化，個案數過少 |
| [NCT00909948](https://clinicaltrials.gov/study/NCT00909948) | Phase 1 | 提前終止 | 7 | 非清髓異體移植後刻意誘發移植物排斥，個案數過少 |
| [NCT03093168](https://clinicaltrials.gov/study/NCT03093168) | Phase 1 | 未知 | 10 | BCMA CAR-T；fludarabine 僅作淋巴清除 |
| [NCT05020444](https://clinicaltrials.gov/study/NCT05020444) | Phase 1 | 進行中（不招募） | 16 | TriPRIL CAR-T，fludarabine 加 cyclophosphamide 為標準淋巴清除 |
| [NCT00014508](https://clinicaltrials.gov/study/NCT00014508) | Phase 2 | 完成 | 未提供 | 自體移植後接迷你異體移植治療骨髓瘤 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | 世代研究 | Transplant Cell Ther | 真實世界資料：ide-cel 前的 fludarabine 暴露量與毒性相關，提示需要劑量管控 |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | 世代研究 | Blood | 標準照護下 cilta-cel 用於復發/難治骨髓瘤的安全性與療效 |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | 世代研究 | J Hematol Oncol | LEGEND-2 五年追蹤：BCMA CAR-T 達長期緩解 |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | 世代研究 | J Clin Oncol | BCMA 與 CD19 CAR-T 合併的長期追蹤 |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | Am J Clin Oncol | bortezomib、fludarabine、melphalan（可併全骨髓照射）作為高風險骨髓瘤異體移植預處理 |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | 回溯分析 | Bone Marrow Transplant | fludarabine 加 treosulfan 低毒性預處理用於骨髓瘤異體移植（34 例） |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leuk Res Rep | 分次 busulfan、fludarabine 與移植後 cyclophosphamide；骨髓瘤僅 2 例，非復發死亡率高 |
| [35046063](https://pubmed.ncbi.nlm.nih.gov/35046063/) | 2022 | Review | Clin Cancer Res | FDA 核准 ide-cel 的摘要 |
| [36384767](https://pubmed.ncbi.nlm.nih.gov/36384767/) | 2022 | Review | Med Lett Drugs Ther | ide-cel 藥物評論 |
| [1415309](https://pubmed.ncbi.nlm.nih.gov/1415309/) | 1992 | Review | Am J Med | 骨髓瘤與 CLL 的異同比較 |

此外，另一預測適應症「惰性漿細胞骨髓瘤」的文獻中，有一篇前臨床研究（PMID 17976186，2007）顯示 fludarabine 對骨髓瘤細胞有體外與體內活性。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60491 | FLUDALYM LYOPHILISATE FOR SOLUTION FOR INJECTION OR INFUSION 50MG（Teva） | 未載明（注射劑） | 未載明 |
| HK-58036 | FLUDARABIN EBEWE SOL FOR INJ 50MG/2ML（Sandoz） | 未載明（注射劑） | 未載明 |
| HK-64955 | FLUDARABINE PHOSPHATE POWDER FOR SOLUTION FOR INJECTION OR INFUSION 50MG（Jindun） | 未載明（注射劑） | 未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤核苷類似物） |
| 骨髓抑制風險 | 高（文獻指出 fludarabine 可造成顯著骨髓抑制，並有治療相關 MDS/AML 的報告） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能；並留意神經毒性（高劑量時有嚴重不可逆神經毒性報告） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

詳細警語請參考原廠仿單。

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，較主要者包括：
  - 中度：Metronidazole、Rosuvastatin、Simvastatin、Tinidazole
  - 輕度：Levofloxacin
  - 其餘多筆（如 Amphotericin B、Cimetidine、Morphine、Metformin、Omeprazole 等）嚴重度未分級
- **其他來源的安全訊號**：真實世界研究顯示，CAR-T 前的 fludarabine 暴露量與 ide-cel 後毒性相關（PMID 40972962）。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個含 fludarabine 的 Phase 2/3 試驗與 CAR-T、異體移植的實務支持，但 fludarabine 在其中是預處理成分，並非獨立抗骨髓瘤療法，證據多為間接。
- 其毒性（骨髓抑制、神經毒性、暴露量相關毒性）需要明確的劑量管控。

**若要推進需要：**
- 釐清定位：以「CAR-T 淋巴清除或移植預處理成分」為目標，而非單藥抗骨髓瘤。
- 取得香港仿單的核准適應症、警語與禁忌症（目前缺漏，屬阻擋性資料缺口）。
- 補充作用機轉資料（DrugBank）。
- 建立依腎功能調整的劑量與暴露量監測計畫。

**其他預測適應症的簡要判斷：**
- 骨髓增生異常症候群（MDS）：證據同為 L1，且有隨機 Phase 3 的 fludarabine 組合預處理證據，亦為 Proceed with Guardrails，角色同樣是預處理成分。
- 惰性漿細胞骨髓瘤：L1，Proceed with Guardrails，但試驗多為混合血液惡性腫瘤，無法分離 fludarabine 的貢獻。
- 未分類 MDS：僅有單篇 2011 年預處理研究，列為研究問題（Research Question）。
- 甲狀腺機能亢進、遺傳性罕見病（家族性血尿合併視網膜小動脈迂曲症候群、甲狀腺素抗性症、腦小血管病）、5q 缺失、糖尿病腎病變：僅有模型預測或無關文獻，缺乏機轉依據，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

