---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 749
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Quetiapine：預測新適應症為視網膜失養症 (retinal dystrophy with or without extraocular anomalies)（證據等級 L5）。原適應症：雙相情緒障礙、重度情感性疾患、躁期雙相情感障礙、思覺失調症"
monitor_inn: "QUETIAPINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "distal 17p13.3 microdeletion syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
---

# Quetiapine
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

# Quetiapine：從雙相情緒障礙／思覺失調症到視網膜失養症

## 一句話總結

Quetiapine 是一種非典型抗精神病藥，原本用於雙相情緒障礙、躁症發作及思覺失調症。
TxGNN 模型預測它可能對**視網膜失養症（retinal dystrophy with or without extraocular anomalies）**有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 雙相情緒障礙、重度情感性疾患、躁期雙相情感障礙、思覺失調症（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 視網膜失養症 (retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，quetiapine 是拮抗血清素 5-HT2A 與多巴胺 D2 受體的非典型抗精神病藥，其療效在雙相情緒障礙與思覺失調症中已被證實。

然而，視網膜失養症屬於遺傳性、退行性的視網膜疾病，與神經傳導物質受體調控之間，並沒有已建立的關聯。就現有資料而言，找不到可支持的機轉連結。

此外，quetiapine 本身有眼部安全性考量（例如白內障相關警語），用於視網膜疾病需特別謹慎。99.57% 的高分是知識圖譜的計算結果，不應視為療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

資料中的許可證均未載明劑型與核准適應症文字，以下列出 5 張主要許可證（共 20 張，均為有效的單方製劑）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52580 | SEROQUEL TAB 300MG（Luye Pharma） | 未載明 | 未載明 |
| HK-58348 | SEROQUEL XR EXTENDED RELEASE TAB 150MG（Luye Pharma） | 未載明（緩釋錠） | 未載明 |
| HK-57716 | SEROQUEL XR EXTENDED RELEASE TAB 200MG（Luye Pharma） | 未載明（緩釋錠） | 未載明 |
| HK-58567 | QUETIAPINE-TEVA TAB 25MG（Teva） | 未載明 | 未載明 |
| HK-65854 | QUETIAPINE TABLETS 100MG（Controlled Medications） | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌／風險相關疾病**（來源為知識圖譜，非仿單內容），主要包括：
  - 心血管：高血壓、姿勢性低血壓、長 QT 症候群、尖端扭轉型心律不整、心肌梗塞
  - 代謝：糖尿病、糖尿病酮酸中毒、高血糖、高血脂、高三酸甘油脂血症、肥胖
  - 血液：嗜中性白血球減少、顆粒球缺乏症
  - 神經：癲癇、基底核疾病、眼瞼痙攣
  - 其他：肝臟疾病、膽囊疾病、甲狀腺功能低下、低血鉀、乳癌
- **藥物交互作用**：共查到 100 筆，其中列出的重度（Major）交互作用包括：
  - Bupropion
  - Morphine

  中度（Moderate）交互作用包括降血糖藥（如 metformin、pioglitazone、acarbose、alogliptin、canagliflozin）、抗膽鹼藥（如 atropine、hyoscyamine）、epinephrine、dexamethasone 等。

仿單警語與禁忌的正式內容仍請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有臨床試驗或文獻佐證，且機轉上找不到合理的連結。
- Quetiapine 有眼部及多項代謝、心血管安全性顧慮，在缺乏效益證據的情況下不宜推進。

**若要推進需要：**
- 補齊 quetiapine 的作用機轉資料，並評估與視網膜失養症病理的可能關聯
- 取得香港衛生署仿單的警語與禁忌內容，完成安全性篩選
- 前臨床（細胞或動物模型）研究，確認對視網膜退化有無保護作用
- 評估眼部安全性（如白內障風險）對此族群的影響
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

