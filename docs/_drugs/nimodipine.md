---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 620
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "NIMODIPINE"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
description: "Nimodipine：預測新適應症為同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia)（證據等級 L5）。香港藥劑製品註冊：4 張（有效 4 張）"
---

# Nimodipine
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

## Nimodipine: 同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia)
{: .text-alpha }

## 一句話總結

Nimodipine 是一種二氫吡啶類鈣離子通道阻斷劑，原本用於蛛網膜下腔出血（動脈瘤性）的治療。
TxGNN 模型預測它可能對**同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 同合子家族性高膽固醇血症 (homozygous familial hypercholesterolemia) |
| TxGNN 預測分數 | 0.9929 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Nimodipine 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Nimodipine為一種dihydropyridine類鈣離子通道阻斷劑。平滑肌細胞的收縮過程有賴於鈣離子，鈣離子在去極化期間以緩慢離子跨膜電流的形式進入這些細胞。」英文原文："Nimodipine is a dihydropyridine calcium channel blocker. The contractile processes of smooth muscle cells are dependent upon calcium ions, which enter these cells during depolarization as slow ionic transmembrane currents."（[DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10)，版本日期 2024-08-30；查閱日期 2026-11-19）。根據已知資訊，Nimodipine 是對腦血管具選擇性的二氫吡啶類 L 型鈣離子通道阻斷劑，其在蛛網膜下腔出血中的角色已被確立，但機轉上是否適用於同合子家族性高膽固醇血症，尚無法由現有資料驗證。

同合子家族性高膽固醇血症主要由 LDL 受體途徑缺陷（LDLR、APOB、PCSK9、LDLRAP1）造成。Nimodipine 與此途徑沒有已知的直接關聯。唯一可能的連結是間接的，例如鈣離子通道阻斷劑對血管平滑肌或動脈粥樣硬化進展的影響，但這無法改善根本的 LDL 清除缺陷。

換言之，0.993 的高分只是計算預測，沒有任何證據支持降脂療效。

另一個模型預測的適應症為**腎因性抗利尿激素不適當分泌症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis)**（分數 0.9905）。此症由 AVPR2 功能增強突變造成，Nimodipine 並不作用於 V2 受體或其 cAMP／水通道蛋白-2 訊號，任何關聯都屬推測，同樣沒有臨床試驗或文獻支持，證據等級為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-28973 | NIMOTOP INFUSION SOLUTION 10MG/50ML | 單一成分 | ZUELLIG PHARMA LIMITED | 有效 |
| HK-64672 | NIMODIPINE SOLUTION FOR INFUSION 0.2MG/ML | 單一成分 | HIND WING CO LTD | 有效 |
| HK-28974 | NIMOTOP TAB 30MG | 單一成分 | ZUELLIG PHARMA LIMITED | 有效 |
| HK-65564 | NORTOLAN TABLETS 30MG | 單一成分 | HONG KONG MEDICAL SUPPLIES LTD | 有效 |

<!-- licenses:end -->

## 安全性考量

- **知識圖譜標示的相關疾病禁忌**：肝病、膽囊疾病、低血壓性疾患（此為模型知識圖譜資料，非仿單原文）。
- **藥物交互作用**：已查得 100 筆交互作用，以下為部分範例。
  - 重度 (Major)：Clarithromycin、Dolasetron
  - 中度 (Moderate)：Bupropion、Aprepitant、Morphine、Acetylsalicylic acid、Cimetidine、Miconazole、Magnesium sulfate，以及 Canagliflozin、Dapagliflozin、Empagliflozin 等 SGLT2 抑制劑

仿單中的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症都僅有模型分數，沒有臨床試驗或文獻佐證（L5）。
- 作用機轉資料缺漏，且預測疾病的致病機轉（LDL 受體途徑缺陷）與 Nimodipine 的藥理作用無明確關聯。

**若要推進需要：**
- 補齊 Nimodipine 的作用機轉（MOA）資料。
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選。
- 系統性檢索前臨床與臨床文獻，確認是否有鈣離子通道阻斷劑與家族性高膽固醇血症的相關證據。
- 在取得任何支持證據之前，不建議投入進一步開發資源。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

