---
layout: default
title: Berberine
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Berberine：從傳統草藥到嚴重型子癇前症

## 一句話總結

Berberine 是源自黃連、黃柏等植物的異喹啉生物鹼，傳統上用於消炎、抗菌，目前在香港無正式核准藥品適應症。
TxGNN 模型預測它最有可能對**嚴重型子癇前症 (Severe Pre-eclampsia)** 有效（預測分數 99.83%）。
本特定適應症目前無直接臨床試驗或文獻支持，但高度相關的適應症「妊娠毒血症 (Toxemia of Pregnancy)」已有 **2 篇機轉文獻**提供間接佐證。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式核准適應症（傳統草藥成分） |
| 預測新適應症 | 嚴重型子癇前症 (Severe Pre-eclampsia) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Berberine 是一種異喹啉生物鹼，廣泛存在於傳統中藥材（黃連、黃柏、三顆針），具抗炎、抗氧化、代謝調節等多元藥理活性。其在分子層面已知可活化 AMPK 通路、抑制 NF-κB 訊號、調控巨噬細胞極化。

子癇前症的核心病理機轉為全身性炎症、血管內皮功能障礙與氧化壓力的交互惡化。Berberine 透過 AMPK 活化改善代謝壓力、抑制 NF-κB 降低 IL-6 與 TNF-α 等促炎細胞激素，理論上可直接干預子癇前症的上游病理通路。相關適應症「妊娠毒血症」下的 2026 年最新文獻（PMID 41671580）在 LPS 誘導子癇前症小鼠模型中直接驗證 Berberine 可調控 M1/M2 巨噬細胞極化與 Th1/Th2 免疫平衡，為本預測提供動物模型層級的佐證。

值得注意的是，TxGNN 模型在前 10 名預測中將 4 個子癇前症相關疾病（嚴重型、輕度型、preeclampsia/eclampsia、toxemia of pregnancy）一致納入，顯示預測具高度內部一致性，並非孤立的雜訊訊號；然而現有直接針對「嚴重型」此一特定定義的臨床前或臨床數據仍然缺乏，需謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

> **說明**：資料庫查詢雖發現一個與 Berberine 相關的試驗（NCT01116167，660 人 PCOS 不孕症研究），但其適應症為多囊卵巢症候群，與嚴重型子癇前症無直接關聯，相關性評級為 C 級，不計入本適應症證據庫。

---

## 文獻證據

本適應症（嚴重型子癇前症）目前無直接掛載文獻。以下為來自高度相關適應症「妊娠毒血症 (Toxemia of Pregnancy)」的支持文獻，機轉與本適應症高度重疊，建議合併評估：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [41671580](https://pubmed.ncbi.nlm.nih.gov/41671580/) | 2026 | 動物／機轉研究 | British Journal of Pharmacology | Berberine 於 LPS 誘導子癇前症小鼠模型中，透過調控 M1/M2 巨噬細胞極化與 Th1/Th2 細胞激素平衡，顯著改善子癇前症相關症狀 |
| [38166707](https://pubmed.ncbi.nlm.nih.gov/38166707/) | 2024 | 回顧／機轉研究 | BMC Pregnancy and Childbirth | 系統性梳理子癇前症自噬相關生物標記與藥物篩選靶點，間接支持 Berberine 可能作用的調控節點 |

**補充說明**：單核球白血病（Rank 3）適應症下另有 2 篇體外細胞株研究（PMID [28656088](https://pubmed.ncbi.nlm.nih.gov/28656088/)、[41715293](https://pubmed.ncbi.nlm.nih.gov/41715293/)）驗證 Berberine 對 THP-1 細胞的毒殺效果，反映 Berberine 的廣泛生物活性，但與子癇前症無直接關聯。

---

## 香港上市資訊

Berberine 在香港目前無正式藥品許可證，未以藥品形式上市，許可證數為 0。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 嚴重型子癇前症為高風險妊娠急症，現有證據等級僅 L5（純模型預測），尚無針對此特定適應症的直接臨床前或人體研究，在妊娠期用藥的風險效益比尚未建立。
- 相關動物模型數據（PMID 41671580）提供初步機轉支持，但僅適用於廣義「子癇前症」，距臨床轉譯仍有顯著距離。

**若要推進需要：**
- 針對嚴重型子癇前症的專屬臨床前研究（如 sFlt-1 過表現或 LPS 誘導動物模型）
- Berberine 在妊娠期的安全性資料與藥動學研究（尤其胎盤通透性評估）
- 詳細 MOA 資料，確認 AMPK／NF-κB 通路在子癇前症病理中的特異性貢獻
- 香港無上市前提下的法規路徑評估（新適應症申請策略）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

