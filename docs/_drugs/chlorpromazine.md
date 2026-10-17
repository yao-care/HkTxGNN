---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorpromazine：預測新適應症為伴或不伴眼外異常的視網膜失養症 (Retinal dystrophy with or without extraocular anomal…（證據等級 L5）。原適應症：躁期雙相情感障礙、精神病性疾患、精神分裂症、思覺失調情感性疾患等"
monitor_inn: "Chlorpromazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Chlorpromazine
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

# Chlorpromazine：從精神分裂症等精神疾病到遺傳性視網膜失養症（預測）

## 一句話總結

Chlorpromazine（氯丙嗪）是經典的第一代抗精神病藥，原本用於精神分裂症、躁鬱症躁期、精神病性疾患及急性間歇性紫質症等。
TxGNN 模型預測它可能對**伴或不伴眼外異常的視網膜失養症 (Retinal dystrophy with or without extraocular anomalies)** 有效，但目前**沒有任何臨床試驗**，僅有 **1 篇 1967 年的文獻**，且內容是藥物引起的光毒性反應，並非療效證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 躁期雙相情感障礙、精神病性疾患、精神分裂症、思覺失調情感性疾患等（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 伴或不伴眼外異常的視網膜失養症 (Retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L4（僅有 1 篇個案/毒性觀察文獻，且指向不良反應） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 chlorpromazine 主要是多巴胺 D2 受體拮抗劑，在精神分裂症與精神病性疾患中的療效已被長期證實。

然而，遺傳性視網膜失養症是基因缺陷導致的視網膜退化，與精神疾病的病理差異很大。唯一的文獻是 1967 年關於高劑量 chlorpromazine 與 thioridazine 引起光毒性反應的報告，記錄的是**藥物不良反應**，不但不支持療效，反而可能不利於此適應症。

因此，99.95% 的高分屬於模型的計算結果，缺乏臨床或機轉證據支持，應謹慎解讀。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [5336672](https://pubmed.ncbi.nlm.nih.gov/5336672/) | 1967 | 個案報告/毒性觀察 | JAMA | 高劑量 chlorpromazine 與 thioridazine 可誘發光毒性反應（不良反應，非療效） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53900 | CHLOZINE EXTRA TAB 100MG | 未載明 | 未載明 |
| HK-44623 | CHLOZINE PLUS TAB 50MG | 未載明 | 未載明 |
| HK-44714 | CHLOZINE TAB 25MG | 未載明 | 未載明 |

三張許可證皆為單方、有效，持證商為 APT PHARMA LIMITED。

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單原文）**：包括
  - 心血管與心律：long QT 症候群、torsades de pointes、心臟傳導疾病、猝死性心臟停止、心肌梗塞、直立性低血壓
  - 血液：嗜中性白血球低下、顆粒球缺乏症、白血球低下、血小板低下、貧血
  - 神經：癲癇、基底核疾病、眼瞼痙攣
  - 其他：肝病、膽囊疾病、高血糖、良性前列腺肥大、物質濫用/依賴、肥胖、女性乳癌
- **藥物交互作用**：資料庫共查得 100 筆交互作用，其中較需注意的為 **Major 等級**：
  - Bupropion
  - Morphine

  另有多項 Moderate 等級，例如 acarbose、famotidine、epinephrine、hydrocortisone、metformin、pioglitazone、amphotericin B、atropine、loperamide 等（涵蓋降血糖藥、抗膽鹼藥等）。
- **眼部相關風險**：chlorpromazine 已知有光毒性及眼部（水晶體/角膜沉積）副作用，對視網膜疾病族群尤需考量。

仿單的警語與禁忌症資料尚未取得，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有臨床試驗；唯一文獻顯示的是光毒性不良反應，與預期療效方向相反。
- 缺乏作用機轉資料，加上已知眼部副作用，目前不適合推進。

**若要推進需要：**
- 取得香港仿單的警語與禁忌症，完成基本安全性篩選
- 補充作用機轉資料，釐清 chlorpromazine 與視網膜失養症之間是否有合理的生物學連結
- 進行前臨床（視網膜模型）研究，並評估光毒性風險
- 若無任何支持證據，建議不再優先考慮此適應症

---

### 補充：其他預測適應症

資料中其他預測項目證據同樣薄弱：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 2–9 | 糖基化先天異常（岩藻糖化缺陷）、X 連鎖近視、症候群性近視、無腦迴畸形、腦裂畸形合併小腦發育不全等、Charcot-Marie-Tooth 1G 型、非典型甘胺酸腦病變等 | 99.92%–99.94% | L5 | Hold（無臨床或文獻證據，亦無可辨識的機轉連結） |
| 10 | 早發型精神分裂症 (Early-onset schizophrenia) | 99.47% | L4 | 研究問題（Research Question） |

其中**早發型精神分裂症**與原適應症最接近，有 6 篇文獻，但皆為觀察性、基因關聯、神經影像或劑量研究，沒有試驗登記或兒童 RCT。它較屬於既有適應症的年齡層延伸，而非真正的藥物再利用；若要推進，需要兒童療效與安全性數據，並特別留意錐體外症狀、鎮靜與代謝副作用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

