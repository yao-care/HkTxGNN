---
layout: default
title: Morphine
parent: 僅模型預測 (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Morphine：預測新適應症為肌筋膜疼痛症候群 (Myofascial Pain Syndrome)（證據等級 L5）。原適應症：腹瀉性疾病"
---

# Morphine
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

# Morphine：從腹瀉性疾病到不寧腿症候群

## 一句話總結

Morphine（嗎啡）是經典的 mu 類鴉片受體促效劑，在本次資料中的原適應症為腹瀉性疾病（diarrheal disease）。
TxGNN 模型預測的首位新適應症為**肌筋膜疼痛症候群 (myofascial pain syndrome)**，但該項證據薄弱。依證據強度，較值得關注的是**不寧腿症候群 (restless legs syndrome, RLS)**：有 **1 個臨床試驗**（Phase 1）和多篇觀察性研究、病例報告支持。

> 說明：預測排名第一的肌筋膜疼痛症候群僅有間接文獻，無臨床試驗。以下表格依規定呈現排名第一的預測，並另列證據最強的 RLS 供決策參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腹瀉性疾病（diarrheal disease，來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 肌筋膜疼痛症候群 (Myofascial Pain Syndrome) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L4（肌筋膜疼痛症候群）；證據最強的候選 RLS 為 L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Hold（肌筋膜疼痛症候群）；RLS 列為研究問題 |

### 前 10 名預測概覽

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|------|-----------|------|---------|------|
| 1 | 肌筋膜疼痛症候群 | 99.75% | L4 | Hold |
| 2 | 躁型雙極性情感障礙 | 99.64% | L5 | Hold |
| 3 | 妥瑞氏症 | 99.48% | L5 | Hold |
| 4 | 不寧腿症候群 | 99.47% | L3 | 研究問題 |
| 5 | 注意力不足過動症（注意力不足型） | 99.34% | L5 | Hold |
| 6 | 偏頭痛 | 99.32% | L4 | Hold |
| 7 | 拔毛症 | 99.29% | L5 | Hold |
| 8 | 高鐵血紅素血症 | 99.15% | L5 | Hold |
| 9 | 伴腦幹先兆的偏頭痛 | 99.15% | L5 | Hold |
| 10 | 特定發展障礙 | 99.06% | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，嗎啡是 mu 類鴉片受體促效劑，具有確立的鎮痛作用，這也是它與疼痛類疾病產生關聯的基礎。

**肌筋膜疼痛症候群：**肌筋膜疼痛以周邊肌肉骨骼問題為主，鴉片類藥物並非標準治療。現有文獻為間接證據，包括顳顎關節功能障礙的長期鴉片使用、嗎啡加 dexmedetomidine 用於脊椎融合術肌筋膜浸潤的隨機試驗，以及圍手術期疼痛研究，並未直接證明嗎啡能治療肌筋膜疼痛症候群。

**不寧腿症候群：**鴉片類藥物作用於內源性鴉片系統，並調節與 RLS 相關的多巴胺與感覺傳導路徑。對於多巴胺促效劑或 α2δ 配體無效、或出現加重現象（augmentation）的難治型 RLS，低劑量鴉片類藥物已在臨床上使用，嗎啡（含脊髓腔內給藥）也有案例與病例系列報告。這是目前機轉與臨床線索最一致的方向。

---

## 臨床試驗證據

肌筋膜疼痛症候群目前無相關臨床試驗登記。

證據最強的候選適應症 RLS 有 1 個試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01476124](https://clinicaltrials.gov/study/NCT01476124) | Phase 1 | 完成 | 18 | 健康受試者的三階段交叉試驗，評估 gabapentin enacarbil 與嗎啡單獨及併用時的藥動學和耐受性；無 RLS 病人的療效資料 |

---

## 文獻證據

### 肌筋膜疼痛症候群（排名第一）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | RCT | Asian Spine J | 脊椎融合術中，dexmedetomidine 加嗎啡與單用 ropivacaine 做肌筋膜浸潤的雙盲比較 |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | RCT | Eur J Obstet Gynecol Reprod Biol | 評估陰部神經阻斷是否改善肌筋膜骨盆疼痛 BTA 注射後的疼痛 |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | RCT | Eur J Pain | 比較硬膜外鎮痛（含嗎啡）與肋間神經冷凍鎮痛用於開胸術後疼痛 |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohort | Pain Pract | 結構化伸展運動計畫對肌筋膜疼痛緩解與鴉片類藥物使用的影響 |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | 顳顎關節功能障礙長期使用鴉片類藥物的證據既不能支持也不能否定 |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Review | J Oral Maxillofac Surg | 顳顎關節灌洗後關節內嗎啡注射的臨床做法 |

上述文獻多為間接證據，無一直接檢驗嗎啡治療肌筋膜疼痛症候群。

### 不寧腿症候群（證據最強的候選）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41543123](https://pubmed.ncbi.nlm.nih.gov/41543123/) | 2026 | Cohort | Sleep | 全國 RLS 鴉片登錄系統 5 年資料，評估療效與劑量穩定性 |
| [39106456](https://pubmed.ncbi.nlm.nih.gov/39106456/) | 2024 | Cohort | Pain | 長期脊髓腔內低劑量嗎啡可緩解嚴重 RLS，且未誘發耐受 |
| [36697248](https://pubmed.ncbi.nlm.nih.gov/36697248/) | 2023 | Cohort | Neurology | 2 年登錄資料，探討鴉片類藥物的長期安全性、劑量穩定性與療效 |
| [31883387](https://pubmed.ncbi.nlm.nih.gov/31883387/) | 2020 | Cohort | Acta Neurol Scand | 植入式幫浦給予脊髓腔內嗎啡治療難治型 RLS 的療效與併發症 |
| [32918469](https://pubmed.ncbi.nlm.nih.gov/32918469/) | 2021 | Cohort | Sleep | 全國 RLS 鴉片登錄系統基線與 1 年追蹤資料 |
| [27310338](https://pubmed.ncbi.nlm.nih.gov/27310338/) | 2016 | Review | Expert Opin Drug Metab Toxicol | 鴉片類藥物治療 RLS 的藥理與臨床面向 |
| [27964861](https://pubmed.ncbi.nlm.nih.gov/27964861/) | 2017 | Review | Sleep Med | 疼痛、鴉片類藥物與睡眠對 RLS 治療的意涵 |
| [29304922](https://pubmed.ncbi.nlm.nih.gov/29304922/) | 2018 | 文獻回顧（專家建議） | Mayo Clin Proc | 總結鴉片類藥物用於難治型 RLS 的基礎與臨床證據 |
| [31133964](https://pubmed.ncbi.nlm.nih.gov/31133964/) | 2019 | Case report | Front Neurol | 癌症疼痛病人使用嗎啡與 fentanyl 後 RLS 改善 |
| [36692170](https://pubmed.ncbi.nlm.nih.gov/36692170/) | 2023 | Case report | J Clin Sleep Med | 停用鴉片類藥物期間出現 RLS |

---

## 香港上市資訊

目前資料顯示共有 15 張有效許可證，皆為單方製劑。許可證資料中未載明劑型與核准適應症文字，以下列出主要 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-28287 | MORPHINE SULPHATE INJ 10MG/ML (B. BRAUN) | 注射劑（依品名） | 資料未載明 |
| HK-64596 | OMORFATE ORAL SOLUTION 5MG/5ML | 口服溶液（依品名） | 資料未載明 |
| HK-64155 | UNI-MORPHINE SYRUP (ALCOHOL FREE) 50MG/5ML | 糖漿（依品名） | 資料未載明 |
| HK-45210 | MST CONTINUS TAB 10MG-PROLONGED RELEASE | 持續釋放錠（依品名） | 資料未載明 |
| HK-40464 | MORPHINE SULPHATE INJ 10MG/ML | 注射劑（依品名） | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物與疾病禁忌關聯，非仿單文字）：高血壓、姿勢性低血壓、長 QT 症候群、尖端扭轉型心律不整、肝衰竭與肝病、腎臟疾病、癲癇、慢性阻塞性肺病、胃潰瘍、胰臟炎、膽囊疾病、甲狀腺功能低下、精神病性疾患與思覺失調相關疾患、焦慮症、鉀缺乏症等。
- **藥物交互作用**：資料庫共有 100 筆交互作用紀錄，列出的 20 筆中，重大（Major）等級包括 fentanyl、dihydrocodeine、codeine、tramadol、butalbital、乙醇、alprazolam、dichloralphenazone。這些多為中樞神經與呼吸抑制疊加風險，應避免或嚴密監測合併使用。中度等級包括 chlorpheniramine、cetirizine、nifedipine、hydrochlorothiazide、metformin 等。
- **新適應症相關風險**：用於 RLS 時需注意依賴性、鴉片類藥物引起的睡眠呼吸障礙，以及停藥後 RLS 症狀出現或加重。用於偏頭痛時有藥物過度使用型頭痛與痛覺過敏風險。用於躁症時有濫用傾向與情緒不穩惡化的疑慮。

香港仿單的警語與禁忌尚未取得，詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（肌筋膜疼痛症候群）；RLS 作為研究問題優先評估**

**理由：**
- 排名第一的肌筋膜疼痛症候群僅有間接文獻，且鴉片類藥物並非其標準治療，不支持推進。其餘多數預測（雙極性躁症、妥瑞氏症、ADHD、拔毛症、高鐵血紅素血症等）為 L5 純模型預測，或機轉不合理。偏頭痛則因現行指引不建議使用鴉片類藥物而不宜推進。
- RLS 有觀察性登錄研究、病例系列及專家共識支持，嗎啡（含脊髓腔內給藥）用於難治型 RLS 有臨床基礎，但缺乏嗎啡專屬的 Phase 2/3 RCT，且多數研究以鴉片類藥物整體為對象，嗎啡的特定療效未獲證實。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，完成安全性篩選。
- 補充詳細的作用機轉資料。
- 針對難治型 RLS 設計嗎啡專屬的對照試驗，或系統性回顧現有登錄與病例資料。
- 建立依賴性、呼吸抑制、加重現象的風險管理計畫，並確認管制藥品使用規範。
- 評估適用劑型與給藥途徑（口服與脊髓腔內）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

