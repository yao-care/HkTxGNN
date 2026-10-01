---
layout: default
title: Insulin Detemir
parent: 高證據等級 (L1-L2)
nav_order: 463
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

# Insulin Detemir：預測新適應症為第 1 型糖尿病（實為標籤內用途）

## 一句話總結

Insulin Detemir（商品名 Levemir）是長效基礎胰島素類似物，在香港已有 3 張上市許可證。
TxGNN 預測它對**第 1 型糖尿病 (Type 1 Diabetes Mellitus)** 有效，目前有 **50 個臨床試驗**和 **19 篇文獻**支持。
但這項適應症本來就是藥物的既有用途，應視為模型的陽性對照，不算新的老藥新用發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 第 1 型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位為空）。文獻摘要提供了以下說明：Insulin Detemir 是以 14 碳脂肪酸修飾的可溶性長效人類胰島素類似物。脂肪酸使它能可逆地結合白蛋白，吸收因此變慢，代謝作用可持續最長約 24 小時。它與胰島素受體結合，補充第 1 型糖尿病患者缺少的內源性胰島素。

第 1 型糖尿病的核心問題是胰島 β 細胞無法分泌足夠的胰島素，需要終身補充。基礎胰島素類似物正是為此設計，與 NPH 胰島素相比，藥效變異較小，夜間低血糖風險也較低。因此這個預測的機轉合理，並與藥物的既有用途一致。

原始適應症資料（`original_indications`）與香港許可證的核准適應症文字皆為空白，屬於來源資料缺漏，不代表這是新用途。發布前應先到香港衞生署資料庫確認實際的核准適應症。

---

## 臨床試驗證據

以下列出最相關的 10 項，另有 40 項未列出。多數為第 3 期隨機對照試驗，直接比較 Insulin Detemir 與其他基礎胰島素。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | 完成 | 752 | 6 個月開放標籤平行試驗，比較 Detemir 與 NPH 胰島素在基礎－餐時療法中的療效與安全性 |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | 完成 | 598 | Detemir＋Aspart 對比 NPH＋人類可溶性胰島素，比較血糖控制 |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 完成 | 350 | 兒童與青少年 26 週試驗，Degludec 對比 Detemir（Detemir 為對照組） |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | 完成 | 330 | 12 個月雙盲試驗，比較新舊兩種製程生產的 Detemir 之安全性與療效 |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | 完成 | 447 | Detemir 對比 Glargine（均搭配 Aspart），檢驗 Detemir 是否至少同樣有效且安全 |
| [NCT00487240](https://clinicaltrials.gov/study/NCT00487240) | Phase 3 | 完成 | 387 | Lispro 魚精蛋白懸液（ILPS）對比 Detemir，用於第 1 型糖尿病基礎－餐時療法 |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | 完成 | 470 | 第 1 型糖尿病孕婦，Detemir 對比 NPH 胰島素的血糖控制與安全性 |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | 完成 | 114 | 成人第 1 型糖尿病，Detemir＋Aspart 對比 NPH＋Aspart |
| [NCT00605137](https://clinicaltrials.gov/study/NCT00605137) | Phase 3 | 完成 | 83 | 日本兒童第 1 型糖尿病，Detemir 與 NPH 的安全性 |
| [NCT01461616](https://clinicaltrials.gov/study/NCT01461616) | Phase 3 | 完成 | 19 | 三交叉試驗，觀察對 IGFBP-1 與 IGF-I 的影響；屬機轉性結果，不能直接證明臨床療效 |

---

## 文獻證據

以下列出最相關的 10 篇，優先列出隨機對照試驗，其次為系統性回顧，最後為綜述。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT 試驗：第 1 型糖尿病孕婦中，比較 Degludec 與 Detemir（均搭配 Aspart）的療效與安全性，採非劣性設計 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 系統性回顧／統合分析 | Clin Ther | 比較 Degludec 與 Glargine、Detemir 等長效基礎胰島素在第 1、2 型糖尿病的療效與耐受性 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 系統性回顧／網絡統合分析 | Value Health | 評估成人第 1 型糖尿病各基礎胰島素方案的相對療效與安全性 |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | 系統性回顧／統合分析 | Pol Arch Med Wewn | 比較 Detemir 與 NPH 在第 1 型糖尿病的血糖控制；先前研究的獲益並非各研究一致 |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | 綜述 | Drugs | 說明 Detemir 為基礎胰島素，藥效延長來自自我聚合與白蛋白結合；血糖鉗夾試驗中，藥效變異小於 NPH |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | 綜述 | Drugs | Detemir 的療效比 NPH 更可預測、更持久，個體內變異較小 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | 綜述 | Vasc Health Risk Manag | Detemir 藥動學變異較小，可降低低血糖（尤其夜間低血糖）風險 |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | 綜述 | Vasc Health Risk Manag | 與 NPH 比較，HbA1c 無顯著差異，低血糖率較低 |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | 綜述 | Lancet Diabetes Endocrinol | 更新第 1 型糖尿病孕期管理，包括生活方式、藥物治療與新型技術 |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | 綜述 | Paediatr Drugs | 胰島素類似物在兒童與青少年第 1 型糖尿病的使用 |

---

## 香港上市資訊

許可證資料中的劑型與核准適應症文字皆為空白，僅能列出以下資訊：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65011 | LEVEMIR FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | NOVO NORDISK HONG KONG LIMITED |
| HK-53538 | LEVEMIR FLEXPEN INJ 100U/ML | NOVO NORDISK HONG KONG LIMITED |
| HK-67929 | LEVEMIR FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | NOVO NORDISK HONG KONG LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的第 3 期隨機對照試驗與系統性回顧，直接支持 Insulin Detemir 用於第 1 型糖尿病，證據等級為 L1。
- 這是既有標籤用途，不是新發現。仿單的警語與禁忌資料尚未取得，這是阻擋性的資料缺口，所以決策附帶防護條件。

**若要推進需要：**
- 下載並解析香港衞生署的仿單，補齊警語、禁忌症與核准適應症，這是進入安全性篩選的前提。
- 在本地許可證資料庫確認核准適應症，修正 `original_indications` 空白的問題。
- 補上 DrugBank 的作用機轉資料。
- 在報告中將此項標示為陽性對照，不作為新適應症宣傳。

**其他預測適應症：** 排名第 2 至第 5 的預測（自體免疫性卵巢炎、Opsismodysplasia、硫胺素反應性功能障礙症候群、典型僵硬人症候群）都沒有臨床試驗或文獻，證據等級為 L5，建議 **Hold**。它們的高分可能來自與第 1 型糖尿病的共病或共同自體免疫背景，不代表基礎胰島素有治療效果。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

