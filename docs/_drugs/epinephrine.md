---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Epinephrine"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
description: "Epinephrine：預測新適應症為阻塞性肺病 (obstructive lung disease)（證據等級 L5）。香港藥劑製品註冊：16 張（有效 16 張）"
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Epinephrine: 阻塞性肺病 (obstructive lung disease)
{: .text-alpha }

## 一句話總結

Epinephrine（腎上腺素）是非選擇性腎上腺素受體促效劑，原本用於氣喘、支氣管炎、過敏性休克（anaphylaxis）、低血壓與開角型青光眼等。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，
目前有 **15 個臨床試驗**和 **20 篇文獻**與此方向相關。
不過這個訊號大致是原有氣喘、支氣管炎適應症的延伸，並非全新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 阻塞性肺病 (obstructive lung disease) |
| TxGNN 預測分數 | 0.9971 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 16 張／共 16 張） |
| 許可證數 | 16 張（有效 16 張） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Epinephrine 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Epinephrine 同時作用於 α 及 β 腎上腺素受體。透過其對 α 腎上腺素受體的作用，epinephrine 可減輕過敏性休克期間所發生的血管擴張及血管通透性增加，此等情況可導致血管內液體容積流失及低血壓。」英文原文："Epinephrine acts on both alpha and beta-adrenergic receptors. Through its action on alpha-adrenergic receptors, epinephrine lessens the vasodilation and increased vascular permeability that occurs during anaphylaxis, which can lead to loss of intravascular fluid volume and hypotension."（[DailyMed: Auvi-Q (epinephrine) prescribing information, Sportpharm LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f40988b-8365-4f7b-84d1-b88e053725cf)，版本日期 2026-09-18；查閱日期 2026-11-19）。就藥理學而言，Epinephrine 是非選擇性腎上腺素受體促效劑：活化 β2 受體可使支氣管平滑肌鬆弛而擴張氣道，活化 α1 受體則透過血管收縮減輕氣道黏膜水腫。

阻塞性肺病涵蓋氣喘與慢性阻塞性肺病（COPD），而氣喘、支氣管炎本來就是 Epinephrine 的既有適應症。因此這個預測更像是原適應症的延伸，而非真正的新用途。

需要留意的是，對於嬰兒細支氣管炎（bronchiolitis）這類相關的氣道阻塞疾病，Cochrane 系統性回顧與網絡統合分析顯示療效有限或不一致，不能直接類推為有效。

---

## 臨床試驗證據

以下列出與阻塞性肺病最相關的 10 個試驗（其餘為藥動學研究或相關性待評估者）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Phase 3 | 完成 | 373 | Epinephrine HFA 吸入氣霧劑對青少年與成人氣喘的 12 週療效與安全性，對照安慰劑及 Primatene Mist |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Phase 3 | 完成 | 208 | 氣喘患者 3 個月安全性延伸研究，累積 6 個月安全性資料 |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | 完成 | 70 | 吸入 Epinephrine (E004) 用於 4–11 歲氣喘兒童，4 週療效與安全性 |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | 完成 | 28 | E004 單劑用於氣喘兒童的交叉試驗（規模小） |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | 完成 | 49 | 肌肉注射 Epinephrine 作為重度兒童氣喘急性發作的輔助治療 |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | 完成 | 120 | Epinephrine、Dexamethasone 與高張食鹽水用於細支氣管炎（複方設計） |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | 狀態未知 | 500 | 嬰兒急性細支氣管炎的最佳吸入治療 |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Phase 2 | 狀態未知 | 100 | Epinephrine、Dexamethasone 與高張食鹽水用於細支氣管炎 |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | 不適用 | 狀態未知 | 600 | Epinephrine 與 Albuterol 用於細支氣管炎的比較 |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | 不適用 | 完成 | 65 | 吸入腎上腺素與鼻減充血滴劑用於細支氣管炎的比較 |

另有數個藥動學研究（NCT01255709、NCT04207840、NCT01737892、NCT01188577）以及高張食鹽水研究（NCT01276821）和嬰兒氣道阻塞評估（NCT00435994）。這些主要提供暴露量或安全性資訊，未列入上表。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | RCT | The Journal of Pediatrics | 重症加護病房兒童細支氣管炎，評估類固醇合併霧化 Epinephrine 能否縮短正壓支持時間 |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | Epinephrine 用於細支氣管炎的療效評估 |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 支氣管擴張劑對輕中度細支氣管炎有短期的有限助益 |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | 網絡統合分析 | Pediatrics | 比較急診細支氣管炎各種介入的療效 |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Review | Emerg Med Clin North Am | 急診處理氣喘與 COPD 急性發作 |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | 回顧消旋腎上腺素、類固醇、高張食鹽水與高流量氧氣治療細支氣管炎的角色 |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Review | Duodecim | 細支氣管炎治療以氧合監測與補充氧氣為核心，必要時使用消旋腎上腺素吸入 |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Review | Curr Opin Pediatr | 細支氣管炎的治療皆未被證實能改變病程，僅少數有初步前景 |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | 成本效益分析 | Pediatrics | 以加拿大試驗資料評估 Epinephrine 與 Dexamethasone 的成本效益 |
| [11940264](https://pubmed.ncbi.nlm.nih.gov/11940264/) | 2002 | Review | Critical Care | 重度氣喘與氣喘持續狀態的臨床回顧 |

---

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑（張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表），以下列出部分主要許可證（許可證資料未載明劑型與核准適應症文字）：

<!-- review:begin hk-lic-20261124b-epinephrine-1 -->

> **查核更正（2026-11-24）**：原文為「香港共有 16 張有效的單一成分許可證，以下列出 5 張主要許可證（許可證資料未載明劑型與核准適應症文字）：」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-epinephrine-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-50701 | ADRENALINE INJ 1:1000 | 單一成分 | ATLANTIC PHARMACEUTICAL LIMITED | 有效 |
| HK-66600 | ADRENALINE AGUETTANT SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 1MG/10ML | 單一成分 | HONG KONG MEDICAL SUPPLIES LTD | 有效 |
| HK-00410 | ADRENALINE INJ BP 1:1000 | 單一成分 | PFIZER CORPORATION HONG KONG LIMITED | 有效 |
| HK-64270 | JEXT 300 MICROGRAMS SOLUTION FOR INJECTION IN PRE-FILLED PEN 300MCG/0.3ML | 單一成分 | ALK-ABELLO A/S | 有效 |
| HK-64269 | JEXT 150 MICROGRAMS SOLUTION FOR INJECTION IN PRE-FILLED PEN 150MCG/0.15ML | 單一成分 | ALK-ABELLO A/S | 有效 |

上表列出其中 5 張（共 16 張）。

<!-- licenses:end -->

其餘許可證多為含 Adrenaline 的局部麻醉注射劑（如牙科用 Septanest、Xylocaine、Marcain 等）。

---

## 安全性考量

- **禁忌症（知識圖譜資料，非仿單內容）**：高血壓、冠狀動脈疾病、心肌梗塞、心房顫動、心臟傳導疾病、心臟驟停、心血管疾病、閉角型青光眼、糖尿病及酮酸中毒、癲癇、肝腎疾病、甲狀腺機能亢進、重症肌無力、良性攝護腺肥大、呼吸衰竭等。
- **藥物交互作用**：資料庫共查得 100 筆。主要為 Major 等級的 Amitriptyline、Amoxapine（三環類抗憂鬱劑）。Moderate 等級包括 β 阻斷劑（Acebutolol、Atenolol、Betaxolol）、β2 促效劑（Formoterol、Salbutamol、Arformoterol）、刺激劑（Amphetamine、Methylphenidate、Atomoxetine）、抗精神病藥（Aripiprazole、Asenapine、Amisulpride）以及降血糖藥（Acarbose、Alogliptin、Albiglutide、Acetohexamide）。

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 氣喘試驗（吸入型 E004，NCT01357642、NCT01460511 等），且 Epinephrine 已在香港上市。
- 但這主要是既有適應症的延伸，細支氣管炎的證據並不一致，COPD 的直接證據也不足。心血管等禁忌族群多，需設立使用防護。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，並補充詳細的作用機轉資料
- 釐清目標族群（氣喘、COPD 或細支氣管炎），並取得 COPD 的專屬臨床證據
- 確認給藥途徑與劑型（香港現有許可證皆為注射劑，未見吸入劑型）
- 針對心血管疾病患者及 Major 等級交互作用（如三環類抗憂鬱劑）制定篩選與監測計畫

---

### 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 食物依賴型運動誘發過敏性休克 | 0.9957 | L5 | Research Question：無專屬試驗，僅有系統性回顧與病例文獻，主要由一般過敏性休克指引推論 |
| 呼吸道畸形 (Respiratory Malformation) | 0.9956 | L3 | Research Question：僅 1 個 Phase 1 新生兒暫時性呼吸急促試驗，結構性畸形預期不會對 Epinephrine 有反應 |
| Rienhoff 症候群 | 0.9957 | L5 | Hold：無試驗、無文獻，也找不到合理的機轉連結，僅為模型預測 |

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Auvi-Q (epinephrine) prescribing information, Sportpharm LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f40988b-8365-4f7b-84d1-b88e053725cf) |
| 2026-11-24 | 「香港共有 16 張有效的單一成分許可證，以下列出 5 張主要許可證（許可證資料未」→「香港含本藥成分的許可證包括單一成分與複方製劑（張數（含有效、」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

