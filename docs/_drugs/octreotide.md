---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Octreotide：預測新適應症為外陰倒置性毛囊角化症 (vulvar inverted follicular keratosis)（證據等級 L5）。原適應症：肢端肥大症、垂體機能亢進、類癌症候群"
monitor_inn: "OCTREOTIDE"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
---

# Octreotide
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

## Octreotide：從肢端肥大症到外陰倒置性毛囊角化症
{: .text-alpha }

## 一句話總結

Octreotide 是體抑素（somatostatin）類似物，原本用於肢端肥大症、垂體機能亢進與類癌症候群。
TxGNN 模型預測它可能對**外陰倒置性毛囊角化症 (vulvar inverted follicular keratosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肢端肥大症、垂體機能亢進、類癌症候群 |
| 預測新適應症 | 外陰倒置性毛囊角化症 (vulvar inverted follicular keratosis) |
| TxGNN 預測分數 | 0.9958 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 22 張／共 22 張） |
| 許可證數 | 22 張（有效 22 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Octreotide 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Sandostatin 注射劑發揮的藥理作用與天然激素體抑素（somatostatin）相似。其對 GH、升糖素及胰島素的抑制作用比體抑素更強。[…] 基於這些藥理作用，octreotide 已被用於治療與轉移性類癌腫瘤相關的症狀（潮紅及腹瀉），以及分泌 VIP 的腺瘤相關症狀（水樣腹瀉）。」英文原文："Sandostatin Injection exerts pharmacologic actions similar to the natural hormone, somatostatin. It is an even more potent inhibitor of GH, glucagon, and insulin than somatostatin. […] By virtue of these pharmacological actions, octreotide has been used to treat the symptoms associated with metastatic carcinoid tumors (flushing and diarrhea), and VIP secreting adenomas (watery diarrhea)."（[DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39)，版本日期 2026-07-22；查閱日期 2026-11-19）。一般認為 Octreotide 是體抑素類似物，主要作用於體抑素受體 SSTR2 與 SSTR5，可抑制生長激素等激素分泌，這與其在肢端肥大症與類癌症候群的用途相符。

外陰倒置性毛囊角化症是良性上皮病變，目前**沒有已知機轉**將體抑素受體訊號與此疾病連結。任何假設（例如抗增生作用）都屬推測，尚未經驗證。此分數來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據。

另一個排名第二的預測為**脂漏性角化症 (seborrheic keratosis)**，分數 0.9955，同樣沒有任何臨床或文獻證據。兩者分數極為接近，此分數來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非疾病特異性的生物機轉。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港含本藥成分的許可證皆為單一成分，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。以下列出 5 張主要許可證，核准適應症欄位於現有資料中未提供。

<!-- review:begin hk-lic-20261117-octreotide-1 -->

> **查核更正（2026-11-24）**：原文為「資料顯示 Octreotide 在香港有 20 張有效單方許可證（無複方、無已註銷）。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證皆為單一成分，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-octreotide-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-32471 | SANDOSTATIN INJ 0.1MG/ML | 單一成分 | NOVARTIS PHARMACEUTICALS (HK) LIMITED | 有效 |
| HK-33912 | SANDOSTATIN INJ 0.5MG/ML | 單一成分 | NOVARTIS PHARMACEUTICALS (HK) LIMITED | 有效 |
| HK-44140 | SANDOSTATIN LAR FOR INJ 20MG | 單一成分 | NOVARTIS PHARMACEUTICALS (HK) LIMITED | 有效 |
| HK-62639 | DBL OCTREOTIDE INJECTION 0.5MG/ML | 單一成分 | PFIZER CORPORATION HONG KONG LIMITED | 有效 |
| HK-68938 | OCTREOTIDE BENDALIS SOLUTION FOR INJECTION/INFUSION 0.1MG/1ML | 單一成分 | MEKIM LTD | 有效 |

上表列出其中 5 張（共 22 張）。

<!-- licenses:end -->

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎情形**（來自模型知識圖譜，非仿單內容）：高血糖、糖尿病、糖尿病酮酸中毒、低血糖、甲狀腺功能低下（含黏液水腫、先天性甲狀腺功能低下）、肝硬化與肝病、膽囊疾病與膽結石（膽石症、膽囊結石、膽總管結石）、腸阻塞與腸道阻塞、心臟驟停、心臟傳導疾病、腎衰竭與尿毒症、維生素 B12 缺乏。
- **藥物交互作用**：查詢共找到 100 筆，以下為資料中列出的部分中等程度（Moderate）交互作用，主要為降血糖藥物：
  - 口服及注射降血糖藥：Acarbose、Metformin、Glimepiride、Chlorpropamide、Alogliptin、Linagliptin
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin
  - GLP-1 類藥物：Albiglutide、Dulaglutide、Semaglutide
  - 各類胰島素：Insulin aspart、degludec、detemir、glargine、glulisine、human (isophane / regular / inhalation)

  Octreotide 會影響血糖調節，與上述藥物併用時需密切監測血糖。

仿單的正式警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症（外陰倒置性毛囊角化症、脂漏性角化症）皆僅有模型分數，沒有臨床試驗、文獻或已知機轉支持，證據等級為 L5。
- 疾病為良性皮膚病變，而 Octreotide 為需注射的藥物，且具血糖、膽道、心臟傳導等安全性顧慮，風險效益比目前無從支持推進。

**若要推進需要：**
- 取得 Octreotide 詳細的作用機轉資料，並釐清體抑素受體在角化症相關皮膚組織的表現與角色
- 進行文獻與臨床試驗的系統性檢索，確認是否存在任何病例報告或前臨床研究
- 取得香港衛生署的仿單（警語、禁忌與核准適應症），完成安全性篩選
- 評估給藥途徑的適配性（目前為注射劑，是否適合局部或皮膚病變用途尚待評估）
- 若有機轉假設，先以前臨床或探索性研究驗證，再考慮進入臨床階段

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「資料顯示 Octreotide 在香港有 20 張有效單方許可證（無複方、無已註」→「香港含本藥成分的許可證皆為單一成分，張數與有效張數見本頁快速」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

