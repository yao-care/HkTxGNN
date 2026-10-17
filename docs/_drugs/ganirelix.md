---
layout: default
title: Ganirelix
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ganirelix：預測新適應症為多毛症 (Hypertrichosis)（證據等級 L5）。原適應症：預防卵巢刺激期間提早排卵"
monitor_inn: "GANIRELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Ganirelix
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ganirelix：從控制性卵巢刺激期間預防提早排卵到多毛症

## 一句話總結

Ganirelix 是一種 GnRH 受體拮抗劑，臨床上用於接受不孕症治療、進行卵巢刺激的女性，以預防提早排卵。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防卵巢刺激期間提早排卵（來自藥理資料庫；香港許可證未載明適應症文字） |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料，Ganirelix 是 GnRH₁ 受體（GNRHR）的拮抗劑，可抑制 LH 與 FSH 分泌，並間接降低性腺性荷爾蒙。

多毛症 (Hypertrichosis) 並非典型由性腺雄性素過多所驅動（那是多毛症中的 hirsutism，即男性型多毛），因此機轉上的關聯性薄弱。0.9998 的高分僅反映知識圖譜中的網路鄰近性，不代表有生物學或臨床依據。

其他排名靠前的預測也呈現相同問題，包括 Ambras 型先天性全身多毛症、伴牙齒或牙周異常的畸形症候群、以 Dandy-Walker 畸形為主要特徵的症候群，以及遺傳性毛幹異常。這些多屬先天發育或結構性基因缺陷，抑制 GnRH 與性荷爾蒙軸線不太可能改變其病程。

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
| HK-49750 | ORGALUTRAN INJ 0.25MG/0.5ML | 注射劑 | 許可證資料未載明 |

製造商：ORGANON HONG KONG LIMITED

---

## 安全性考量

- **藥物交互作用**：已查得 7 筆交互作用紀錄，其中 6 筆為中度（Moderate）等級，皆為其他促進生殖功能或 GnRH 類藥物：
  - Gonadorelin
  - 人類絨毛膜促性腺素 (Chorionic Gonadotropin)
  - Menotropins
  - Triptorelin
  - Follitropin
  - Urofollitropin
  
  另有 1 筆為藥理資料，指出作用標的為 GnRH₁ 受體，並非藥物間交互作用。

其餘警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 機轉上，GnRH 拮抗作用與多毛症（尤其是先天性或結構性類型）缺乏合理連結。

**若要推進需要：**
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩選
- 補充 Ganirelix 的詳細作用機轉資料（如 DrugBank）
- 釐清目標族群，區分多毛症 (hypertrichosis) 與男性型多毛 (hirsutism)，後者與荷爾蒙較相關
- 進行系統性文獻檢索，確認是否有任何前臨床或病例報告支持
- 評估給藥途徑的相容性（目前為注射劑，需確認是否適合長期使用於皮膚或毛髮相關適應症）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

