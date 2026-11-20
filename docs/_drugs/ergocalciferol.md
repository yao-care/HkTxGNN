---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 5
monitor_inn: "ERGOCALCIFEROL"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "renal osteodystrophy", "calcium-alkali syndrome"]
last_modified_at: 2026-11-20
description: "Ergocalciferol：預測新適應症為肢中段發育不良，Campailla-Martinelli 型 (acromesomelic dysplasia, Campailla Martinelli type)（證據等級 L5）。香港藥劑製品註冊：4 張（有效 4 張）"
---

# Ergocalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Ergocalciferol: 肢中段發育不良，Campailla-Martinelli 型 (acromesomelic dysplasia, Campailla Martinelli type)
{: .text-alpha }

## 一句話總結

Ergocalciferol 是維生素 D2，屬於維生素 D 類補充劑。
TxGNN 模型預測它可能對**肢中段發育不良，Campailla-Martinelli 型 (acromesomelic dysplasia, Campailla Martinelli type)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 肢中段發育不良，Campailla-Martinelli 型 (acromesomelic dysplasia, Campailla Martinelli type) |
| TxGNN 預測分數 | 0.9983 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Ergocalciferol 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「維生素 D 主要具生物活性之代謝物的體內合成分兩個步驟進行。Ergocalciferol 的第一次羥化作用在肝臟進行（生成 25-羥基維生素 D），第二次則在腎臟進行（生成 1, 25-二羥基維生素 D）。」英文原文："The in vivo synthesis of the major biologically active metabolites of vitamin D occurs in two steps. The first hydroxylation of ergocalciferol takes place in the liver (to 25-hydroxyvitamin D) and the second in the kidneys (to 1, 25-dihydroxyvitamin D)."（[DailyMed: Vitamin D (ergocalciferol) prescribing information, Preferred Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba2076ef-1650-45e1-b092-a4c449dd6210)，版本日期 2026-11-02；查閱日期 2026-11-19）。Ergocalciferol 是維生素 D2，一般認為其作用是在體內轉化為活性形式，調節鈣磷代謝與骨骼礦化。

肢中段發育不良（Campailla-Martinelli 型）是一種罕見的遺傳性骨骼發育不良疾病。根據目前整理的資料，**尚未找到任何機轉上的連結**，補充維生素 D2 是否對這種遺傳性骨骼結構異常有幫助並無支持證據。較高的 TxGNN 分數僅代表模型預測，不能視為療效證明。

因此，這項預測目前應視為待驗證的假說，而非有依據的治療方向。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-36205 | VITALIPID N INFANT INJ | FRESENIUS KABI HONG KONG LIMITED |
| HK-36206 | VITALIPID N ADULT INJ | FRESENIUS KABI HONG KONG LIMITED |
| HK-01178 | POLIBABY CREAM | SATO PHARMACEUTICAL (HK) CO LTD |
| HK-52479 | AMINOLEBAN EN POWDER | OTSUKA PHARMACEUTICAL (H.K.) LIMITED |

目前列出的 4 張許可證皆為有效狀態，香港市場上已有上市產品。

## 安全性考量

- **藥物交互作用**：共查得 55 項潛在交互作用，主要包括：
  - **嚴重 (Major)**：Cholecalciferol、Calcifediol、Calcitriol、Doxercalciferol（其他維生素 D 類製劑，併用有高血鈣風險）
  - **中度 (Moderate)**：Hydrochlorothiazide、Chlorothiazide、Chlorthalidone（噻嗪類利尿劑）、Carbamazepine、Amobarbital、Butalbital、Rifabutin、Digoxin、Cholestyramine、Colestipol、Colesevelam、Sevelamer、Magnesium oxide 等

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測沒有任何臨床試驗或文獻支持，也找不到合理的機轉連結，證據等級為 L5，僅為模型預測。

**若要推進需要：**
- 釐清維生素 D2 與此疾病病理機轉（遺傳性骨骼發育異常）之間是否存在生物學關聯
- 取得作用機轉（MOA）資料
- 在有任何前臨床或病例層級證據之前，不建議投入臨床開發
- 取得香港原廠仿單，完成警語與禁忌症的安全性審查

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Vitamin D (ergocalciferol) prescribing information, Preferred Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba2076ef-1650-45e1-b092-a4c449dd6210) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

