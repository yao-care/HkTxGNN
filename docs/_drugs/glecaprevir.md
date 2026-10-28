---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
monitor_inn: "GLECAPREVIR"
predicted_indications: ["HIV infectious disease", "hepatitis B virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "Kyasanur forest disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Glecaprevir：預測新適應症為HIV 感染（證據等級 L5）。原適應症：慢性 C 型肝炎病毒感染"
---

# Glecaprevir
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

## Glecaprevir：從慢性 C 型肝炎到 HIV 感染
{: .text-alpha }

## 一句話總結

Glecaprevir 是 C 型肝炎病毒 NS3/4A 蛋白酶抑制劑，知識圖譜中記錄的原適應症為慢性 C 型肝炎病毒感染。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有關，但現有的 6 個臨床試驗與文獻都是在 HIV/HCV 共感染族群中治療 C 型肝炎，**並沒有直接研究 glecaprevir 對 HIV 本身的作用**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎病毒感染（知識圖譜記錄；香港許可證未載明適應症文字） |
| 預測新適應症 | HIV 感染 |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 glecaprevir 是 C 型肝炎病毒 NS3/4A 蛋白酶抑制劑，與 pibrentasvir 組成複方使用，用於治療 C 型肝炎。

HIV 與 HCV 常同時感染，在疾病網絡與抗病毒藥物上有許多共同鄰近節點，這很可能是 TxGNN 給出高分的原因。但 glecaprevir 沒有已知的直接抗 HIV 活性，相關試驗中藥物治療的是 HCV 部分。若有任何益處，也屬間接，例如清除 HCV 後降低共感染者的心血管與肝臟風險。

因此，這個預測應視為待驗證的研究假說，而非有機轉支持的新適應症。

## 臨床試驗證據

以下試驗都是在含 HIV 共感染的 HCV 族群中進行，**沒有一項直接以 HIV 感染作為研究疾病**，終點皆為 HCV 治癒或相關結果。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | 完成 | 153 | EXPEDITION-2：評估 glecaprevir/pibrentasvir 用於 HCV 與 HIV-1 共感染成人的療效與安全性 |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | 完成 | 546 | 亞洲非肝硬化 HCV 成人（含或不含 HIV 共感染）的安慰劑對照試驗 |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | 完成 | 160 | 亞洲代償性肝硬化 HCV 成人（含或不含 HIV 共感染）的開放標籤試驗 |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | 完成 | 83 | 新近感染 HCV（含或不含 HIV）的直接作用抗病毒藥物先導試驗 |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 完成 | 87 | HIV/HCV 共感染者清除 HCV 後的心血管風險變化 |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | 完成 | 45 | 急性 HCV（含或不含 HIV-1 共感染）給予 4 週 G/P 的療效 |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | 招募中 | 30 | 懷孕期 HCV 女性（含或不含 HIV）使用 G/P 的藥動學與安全性 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | 世代研究 | J Antimicrob Chemother | 評估 G/P 在臨床實務中用於 HIV/HCV 共感染者的反應 |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | 世代研究 | Clin Exp Hepatol | HIV/HCV 共感染且使用 bictegravir/emtricitabine/TAF 者，G/P 的真實世界療效與安全性 |
| [41297677](https://pubmed.ncbi.nlm.nih.gov/41297677/) | 2026 | 單臂試驗 | J Hepatol | 8 週 G/P 用於急性 C 型肝炎成人 |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | 世代研究 | Adv Ther | 8 週 G/P 用於未治療的代償性肝硬化患者之真實世界使用 |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | 藥動學研究 | J Infect Dis | G/P 與 HIV 抗反轉錄病毒藥物併用的藥物交互作用 |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | 系統性回顧與統合分析 | Int J Antimicrob Agents | G/P 治療 HCV 基因型 1-6 的整體 SVR12 為 97.8% |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | 回顧 | Future Microbiol | G/P 治療慢性 HCV 的回顧 |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | 回顧 | Expert Opin Pharmacother | HCV 蛋白酶抑制劑治療回顧，提及 HIV 共感染比例 |

這些文獻同樣以 HCV 治療為主，未顯示 glecaprevir 具有抗 HIV 效果。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65653 | MAVIRET TABLETS | 未載明 | 未載明 |

## 安全性考量

- **藥物交互作用**：共查得 57 筆。主要為：
  - **嚴重**：Rosuvastatin、Simvastatin、Edoxaban
  - **中度**：Dexamethasone、Esomeprazole、Omeprazole、Apixaban、Betrixaban、Cobicistat、Deferasirox、Metreleptin、Naldemedine、Troglitazone 等
  - **輕度**：Fidaxomicin、Naloxegol、Prucalopride、Indacaterol

其他警語與禁忌症請參考原廠仿單。若用於 HIV 共感染者，需特別留意與抗反轉錄病毒藥物的交互作用。此外，HCV 直接作用抗病毒藥物治療期間有 B 型肝炎再活化的安全考量。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有支持證據都是 HIV/HCV 共感染者的 HCV 治療，沒有研究直接探討 glecaprevir 對 HIV 本身的作用，且機轉上無依據，因此證據等級僅為 L5。
- 高分很可能反映疾病網絡相似性，而非藥物標的生物學。

**若要推進需要：**
- 體外實驗檢驗 glecaprevir 對 HIV 複製或 HIV 蛋白酶的抑制活性
- 詳細的作用機轉資料
- 取得香港許可證的仿單，確認核准適應症、警語與禁忌症
- 若目標是共感染者的間接獲益，應改以「HCV 治療對 HIV 共感染者的結果」作為研究問題，而非 HIV 新適應症

### 其他預測適應症簡述

排名第 2 至第 10 的預測（B 型肝炎、猴免疫缺陷病毒感染、貓後天免疫缺乏症候群、E 型肝炎、動物病毒性肝炎、A 型肝炎、鄂木斯克出血熱、凱薩努爾森林病、一種罕見神經發展障礙）皆無直接研究支持 glecaprevir 對這些疾病有效，也缺乏機轉依據，建議全部維持 Hold。其中 A 型肝炎相關的大量試驗實為 HCV 試驗，不構成 HAV 證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

