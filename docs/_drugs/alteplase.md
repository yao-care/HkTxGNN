---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Alteplase：預測新適應症為後側壁心肌梗塞 (Posterolateral Myocardial Infarction)（證據等級 L5）。原適應症：肺栓塞、缺血性中風、心肌梗塞、冠狀動脈血栓"
monitor_inn: "ALTEPLASE"
predicted_indications: ["posterolateral myocardial infarction", "posteroinferior myocardial infarction", "septal myocardial infarction", "heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Alteplase：從心肌梗塞到血栓性疾病（Thrombophilia）

## 一句話總結

Alteplase 是重組組織型纖維蛋白溶解酶原活化劑（tPA），原本用於心肌梗塞、肺栓塞、缺血性中風等急性血栓事件。
TxGNN 模型預測分數最高的新適應症多為心肌梗塞的解剖亞型（如後側壁心肌梗塞），這些與原適應症高度重疊，並非真正的再利用訊號。
較具探索價值的方向是**血栓性體質（Thrombophilia）**：目前有 **1 個進行中的 Phase 2 試驗**和 **20 篇文獻**（以個案報告為主），整體證據偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺栓塞、缺血性中風、心肌梗塞、冠狀動脈血栓（取自知識圖譜；香港許可證未登載適應症文字） |
| 預測新適應症 | 後側壁心肌梗塞 (Posterolateral Myocardial Infarction)（排名第 1）；較值得探索者為血栓性體質 (Thrombophilia)（排名第 8） |
| TxGNN 預測分數 | 99.79%（後側壁心肌梗塞）；99.43%（血栓性體質） |
| 證據等級 | L5（排名第 1 預測）；L3（血栓性體質） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（排名第 1 預測）；血栓性體質列為研究問題 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，alteplase 屬於纖維蛋白溶解劑（plasminogen activator）類別，一般可將纖維蛋白溶解酶原轉化為纖維蛋白溶解酶，溶解急性血栓。這是基於藥物類別的通識說明，並非來自本報告所整理的資料。

排名前三的預測（後側壁、後下壁、間隔心肌梗塞）都是已核准「心肌梗塞」適應症的解剖亞型。高分最可能反映知識圖譜中疾病本體的鄰近關係，而不是新的再利用發現。

血栓性體質（如抗凝血酶缺乏、肝素輔因子 II 缺乏、第五因子過量）則是另一種情形：患者容易發生靜脈與動脈血栓，alteplase 可溶解其急性血栓，但**無法矯正潛在的凝血異常**。此外，已有個案報告顯示抗凝血酶缺乏患者可能對全身性溶栓產生抗性。

---

## 臨床試驗證據

以下為預測血栓性體質的試驗（排名第 1 至 7 及 9 的預測無登記試驗）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05540834](https://clinicaltrials.gov/study/NCT05540834) | Phase 2 | 招募中 | 70 | 以黏彈性檢測（VET）引導 tPA 治療重症促血栓性急性呼吸衰竭的安全性、劑量探索與療效；與血栓性體質的關聯尚待確認，目前無結果 |

---

## 文獻證據

以下為血栓性體質相關文獻（共檢索 20 篇，列出較具代表性者，皆為個案報告，無 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36163059](https://pubmed.ncbi.nlm.nih.gov/36163059/) | 2022 | Case report | J Natl Med Assoc | 鐮刀型貧血患者急性視網膜中央動脈阻塞的全身溶栓 |
| [41876387](https://pubmed.ncbi.nlm.nih.gov/41876387/) | 2026 | Case report | Catheter Cardiovasc Interv | 抗凝血酶 III 缺乏者對全身溶栓抗性，經導管導向溶栓挽救 |
| [26588446](https://pubmed.ncbi.nlm.nih.gov/26588446/) | 2016 | Case report | Blood Coagul Fibrinolysis | 遺傳性抗凝血酶缺乏合併合成代謝類固醇導致肺栓塞，接受導管導向溶栓 |
| [29196364](https://pubmed.ncbi.nlm.nih.gov/29196364/) | 2017 | Case report/Review | Clin Med | 懷孕期缺血性中風使用 alteplase 溶栓 |
| [37241103](https://pubmed.ncbi.nlm.nih.gov/37241103/) | 2023 | Case report | Medicina | 產後廣泛靜脈血栓的處置 |
| [37041727](https://pubmed.ncbi.nlm.nih.gov/37041727/) | 2023 | Case report | Am J Case Rep | 高風險肺栓塞，後診斷為原發性抗磷脂症候群與高同半胱胺酸血症 |
| [26422681](https://pubmed.ncbi.nlm.nih.gov/26422681/) | 2015 | Case report | Am J Case Rep | 14 歲遺傳性血栓性體質女孩的口服避孕藥相關致命性肺栓塞 |
| [19260122](https://pubmed.ncbi.nlm.nih.gov/19260122/) | 2009 | Case report | Am J Hematol | 有 HIT 病史患者使用 argatroban 與導管導向 alteplase 溶栓處理肢體與移植物血栓 |

另有冠狀動脈狹窄（排名第 9）方面的文獻，包含 1993 年一項 alteplase 對照安慰劑、針對靜息性胸痛的雙盲 RCT（[PMID 8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/)）與 1991 年難治性不穩定型心絞痛的 RCT（[PMID 1782951](https://pubmed.ncbi.nlm.nih.gov/1782951/)），但內容多為重述已核准的心肌梗塞用途，且早於現行以 PCI 為主的照護模式。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37894 | ACTILYSE LYOPHILISED PDR FOR IV INJ 20MG | 靜脈注射用凍晶粉 | 許可證資料未載明 |
| HK-30511 | ACTILYSE LYOPHILISED PDR FOR IV INF 50MG | 靜脈輸注用凍晶粉 | 許可證資料未載明 |

兩張許可證皆為單一成分製劑，狀態有效，廠商為 Boehringer Ingelheim (HK) Ltd。

---

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下列出部分主要者。
  - 重大（Major）：Abciximab、Apixaban、Fondaparinux、Acalabrutinib、Anisindione、Deferasirox、Ibritumomab tiuxetan、Tositumomab
  - 中度（Moderate）：Acetylsalicylic acid、Ibuprofen、Ketorolac、Fosinopril、Aminocaproic acid、Fluvoxamine、Aprotinin 等

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（排名第 1 預測）；血栓性體質可作為研究問題進一步探討。

**理由：**
- 排名前三的預測屬於已核准心肌梗塞的亞型，並非新適應症，也缺乏亞型專屬證據。
- 血栓性體質目前僅有個案報告與一項關聯尚待確認的 Phase 2 試驗；alteplase 無法矯正潛在凝血缺陷，且出血風險與溶栓抗性（如抗凝血酶缺乏）都需考量。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症文字
- 補充詳細的作用機轉資料
- 確認 NCT05540834 的族群與血栓性體質的實際關聯
- 針對特定血栓性體質亞型設計前瞻性或對照研究，並建立出血風險評估與監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

