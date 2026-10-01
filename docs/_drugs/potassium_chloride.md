---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 703
evidence_level: L5
indication_count: 1
---

# Potassium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Potassium Chloride（氯化鉀）：從（許可證未載明原適應症）到腎小管酸中毒

## 一句話總結

Potassium Chloride 是常見的鉀離子補充劑，香港已有多張注射液與口服溶液許可證，但許可證文件未載明原適應症。
TxGNN 模型預測它可能對**腎小管酸中毒 (Renal Tubular Acidosis, RTA)** 有效，但目前**沒有任何直接測試 KCl 的臨床試驗**，只有 9 個間接相關試驗和 20 篇文獻（多為綜述與個案報告）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 腎小管酸中毒 (Renal Tubular Acidosis) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L4（僅有機轉層面的間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，藥物資料庫中也沒有原適應症紀錄，因此無法用已知機轉驗證 TxGNN 的高分預測。

從生理學來看，遠端腎小管酸中毒（第 1 型）與近端腎小管酸中毒（第 2 型）常造成腎臟排鉀增加與低血鉀，補鉀是標準的支持性治療（見 PMID 17297212、33459628）。因此 KCl 與 RTA 在臨床上有關聯，但它**矯正的是電解質後果，並非治療腎小管本身的缺陷**。

KCl 並非 RTA 的首選鉀鹽。氯化物鹽無法矯正代謝性酸中毒，一般會優先選擇檸檬酸鉀或碳酸氫鉀等鹼性鉀鹽。第 4 型 RTA 伴隨高血鉀，使用 KCl 有禁忌或高風險（PMID 37081692）。若要推進，只能限縮在低血鉀型 RTA 次型，並搭配血鉀監測。

---

## 臨床試驗證據

以下 9 個試驗沒有任何一個直接測試 KCl 用於 RTA。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | 提前終止 | 3 | ADV7103（檸檬酸鉀/碳酸氫鉀）用於遠端 RTA 的隨機停藥試驗；僅收 3 人，無可用療效結果，且藥物並非 KCl |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | 撤回 | 0 | 檸檬酸鉀用於兒童特發性高尿鈣與結石；未收案，無資料 |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | 招募中 | 33 | 原發性醛固酮增多症的 24 小時尿醛固酮診斷一致性研究；非 RTA 治療試驗 |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | 招募中 | 130 | SGLT2 抑制劑用於急性心腎症候群；藥物與疾病皆不相關 |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | 狀態未知 | 31 | Eplerenone 用於環孢素治療的移植受者安全性；涉及鉀代謝與高血鉀風險，未測試 KCl |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | 提前終止 | 36 | Spironolactone 預防 Amphotericin B 引起的電解質異常（失鉀）；藥物與族群不同 |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | 提前終止 | 7 | 鐮刀型貧血的鹼劑治療（口服碳酸氫鈉）；概念相關但非 KCl、非 RTA |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | 招募中 | 43 | 外源性酮體用於 CKD 蛋白尿；僅有酸鹼主題上的關聯 |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | 狀態未知 | 40 | 碳酸氫鈉用於 topiramate 治療兒童的血尿鹼化（藥物引起的類 RTA 酸中毒）；藥物為鹼劑，僅間接相關 |

---

## 文獻證據

沒有 RCT。以下依綜述、生理與世代研究、個案報告的順序列出。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Med Indones | 低血鉀的診斷思路，區分鉀缺乏與鉀位移，涵蓋腎性與腎外性流失 |
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Arch Esp Urol | RTA 與腎結石的診斷與處置；遠端 RTA 為尿液偏鹼、磷酸鈣結石 |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Literature review | Endocr J | 假性低醛固酮症 II 型歸類為第 4 型 RTA，特徵為高血鉀性酸中毒 |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Arch Intern Med | RTA 的病理生理與診斷 |
| [3518609](https://pubmed.ncbi.nlm.nih.gov/3518609/) | 1986 | 綜述（未分類） | Annu Rev Med | RTA 臨床譜系：近端型、低血鉀遠端型、高血鉀遠端型 |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | 未分類 | Int J Clin Pract | 成人 RTA 臨床處理，說明第 1、2、4 型的差異 |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | 臨床生理研究 | J Clin Invest | 10 位第 1 型 RTA 患者以口服碳酸氫鉀持續矯正酸中毒，部分患者鈉保留受損 |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | 世代研究 | Tunis Med | 突尼西亞遠端 RTA 的基因型與表型關聯，常見低血鉀與腎鈣化 |
| [20228475](https://pubmed.ncbi.nlm.nih.gov/20228475/) | 2010 | 未分類（個案報告加文獻回顧） | Neurol India | RTA 表現為呼吸麻痺，給予碳酸氫鈉與補鉀後改善 |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case report | J Nephrol | 孕期遠端 RTA 合併低血鉀性週期性麻痺 |

---

## 香港上市資訊

目前共有 20 張許可證，以下列出 5 張。各許可證均未載明劑型與核准適應症。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42421 | POTASSIUM CHLORIDE MIXTURE 10%（MARCHING PHARMACEUTICAL） | 未載明 | 未載明 |
| HK-68416 | POTASSIUM CHLORIDE CONCENTRATE FOR SOLUTION FOR INFUSION 14.9% W/V（B. BRAUN） | 未載明 | 未載明 |
| HK-31753 | POTASSIUM CHLORIDE INJ 14.9%（B. BRAUN） | 未載明 | 未載明 |
| HK-06492 | POTASSIUM CHLORIDE INJ 15%（ATLANTIC PHARMACEUTICAL） | 未載明 | 未載明 |
| HK-06446 | POTASSIUM CHLORIDE INJ 3G/20ML（ATLANTIC PHARMACEUTICAL） | 未載明 | 未載明 |

---

## 安全性考量

- **藥物交互作用**：查詢無結果。
- **新適應症的特殊風險**：第 4 型 RTA 伴隨高血鉀，使用 KCl 有禁忌或高風險（PMID 37081692）。若評估用於 RTA，必須限縮在低血鉀型次型，並監測血鉀。

警語與禁忌症的完整資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，但沒有任何直接測試 KCl 的 RTA 試驗，現有證據只有生理學推論與間接文獻。
- 香港仿單的警語與禁忌症缺漏，屬於阻擋性資料缺口，無法進入安全性篩選。
- KCl 不能矯正酸中毒，臨床上多半被鹼性鉀鹽取代，在第 4 型 RTA 更有高血鉀風險。

**若要推進需要：**
- 取得衛生署（Department of Health）核准仿單，補齊警語、禁忌症與適應症。
- 補齊 KCl 的作用機轉資料（DrugBank）。
- 釐清 KCl 與檸檬酸鉀、碳酸氫鉀相比，在低血鉀型 RTA 的角色，並搜尋直接比較證據。
- 若仍要評估，限縮於低血鉀型 RTA 次型，設計血鉀與酸鹼監測計畫。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

