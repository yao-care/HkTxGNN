---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 474
evidence_level: L5
indication_count: 10
monitor_inn: "INSULIN HUMAN"
predicted_indications: ["autoimmune oophoritis", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy"]
last_modified_at: 2026-11-24
description: "Insulin Human：預測新適應症為自體免疫性卵巢炎 (Autoimmune Oophoritis)（證據等級 L5）。原適應症：第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒"
---

# Insulin Human
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## 人類胰島素（Insulin Human）：從糖尿病到自體免疫性卵巢炎
{: .text-alpha }

## 一句話總結

人類胰島素是用於控制血糖的藥物，知識圖譜中記錄的原適應症包括第 1 型與第 2 型糖尿病及糖尿病酮酸中毒。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒（知識圖譜中記錄的關聯，香港許可證資料未載明適應症文字） |
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 0.9984 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 18 張／共 18 張） |
| 許可證數 | 18 張（有效 18 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Insulin Human 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「調節葡萄糖代謝是胰島素（包括HUMULIN R U-500）的主要作用。胰島素透過刺激骨骼肌及脂肪的周邊葡萄糖攝取，以及抑制肝臟葡萄糖生成，從而降低血糖。」英文原文："Regulation of glucose metabolism is the primary activity of insulins, including HUMULIN R U-500. Insulins lower blood glucose by stimulating peripheral glucose uptake by skeletal muscle and fat, and by inhibiting hepatic glucose production."（[DailyMed: Humulin R U-500 Kwikpen (insulin human) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60e8dd0-1d48-4dc9-87fd-e14675255e8c)，版本日期 2026-07-01；查閱日期 2026-11-19）。根據已知資訊，人類胰島素是替代內源性胰島素、調節血糖的荷爾蒙製劑，但這不足以說明它對自體免疫性卵巢炎的作用。

這個預測來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據：自體免疫性卵巢炎常與多腺體自體免疫症候群（包括第 1 型糖尿病）並存，可能因此讓模型把它與胰島素連在一起。胰島素本身沒有已知的免疫調節或卵巢保護作用。

因此，這個高分應視為計算預測，不是機轉或臨床上的證據。

### 其他預測新適應症（皆為 L5、建議 Hold）

| 排名 | 預測疾病 | TxGNN 分數 | 評語 |
|-----|---------|-----------|------|
| 2 | 局限性僵硬肢體症候群 | 0.9981 | 與抗 GAD65 自體免疫及併發的第 1 型糖尿病有關，胰島素只處理血糖，不影響神經症狀 |
| 3 | 典型僵人症候群 | 0.9981 | 同上，治療依賴 GABA 類藥物與免疫治療 |
| 4 | 硫胺素反應性功能障礙症候群 | 0.9980 | 胰島素已用於其併發的糖尿病，根本治療是補充硫胺素 |
| 5 | 蛙狀骨發育不良 (Opsismodysplasia) | 0.9979 | INPPL1 與胰島素訊息路徑有關，僅屬推測 |
| 6 | 藥物引起的局部脂質營養不良 | 0.9972 | 胰島素本身會造成注射部位脂質營養不良，屬安全性疑慮 |
| 7 | 離心性脂質營養不良 | 0.9970 | 無證據顯示有效，局部注射可能反而造成脂肪變化 |
| 8 | 壓力引起的局部脂肪萎縮 | 0.9970 | 成因為機械性，且胰島素注射可致脂肪萎縮 |
| 9 | 胰臟發育不全 | 0.9970 | 胰島素替代本就是標準支持治療，屬原適應症延伸而非新用途 |
| 10 | 特發性局部脂質營養不良 | 0.9968 | 無證據，且胰島素可能引起注射部位脂質營養不良 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑（張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表；下表列出部分，許可證資料中未載明劑型與核准適應症文字）：

<!-- review:begin hk-lic-20261124b-insulin_human-1 -->

> **查核更正（2026-11-24）**：原文為「香港共有 18 張有效的單一成分許可證（完整清單如下，許可證資料中未載明劑型與核准適應症文字）：」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-insulin_human-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-60290 | ACTRAPID PENFILL INJ 100IU/ML (BRAZIL) | 單一成分 | NOVO NORDISK HONG KONG LIMITED | 有效 |
| HK-63758 | ACTRAPID SOLUTION FOR INJECTION 100IU/ML | 單一成分 | NOVO NORDISK HONG KONG LIMITED | 有效 |
| HK-54859 | SCILIN R INJ 100 IU/ML (CARTRIDGE) | 單一成分 | KEEN HEALTH LIMITED | 有效 |
| HK-54861 | SCILIN R INJ 100 IU/ML (VIAL) | 單一成分 | KEEN HEALTH LIMITED | 有效 |
| HK-39494 | HUMULIN R INSULIN INJ 100IU/ML-CARTRIDGE | 單一成分 | ELI LILLY ASIA, INC. | 有效 |

上表列出其中 5 張（共 18 張）。

<!-- licenses:end -->

另有 13 張許可證（包含 Actrapid、Humulin、Mixtard、Scilin M30 等系列）同樣有效。

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分中度交互作用：
  - 擬交感神經藥：Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol
  - β 阻斷劑：Acebutolol
  - 其他降血糖藥：Metformin、Pioglitazone、Alogliptin、Albiglutide
  - 荷爾蒙類：Ethinylestradiol、Estradiol、Hydrocortisone
  - 其他：Acetazolamide、Doxycycline、Ethanol、Hydrochlorothiazide、Alpelisib、Benazepril
- **局部脂質營養不良**：胰島素注射本身是已知的注射部位脂質營養不良（脂肪增生或萎縮）原因，對於預測的局部脂質營養不良類疾病，這是安全性疑慮。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都沒有臨床試驗或文獻直接支持，證據等級為 L5，高分很可能來自自體免疫共病、糖尿病表型重疊等網路關聯，而非治療機轉。
- 部分預測（如胰臟發育不全、硫胺素反應性功能障礙症候群）只是對併發糖尿病的症狀治療，不算新的再利用機會；脂質營養不良類疾病反而有安全疑慮。

**若要推進需要：**
- 補齊作用機轉資料
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 針對自體免疫性卵巢炎進行文獻與試驗檢索，確認是否存在直接研究
- 若有直接證據，再評估給藥途徑與族群安全性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Humulin R U-500 Kwikpen (insulin human) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60e8dd0-1d48-4dc9-87fd-e14675255e8c) |
| 2026-11-24 | 「香港共有 18 張有效的單一成分許可證（完整清單如下，許可證資料中未載明劑型與核」→「香港含本藥成分的許可證包括單一成分與複方製劑（張數（含有效、」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

