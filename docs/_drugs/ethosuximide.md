---
layout: default
title: Ethosuximide
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Ethosuximide：預測新適應症為腎因性抗利尿不適當症候群 (NSIAD)（證據等級 L5）。原適應症：失神發作癲癇 (absence epilepsy)"
monitor_inn: "ETHOSUXIMIDE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Ethosuximide：從失神發作癲癇到抗利尿不適當腎因性症候群
{: .text-alpha }

## 一句話總結

Ethosuximide 原本用於治療失神發作癲癇 (absence epilepsy)。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，預測僅來自模型運算。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 失神發作癲癇 (absence epilepsy) |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為 ethosuximide 會阻斷丘腦神經元的 T 型鈣離子通道，這是它用於失神發作癲癇的基礎。

NSIAD 的成因是血管加壓素 V2 受體 (AVPR2) 的功能獲得性突變，或在部分病例中是 GNAS 突變，導致不依賴血管加壓素的持續抗利尿。目前沒有已知的路徑能把 T 型鈣離子通道阻斷與 AVPR2 訊號異常連結起來。

0.999 的高分來自知識圖譜的連結性，並沒有臨床或文獻證據佐證，任何機轉關聯都仍屬假設。另外，ethosuximide 在少數報告中曾與低血鈉或類 SIADH 效應有關，這與 NSIAD 的治療方向相反，需要特別留意。

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
| HK-68479 | ETHOSUXIMIDE CAPSULES 250MG | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜中的禁忌疾病（非仿單內容）**：焦慮症、神經症、輕鬱症 (dysthymic disorder)、腎臟疾病、輸尿管積膿、血液疾病、肝臟疾病、膽囊疾病、系統性紅斑狼瘡（含兒童型）、嗜中性白血球低下、顆粒球缺乏症、急性間歇性紫質症。
- **藥物交互作用**：共查得 92 筆，以下為部分中度交互作用：
  - 中樞抑制相關：Morphine、Opium、Dronabinol、Nabilone、Promethazine、Chlorpheniramine、Ethanol
  - 其他：Aprepitant、Metoclopramide、Cobicistat、Folic acid、Leucovorin、Levoleucovorin、Deferasirox、Fostamatinib、Chloroquine、Mefloquine、Hydroxychloroquine、Sibutramine

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或文獻，證據等級僅為 L5。
- 機轉上沒有合理的連結，且 ethosuximide 可能引起低血鈉或類 SIADH 效應，與 NSIAD 的治療方向可能相反。

**若要推進需要：**
- 取得完整作用機轉資料，並做機轉合理性分析（T 型鈣離子通道與 AVPR2/GNAS 訊號的關聯）。
- 進行前臨床研究（如細胞或動物模型）驗證是否有任何效應。
- 取得香港仿單的警語與禁忌資料，完成安全性篩選。
- 評估 ethosuximide 造成低血鈉或類 SIADH 效應的風險，以及腎臟疾病禁忌對目標族群的影響。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

