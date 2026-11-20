---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 2
monitor_inn: "HYDROXOCOBALAMIN"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding"]
last_modified_at: 2026-10-28
description: "Hydroxocobalamin：預測新適應症為無出血的食道靜脈曲張（證據等級 L5）。原適應症：知識圖譜中記錄的關聯：維生素 B12 缺乏、氰化物中毒、惡性貧血"
---

# Hydroxocobalamin
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

## Hydroxocobalamin：從維生素 B12 缺乏到無出血的食道靜脈曲張
{: .text-alpha }

## 一句話總結

Hydroxocobalamin（羥鈷胺素）是維生素 B12 的一種形式，知識圖譜中記錄的用途包括維生素 B12 缺乏、氰化物中毒與惡性貧血。
TxGNN 模型預測它可能對**無出血的食道靜脈曲張 (Esophageal Varices without Bleeding)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯：維生素 B12 缺乏、氰化物中毒、惡性貧血（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 無出血的食道靜脈曲張 |
| TxGNN 預測分數 | 0.9923 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Hydroxocobalamin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「氰化物是一種劇毒毒物。若未能迅速且充分治療，暴露於高劑量氰化物可因細胞色素氧化酶受到抑制而導致細胞呼吸停止，於數分鐘內造成死亡。[…] 每個 hydroxocobalamin 分子可藉由以一個氰離子取代與三價鈷離子相連的羥基配位基而結合該氰離子，形成 cyanocobalamin，隨後經由尿液排出。」英文原文："Cyanide is an extremely toxic poison. In the absence of rapid and adequate treatment, exposure to a high dose of cyanide can result in death within minutes due to the inhibition of cytochrome oxidase resulting in arrest of cellular respiration. […] Each hydroxocobalamin molecule can bind one cyanide ion by substituting it for the hydroxo ligand linked to the trivalent cobalt ion, to form cyanocobalamin, which is then excreted in the urine."（[DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b)，版本日期 2023-04-27；查閱日期 2026-11-19）。已知 hydroxocobalamin 是維生素 B12 的一種形式，用於 B12 缺乏，也用於氰化物解毒（鈷中心可與氰化物結合）。

與食道靜脈曲張之間**沒有已確立的機轉連結**。一個純屬推測的方向是：hydroxocobalamin 可能清除一氧化氮（NO），進而影響 NO 介導的內臟血管擴張與門脈高壓（靜脈曲張形成的主要驅動因素）。這個假說沒有本報告所編整資料的支持。

此外，同一藥物對「食道靜脈曲張伴出血」的預測分數完全相同（0.9923）。此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62101 | CYANOKIT POWDER FOR SOLUTION FOR INFUSION 5G | 未載明 | 未載明 |
| HK-18055 | HYCOBAL INJ 5MG/2ML | 未載明 | 未載明 |
| HK-18525 | HEPATOSWISS FOR IV INFUSION INJ | 未載明 | 未載明 |
| HK-18057 | HEPATOSWISS IM INJ | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單文字）：高血壓相關疾患（hypertensive disorder、hypertension）。
- **藥物交互作用**：共查詢到 32 筆交互作用，以下為資料中標示的主要項目：
  - 中度：三氧化二砷（Arsenic trioxide）、氯黴素（Chloramphenicol）、碘-131、碘-123
  - 等級未明：奧美拉唑、蘭索拉唑、辛伐他汀、洛哌丁胺、潑尼松龍、雷尼替丁、阿斯匹靈、布地奈德、葉酸、纈沙坦、雷米普利、勞拉西泮、西酞普蘭、乙醯胺酚、米氮平、左旋甲狀腺素等

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有任何臨床試驗或文獻直接研究此疾病，證據等級為 L5，且機轉連結屬推測。
- 食道靜脈曲張已有成熟的標準治療，新候選藥物需要有力證據才具考量價值。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並驗證 NO 清除與門脈高壓之間的假說
- 進行前臨床或動物模型研究，評估對門脈壓力的影響
- 取得香港仿單的警語與禁忌症（並確認核准適應症文字），完成安全性篩選
- 評估給藥途徑的適用性（目前路徑相容性資料尚待補充）
- 考量知識圖譜記錄的高血壓禁忌關聯，以及與現行門脈高壓用藥的交互作用

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

