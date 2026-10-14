---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 805
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Selpercatinib：從 RET 相關癌症到肺高壓

## 一句話總結

Selpercatinib 是選擇性 RET 激酶抑制劑，在香港以 RETSEVMO 品名上市。
TxGNN 模型預測它可能對**肺高壓 (Pulmonary Hypertension)** 有效，但目前**沒有臨床試驗**，檢索到的 3 篇文獻也都與肺高壓無直接關聯，證據僅限於模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症 |
| 預測新適應症 | 肺高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Selpercatinib 是一種高度選擇性的 RET 激酶抑制劑，檢索到的文獻顯示其用於 RET 驅動的癌症（RET 融合陽性非小細胞肺癌、多發性內分泌腫瘤 2B 型的甲狀腺髓質癌）。

目前資料中並未建立 RET 抑制與肺血管重塑之間的機轉路徑。過去曾有帶有 PDGFR 等其他標靶的多激酶抑制劑被探索用於肺動脈高壓，但 Selpercatinib 對 RET 的選擇性很高，這類經驗無法直接套用。

因此，0.99 的預測分數目前只能視為模型在知識圖譜上的關聯訊號，尚無生物學或臨床證據支持。

其他預測的新適應症（偏頭痛 99.17%、腦幹先兆偏頭痛 99.05%）同樣沒有任何臨床試驗或文獻，也同為 L5、Hold。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | 回溯性分析 | Ther Adv Med Oncol | 透過用藥可近計畫治療的 RET 融合陽性非小細胞肺癌真實世界療效分析（與肺高壓無關） |
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | 真實世界藥物警戒研究 | Front Pharmacol | 以 FDA 不良事件通報系統比較 pralsetinib 與 selpercatinib 的不良事件差異 |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | 個案報告 | Cureus | RET M918T 突變 MEN2B 轉移性甲狀腺髓質癌的長期管理與標靶治療挑戰 |

以上文獻皆非針對肺高壓，應是僅因藥名被檢索到，不能作為支持新適應症的證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67999 | RETSEVMO CAPSULES 40MG | 未載明 | 未載明 |
| HK-68000 | RETSEVMO CAPSULES 80MG | 未載明 | 未載明 |

兩張許可證皆為單方、有效，持證商為 ELI LILLY ASIA, INC.。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（選擇性 RET 激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共有 100 筆交互作用紀錄，以下為部分列出的項目：
  - **重大 (Major)**：Famotidine、Ranitidine、Cimetidine、Omeprazole、Rabeprazole、Dexlansoprazole（制酸劑／氫離子幫浦抑制劑類）、Aprepitant、Dexamethasone、Clarithromycin、Magnesium oxide
  - **中度 (Moderate)**：Hydrocortisone、Triamcinolone、Betamethasone、Budesonide、Pioglitazone、Saxagliptin、Loperamide、Bisacodyl、Polyethylene glycol

其餘警語與禁忌症資料缺漏，請參考原廠仿單。對於肺高壓或偏頭痛這類慢性非致命疾病，如此大量的交互作用，加上此類藥物已知的安全負擔，使風險效益評估明顯不利。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 肺高壓預測僅來自 TxGNN 圖譜分數，無臨床試驗，文獻亦與肺高壓無關，證據等級為 L5。
- RET 抑制與肺血管病變之間沒有已建立的機轉連結，且藥物交互作用多，用於非腫瘤適應症的風險效益不佳。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並評估 RET 訊號與肺血管重塑的生物學關聯
- 取得前臨床研究（如肺高壓動物模型或細胞實驗）證據
- 取得香港衛生署核准適應症與仿單中的警語、禁忌症
- 完整評估安全性（特別是心血管與藥物交互作用），再決定是否進入下一階段
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

