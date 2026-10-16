---
layout: default
title: Thyrotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 875
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Thyrotropin Alfa：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：目前許可證資料未載明核准適應症"
monitor_inn: "Thyrotropin alfa"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Raynaud disease", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "kyphoscoliotic heart disease", "postural orthostatic tachycardia syndrome", "hyperthyroidism"]
---

# Thyrotropin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Thyrotropin alfa：從甲狀腺癌診斷輔助到偏頭痛（僅為模型預測）

## 一句話總結

Thyrotropin alfa 是重組人類促甲狀腺素（TSH），在香港以 THYROGEN 品名上市。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料未載明核准適應症 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Thyrotropin alfa 是重組 TSH，作用於甲狀腺組織的 TSH 受體，促進甲狀腺細胞活性與甲狀腺激素的產生。

目前沒有建立起來的機轉連結可以說明它與偏頭痛的關係。高分很可能來自知識圖譜中的網路鄰近性或共享基因/路徑，而不是真正的治療證據。若要把兩者連起來（例如透過甲狀腺荷爾蒙狀態影響偏頭痛），目前也只是推測。

其他排名靠前的預測（偏頭痛亞型、雷諾氏症、肺動脈高壓、姿勢性心搏過速症候群等）同樣沒有試驗或文獻支持，多半反映疾病層級的關聯或圖譜冗餘。其中**甲狀腺機能亢進**在機轉上反而是禁忌，因為 TSH 受體刺激會增加甲狀腺激素分泌，可能惡化病情。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-54932 | THYROGEN FOR INJ 1.1MG | 未載明 | 未載明（製造商：SANOFI HONG KONG LIMITED） |

---

## 安全性考量

- **藥物交互作用**：已查得 45 筆交互作用紀錄，以下列出部分（皆為中度）：
  - 降血糖藥物類：Acarbose、Metformin、Glimepiride、Glipizide、Glyburide、Chlorpropamide、Acetohexamide
  - DPP-4 抑制劑與 SGLT2 抑制劑：Alogliptin、Saxagliptin、Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin
  - GLP-1 類藥物：Albiglutide、Dulaglutide、Exenatide、Semaglutide
  - 胰島素類：Insulin human、Insulin aspart

  整體看來，併用糖尿病藥物時需留意血糖控制的變化。

- **預測適應症的安全疑慮**：對於甲狀腺機能亢進等預測項目，TSH 刺激在機轉上可能使病情惡化。姿勢性心搏過速症候群也有類似疑慮，外源性 TSH 可能增加甲狀腺激素輸出而加重心搏過速。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都僅有模型分數，沒有臨床試驗或文獻，證據等級為 L5。
- 缺乏可辨識的機轉連結，且部分預測（如甲狀腺機能亢進）在機轉上有安全疑慮，目前不建議投入開發。

**若要推進需要：**
- 取得 Thyrotropin alfa 的詳細作用機轉資料（MOA）
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 以文獻回顧確認 TSH 或甲狀腺功能與偏頭痛是否有可驗證的生物學關聯
- 如找到合理假說，先進行前臨床或小規模探索性研究，再重新評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

