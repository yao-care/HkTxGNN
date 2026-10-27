---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Felodipine：預測新適應症為肺高壓…（證據等級 L5）。原適應症：高血壓"
monitor_inn: "FELODIPINE"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome"]
---

# Felodipine
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

## Felodipine：從高血壓到肺高壓（預測新適應症）
{: .text-alpha }

## 一句話總結

Felodipine 是二氫吡啶類鈣離子通道阻斷劑，原本用於治療高血壓。
TxGNN 模型預測它可能對**肺高壓（pulmonary hypertension with unclear multifactorial mechanism）**有效，
但目前**沒有任何臨床試驗**，僅有 **9 篇間接的前臨床文獻**（針對缺氧相關的肺高壓預測項目），證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（hypertension；依據知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 肺高壓，機轉不明的多因素型 (pulmonary hypertension with unclear multifactorial mechanism) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Felodipine 是二氫吡啶類 L 型鈣離子通道阻斷劑，透過血管擴張降低血壓。理論上，這種血管擴張作用也可能作用於肺血管，這很可能是 TxGNN 給出高分的原因。

高血壓與肺高壓同屬血管壓力異常的疾病，在網路關聯上相近。但需要注意：鈣離子通道阻斷劑在肺動脈高壓中，僅建議用於少數對血管擴張劑有反應（vasoreactive）的病人，並不適用於更廣泛的多因素型肺高壓。

此外，TxGNN 同時預測了另一個相關項目「缺氧或肺部疾病引起的肺高壓」。其文獻多為缺氧/再氧合的動物或離體實驗，顯示 Felodipine 可能有一般性的細胞保護與血管舒張作用，但沒有任何研究直接檢視肺循環或肺高壓病人。血管擴張劑還可能使缺氧肺部的通氣灌流比例惡化，是潛在的安全疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（機轉不明的多因素型肺高壓）無相關文獻。以下為排名第 2 的預測「缺氧或肺部疾病引起的肺高壓」所檢索到的文獻，全部為前臨床或離體研究，僅屬間接證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8160846](https://pubmed.ncbi.nlm.nih.gov/8160846/) | 1994 | 前臨床（血管） | Am J Physiol | 大鼠主動脈環先前的缺氧會減弱後續缺氧引起的血管舒張 |
| [8584414](https://pubmed.ncbi.nlm.nih.gov/8584414/) | 1995 | 前臨床（大鼠腎小管） | Pflugers Arch | Felodipine 以不依賴鈣的機轉保護近曲小管免於缺氧損傷 |
| [9431863](https://pubmed.ncbi.nlm.nih.gov/9431863/) | 1997 | 離體（人類心房肌） | Int J Cardiol | Felodipine 可保護人類心房肌免於缺氧-再氧合功能障礙 |
| [3142891](https://pubmed.ncbi.nlm.nih.gov/3142891/) | 1988 | 前臨床（腦動脈） | J Cereb Blood Flow Metab | 血管擴張劑影響再氧合與鈣誘發的狗腦動脈收縮 |
| [9864178](https://pubmed.ncbi.nlm.nih.gov/9864178/) | 1999 | 前臨床（嗜中性球/NO） | Blood | 一氧化氮增強缺氧再氧合後嗜中性球自由基生成 |
| [8394565](https://pubmed.ncbi.nlm.nih.gov/8394565/) | 1993 | 前臨床（細胞內鈣） | Pflugers Arch | L 型鈣通道阻斷劑影響缺氧所致兔近曲小管細胞內鈣上升 |
| [8110031](https://pubmed.ncbi.nlm.nih.gov/8110031/) | 1993 | 前臨床（動物行為） | Arch Int Pharmacodyn Ther | 測試 nicardipine、felodipine、nifedipine 對大鼠被動迴避學習及缺氧所致記憶缺損的影響 |
| [3961832](https://pubmed.ncbi.nlm.nih.gov/3961832/) | 1986 | 前臨床（腦血流） | Stroke | 二氫吡啶類鈣拮抗劑抑制缺氧引起的大鼠腦血流增加 |
| [3343292](https://pubmed.ncbi.nlm.nih.gov/3343292/) | 1988 | 前臨床（大鼠大腦皮質） | J Cereb Blood Flow Metab | Nifedipine 與 felodipine 抑制缺氧誘發的腺苷與肌苷釋放 |

---

## 香港上市資訊

香港共有 16 張有效的單方許可證，以下列出 5 張主要許可證（資料中未載明劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37191 | PLENDIL TAB 2.5MG EXTENDED RELEASE | 緩釋錠 | 未載明 |
| HK-32696 | PLENDIL TAB 5MG EXTENDED RELEASE | 緩釋錠 | 未載明 |
| HK-32695 | PLENDIL TAB 10MG EXTENDED RELEASE | 緩釋錠 | 未載明 |
| HK-38314 | LOGIMAX TAB EXTENDED RELEASE | 緩釋錠 | 未載明 |
| HK-49353 | FELODIPIN STADA RETARD TAB 5MG | 緩釋錠 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單文字，僅供參考）：腎臟疾病、肝臟疾病、膽囊疾病、血管性水腫、嗜中性白血球低下／顆粒球缺乏症、主動脈瓣狹窄、低血壓、肥厚性心肌病變、腎動脈阻塞、心肌梗塞、冠狀動脈疾病、動脈粥狀硬化等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 重大（Major）：Dolasetron
  - 中度（Moderate）：Cimetidine、Clarithromycin、Aprepitant、Bupropion、Morphine、Acetylsalicylic acid、多種皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone）、SGLT2 抑制劑（Canagliflozin、Dapagliflozin、Empagliflozin）等
- 另外，血管擴張劑可能使缺氧肺部疾病的通氣灌流比例惡化，用於肺高壓時需特別留意。

其餘仿單警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測的肺高壓項目沒有任何臨床試驗或文獻，僅有模型預測（L5）；相關缺氧文獻（L4）皆為前臨床間接證據，未涉及肺循環。
- 鈣離子通道阻斷劑僅適用於少數血管反應陽性的肺動脈高壓病人，且在缺氧性肺疾病中有惡化通氣灌流匹配的風險。
- 其他排名較前的預測（惡性腎血管性高血壓、惡性高血壓腎病）多屬既有高血壓適應症的延伸；Braddock 症候群則缺乏明確機轉依據。

**若要推進需要：**
- 補齊 Felodipine 的作用機轉資料（MOA）及香港仿單的警語與禁忌。
- 取得針對肺循環或肺高壓的直接證據，例如肺血管張力的前臨床研究，或血管反應性檢測陽性病人的臨床資料。
- 明確界定目標族群（如血管反應性肺動脈高壓），並評估與現有標準治療的比較及安全性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

