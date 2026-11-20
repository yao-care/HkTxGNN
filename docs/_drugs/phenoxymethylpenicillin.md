---
layout: default
title: Phenoxymethylpenicillin
parent: 僅模型預測 (L5)
nav_order: 690
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "PHENOXYMETHYLPENICILLIN"
predicted_indications: ["epiglottitis", "laryngitis"]
description: "Phenoxymethylpenicillin：預測新適應症為會厭炎 (epiglottitis)（證據等級 L5）。香港藥劑製品註冊：1 張（有效 1 張）"
---

# Phenoxymethylpenicillin
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

## Phenoxymethylpenicillin: 會厭炎 (epiglottitis)
{: .text-alpha }

## 一句話總結

Phenoxymethylpenicillin（青黴素 V）是口服窄效 β-內醯胺類抗生素，原本用於咽炎、中耳炎、鏈球菌感染、呼吸道感染等。
TxGNN 模型預測它可能對**會厭炎 (Epiglottitis)** 有效，但目前**沒有臨床試驗與文獻**支持，僅有模型預測（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 會厭炎 (epiglottitis) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Phenoxymethylpenicillin 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「Penicillin V 於對 penicillin 敏感的微生物處於活躍增殖階段時發揮殺菌作用。其作用是透過抑制細胞壁黏肽的生物合成。本藥對產生 penicillinase 的細菌不具活性，此類細菌包括許多葡萄球菌菌株。」英文原文："Penicillin V exerts a bactericidal action against penicillin-sensitive microorganisms during the stage of active multiplication. It acts through the inhibition of biosynthesis of cell-wall mucopeptide. It is not active against the penicillinase-producing bacteria, which include many strains of staphylococci."（[DailyMed: penicillin v potassium prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ceddc406-4a17-471f-917e-63b4b03779ea)，版本日期 2026-11-12；查閱日期 2026-11-19）。根據已知資訊，青黴素 V 屬於 β-內醯胺類抗生素，透過抑制細菌細胞壁合成，對敏感的革蘭氏陽性菌（如鏈球菌）有活性。

會厭炎是上呼吸道的細菌感染，過去以 b 型流感嗜血桿菌 (H. influenzae type b) 為主，較少由鏈球菌和金黃色葡萄球菌引起。因此對鏈球菌引起的病例，機轉上有合理性，這也可能是模型給出高分的原因：該藥已有咽炎與呼吸道感染的適應症。

但這個預測有明顯限制：
- 青黴素 V 對會產生 β-內醯胺酶的 H. influenzae 無效。
- 會厭炎屬急性氣道急症，通常以靜脈注射的廣效抗生素（如第三代頭孢菌素）處理，口服窄效青黴素不適合作為首選。
- 高分（0.999）較可能反映既有呼吸道感染適應症的相似性，而非臨床資料。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無與會厭炎相關的文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-33028 | PENICILLIN VK TAB 250MG | 錠劑（許可證未載明劑型） | 許可證未載明 |

製造商：DCH Auriga (Hong Kong) Limited – Universal Division

---

## 安全性考量

- **知識圖譜標示的相關疾病風險**（來自藥物－疾病禁忌關聯，非仿單文字）：腎臟疾病、輸尿管積膿、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、傳染性單核球增多症、慢性 EB 病毒感染症候群。
- **藥物交互作用**：共查得 32 筆，以下列出部分主要項目：
  - 中度：Doxycycline、Minocycline、Tetracycline（四環素類）、Neomycin、Balsalazide、Picosulfuric acid、Warfarin、Dicoumarol、Iodide I-123、Iodide I-131
  - 輕度：Clarithromycin
  - 等級未明：Omeprazole、Lansoprazole、Simvastatin、Prednisolone、Dexamethasone、Acetylsalicylic acid、Clopidogrel、Heparin、Ibuprofen

  與 Warfarin 等抗凝血藥併用時，建議留意凝血功能。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 會厭炎目前只有模型預測，沒有任何臨床試驗或文獻支持。
- 臨床上，會厭炎的致病菌（特別是產 β-內醯胺酶的 H. influenzae）與口服窄效青黴素的抗菌譜不符，且屬急症，標準處置為靜脈廣效抗生素，因此不建議推進。

**若要推進需要：**
- 作用機轉資料（MOA）與仿單的警語、禁忌症
- 會厭炎的致病菌分布與青黴素 V 敏感性資料
- 與現行標準治療比較的臨床證據
- 確認是否有適合急症使用的給藥途徑（目前資料顯示僅有口服錠劑）

---

## 補充：次要預測（喉炎）

TxGNN 對**喉炎 (Laryngitis)** 的預測分數為 0.9985，證據等級同為 L5，建議 Hold。成人急性喉炎多為病毒性，抗生素效益並未確立。唯一提供的文獻（PMID [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/)，1992 年，Acta Oto-Laryngologica Supplementum）研究的是 erythromycin，而非青黴素 V，其摘要並指出 phenoxymethylpenicillin 對臨床病程無影響。因此該文獻不支持本藥用於喉炎，且基於抗生素合理使用原則，沒有試驗證據前不建議推進。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: penicillin v potassium prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ceddc406-4a17-471f-917e-63b4b03779ea) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

