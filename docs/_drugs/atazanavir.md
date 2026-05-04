---
layout: default
title: Atazanavir
parent: 高證據等級 (L1-L2)
nav_order: 65
evidence_level: L1
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L1** | 預測適應症: **6** 個
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

# Atazanavir：從 HIV 感染到 AIDS 相關複合症

> ⚠️ 本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選需經過臨床驗證才能應用。

---

## 一句話總結

Atazanavir 是一種 HIV-1 蛋白酶抑制劑，廣泛用於成人及兒童 HIV 感染的抗病毒治療方案中。
TxGNN 模型在本次多適應症分析（6 個預測）中，以 **AIDS 相關複合症 (AIDS Related Complex)** 的臨床證據最為完整，目前有 **2 個已完成的 Phase 3 臨床試驗**及 **3 篇文獻**直接支持；此外模型亦識別出**先天性 HIV 感染**（L3，Research Question）等具研究潛力的延伸適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（抗病毒治療方案，蛋白酶抑制劑類別） |
| 主要預測適應症 | AIDS 相關複合症 (AIDS Related Complex) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 查詢存在資料缺口）。根據已知資訊，Atazanavir（DrugBank ID：DB01072）屬 HIV-1 蛋白酶抑制劑類別，透過直接抑制 HIV 蛋白酶的催化活性，阻斷 HIV 多蛋白前體（Gag-Pol polyprotein）的切割步驟，使新產生的病毒粒子無法成熟為具感染性形態，從而在複製週期後期抑制病毒擴散。

AIDS 相關複合症（ARC）是 HIV 感染由慢性無症狀期進展至 AIDS 的中間臨床階段，以 CD4+ T 細胞計數持續下降、體重減輕、慢性腹瀉、淋巴結腫大等全身症狀為特徵，但尚未達到 CDC 定義的 AIDS 診斷標準。ARC 的核心病理機制即是持續的 HIV 複製導致免疫系統逐漸耗竭——與 Atazanavir 的抗病毒機轉高度吻合。

此預測實質上是 Atazanavir 在 HIV 疾病連續譜（HIV disease continuum）不同臨床分期上的「延伸適應症」。NCT00035932（Phase 3，開放標籤）標題直接包含 Atazanavir（BMS-232632），評估 ATV 聯合 RTV 或 SQV 在治療有經驗 HIV 感染者中的抗病毒效果，達到 L1 直接臨床證據等級，機轉合理性充分。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | 完成 | 571 | 評估 Atazanavir (BMS-232632) 聯合 Ritonavir 或 Saquinavir 搭配 TDF 及核苷類藥物，對比 LPV/RTV 方案在治療有經驗 HIV 感染者的抗病毒療效；為最直接的 ATV Phase 3 證據 |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | 完成 | 82 | 前瞻性單臂開放標籤國際多中心研究（PRINCE I），評估 ATV 粉末劑型聯合 RTV 在 3 個月至 6 歲 HIV 感染兒童中的安全性、療效及藥代動力學 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | 觀察性世代研究 | J Acquir Immune Defic Syndr | 分析常用 cART 方案對 AIDS 定義性神經系統疾病發生率的差異影響，提供 ART 方案在 AIDS 進程防治中的比較效益資料，與 ARC 進展管理直接相關 |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | 基礎研究（In vitro） | Antimicrob Agents Chemother | 新一代 CNS 靶向 HIV 蛋白酶抑制劑（GRL-08513/08613）對多重耐藥 HIV-1 株具強效抗病毒活性，提供蛋白酶抑制劑類藥物機轉改良的背景資料 |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | 觀察性研究 | AIDS Reviews | 分析 HIV 感染者及 ART 治療者的胃腸道不良事件風險因子，與 ARC 常見的消化道症狀鑑別診斷及 ATV 耐受性評估相關 |

---

## 香港上市資訊

Atazanavir 目前在香港**未有上市許可**（許可證數：0），無相關登記資料可供查閱。若有臨床使用需求，須透過香港衛生署特殊用藥申請途徑辦理，並評估是否可取得已於其他司法管轄區核准之製劑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意：** 本次分析未能取得完整的警語、禁忌症及藥物交互作用資料（均為資料缺口）。Atazanavir 屬 HIV 蛋白酶抑制劑，臨床上需特別注意其與 CYP3A4 代謝途徑相關藥物的交互作用風險，正式評估前務必查閱完整仿單。

---

## 其他 TxGNN 預測適應症概覽

本次為多適應症分析（candidate_id: TW-DB01072-multi），共識別 6 個預測適應症，以下為完整概覽：

| 排名 | 疾病名稱 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|------|---------|-----------|---------|------|------|
| 6 | AIDS 相關複合症 (ARC) | 99.71% | **L1** | **Proceed with Guardrails** | 2 個 Phase 3 臨床試驗直接涉及 ATV，機轉直接相關 |
| 5 | 先天性 HIV 感染 (Congenital HIV) | 99.71% | L3 | Research Question | 有多項 ATV PK/安全性兒科研究（PRINCE I/II），需評估新生兒特殊藥代動力學 |
| 1 | 猴免疫缺乏病毒感染 (SIV) | 99.98% | L4 | Hold | 非人類靈長類研究範疇，交叉抑制活性需獨立實驗確認，不適用於人類臨床開發 |
| 2 | 貓愛滋病 (Feline AIDS) | 99.98% | L5 | Hold | 獸醫適應症，FIV 蛋白酶結構（尤其活性位點 flap 區域）與 HIV-1 差異顯著，無任何體外/體內抑制數據 |
| 3 | 神經發育障礙（無語言、共濟失調步態） | 99.98% | L5 | Hold | 無生物學機轉連結，高 TxGNN 分數可能源於知識圖譜白質異常節點的拓撲鄰近雜訊 |
| 4 | 廢棄家族性混合型高脂血症 | 99.82% | L5 | Hold | 疾病分類已廢棄（obsolete）；且 PI 類藥物本身為血脂異常已知風險因子，存在反向安全疑慮 |

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
AIDS 相關複合症（ARC）為 HIV 感染自然病程的一部分，Atazanavir 作為 HIV-1 蛋白酶抑制劑，機轉完全針對 ARC 的致病根源（持續 HIV 複製導致的免疫耗竭）。已有 Phase 3 直接試驗（NCT00035932，571 人）以 ATV 為主要研究藥物，達 L1 最高證據等級，推進基礎紮實。香港未上市為主要監管障礙，需透過特殊途徑解決。

**若要推進需要：**
- **監管路徑**：評估香港衛生署特殊用藥申請的可行性，或尋求在港上市途徑
- **MOA 補全**：查詢 DrugBank API 補充完整作用機轉資料，強化機轉合理性文件
- **安全性評估**：獲取完整仿單資料，重點評估 CYP3A4 相關 DDI、腎結石風險（高膽紅素血症）及與胃酸抑制劑的交互作用
- **延伸評估（先天性 HIV）**：若同時考慮 Congenital HIV 適應症，需深入分析 PRINCE I（NCT01099579）及 PRINCE II（NCT01335698）的完整 PK 與安全性資料，以確認兒科用藥方案
- **現實定位**：鑑於目前 HIV 治療已高度標準化（整合酶抑制劑為主流），需評估 ATV 相對於當代方案（如 DTG、BIC 基礎方案）的定位與競爭優勢
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

