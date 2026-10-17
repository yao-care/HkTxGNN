---
layout: default
title: Etofenamate
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Etofenamate：預測新適應症為脊椎關節病變易感性 (spondyloarthropathy, susceptibility to)（證據等級 L5）。原適應症：骨關節炎、關節病變"
monitor_inn: "ETOFENAMATE"
predicted_indications: ["ankylosing spondylitis", "rheumatoid vasculitis", "hypermobility of coccyx", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Etofenamate
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

# Etofenamate：從骨關節炎到脊椎關節病變易感性

## 一句話總結

Etofenamate 是一種外用非類固醇消炎藥（NSAID，為 flufenamic acid 的酯類衍生物），原本用於骨關節炎與關節病變。
TxGNN 模型預測它可能對**脊椎關節病變易感性 (spondyloarthropathy, susceptibility to)** 有效，
但目前**沒有臨床試驗與文獻**直接支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨關節炎、關節病變（依知識圖譜適應症資料；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 脊椎關節病變易感性 (spondyloarthropathy, susceptibility to) |
| TxGNN 預測分數 | 99.9996% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Etofenamate 是外用 NSAID，一般認為其透過抑制環氧合酶（COX）、減少前列腺素介導的發炎反應而發揮作用。這在發炎性脊椎關節病變中機轉上有一定合理性。

不過，此預測對象是一個「遺傳易感性」分類，並非可直接治療的臨床疾病，因此高分更可能反映知識圖譜中肌肉骨骼與關節病變之間的關聯，而非真正的療效訊號。

若改看同一藥物的其他預測，**僵直性脊椎炎 (ankylosing spondylitis)**（預測分數 99.998%）在臨床上較有意義：NSAID 是其一線症狀治療，但外用劑型難以作用於軸心（脊椎）病變，實用性有限。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（脊椎關節病變易感性）目前無相關文獻。

與次要預測「僵直性脊椎炎」相關的間接文獻如下：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/) | 2001 | 藥物動力學研究 | Arzneimittel-Forschung | 11 位下背痛與 13 位膝關節滑膜炎患者，以離子導入法連續 5 天給予 Etofenamate 凝膠，於血清與滑液中測得藥物濃度，顯示可送達關節組織；未評估對僵直性脊椎炎的療效或安全性 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53359 | FLOGOPROFEN GEL 5% | 凝膠 | 資料未載明 |
| HK-52785 | FLOGOPROFEN SOLUTION 5% | 溶液 | 資料未載明 |
| HK-55383 | ORDOFEN GEL 10% | 凝膠 | 資料未載明 |
| HK-40437 | NISOLON GEL 50MG/G | 凝膠 | 資料未載明 |
| HK-41266 | SULKY GEL 5% | 凝膠 | 資料未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測對象是遺傳易感性分類而非可治療疾病，且無任何臨床試驗或文獻支持，證據等級僅 L5。
- 外用劑型難以作用於軸心脊椎病變；其他預測（類風濕血管炎、尾骨過度活動、肢中型發育不良）機轉合理性更低。

**若要推進需要：**
- 釐清目標族群，改以臨床上可治療的疾病（如僵直性脊椎炎或附著點炎相關症狀）作為評估對象
- 補充詳細的作用機轉資料
- 取得原廠仿單的警語與禁忌資料，完成安全性篩選
- 評估外用劑型與目標病灶的給藥途徑相容性
- 針對局部症狀緩解設計小型探索性臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

