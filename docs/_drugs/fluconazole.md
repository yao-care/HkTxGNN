---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "FLUCONAZOLE"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
description: "Fluconazole：預測新適應症為點狀上皮角膜結膜炎 (punctate epithelial keratoconjunctivitis)（證據等級 L5）。香港藥劑製品註冊：40 張（有效 36 張）"
---

# Fluconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Fluconazole: 點狀上皮角膜結膜炎 (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## 一句話總結

Fluconazole 是三唑類抗黴菌藥，原本用於口咽、食道、陰道念珠菌感染、念珠菌血症及隱球菌腦膜炎等。
TxGNN 模型預測它可能對**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，
但目前**沒有臨床試驗和文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 點狀上皮角膜結膜炎 (punctate epithelial keratoconjunctivitis) |
| TxGNN 預測分數 | 0.9924 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 36 張／共 40 張） |
| 許可證數 | 40 張（有效 36 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Fluconazole 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Fluconazole 是真菌細胞色素 P450 依賴性酵素羊毛固醇 14-α-去甲基酶的高度選擇性抑制劑。此酵素的作用為將羊毛固醇轉化為麥角固醇。隨後正常固醇的流失與真菌體內 14-α-甲基固醇的蓄積相關，並可能是 fluconazole 抑制真菌生長活性的原因。」英文原文："Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole."（[DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204)，版本日期 2026-04-02；查閱日期 2026-11-19）。一般認為 fluconazole 是三唑類抗黴菌藥，可抑制真菌 CYP51（羊毛固醇 14-α-去甲基酶），干擾真菌細胞膜的麥角固醇合成。這是從藥物類別推論，並非本次整理資料所提供的內容。

點狀上皮角膜結膜炎常見原因為病毒（如腺病毒）或非感染性因素，並非典型的黴菌感染。因此，抗黴菌作用在機轉上並不明顯適用。此分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，並非生物學證據。

目前這項預測是唯一的支持訊號，沒有試驗或文獻佐證。在釐清病因與機轉前，應謹慎看待這個高分。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 40 張含本藥成分的許可證（有效 36 張、已註銷 4 張；皆為單一成分）。下表列出 5 張主要許可證，其核准適應症文字在資料中皆為空白。

<!-- review:begin hk-lic-20261117-fluconazole-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 20 張有效的單一成分許可證，無已註銷者。」。已更正：HK-54401 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。 已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 40 張含本藥成分的許可證（有效 36 張、已註銷 4 張；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-fluconazole-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-31175 | DIFLUCAN CAP 50MG | 單一成分 | PFIZER CORPORATION HONG KONG LIMITED | 有效 |
| HK-32536 | DIFLUCAN INJ 2MG/ML | 單一成分 | PFIZER CORPORATION HONG KONG LIMITED | 有效 |
| HK-52849 | FLUCONAZOLE-TEVA CAP 50MG | 單一成分 | TEVA PHARMACEUTICAL HONG KONG O/B TEVA PHARMACEUTICAL HONG KONG LIMITE… | 有效 |
| HK-52848 | FLUCONAZOLE-TEVA CAP 150MG | 單一成分 | TEVA PHARMACEUTICAL HONG KONG O/B TEVA PHARMACEUTICAL HONG KONG LIMITE… | 有效 |
| HK-67485 | FLUCONAZOLE SOLUTION FOR INFUSION 100MG/50ML | 單一成分 | HONG KONG MEDICAL SUPPLIES LTD | 有效 |

上表列出其中 5 張（共 40 張）。

<!-- licenses:end -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自圖譜關聯，非仿單內容）：long QT 症候群、家族性 long QT 症候群、腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病。
- **藥物交互作用**：共查得 100 筆，以下為部分摘要。
  - **重度 (Major)**：Chlorpropamide
  - **中度 (Moderate)**：Famotidine、Rabeprazole、Omeprazole、Dexlansoprazole、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide、Aprepitant、Loperamide、Saxagliptin
  - **輕度 (Minor)**：Amphotericin B、Clarithromycin

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數很高（0.9924），但這是唯一的證據，沒有任何臨床試驗或文獻。
- 該疾病多為病毒性或非感染性，抗黴菌機轉並不明顯適用。

**若要推進需要：**
- 釐清目標病因，確認是否有黴菌成分，並檢視與其他眼表疾病的關聯
- 補齊作用機轉資料
- 文獻與試驗檢索，包括眼科局部或全身使用 fluconazole 的研究
- 取得香港仿單的警語與禁忌，完成安全性篩選
- 評估給藥途徑是否適合眼部用藥（目前路徑相容性尚未評估）
- 若要考慮用於 long QT 或肝腎疾病患者，需制定安全監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 20 張有效的單一成分許可證，無已註銷者。」→「香港共有 40 張含本藥成分的許可證（有效 36 張、已註銷」 | 更正（2026-11-17 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

