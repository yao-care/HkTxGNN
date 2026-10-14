---
layout: default
title: Amiodarone
parent: 高證據等級 (L1-L2)
nav_order: 54
evidence_level: L1
indication_count: 10
---

# Amiodarone
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

# Amiodarone：從心室纖維顫動到心室心搏過速

## 一句話總結

Amiodarone（胺碘酮）是一種多通道抗心律不整藥物，原本用於心室纖維顫動（ventricular fibrillation）。
我們依 TxGNN 預測分數與證據強度，以排名第 3 的**心室心搏過速 (Ventricular Tachycardia)** 作為主要評估對象。
目前有 **18 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含 3 個已完成的 Phase 3 試驗與多個 Phase 4 比較試驗。

> 說明：TxGNN 分數最高的是「兒茶酚胺敏感性多形性心室心搏過速 (CPVT)」（99.78%），但其文獻僅為病例與世代描述，且 amiodarone 並非該病的標準治療，因此證據上以心室心搏過速作為主要評估重點。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心室纖維顫動（資料來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 心室心搏過速 (Ventricular Tachycardia) |
| TxGNN 預測分數 | 99.64% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料庫條目，但依文獻所述，Amiodarone 屬 Vaughan Williams 第 III 類抗心律不整藥，可阻斷鉀離子通道以延長再極化時間，同時也具有鈉通道、鈣通道及 β 腎上腺素受體阻斷作用。

心室纖維顫動與心室心搏過速同屬心室性心律不整，常見機轉都是折返與觸發活動。Amiodarone 的多通道作用可直接針對這些機轉，因此用於心室心搏過速在機轉上相當合理，屬於接近原適應症的用法（on-label 或 near-label）。

---

## 臨床試驗證據

以下列出最相關的 10 個試驗（依相關性分級排序）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Phase 3 | 完成 | 3024 | Amiodarone、lidocaine 或安慰劑用於院外心臟驟停（VF／無脈搏 VT） |
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Phase 3 | 完成 | 未提供 | AVID：抗心律不整藥物（以 amiodarone 為主）vs 植入式去顫器，用於致命性心室心律不整 |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Phase 4 | 完成 | 400 | OPTIC：amiodarone + β 阻斷劑 vs 單用 β 阻斷劑 vs sotalol，預防 ICD 電擊 |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Phase 4 | 完成 | 416 | 心肌梗塞後持續性單形性 VT：導管消融 vs 抗心律不整藥物 |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Phase 4 | 未知 | 80 | 急診穩定性 VT：amiodarone vs lidocaine |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Phase 4 | 提前終止 | 302 | PROCAMIO：IV amiodarone vs IV procainamide 用於寬 QRS 心搏過速 |
| [NCT03855826](https://clinicaltrials.gov/study/NCT03855826) | Phase 4 | 未知 | 756 | Nifekalant 用於 VT/VF，amiodarone 可能為對照組 |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | N/A | 未知 | 1100 | CHAGASICS：Chagas 心肌病變中 amiodarone vs ICD |
| [NCT01097330](https://clinicaltrials.gov/study/NCT01097330) | Phase 3 | 提前終止 | 12 | 導管消融 vs amiodarone 用於 ICD 患者的電擊預防（收案過少） |
| [NCT02114528](https://clinicaltrials.gov/study/NCT02114528) | Phase 4 | 提前終止 | 3 | 抗心律不整藥物 vs 導管消融（僅收 3 人） |

另有多個消融 vs 藥物比較試驗（部分已撤回或提前終止），資料價值有限。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | RCT | European Heart Journal | PROCAMIO：IV procainamide 與 amiodarone 用於可耐受的寬 QRS 心搏過速之安全性與療效比較 |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Review | Vasc Health Risk Manag | Amiodarone 是終止與預防 VF/VT 的主要抗心律不整藥物，電擊難治性心臟驟停時最有效 |
| [36878200](https://pubmed.ncbi.nlm.nih.gov/36878200/) | 2023 | Review | Cardiology | 心室心律不整的藥物治療總覽 |
| [28900864](https://pubmed.ncbi.nlm.nih.gov/28900864/) | 2017 | Review | Curr Cardiol Rep | ICD 電擊患者何時用藥、何時消融；抗心律不整藥療效不完全且副作用多 |
| [9137212](https://pubmed.ncbi.nlm.nih.gov/9137212/) | 1997 | Review | J Am Coll Cardiol | 靜脈注射 amiodarone 的藥理與對惡性心室心律不整的療效 |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Cohort | Emerg Med Australas | 救護人員於院前給予 amiodarone 治療穩定性 VT 的安全性與療效 |
| [41217320](https://pubmed.ncbi.nlm.nih.gov/41217320/) | 2026 | 子研究 | J Am Coll Cardiol | VANISH2 子研究：導管消融 vs sotalol 或 amiodarone |
| [37380314](https://pubmed.ncbi.nlm.nih.gov/37380314/) | 2023 | 研究 | JACC Clin Electrophysiol | 消融 vs 升級抗心律不整藥物對 VT 與 ICD 治療負擔的影響 |
| [10666663](https://pubmed.ncbi.nlm.nih.gov/10666663/) | 2000 | Review | Curr Opin Cardiol | Amiodarone 主要與次要預防試驗（EMIAT、CAMIAT 等）回顧 |
| [8258259](https://pubmed.ncbi.nlm.nih.gov/8258259/) | 1993 | 病例 | Clin Pharm | Amiodarone 引起的甲狀腺功能異常 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27296 | CORDARONE INJECTABLE SOLUTION 0.15G/3ML（Sanofi） | 注射劑 | 資料未載明 |
| HK-27294 | CORDARONE TAB 200MG（Sanofi） | 錠劑 | 資料未載明 |
| HK-66829 | AMIODARONE RIVOPHARM TABLETS 200MG | 錠劑 | 資料未載明 |
| HK-65597 | AMIODARONE GP TABLETS 200MG | 錠劑 | 資料未載明 |
| HK-60895 | AMIODARONE SANDOZ TAB 200MG | 錠劑 | 資料未載明 |

另有 HK-65675（AMIODARONE-HAMELN 注射濃縮液）與 HK-58487（ADARONE 錠 200MG），共 7 張許可證，皆為有效的單一成分製劑。

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（非仿單文字）：長 QT 症候群（含家族性）、尖端扭轉型心搏過速、房室傳導阻滯、病竇症候群、肝臟疾病與藥物性肝損傷、甲狀腺功能低下與亢進（含 Graves 病、甲狀腺毒症）、間質性肺病、嗜酸性肺炎、過敏性肺炎、周邊神經病變、視神經炎、角膜沉積、低血鉀等。
- **藥物交互作用**：共查得 100 筆。主要（Major）等級包括 cisapride、clarithromycin、dolasetron、eliglustat、clotrimazole、dexamethasone、hydrocortisone、amphotericin B 各劑型、agalsidase beta 等；中度包括 famotidine、cimetidine、aprepitant、bisacodyl、budesonide 等。
- **文獻提示的毒性**：肺毒性（纖維化、肺泡出血）、甲狀腺功能異常、QT 延長、低血壓。

詳細警語與禁忌請參考原廠仿單。

---

## 其他預測適應症簡評

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|------|-----------|------|---------|------|
| 1 | CPVT | 99.78% | L4 | Hold：標準治療為 β 阻斷劑與 flecainide，amiodarone 通常被認為無效或較差 |
| 2 | 持續性嬰兒心室心搏過速 | 99.65% | L2 | 研究問題：有 IV amiodarone 兒科 RCT（PMID 16316969），但多為上心室或交界性心搏過速，需留意嬰兒安全性 |
| 4–9 | 舊版束支傳導阻滯、類風濕性關節炎、短指並指症候群、肝素輔因子 II 缺乏、拔毛症、眼缺損小眼畸形—肢根型發育不良症候群 | 99.2–99.6% | L5 | Hold：無試驗或文獻支持；部分文獻反映的是藥物不良反應 |
| 10 | 痛風 | 99.19% | L5 | Hold：文獻多為藥物交互作用情境，非療效證據 |

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對心室心搏過速）

**理由：**
- 有 3 個已完成的 Phase 3 試驗（含 n=3024 的大型試驗）與多個 Phase 4 比較試驗，加上 RCT 文獻，證據等級為 L1，且屬於接近原適應症的使用。
- 但 amiodarone 的毒性與交互作用負擔重，必須設定安全防護。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌（目前為阻擋性資料缺口）。
- 補充詳細作用機轉（MOA）資料。
- 建立監測計畫：肺功能、甲狀腺功能、肝功能、心電圖（QT 間期）、眼科檢查。
- 針對 100 筆交互作用建立用藥審查流程，尤其是 Major 等級者。
- 若考慮嬰兒心室心搏過速，需另行評估兒科劑量與安全性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

