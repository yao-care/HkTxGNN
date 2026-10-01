---
layout: default
title: Simvastatin
parent: 高證據等級 (L1-L2)
nav_order: 800
evidence_level: L1
indication_count: 5
---

# Simvastatin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Simvastatin：從降血脂治療到家族性高膽固醇血症

## 一句話總結

Simvastatin 是一種史他汀（statin）類降血脂藥，在香港已有 20 張許可證。
TxGNN 模型預測它可能對**家族性高膽固醇血症 (Familial Hypercholesterolemia)** 有效，
目前有 **19 個臨床試驗**和 **18 篇文獻**支持這個方向，其中多個為已完成的 Phase 3 試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證與 DrugBank 資料均未載明（藥理上屬降血脂藥） |
| 預測新適應症 | 家族性高膽固醇血症 (Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前沒有資料，以下機轉說明來自本次分析的推論。Simvastatin 抑制 HMG-CoA 還原酶，降低肝臟的膽固醇合成，並使肝細胞表面的 LDL 受器增加，加速血中 LDL-C 清除。

家族性高膽固醇血症的核心問題是 LDL-C 清除不足，通常由 LDLR、APOB 或 PCSK9 變異造成。異合子型（heterozygous）患者仍保有部分 LDL 受器功能，所以透過 statin 提高受器表現，機轉上直接對應病因。Simvastatin 本身就是 FH 的既有降血脂選項，與預測方向一致。

原適應症欄位為空，這是資料缺口，不構成反對證據。限制在於同合子型（homozygous）且為 LDLR 完全無功能的患者，statin 效果有限，常需合併 ezetimibe 或 PCSK9 抑制劑。

## 臨床試驗證據

以下為與 simvastatin 關聯度較高的 10 項（共 19 項）。多數試驗中 simvastatin 是合併用藥或背景治療，並非單獨受試藥物。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | 完成 | 720 | ENHANCE：ezetimibe + 高劑量 simvastatin 對比單用 simvastatin，評估異合子型 FH 頸動脈內中膜粥樣硬化進展 |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | 完成 | 248 | ezetimibe 與 simvastatin 併用，用於 10-17 歲異合子型 FH 青少年的療效與安全性 |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | 完成 | 199 | SUPREME：niacin ER + simvastatin 對比 atorvastatin，比較高血脂/混合型血脂異常的 HDL-C 提升（是否限於 FH 未確認） |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 完成 | 44 | ezetimibe 加 atorvastatin 或 simvastatin，同合子型 FH 的 24 個月長期安全性延伸研究 |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 完成 | 50 | ezetimibe 加 atorvastatin 或 simvastatin，同合子型 FH 的療效與安全性 |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | 完成 | 442 | rosuvastatin 與 simvastatin 對腎臟影響的比較，族群含異合子型 FH |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | 完成 | 194 | colesevelam 用於穩定使用 statin（含 simvastatin）的兒童異合子型 FH，simvastatin 為背景治療 |
| [NCT00475826](https://clinicaltrials.gov/study/NCT00475826) | 未分類 | 未知 | 未提供 | 異合子型 FH 患者使用 statin 加 ezetimibe 時，乳糜微粒代謝與亞臨床動脈硬化的關係 |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | 完成 | 486 | alirocumab 加既有降脂治療用於異合子型 FH，simvastatin 可能為背景治療，屬間接證據 |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | 完成 | 216 | alirocumab 加穩定 statin 治療用於異合子型 FH 或高心血管風險者，屬間接證據 |

## 文獻證據

以下為 10 篇代表性文獻（共 18 篇）。部分文獻的摘要在資料中被截斷，主要發現僅依可見內容摘要。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | N Engl J Med | simvastatin 單用對比合併 ezetimibe，用於 FH；探討對動脈粥樣硬化進展的影響（摘要未載結果） |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | 系統性回顧 | Cochrane Database Syst Rev | 評估 statin 用於兒童 FH 的證據 |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | 臨床比較研究 | Nutr Metab Cardiovasc Dis | 比較 atorvastatin 與 simvastatin 在異合子型 FH 達成 LDL-C 目標的效果 |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | 未分類 | J Am Coll Cardiol | 量化 statin 在異合子型 FH 對冠心病事件與死亡率的降低幅度 |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | 評估 simvastatin 用於 FH 的效益與風險，強調長期安全性與耐受性 |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | simvastatin 用於 FH 患者的效益與風險 |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | 橫斷面/世代研究 | J Clin Med | 26 名 FH 兒童（13 名服用 simvastatin 10 mg）的細胞免疫參數比較 |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | 指引 | J Am Coll Cardiol | 2026 ACC/AHA 等學會血脂異常處置指引，取代 2018 膽固醇指引 |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | 指引 | Endocr Pract | AACE/ACE 血脂異常處置與心血管疾病預防指引 |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | 回溯性研究 | Atherosclerosis | 斯洛伐克 FH 治療現況，指出 statin 為核心治療，但不少患者治療不足 |

## 香港上市資訊

共 20 張許可證，以下列出 5 張。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51793 | APO-SIMVASTATIN TAB 40MG | — | — |
| HK-55637 | VAS TAB 40MG | — | — |
| HK-56763 | JMP SIMVASTATIN TAB 20MG | — | — |
| HK-59425 | PEAUSOIN SIMVASTATIN TAB 10MG | — | — |
| HK-58993 | SIMPLAQOR TAB 10MG | — | — |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多項已完成的 Phase 3 試驗（如 ENHANCE、ezetimibe 併用 simvastatin 的青少年試驗）直接涉及 simvastatin 與 FH，並有 RCT 與系統性回顧支持，機轉上也直接對應。不過多數試驗中 simvastatin 是合併治療或背景用藥，且香港仿單的安全資料仍有缺口，因此需附帶防護條件。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症（目前列為阻斷性缺口，不補齊無法進入安全性篩查）
- 確認香港許可證的核准適應症是否已涵蓋 FH
- 補充 DrugBank 的作用機轉資料
- 納入使用條件：
  - 同合子型且 LDLR 完全無功能者效果有限，常需合併 ezetimibe 或 PCSK9 抑制劑
  - 兒童與青少年需依年齡調整劑量並監測
  - 注意高劑量時的肌病風險與 CYP3A4 藥物交互作用
- 自家族性高膽固醇血症（顯性遺傳）的預測（排名第 4）共用同一批證據，可一併評估；其餘預測（腦幹梗塞、CETP 缺乏症、CYP7A1 缺乏所致高膽固醇血症）僅有模型預測，證據等級為 L5，建議暫緩（Hold）

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

