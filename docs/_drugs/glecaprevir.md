---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 5
---

# Glecaprevir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Glecaprevir：從 C 型肝炎到 HIV 感染

## 一句話總結

Glecaprevir 是 C 型肝炎病毒（HCV）NS3/4A 蛋白酶抑制劑，在香港以 Glecaprevir/Pibrentasvir 複方（MAVIRET）上市，用於治療 C 型肝炎。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有效。
目前有 **15 個相關臨床試驗**和 **20 篇文獻**與這個方向有關，但全部是 HCV 治療研究，**沒有任何研究顯示它對 HIV 本身有效**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明；依臨床試驗與文獻推斷為慢性 C 型肝炎（HCV） |
| 預測新適應症 | HIV 感染 (HIV infectious disease) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L4（依 Evidence Pack 評級；實際上沒有針對 HIV 本身的療效證據，僅有 HIV/HCV 共感染族群的 HCV 研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Glecaprevir 是 Glecaprevir/Pibrentasvir 複方的一部分，是 HCV 專一的 NS3/4A 絲胺酸蛋白酶抑制劑。它在 C 型肝炎的療效已被大量研究證實，例如一項納入 13 個研究、3,082 名病人的統合分析，整體 SVR12 為 97.8%。

**這個預測在機轉上缺乏支持。** HIV-1 蛋白酶屬於天門冬胺酸蛋白酶，結構與作用機轉都與 HCV 的 NS3/4A 絲胺酸蛋白酶不同，文獻中也沒有 Glecaprevir 抗 HIV 活性的紀錄。模型的高分較可能來自知識圖譜中「蛋白酶抑制劑類抗病毒藥」以及「HIV/HCV 共感染」的關聯，並非真實的抗病毒機轉。

所有相關試驗與文獻都是在 HIV 感染者身上治療 HCV，證明的是 HCV 治癒與用藥安全，不是 HIV 控制。唯一站得住腳的連結是共感染管理，包括與抗反轉錄病毒藥物的交互作用，以及 HCV 治癒後的心血管風險等，這些都是間接關係。

---

## 臨床試驗證據

以下為與 HIV 共感染族群最相關的 10 個試驗。**所有試驗的主要終點都是 HCV 的療效或安全性，沒有任何一個以 HIV 病毒控制為終點。**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | 完成 | 153 | EXPEDITION-2：ABT-493/ABT-530 用於 HCV 基因型 1–6 合併 HIV-1 共感染成人的療效與安全性 |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | 完成 | 546 | 隨機、雙盲、安慰劑對照；亞洲無肝硬化 HCV 成人，可含 HIV 共感染 |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | 完成 | 160 | 開放標示；亞洲代償性肝硬化 HCV 成人，可含 HIV 共感染 |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | 完成 | 45 | PURGE-C：G/P 治療 4 週用於急性 HCV，可含 HIV-1 共感染；終點為 HCV 療效 |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 完成 | 87 | HIV/HCV 共感染者根除 HCV 後的心血管風險；終點非 HIV 控制 |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | 完成 | 83 | 近期感染 HCV（可含 HIV 共感染）的多種 DAA 方案先導研究；不專屬於 Glecaprevir |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | 尚未招募 | 30 | 懷孕期開始使用 G/P 的藥動學與安全性，可含 HIV 共感染孕婦 |
| [NCT04189627](https://clinicaltrials.gov/study/NCT04189627) | 不適用 | 完成 | 99 | 俄羅斯 12 至未滿 18 歲青少年真實世界研究，含 HCV/HIV 共感染亞群 |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | 不適用 | 完成 | 17 | 針具交換站遠距醫療，提供 MOUD、HIV PrEP 與 C 肝治療；屬服務模式研究，無 HIV 抗病毒療效資料 |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | 完成 | 33 | MAGELLAN-3：G/P 併用 sofosbuvir 與 ribavirin，用於 AbbVie 研究中病毒學失敗的 HCV 病人 |

---

## 文獻證據

沒有 RCT。以下依統合分析、綜述、世代研究、藥物交互作用研究、個案報告排序。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | 系統性回顧與統合分析 | Int J Antimicrob Agents | 納入 13 個研究、3,082 名病人，G/P 治療 HCV 基因型 1–6 的整體 SVR12 為 97.8% |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | 綜述 | Future Microbiol | G/P 治療慢性 HCV 的療效與安全性回顧 |
| [31537106](https://pubmed.ncbi.nlm.nih.gov/31537106/) | 2020 | 綜述 | Ann Pharmacother | 回顧 G/P 的藥理、藥動學、療效、安全性、劑量與成本，為首個適用 12 歲以上的 8 週泛基因型 HCV 療法 |
| [30090878](https://pubmed.ncbi.nlm.nih.gov/30090878/) | 2018 | 綜述 | Drugs Today | G/P 用於成人慢性 HCV 基因型 1–6 的核准與臨床資料 |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | 綜述 | Hepatol Int | G/P 擴大治療可及性，並降低 HCV 療程與成本 |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | 世代研究 | J Antimicrob Chemother | 探討 G/P 在 HIV/HCV 共感染病人臨床實務中的反應（終點為 HCV 的 SVR） |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | 世代研究 | Adv Ther | 真實世界中，未曾治療的代償性肝硬化病人使用 8 週 G/P 的結果（HCV） |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | 藥物交互作用研究 | J Infect Dis | 評估 G/P 與 HIV 抗反轉錄病毒藥物併用時的交互作用，是共感染治療的重要參考 |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | 個案報告 | Clin J Gastroenterol | 日本血友病病人合併 HIV 與 HCV 基因型 4a，經 G/P 成功治療 HCV |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | 個案報告 | J Prev Med Hyg | HIV 感染者同時使用 G/P 與 ART 後出現間接高膽紅素血症與黃疸，義大利首例 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65653 | MAVIRET TABLETS（廠商：ABBVIE LIMITED） | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Glecaprevir 針對 HCV 的 NS3/4A 蛋白酶，與 HIV 的蛋白酶不同，沒有任何抗 HIV 活性的證據。TxGNN 的高分應視為圖譜關聯造成的假訊號。
- 所有試驗與文獻都是在 HIV 感染者身上治療 HCV，屬於共感染管理，不是老藥新用。

其他排名較高的預測也屬同一類型，建議一併 Hold：
- **B 型肝炎**：沒有可用的作用靶點，試驗皆為 HCV 研究。臨床上 HBV 是 DAA 治療時需注意再活化的安全議題，不是治療標的。
- **猴免疫缺乏病毒感染（SIV）**、**貓後天免疫缺乏症候群（FIV）**：沒有任何試驗、文獻或前臨床資料，且為動物模式或獸醫適應症。
- **E 型肝炎**：關聯的試驗全是 HCV 研究，沒有 HEV 終點，判斷為關鍵字誤配。

**若要推進需要：**
- 先做體外實驗，確認 Glecaprevir 對 HIV-1 蛋白酶或病毒複製有無抑制活性。沒有這項證據，不建議投入臨床研究。
- 取得 DrugBank 的作用機轉資料與香港衛生署仿單，補齊警語、禁忌與適應症。
- 若目標是共感染管理，改以「HIV/HCV 共感染病人的 HCV 治療」為題，整理與抗反轉錄病毒藥物的交互作用（如 PMID 31504702）與 HBV 再活化風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

