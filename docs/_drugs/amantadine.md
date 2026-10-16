---
layout: default
title: Amantadine
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Amantadine：預測新適應症為Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)（證據等級 L5）。原適應症：帕金森氏症及相關動作障礙"
---

# Amantadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Amantadine：從帕金森氏症到 Rasmussen 亞急性腦炎

## 一句話總結

Amantadine（金剛烷胺）原本用於帕金森氏症及相關錐體外徑疾病的治療。
TxGNN 模型預測它可能對 **Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個預測，僅屬模型推論階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 帕金森氏症及相關動作障礙（香港許可證未載明核准適應症文字） |
| 預測新適應症 | Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis) |
| TxGNN 預測分數 | 99.48% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理知識，amantadine 是 NMDA 受體拮抗劑，也具有多巴胺調節作用。Rasmussen 腦炎是一種免疫介導的慢性腦炎，與麩胺酸相關的興奮性神經毒性損傷可能有關，因此在機轉上存在一個可能但**尚未驗證**的連結。

原適應症（帕金森氏症等動作障礙）與 Rasmussen 腦炎同屬中樞神經系統疾病，但病理本質不同：前者以神經退化為主，後者以免疫發炎為主。此推論屬推測性質，缺乏所提供資料的支持。

**其他預測的參考：**
- **脊髓炎 (myelitis)**（分數 99.24%，L4）：文獻多半與小兒麻痺後症候群的疲勞處理有關，屬間接證據，並非針對脊髓炎本身的治療。
- **PLA2G6 相關神經退化 (PLA2G6-associated neurodegeneration)**（分數 99.23%，L4）：僅有 1 篇針對另一亞型（PKAN）步態障礙的文獻，屬類比性間接證據。
- **轉醛醇酶缺乏症 (transaldolase deficiency)**（分數 99.27%，L5）：屬戊糖磷酸途徑代謝疾病，與 amantadine 藥理無明顯關聯，分數可能是知識圖譜的假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27366 | PK-MERZ TAB 100MG | — | — |
| HK-34789 | ENZIL TAB 100MG | — | — |
| HK-62120 | AMANDIN CAPSULES 100MG | — | — |
| HK-45493 | PMS-AMANTADINE HYDROCHLORIDE CAP 100MG | — | — |
| HK-59608 | AMANTADINE F.C. TAB 100MG | — | — |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單內容）：多系統萎縮、姿勢性姿態心搏過速症候群、姿態性低血壓、癲癇、腎臟病、膿輸尿管、充血性心衰竭、精神病性疾患、類精神分裂症、精神疾患、情感性精神分裂症、黑色素瘤、隅角閉鎖型青光眼、物質相關疾患／濫用依賴、異位性濕疹、皮膚炎。
- **藥物交互作用**：共查得 93 筆，以下為主要項目：
  - **重度**：Bupropion
  - **中度**：抗膽鹼藥物類，如 Atropine、Scopolamine、Hyoscyamine、Dicyclomine、Glycopyrronium、Clidinium、Mepenzolate、Methscopolamine、Propantheline、Trospium；另有 Metoclopramide、Polyethylene glycol（含電解質）、Picosulfuric acid、Sodium sulfate

仿單警語與禁忌資料尚未取得，詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Rasmussen 腦炎的預測分數雖高（99.48%），但沒有任何臨床試驗或文獻，證據等級僅為 L5，機轉連結也屬推測。
- 作用機轉與仿單安全性資料皆有缺口，目前無法進入安全性篩選。

**若要推進需要：**
- 取得 DrugBank 的作用機轉（MOA）資料
- 取得香港衛生署仿單的警語與禁忌資料
- 針對 Rasmussen 腦炎進行系統性文獻與試驗檢索，並評估 NMDA 拮抗作用的實驗依據
- 若考慮其他預測，可優先探討**脊髓炎**與 **PLA2G6 相關神經退化**（均為 L4），但需先釐清現有文獻實際對應的疾病（如小兒麻痺後症候群、PKAN）與預測適應症的差異
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

