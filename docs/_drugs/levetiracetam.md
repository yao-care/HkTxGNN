---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 522
evidence_level: L5
indication_count: 1
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-10-23
description: "Levetiracetam：預測新適應症為β-酮硫解酶缺乏症（證據等級 L5）。原適應症：局部癲癇"
---

# Levetiracetam
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

## Levetiracetam：從局部癲癇到 β-酮硫解酶缺乏症
{: .text-alpha }

## 一句話總結

Levetiracetam 是抗癲癇藥物，知識圖譜中記錄的原適應症為局部癲癇（partial epilepsy）。
TxGNN 模型預測它可能對 **β-酮硫解酶缺乏症（beta-ketothiolase deficiency）** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部癲癇（知識圖譜中記錄的關係；本次整理的香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | β-酮硫解酶缺乏症 |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為 levetiracetam 會結合突觸囊泡蛋白 SV2A，調節神經傳導物質釋放，這是其抗癲癇作用的基礎，但此說法並非來自本次整理的資料。

β-酮硫解酶缺乏症是酮體利用與異白胺酸分解的代謝疾病，主要表現為酮酸中毒危象，病因是 ACAT1（T2）酶缺陷。目前沒有資料顯示 levetiracetam 與此酶缺陷或相關代謝路徑有生物學連結。

因此，高分預測僅是計算模型的結果。若有任何益處，也最多限於神經症狀的對症處理，而非改變疾病本身。原適應症與新適應症的相似性評估尚待進行。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

本次整理的資料中，許可證的劑型與核准適應症文字皆為空白。以下為部分主要許可證（清單可能不完整）：

| 許可證號 | 品名 | 核准適應症 |
|---------|------|-----------|
| HK-48231 | KEPPRA TAB 500MG | 資料未載明 |
| HK-48230 | KEPPRA TAB 250MG | 資料未載明 |
| HK-67539 | LECETAM 250 TABLETS 250MG | 資料未載明 |
| HK-66922 | ACCORD LEVETIRACETAM 750 TABLETS 750MG | 資料未載明 |
| HK-65814 | HOSPIRA LEVETIRACETAM CONCENTRATE FOR IV INFUSION 500MG/5ML | 資料未載明 |

品名顯示有錠劑、口服溶液與靜脈輸注濃縮液等型式。

## 安全性考量

- **知識圖譜中記錄的禁忌關係**（非仿單文字）：焦慮症、神經症、輕度抑鬱症、腎臟疾病、肝臟疾病、膽囊疾病、精神病性障礙、類精神分裂症、思覺失調情感性疾患、精神疾患、嗜中性白血球低下、顆粒球缺乏症、白血球低下、全血球低下、失人格感障礙等。
- **藥物交互作用**：共查得 100 筆，以下為其中的中度交互作用：Morphine（含脂質體劑型）、Dronabinol、Metoclopramide、Nabilone、Opium、Sibutramine。其餘多為等級未明，包括 Pantoprazole、Omeprazole、Metformin、Vancomycin 等。這些多與中樞神經抑制或鎮靜疊加有關，但資料未提供機轉細節。

正式警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究此疾病，證據等級為 L5。
- 沒有已知的機轉連結，且此疾病為酶缺陷型代謝病，TxGNN 高分不足以支持推進。

**若要推進需要：**
- 取得 levetiracetam 的作用機轉資料，並評估與 ACAT1／酮體代謝的可能連結
- 前臨床或病例層級證據，說明是否有神經症狀層面的益處
- 取得香港衛生署仿單，確認警語與禁忌症
- 安全性評估，特別是腎功能、血液學及精神症狀方面的風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

