---
layout: default
title: Febuxostat
parent: 中證據等級 (L3-L4)
nav_order: 364
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Febuxostat：預測新適應症為腎性低尿酸血症 (Hypouricemia, Renal)（證據等級 L4）。原適應症：高尿酸血症（obsolete hyperuricemia）"
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

## Febuxostat：從高尿酸血症到腎性低尿酸血症
{: .text-alpha }

## 一句話總結

Febuxostat 是一種非嘌呤類黃嘌呤氧化酶抑制劑，原本用於治療高尿酸血症。
TxGNN 模型預測它可能對**腎性低尿酸血症 (Hypouricemia, Renal)** 有效，但目前僅有 **1 個相關性不明的臨床試驗**和 **2 篇文獻**，證據薄弱，且機轉上有疑慮。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高尿酸血症（obsolete hyperuricemia） |
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, Renal) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L4 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Febuxostat 是選擇性黃嘌呤氧化酶抑制劑，可降低血清尿酸，其在高尿酸血症中的療效已被證實。

不過，腎性低尿酸血症的特徵是腎臟尿酸再吸收缺陷（如 URAT1/SLC22A12 或 GLUT9/SLC2A9 功能喪失），患者血中尿酸本來就偏低。進一步降尿酸缺乏明確的治療理由，還可能增加運動誘發急性腎損傷或泌尿道結石的風險。高分預測較可能反映的是模型中該藥與尿酸代謝的網絡鄰近性，而非真正的治療關聯。

唯一值得留意的是 2023 年的文獻，討論以非嘌呤類黃嘌呤氧化還原酶抑制劑預防腎性低尿酸血症患者的運動誘發急性腎損傷。這屬於假說層次，並非療效證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | 未知 | 100 | 探討控制尿酸對高尿酸血症結石患者結石復發與腎功能的影響；與腎性低尿酸血症的關聯無法確認，不能作為直接證據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | 病例報告（資料庫分類為 Review） | Internal Medicine | 一名患有家族性腎性低尿酸血症（URAT1 複合雜合突變）的 16 歲足球員反覆發生運動誘發急性腎損傷；水分補充無法預防，之後嘗試使用 febuxostat 作為預防 |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | 為臨床風濕科醫師整理低尿酸血症（血清尿酸 < 2 mg/dL）的病因與處置 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61185 | FEBURIC TABLETS 80 MG（Astellas） | 錠劑 | 未提供 |
| HK-61186 | FEBURIC TABLETS 120 MG（Astellas） | 錠劑 | 未提供 |
| HK-67630 | FEBUSTAD 80 TABLETS 80MG | 錠劑 | 未提供 |
| HK-67470 | FEBUXOSTAT GENEPHARM TABLETS 80MG | 錠劑 | 未提供 |
| HK-67668 | FEBUXOSTAT SANDOZ TABLETS 80MG | 錠劑 | 未提供 |

香港共有 12 張有效單方許可證，上表僅列出 5 張。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單內容）：中風、腦血管疾病、腦梗塞、心肌梗塞、冠狀動脈血栓、血紅素病變。
- **藥物交互作用**：共 22 筆，其中**重大 (Major)** 交互作用包括：
  - Mercaptopurine
  - Azathioprine
  - Leflunomide
  - Teriflunomide

  中度 (Moderate) 交互作用包括 Theophylline、Aminophylline、Dyphylline、Oxtriphylline、Methotrexate、Naltrexone、Tioguanine、Epirubicin、Clofarabine 等。
- **預測適應症相關風險**：進一步降低尿酸可能加重運動誘發急性腎損傷或尿路結石的風險。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 腎性低尿酸血症的問題是尿酸過低，繼續降尿酸缺乏明確治療依據，且有加重腎臟風險的可能。高 TxGNN 分數較可能是網絡鄰近性造成的假象。
- 現有證據僅有 1 個相關性未確認的試驗與個案層級文獻，無法支持推進。

**若要推進需要：**
- 補充作用機轉資料，並釐清其與 URAT1/GLUT9 缺陷病理的關聯
- 確認 NCT04398251 登記內容是否真與腎性低尿酸血症有關
- 取得香港仿單的警語與禁忌資料
- 對 2023 年個案中 febuxostat 的實際用法與結果做更詳細的檢視，再評估是否值得設計前瞻性研究

---

### 其他值得關注的預測方向

模型另外預測兩個機轉上較合理的適應症，目前同樣只有個案層級證據，無臨床試驗，建議列為研究問題：

- **次黃嘌呤鳥嘌呤磷酸核糖轉移酶部分缺乏症 (partial HPRT deficiency)**（TxGNN 分數 0.9998）：尿酸過度生成，抑制黃嘌呤氧化酶機轉上合理。需留意次黃嘌呤與黃嘌呤累積造成黃嘌呤腎病變或結石的風險。
- **Lesch-Nyhan 症候群**（TxGNN 分數 0.9968）：可作為對 allopurinol 不耐受時的替代，但無法改善神經與行為症狀；兒童使用與黃嘌呤結石風險需謹慎。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

