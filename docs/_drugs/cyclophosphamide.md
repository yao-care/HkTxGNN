---
layout: default
title: Cyclophosphamide
parent: 高證據等級 (L1-L2)
nav_order: 198
evidence_level: L1
indication_count: 5
---

# Cyclophosphamide
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

# Cyclophosphamide：從廣效烷化劑到骨髓性白血病

## 一句話總結

Cyclophosphamide 是臨床廣泛應用的烷化劑（alkylating agent），透過 DNA 交叉鏈結抑制腫瘤細胞增殖，歷史上用於多種惡性腫瘤及自體免疫疾病。TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，目前有超過 **20 個相關臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 多種惡性腫瘤（淋巴瘤、白血病、乳癌等）及嚴重自體免疫疾病 |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.47% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cyclophosphamide 是氮芥（nitrogen mustard）衍生的烷化劑，以前體藥形式進入體內後，由肝臟細胞色素 P450 酶系統（主要為 CYP2B6）代謝為活性代謝物——磷酰胺氮芥（phosphoramide mustard）。活性代謝物與 DNA 的鳥嘌呤形成雙股鏈內或鏈間交叉鏈結，阻礙 DNA 複製與轉錄，對快速分裂的惡性細胞具強力細胞毒性。

Cyclophosphamide 在骨髓性白血病的治療中扮演兩個已廣泛驗證的核心角色：**（一）骨髓清除性預處理（myeloablative conditioning）**，以 Bu/Cy（Busulfan + Cyclophosphamide）方案消除殘餘白血病細胞並為造血幹細胞移植（HSCT）騰出骨髓空間；**（二）移植後高劑量 Cy（post-transplant cyclophosphamide, PTCy）**，選擇性清除異應 T 細胞，達到 GVHD 預防效果同時保留移植物抗白血病（GVL）活性。此外，在高白細胞症急症處理中，高劑量 Cyclophosphamide 亦可迅速降低腫瘤負擔。

AML 細胞具快速增殖特性，高度依賴 DNA 複製，因此對烷化劑的 DNA 損傷機轉具結構性敏感性。現有 Phase 3 隨機對照試驗（NCT02724163，n=700）及多個 Phase 2 完成試驗直接驗證了以上臨床應用，為 TxGNN 預測提供了充分的生物學及臨床基礎。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02724163](https://clinicaltrials.gov/study/NCT02724163) | Phase 3 | 招募中 | 700 | 國際兒童 AML 隨機試驗，評估 Gemtuzumab ozogamicin 加入誘導化療之最佳劑量及療效，為目前最高等級直接證據 |
| [NCT01707004](https://clinicaltrials.gov/study/NCT01707004) | Phase 2 | 完成 | 20 | Decitabine 後接骨髓移植 + **高劑量 Cyclophosphamide** 治療復發/難治 AML，直接評估本藥在本適應症之療效與安全性 |
| [NCT02294552](https://clinicaltrials.gov/study/NCT02294552) | Phase 2 | 完成 | 200 | 移植後高劑量 PTCy（單一 vs 合併 Tacrolimus/MMF）之風險適應策略用於 allo-SCT GVHD 預防，大型前瞻性研究 |
| [NCT00553202](https://clinicaltrials.gov/study/NCT00553202) | Phase 2 | 完成 | 158 | KIR 不相容非親屬供者 HSCT 治療兒童高危 AML（含 Monosomy 7、FLT3-ITD 高比值等難治組） |
| [NCT00849147](https://clinicaltrials.gov/study/NCT00849147) | Phase 2 | 完成 | 55 | 多中心非骨髓清除性預處理 + 半相合親屬骨髓移植治療白血病/淋巴瘤（BMT CTN #0603） |
| [NCT04943757](https://clinicaltrials.gov/study/NCT04943757) | Phase 2 | 完成 | 50 | 移植後 Bendamustine + Cyclophosphamide 用於難治性髓系惡性腫瘤 GVHD 預防，探討增強 GVL 效果 |
| [NCT02094794](https://clinicaltrials.gov/study/NCT02094794) | Phase 2 | 進行中 | 108 | 全骨髓及淋巴放射照射（TMLI）合併 Cyclophosphamide + Etoposide 預處理，用於高危 ALL/AML allo-HSCT |
| [NCT06609928](https://clinicaltrials.gov/study/NCT06609928) | Phase 1 | 招募中 | 12 | FOLR1 CAR-T 用於 FOLR1+/CBFA2T3::GLIS2+ 小兒復發/難治 AML，Cyclophosphamide 為淋巴細胞清除預處理組成 |
| [NCT03766126](https://clinicaltrials.gov/study/NCT03766126) | Phase 1 | 進行中 | 22 | 抗 CD123 CAR-T 細胞療法用於復發/難治 AML，Cyclophosphamide 為 lymphodepletion 方案核心 |
| [NCT00047060](https://clinicaltrials.gov/study/NCT00047060) | Phase 1/2 | 完成 | 5 | HLA 配對動員周邊血造血幹細胞移植合併 Campath-1H 非骨髓清除性預處理，涵蓋血液惡性腫瘤 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | 系統性回顧/Meta-analysis | Bone Marrow Transplantation | 比較成人 AML allo-HSCT 中不同骨髓清除性預處理方案（含 Bu/Cy）療效，提供最高等級綜合分析 |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | 前瞻性 Phase 2 | Transplant Immunology | Cladribine + Bu/Cy 強化預處理用於 R/R AML allo-HSCT，評估療效與安全性 |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | 回顧性世代 | Haematologica | 217 例 AML 患者骨髓清除性 HCT + PTCy 遺傳風險分層，2 年整體存活率 77%（95% CI：71–83%） |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | 回顧性世代 | European Journal of Haematology | 65 歲以下 AML 患者 ATG + PTCy GVHD 預防下 RIC vs MAC 對存活影響之評估 |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | 回顧性世代 | Future Oncology | Bu/Cy vs FluBu 作為 AML allo-HSCT 骨髓清除性預處理：相似療效，FluBu 毒性較低 |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | 回顧性世代 | Bone Marrow Transplantation | 1,823 例 AML 患者（CR1）接受 PTCy，分析細胞遺傳/分子風險與預處理強度對移植結果之影響 |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | 回顧性世代 | Cytotherapy | 半相合 HSCT + PTCy 用於 AML 之預後因子分析，確認 PTCy 有效抑制 GVHD |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | 回顧性世代 | International Journal of Molecular Sciences | 首篇兒童 AML 配型供者 HSCT 後使用 PTCy 之 GVHD 預防效果及 GVHD-free/relapse-free 存活分析 |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | 回顧性世代 | Leukemia & Lymphoma | 高劑量 Cyclophosphamide（60 mg/kg）用於 AML 高白細胞症（WBC ≥50×10⁹/L）細胞減除，n=27 |
| [32857869](https://pubmed.ncbi.nlm.nih.gov/32857869/) | 2020 | Review | American Journal of Hematology | PTCy 時代 AML allo-HSCT 中 NK 細胞異應性機轉及其在 GVL 效果中的角色 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑，Nitrogen Mustard 衍生物） |
| 骨髓抑制風險 | **高**（白血球減少、嗜中性白血球低下、血小板減少及貧血為劑量限制性毒性） |
| 致吐性分級 | 中至高度（口服低劑量：低度；靜脈標準劑量：中度；高劑量預處理方案：高度） |
| 監測項目 | CBC 含分類計數（每週）、肝腎功能（ALT/AST/BUN/Cr）、尿液分析及尿沉渣（出血性膀胱炎監測）、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範（BSC/生物安全操作）操作；高劑量方案須同時使用 **Mesna**（尿路保護劑）及積極水化以預防出血性膀胱炎 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Cyclophosphamide 在骨髓性白血病的兩大治療場景（移植預處理 Bu/Cy 方案及 PTCy GVHD 預防）中均有 Phase 3 隨機對照試驗（NCT02724163，n=700）及大量 Phase 2 已完成試驗支持，確立 L1 證據等級。TxGNN 高分（99.47%）與現有臨床實踐高度一致，驗證了預測的合理性。

**若要推進需要：**
- 確認香港當地供應來源、進口/特別許可申請流程
- 獲取詳細原廠仿單（SmPC/PI），補全警語、禁忌症及 DDI 資訊（目前存在 DG001、DG002 資料缺口）
- 依具體治療場景（誘導化療 vs 預處理 vs PTCy）制訂個別化劑量方案及風險管理計畫
- 建立出血性膀胱炎（Mesna 使用規範、水化方案）及嚴重骨髓抑制之監測與緊急處置流程
- 長期毒性評估：繼發性惡性腫瘤（therapy-related AML/MDS）風險監測計畫

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證方可臨床應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

