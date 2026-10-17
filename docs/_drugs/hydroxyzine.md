---
layout: default
title: Hydroxyzine
parent: 中證據等級 (L3-L4)
nav_order: 449
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Hydroxyzine：預測新適應症為過敏性蕁麻疹 (Allergic Urticaria)（證據等級 L4）。原適應症：異位性皮膚炎、過敏性鼻炎、蕁麻疹、血管性水腫等"
---

# Hydroxyzine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Hydroxyzine：從過敏性皮膚與呼吸道疾病到過敏性蕁麻疹

## 一句話總結

Hydroxyzine 是第一代 H1 受體拮抗劑，原本用於異位性皮膚炎、過敏性鼻炎、蕁麻疹及血管性水腫等過敏性疾病。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效，
目前**無臨床試驗**登記，但有 **18 篇文獻**（多為抗組織胺類別的綜述）支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 異位性皮膚炎、過敏性鼻炎、蕁麻疹、血管性水腫等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold（過敏性蕁麻疹）；備選方向「寒冷性蕁麻疹」可 Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未收錄）。就已知的藥理分類，Hydroxyzine 是第一代 H1 受體拮抗劑（反向促效劑）。過敏性蕁麻疹的風團與紅暈，主要由肥大細胞釋放組織胺所驅動，因此阻斷 H1 受體在機轉上直接對應。

蕁麻疹與血管性水腫本來就在 Hydroxyzine 的原適應症清單中，所以這項預測較接近既有適應症的延伸，而非全新的治療方向。

需要注意：目前文獻多為抗組織胺類別的綜述，且不少討論的是它的活性代謝物 cetirizine 或其他藥物，並非 Hydroxyzine 本身的試驗。此外，近年立場聲明（如 CSACI 2019）建議新一代抗組織胺因安全性較佳，應作為過敏性鼻炎與蕁麻疹的第一線用藥。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下表依優先順序列出較相關者（以 Review 為主，無 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | 慢性自發性蕁麻疹以抗組織胺為起點，過去曾使用 hydroxyzine 等第一代藥物，劑量常需高於過敏性鼻炎 |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Review | Allergy Asthma Clin Immunol | 立場聲明：第一代抗組織胺（含 hydroxyzine）有鎮靜、認知受損等副作用，新一代應為首選 |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | 回顧第一代與新一代口服抗組織胺用於過敏性鼻炎與慢性特發性蕁麻疹的療效與安全性 |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | H1 拮抗劑對兒童過敏性鼻結膜炎有一級證據支持 |
| [10582734](https://pubmed.ncbi.nlm.nih.gov/10582734/) | 1999 | Review | Ann Allergy Asthma Immunol | 彙整 cetirizine（Hydroxyzine 代謝物）在皮膚疾病的療效與安全性 |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | 藥理與臨床回顧 | Drugs | Loratadine 與 hydroxyzine 等藥物在對照研究中療效相當 |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case report | J Clin Gastroenterol | Cetirizine 引起膽汁鬱滯的個案（安全性訊號，非療效證據） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48205 | POLIZINE TAB 10MG | 錠劑 | 未載明 |
| HK-58686 | ALLERAX-FC TAB 10MG | 錠劑 | 未載明 |
| HK-48897 | HYDROXYZINE TAB 25MG | 錠劑 | 未載明 |
| HK-43483 | APO-HYDROXYZINE CAP 25MG | 膠囊 | 未載明 |
| HK-49038 | HYDROXYZINE TAB 10MG | 錠劑 | 未載明 |

以上為 11 張有效許可證中的 5 張，均為單方製劑，無已註銷者。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單文字）：高血壓、癲癇、肝病、膽囊疾病、甲狀腺功能低下或亢進、消化性潰瘍、開角型與閉角型青光眼、精神疾病、糖尿病、良性前列腺增生、物質濫用或依賴、冠狀動脈疾病、心肌梗塞、心臟傳導疾病、心臟猝死及其他心血管疾病。
- **藥物交互作用**：共查得 100 筆，以下為主要的 Major 等級：
  - Morphine
  - Potassium citrate
  - Dolasetron
  
  另有多筆 Moderate 等級，如抗膽鹼藥（Atropine、Hyoscyamine、Dicyclomine、Trospium）、Clarithromycin、Levofloxacin 等。
- **文獻提示的風險**：鎮靜、抗膽鹼負擔、QT 延長風險，以及老年與兒童劑量需特別留意。

完整警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold（針對「過敏性蕁麻疹」）**

**理由：**
- 過敏性蕁麻疹的預測分數很高，機轉也合理，但目前沒有任何臨床試驗，文獻多為類別綜述或 cetirizine 相關資料，缺乏 Hydroxyzine 專屬的直接證據（證據等級 L4）。此外，蕁麻疹本已是既有適應症，新增價值有限，且新一代抗組織胺為首選。
- 同一份預測中，**寒冷性蕁麻疹 (Cold Urticaria)** 的證據較佳（L3）：有 1984 年比較 hydroxyzine 與其他藥物的雙盲研究（PMID 6480953）及單一病人研究（PMID 475987），可考慮以 Proceed with Guardrails 方式作為優先探索方向。其餘預測（酒糟性結膜炎、頑固型異位性皮膚炎、異位性 IgE 反應性）僅有模型分數，建議 Hold。

**若要推進需要：**
- 取得 Hydroxyzine 專屬的作用機轉資料（MOA）
- 取得香港許可證的核准適應症文字與仿單警語、禁忌症
- 設計或檢索 Hydroxyzine 對蕁麻疹的對照試驗，並與新一代抗組織胺做比較
- 建立安全性監測計畫，涵蓋鎮靜、抗膽鹼作用、QT 延長，以及老年與兒童族群的劑量
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

