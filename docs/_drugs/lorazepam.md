---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 539
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "LORAZEPAM"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Lorazepam：預測新適應症為三叉神經腫瘤 (trigeminal nerve neoplasm)（證據等級 L5）。香港藥劑製品註冊：9 張（有效 9 張）"
---

# Lorazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Lorazepam: 三叉神經腫瘤 (trigeminal nerve neoplasm)
{: .text-alpha }

## 一句話總結

Lorazepam 是苯二氮平類（benzodiazepine）藥物，原本用於焦慮症與多種癲癇（如癲癇持續狀態、失神癲癇、Lennox-Gastaut 症候群）。
TxGNN 模型預測分數最高的新適應症是**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)**，但目前**沒有任何臨床試驗或文獻**支持。
相對上，**失眠 (Insomnia)** 有 **16 篇文獻**，證據較多，較值得優先探討。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 三叉神經腫瘤 (trigeminal nerve neoplasm) |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | 上市中（有效許可證 9 張／共 9 張） |
| 許可證數 | 9 張（有效 9 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Lorazepam 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Lorazepam 透過與腦內 γ-胺基丁酸-A（GABA A ）受體的 benzodiazepine 位點結合，而發揮治療焦慮症的作用，並增強 GABA 介導的突觸抑制。」英文原文："Lorazepam exerts its effect for the treatment of anxiety disorders through binding to the benzodiazepine site of the gamma-aminobutyric acid-A (GABA A ) receptors in the brain and enhances GABA-mediated synaptic inhibition."（[DailyMed: Loreev Xr (lorazepam) prescribing information, Almatica Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=227734c1-bf01-9607-73ea-5a1f38a89bd9)，版本日期 2025-10-08；查閱日期 2026-11-19）。根據已知資訊，Lorazepam 是 GABA-A 受體正向異構調節劑，具有抗焦慮、鎮靜與抗痙攣作用。

就**三叉神經腫瘤**而言，機轉上看不出合理的連結。Lorazepam 對神經腫瘤沒有已知的抗腫瘤作用，0.9987 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。即使在神經腫瘤情境中使用，也只是處理焦慮或癲癇的支持性照護，並非治療腫瘤本身。

其他預測適應症的合理性不同：
- **失眠**：GABA-A 增強帶來的鎮靜催眠作用，機轉上合理，但這更像是苯二氮平類既有鎮靜特性的延伸，並非全新的再利用。
- **閱讀性癲癇、聲源性癲癇、性高潮誘發癲癇**：均屬反射性癲癇，GABA-A 增強可能有抑制作用，與 Lorazepam 既有的癲癇適應症高度相近。

---

## 臨床試驗證據

目前無相關臨床試驗登記（三叉神經腫瘤；其他預測適應症同樣無登記試驗）。

---

## 文獻證據

三叉神經腫瘤：目前無相關文獻。

以下列出與較有證據的預測適應症相關的代表性文獻（摘自失眠、閱讀性癲癇等項目，非三叉神經腫瘤）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | 臨床研究 | Int Clin Psychopharmacol | 比較 Lorazepam 每日三次與睡前單次用於慢性失眠（失眠） |
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | 對照臨床研究 | J Clin Pharmacol | 8 名慢性失眠者雙盲交叉試驗，Lorazepam 2 mg 在多數睡眠指標優於 flurazepam 30 mg（失眠） |
| [11593256](https://pubmed.ncbi.nlm.nih.gov/11593256/) | 2001 | 小型病例系列 | Neurol India | 5 例光敏感性癲癇合併趨日性，Lorazepam 作為輔助治療（閱讀性癲癇，間接證據） |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | J Multidiscip Healthc | COVID-19 患者失眠治療的療效、安全性與藥物交互作用 |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | 慢性失眠藥物回顧 |
| [21951369](https://pubmed.ncbi.nlm.nih.gov/21951369/) | 2011 | Review | CNS Neurosci Ther | 癲癇（非癲癇持續狀態）的急性給藥回顧 |
| [6127668](https://pubmed.ncbi.nlm.nih.gov/6127668/) | 1981 | 前臨床 | Pol J Pharmacol Pharm | 大鼠與小鼠中 Lorazepam 可抑制聲源性癲癇（聲源性癲癇，前臨床） |
| [10744342](https://pubmed.ncbi.nlm.nih.gov/10744342/) | 2000 | 前臨床 | Clin Exp Pharmacol Physiol | 大鼠 Lorazepam 戒斷症候群，聲源性癲癇為戒斷指標，非治療效果 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63368 | PMS-LORAZEPAM TABLETS 0.5MG | 錠劑（資料未載明） | 資料未載明 |
| HK-34394 | SILENCE TAB 1MG | 錠劑（資料未載明） | 資料未載明 |
| HK-35048 | LORANS 2 TAB 2MG | 錠劑（資料未載明） | 資料未載明 |
| HK-63369 | PMS-LORAZEPAM TABLETS 2MG | 錠劑（資料未載明） | 資料未載明 |
| HK-63367 | PMS-LORAZEPAM TABLETS 1MG | 錠劑（資料未載明） | 資料未載明 |

香港共有 9 張有效單方許可證（其餘 4 張為 LORANS 0.5/1、LOTEVEM 0.5/1 mg），無已註銷者。

---

## 安全性考量

- **知識圖譜中標示的禁忌或不宜使用情況**（來自圖譜資料，非仿單原文）：肝衰竭、肝病、肝性腦病變、腎臟病、急性閉角型與開角型青光眼、阻塞性睡眠呼吸中止症、呼吸衰竭、先天性中樞通氣不足症候群、紫質症、物質濫用/依賴等。
- **藥物交互作用**：共查得 100 筆，以下為主要者：
  - **重大 (Major)**：Morphine、Morphine (liposomal)（合用有中樞與呼吸抑制風險）
  - **中度 (Moderate)**：Bupropion、Dronabinol、Nabilone、Metoclopramide、Opium、Sibutramine、Teduglutide
  - **輕微 (Minor)**：多種制酸劑（氫氧化鋁、碳酸鈣、氧化鎂等）
- 苯二氮平類的耐受性、依賴與隔日鎮靜風險，在失眠長期使用上尤其需要留意。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（三叉神經腫瘤）

**理由：**
- 三叉神經腫瘤沒有任何試驗或文獻，機轉上也無抗腫瘤依據，預測分數（0.9987）雖高，但來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據（L5）。

**若要推進需要：**
- 取得 DrugBank 作用機轉資料與香港仿單的警語、禁忌與核准適應症（目前為資料缺口，屬阻擋性）
- 若要研究失眠：需近期、設計良好的 RCT 或系統性回顧，並與現行指引的首選藥物比較
- 若要研究反射性癲癇：需蒐集臨床病例或對照資料，評估 Lorazepam 的實際療效
- 三叉神經腫瘤：除非有新的機轉或臨床證據，不建議投入資源

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Loreev Xr (lorazepam) prescribing information, Almatica Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=227734c1-bf01-9607-73ea-5a1f38a89bd9) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

