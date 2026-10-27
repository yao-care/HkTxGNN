---
layout: default
title: Olmesartan
parent: 僅模型預測 (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Olmesartan：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：本次資料中香港許可證未載明核准適應症"
monitor_inn: "olmesartan"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
---

# Olmesartan
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

## Olmesartan：從高血壓到偏頭痛
{: .text-alpha }

## 一句話總結

Olmesartan 是一種血管收縮素 II 第一型受體（AT1）拮抗劑，在香港已有 20 張有效許可證。
TxGNN 模型的預測中，證據最完整的方向是**偏頭痛 (Migraine Disorder)**，目前有 **3 篇文獻**（無已登記的臨床試驗），證據等級為 L3。
預測分數最高的是變異型心絞痛（Prinzmetal angina，99.84%），但目前沒有任何試驗或文獻支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次資料中香港許可證未載明核准適應症 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder)；為證據最完整的候選（TxGNN 排名第 3） |
| TxGNN 預測分數 | 99.64%（偏頭痛）；排名第 1 的變異型心絞痛為 99.84% |
| 證據等級 | L3（偏頭痛）；變異型心絞痛僅 L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（偏頭痛方向可列為研究問題，需進一步驗證） |

> 說明：預測分數最高的前兩名（變異型心絞痛、頭皮單純性毛髮稀少症）缺乏任何試驗或文獻。本報告以證據最完整的偏頭痛作為主要評估對象，並簡述其他候選。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，olmesartan 屬於 AT1 受體拮抗劑（ARB）類降血壓藥，可阻斷腎素-血管收縮素系統（RAS）。

**偏頭痛：** RAS 調控可能透過血管張力、神經性發炎與交感神經活性，降低偏頭痛發作頻率。現有文獻包括 2006 年一項在高血壓／高血壓前期病人中評估 olmesartan 預防偏頭痛的研究，以及 2019 年關於 ACE 抑制劑與 ARB 預防發作性偏頭痛的系統性回顧。不過證據多限於高血壓族群，且依標題判斷研究設計並非決定性，研究類型僅由標題推測。

**肺高壓：** 血管收縮素 II 經由 AT1 受體參與肺血管重塑與收縮。大鼠 monocrotaline 模型與慢性缺氧模型等前臨床研究支持此機轉，但尚無人體療效資料。

**其他候選：** 開角型青光眼有 RAS 存在於眼組織的合理推測，但僅有一篇與 olmesartan 無直接關聯的一般性回顧。毛髮相關疾病（頭皮單純性毛髮稀少症、先天性毛髮稀少伴粟丘疹、禿髮、瀰漫性斑禿）看不出與 AT1 阻斷有明確機轉關聯，高分可能反映知識圖譜的網路鄰近性，而非生物學因果。

---

## 臨床試驗證據

**偏頭痛：** 目前無相關臨床試驗登記。

**肺高壓（參考）：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04330300](https://clinicaltrials.gov/study/NCT04330300) | Phase 4 | 暫停 | 2414 | COVID-19 病人 ACEi/ARB 的繼續或停用策略；與肺高壓無直接關聯，相關性低 |

---

## 文獻證據

**偏頭痛：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31515634](https://pubmed.ncbi.nlm.nih.gov/31515634/) | 2019 | 系統性回顧（由標題推斷） | Current Pain and Headache Reports | 回顧 ACEi 與 ARB 預防成人發作性偏頭痛的療效，並指出研究缺口 |
| [16618270](https://pubmed.ncbi.nlm.nih.gov/16618270/) | 2006 | 臨床研究（設計未確認） | Headache | 探討 olmesartan 對合併高血壓／高血壓前期病人偏頭痛頻率與嚴重度的影響 |
| [16942482](https://pubmed.ncbi.nlm.nih.gov/16942482/) | 2006 | 評論／信件（由標題推斷） | Headache | 討論 olmesartan、偏頭痛與血壓的關係 |

**肺高壓（前臨床，參考）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18209564](https://pubmed.ncbi.nlm.nih.gov/18209564/) | 2008 | 前臨床 | J Cardiovasc Pharmacol | 在大鼠 monocrotaline 肺高壓模型中評估 olmesartan |
| [16336959](https://pubmed.ncbi.nlm.nih.gov/16336959/) | 2005 | 前臨床 | Eur J Pharmacol | 在慢性缺氧大鼠中評估 olmesartan 對缺氧性肺高壓的作用 |
| [17089097](https://pubmed.ncbi.nlm.nih.gov/17089097/) | 2006 | 前臨床 | Naunyn-Schmiedeberg's Arch Pharmacol | olmesartan 對小鼠肺部缺氧誘發 ERK1/2 活化與促發炎訊號的影響 |

---

## 香港上市資訊

香港共有 20 張有效單一成分許可證（本次資料未載明劑型與核准適應症），以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53022 | OLMETEC TAB 20MG（Pfizer） | 資料未載明 | 資料未載明 |
| HK-53023 | OLMETEC TAB 10MG（Pfizer） | 資料未載明 | 資料未載明 |
| HK-53024 | OLMETEC TAB 40MG（Pfizer） | 資料未載明 | 資料未載明 |
| HK-60989 | OLMESARTAN SANDOZ TAB 20MG（Sandoz） | 資料未載明 | 資料未載明 |
| HK-55166 | OLMETEC PLUS TAB 20MG/12.5MG（Pfizer） | 資料未載明 | 資料未載明 |

---

## 安全性考量

- **藥物交互作用：** 資料庫共記錄 94 筆交互作用。
  - **重大（Major）：** 碳酸氫鉀、氯化鉀（高血鉀風險，需監測血鉀）。
  - **中度（Moderate）：** 氫化可的松、各類胰島素（包含人類胰島素、aspart、degludec、detemir、glargine、glulisine、lispro 等）、exenatide、eluxadoline、聚乙二醇電解質製劑等。與降血糖藥併用時應留意血糖變化。
- 另一篇個案報告提到，ARB 類藥物因抑制胎兒腎素-血管收縮素系統，於懷孕期間屬禁忌（可能造成羊水過少、腎發育不良、肺發育不全）。此為文獻背景資訊，非仿單內容。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數最高的候選（變異型心絞痛、毛髮相關疾病）完全沒有試驗或文獻支持，屬 L5 純模型預測。
- 偏頭痛有初步文獻（L3），但多為高血壓族群、設計不明確的研究，尚無登記的臨床試驗，適合列為研究問題而非進入開發。肺高壓僅有動物資料（L4），且 ARB 在懷孕期間的風險也需納入考量。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症（目前為阻斷性資料缺口）。
- 補充 olmesartan 的作用機轉資料（DrugBank）。
- 針對偏頭痛，全文審閱上述 2006 年研究與 2019 年系統性回顧，確認實際設計、樣本數與效果量。
- 設計非高血壓族群的偏頭痛預防性隨機對照試驗，或先做前導研究。
- 對肺高壓，需先有人體早期研究，並評估低血壓與腎功能風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

