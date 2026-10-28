---
layout: default
title: Clofedanol
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "Clofedanol"
predicted_indications: ["nasal cavity disease", "allergic urticaria", "papillary conjunctivitis", "cold urticaria", "faucial diphtheria", "cervical disc degenerative disorder"]
description: "Clofedanol：預測新適應症為鼻腔疾病 (nasal cavity disease)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Clofedanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Clofedanol: 鼻腔疾病 (nasal cavity disease)
{: .text-alpha }

## 一句話總結

Clofedanol 原本用於過敏性鼻炎、血管運動性鼻炎、咽炎及普通感冒等上呼吸道症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
但目前**沒有臨床試驗和文獻**支持，屬於僅有模型預測的階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 鼻腔疾病 (nasal cavity disease) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Clofedanol 是一種鎮咳藥，兼具抗組織胺特性，
可能緩解上呼吸道症狀，但此作用機轉在本次彙整的資料中尚未獲得驗證。

「鼻腔疾病」是涵蓋過敏性鼻炎、血管運動性鼻炎及鼻炎的較廣泛類別。
模型的高分很可能來自與這些既有適應症的重疊。
因此，這個預測較可能是**既有適應症的範圍延伸**，而非真正的新用途開發機會。

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
| HK-22202 | COLDRIN TAB 12.5MG | 未載明 | 未載明 |

---

## 其他 TxGNN 預測的候選適應症

| 排名 | 預測適應症 | 分數 | 評估 |
|------|-----------|------|------|
| 3 | 過敏性蕁麻疹 (Allergic Urticaria) | 0.9997 | 可能與 H1 抗組織胺活性有關，但未獲資料證實 |
| 4 | 乳突性結膜炎 (Papillary Conjunctivitis) | 0.9984 | 可能共享過敏與組織胺路徑，屬推測；眼部給藥需另行開發劑型 |
| 5 | 寒冷性蕁麻疹 (Cold Urticaria) | 0.9978 | 可能因名稱與「普通感冒」相近而使分數偏高，宜謹慎看待 |
| 6 | 咽白喉 (Faucial Diphtheria) | 0.9933 | 白喉為細菌感染，最多只能緩解症狀，此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據 |
| 7 | 頸椎椎間盤退化 (Cervical Disc Degenerative Disorder) | 0.9929 | 找不到合理的機轉連結，可能是虛假預測 |

以上候選適應症皆無臨床試驗或文獻支持，證據等級均為 L5。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自模型知識圖譜，非仿單內容）：高血壓、胰臟炎、消化性潰瘍、糖尿病及糖尿病酮酸中毒、良性前列腺增生、冠狀動脈疾病、心肌梗塞、動脈粥狀硬化、血紅素病變、高眼壓、閉角型青光眼、甲狀腺機能亢進（Graves 病）、膀胱頸阻塞、心室頻脈、酸中毒、房室傳導阻滯等。
- **藥物交互作用**：共查得 100 筆，以下為部分中度交互作用的藥物：
  - 鴉片類及中樞抑制劑：Morphine、Codeine、Dihydrocodeine、Fentanyl、Alfentanil、Tramadol、Opium、Diphenoxylate、Difenoxin
  - 抗組織胺：Chlorpheniramine、Cetirizine、Promethazine、Phenyltoloxamine
  - 其他：Alprazolam、Ethanol、Dronabinol、Nabilone、Metoclopramide、Sibutramine、Dichloralphenazone
  - 這些藥物多可能產生中樞神經抑制的疊加效應。

香港仿單的警語與禁忌資料尚未取得，詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何臨床試驗或文獻佐證（L5），且作用機轉資料缺乏。
- 「鼻腔疾病」與既有鼻炎適應症高度重疊，較像是原適應症的延伸，而非新的再利用機會。

**若要推進需要：**
- 取得並解析香港衛生署的仿單，確認警語、禁忌及核准適應症
- 補充 Clofedanol 的作用機轉資料（例如查詢 DrugBank）
- 釐清「鼻腔疾病」預測與既有鼻炎適應症的實質差異，確認是否有真正的新增價值
- 搜尋並評估相關臨床試驗與文獻
- 完成安全性篩檢，特別是對高血壓、心血管疾病、青光眼等族群，以及與中樞抑制劑併用的風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

