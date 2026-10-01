---
layout: default
title: Ipratropium
parent: 高證據等級 (L1-L2)
nav_order: 474
evidence_level: L1
indication_count: 10
---

# Ipratropium
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Ipratropium：從抗膽鹼支氣管擴張劑到阻塞性肺疾病 (Obstructive Lung Disease)

## 一句話總結

Ipratropium 是抗膽鹼類吸入型支氣管擴張劑，已在香港上市。
TxGNN 模型預測它可能對**阻塞性肺疾病 (Obstructive Lung Disease)** 有效，目前有 **50 個臨床試驗**和 **20 篇文獻**與這個方向相關，其中多數是間接證據。
這很可能是既有的核准用途，不是真正的新用途，需先核對仿單適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 阻塞性肺疾病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Proceed with Guardrails |

香港許可證資料未提供核准適應症文字，因此無法填寫「原適應症」，也無法確認預測是否屬於既有適應症。

## 為什麼這個預測合理？

Ipratropium 是非選擇性的蕪毒鹼受體 (muscarinic) 拮抗劑。它阻斷迷走神經膽鹼性的支氣管收縮，並減少呼吸道黏液分泌，機轉上直接對應阻塞性氣道疾病。這段機轉說明來自預測模型的推論，DrugBank 的 MOA 欄位目前沒有資料。

文獻證據也支持這個方向。多篇回顧與 Cochrane 系統性回顧探討 ipratropium 在 COPD 的角色，包括與 tiotropium、短效與長效 β2 促效劑的比較。臨床試驗中也有多項以 ipratropium 或含 ipratropium 的複方（如 Combivent、Berodual）作為治療組或對照組的 COPD 研究。

需要注意，這個預測很可能只是重現已知的適用範圍。現有資料缺少原適應症與 MOA，這是輸入資料的缺口，不代表發現了新用途。在核對仿單前，不宜把它當成真正的老藥新用候選。

## 臨床試驗證據

在 50 個檢索到的試驗中，以下 10 個與 ipratropium 或含 ipratropium 的產品最直接相關。其餘多為給藥方式、輔助療法或其他藥物的研究，僅間接相關。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | 完成 | 1118 | Ipratropium/salbutamol Respimat 對比 Combivent、ipratropium 單方與安慰劑，為期 12 週的 COPD 療效與安全性研究 |
| [NCT02194205](https://clinicaltrials.gov/study/NCT02194205) | Phase 3 | 終止 | 360 | Combivent HFA 對比 CFC 劑型與安慰劑，為期 1 年的 COPD 研究 |
| [NCT00388882](https://clinicaltrials.gov/study/NCT00388882) | Phase 4 | 完成 | 327 | Tiotropium 對比 Combivent CFC MDI，為期 12 週的 COPD 研究 |
| [NCT01350128](https://clinicaltrials.gov/study/NCT01350128) | Phase 2 | 完成 | 103 | PT001 四種劑量，以 Atrovent HFA 為開放標籤活性對照 |
| [NCT06040424](https://clinicaltrials.gov/study/NCT06040424) | Phase 3 | 未知 | 74 | Ipratropium/levosalbutamol 固定複方對比自由複方，穩定期 COPD 非劣性試驗 |
| [NCT01243788](https://clinicaltrials.gov/study/NCT01243788) | Phase 4 | 未知 | 450 | Salmeterol/fluticasone 對比 ipratropium/albuterol，中國中重度 COPD 病人 |
| [NCT02238197](https://clinicaltrials.gov/study/NCT02238197) | 無分期（上市後監測） | 完成 | 477 | Atrovent 500µg/2ml 吸入液用於 COPD 的日常使用耐受性與療效 |
| [NCT02238171](https://clinicaltrials.gov/study/NCT02238171) | 無分期（上市後監測） | 完成 | 346 | Atrovent Inhalets 用於 COPD 的日常使用耐受性與療效 |
| [NCT04315558](https://clinicaltrials.gov/study/NCT04315558) | Phase 2 | 完成 | 21 | 霧化 revefenacin 對比霧化 ipratropium，用於需插管的 COPD 急性呼吸衰竭 |
| [NCT03480997](https://clinicaltrials.gov/study/NCT03480997) | Phase 1 | 完成 | 46 | Albuterol 或 albuterol/ipratropium 吸入器的支氣管擴張效果（藥效等效性） |

證據的限制：
- 多項試驗把 ipratropium 當作對照藥或複方成分，不是單獨檢驗它的療效。
- NCT02194205 已終止，證據權重有限。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | 回溯性分析（資料庫分類為 RCT） | Medicine | 118 位 COPD 病人，比較益生菌加 budesonide 與 ipratropium 對肺功能與腸道菌群的影響 |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | 系統性回顧 | Cochrane Database Syst Rev | 比較 tiotropium 與 ipratropium 用於穩定期 COPD |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | 系統性回顧 | Expert Opin Drug Metab Toxicol | 回顧 albuterol、ipratropium 及其複方在 COPD 的機轉、療效與安全性 |
| [16625543](https://pubmed.ncbi.nlm.nih.gov/16625543/) | 2006 | 系統性回顧 | Cochrane Database Syst Rev | Ipratropium 對比短效 β2 促效劑，用於穩定期 COPD |
| [16856113](https://pubmed.ncbi.nlm.nih.gov/16856113/) | 2006 | 系統性回顧 | Cochrane Database Syst Rev | Ipratropium 對比長效 β2 促效劑，用於穩定期 COPD |
| [1835291](https://pubmed.ncbi.nlm.nih.gov/1835291/) | 1991 | 雙盲交叉試驗 | Am J Med | 21 位穩定期 COPD 病人，單次 ipratropium 與茶鹼的急性支氣管擴張效果比較 |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | Ann Pharmacother | 評估 ipratropium 與 tiotropium 併用於 COPD 的療效與安全性 |
| [15257628](https://pubmed.ncbi.nlm.nih.gov/15257628/) | 2004 | Review | Drugs | 回顧 ipratropium/fenoterol（Berodual）經 Respimat 用於氣喘與 COPD |
| [28461224](https://pubmed.ncbi.nlm.nih.gov/28461224/) | 2017 | 研究 | EBioMedicine | 探討輕中度 COPD 男女病人對 ipratropium 的 FEV1 反應是否有性別差異 |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Review | Clin Pharm | 回顧 ipratropium 的藥理、藥動學、療效、不良反應與劑量 |

## 香港上市資訊

共 7 張許可證，以下列出 5 張主要許可證。資料未提供劑型與核准適應症文字，因此省略這兩欄。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-23564 | ATROVENT SOLN FOR INHALATION 0.025% | BOEHRINGER INGELHEIM (HK) LTD |
| HK-50402 | ATROVENT M/D INHALER 20MCG/PUFF-CFC FREE | BOEHRINGER INGELHEIM (HK) LTD |
| HK-36372 | ATROVENT SOLN FOR INHALATION 500MCG/2ML | BOEHRINGER INGELHEIM (HK) LTD |
| HK-64628 | IPRATRAN NEBULISER SOLUTION 0.25MG/ML | WINGS PHARMACEUTICAL LTD |
| HK-62900 | IPRATROPIUM BROMIDE ALDO-UNION INHALER 20MCG/ACTUATION | MEKIM LTD |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢無結果。

文獻中有兩項與安全性相關的訊號：
- **過敏性休克**：有吸入 ipratropium 後發生嚴重過敏性休克的病例報告（[PMID 8449120](https://pubmed.ncbi.nlm.nih.gov/8449120/)）。
- **單側瞳孔放大**：有嬰兒吸入 ipratropium 後出現單側瞳孔放大的病例報告（[PMID 40069469](https://pubmed.ncbi.nlm.nih.gov/40069469/)），這是抗膽鹼藥物的眼部效應。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 試驗（如 NCT02177253）與多篇 Cochrane 系統性回顧，證據等級可達 L1，機轉也直接對應阻塞性氣道疾病。
- 這很可能是既有適應症，而非新用途，且香港仿單的警語與禁忌資料仍缺（屬阻擋性缺口），因此需設防護條件。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症是否已涵蓋阻塞性肺疾病，並補齊警語與禁忌症。
- 若確認屬既有適應症，改以「既有適應症的證據整理」呈現，不列為老藥新用候選。
- 從 DrugBank 補上 MOA 與原適應症資料。
- 其餘預測（排名第 2 至 10，如鼻腔疾病、咽炎、氣管疾病、過敏性休克等）證據不足或僅為模型預測，建議維持 Hold 或列為研究問題。過敏性休克一項另有 ipratropium 本身引發過敏反應的安全訊號，不宜視為治療候選。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

