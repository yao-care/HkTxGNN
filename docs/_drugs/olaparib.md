---
layout: default
title: Olaparib
parent: 高證據等級 (L1-L2)
nav_order: 628
evidence_level: L1
indication_count: 1
---

# Olaparib
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Olaparib：從卵巢癌到女性乳癌

## 一句話總結

Olaparib 是口服 PARP 抑制劑，最早用於 BRCA 突變的卵巢癌維持治療。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效。
目前有 **40 多個相關臨床試驗登記**和 **19 篇文獻**支持這個方向，其中包含多篇 Phase 3 隨機對照試驗（OlympiA、OlympiAD）的發表。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌（BRCA 突變、鉑類敏感復發，依臨床試驗描述；香港許可證未載明適應症文字） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.09% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記錄。以下說明來自一般藥理知識與已發表文獻，並非本次資料包內建的欄位。

Olaparib 抑制 PARP1/2。BRCA1/2 或其他同源重組修復（HR）缺陷的細胞無法修復單股 DNA 斷裂，這些斷裂會變成雙股斷裂，最終導致「合成致死」。

帶有 BRCA1/2 突變的乳癌本身就是 HR 缺陷的腫瘤，與卵巢癌共享同一個脆弱點。這也是模型給出高分（99.09%）的原因。

預期的獲益主要在有生物標記的族群，例如種系 BRCA1/2 突變、HER2 陰性的乳癌。對未經篩選的乳癌，證據較弱。

## 臨床試驗證據

以下列出與乳癌最相關的 10 個試驗。資料包中的 Phase 3 試驗（NCT02282020、NCT06580314、NCT03402841）都是卵巢癌研究，不列為乳癌證據。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | 完成 | 99 | AZD2281（olaparib）用於 BRCA 突變或三陰性乳癌與卵巢癌，評估反應率與相關標記 |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | 進行中（不再招募） | 50 | Olaparib 單用或合併 durvalumab，作為 BRCA 突變、HER2 陰性早期乳癌的術前治療 |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | 招募中 | 176 | Olaparib 加或不加 elacestrant，用於 gBRCA1/2 突變、HR 陽性 HER2 陰性的晚期乳癌 |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | 進行中（不再招募） | 200 | PETREMAC：高風險乳癌的個人化術前治療 |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | 完成 | 103 | Olaparib 合併 carboplatin，用於 BRCA 突變帶原者及三陰性乳癌，含擴展世代 |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | 完成 | 25 | Carboplatin 加 olaparib，再接 olaparib 單用，用於 BRCA 突變 HER2 陰性晚期乳癌；先確認合併劑量 |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | 進行中（不再招募） | 155 | Cediranib 加 olaparib，用於復發三陰性乳癌或卵巢癌 |
| [NCT02208375](https://clinicaltrials.gov/study/NCT02208375) | Phase 1 | 進行中（不再招募） | 159 | Olaparib 合併 vistusertib 或 capivasertib，用於復發三陰性乳癌等 |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | 進行中（不再招募） | 36 | Olaparib 合併 navitoclax，用於 BRCA1/2 或 PALB2 突變的三陰性乳癌 |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | 完成 | 202 | 印度族群，含 gBRCA1/2 突變轉移性乳癌與鉑類敏感復發卵巢癌 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT（OlympiA） | N Engl J Med | 評估 olaparib 作為 BRCA1/2 種系突變早期乳癌的輔助治療 |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT（OlympiA） | Ann Oncol | 高風險 HER2 陰性早期乳癌，olaparib 對比安慰劑 1 年；報告整體存活期，首次期中分析已顯示無侵襲性疾病存活期顯著改善 |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT（OlympiAD） | N Engl J Med | 評估 olaparib 用於 gBRCA 突變轉移性乳癌 |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT（OlympiAD） | Ann Oncol | Olaparib 較醫師選擇的化療延長無惡化存活期；最終整體存活期中位數 19.3 對 17.1 個月（P = 0.513，無顯著差異） |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT（OlympiAD 延長追蹤） | Eur J Cancer | 延長追蹤 25.7 個月，更新整體存活期與安全性 |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | Phase 2-3 RCT（PARTNER） | Nature | 559 位種系 BRCA 野生型三陰性乳癌，術前 carboplatin-paclitaxel 加或不加 olaparib |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 隨機試驗（I-SPY2） | Cancer Cell | Durvalumab、olaparib 加 paclitaxel 提高 HER2 陰性乳癌的病理完全緩解率（20%-37%） |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 試驗（TBCRC 048） | J Clin Oncol | Olaparib 用於體細胞 BRCA1/2 突變或其他 HR 相關基因突變的轉移性乳癌 |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | PARP 抑制劑用於乳癌的整理；olaparib 與 talazoparib 已核准用於種系 BRCA 突變、HER2 陰性乳癌 |
| [31218365](https://pubmed.ncbi.nlm.nih.gov/31218365/) | 2019 | Review | Ann Oncol | PARP 抑制劑十年臨床發展回顧，說明 PARP 抑制與 BRCA 缺陷之間的合成致死關係 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-65987 | LYNPARZA TABLETS 150MG | ASTRAZENECA HONG KONG LIMITED |
| HK-65988 | LYNPARZA TABLETS 100MG | ASTRAZENECA HONG KONG LIMITED |

本次資料未取得這兩張許可證的核准適應症文字，是否已含乳癌需另行確認。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP 抑制劑） |
| 骨髓抑制風險 | 中（PARP 抑制劑類別常見貧血、嗜中性白血球減少、血小板減少；此為類別知識，非本次資料包內容） |
| 致吐性分級 | 低至中 |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 口服抗腫瘤藥，建議依機構的危害性藥品處置規範操作 |

實際警語與注意事項請參考原廠仿單。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- OlympiA 與 OlympiAD 這兩個 Phase 3 隨機對照試驗已發表，且 TxGNN 分數很高（99.09%），機轉（BRCA 缺陷的合成致死）也吻合，因此證據等級為 L1。
- 獲益集中在 BRCA1/2 突變、HER2 陰性等有生物標記的族群，對未篩選的乳癌證據較弱，所以須設下使用條件。
- 香港許可證的核准適應症文字與安全性資料都尚未取得，無法直接視為可放行。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌症），並確認 HK-65987 和 HK-65988 是否已核准乳癌適應症。
- 補齊 DrugBank 的作用機轉記錄。
- 限定 BRCA1/2 突變檢測陽性、HER2 陰性的病人，並訂定檢測流程。
- 建立血液學監測計畫（CBC、肝腎功能）。
- 追蹤進行中的乳癌試驗（如 NCT05498155、NCT06201234）與 PARTNER 的完整結果。

本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

