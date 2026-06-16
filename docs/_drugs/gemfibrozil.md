---
layout: default
title: Gemfibrozil
parent: 中證據等級 (L3-L4)
nav_order: 345
evidence_level: L4
indication_count: 5
---

# Gemfibrozil
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Gemfibrozil：從高三酸甘油酯血症到類風濕性關節炎

## 一句話總結

Gemfibrozil 是 fibrate 類 PPARα 促效劑，已在國際市場廣泛用於治療高三酸甘油酯血症及混合型血脂異常。
TxGNN 模型預測其最高分適應症為**類風濕性關節炎 (Rheumatoid Arthritis)**，
目前有 **0 個臨床試驗**和 **2 篇動物模型研究**直接支持此機轉假說，整體證據屬早期探索階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高三酸甘油酯血症 / 混合型血脂異常 |
| 預測新適應症（Rank 1）| 類風濕性關節炎（Rheumatoid Arthritis）|
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Gemfibrozil 屬 fibrate 類藥物，核心機轉為活化 PPARα（過氧化物酶體增殖物活化受體 alpha），藉此抑制 VLDL 合成、降低三酸甘油酯、提升 HDL-C。雖然仿單詳細 MOA 資料目前缺乏正式記錄，但其 PPARα 促效劑特性在大量文獻中有充分佐證。

PPARα 活化的效果不僅止於代謝調節——理論上可透過抑制 NF-κB 訊號，下調 TNF-α、IL-6、IL-1β 等促炎細胞因子。類風濕性關節炎（RA）的核心病理機轉正是 TNF-α/IL-6 驅動的慢性滑膜炎，此機轉重疊構成了再利用假說的生物學基礎。

動物模型研究（PMID 30074417）在佐劑誘導性關節炎（AIA）大鼠中顯示，gemfibrozil（30 mg/kg）與減量 prednisolone 合用，效果與全量類固醇相當。同類 pan-PPAR 促效劑 bezafibrate 亦在實驗性 RA 中透過 PPARγ 活化展現抗炎效果（PMID 41207105），進一步支持 PPAR 促效劑此一藥物類別在 RA 中的機轉合理性。然而，目前尚無任何直接評估 gemfibrozil 於 RA 患者療效的人體臨床試驗，假說有待臨床驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | 動物模型 | Modern Rheumatology | Gemfibrozil 與減量 prednisolone 合用於 AIA 大鼠，療效相當於全量類固醇，支持 PPARα 促效劑的抗炎潛力 |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | 動物模型 | Int Immunopharmacol | Pan-PPAR 促效劑 bezafibrate 透過 PPARγ 活化於實驗性 RA 模型中抑制炎症路徑，確立 PPAR 類藥物的機轉共性 |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | 基礎研究 | J Immunol | NO 透過降低 Foxp3 影響調節性 T 細胞功能，揭示自體免疫病中 Treg 調控機轉（間接背景研究）|

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
現有支持證據僅限於動物模型（AIA 大鼠），尚無 RA 患者人體臨床試驗；加以 RA 已有 anti-TNF、anti-IL-6 等成熟生物製劑標準療法，Gemfibrozil 再利用的差異化定位尚不明確，優先順序較低。

**若要推進需要：**
- 補充 Gemfibrozil 完整 MOA 資料（DrugBank API）
- 設計 PoC 小型人體試驗，以 IL-6、CRP、ESR 為替代療效生物標記
- 探索 RA 合併代謝症候群族群作為初步目標人群（機轉與適應症雙重覆蓋）
- 補充香港本地仿單警語與禁忌症資料（目前未上市，須查閱原廠仿單）

---

## 其他值得關注的預測適應症

本 Evidence Pack 共涵蓋 5 個預測適應症。以下 2 項具有比 Rank 1 更強的臨床證據，建議優先評估：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 建議決策 |
|------|--------|-----------|---------|---------|------|---------|
| 3 | HIV 相關高三酸甘油酯血症 | 99.80% | L2 | 3 個（含 1 RCT）| 20 篇 | Proceed with Guardrails |
| 4 | 低 HDL 血症（Hypoalphalipoproteinemia）| 99.77% | L2 | 0 個 | 13 篇（含多項對照試驗）| Proceed with Guardrails |

以下 2 項無生物合理性支持，建議不列入研究優先順序：

| 排名 | 適應症 | 建議決策 | 原因 |
|------|--------|---------|------|
| 2 | 多發性內分泌腫瘤（MEN）| Hold | 無機轉連結；MEN1/RET 突變與 PPARα 路徑無已知關聯 |
| 5 | 短指-並指症候群 | Hold | 先天骨骼發育異常，與脂質代謝路徑無生物學關聯 |

---

### HIV 相關高三酸甘油酯血症（Rank 3 · L2 · Proceed with Guardrails）

**機轉**：Gemfibrozil 透過 PPARα 活化降低 VLDL 合成與三酸甘油酯，改善 HIV 患者接受蛋白酶抑制劑（PI）後發生的脂質代謝異常（PI-associated hyperlipidemia）。此為輔助代謝管理，非抗病毒治療。

**臨床試驗證據**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT12409741-RCT](https://pubmed.ncbi.nlm.nih.gov/12409741/)（PMID，非 NCT）| RCT | 已完成 | — | 隨機雙盲試驗直接評估 gemfibrozil 於 PI 誘導高三酸甘油酯血症的療效與安全性 |
| [NCT00474201](https://clinicaltrials.gov/study/NCT00474201) | N/A | 已完成 | 15 | 確立 lopinavir/ritonavir 顯著影響 gemfibrozil 血中濃度的 DDI 風險（核心安全性數據）|
| [NCT00039663](https://clinicaltrials.gov/study/NCT00039663) | Phase 1 | 已完成 | 75 | 確立 HIV 患者 HAART 治療後存在心血管代謝高風險，支持介入的臨床合理性 |

**關鍵文獻（精選）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12409741](https://pubmed.ncbi.nlm.nih.gov/12409741/) | 2002 | RCT | AIDS | 隨機雙盲試驗：gemfibrozil 用於 PI 相關高三酸甘油酯血症的療效與安全性 |
| [23892238](https://pubmed.ncbi.nlm.nih.gov/23892238/) | 2013 | 比較效益研究 | J Acquir Immune Defic Syndr | 大型 HIV 患者隊列中 gemfibrozil vs fenofibrate vs 魚油降三酸甘油酯效益比較 |
| [14640387](https://pubmed.ncbi.nlm.nih.gov/14640387/) | 2003 | 對照試驗 | Antiviral Therapy | Metformin 或 gemfibrozil 對 HIV PI 相關脂肪代謝異常的影響 |
| [19258558](https://pubmed.ncbi.nlm.nih.gov/19258558/) | 2009 | 世代研究 | Ann Intern Med | HIV 感染者對降脂治療反應差異分析 |
| [11371708](https://pubmed.ncbi.nlm.nih.gov/11371708/) | 2001 | 安全性報告 | AIDS | ⚠️ HIV 患者 cerivastatin + gemfibrozil 併用導致橫紋肌溶解症案例 |

> ⚠️ **關鍵安全性警示**：Lopinavir/ritonavir 等 PI 透過抑制 CYP2C8，可顯著提升 gemfibrozil 血中濃度，增加肌病及橫紋肌溶解症風險。NCT00474201 已直接量化此 DDI，臨床使用須嚴格監測 CK、肌肉症狀，並評估是否改用 fenofibrate（DDI 風險較低）。

---

### 低 HDL 血症（Hypoalphalipoproteinemia · Rank 4 · L2 · Proceed with Guardrails）

**機轉**：Gemfibrozil 透過 PPARα 活化上調 ApoA-I 和 ApoA-II 基因轉錄、促進 HDL 合成、抑制 HDL 分解代謝，使 HDL-C 水平提升。低 HDL 血症正是此機轉的核心靶點，Helsinki Heart Study 已確立 gemfibrozil 對 HDL 的提升效果與心血管事件降低的相關性。

**文獻證據（精選）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2810673](https://pubmed.ncbi.nlm.nih.gov/2810673/) | 1989 | 對照試驗 | JAMA | 22 名正常血脂但低 HDL 患者中比較 lovastatin 與 gemfibrozil；gemfibrozil 顯著提升 HDL-C |
| [10716466](https://pubmed.ncbi.nlm.nih.gov/10716466/) | 2000 | 對照試驗 | J Am Coll Cardiol | 隨機交叉研究：菸鹼酸、gemfibrozil 及聯合療法於孤立性低 HDL 血症的效益比較 |
| [8318063](https://pubmed.ncbi.nlm.nih.gov/8318063/) | 1993 | 對照試驗 | Atherosclerosis | 隨機雙盲交叉試驗：gemfibrozil 改善低 HDL + 輕度高三酸甘油酯症候群的餐後脂蛋白清除 |
| [8267492](https://pubmed.ncbi.nlm.nih.gov/8267492/) | 1994 | 對照試驗 | Arch Intern Med | 正常血脂但低 HDL 患者中 lovastatin、gemfibrozil 及菸鹼酸的脂蛋白反應比較 |
| [8736620](https://pubmed.ncbi.nlm.nih.gov/8736620/) | 1996 | 回顧 | Drugs | Gemfibrozil 藥理特性與血脂異常管理地位的系統性回顧 |

> ⚠️ **Guardrail**：需排除遺傳性低 HDL 症（Tangier disease、LCAT deficiency 等）造成的繼發性病因；在此類罕見遺傳疾病中，單純提升 HDL 數值不等同改善心血管預後。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

