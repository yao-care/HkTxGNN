---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Domperidone：預測新適應症為腎因性抗利尿不適當症候群 (NSIAD)（證據等級 L5）。原適應症：香港許可證未載明核准適應症文字"
monitor_inn: "DOMPERIDONE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Domperidone
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

## Domperidone：從消化道症狀（適應症資料缺失）到腎因性抗利尿不適當症候群
{: .text-alpha }

## 一句話總結

Domperidone 是週邊多巴胺 D2/D3 受體拮抗劑，臨床上用於處理消化不良、胃灼熱、上腹痛、噁心與嘔吐。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症文字（藥理資料顯示用於消化不良、噁心、嘔吐等） |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 0.9908 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 41 張／共 41 張） |
| 許可證數 | 41 張（有效 41 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

ChEMBL（EMBL-EBI）收錄的 Domperidone 作用機轉（非官方翻譯）：「多巴胺 D2 受體拮抗劑」。英文原文："Dopamine D2 receptor antagonist"（[ChEMBL CHEMBL219916 (domperidone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL219916)，CC BY-SA 3.0；查閱日期 2026-11-19）。已知 domperidone 是週邊多巴胺 D2/D3 受體拮抗劑（標靶為 DRD2、DRD3），作為促腸胃蠕動與止吐藥使用。

NSIAD 是由血管加壓素 V2 受體 (AVPR2) 的功能獲得性突變所致，會在沒有血管加壓素的情況下造成水分滯留與低血鈉。目前並無已知路徑將 D2 拮抗作用與 V2 受體活性或腎臟水分處理連結起來。

因此，這個預測分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性（例如低血鈉、水分平衡相關疾病），而非生物學證據。此連結目前仍屬推測，若要進一步考慮，需先有合理的標靶層級論證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 41 張含本藥成分的許可證（全部有效；皆為單一成分），以下列出 5 張代表性許可證（資料中未提供劑型與核准適應症文字）：

<!-- review:begin hk-lic-20261117-domperidone-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 20 張有效單方許可證，以下列出 5 張代表性許可證（資料中未提供劑型與核准適應症文字）：」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 41 張含本藥成分的許可證（全部有效；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-domperidone-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-58627 | APO-DOMPERIDONE TAB 10MG | 單一成分 | HIND WING CO LTD | 有效 |
| HK-64541 | DOSIN TABLETS 10MG | 單一成分 | TOP HARVEST PHARMACEUTICALS COMPANY LIMITED | 有效 |
| HK-48289 | NIDOLIUM TAB 10MG | 單一成分 | SUNTOL MEDICAL LIMITED | 有效 |
| HK-44630 | DOMPEON TAB 10MG | 單一成分 | NEOCHEM PHARMACEUTICAL LABORATORIES LTD. | 有效 |
| HK-50698 | VICKTILIN SYRUP 5MG/5ML | 單一成分 | VICKMANS LABORATORIES LTD | 有效 |

上表列出其中 5 張（共 41 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物－疾病禁忌關係，非仿單文字）：長 QT 症候群、家族性長 QT 症候群、尖端扭轉型心室頻脈 (torsades de pointes)、肝臟疾病、膽囊疾病。
- **QT 風險**：domperidone 具有 QT 延長與心律不整風險。NSIAD 患者常有低血鈉與電解質異常，而這些本身是 QT 相關事件的危險因子，此族群可能特別脆弱。
- **藥理交互作用紀錄**：共 2 筆，皆為藥理標靶紀錄（D2 受體、D3 受體），並非藥物間交互作用。

其餘警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數（0.9908），沒有臨床試驗或文獻佐證，且 D2/D3 拮抗與 V2 受體或腎臟水分處理之間缺乏已知機轉連結。
- 目標族群的低血鈉與電解質異常會加重 domperidone 的 QT 風險，安全性疑慮明顯。

**若要推進需要：**
- 提出標靶層級的合理機轉假說（D2/D3 或其他路徑如何影響 AVPR2 或腎臟水分處理）
- 取得完整作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌症，完成安全性篩選
- 進行文獻與臨床前研究的系統性檢索，確認是否有任何支持證據
- 若未來考慮推進，需先評估 QT 與電解質監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 20 張有效單方許可證，以下列出 5 張代表性許可證（資料中未提供劑型」→「香港共有 41 張含本藥成分的許可證（全部有效；皆為單一成分」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄（2026-11-20 修訂，前版保留於紀錄） | [ChEMBL CHEMBL219916 (domperidone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL219916) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

