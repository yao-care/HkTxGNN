---
layout: default
title: Homatropine
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Homatropine：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：消化性潰瘍、葡萄膜炎、虹膜疾病、睫狀肌麻痺等"
monitor_inn: "Homatropine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "gastroduodenitis", "overactive bladder (disease)"]
---

# Homatropine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Homatropine：從消化性潰瘍與眼科疾病到脊髓馬尾症候群
{: .text-alpha }

## 一句話總結

Homatropine 是一種抗膽鹼（毒蕈鹼拮抗）藥物，原本用於消化性潰瘍、葡萄膜炎、睫狀肌麻痺等疾病。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消化性潰瘍、葡萄膜炎、虹膜疾病、睫狀肌麻痺等（香港許可證未載明核准適應症，此為知識圖譜所列） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Homatropine 屬於毒蕈鹼拮抗劑（抗膽鹼藥物）類別，這類藥物能降低逼尿肌收縮力，理論上可能改善馬尾症候群繼發的膀胱功能障礙。

但需要注意：馬尾症候群的本質是需要緊急手術處理的神經壓迫，抗膽鹼藥物最多只能緩解下游的泌尿症狀，無法治療疾病本身。此預測完全依賴模型分數，缺乏任何實證支持。

模型另外預測了三個適應症，同樣僅有 L5 證據：

| 排名 | 預測適應症 | 預測分數 | 說明 |
|------|-----------|---------|------|
| 2 | 神經性膀胱（本體論中已標為過時術語） | 99.75% | 抗毒蕈鹼藥物用於神經性逼尿肌過動有類別層級的依據；需先對應到現行術語（如 neurogenic detrusor overactivity）再評估 |
| 3 | 胃十二指腸炎 | 99.51% | 與既有的消化性潰瘍適應症最接近，但抗膽鹼藥物已非標準治療 |
| 4 | 膀胱過動症 | 99.16% | 類別層級理由強，但已有更具膀胱選擇性且研究較充分的藥物，且抗膽鹼副作用需評估 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66532 | HOMATROPINE HBR EYE DROPS 2% W/V | 滴眼液（依品名） | 資料未載明 |

此為香港唯一的許可證（單一成分、有效），製造商為 JEAN-MARIE PHARMACAL CO LTD。目前上市的劑型為眼用製劑，與預測的新適應症（泌尿或神經相關）給藥途徑不同，若要推進需評估劑型與途徑的相容性。

## 安全性考量

- **禁忌症（來自知識圖譜，非仿單內容）**：知識圖譜列出的相關疾病包括高血壓、低血壓、肝衰竭、肝性腦病變、癲癇、胃潰瘍、焦慮症、卟啉症、腎臟疾病、膽囊疾病、血小板低下、嗜中性球低下、顆粒球缺乏症、甲狀腺功能低下、發炎性腸道疾病、良性前列腺增生、冠狀動脈疾病、阻塞性睡眠呼吸中止症、物質濫用或依賴等。
- **藥物交互作用**：共 17 筆紀錄，其中：
  - **重大 (Major)**：氯化鉀 (Potassium chloride)、檸檬酸鉀 (Potassium citrate)
  - **中度 (Moderate)**：其他抗膽鹼藥物（Dicyclomine、Glycopyrronium、Hyoscyamine、Mepenzolate、Methscopolamine、Propantheline、Ipratropium）、鴉片類（Opium、Hydrocodone）、膽鹼酯酶抑制劑（Edrophonium、Physostigmine），以及 Cyclizine、Phenindamine、Phenylephrine、Thiethylperazine 等

仿單的警語與禁忌資料尚未取得，詳細資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 四項預測皆僅有模型分數支持（L5），沒有任何臨床試驗或文獻。
- 馬尾症候群的核心問題是神經壓迫，抗膽鹼藥物無法治療疾病本身；香港現有劑型也是眼用製劑，與預測用途不符。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 補充作用機轉（MOA）資料
- 將「神經性膀胱」對應到現行本體論術語後重新評估
- 針對 Homatropine 本身進行文獻與臨床試驗檢索
- 評估是否需要全身性或其他劑型，並與已有充分證據的膀胱選擇性抗毒蕈鹼藥物比較
- 若仍想探索，優先考慮與既有適應症最接近的胃十二指腸炎，或以膀胱症狀為目標的方向，而非馬尾症候群本身
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

