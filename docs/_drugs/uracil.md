---
layout: default
title: Uracil
parent: 中證據等級 (L3-L4)
nav_order: 918
evidence_level: L3
indication_count: 10
---

# Uracil
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Uracil：從（原適應症未登載）到大腸腫瘤

## 一句話總結

Uracil（尿嘧啶）是 UFT（tegafur-uracil）複方的調節成分，在香港有 2 張有效許可證。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效。
目前有 1 個臨床試驗登記（與 uracil 無直接關聯）和 20 篇文獻，其中多數證據針對 tegafur-uracil 複方，**並非 uracil 單方**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明核准適應症 |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails（僅限複方 UFT 的研究方向） |

---

## 為什麼這個預測合理？

目前缺乏 uracil 本身詳細的作用機轉資料。根據已知資訊，uracil 是 UFT（tegafur-uracil）複方中的調節成分。Tegafur 是 5-FU 的前驅藥，uracil 則競爭性抑制二氫嘧啶去氫酶（DPD），減緩 5-FU 的分解，使腫瘤組織中的 5-FU 暴露量上升。

因此，支持大腸腫瘤的證據**屬於複方，而非 uracil 單方**。Uracil 單獨使用並無已確立的抗腫瘤活性。此外，uracil 啟動的鹼基切除修復，以及葉酸/維生素 B12 相關的 uracil 錯誤嵌入，可作為大腸致癌過程的生物學背景，但並非直接的療效證據。

TxGNN 預測的其他疾病中，良性病變（如結腸脂肪瘤、淋巴管瘤、血管瘤、平滑肌瘤）缺乏細胞毒性化療的合理依據，高分可能反映圖譜上的鄰近關係，而非生物學意義。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04164069](https://clinicaltrials.gov/study/NCT04164069) | Phase 1 | 完成 | 9 | Dasatinib 預防 FOLFOX 引起的神經病變；未測試 uracil 或 UFT，僅與大腸癌情境有間接關聯 |

此登記試驗與 uracil 無直接關係，不能視為支持證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29677641](https://pubmed.ncbi.nlm.nih.gov/29677641/) | 2018 | RCT | Eur J Cancer | SACURA 試驗：口服 UFT 一年輔助化療 vs 單純手術，用於 II 期結腸癌 |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT（Phase III） | Clin Colorectal Cancer | ACTS-CC 02：SOX 對比 UFT/LV 用於高風險 III 期結腸癌輔助治療 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | Phase III（5 年更新） | ESMO Open | SOX 在 DFS 上未優於 UFT/LV；報告最終 OS 與分期亞組分析 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 世代研究與統合分析 | Medicine | 台灣全國資料庫：比較 UFT 與 5-FU 用於 II/III 期結腸癌術後輔助化療 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | OK-432 免疫化療與 HCFU、UFT 口服嘧啶類的組合用於大腸直腸癌輔助治療 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT 作為肺、胃、大腸、乳房癌術後輔助化療的臨床證據與機轉 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | 共識指引 | Clin Colorectal Cancer | 亞洲轉移性大腸直腸癌治療指引調適 |
| [16111469](https://pubmed.ncbi.nlm.nih.gov/16111469/) | 2005 | Review | Expert Rev Anticancer Ther | 結腸癌各分期的化療選擇 |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | 病例報告 | Cancer Chemother Pharmacol | 轉移性結腸癌患者使用 UFT 後發生溶血性貧血 |
| [11554295](https://pubmed.ncbi.nlm.nih.gov/11554295/) | 2001 | 前臨床/機轉 | Prog Nucleic Acid Res Mol Biol | 人類大腸腺癌 LoVo 細胞萃取物中 uracil 啟動的鹼基切除修復合成保真度 |

文獻中的療效證據均針對 UFT 複方（tegafur + uracil），不能直接推論至 uracil 單方。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48265 | UNITORAL CAP | 膠囊（依品名推定，資料未載明） | 資料未載明 |
| HK-60904 | UFUR CAP | 膠囊（依品名推定，資料未載明） | 資料未載明 |

兩張皆為單方、有效狀態。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物複方（Fluoropyrimidine 類，UFT 中的 tegafur 為 5-FU 前驅藥；uracil 為 DPD 抑制調節劑） |
| 骨髓抑制風險 | 請參考原廠仿單；文獻有 UFT 引起溶血性貧血的病例報告 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 建議監測 CBC（含分類）、肝腎功能 |
| 處置防護 | 請參考原廠仿單與細胞毒性藥物處置規範 |

---

## 安全性考量

- **藥物不良反應個案**：文獻曾報告一例轉移性結腸癌患者使用 UFT 後發生溶血性貧血。

其餘警語、禁忌症與藥物交互作用資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 大腸癌方向有多項 UFT 複方的 RCT 與世代研究（如 SACURA、ACTS-CC 02），但證據針對 tegafur-uracil 複方，uracil 單方並無抗腫瘤活性依據；故證據等級為 L3，僅宜視為研究問題。
- 其他預測疾病（直腸乙狀結腸交界腫瘤、胃癌以外的良性結腸病變等）證據薄弱，應暫緩（Hold）。胃癌方向有 Phase II 及 SAMIT Phase III 對 UFT 的研究，但多為較早期資料，且登記試驗未測試 uracil。

**若要推進需要：**
- 釐清兩張許可證（UNITORAL、UFUR）的核准適應症與成分組成，確認是否為 tegafur-uracil 複方
- 取得香港衞生署核准仿單，補齊警語、禁忌症與交互作用資料
- 補充 uracil 的作用機轉資料
- 明確將研究問題界定為「UFT 複方」而非「uracil 單方」，並篩選直接測試 UFT 的試驗
- 針對 DPD 活性相關風險建立安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

