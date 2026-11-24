---
layout: default
title: Sennosides
parent: 僅模型預測 (L5)
nav_order: 807
evidence_level: L5
indication_count: 6
monitor_inn: "SENNOSIDES"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "primary hereditary glaucoma", "alopecia"]
last_modified_at: 2026-11-24
description: "Sennosides：預測新適應症為頭皮單純性毛髮稀少症 (hypotrichosis simplex of the scalp)（證據等級 L5）。原適應症：許可證資料中未載明核准適應症文字"
---

# Sennosides
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Sennosides：從便秘（緩瀉）到頭皮單純性毛髮稀疏
{: .text-alpha }

## 一句話總結

Sennosides（番瀉苷）是刺激性緩瀉劑，在香港有多張單一成分許可證。
TxGNN 模型預測它可能對**頭皮單純性毛髮稀少症 (hypotrichosis simplex of the scalp)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測，建議暫緩（Hold）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料中未載明核准適應症文字 |
| 預測新適應症 | 頭皮單純性毛髮稀少症 (hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 0.9929 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 11 張／共 11 張） |
| 許可證數 | 11 張（有效 11 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理知識，Sennosides 是刺激性緩瀉劑，其活性代謝物 rheinanthrone 作用於結腸黏膜與腸道神經元，增加前列腺素 E2 並改變水與電解質的運輸。

這個作用與毛囊生物學，或與頭皮單純性毛髮稀少症的遺傳成因（如 CDSN、APCDD1、RPL21）之間，目前沒有已知的連結。高分預測的分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，也缺乏臨床資料支持。

因此，這項預測目前**無法在機轉上得到合理解釋**，只能視為待驗證的假說。

其他分數相近的預測（先天性毛髮稀少伴粟丘疹、瀰漫性斑禿、開角型青光眼、原發性遺傳性青光眼、一般禿髮）同樣沒有試驗或文獻，也沒有可成立的機轉。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-68436 | NEPURGO SENNOSIDES TABLETS 20MG | 單一成分 | WELLDONE PHARMACEUTICALS LIMITED | 有效 |
| HK-66475 | WEL-HEALTH LAXATIVE TABLETS 12MG | 單一成分 | VAST RESOURCES PHARMACEUTICAL LTD | 有效 |
| HK-68435 | EFORMAT SENNOSIDES TABLETS 20MG | 單一成分 | WELLDONE PHARMACEUTICALS LIMITED | 有效 |
| HK-45031 | PMS-SENNOSIDES TAB 8.6MG | 單一成分 | TRENTON-BOMA LTD | 有效 |
| HK-68434 | EASUWEI SENNOSIDES TABLETS 20MG | 單一成分 | WELLDONE PHARMACEUTICALS LIMITED | 有效 |

上表列出其中 5 張（共 11 張）。

<!-- licenses:end -->

香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表，此處僅列出部分許可證。

<!-- review:begin hk-lic-20261117-sennosides-1 -->

> **查核更正（2026-11-24）**：原文為「共 9 張許可證，皆為單一成分且有效；此處僅列出 5 張。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證包括單一成分與複方製劑，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-sennosides-1 -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測，無任何臨床試驗或文獻直接研究此疾病，證據等級為 L5。
- 刺激性緩瀉劑的作用部位在腸道，與毛囊生物學無已知關聯；長期濫用緩瀉劑還可能造成營養不良，反而不利毛髮。

**若要推進需要：**
- 取得 Sennosides 的作用機轉資料，並釐清其與毛囊或相關疾病通路是否有關
- 取得香港仿單的核准適應症、警語與禁忌資料
- 以文獻與臨床試驗登記系統檢索，確認是否有直接研究此疾病的資料
- 若上述皆無支持，不建議投入進一步開發

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「共 9 張許可證，皆為單一成分且有效；此處僅列出 5 張。」→「香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

