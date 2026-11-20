---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 7
monitor_inn: "acetylsalicylic acid"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "trigeminal autonomic cephalalgia", "thrombophilia"]
last_modified_at: 2026-11-20
description: "Acetylsalicylic Acid：預測新適應症為萎縮性蚓狀皮膚病 (atrophoderma vermiculata)（證據等級 L5）。香港藥劑製品註冊：14 張（有效 14 張）"
---

# Acetylsalicylic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Acetylsalicylic acid：抗血小板／環氧合酶抑制劑 → 萎縮性蚓狀皮膚病 (atrophoderma vermiculata)
{: .text-alpha }

## 一句話總結

Acetylsalicylic acid（阿斯匹靈）是一種廣泛使用的環氧合酶抑制型藥物，香港已有多張單一成分許可證上市。
TxGNN 模型預測它可能對**萎縮性蚓狀皮膚病 (atrophoderma vermiculata)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 萎縮性蚓狀皮膚病 (atrophoderma vermiculata) |
| TxGNN 預測分數 | 0.9959 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 14 張／共 14 張） |
| 許可證數 | 14 張（有效 14 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 aspirin and extended - release dipyridamole（含 Acetylsalicylic Acid 的複方） 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Aspirin Aspirin 透過不可逆地抑制血小板環氧合酶而抑制血小板凝集，從而抑制血栓素 A 2 的生成；血栓素 A 2 是強效的血小板凝集及血管收縮誘導物。」英文原文："Aspirin Aspirin inhibits platelet aggregation by irreversible inhibition of platelet cyclooxygenase and thus inhibits the generation of thromboxane A 2, a powerful inducer of platelet aggregation and vasoconstriction."（[DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1)，版本日期 2026-08-19；查閱日期 2026-11-19）。阿斯匹靈一般已知透過抑制環氧合酶來減少血小板聚集與前列腺素合成，具抗血小板與抗發炎作用。

萎縮性蚓狀皮膚病是一種好發於臉頰的毛囊性萎縮性皮膚疾病。就目前整理的資料而言，找不到能把阿斯匹靈的抗血小板或抗發炎作用與此疾病連結起來的合理機轉。

因此，這個高分預測目前只能視為模型的統計結果，缺乏可辨識的機轉依據，也沒有任何研究佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 14 張有效的單一成分許可證，皆為上市狀態，目前無已註銷者。以下列出 5 張主要許可證，許可證資料中未記載核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48244 | PROPIRIN ENTERIC COATED TAB 100MG | 未記載 | 未記載 |
| HK-68481 | CASPRIN GASTRO-RESISTANT CAPSULES 100MG | 未記載 | 未記載 |
| HK-65427 | SAMJIN ASPIRIN ENTERIC-COATED TABLETS 100MG | 未記載 | 未記載 |
| HK-62059 | ASP TABLETS 100MG | 未記載 | 未記載 |
| HK-59150 | ASCOT 81 ENTERIC-COATED TAB 81MG | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：本次整理的資料共記錄 657 項已知藥物交互作用。部分代表性例子：
  - 嚴重（Major）：Acalabrutinib、Acetazolamide、Ketorolac、Ibuprofen、Fondaparinux、Trastuzumab emtansine
  - 中度（Moderate）：Abciximab、Nifedipine、Hydrocortisone、Ethanol、Alendronic acid、Fluvoxamine、Fosinopril
  - 輕微（Minor）：Acebutolol、Caffeine、Rabeprazole、Fosphenytoin、Furosemide

  整體而言，與其他抗凝血藥、抗血小板藥或非類固醇抗發炎藥併用時，出血風險需特別留意。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
此預測沒有任何臨床試驗或文獻支持，也找不到合理的作用機轉，僅憑模型分數不足以推進。

**若要推進需要：**
- 取得阿斯匹靈的詳細作用機轉資料，並評估與萎縮性蚓狀皮膚病病理的關聯
- 進行文獻與病例回顧，確認是否有任何皮膚科使用經驗
- 取得香港仿單的警語與禁忌症資料，以進行安全性篩選

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

