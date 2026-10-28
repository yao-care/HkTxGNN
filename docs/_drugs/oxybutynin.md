---
layout: default
title: Oxybutynin
parent: 僅模型預測 (L5)
nav_order: 651
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "Oxybutynin"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
description: "Oxybutynin：預測新適應症為不寧腿症候群 (restless legs syndrome)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Oxybutynin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Oxybutynin: 不寧腿症候群 (restless legs syndrome)
{: .text-alpha }

## 一句話總結

Oxybutynin 原本用於治療膀胱過動症、神經性膀胱等下泌尿道問題。
TxGNN 模型預測它可能對**不寧腿症候群 (Restless Legs Syndrome)** 有效，但目前**沒有臨床試驗和文獻**直接支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 不寧腿症候群 (restless legs syndrome) |
| TxGNN 預測分數 | 0.9974 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

> 備註：香港許可證資料未提供核准適應症文字。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Oxybutynin 是抗膽鹼（抗毒蕈鹼）類藥物，並具有平滑肌direct 解痙作用，在膀胱過動症中的療效已被廣泛使用。

就不寧腿症候群而言，理論上可能是透過抗膽鹼作用調節中樞神經的膽鹼—多巴胺平衡，但這僅是推測。此外，Oxybutynin 本身會造成嗜睡、混亂等中樞神經副作用，且有報告指出抗膽鹼藥物可能使不寧腿症狀惡化，因此作用方向並不確定。

模型分數雖高，但沒有任何實證資料可以驗證，不應僅憑分數推進。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 其他預測適應症（供參考）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|------|-----------|-----------|---------|------|
| 2 | 胃十二指腸炎 (Gastroduodenitis) | 0.9962 | L5 | 無試驗或文獻；抗膽鹼作用可降低胃腸蠕動，但也可能延緩胃排空、降低下食道括約肌張力而加重上消化道症狀 |
| 3 | 消化性潰瘍 (Peptic Ulcer Disease) | 0.9931 | L5 | 僅有 3 篇早期文獻（見下表）；現今以 PPI 與 H. pylori 根除為主，附加價值低 |

消化性潰瘍相關文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | 病例報告 | DICP | Oxybutynin 因降低下食道括約肌張力，可能誘發逆流性食道炎，提示消化道安全疑慮 |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | 藥理學回顧 | Arch Int Pharmacodyn Ther | 描述 Oxybutynin 為具中度抗膽鹼作用的肌肉性解痙藥 |
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | 臨床評估 | Curr Ther Res | Oxybutynin 用於消化道疾病的早期臨床評估（無摘要，設計無法確認） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66392 | OXYBUTYNIN CHLORIDE TABLETS USP 5MG | 未提供 | 未提供 |
| HK-40556 | APO-OXYBUTYNIN TAB 5MG | 未提供 | 未提供 |
| HK-61447 | PMS-OXYBUTYNIN TABLETS 2.5MG | 未提供 | 未提供 |
| HK-66556 | OXYBUTYNIN HYDROCHLORIDE TABLETS 5MG | 未提供 | 未提供 |
| HK-61448 | PMS-OXYBUTYNIN TABLETS 5MG | 未提供 | 未提供 |

---

## 安全性考量

以下禁忌資料來自知識圖譜的藥物—疾病關聯，並非仿單文字：

- **禁忌／需避免的疾病**：
  - 消化道：麻痺性腸阻塞、腸阻塞、毒性巨結腸、潰瘍性結腸炎、發炎性腸道疾病、裂孔疝、胃食道逆流、食道炎
  - 眼睛：隅角閉鎖型青光眼
  - 神經肌肉：重症肌無力及相關神經肌肉接合部疾病
  - 泌尿：膀胱頸阻塞、良性攝護腺肥大
  - 心血管：高血壓、冠狀動脈疾病、心臟傳導疾病、心因性猝死
  - 其他：腎臟疾病、肝臟疾病、膽囊疾病、甲狀腺機能亢進（含 Graves 病）
- **藥物交互作用**（共查詢到 100 筆，以下為主要項目）：
  - **嚴重 (Major)**：氯化鉀、檸檬酸鉀
  - **中度 (Moderate)**：其他抗膽鹼／抗痙攣藥（Hyoscyamine、Atropine、Glycopyrronium、Dicyclomine、Trospium、Propantheline 等）、鴉片類（Morphine、Opium）、Loperamide、Metoclopramide、Aprepitant、Eluxadoline、Pramlintide
- **文獻提示**：Oxybutynin 可能導致逆流性食道炎（1990 年病例報告），並常見嗜睡、混亂等中樞神經副作用。

仿單的警語與禁忌資料尚未取得，完整資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 不寧腿症候群的預測分數很高（0.9974），但沒有任何臨床試驗或文獻佐證，屬於 L5 等級；機轉方向也不確定，抗膽鹼藥物甚至可能加重症狀。
- 次要預測（消化性潰瘍、胃十二指腸炎）同樣缺乏現代證據，且 Oxybutynin 有潛在的消化道不良反應。

**若要推進需要：**
- 取得 Oxybutynin 的作用機轉資料（如 DrugBank）
- 取得香港衛生署仿單的警語與禁忌，完成安全性篩選
- 系統性搜尋不寧腿症候群與抗膽鹼藥物的文獻，釐清作用方向（有益或惡化）
- 若方向合理，再設計小規模探索性研究，並特別監測中樞神經與消化道不良反應
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

