---
layout: default
title: Mycophenolic Acid
parent: 僅模型預測 (L5)
nav_order: 604
evidence_level: L5
indication_count: 10
monitor_inn: "MYCOPHENOLIC ACID"
predicted_indications: ["hemoglobinopathy", "migraine disorder", "migraine with brainstem aura", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "pyropoikilocytosis, hereditary", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyruvate kinase deficiency of red cells", "rheumatoid arthritis", "antithrombin deficiency type 2"]
last_modified_at: 2026-10-28
description: "Mycophenolic Acid：預測新適應症為血紅素病變 (hemoglobinopathy)（證據等級 L5）。原適應症：本次整理的資料中，許可證未提供核准適應症文字"
---

# Mycophenolic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Mycophenolic Acid：從器官移植相關免疫抑制到血紅素病變（hemoglobinopathy）
{: .text-alpha }

## 一句話總結

Mycophenolic Acid（黴酚酸）是一種抑制 IMPDH 的免疫抑制劑，在香港已有 12 張單方許可證，但本次資料中未包含各許可證的核准適應症文字。
TxGNN 模型預測它可能對**血紅素病變 (hemoglobinopathy)** 有效。
目前有 **1 個相關性較低的臨床試驗**和 **1 篇直接相關的文獻**（地中海型貧血兒童造血幹細胞移植後的 MMF 劑量研究），整體屬於早期研究假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，許可證未提供核准適應症文字 |
| 預測新適應症 | 血紅素病變 (hemoglobinopathy) |
| TxGNN 預測分數 | 0.9960 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

**證據等級說明：** 唯一的臨床試驗（NCT02342145）測試的是 basiliximab，不是本藥。文獻（PMID 39891881）研究的是 mycophenolate mofetil（MMF，本藥的前驅藥）在移植後的藥物動力學與劑量，並未檢驗對血紅素病變本身的療效。依規則，沒有研究直接探討此疾病的療效時，等級定為 L5。

## 為什麼這個預測合理？

黴酚酸會抑制肌苷單磷酸脫氫酶（IMPDH），耗竭鳥苷核苷酸，進而抑制 T 與 B 淋巴球增殖。目前缺乏 DrugBank 的詳細作用機轉資料，上述機轉來自本次整理的文獻與分析。

血紅素病變（例如重度地中海型貧血）的主要治療之一是造血幹細胞移植，移植後需要預防移植物抗宿主病（GVHD），而 MMF/黴酚酸是常用的免疫抑制選項之一。此外，免疫機轉也可能與反覆輸血後的同種免疫反應有關。

需要注意，這個機轉只作用在免疫面，**無法矯正珠蛋白（globin）本身的缺陷**。因此，這項預測較合理的解讀是「移植輔助免疫抑制」，而非針對疾病本身的治療。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02342145](https://clinicaltrials.gov/study/NCT02342145) | Phase 4 | 完成 | 205 | 評估 basiliximab 預防重度地中海型貧血非血緣異基因造血幹細胞移植後的急性 GVHD。黴酚酸可能屬於背景用藥，並非受測藥物，僅為間接佐證 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | 世代研究 | European Journal of Drug Metabolism and Pharmacokinetics | 建立地中海型貧血兒童造血幹細胞移植後 MMF 的族群藥物動力學模型，並模擬建議劑量；屬於仿單外使用的劑量研究，未評估疾病療效 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51396 | MYFORTIC GASTRO-RESISTANT TAB 180MG | 未提供 | 未提供 |
| HK-51397 | MYFORTIC GASTRO-RESISTANT TAB 360MG | 未提供 | 未提供 |
| HK-65062 | APO-MYCOPHENOLIC ACID ENTERIC COATED TABLETS 180MG | 未提供 | 未提供 |
| HK-65235 | ACCORD MYCOPHENOLIC ACID GASTRO-RESISTANT TABLETS 180MG | 未提供 | 未提供 |
| HK-67224 | MOFECON-GR 180 GASTRO-RESISTANT TABLETS 180MG | 未提供 | 未提供 |

以上僅列出 12 張有效單方許可證中的 5 張，其餘包括 Myfortic 另外 2 張、Apo-Mycophenolic Acid 360mg、Accord 360mg、DCH Auriga 180/360mg 及 Mofecon-GR 360。

## 安全性考量

**藥物交互作用**（共查得 100 筆，以下列出部分）：

- **嚴重（Major）**：活性碳（Activated charcoal）
- **中度（Moderate）**：抗生素類（doxycycline、amoxicillin、clarithromycin、minocycline、tetracycline、vancomycin、kanamycin、paromomycin、levofloxacin、metronidazole）；含鋁、鎂、鈣的制酸劑（aluminum hydroxide、magnesium oxide、magnesium hydroxide、magnesium carbonate、magaldrate、calcium carbonate）
- **輕微（Minor）**：鋅（zinc sulfate、zinc acetate）、鐵

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何研究直接驗證黴酚酸對血紅素病變本身的療效，現有證據僅是移植情境下的劑量研究與間接試驗，屬於研究假說層級（L5）。
- 作用機轉僅涉及免疫抑制，無法處理珠蛋白缺陷，且預測清單中多數其他條目（如偏頭痛、紅血球酵素缺乏症）缺乏任何機轉或臨床支持。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌症，並補齊 DrugBank 的作用機轉資料
- 明確界定研究問題：是否專指地中海型貧血造血幹細胞移植後的 GVHD 預防
- 收集 MMF/黴酚酸在該族群的對照性臨床研究（療效與安全性）
- 評估移植族群的感染風險、骨髓抑制與藥物交互作用監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

