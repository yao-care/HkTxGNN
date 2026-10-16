---
layout: default
title: Terbutaline
parent: 高證據等級 (L1-L2)
nav_order: 863
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-14
description: "Terbutaline：預測新適應症為阻塞性肺病 (Obstructive Lung Disease)（證據等級 L1）。原適應症：氣喘、支氣管炎、肺氣腫等"
---

# Terbutaline
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
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

# Terbutaline：從氣喘到阻塞性肺病

## 一句話總結

Terbutaline 是選擇性 β2 腎上腺素受體促效劑，原本用於氣喘、支氣管炎與肺氣腫等呼吸道疾病。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，
目前有 **14 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過阻塞性肺病與原適應症高度重疊，實質上屬於仿單內或接近仿單內的用途，而非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘、支氣管炎、肺氣腫等（許可證資料未載明核准適應症文字，此處依藥物原有適應症資料） |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Terbutaline 是選擇性 β2 腎上腺素受體促效劑。它活化 Gs 偶聯受體，使細胞內 cAMP 上升，進而放鬆支氣管平滑肌，產生支氣管擴張作用。這也是它用於氣喘、支氣管炎與肺氣腫的機轉基礎。（DrugBank 的 MOA 欄位目前缺乏資料，以上機轉說明來自分析時的機轉推論。）

阻塞性肺病（如氣喘、COPD）的核心問題是可逆的氣流受限，與 terbutaline 原有適應症在病理與治療目標上高度重疊。因此這個預測更像是在原適應症範圍內的延伸，而非跨疾病領域的再利用。

需要留意的是，Phase 3 證據多半是以 budesonide/formoterol 為實驗組，terbutaline 僅作為對照或緩解用藥。這些試驗支持的是 terbutaline 作為參考緩解藥物的角色，而不是證明它本身是實驗介入。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | 完成 | 4215 | Symbicort 視需要使用 vs. Pulmicort 每日兩次加視需要使用 terbutaline（氣喘） |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | 完成 | 3850 | Symbicort 視需要使用 vs. terbutaline 視需要使用 vs. Pulmicort 加 terbutaline（氣喘） |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | 完成 | 120 | 靜脈硫酸鎂 vs. terbutaline 用於兒童急性氣喘發作 |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | 完成 | 2091 | Symbicort SMART vs. Symbicort 加 terbutaline 視需要使用（氣喘） |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | 完成 | 1970 | Symbicort 與 Pulmicort+Oxis 加 Bricanyl（terbutaline）的真實世界醫療成本比較 |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | 完成 | 1600 | Symbicort 單一吸入器療法 vs. 常規最佳治療（氣喘） |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | 完成 | 860 | 視需要使用 vs. 規律使用 budesonide/formoterol 加視需要使用 terbutaline |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | 完成 | 95 | Bricanyl Turbuhaler M3 vs. M2，對乙醯膽鹼激發支氣管收縮的保護效果（輕中度氣喘） |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | 完成 | 24 | 日本成人氣喘患者中 terbutaline Turbuhaler 0.4 mg 與 salbutamol pMDI 的相對療效 |
| [NCT04973345](https://clinicaltrials.gov/study/NCT04973345) | Phase 2/3 | 撤回 | 0 | terbutaline 暴露－反應交叉試驗，未收案，無證據價值 |

另有登記試驗為 Phase 4 或僅以 terbutaline 為背景用藥，直接相關性低，此處未列出。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | 輕度氣喘視需要使用吸入型 budesonide-formoterol 可作為傳統治療的替代 |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | 口服 terbutaline 可增加 COPD 患者的橫膈收縮力 |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | 慢性阻塞性肺病中 clenbuterol 與 terbutaline 的支氣管擴張效果比較 |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | RCT | Chest | β 阻斷劑與 terbutaline 併用於慢性阻塞性肺病的效果與交互作用 |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Review | Am J Respir Crit Care Med | β2 促效劑（含 terbutaline）在肺部疾病的應用，提供快速症狀緩解 |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | 系統性回顧 | Naunyn Schmiedebergs Arch Pharmacol | terbutaline 在人體的臨床藥物動力學 |
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | 隨機雙盲對照試驗 | Acad Emerg Med | COPD 急性惡化需非侵入性通氣時，terbutaline 加 ipratropium 與單用 terbutaline 的比較 |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | 雙盲交叉試驗 | Lung | 單劑 terbutaline 對 COPD 患者運動能力與肺功能的影響 |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | 雙盲交叉試驗 | Respir Med | 吸入 terbutaline 對 COPD 患者 FEV1、FVC、呼吸困難與步行距離的影響 |
| [26963310](https://pubmed.ncbi.nlm.nih.gov/26963310/) | 2015 | Review | Tuberk Toraks | 氣喘－COPD 重疊症候群的特徵與處置 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48007 | TERBUTA TAB 2.5MG | 錠劑（2.5 mg） | 資料未載明 |
| HK-46514 | BALTIC-D TAB 2.5MG | 錠劑（2.5 mg） | 資料未載明 |
| HK-49032 | VICKTALINE SYRUP 3MG/5ML | 糖漿（3 mg/5 mL） | 資料未載明 |
| HK-55764 | APT-TERBUTALINE SR TAB 5MG | 緩釋錠（5 mg） | 資料未載明 |
| HK-64629 | BUTANYL NEBULISER SOLUTION 2.5MG/ML | 噴霧吸入液（2.5 mg/mL） | 資料未載明 |

香港共有 19 張有效的單方許可證，無已註銷者，涵蓋錠劑、糖漿、緩釋錠與噴霧吸入液。上表僅列出 5 張代表性許可證。

---

## 安全性考量

- **禁忌症（知識圖譜關聯，非仿單內容）**：知識圖譜顯示 terbutaline 與下列疾病存在禁忌關聯，使用前需評估：
  - 心血管：高血壓、心肌缺血、冠狀動脈疾病、心臟傳導疾病、心因性猝死
  - 代謝與內分泌：高血糖、糖尿病、糖尿病酮酸中毒、缺鉀症、甲狀腺功能亢進、葛瑞夫茲氏症、甲狀腺毒症
  - 神經與呼吸：癲癇、呼吸衰竭、肺水腫
  - 產科：胎盤早期剝離
- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為部分範例：
  - 中度：acarbose、isometheptene、famotidine、epinephrine、albiglutide、alogliptin、pioglitazone、canagliflozin、chlorpropamide、clarithromycin、loperamide、bisacodyl
  - 輕度：hydrocortisone、triamcinolone、dexamethasone、beclomethasone、betamethasone、budesonide
- **使用注意**：機轉分析建議監測心搏過速、低血鉀與震顫，並謹慎與 β 阻斷劑併用，以及用於有心血管共病者。

仿單的主要警語與正式禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 阻塞性肺病與 terbutaline 原有適應症幾乎重疊，且有多個大型 Phase 3 RCT 及多項 COPD 的雙盲試驗支持其支氣管擴張作用，證據等級為 L1。但 Phase 3 證據多以 terbutaline 為對照或緩解藥物，而非實驗介入，且此預測並非真正的新適應症。
- 心血管、代謝與電解質相關的禁忌關聯明顯，需要設置安全防護。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認核准適應症、警語與禁忌症（目前許可證資料皆未載明適應症文字）
- 補充 DrugBank 的作用機轉資料
- 釐清各劑型（錠劑、糖漿、緩釋錠、噴霧吸入液）與目標族群的適用性
- 制定心率、血鉀、血糖的監測計畫，以及 β 阻斷劑併用的處置原則

---

### 附註：其他預測適應症

- **呼吸道畸形 (Respiratory Malformation)**（分數 99.52%，L4，建議 Hold）：terbutaline 的支氣管擴張或許能緩解伴隨的可逆性氣流阻塞，但無法處理結構缺陷。目前僅有一項兒童藥動學與安全性的觀察性計畫（NCT04278404），文獻多與氣喘、支氣管炎或其他疾病有關，缺乏畸形的對照證據，且高分可能反映網路鄰近性而非疾病特異性機轉。
- **Rienhoff 症候群**（分數 99.38%，L5，建議 Hold）：無臨床試驗與文獻，機轉上也看不出 β2 促效作用與此疾病（與 TGF-β 路徑失調相關）的關聯，需先完成前臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

