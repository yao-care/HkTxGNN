---
layout: default
title: Cocaine
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cocaine：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：香港許可證未載明核准適應症"
monitor_inn: "Cocaine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "rhinitis", "irritable bowel syndrome", "anaphylaxis", "neurocirculatory asthenia", "atopic conjunctivitis", "food-dependent exercise-induced anaphylaxis", "pharyngitis"]
---

# Cocaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Cocaine：從局部麻醉（適應症未載明）到脊髓馬尾症候群

## 一句話總結

Cocaine（古柯鹼）在香港以眼鼻滴劑形式登記，臨床上曾作為鼻、口、喉手術的局部麻醉劑。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**與藥物無直接關聯的病例報告，實質證據不足，且該預測很可能是知識圖譜的假象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症（藥理資料顯示臨床用於鼻、口、喉手術的局部麻醉） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cocaine 是局部麻醉劑兼單胺類再攝取抑制劑，藥理資料顯示它作用於血清素 5-HT3 受體與多巴胺轉運體（DAT）。

馬尾症候群是需要手術減壓的壓迫性神經急症，與 Cocaine 的藥理作用沒有可信的機轉連結。唯一檢索到的文獻是腰薦椎椎間盤病變的病例報告，並未使用 Cocaine 治療。因此，高預測分數較可能是知識圖譜的人為假象，不宜視為有效訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | 病例報告／文獻回顧 | Surgical Neurology International | 遠端馬尾症候群與腰薦椎椎間盤病變的病例報告，未涉及 Cocaine 治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50765 | COCAINE HCL EYE/NOSE DROPS 5% | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示之禁忌疾病**（來自藥物－疾病關聯資料，非仿單文字）：癲癇、心臟驟停、心臟傳導疾病、甲狀腺毒症、甲狀腺機能亢進、Graves 病。
- **藥理交互作用**：資料顯示 Cocaine 與 5-HT3A/5-HT3AB 受體及多巴胺轉運體（DAT）有藥理作用，但未提供臨床嚴重度分級。

其他警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（L5），無臨床試驗，唯一文獻與 Cocaine 治療無關，機轉上也無可信連結。
- Cocaine 具心血管與神經方面風險，且知識圖譜顯示多項相關禁忌，風險效益不利。

**若要推進需要：**
- 取得香港衛生署許可證的完整仿單（警語、禁忌、核准適應症）。
- 補齊作用機轉資料，並重新評估與馬尾症候群的任何生物學關聯。
- 補充其他排名較高預測（如鼻炎、咽炎、過敏性休克）的檢討：現有文獻多顯示 Cocaine 造成黏膜損傷而非治療效果，亦不建議推進。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

