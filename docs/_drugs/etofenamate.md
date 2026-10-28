---
layout: default
title: Etofenamate
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 9
monitor_inn: "ETOFENAMATE"
predicted_indications: ["ankylosing spondylitis", "rheumatoid vasculitis", "hypermobility of coccyx", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "pseudoachondroplasia", "myosclerosis", "polyarticular juvenile rheumatoid arthritis", "Kummell disease"]
last_modified_at: 2026-10-28
description: "Etofenamate：預測新適應症為僵直性脊椎炎 (Ankylosing Spondylitis)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯為骨關節炎、骨關節炎易感性、關節病變"
---

# Etofenamate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Etofenamate：從骨關節炎到僵直性脊椎炎
{: .text-alpha }

## 一句話總結

Etofenamate 是外用非類固醇消炎藥（fenamate 類，flufenamic acid 的酯類衍生物），在知識圖譜中記錄的原適應症為骨關節炎與關節病變。
TxGNN 模型預測它可能對**僵直性脊椎炎 (Ankylosing Spondylitis)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇文獻**（藥物動力學研究），且該文獻並未直接研究此疾病，證據僅屬模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯為骨關節炎、骨關節炎易感性、關節病變（香港許可證資料未載明核准適應症） |
| 預測新適應症 | 僵直性脊椎炎 (Ankylosing Spondylitis) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別推論，Etofenamate 屬於外用 NSAID（fenamate 類），推測透過抑制環氧化酶（COX）產生消炎止痛作用。此為依類別的推論，並非已記載的機轉。

NSAID 是僵直性脊椎炎的一線治療，因此在類別層面存在機轉上的合理性。唯一連結的文獻是一項藥物動力學研究，顯示 Etofenamate 經離子導入後可在人體血清與關節滑液中測得，支持其組織穿透能力，但並不能證明對軸性脊椎關節炎的療效。此外，僵直性脊椎炎病灶位於脊椎與薦髂關節，外用劑型能否到達足夠深度仍有疑問。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/) | 2001 | 藥物動力學研究 | Arzneimittel-Forschung | 11 名下背痛與 13 名膝關節滑膜炎患者，連續 5 天以離子導入給予 Etofenamate 凝膠後，於血清及滑液中測得藥物濃度，顯示可穿透至關節組織；未評估僵直性脊椎炎療效 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53359 | FLOGOPROFEN GEL 5% | 凝膠（品名所示） | 資料未載明 |
| HK-52785 | FLOGOPROFEN SOLUTION 5% | 外用溶液（品名所示） | 資料未載明 |
| HK-55383 | ORDOFEN GEL 10% | 凝膠（品名所示） | 資料未載明 |
| HK-40437 | NISOLON GEL 50MG/G | 凝膠（品名所示） | 資料未載明 |
| HK-41266 | SULKY GEL 5% | 凝膠（品名所示） | 資料未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症

其餘預測皆無臨床試驗或文獻，僅為模型預測（L5），建議均為 Hold：

| 排名 | 預測疾病 | TxGNN 分數 | 評語 |
|------|---------|-----------|------|
| 2 | 類風濕性血管炎 | 1.0000 | 需免疫抑制治療，外用 NSAID 不足 |
| 3 | 尾骨過度活動 | 1.0000 | 局部止痛尚屬合理，但無資料支持 |
| 4 | 肢中發育不良（Hunter-Thompson 型） | 1.0000 | 基因性骨骼發育不良，無機轉關聯；此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，並非生物學證據 |
| 5 | 短指（牙）-牙釉質發育不全症候群 | 1.0000 | 無合理 NSAID 機轉 |
| 6 | 假性軟骨發育不全 | 1.0000 | 至多緩解繼發性關節痛 |
| 7 | 肌硬化症 | 1.0000 | 僅有非特異性症狀緩解可能 |
| 8 | 多關節型幼年類風濕性關節炎 | 1.0000 | 類別層面合理，但兒童安全性與劑量未確立 |
| 9 | Kummell 病 | 1.0000 | 以手術或介入治療為主，外用 NSAID 無角色 |

## 結論與下一步

**決策：Hold**

**理由：**
- 僵直性脊椎炎目前僅有模型預測與類別層面的推論，沒有直接研究該疾病的臨床試驗或文獻，證據等級為 L5。
- 唯一文獻為藥物動力學研究，只能說明藥物可進入關節組織；且香港仿單的警語與禁忌資料缺漏，尚無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充作用機轉（MOA）資料（如 DrugBank）
- 評估外用劑型能否到達脊椎與薦髂關節的深度及足夠濃度
- 針對僵直性脊椎炎進行文獻回顧，必要時規劃早期探索性臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

