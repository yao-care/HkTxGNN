---
layout: default
title: Dihydrocodeine
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Dihydrocodeine：預測新適應症為鼻腔疾病 (Nasal Cavity Disease)（證據等級 L5）。原適應症：過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、鼻咽炎"
monitor_inn: "Dihydrocodeine"
predicted_indications: ["acute laryngopharyngitis", "allergic urticaria", "papillary conjunctivitis", "faucial diphtheria", "cervical disc degenerative disorder", "headache disorder", "cold urticaria", "trigeminal autonomic cephalalgia"]
---

# Dihydrocodeine
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

# Dihydrocodeine：從過敏性鼻炎與感冒相關上呼吸道疾病到鼻腔疾病

## 一句話總結

Dihydrocodeine 是一種鴉片類鎮咳／止痛藥，原本用於過敏性鼻炎、咽炎、感冒等上呼吸道症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，但目前**沒有臨床試驗與文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、鼻咽炎（香港許可證未載明適應症文字，此處依知識圖譜適應症資料） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dihydrocodeine 是鴉片類鎮咳／止痛藥，透過中樞 mu-opioid 受體作用，可緩解咳嗽與疼痛等症狀，但這個機轉無法直接解釋對鼻腔疾病的療效。

鼻腔疾病與其原適應症（鼻炎、感冒）在疾病分類上高度相鄰。模型的高分很可能反映知識圖譜中的「鄰近效應」，而非新的實質證據。

其他預測適應症也顯示類似狀況：
- **急性喉咽炎**（99.99%）：與已知的咽炎、鼻咽炎適應症高度相近，較像既有適應症的延伸。
- **過敏性蕁麻疹、寒冷性蕁麻疹**：鴉片類可能引起組織胺釋放，作用方向可能是不良反應而非治療。
- **頭痛疾患**（99.26%）：止痛機轉合理，但現有文獻間接，且鴉片類有藥物過度使用性頭痛風險。這是唯一有文獻（2 篇）的預測，證據等級為 L4，建議定位為研究問題。
- 其餘（乳頭狀結膜炎、咽白喉、頸椎椎間盤退化、三叉自主神經性頭痛）僅為模型預測，缺乏支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（鼻腔疾病）目前無相關文獻。

下表為排名第 7 的預測「頭痛疾患」的間接文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11915306](https://pubmed.ncbi.nlm.nih.gov/11915306/) | 2002 | 個案系列 | Nihon Arukoru Yakubutsu Igakkai zasshi | 含 dihydrocodeine 的鎮咳糖漿在日本曾有濫用與依賴問題，並非治療頭痛的證據 |
| [28521551](https://pubmed.ncbi.nlm.nih.gov/28521551/) | 2017 | Review | J Pain Palliat Care Pharmacother | Cochrane 系統性回顧的季度整理，與本藥關聯間接 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65861 | VICK-DICOT TABLETS 30MG | 未載明 | 未載明 |
| HK-57588 | DICODEIN TAB 30MG | 未載明 | 未載明 |
| HK-54981 | REUTOO SYRUP 10MG/5ML | 未載明 | 未載明 |
| HK-57139 | DICODEIN ORAL SOLUTION 15MG/5ML | 未載明 | 未載明 |
| HK-55815 | PARACODONE TAB | 未載明 | 未載明 |

共 11 張有效單方許可證（上表僅列 5 張），無已註銷者。

---

## 安全性考量

- **知識圖譜標示的相關疾病風險**（來自圖譜關聯，非仿單文字）：高血壓、肝衰竭、癲癇、慢性阻塞性肺病、腎臟疾病、胰臟炎、消化性潰瘍、發炎性腸病、糖尿病酮酸中毒、良性攝護腺肥大、甲狀腺功能低下、物質濫用／依賴、冠狀動脈疾病、心肌梗塞等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重 (Major)：Alvimopan、Bupropion
  - 中度 (Moderate)：Aprepitant、Atropine、Cimetidine、Dexamethasone、Loperamide、Glycopyrronium 等
- **濫用與依賴風險**：文獻指出含 dihydrocodeine 的鎮咳製劑曾出現濫用與依賴。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（鼻腔疾病）雖然分數很高，但沒有任何臨床試驗或文獻，且很可能是與原適應症相鄰所致的模型效應，證據等級僅 L5。
- 鴉片類藥物有依賴、濫用與多項疾病相關風險，在缺乏療效證據下不宜推進。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，建立鼻腔疾病的機轉連結
- 取得香港仿單的警語與禁忌症，完成安全性篩選
- 補齊許可證的劑型與核准適應症資料
- 若有興趣，可將「頭痛疾患」作為研究問題，另行評估療效與藥物過度使用性頭痛的風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

