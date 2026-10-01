---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 6
---

# Desloratadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Desloratadine：從過敏性疾病（依藥物類別推定）到寒冷性蕁麻疹

## 一句話總結

Desloratadine 是第二代選擇性 H1 抗組織胺，香港許可證未載明適應症，一般用於過敏性疾病。
TxGNN 模型預測它可能對**寒冷性蕁麻疹 (Cold Urticaria)** 有效，
目前有 **3 個臨床試驗**和 **7 篇文獻**支持這個方向，其中包含多項隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 寒冷性蕁麻疹 (Cold Urticaria) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L1（判斷性歸級，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Proceed with Guardrails |

> **證據等級說明：** 目前試驗標示為 Phase 4，並非 Phase 3。L1 是因為有多項直接相關的隨機對照研究，屬判斷性歸級。若嚴格依「≥2 個已完成 Phase 3 RCT」的標準，則不符合。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別，Desloratadine 是選擇性外周 H1 受體反向促效劑（inverse agonist），此機轉是依藥物類別與檢索到的研究推論，並非來自已驗證的仿單。

寒冷性蕁麻疹由肥大細胞和組織胺介導，遇冷會產生風團。H1 受體阻斷可抑制風團形成，機轉上與 Desloratadine 的作用高度吻合。國際指引也建議，標準劑量反應不佳的患者可提高第二代抗組織胺的劑量。

TxGNN 分數很高（0.999），與臨床證據方向一致。已有隨機對照研究直接比較不同劑量 Desloratadine 對寒冷性蕁麻疹的效果。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | 完成 | 33 | 隨機、雙盲、安慰劑對照交叉試驗，比較 5 mg 與 20 mg Desloratadine 對後天性寒冷性蕁麻疹的效果（以熱成像、體積測量等評估）。標題被截斷，確切族群未確認 |
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | 完成 | 30 | 多中心、雙盲、劑量遞增試驗（5、10、20 mg），評估足以抑制寒冷性蕁麻疹症狀的劑量 |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | 完成 | 150 | 比較 5 種抗組織胺對蕁麻疹的抑制效果。未指明蕁麻疹亞型，可能非寒冷性專屬，相關性較間接 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | 隨機、安慰劑對照交叉試驗：高劑量 Desloratadine 相較標準劑量，能減少風團體積並改善冷激發閾值 |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | 以臨界溫度閾值評估 H1 抗組織胺劑量遞增，探討寒冷性蕁麻疹療效反應。摘要未列出結果數據 |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatolog Treat | 12 位寒冷性蕁麻疹患者服用 5 mg Desloratadine 4 天，以冰塊試驗比較治療前後。摘要未列出結果數據 |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | 慢性蕁麻疹的病因、處置與現行及未來治療選項 |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | 探討 Ebastine 用於過敏性鼻炎與慢性特發性蕁麻疹（為另一種抗組織胺，屬間接證據） |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | 黑螞蟻咬傷過敏性休克後出現寒冷誘發蕁麻疹的首例報告 |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case report | J Allergy Clin Immunol Pract | 描述食物依賴性寒冷性蕁麻疹這種物理性蕁麻疹新變異型 |

---

## 香港上市資訊

共 15 張許可證，以下列出 5 張主要許可證。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66259 | LOTARIUS TABLETS 5MG | VICKMANS LABORATORIES LTD |
| HK-68990 | DESLORATADINE TABLETS 5MG | CONTROLLED MEDICATIONS LIMITED |
| HK-66347 | ALLORA 5 TABLETS 5MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-63392 | LORASTAD D FILM-COATED TABLETS 5MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-57332 | LARINEX TAB 5MG | CHARIOT PHARMA LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢無結果。

需特別注意：試驗中使用最高 20 mg 的劑量遞增屬於仿單外使用，若要推進，需搭配安全性監測。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項隨機、對照且直接相關的研究（3 項 Phase 4 試驗與 3 篇 RCT）支持 Desloratadine 用於寒冷性蕁麻疹，且機轉合理。
- 但這些試驗為 Phase 4 而非 Phase 3，高劑量屬仿單外使用，香港仿單的警語與禁忌資料也尚未取得。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症，這是目前的阻斷性缺口。
- 補齊作用機轉資料（可查詢 DrugBank）。
- 確認香港核准的適應症，並訂定高劑量使用的安全性監測計畫。
- 確認試驗標題被截斷的三項研究，其族群與比較藥物與寒冷性蕁麻疹是否相符。

**其他預測適應症（暫不建議推進）：**
- 鼻腔疾病 (L3)：疾病名稱過於籠統，文獻僅為相關藥物或非抗組織胺的動物研究，列為研究問題。
- 急性喉咽炎、頑固性異位性皮膚炎、異位性 IgE 反應性、酒糟性結膜炎 (皆為 L5)：僅有模型預測，無試驗或文獻支持，建議 Hold。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

