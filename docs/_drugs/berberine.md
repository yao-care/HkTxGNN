---
layout: default
title: Berberine
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Berberine：預測新適應症為嚴重子癇前症 (Severe Pre-eclampsia)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Berberine"
predicted_indications: ["severe pre-eclampsia", "mild pre-eclampsia", "monocytic leukemia", "multiple endocrine neoplasia", "preeclampsia/eclampsia", "spermatocytic seminoma", "placental hemangioma", "tubular variant testicular seminoma", "gestational trophoblastic neoplasm", "toxemia of pregnancy"]
---

# Berberine
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

## Berberine：從（原適應症未載明）到嚴重子癇前症
{: .text-alpha }

## 一句話總結

Berberine（小檗鹼，黃連素）在香港已有 3 張單方許可證，但本次整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**嚴重子癇前症 (Severe Pre-eclampsia)** 有效，預測分數很高，但目前**沒有臨床試驗與直接文獻**支持該適應症，僅有一項相關的 2026 年前臨床研究（歸在「妊娠毒血症」項下）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 嚴重子癇前症 (Severe Pre-eclampsia) |
| TxGNN 預測分數 | 0.9983 |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Berberine 是一種異喹啉類生物鹼，為黃連（Coptidis Rhizoma）的主要活性成分，但本報告所用資料並未收錄正式的 MOA，也未載明原適應症，因此無法從原適應症與新適應症的關聯性來推論。

間接線索來自一項 2026 年發表於 British Journal of Pharmacology 的前臨床研究（PMID 41671580）：在 LPS 誘導的子癇前症小鼠模型中，berberine 可能透過調節 M1/M2 巨噬細胞極化及 Th1/Th2 細胞激素平衡來減輕病況。子癇前症以免疫失衡、發炎和腸道菌叢失調為特徵，這個免疫調節機轉在邏輯上與預測相符。

需注意：該研究屬動物模型，且是針對一般子癇前症，並非專門針對「嚴重」型；目前沒有人體試驗。此外，berberine 在孕婦的安全性尚未確立，對這個族群是重大疑慮。

其他排名較前的預測（輕度子癇前症、子癇前症/子癇等）情況相同：僅有模型分數，沒有直接證據。單核球性白血病則有細胞株層級的體外研究，證據等級為 L4。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對「嚴重子癇前症」本身目前無直接文獻。以下為相關疾病（妊娠毒血症）項下的文獻，可作為間接參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41671580](https://pubmed.ncbi.nlm.nih.gov/41671580/) | 2026 | 前臨床研究 | Br J Pharmacol | Berberine 在 LPS 誘導的子癇前症小鼠模型中，透過調節 M1/M2 巨噬細胞極化與 Th1/Th2 平衡減輕病況 |
| [38166707](https://pubmed.ncbi.nlm.nih.gov/38166707/) | 2024 | 生物資訊/回顧 | BMC Pregnancy Childbirth | 探討子癇前症的自噬相關生物標記、免疫微環境與藥物篩選，僅提供背景脈絡 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60643 | KL HUANG LIAN SU TAB 100 MG | 未載明 | 未載明 |
| HK-60066 | HUANG LIAN SU TAB 100MG | 未載明 | 未載明 |
| HK-53189 | TESMIN ACE CAP | 未載明 | 未載明 |

---

## 安全性考量

- **孕婦安全性**：berberine 在妊娠期的安全性尚未確立，而預測的新適應症（子癇前症）正是孕婦族群，必須在任何臨床推進前優先釐清胎兒安全性。

其他安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高（0.9983），但對嚴重子癇前症沒有臨床試驗或直接文獻，僅有一項動物模型的間接支持。
- 目標族群為孕婦，而 berberine 的妊娠安全性未明，風險與證據不成比例。

**若要推進需要：**
- 取得香港衛生署仿單，釐清原核准適應症、警語與禁忌症
- 補齊詳細的作用機轉資料（MOA）
- 進行妊娠期與胎兒安全性評估（含動物生殖毒性資料）
- 在更多動物模型中驗證 berberine 對子癇前症的療效，並確認是否適用於嚴重型
- 評估劑量與暴露量是否能在安全範圍內達到有效濃度，再考慮早期臨床研究設計
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

