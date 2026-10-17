---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 825
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sofosbuvir：預測新適應症為B 型肝炎病毒感染（證據等級 L5）。原適應症：慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection)"
monitor_inn: "SOFOSBUVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever"]
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Sofosbuvir：從慢性 C 型肝炎到 E 型肝炎（及其他病毒性肝炎）

## 一句話總結

Sofosbuvir 是 C 型肝炎病毒 (HCV) 的核苷酸類聚合酶抑制劑，原本用於慢性 C 型肝炎治療。
TxGNN 模型對 B 型肝炎的預測分數最高，但綜合證據後，**E 型肝炎 (Hepatitis E virus infection)** 才是機轉與臨床線索較合理的方向。
目前 E 型肝炎有 **2 個臨床試驗**（其中 1 個直接相關）和 **約 20 篇文獻**，但臨床效果並不穩定。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection) |
| 預測新適應症 | B 型肝炎病毒感染 (TxGNN 排名第 1)；E 型肝炎為證據較佳的候選 |
| TxGNN 預測分數 | B 型肝炎 99.77%；E 型肝炎 99.49% |
| 證據等級 | B 型肝炎 L2（資料編譯結果；實為 HCV/HBV 共感染資料，不支持直接抗 HBV 療效）；E 型肝炎 L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | B 型肝炎：Hold（僅屬研究問題）；E 型肝炎：Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，sofosbuvir 是 HCV NS5B RNA 依賴性 RNA 聚合酶的核苷酸類似物抑制劑，其活性三磷酸代謝物可中止病毒 RNA 合成。

**B 型肝炎：** HBV 是 DNA 病毒，透過 RNA 中間體以反轉錄酶/聚合酶複製，與 sofosbuvir 的作用標的並無明確的直接機轉關聯。TxGNN 的極高分數可能反映的是「肝炎／抗病毒」的共同脈絡，而非真正的抗 HBV 活性。現有臨床資料多為 HCV/HBV 共感染，重點在 HBV 再活化的安全風險，而非療效。不過，一項 Phase 2 研究 (ledipasvir/sofosbuvir 用於 HBV 單一感染) 觀察到 HBsAg 的些微下降，僅屬探索性訊號。

**E 型肝炎：** HEV 是正股單股 RNA 病毒，複製依賴 RNA 依賴性 RNA 聚合酶，機轉上對核苷酸類似物具潛在敏感性。體外研究顯示 sofosbuvir 可抑制 HEV 複製，與 ribavirin 併用有加成效果；兔子模型中高劑量 sofosbuvir 亦有抑制作用。然而臨床上，慢性 E 型肝炎病人使用後病毒量雖初期下降，卻未達持續病毒學反應，並曾觀察到抗藥性相關變異。

**其他：** A 型肝炎僅有體外證據；Omsk 出血熱 (同屬黃病毒科) 僅有理論推測，無任何研究；「動物病毒性肝炎」並非具臨床意義的人類適應症。

---

## 臨床試驗證據

以下以 E 型肝炎 (證據較佳的候選) 為主，並附 B 型肝炎中相關性較高的試驗。

**E 型肝炎**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03282474](https://clinicaltrials.gov/study/NCT03282474) | Phase 2 | 完成 | 10 | HepNet 單臂前導試驗，sofosbuvir 治療慢性 E 型肝炎；已發表結果顯示病毒量初期下降，但無持續病毒學反應 |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | 未知 | 25 | HIV/HCV 共感染病人轉換抗病毒方案研究，與 HEV 關聯薄弱且間接 |

**B 型肝炎（相關性較高者）**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | 完成 | 21 | Ledipasvir/sofosbuvir 12 週用於 HBV 感染者，單臂小型研究 |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 完成 | 23 | HCV/HBV 共感染接受直接抗病毒藥物，評估 HBV 再活化，並非 HBV 療效 |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | SOF/VEL 合併預防性 TAF，用於 HCV/HBV 共感染，重點為管理 HBV 再活化 |

其餘 B 型肝炎與 A 型肝炎名下列出的試驗，多為 HCV 治療或公共衛生計畫，與該新適應症無直接關聯，故不列入。動物病毒性肝炎與 Omsk 出血熱目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35814503](https://pubmed.ncbi.nlm.nih.gov/35814503/) | 2022 | Review | J Clin Exp Hepatol | 整理 sofosbuvir 治療 E 型肝炎的體外與體內證據 |
| [37334496](https://pubmed.ncbi.nlm.nih.gov/37334496/) | 2023 | 試驗分析 | Hepatology | NCT03282474 試驗中，治療使病毒量初期下降但未達持續反應，並出現抗藥性相關變異 |
| [36942308](https://pubmed.ncbi.nlm.nih.gov/36942308/) | 2023 | 病例報告 | IDCases | Ribavirin 難治的持續性 HEV，使用 ledipasvir/sofosbuvir 加 ribavirin 後有反應 |
| [31404927](https://pubmed.ncbi.nlm.nih.gov/31404927/) | 2019 | 病例系列 | Open Forum Infect Dis | 3 位器官移植者在 ribavirin 失敗後加用 sofosbuvir，未達持續病毒學反應 |
| [26408347](https://pubmed.ncbi.nlm.nih.gov/26408347/) | 2016 | 體外研究 | Gastroenterology | Sofosbuvir 抑制 HEV 基因型 3 複製，與 ribavirin 有加成效果 |
| [35247472](https://pubmed.ncbi.nlm.nih.gov/35247472/) | 2022 | 動物/體外 | Antiviral Res | 高劑量 sofosbuvir 及合併 ribavirin 在兔子急性 HEV 模型中抑制病毒複製 |
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 | J Med Virol | Ledipasvir/sofosbuvir 用於 HBV 單一感染者，觀察 HBsAg 下降 |
| [29653132](https://pubmed.ncbi.nlm.nih.gov/29653132/) | 2018 | 體外研究 | Antiviral Res | Sofosbuvir 在細胞模型中抑制 A 型肝炎病毒複製 |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | 前瞻性觀察 | J Viral Hepat | 癌症病人接受 HCV 直接抗病毒藥物時的 HBV 再活化風險 |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | 病例報告 | J Med Case Rep | SOF/VEL 治療 HCV 期間發生 HBV 再活化 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65046 | EPCLUSA TABLETS 400MG/100MG | 錠劑 | （資料未載明） |
| HK-65775 | VOSEVI TABLETS | 錠劑 | （資料未載明） |

兩張許可證均由 Gilead Sciences Hong Kong Limited 持有，狀態皆為有效。

---

## 安全性考量

- **藥物交互作用**：共查得 8 項，其中：
  - **重大 (Major)**：Apalutamide、Enzalutamide、Lorlatinib
  - **中度 (Moderate)**：Fostamatinib、Warfarin、Dicoumarol、Encorafenib
  - **輕微 (Minor)**：Cyclosporine
- **HBV 再活化**：現有文獻一致指出，HCV/HBV 共感染者接受 sofosbuvir 為基礎的直接抗病毒藥物時，有 HBV 再活化風險，通常需搭配 HBV 核苷（酸）類似物（如 TAF）預防。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：**
- **E 型肝炎：Proceed with Guardrails**
- **B 型肝炎：Hold（僅屬研究問題）**
- **A 型肝炎、Omsk 出血熱、動物病毒性肝炎：Hold**

**理由：**
- B 型肝炎雖然 TxGNN 分數最高，但機轉上缺乏直接依據，現有臨床資料主要是共感染與再活化安全議題，並非療效證據。
- E 型肝炎有機轉合理性、體外及動物證據及一項直接臨床前導試驗，但臨床結果顯示無持續病毒學反應並有抗藥性變異，因此只適合在嚴格監測下作為 ribavirin 難治病人的探索性選項，而非常規適應症。

**若要推進需要：**
- 取得香港核准適應症文字與仿單的警語、禁忌症資料
- 取得詳細作用機轉資料（MOA）
- E 型肝炎：設計較大規模、有對照組的試驗，評估 sofosbuvir 合併 ribavirin 的療效及抗藥性風險，並釐清最適劑量
- B 型肝炎：需先有獨立的機轉或體外證據，才有必要投入臨床研究；同時確認 HBV 再活化的篩檢與預防流程
- 針對 A 型肝炎等僅有體外或理論依據的方向，需先累積前臨床及動物證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

