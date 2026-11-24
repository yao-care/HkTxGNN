---
layout: default
title: Prucalopride
parent: 僅模型預測 (L5)
nav_order: 744
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
description: "Prucalopride：預測新適應症為低 α 脂蛋白血症 (hypoalphalipoproteinemia)（證據等級 L5）。香港藥劑製品註冊：1 張（有效 1 張）"
---

# Prucalopride
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

## Prucalopride: 低 α 脂蛋白血症 (hypoalphalipoproteinemia)
{: .text-alpha }

## 一句話總結

Prucalopride 是一種選擇性 5-HT4 受體促效劑，原本用於治療便秘。
TxGNN 模型預測它可能對**低 α 脂蛋白血症 (Hypoalphalipoproteinemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 低 α 脂蛋白血症 (hypoalphalipoproteinemia) |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Prucalopride 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Prucalopride 為一種選擇性血清素第 4 型（5-HT 4 ）受體促效劑，屬胃腸道（GI）促動力藥，可刺激結腸蠕動（高振幅推進性收縮 [HAPCs]），從而增加腸道蠕動。在體外試驗中，於濃度超過 5-HT 4 受體親和力 150 倍或以上時，prucalopride 並未產生經由 5-HT 2A、5-HT 2B、5-HT 3、胃動素（motilin）或 CCK-A 受體所介導的作用。」英文原文："Prucalopride, a selective serotonin type 4 (5-HT 4 ) receptor agonist, is a gastrointestinal (GI) prokinetic agent that stimulates colonic peristalsis (high-amplitude propagating contractions [HAPCs]), which increases bowel motility. Prucalopride was devoid of effects mediated via 5-HT 2A, 5-HT 2B, 5-HT 3, motilin or CCK-A receptors in vitro at concentrations exceeding 5-HT 4 receptor affinity by 150-fold or greater."（[DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b)，版本日期 2025-07-17；查閱日期 2026-11-19）。根據已知資訊，Prucalopride 是選擇性 5-HT4 受體促效劑，作用於腸道蠕動，其在便秘中的角色已為人所知。

然而，5-HT4 促效作用與 HDL 代謝或 ApoA-I 調控之間，並無已知的關聯。這個高分預測來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，也沒有任何試驗或文獻佐證，因此目前無法建立可信的機轉連結。

TxGNN 預測分數高，不代表臨床上合理，建議將此結果視為待驗證的假設，而非可行動的證據。

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
| HK-61189 | RESOLOR TABLETS 1MG | 單一成分 | AMDIPHARM MERCURY (HONG KONG) LIMITED | 有效 |

<!-- licenses:end -->

廠商：AMDIPHARM MERCURY (HONG KONG) LIMITED，狀態為有效（單一成分）。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜，非仿單內容）：潰瘍性結腸炎、發炎性腸道疾病、腸穿孔。
- **藥物交互作用**：共記錄 98 筆，以下為已列出的部分項目。
  - 中度：Aclidinium、Levonorgestrel、Norethisterone、Hyoscyamine、Ethinylestradiol、Atropine、Benzatropine、Biperiden、Glycopyrronium、Clidinium
  - 輕度：Nifedipine、Afatinib、Alpelisib、Amiodarone、Cobicistat、Captopril、Diltiazem、Spironolactone、Carvedilol、Conivaptan

  抗膽鹼類藥物（如 Atropine、Hyoscyamine）與促腸蠕動藥物的作用方向相反，併用時需留意。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（0.9982），但沒有任何臨床試驗或文獻支持，機轉上也找不到合理連結，屬於 L5 等級。
- 其他排名前 10 的預測中，僅「澱粉樣變性 (amyloidosis)」與「原發性澱粉樣變性」有間接線索（針對澱粉樣變性相關腸道動力障礙的症狀緩解），目前僅被列為研究問題，且現有文獻也沒有 Prucalopride 療效的資料。

**若要推進需要：**
- 補齊作用機轉資料，並評估與低 α 脂蛋白血症的生物學關聯
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 進行文獻與試驗的系統性檢索；若仍無證據，建議轉而優先評估澱粉樣變性相關腸道動力障礙這類有間接機轉線索的方向
- 若考慮更多預測適應症，需先釐清 98 筆藥物交互作用在目標族群中的實際影響

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

