---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Basiliximab：預測新適應症為漿細胞骨髓瘤 (Plasma Cell Myeloma)（證據等級 L5）。原適應症：資料中未載明"
---

# Basiliximab
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

# Basiliximab：從器官移植排斥反應預防到多發性骨髓瘤（漿細胞骨髓瘤）

## 一句話總結

Basiliximab 是一種抗 CD25（IL-2 受體 α 鏈）單株抗體，在香港已有上市許可證，但本次資料中未載明核准適應症文字。
TxGNN 模型預測它可能對**漿細胞骨髓瘤 (Plasma Cell Myeloma)** 有效，目前有 **3 個臨床試驗**和 **4 篇文獻**與此方向相關。
不過這些證據多屬「移植輔助／免疫調節」性質，而非直接的抗骨髓瘤療效。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明（香港許可證未提供核准適應症文字） |
| 預測新適應症 | 漿細胞骨髓瘤 (Plasma Cell Myeloma) |
| TxGNN 預測分數 | 95.61% |
| 證據等級 | L2（依資料編譯時的評分；僅有 Phase 2 小型研究，且為 GVHD 預防終點，實質證據偏弱） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold（列為研究性問題，暫不推進） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 未取得）。不過依已知資訊，Basiliximab 是抗 CD25 單株抗體，可阻斷活化 T 細胞上的 IL-2 受體 α 鏈，因此能耗竭活化 T 細胞與調節性 T 細胞 (Treg)。

在骨髓瘤情境中，這個機轉有兩種用法：
1. **異體移植後預防 GVHD**：在非清髓性異體移植中，以 basiliximab 耗竭活化 T 細胞。
2. **自體移植後免疫調節**：自體幹細胞移植後 Treg 會快速重建並抑制抗骨髓瘤免疫，耗竭 Treg 理論上可增強抗腫瘤免疫。

需要強調的是，這兩種連結都屬於**支持性照護／免疫調節**，並非直接殺傷骨髓瘤細胞。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | 完成 | 17 | Basiliximab 加 cyclosporine 於非清髓性異體移植預防 GVHD；族群含骨髓瘤，為小型單臂研究，終點非骨髓瘤控制 |
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | 完成 | 30 | 骨髓瘤自體幹細胞移植中以 basiliximab 耗竭 Treg 的先導試驗，評估可行性與安全性，無療效結論 |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | NA | 提前終止 | 10 | 同為 T 細胞耗竭預防 GVHD，樣本極小且提前終止，可解讀性低 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | 世代研究 | Bone Marrow Transplant | 17 位類固醇難治性急性 GVHD 患者（含 1 位多發性骨髓瘤）使用 basiliximab，耐受性良好且有效 |
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | 先導世代研究 | J Immunother Cancer | 骨髓瘤自體移植後耗竭 Treg 的先導研究，探討移植後免疫功能失調 |
| [42379467](https://pubmed.ncbi.nlm.nih.gov/42379467/) | 2026 | 病例報告/回顧 | Am J Kidney Dis | CAR-T 治療後骨髓瘤患者接受腎臟移植，屬移植情境討論 |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | 病例報告 | Am J Kidney Dis | 4 位骨髓瘤所致腎衰竭患者接受腎臟移植的經驗 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44725 | SIMULECT POWDER FOR INJ 20MG（Novartis） | 注射用粉劑 | 資料中未載明 |

---

## 安全性考量

- **藥物交互作用**：共查得 69 筆交互作用，其中主要需留意：
  - **嚴重 (Major)**：Adalimumab、Baricitinib、Certolizumab pegol、卡介苗（BCG，Tice 株活菌）等免疫抑制劑或活疫苗，合用會加重免疫抑制與感染風險。
  - **中度 (Moderate)**：Azathioprine、Alemtuzumab、Anakinra、Canakinumab、Alefacept、Roflumilast，以及多種疫苗（破傷風類毒素、炭疽疫苗、腺病毒疫苗、霍亂活疫苗等）。
  - **輕微 (Minor)**：各種鋅鹽類。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據都是 GVHD 預防或 Treg 耗竭的支持性／免疫調節用途，沒有顯示直接抗骨髓瘤療效的研究。試驗規模小（10–30 人），且為 Phase 1／2 或提前終止，雖然評分為 L2，實質證據強度偏弱。
- 此外，免疫抑制本身可能影響抗腫瘤免疫，且與多種免疫抑制劑和活疫苗有嚴重交互作用。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料與香港仿單（核准適應症、警語、禁忌症）。
- 針對骨髓瘤設計以腫瘤控制、無惡化存活期為終點的對照試驗。
- 追蹤 NCT01526096 的免疫與臨床結果，確認 Treg 耗竭是否帶來實質益處。
- 明確界定用途（移植支持性照護 vs. 抗腫瘤免疫調節），再決定是否推進。

**其他預測適應症補充：**
- **血紅素病變 (Hemoglobinopathy)**：有 Phase 4 試驗（NCT02342145，n=205，已完成；NCT03171831，n=30）顯示 basiliximab 用於地中海型貧血異體移植的 GVHD 預防，但其效益在移植情境，而非治療疾病本身。
- **支氣管炎、胃癌等**：證據多為肺移植排斥或偶發性病例報告，推測是本體論比對的假象，不建議推進。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

