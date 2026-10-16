---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 792
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Rufinamide：預測新適應症為熱病相關難治性癲癇症候群 (FIRES)（證據等級 L5）。原適應症：Lennox-Gastaut 症候群"
monitor_inn: "RUFINAMIDE"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "photosensitive occipital lobe epilepsy", "atypical childhood epilepsy with centrotemporal spikes", "cryptogenic late-onset epileptic spasms"]
---

# Rufinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rufinamide：從 Lennox-Gastaut 症候群到熱病相關難治性癲癇症候群（FIRES）

## 一句話總結

Rufinamide 是一種抗癲癇藥物，原本用於治療 Lennox-Gastaut 症候群。
TxGNN 模型預測它可能對**熱病相關難治性癲癇症候群 (Febrile Infection-Related Epilepsy Syndrome, FIRES)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Lennox-Gastaut 症候群（來源為知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 熱病相關難治性癲癇症候群 (FIRES) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理學一般知識，Rufinamide 是鈉離子通道調節劑，可延長電壓門控鈉離子通道的不活化狀態，已用於 Lennox-Gastaut 症候群這類嚴重的發展性與癲癇性腦病變。（此說明為一般藥理推論，非來自本次彙整的資料。）

FIRES 是發燒性感染後出現的難治性癲癇性腦病變，與 Lennox-Gastaut 症候群同樣有嚴重的癲癇發作表現，這是合理但未經證實的關聯。

不過，FIRES 的病程涉及神經發炎，單純阻斷鈉離子通道不一定能處理其發炎成因。TxGNN 分數雖高，但缺乏實際研究佐證，應視為提出假說的線索。

**其他預測適應症（皆為 L5、Hold）：**

| 排名 | 預測適應症 | TxGNN 分數 | 備註 |
|------|-----------|-----------|------|
| 2 | 口周肌陣攣伴失神發作 (Perioral myoclonia with absences) | 99.51% | 失神發作主要由丘腦皮質 T 型鈣離子通道驅動，鈉離子通道阻斷劑可能使失神發作惡化，需留意安全性 |
| 3 | 光敏感性枕葉癲癇 (Photosensitive occipital lobe epilepsy) | 99.44% | 局部性癲癇，屬抗癲癇藥物類別層級的推論 |
| 4 | 非典型兒童中央顳區棘波癲癇 | 99.44% | 與 Lennox-Gastaut 症候群有表型重疊，但鈉離子通道阻斷劑在非典型型態可能加重發作 |
| 5 | 隱源性晚發性癲癇性痙攣 | 99.44% | 可能與 Lennox-Gastaut 症候群重疊或演變，但一線藥物（ACTH、類固醇、vigabatrin）機轉不同 |

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
| HK-64099 | INOVELON TABLETS 400MG（Eisai） | 錠劑 | 許可證資料未載明 |
| HK-64097 | INOVELON TABLETS 100MG（Eisai） | 錠劑 | 許可證資料未載明 |
| HK-64098 | INOVELON TABLETS 200MG（Eisai） | 錠劑 | 許可證資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容）：肝衰竭、肝臟疾病、膽囊疾病、白血球低下、焦慮症、神經官能症、情緒低落症（dysthymic disorder）。
- **藥物交互作用**：共查得 100 筆，以下為其中部分中度 (Moderate) 交互作用：
  - 類固醇類：Hydrocortisone、Triamcinolone、Betamethasone、Prednisone
  - 維生素 D 類：Cholecalciferol、Calcifediol、Calcitriol
  - 中樞神經／鴉片類：Morphine、Difenoxin、Diphenoxylate、Dronabinol、Nabilone
  - 其他：Pioglitazone、Bupropion、Eliglustat、Naloxegol、Metoclopramide、Nitisinone、Ondansetron、Rolapitant
- 其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆僅有模型預測（L5），沒有臨床試驗或文獻佐證。
- FIRES 的發炎性病程與鈉離子通道機轉不完全吻合，部分其他預測適應症（如失神發作類）甚至有惡化風險。

**若要推進需要：**
- 取得 Rufinamide 的作用機轉資料，並完成機轉與 FIRES 病理的對應分析。
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症。
- 系統性檢索 FIRES 及相關癲癇症候群中使用 Rufinamide 的病例報告與觀察性研究。
- 針對失神發作類與非典型癲癇症候群，先評估鈉離子通道阻斷劑可能加重發作的風險。
- 若上述初步證據支持，再考慮設計探索性臨床研究。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

