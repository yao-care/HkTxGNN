---
layout: default
title: Insulin Detemir
parent: 高證據等級 (L1-L2)
nav_order: 400
evidence_level: L1
indication_count: 5
---

# Insulin Detemir
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

# Insulin Detemir：作用機轉本身即為第一型糖尿病基礎胰島素治療

## 一句話總結

Insulin Detemir（DB01307）是全球廣泛使用的長效基礎胰島素類似物。
本評估包中原始適應症與作用機轉資料因故缺失，但 TxGNN 模型仍以 **99.77%** 的高分預測其對**第一型糖尿病 (Type 1 Diabetes Mellitus)** 有效——
這實際上是**確認而非發現**，因為胰島素本來就是 T1DM 的標準治療藥物，
目前有 **超過 50 個臨床試驗**（多為 Phase 3 大型 RCT）與 **19 篇文獻**支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（未記錄），依藥理機轉判斷應為糖尿病基礎胰島素治療 |
| 預測新適應症 | 第一型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。但已知 Insulin Detemir 是一種以 14 碳脂肪酸醯化修飾的長效人類胰島素類似物，此修飾使其能可逆結合白蛋白，達到緩慢吸收與長達 24 小時的穩定降血糖效果，屬於**胰島素受體促效劑**，機轉上促進周邊組織葡萄糖攝取並抑制肝糖新生。

值得特別說明的是：這個案例與典型的「老藥新用」不同。第一型糖尿病並非 Insulin Detemir 的新適應症，而是它**本來就在治療**的核心適應症；本評估包中「原適應症」欄位缺失，並非藥物真的沒有已知用途，而是資料收集階段的缺口。TxGNN 的高分預測，本質上反映了知識圖譜正確捕捉到「胰島素—T1DM」這組已確立的藥理關係，可視為模型準確性的驗證，而非新發現。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | 完成 | 598 | 多國多中心 RCT，比較 detemir+aspart 與 NPH+人類胰島素在 T1DM basal-bolus 療法之血糖控制 |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | 完成 | 752 | 大型 RCT，評估 2400 nmol/mL 劑型 detemir 於 T1DM basal-bolus 療法之療效與安全性 |
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Phase 3 | 完成 | 2287 | 大型非隨機安全性研究，評估 detemir 治療胰島素依賴型 T1DM/T2DM 之安全性 |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 完成 | 350 | 兒童青少年 T1DM，比較 degludec 與 detemir 之效力與安全性（含 26 週延伸試驗） |
| [NCT01831765](https://clinicaltrials.gov/study/NCT01831765) | Phase 3 | 完成 | 1290 | FIAsp 併用 detemir vs. aspart 併用 detemir，於成人 T1DM 之療效安全性比較 |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | 完成 | 470 | 多國 RCT，detemir 用於妊娠合併 T1DM 孕婦之血糖控制與安全性 |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | 完成 | 447 | detemir+aspart vs. glargine+aspart 於 T1DM basal-bolus 療法之效力安全性比較 |
| [NCT00487240](https://clinicaltrials.gov/study/NCT00487240) | Phase 3 | 完成 | 387 | 比較胰島素 lispro 魚精蛋白懸液與 detemir 作為 T1DM 基礎胰島素之效力安全性 |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | 完成 | 330 | 12 個月雙盲 RCT，比較不同製程之 detemir 於 T1DM basal-bolus 療法之安全性 |
| [NCT00687284](https://clinicaltrials.gov/study/NCT00687284) | N/A | 完成 | 2188 | 大型觀察性研究，評估 Levemir® 作為起始胰島素治療對血糖控制之影響（斯洛伐克） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT 試驗：degludec 與 detemir（併用 aspart）於妊娠合併 T1DM 之非劣效性比較 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 系統性回顧/網絡統合分析 | Value in Health | 成人 T1DM 基礎胰島素療法之相對效力與安全性統合分析 |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | 系統性回顧/統合分析 | Pol Arch Med Wewn | Detemir 與 NPH 胰島素於 T1DM 之系統性回顧與統合分析 |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | T1DM 與 T2DM 治療更新，聚焦長效胰島素類似物 detemir |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Insulin detemir 於糖尿病管理應用之綜合回顧 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Insulin detemir 於 T1DM 與 T2DM 治療之獨特機轉與臨床應用 |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Insulin detemir 於 T1DM 與 T2DM 焦點回顧 |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Insulin detemir 於 T1DM 與 T2DM 管理應用之回顧 |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | 妊娠合併 T1DM 之生活型態、藥物治療與新科技管理更新 |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | 兒童青少年 T1DM 胰島素類似物製劑應用回顧 |

---

## 香港上市資訊

Insulin Detemir 目前**未於香港取得藥劑製品註冊證**，無許可證資料可供列示。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 第一型糖尿病此一「預測適應症」有充分的 L1 等級證據（多個大型 Phase 3 RCT、系統性回顧），但需明確認知這是對藥物**既有核心用途**的確認，而非真正的老藥新用發現。
- 藥物目前未於香港上市，若要推進需先確認正式的上市註冊路徑。

**若要推進需要：**
- 補齊 DrugBank 完整 MOA 與原始適應症資料，釐清資料缺口成因
- 取得原廠仿單警語、禁忌症與藥物交互作用資料（DG001，Blocking 等級，目前無法進入 S1 安全性初評）
- 若考慮於香港上市，需啟動藥劑製品註冊申請流程評估

**附註：** 其餘 4 個候選適應症（autoimmune oophoritis、opsismodysplasia、thiamine-responsive dysfunction syndrome、classic stiff person syndrome）皆為 L5（僅模型預測、無臨床試驗或文獻支持），研判為知識圖譜共病節點造成的間接關聯而非藥理學合理連結，建議維持 **Hold**，暫不投入資源。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

