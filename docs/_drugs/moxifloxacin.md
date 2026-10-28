---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 601
evidence_level: L5
indication_count: 9
monitor_inn: "MOXIFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
last_modified_at: 2026-10-23
description: "Moxifloxacin：預測新適應症為多形性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)（證據等級 L5）。原適應症：知識圖譜記錄的細菌感染相關用途（如細菌性肺炎、腹膜炎、結膜炎、鼠疫）"
---

# Moxifloxacin
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

## Moxifloxacin：從細菌感染到多形性高黏滯症候群（預測分數最高者）
{: .text-alpha }

## 一句話總結

Moxifloxacin 是氟喹諾酮類抗菌藥物，知識圖譜中記錄的原適應症包括肺炎、腹膜炎、結膜炎、鼠疫等細菌感染。
TxGNN 模型預測分數最高的新適應症為**多形性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)**，但目前**沒有任何臨床試驗或文獻**直接支持，證據等級為 L5，建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的細菌感染相關用途（如細菌性肺炎、腹膜炎、結膜炎、鼠疫）；香港許可證資料中未提供核准適應症文字 |
| 預測新適應症 | 多形性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 10 張／共 10 張） |
| 許可證數 | 10 張（有效 10 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，Moxifloxacin 屬氟喹諾酮類抗菌藥，作用於細菌 DNA 旋轉酶與拓樸異構酶 IV。

多形性高黏滯症候群是免疫球蛋白過多造成血液黏滯度上升，並非感染性疾病。**目前沒有可辨識的合理機轉連結**，高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據，因此此預測可信度低。

### 其他預測候選一覽

同一批預測中的其他疾病同樣缺乏支持：

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 說明 |
|------|---------|-----------|---------|------|
| 2 | 高澱粉酶血症 | 0.9998 | L5 | 無機轉連結，無試驗或文獻 |
| 3 | 先天性無白蛋白血症 | 0.9997 | L5 | 僅有 1 篇與療效無關的病例報告（低血糖），不直接支持治療用途 |
| 4 | 血型不合 | 0.9996 | L5 | 無機轉連結 |
| 5 | 癌前血液系統疾病 | 0.9995 | L5 | 無機轉連結 |
| 6 | 單株免疫球蛋白病變 | 0.9995 | L5 | 僅有感染併發症的病例報告與不相關試驗 |
| 7 | 伴隨後天性周邊神經病變的血液疾病 | 0.9994 | L5 | 與已知安全性（周邊神經病變警語）相抵觸 |
| 8 | 先天性血液疾病 | 0.9991 | L5 | 僅有間接的感染預防試驗 |
| 9 | 造血及淋巴系統腫瘤 | 0.9967 | L5 | 無直接抗腫瘤證據 |

> 說明：第 3、6、8 項雖有少量相關文獻或試驗，但均未直接研究 Moxifloxacin 對該疾病本身的療效，依規則一律評為 L5。

---

## 臨床試驗證據

目前無相關臨床試驗登記（針對首位預測的多形性高黏滯症候群）。

---

## 文獻證據

目前無相關文獻（針對首位預測的多形性高黏滯症候群）。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65835 | RIVOMOXI TABLETS 400MG | — | 資料未提供 |
| HK-68207 | MOXIFORCE EYE DROPS 0.5% W/V | — | 資料未提供 |
| HK-65455 | MOXIFLOXACIN TABLETS 400MG | — | 資料未提供 |
| HK-53158 | VIGAMOX OPHTHALMIC SOLUTION 0.5% | — | 資料未提供 |
| HK-46950 | AVELOX TAB 400MG | — | 資料未提供 |

本藥共有 10 張有效許可證（皆為單一成分），上表僅列前 5 張。其餘包括口服錠劑、靜脈注射劑與多款眼藥水。

---

## 安全性考量

- **知識圖譜中記錄的禁忌關聯（非仿單內容）**：長 QT 症候群、尖端扭轉型心室頻脈、癲癇、肝硬化、低血鉀、肌腱炎、周邊神經病變、困難梭狀芽孢桿菌結腸炎、重症肌無力、藥物性肝損傷、心肌缺血、冠狀動脈疾病等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重（Major）：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone（皮質類固醇，與肌腱損傷風險相關）、Bupropion、Chlorpropamide
  - 中度（Moderate）：Acarbose、Metformin、Pioglitazone、Famotidine、Loperamide、Acetylsalicylic acid、鈣鹽類等（多與血糖異常或吸收相關）

仿單的警語與禁忌資料尚未取得，詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測缺乏任何臨床試驗與文獻，也沒有合理的作用機轉；高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。
- 部分預測（如周邊神經病變相關血液疾病）與已知安全性風險相抵觸，不建議推進。

**若要推進需要：**
- 取得 DrugBank 作用機轉資料與香港仿單的警語、禁忌內容
- 重新評估預測，優先考慮有生物學合理性的疾病
- 若仍要探討特定疾病，需先有直接研究該疾病的臨床或前臨床證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

