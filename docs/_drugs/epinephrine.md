---
layout: default
title: Epinephrine
parent: 高證據等級 (L1-L2)
nav_order: 322
evidence_level: L1
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **4** 個
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

# Epinephrine：從原適應症（未載明）到阻塞性肺疾病

## 一句話總結

Epinephrine（腎上腺素）在香港已有 16 張許可證，但證據包內的許可證資料未載明原適應症。
TxGNN 模型預測它可能對**阻塞性肺疾病 (Obstructive Lung Disease)** 有效。
目前檢索到 **50 筆臨床試驗**（其中 8 筆經確認以腎上腺素為受試藥物，含 3 個已完成的 Phase 3）和 **20 篇文獻**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 阻塞性肺疾病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

證據包缺少詳細的作用機轉（MOA）資料。依已知藥理，Epinephrine 是非選擇性腎上腺素受體促效劑：

- 活化 Beta-2 受體，使氣道平滑肌鬆弛。
- 活化 Alpha-1 受體，減輕黏膜水腫。

這兩者都直接對應支氣管收縮與氣道腫脹，所以在機轉上說得通。

需要注意，這個預測較接近「既有用途或相鄰用途」，不是典型的老藥新用。吸入型腎上腺素已有用於氣喘的產品，臨床試驗也有氣喘的直接研究。細支氣管炎的證據則較不確定。文獻中有 Cochrane 系統性回顧，但檢索到的摘要沒有顯示結論，是否支持常規使用需查閱全文確認。

## 臨床試驗證據

以下為與腎上腺素直接相關、最具參考價值的試驗。其餘檢索結果多為無關試驗或以其他藥物為主的研究，未列入。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | 完成 | 70 | 吸入型腎上腺素氣霧劑 (E004) 對 4–11 歲氣喘兒童的療效與安全性，隨機、雙盲、安慰劑對照，為 4 週試驗 |
| [NCT03567473](https://clinicaltrials.gov/study/NCT03567473) | Phase 3 | 完成 | 864 | 吸入腎上腺素併口服 dexamethasone vs 安慰劑，用於嬰兒細支氣管炎，觀察 7 天內住院率 |
| [NCT00116584](https://clinicaltrials.gov/study/NCT00116584) | Phase 3 | 完成 | 72 | 以氦氧混合氣驅動 racemic epinephrine 噴霧，用於中重度細支氣管炎，評估氣道改善速度 |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | 完成 | 120 | 腎上腺素、dexamethasone 與高張生理食鹽水用於兒童細支氣管炎的先導隨機試驗（複方組合，無法單獨判斷腎上腺素效果） |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Phase 2 | 完成 | 18 | 鼻內腎上腺素 (ARS-1) 對持續性氣喘的交叉試驗，與沙丁胺醇 (albuterol) 及安慰劑對照 |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | 完成 | 24 | 吸入型腎上腺素氣霧劑 (HFA-MDI) 在健康成人的藥物動力學與安全性 |
| [NCT01025648](https://clinicaltrials.gov/study/NCT01025648) | Phase 1/2 | 已終止 | 9 | 腎上腺素 HFA-MDI 對氣喘患者的劑量範圍探索，比較安慰劑與 CFC-MDI 對照 |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Phase 2 | 狀態未知 | 100 | 腎上腺素、dexamethasone 與高張生理食鹽水用於兒童細支氣管炎的隨機對照試驗 |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | 狀態未知 | 500 | 挪威 0–12 個月嬰兒急性細支氣管炎的最佳吸入治療（摘要未確認是否含腎上腺素，需人工核對） |

## 文獻證據

證據包內文獻沒有隨機對照試驗，以下依系統性回顧、回顧文章、其他類型排序。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | 系統性回顧 | Cochrane Database Syst Rev | 腎上腺素用於細支氣管炎的 Cochrane 回顧，摘要僅說明支氣管擴張劑常用但療效不確定，結論需查全文 |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | 系統性回顧 | Cochrane Database Syst Rev | 腎上腺素用於細支氣管炎的早期版本，指出既有回顧顯示支氣管擴張劑對輕中度患者有短期小幅益處 |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | 回顧 racemic epinephrine、全身性類固醇、高張生理食鹽水與高流量氧氣在嬰兒細支氣管炎的角色 |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | 霧化腎上腺素可帶來暫時的症狀緩解，急性細支氣管炎缺乏明確的診斷標準與定義 |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | 經濟評估 | Pediatrics | 以加拿大細支氣管炎腎上腺素類固醇試驗的資料，評估腎上腺素與 dexamethasone 的成本效益 |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clin Evid | 細支氣管炎的疾病概述 |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clin Evid | 細支氣管炎的疾病概述（較早版本） |
| [19444115](https://pubmed.ncbi.nlm.nih.gov/19444115/) | 2009 | 回顧 | Curr Opin Pediatr | 腎上腺素在兒童急診的各種應用與最新建議 |
| [31467680](https://pubmed.ncbi.nlm.nih.gov/31467680/) | 2019 | 動物毒性研究 | Pharmacol Res Perspect | Epinephrine HFA (Primatene Mist) 配方中 thymol 的小鼠吸入慢性毒性研究 |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | 其他 | Ann Allergy | 霧化支氣管擴張劑用於阻塞性肺疾病（無摘要，年代久遠） |

## 香港上市資訊

證據包共有 16 張許可證，以下列出 5 張。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50701 | ADRENALINE INJ 1:1000 | 未載明 | 未載明 |
| HK-66600 | ADRENALINE AGUETTANT SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 1MG/10ML | 未載明 | 未載明 |
| HK-00410 | ADRENALINE INJ BP 1:1000 | 未載明 | 未載明 |
| HK-64270 | JEXT 300 MICROGRAMS SOLUTION FOR INJECTION IN PRE-FILLED PEN 300MCG/0.3ML | 未載明 | 未載明 |
| HK-18103 | ADRENALINE INJ 1 IN 10000 | 未載明 | 未載明 |

從品名看，這 5 張皆為注射劑，沒有吸入或噴霧劑型。若要用於阻塞性肺疾病，劑型與給藥途徑是否可行需另行確認。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的 Phase 3 試驗（NCT01460511、NCT03567473、NCT00116584），涵蓋氣喘與細支氣管炎的腎上腺素用藥，證據等級符合 L1。
- 但「阻塞性肺疾病」範圍很廣，證據集中在兒童氣喘與細支氣管炎，細支氣管炎的療效仍有爭議；香港目前所列許可證也都是注射劑。

**若要推進需要：**
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩檢（目前為阻斷性資料缺口）。
- 補齊作用機轉（MOA）資料。
- 查閱 Cochrane 回顧與 Phase 3 試驗全文，確認實際療效結論。
- 界定目標族群（氣喘、COPD 或細支氣管炎）。
- 確認吸入或霧化劑型在香港的可得性。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

