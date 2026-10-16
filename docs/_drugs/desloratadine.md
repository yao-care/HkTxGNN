---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Desloratadine：預測新適應症為寒冷性蕁麻疹 (Cold Urticaria)（證據等級 L5）。原適應症：過敏性鼻炎、血管運動性鼻炎、特發性蕁麻疹、過敏性蕁麻疹等"
monitor_inn: "DESLORATADINE"
predicted_indications: ["cold urticaria", "nasal cavity disease", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
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

# Desloratadine：從過敏性鼻炎與蕁麻疹到寒冷性蕁麻疹

## 一句話總結

Desloratadine 是第二代 H1 抗組織胺藥，原本用於過敏性鼻炎、血管運動性鼻炎、特發性及過敏性蕁麻疹等。
TxGNN 模型預測它可能對**寒冷性蕁麻疹 (Cold Urticaria)** 有效，
目前有 **2 個臨床試驗**和 **6 篇文獻**支持這個方向，其中包含多項隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、血管運動性鼻炎、特發性蕁麻疹、過敏性蕁麻疹等（核准適應症文字於許可證資料中未提供，此處依知識圖譜適應症列出） |
| 預測新適應症 | 寒冷性蕁麻疹 (Cold Urticaria) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L1（依本報告提供的規則，嚴格而言試驗為 Phase 4，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Proceed with Guardrails |

**證據等級說明：**
兩個臨床試驗皆為已完成的 Phase 4 隨機、雙盲試驗，另有 3 篇與寒冷性蕁麻疹相關的 RCT 文獻。依資料編譯的評分結果為 L1，但試驗規模偏小（n=30、33），解讀時宜保守。

---

## 為什麼這個預測合理？

Desloratadine 是選擇性的周邊 H1 受體反向促效劑。寒冷性蕁麻疹屬於物理性蕁麻疹，主要由肥大細胞去顆粒化與組織胺釋放所驅動，因此阻斷 H1 受體直接作用在主要的效應路徑上。

寒冷性蕁麻疹與 Desloratadine 已核准的特發性蕁麻疹、過敏性蕁麻疹同屬蕁麻疹譜系，亞型關係相近。治療指引也建議，標準劑量反應不佳時，可提高第二代抗組織胺的劑量。不過較高劑量（如 10 mg、20 mg）屬於仿單外使用，應在臨床監督下進行。

另外，目前缺乏詳細的作用機轉資料庫記錄（原始 MOA 欄位為空），上述機轉描述來自藥理學共識與預測分析的推論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | 完成 | 30 | 多中心、雙盲、劑量遞增試驗，比較 5、10、20 mg Desloratadine，評估足以抑制寒冷性蕁麻疹症狀的劑量（2009-08 至 2010-05） |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | 完成 | 33 | 隨機、雙盲、安慰劑對照交叉試驗，比較 5 mg 與 20 mg 對實驗誘發蕁麻疹病灶的影響，假設高劑量療效優於標準劑量（2006-11 起） |

註：兩項試驗的標題在登記資料中被截斷，適應症為依上下文推斷，建議再行核對。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | 隨機、安慰劑對照交叉試驗：高劑量 Desloratadine 在後天性寒冷性蕁麻疹可降低風疹塊體積並改善寒冷誘發閾值（優於標準劑量） |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | 以臨界溫度閾值測量評估 H1 抗組織胺劑量遞增於寒冷性蕁麻疹的效果 |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatolog Treat | 12 位寒冷性蕁麻疹患者以 5 mg Desloratadine 治療 4 天，用冰塊試驗比較治療前後反應 |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | 慢性蕁麻疹的病因、處置與現行及未來治療選項回顧 |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Ebastine 於過敏性鼻炎與慢性特發性蕁麻疹的回顧（間接相關，為另一種藥物） |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | 黑螞蟻咬傷過敏反應後出現寒冷性蕁麻疹的首例報告（背景資訊） |

---

## 香港上市資訊

目前共有 15 張有效許可證，皆為單方製劑，無已註銷者。核准適應症文字與劑型欄位在許可證資料中未提供。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-51862 | AERIUS TAB 5MG | BAYER HEALTHCARE LIMITED |
| HK-51453 | AERIUS SYRUP 0.5MG/ML | BAYER HEALTHCARE LIMITED |
| HK-58683 | AERIUS D-12 MODIFIED RELEASE TAB | BAYER HEALTHCARE LIMITED |
| HK-57332 | LARINEX TAB 5MG | CHARIOT PHARMA LIMITED |
| HK-66259 | LOTARIUS TABLETS 5MG | VICKMANS LABORATORIES LTD |

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（來自藥物－疾病關聯，非仿單文字）：高血壓、腎臟疾病、肝臟疾病、膽囊疾病、糖尿病及酮酸中毒、良性攝護腺增生、冠狀動脈疾病與動脈硬化、閉角型青光眼、甲狀腺功能亢進（含 Graves 病）。其中部分可能與複方製劑（如含擬交感神經成分的 D-12 緩釋錠）有關，需對照實際仿單。
- **藥物交互作用**：資料庫查得 100 筆交互作用紀錄，但嚴重度分級皆為「未知」，例如 Calcitriol、Phentermine、Pantoprazole、Doxycycline、Morphine、Metformin、Omeprazole、Cimetidine 等，臨床意義尚待確認。

仿單中的主要警語與禁忌症資料未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多項針對寒冷性蕁麻疹的 RCT（含 2 個已完成的 Phase 4 試驗與 3 篇 RCT 文獻），顯示高劑量 Desloratadine 可能優於標準劑量，且機轉合理。
- 但試驗規模小，高劑量屬仿單外使用，且仿單安全性資料尚未取得，因此需附帶防護條件。

**若要推進需要：**
- 下載並解析香港衛生署的仿單，補齊警語與禁忌症（目前為阻擋性資料缺口）
- 補充 MOA 資料（如 DrugBank）
- 確認兩項試驗的實際適應症（標題被截斷）
- 訂定高劑量使用的臨床監督與安全監測計畫
- 評估較大型、設計嚴謹的試驗證據

---

### 其他預測適應症簡述

| 預測適應症 | 分數 | 證據等級 | 建議 |
|-----------|------|---------|------|
| 鼻腔疾病 (Nasal cavity disease) | 99.87% | L4 | Hold：與既有適應症重疊，僅有動物實驗的間接證據 |
| 急性喉咽炎 (Acute laryngopharyngitis) | 99.85% | L5 | Hold：僅有模型預測，抗組織胺對感染性發炎僅有症狀緩解作用 |
| 頑固性異位性皮膚炎 | 99.75% | L5 | Hold：組織胺非主要驅動因子，機轉上存疑 |
| 異位性 IgE 反應性 | 99.64% | L5 | Hold：屬表型而非可治療疾病 |
| 酒糟性結膜炎 | 99.40% | L5 | Hold：機轉連結薄弱 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

