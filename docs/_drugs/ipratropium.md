---
layout: default
title: Ipratropium
parent: 高證據等級 (L1-L2)
nav_order: 482
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Ipratropium：預測新適應症為阻塞性肺病 (Obstructive Lung Disease)（證據等級 L1）。原適應症：慢性阻塞性肺病、過敏性鼻炎、血管運動性鼻炎、支氣管炎、肺氣腫等"
monitor_inn: "Ipratropium"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "respiratory malformation", "papillary conjunctivitis", "Rienhoff syndrome", "anaphylaxis", "food-dependent exercise-induced anaphylaxis"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Ipratropium：從慢性阻塞性肺病 (COPD) 到阻塞性肺病 (Obstructive Lung Disease)

## 一句話總結

Ipratropium 是吸入型抗膽鹼支氣管擴張劑，原本用於慢性阻塞性肺病 (COPD)、過敏性及血管運動性鼻炎、支氣管炎等。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，目前有 **25 個臨床試驗**和 **20 篇文獻**支持這個方向。
但此預測與原有適應症高度重疊，本質上屬於「適應症內確認」，並非真正的跨疾病再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性阻塞性肺病、過敏性鼻炎、血管運動性鼻炎、支氣管炎、肺氣腫等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位未提供）。依文獻補充，Ipratropium 是非選擇性蕈毒鹼受體拮抗劑，可阻斷氣道平滑肌 M3 受體所介導的支氣管收縮，這是 COPD 與氣喘支氣管擴張的既定機轉。

阻塞性肺病涵蓋 COPD、肺氣腫與支氣管疾病，與 Ipratropium 已知適應症直接重疊，因此這個預測在機轉上合理，但主要是「同適應症的泛化」，而非全新用途。

---

## 臨床試驗證據

資料共收錄 25 個試驗，以下列出最相關的 10 個（依相關性分級與規模選取）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | 完成 | 1118 | Ipratropium/Salbutamol Respimat 與 COMBIVENT 在 COPD 的 12 週支氣管擴張療效與安全性比較 |
| [NCT01415518](https://clinicaltrials.gov/study/NCT01415518) | Phase 4 | 完成 | 581 | 重度 COPD 中，Symbicort 加入 Atrovent＋茶鹼的療效與耐受性 |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Phase 3 | 完成 | 215 | Tiotropium 與 Atrovent MDI 在 COPD 的比較（菲律賓患者） |
| [NCT00239434](https://clinicaltrials.gov/study/NCT00239434) | Phase 3 | 完成 | 200 | Tiotropium 每日一次與 Atrovent MDI 在 COPD 的比較 |
| [NCT00371527](https://clinicaltrials.gov/study/NCT00371527) | NA | 完成 | 200 | 隨機雙盲安慰劑對照，評估 Ipratropium 對無肺部基礎疾病的急性支氣管炎的症狀控制 |
| [NCT02172404](https://clinicaltrials.gov/study/NCT02172404) | Phase 3 | 完成 | 160 | HandiHaler 與 MDI 的操作技巧與易用性比較（偏重器械而非療效） |
| [NCT01136421](https://clinicaltrials.gov/study/NCT01136421) | Phase 3 | 完成 | 124 | COPD 急性惡化時，硫酸鎂與 Ipratropium 搭配短效 β2 促效劑的比較 |
| [NCT01350128](https://clinicaltrials.gov/study/NCT01350128) | Phase 2 | 完成 | 103 | PT001 四種劑量在中重度 COPD 的療效，以 Atrovent HFA 為活性對照 |
| [NCT02686086](https://clinicaltrials.gov/study/NCT02686086) | NA | 完成 | 60 | COPD 患者使用振動網式與噴射式霧化器給予支氣管擴張劑後的肺容積與症狀評分 |
| [NCT04446637](https://clinicaltrials.gov/study/NCT04446637) | Phase 3 | 撤回 | 0 | Ipratropium/Levosalbutamol 固定複方與自由複方的比較（無入組，無資料） |

---

## 文獻證據

資料共收錄 20 篇文獻，以下列出最相關者（以回顧與統合分析為主，未見 RCT 類型標註）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Cochrane 回顧 | Cochrane Database Syst Rev | Tiotropium 與 Ipratropium 用於穩定期 COPD 的比較 |
| [24043433](https://pubmed.ncbi.nlm.nih.gov/24043433/) | 2013 | Cochrane 回顧 | Cochrane Database Syst Rev | 同上之前版本 |
| [35616126](https://pubmed.ncbi.nlm.nih.gov/35616126/) | 2022 | Review | Cochrane Database Syst Rev | 硫酸鎂作為 COPD 急性惡化的輔助治療 |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | Ann Pharmacother | Ipratropium 與 Tiotropium 併用於 COPD 的療效與安全性 |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Albuterol、Ipratropium 及其複方在 COPD 的機轉、療效與安全性 |
| [10565879](https://pubmed.ncbi.nlm.nih.gov/10565879/) | 1999 | Review | Respir Care Clin N Am | 抗膽鹼支氣管擴張劑；Ipratropium 單用及與 Albuterol 併用的肺功能改善已獲證實 |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Review | Clin Pharm | Ipratropium 的藥理、藥動、療效、不良反應與劑量 |
| [6129123](https://pubmed.ncbi.nlm.nih.gov/6129123/) | 1982 | Review | Drugs | 支氣管擴張劑併用的加成效果 |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | 回溯性研究 | Medicine | 益生菌併用 Budesonide 與 Ipratropium 對 COPD 肺功能與腸道菌相的影響（118 位患者） |
| [15257628](https://pubmed.ncbi.nlm.nih.gov/15257628/) | 2004 | Review | Drugs | Ipratropium/Fenoterol 以 Respimat 給藥於氣喘與 COPD |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-23564 | ATROVENT SOLN FOR INHALATION 0.025% | 吸入溶液 | 未載明 |
| HK-50402 | ATROVENT M/D INHALER 20MCG/PUFF-CFC FREE | 吸入器 | 未載明 |
| HK-36372 | ATROVENT SOLN FOR INHALATION 500MCG/2ML | 吸入溶液 | 未載明 |
| HK-64628 | IPRATRAN NEBULISER SOLUTION 0.25MG/ML | 霧化溶液 | 未載明 |
| HK-62900 | IPRATROPIUM BROMIDE ALDO-UNION INHALER 20MCG/ACTUATION | 吸入器 | 未載明 |

（共 7 張有效許可證，皆為單方；其餘 2 張為 HK-51066 IPRAVENT INHALER 與 HK-41964 COMBIVENT SOL FOR INHALATION。）

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**：高血壓、長 QT 症候群、癲癇、低血鉀、糖尿病與酮酸中毒、良性攝護腺增生、高眼壓、閉角型青光眼、代謝性酸中毒、心搏停止、心臟傳導疾病、甲狀腺功能亢進、膀胱頸阻塞、心肌缺血與冠狀動脈疾病等。此資料來自知識圖譜，並非仿單文字。
- **藥物交互作用**：共查得 100 筆，以中度為主，多為其他抗膽鹼或抗蕈毒鹼藥物，例如 Atropine、Hyoscyamine、Glycopyrronium、Scopolamine、Trospium、Promethazine、Chlorpheniramine、Aclidinium，疊加可能增強抗膽鹼副作用。另有與吸入型胰島素的中度交互作用。
- **其他訊號**：有 1 篇病例報告記載吸入 Ipratropium 引發嚴重過敏性反應，另有 1 篇記載吸入後單側瞳孔放大。

仿單警語與禁忌的正式資料尚缺，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個已完成的 Phase 3 試驗（如 NCT02177253，n=1118）支持 Ipratropium 用於阻塞性氣道疾病，且香港已有 7 張有效許可證。
- 此預測與已知適應症基本重疊，屬於適應症內的確認，新增價值有限。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症與正式警語、禁忌
- 補齊作用機轉的正式資料
- 明確界定「阻塞性肺病」的目標族群與給藥途徑，與現行 COPD 標示做區隔
- 針對高風險族群（心血管疾病、青光眼、攝護腺疾病）建立安全性監測，並留意過敏反應

---

## 其他預測適應症簡述

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|------|-----------|------|---------|------|
| 2 | 鼻腔疾病 | 99.86% | L4 | 研究問題（多為已核准的鼻炎適應症，文獻為間接證據） |
| 3 | 咽炎 | 99.85% | L4 | Hold |
| 4 | 急性喉咽炎 | 99.84% | L5 | Hold |
| 5 | 呼吸道畸形 | 99.80% | L3 | 研究問題 |
| 6 | 乳突狀結膜炎 | 99.75% | L5 | Hold |
| 7 | Rienhoff 症候群 | 99.69% | L5 | Hold |
| 8 | 氣管疾病 | 99.66% | L4 | 研究問題（多為前臨床證據） |
| 9 | 過敏性休克 | 99.38% | L4 | Hold（有 Ipratropium 引發過敏性休克的病例報告） |
| 10 | 食物依賴性運動誘發過敏性休克 | 99.36% | L5 | Hold |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

