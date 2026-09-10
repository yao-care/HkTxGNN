---
layout: default
title: Pantoprazole
parent: 高證據等級 (L1-L2)
nav_order: 559
evidence_level: L1
indication_count: 5
---

# Pantoprazole
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

# Pantoprazole：原適應症資料缺失 → 預測新適應症：活動性消化性潰瘍

## 一句話總結

Pantoprazole（DB00213）目前原始核准適應症資料在本檔案中缺失（香港未上市、無許可證與仿單資料），無法確認其原始標籤適應症。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前有 **3 個臨床試驗**和 **19 篇文獻**支持這個方向，其中包含多個已完成的隨機對照試驗。

> ⚠️ 需特別留意：本項證據多數描述的是 PPI（質子幫浦抑制劑）類藥物既有的消化性潰瘍/H. pylori 根除標籤內用途，而非全新機轉的老藥新用假說，詳見下方說明。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（香港未上市，無許可證/仿單資料） |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails（有條件推進） |

## 為什麼這個預測合理？

Pantoprazole 的作用機轉資料在 `drug.original_moa` 欄位標示為缺失，但根據臨床試驗與文獻佐證的機轉描述可知：Pantoprazole 是一種質子幫浦抑制劑（PPI），會不可逆地結合並抑制胃壁細胞的 H+/K+-ATPase，直接減少胃酸分泌，且相較其他 PPI 作用時間較長、在弱酸環境中較不易被活化。

由於原始適應症資料缺失，無法量化「原適應症與新適應症的相似度」。但從證據內容看，多個試驗（如 NCT02084420 的胃/十二指腸潰瘍 H. pylori 根除試驗）與文獻（duodenal ulcer、gastric ulcer healing、H. pylori eradication 相關研究）顯示，**消化性潰瘍治療與 Hp 根除輔助本來就是 PPI 類藥物的核心、標籤內用途**。也就是說，這個預測很可能是模型捕捉到 PPI 類藥物已知的藥理機轉與臨床用途，而非發現一個全新的跨適應症訊號——證據品質雖高，但「新穎性」偏低，建議在決策時將其視為安全性/療效基準驗證，而非典型老藥新用案例。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | 完成 | 323 | Ilaprazole 與 Pantoprazole 三合一療法治療 7 天，比較兩者對 H. pylori 陽性胃/十二指腸潰瘍病人之根除效果與安全性 |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | 完成 | 316 | 探討出血性消化性潰瘍病人接受內視鏡止血合併高劑量 PPI 輸注後，預測早期再出血的危險因子，作為是否需二次內視鏡之篩選標準 |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | 完成 | 320 | 評估 PPI 與 statin 對接受 PCI 併用 clopidogrel 病人抗血小板效果之交互作用影響，非直接消化性潰瘍療效終點 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | 前瞻性隨機研究比較間歇性與持續性 Pantoprazole 輸注對消化性潰瘍再出血之預防效果 |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | 內視鏡治療後併用 Pantoprazole 輸注作為輔助療法，可改善消化性潰瘍出血病人預後 |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | 比較三種 Pantoprazole 為基礎之三合一療法對 H. pylori 根除與胃潰瘍癒合的效果 |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole 併用 amoxycillin 與 azithromycin/clarithromycin 治療十二指腸潰瘍之 H. pylori 根除效果 |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | 比較 amoxycillin/clarithromycin 併用 sucralfate 或 pantoprazole 治療十二指腸潰瘍 H. pylori 根除之隨機對照試驗 |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Cohort | Hepatogastroenterology | 比較 lansoprazole 與 pantoprazole 治療活動性十二指腸潰瘍及 H. pylori 根除之療效 |
| [10228801](https://pubmed.ncbi.nlm.nih.gov/10228801/) | 1999 | 臨床研究 | Hepatogastroenterology | Pantoprazole 併用 amoxycillin、metronidazole 一週三合一療法可快速改善 H. pylori 陽性十二指腸潰瘍症狀 |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Review | Am J Gastroenterol | 系統性回顧與網絡統合分析比較 P-CAB 與 PPI 治療重度食道炎（Grade C/D）之療效與安全性 |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole 藥理總論：不可逆抑制質子幫浦、作用時間長、目前無已知藥物交互作用報告 |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | 動物實驗 | Inflammopharmacology | Pantoprazole 併用脂肪間質幹細胞可透過抗氧化、抗發炎、抗凋亡路徑促進實驗性胃潰瘍癒合 |

## 安全性考量

安全性資訊請參考原廠仿單。目前 `safety.key_warnings`、`contraindications` 及 DDI 查詢皆無有效資料，且此為 Blocking 等級資料缺口（DG001），在取得完整仿單/警語資料前無法完成安全性初評。

## 結論與下一步

**決策：Proceed with Guardrails（有條件推進）**

**理由：**
- 現有 4 篇 Phase 3 等級 RCT 及多篇 Cohort/臨床研究一致支持 Pantoprazole 於消化性潰瘍治療、H. pylori 根除及出血後預防再出血之療效，證據等級達 L1。
- 但此適應症很可能只是反映 PPI 類藥物既有的標籤內用途，而非真正的老藥新用訊號；加上香港未上市（0 張許可證）、原始適應症與 MOA 資料皆缺失，無法完整評估相似度與新穎性。

**若要推進需要：**
- 取得仿單警語與禁忌症資料，解除 DG001（Blocking）以完成 S1 安全性初評
- 補齊 DrugBank 完整 MOA 資料（DG002）
- 確認 Pantoprazole 原始核准適應症文字，釐清此候選是否為真正新增適應症
- 若目標為香港上市，需另行評估藥證申請路徑（目前無許可證）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

