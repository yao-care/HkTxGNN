---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
monitor_inn: "ABACAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Abacavir：預測新適應症為貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome)（證據等級 L5）。香港藥劑製品註冊：10 張（有效 10 張）"
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Abacavir：核苷類逆轉錄酶抑制劑 → 貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## 一句話總結

Abacavir 是一種核苷類逆轉錄酶抑制劑（NRTI），已有多項香港有效許可證。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome)** 有效，
目前**無臨床試驗**，僅有 **1 篇**體外前臨床文獻，且為多藥合併的間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome) |
| TxGNN 預測分數 | 0.9979 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 10 張／共 10 張） |
| 許可證數 | 10 張（有效 10 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 abacavir and lamivudine（含 Abacavir 的複方） 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「阿巴卡韋與拉米夫定為一種抗反轉錄病毒藥物，具有對抗HIV-1的活性。」英文原文："Abacavir and lamivudine is an antiretroviral agent with activity against HIV-1."（[DailyMed: abacavir and lamivudine prescribing information, Laurus Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12e80eb-906c-4932-bb03-b4060ba1d31c)，版本日期 2026-09-18；查閱日期 2026-11-19）。依一般藥理知識，abacavir 在細胞內被磷酸化為 carbovir triphosphate，與 dGTP 競爭並終止病毒 DNA 鏈延長。貓免疫缺乏病毒 (FIV) 同屬慢病毒，同樣依賴逆轉錄酶，因此機轉上有可能適用。

FIV 在分子與臨床層面與人類 HIV 相似，常被作為 HIV 的動物模型。不過，現有唯一文獻（PMID 11684314，2002 年）評估的是 zidovudine、lamivudine 與 abacavir 三藥合併在體外抑制 FIV 複製的效果，無法分離出 abacavir 單獨的貢獻。

TxGNN 的高分很可能反映它與人類 HIV 用藥的相似性，而非針對 FIV 的直接證據。FIV 是獸醫領域疾病，沒有人類臨床開發路徑，對人類藥物再利用的意義有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | 體外／動物模型研究 | Antiviral Research | 評估 zidovudine、lamivudine、abacavir 合併療法抑制 FIV 體外複製，屬多藥合併的間接證據 |

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-63701 | ZIAGEN TABLETS 300MG | 單一成分 | GLAXOSMITHKLINE LIMITED | 有效 |
| HK-46236 | ZIAGEN ORAL SOLUTION 20MG/ML | 單一成分 | GLAXOSMITHKLINE LIMITED | 有效 |
| HK-65647 | ABACAVIR TABLETS 300MG | 單一成分 | I & C (HONG KONG) LIMITED | 有效 |
| HK-65610 | ABACAVIR TABLETS USP 300MG | 單一成分 | VIATRIS HEALTHCARE HONG KONG LIMITED | 有效 |
| HK-65625 | ABACAVIR/LAMIVUDINE SANDOZ TABLETS 600MG/300MG | 複方 | SANDOZ HONG KONG LIMITED | 有效 |

上表列出其中 5 張（共 10 張）。

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：本報告彙整資料共記錄 93 項交互作用，其中分級為中度者包括 Naltrexone、Orlistat；其餘如 Metformin、Morphine、Omeprazole、Prednisone、Vancomycin 等分級為未知。
- 一般已知的 abacavir 安全議題包括 HLA-B*57:01 相關過敏反應與心血管風險訊號，使用前需評估。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前無任何臨床試驗，唯一文獻為多藥合併的體外研究，證據不足以直接支持 abacavir 用於此疾病，故證據等級為 L5。
- FIV 為貓的獸醫疾病，沒有人類臨床開發路徑，對香港人用藥物再利用的價值有限。

**若要推進需要：**
- 單獨評估 abacavir 對 FIV 的體外或動物實驗數據
- 確認是否有獸醫用藥的開發需求與法規路徑
- 補充詳細的作用機轉資料
- 取得原廠仿單中的警語與禁忌症資訊

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: abacavir and lamivudine prescribing information, Laurus Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12e80eb-906c-4932-bb03-b4060ba1d31c) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

