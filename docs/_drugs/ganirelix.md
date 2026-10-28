---
layout: default
title: Ganirelix
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
monitor_inn: "GANIRELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial male-limited precocious puberty", "persistent fetal circulation syndrome", "aromatase excess syndrome", "centra precocious puberty 1", "familial isolated trichomegaly"]
last_modified_at: 2026-10-23
description: "Ganirelix：預測新適應症為多毛症 (Hypertrichosis)（證據等級 L5）。原適應症：香港許可證未載明核准適應症文字"
---

# Ganirelix
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Ganirelix：從生殖輔助治療到毛髮過多症
{: .text-alpha }

## 一句話總結

Ganirelix 是一種 GnRH 受體拮抗劑，臨床上用於在不孕症治療的卵巢刺激過程中預防提早排卵。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持此預測，僅屬模型推論，機轉上的關聯也很薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症文字（藥理資料顯示臨床用途為預防卵巢刺激期間提早排卵） |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Ganirelix 是 GnRH 受體（GNRHR）拮抗劑，會抑制促黃體生成素（LH）與促卵泡激素（FSH）的分泌，間接降低性腺的性荷爾蒙生成。目前缺乏 DrugBank 的詳細作用機轉資料，以上說明來自藥理資料庫的靶點資訊。

毛髮過多症並非主要由促性腺激素驅動的疾病（與依賴雄性素的多毛症 hirsutism 不同），因此機轉上的連結薄弱且屬推測。如此高的預測分數（0.9998）來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，也無臨床或文獻佐證。

整體而言，本預測應視為假說，不足以支持進一步開發。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49750 | ORGALUTRAN INJ 0.25MG/0.5ML | 注射劑 | 許可證資料未載明 |

## 其他排名較前的預測（供參考）

以下預測同樣僅為模型推論，皆無臨床試驗或文獻支持（證據等級均為 L5）：

| 排名 | 預測疾病 | TxGNN 分數 | 機轉評估 | 建議 |
|------|---------|-----------|---------|------|
| 2 | Ambras 型先天性全身多毛症 | 0.9998 | 屬基因體重組造成的發育缺陷，與 GnRH 拮抗無關 | Hold |
| 3 | 伴有牙齒／牙周異常的畸形症候群 | 0.9997 | 發育或遺傳成因，無可信機轉 | Hold |
| 4 | 以 Dandy-Walker 畸形為主要特徵的症候群 | 0.9997 | 先天結構異常，無法以 GnRH 拮抗逆轉 | Hold |
| 5 | 孤立性遺傳毛幹異常 | 0.9997 | 源自結構基因缺陷，與促性腺激素無關 | Hold |
| 6 | 家族性男性限定性性早熟 | 0.9985 | 由 LHCGR 活化突變驅動，不依賴促性腺激素，GnRH 拮抗預期無效 | 研究問題 |
| 7 | 持續性胎兒循環症候群 | 0.9980 | 新生兒肺血管疾病，無機轉關聯 | Hold |
| 8 | 芳香環酶過量症候群 | 0.9980 | 周邊組織芳香環化仍會持續，機轉僅部分合理 | 研究問題 |
| 9 | 中樞性性早熟 1 型 | 0.9975 | 抑制 GnRH 軸為既有治療原則，機轉上最為合理；但短效劑型是實務障礙 | 研究問題 |
| 10 | 家族性孤立性睫毛過長 | 0.9975 | 遺傳性睫毛生長異常，無可信機轉 | Hold |

在這些預測中，中樞性性早熟在生物學上最為連貫，若要探索，可優先考慮此方向。

## 安全性考量

- **藥物交互作用**：共查得 7 筆資料，其中 6 筆為中度等級，涉及其他促性腺激素或 GnRH 相關藥物：
  - Gonadorelin
  - 人類絨毛膜促性腺激素（Chorionic Gonadotropin）
  - Menotropins
  - Triptorelin
  - Follitropin
  - Urofollitropin

  另有 1 筆為藥理資料庫列出的靶點資訊（GnRH₁ 受體），並非藥物交互作用。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 針對毛髮過多症沒有任何臨床試驗或文獻，機轉上關聯薄弱；高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，證據等級為 L5。
- 前十名預測中多數缺乏合理的生物學基礎，僅中樞性性早熟等少數方向值得作為研究問題探討。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料
- 補充詳細的作用機轉資料
- 針對多毛症或中樞性性早熟進行系統性文獻檢索，確認是否有直接研究
- 若選擇中樞性性早熟方向，需評估短效劑型的可行性與兒童使用安全性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

