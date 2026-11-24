---
layout: default
title: Esketamine
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "ESKETAMINE"
predicted_indications: ["agoraphobia", "benign paroxysmal torticollis of infancy"]
description: "Esketamine：預測新適應症為畏曠症 (agoraphobia)（證據等級 L5）。香港藥劑製品註冊：1 張（有效 1 張）"
---

# Esketamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Esketamine: 畏曠症 (agoraphobia)
{: .text-alpha }

## 一句話總結

Esketamine 的原適應症為焦慮症、神經症與輕度慢性憂鬱（情緒低落性疾患）。
TxGNN 模型預測它可能對**畏曠症 (Agoraphobia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 畏曠症 (agoraphobia) |
| TxGNN 預測分數 | 0.9957 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Esketamine 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Esketamine 為消旋 ketamine 的 S-鏡像異構物，是 N -甲基- D -天門冬胺酸（NMDA）受體（一種離子型麩胺酸受體）的非選擇性、非競爭性拮抗劑。Esketamine 發揮其抗憂鬱作用的機轉尚不明。」英文原文："Esketamine, the S-enantiomer of racemic ketamine, is a non-selective, non-competitive antagonist of the N -methyl- D -aspartate (NMDA) receptor, an ionotropic glutamate receptor. The mechanism by which esketamine exerts its antidepressant effect is unknown."（[DailyMed: Spravato (esketamine hydrochloride) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d81a6a79-a74a-44b7-822c-0dfa3036eaed)，版本日期 2026-09-22；查閱日期 2026-11-19）。根據已知資訊，Esketamine 為 NMDA 受體拮抗劑，可增強麩胺酸訊號並促進突觸可塑性。其原適應症與焦慮相關，因此在機轉上可能適用於焦慮譜系疾患。

畏曠症屬於焦慮症，與原適應症在恐懼迴路病理上有重疊，這是模型預測的合理之處。

不過，0.9957 的分數僅為計算預測，並無臨床試驗或文獻佐證。此外，部分患者使用後可能出現解離症狀或焦慮加劇，對恐懼症族群可能是疑慮，且目前沒有針對此族群的安全性資料。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-67010 | SPRAVATO NASAL SPRAY 28MG/DEVICE | 單一成分 | JOHNSON & JOHNSON (HONG KONG) LTD. | 有效 |

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**：血管疾病、動靜脈血管瘤／畸形（來自知識圖譜的藥物－疾病關聯，非仿單內容）。
- **藥物交互作用**：共查得 70 筆，以下為其中的主要項目：
  - **重度（Major）**：Diethylpropion、Phentermine、Fenfluramine、Mazindol、Caffeine
  - **中度（Moderate）**：Morphine、Loperamide、Difenoxin、Diphenoxylate、Dronabinol、Nabilone、Metoclopramide、Scopolamine，以及多種鼻用類固醇與 Ephedrine（鼻用）

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型，沒有臨床試驗或文獻支持（證據等級 L5），且缺乏作用機轉與仿單安全性資料。
- Esketamine 可能引發解離與焦慮，對畏曠症患者的風險與效益尚不明確。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性初篩
- 補充 DrugBank 的作用機轉資料，進行機轉關聯分析
- 系統性檢索畏曠症／恐懼症相關的臨床試驗與文獻
- 評估解離與焦慮加劇風險，以及與重度交互作用藥物（如興奮劑類）併用的管理方式

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Spravato (esketamine hydrochloride) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d81a6a79-a74a-44b7-822c-0dfa3036eaed) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

