---
layout: default
title: Zolpidem
parent: 僅模型預測 (L5)
nav_order: 960
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Zolpidem：預測新適應症為入睡與維持睡眠障礙 (Sleep Disorder, Initiating and Maintaining Sleep)（證據等級 L5）。原適應症：失眠 (Insomnia)"
monitor_inn: "Zolpidem"
predicted_indications: ["sleep disorder, initiating and maintaining sleep", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Zolpidem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Zolpidem：從失眠到入睡與維持睡眠障礙

## 一句話總結

Zolpidem 是一種非苯二氮平類安眠藥，原本用於治療失眠。
TxGNN 模型預測它可能對**入睡與維持睡眠障礙 (Sleep Disorder, Initiating and Maintaining Sleep)** 有效，目前有 **20 篇文獻**支持這個方向，但**無臨床試驗登記**。
需要注意：此預測與原適應症（失眠）本質上相同，屬於對現有用途的確認，並非真正的藥物再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 失眠 (Insomnia) |
| 預測新適應症 | 入睡與維持睡眠障礙 (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L3（文獻以系統性回顧、網絡統合分析與指引為主，無已完成的 Phase 3 RCT 直接以 Zolpidem 為研究藥物） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Zolpidem 是 GABA-A 受體的正向異位調節劑，對含 α1 次單元的受體有較高親和力，主要產生鎮靜與催眠作用，因此能直接改善入睡困難與睡眠維持困難。需說明的是，目前缺乏詳細的作用機轉資料，上述機轉來自一般藥理學知識，而非本次整理的資料。

「入睡與維持睡眠障礙」基本上就是失眠的臨床描述，與 Zolpidem 的原適應症高度重疊。因此 TxGNN 的高分預測，更多反映的是模型正確辨識出既有的適應症。

除此之外，模型還預測了其他兩個適應症，但證據薄弱，目前建議暫緩（Hold）：
- **嬰兒良性陣發性斜頸**：未發現合理的機轉關聯。此病屬偏頭痛譜系的自限性疾病，GABA-A 調節在其病理中沒有已知角色，高分可能只是圖譜上的鄰近關係，且無任何文獻或試驗支持。
- **懼曠症**：只有間接、薄弱的理由。Zolpidem 的 α1 選擇性使其以鎮靜為主，抗焦慮效果極小，標準治療為 SSRI/SNRI 與暴露式認知行為治療，且無支持證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下依證據強度優先，列出最相關的 10 篇：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | 網絡統合分析 | Lancet | 比較各種藥物對成人失眠的急性與長期療效 |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | 臨床實務指引 | J Clin Sleep Med | 美國睡眠醫學會針對慢性失眠個別藥物的建議 |
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Zolpidem ER 作為對照藥，與 lemborexant 及安慰劑比較，用於老年失眠 |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | 網絡統合分析 | J Manag Care Spec Pharm | 比較 lemborexant 與其他失眠治療的療效與安全性 |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | J Fam Pract | 失眠處置的回顧與更新，強調失眠應視為獨立疾病治療 |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | 老年失眠的藥物處置建議 |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | 安眠藥在老年人的安全性與療效回顧 |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z 類藥物（含 zolpidem）有療效證據，但有認知損害、耐受性、依賴等副作用 |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem 為美國最常用的安眠藥 |
| [16696581](https://pubmed.ncbi.nlm.nih.gov/16696581/) | 2006 | Review | CNS Drugs | Zolpidem 緩釋劑型針對入睡與睡眠維持困難的療效 |

---

## 香港上市資訊

本藥在香港共有 19 張有效單方許可證，無已註銷者。以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36433 | STILNOX TAB 10MG（Sanofi） | 錠劑 | 未提供 |
| HK-56391 | STILNOX CR MODIFIED-RELEASE TAB 6.25MG（Sanofi） | 緩釋錠 | 未提供 |
| HK-56392 | STILNOX CR MODIFIED-RELEASE TAB 12.5MG（Sanofi） | 緩釋錠 | 未提供 |
| HK-65359 | ZOLPIDEM SANDOZ TABLETS 10MG | 錠劑 | 未提供 |
| HK-61859 | ZOLPIDEM STADA TABLETS 10MG | 錠劑 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的相關疾病風險**（來自知識圖譜的藥物－疾病禁忌關聯，並非仿單文字）：焦慮症、神經症、輕度憂鬱症、肝病、膽囊疾病、阻塞性睡眠呼吸中止症、睡眠呼吸中止症候群、先天性中樞低通氣症候群、健忘症、逆行性失憶、物質相關疾患與物質濫用／依賴、注意力不足過動症。
- **藥物交互作用**：共查得 100 筆，以下為主要項目：
  - **重度**：Morphine、Morphine (liposomal)（合併使用有中樞神經與呼吸抑制風險）
  - **中度**：Bupropion、Aprepitant、Dexamethasone、Cimetidine、Clarithromycin、Dronabinol、Nabilone、Metoclopramide、Miconazole、Clotrimazole、Opium 等
- 文獻亦指出 Z 類藥物可能有認知損害、耐受性、停藥後反彈性失眠、跌倒與車禍風險、濫用與依賴，老年人尤需謹慎。

仿單中的警語與禁忌症資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對「入睡與維持睡眠障礙」）

**理由：**
- 此適應症與 Zolpidem 原有的失眠適應症本質相同，文獻中有系統性回顧、網絡統合分析與臨床指引支持，且藥品已在香港廣泛上市。但這不屬於真正的藥物再利用，證據也多為間接支持，故以附帶防護措施的方式推進。
- 另兩個預測（嬰兒良性陣發性斜頸、懼曠症）缺乏機轉與證據支持，建議 **Hold**。

**若要推進需要：**
- 取得香港衛生署許可證的核准適應症文字與仿單警語、禁忌症
- 補充詳細的作用機轉（MOA）資料
- 針對老年人、肝病、呼吸功能不全及物質依賴病史族群，建立安全性監測與用藥限制計畫
- 對重度交互作用（如鴉片類藥物）訂定併用管理原則
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

