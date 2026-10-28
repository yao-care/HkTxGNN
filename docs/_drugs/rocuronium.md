---
layout: default
title: Rocuronium
parent: 僅模型預測 (L5)
nav_order: 783
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Rocuronium：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症"
monitor_inn: "Rocuronium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "atrophoderma vermiculata", "ulerythema ophryogenesis", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "sciatic neuropathy", "headache disorder"]
---

# Rocuronium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Rocuronium：從神經肌肉阻斷（麻醉輔助）到偏頭痛
{: .text-alpha }

## 一句話總結

Rocuronium 是一種非去極化型神經肌肉阻斷劑，臨床上用於麻醉時的肌肉鬆弛。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前僅有 **1 個無關聯的藥動學臨床試驗**，沒有直接支持的文獻，屬於僅有模型預測的階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Rocuronium 是競爭性拮抗神經肌肉接合處菸鹼型乙醯膽鹼受體的神經肌肉阻斷劑，在麻醉中用於肌肉鬆弛。

**坦白說，這個預測的合理性很低。** 偏頭痛的病理機轉涉及 CGRP、三叉神經血管活化與皮質擴散性抑制，Rocuronium 與這些路徑沒有已知的關聯。高分（0.9990）來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而不是生物學證據。肉毒桿菌毒素抑制突觸前乙醯膽鹼釋放，機轉與 Rocuronium 不同。

排名前 10 的其他預測（如腦幹先兆偏頭痛、馬尾症候群、腸躁症、坐骨神經病變等）同樣沒有臨床試驗或文獻支持，也缺乏合理的機轉連結。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | 完成 | 3520 | 兒童標準照護下多種缺乏研究藥物的藥動學研究，Rocuronium 只是其中之一，並未評估偏頭痛療效（相關性：低） |

---

## 文獻證據

目前無針對偏頭痛的相關文獻。

與較廣泛的「頭痛疾患」相關的兩篇文獻，僅屬麻醉情境，不支持再利用假說：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/) | 2014 | 臨床研究 | J ECT | 比較 succinylcholine 與 rocuronium-sugammadex 對電痙攣治療後肌痛與頭痛的影響，屬於處置副作用情境，並非頭痛治療 |
| [24196089](https://pubmed.ncbi.nlm.nih.gov/24196089/) | 2013 | 病例報告 | Pediatr Emerg Care | 顱內壓升高兒童的快速順序插管麻醉案例，與頭痛治療無關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67201 | ROCURONIUM BROMIDE SOLUTION FOR INJECTION/INFUSION 50MG/5ML（MAIN LIFE CORP LTD） | 注射液 | 資料未載明 |
| HK-64818 | ROCURONIUM KABI SOLUTION FOR INJECTION/INFUSION 50MG/5ML（FRESENIUS KABI HONG KONG LIMITED） | 注射液 | 資料未載明 |
| HK-59706 | ROCURONIUM SOLUTION FOR INJ 10MG/ML（MEKIM LTD） | 注射液 | 資料未載明 |
| HK-67000 | ROCURONIUM B. BRAUN SOLUTION FOR INJECTION/INFUSION 50MG/5ML（B. BRAUN MEDICAL (HK) LTD） | 注射液 | 資料未載明 |
| HK-67219 | ROCURONIUM BROMIDE KALCEKS SOLUTION FOR INJECTION/INFUSION 50MG/5ML（SB PHARMA LIMITED） | 注射液 | 資料未載明 |

---

## 安全性考量

- **藥物交互作用**：資料庫共收錄 73 筆交互作用。其中列為**嚴重 (Major)** 的包括：
  - Paromomycin
  - Kanamycin
  - Neomycin

  這些胺基糖苷類抗生素可能增強神經肌肉阻斷作用。
- **中度 (Moderate)** 交互作用包括：
  - 四環素類（Doxycycline、Tetracycline、Minocycline）
  - 皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Prednisone、Triamcinolone）
  - Amphotericin B
  - 鎂鹽（硫酸鎂、氯化鎂）
  - Vancomycin
  - Mannitol
  - Metoclopramide
- 另有輕度 (Minor) 交互作用，例如 Ranitidine。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何針對偏頭痛的臨床試驗或文獻，唯一的試驗是無關的兒童藥動學研究。
- 機轉上缺乏合理連結，且 Rocuronium 會造成全身性肌肉麻痺，需要呼吸支持，不適合作為偏頭痛等慢性疾病的治療。

**若要推進需要：**
- 先釐清 Rocuronium 的詳細作用機轉，並檢視 TxGNN 模型（深度學習）預測的依據與限制。
- 取得偏頭痛相關的前臨床或機轉證據，目前不建議投入臨床開發。
- 補齊香港仿單的核准適應症、警語與禁忌症資料。
- 若確實要探索，應優先考慮已有證據的神經肌肉作用藥物（如肉毒桿菌毒素），而非 Rocuronium。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

