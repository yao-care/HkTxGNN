---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 6
monitor_inn: "PREGABALIN"
predicted_indications: ["tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-11-17
description: "Pregabalin：預測新適應症為肌腱炎 (Tendinitis)（證據等級 L5）。原適應症：香港許可證資料中未載明核准適應症"
---

# Pregabalin
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

## Pregabalin：從焦慮症、纖維肌痛等已知用途到肌腱炎
{: .text-alpha }

## 一句話總結

Pregabalin 在知識圖譜中記錄的用途包括焦慮症、纖維肌痛、肌筋膜疼痛症候群與帶狀疱疹後神經痛。
TxGNN 模型預測它可能對**肌腱炎 (Tendinitis)** 有效，但目前**沒有臨床試驗**，文獻也未直接研究肌腱炎本身，證據僅屬模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料中未載明核准適應症；知識圖譜記錄的關聯用途為焦慮症、纖維肌痛、肌筋膜疼痛症候群、帶狀疱疹後神經痛（非核准適應症） |
| 預測新適應症 | 肌腱炎 (Tendinitis) |
| TxGNN 預測分數 | 0.9971 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 57 張／共 57 張） |
| 許可證數 | 57 張（有效 57 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Pregabalin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Pregabalin會與中樞神經系統組織中的alpha 2 ‑delta位點（電壓門控鈣離子通道的一種輔助次單元）高親和力結合。雖然pregabalin的作用機轉尚未完全闡明，但基因改造小鼠及與pregabalin結構相關之化合物（例如gabapentin）的研究結果顯示，與alpha 2 ‑delta次單元結合可能與pregabalin在動物中的抗傷害感受及抗癲癇作用有關。」英文原文："Pregabalin binds with high affinity to the alpha 2 ‑delta site (an auxiliary subunit of voltage‑gated calcium channels) in central nervous system tissues. Although the mechanism of action of pregabalin has not been fully elucidated, results with genetically modified mice and with compounds structurally related to pregabalin (such as gabapentin) suggest that binding to the alpha 2 ‑delta subunit may be involved in pregabalin’s anti‑nociceptive and antiseizure effects in animals."（[DailyMed: Lyrica Cr (pregabalin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f280bbd8-2af2-444a-bd96-e409337ca6dd)，版本日期 2026-03-12；查閱日期 2026-11-19）。根據一般藥理知識，pregabalin 可結合電壓門控鈣離子通道的 alpha-2-delta 次單元，減少興奮性神經傳導物質釋放，可能緩解神經病變性與傷害感受性疼痛。

TxGNN 模型（深度學習）對肌腱炎給出的分數，可能反映模型從相關疾病（如 pregabalin 相關的纖維肌痛、肌筋膜疼痛等疼痛症候群）學到的相似性，而非生物學證據。這最多代表症狀性止痛的可能，並無證據顯示它能改變肌腱本身的病理。

模型分數雖高（0.9971），但沒有任何文獻直接研究 pregabalin 用於肌腱炎，因此分數不應被視為療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻均未直接研究 pregabalin 治療肌腱炎：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | 關節鏡肩袖修補術後，口服 pregabalin 的術後疼痛評分與肌間溝臂神經叢阻斷相當（術後急性疼痛，非肌腱炎） |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | 回溯性世代研究 | J Orthop Sci | 評估 pregabalin 於肩袖修補術後的止痛與節省鴉片類效果（間接證據） |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | 病例報告 | Praxis | 環丙沙星相關失能個案，提及肌腱病變為氟喹諾酮副作用 |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | 社論 | Arthroscopy | 梨狀肌症候群的診斷與坐骨神經鬆解術 |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | 病例報告 | Pain Pract | 馬拉松後股後皮神經壓迫，與肌腱炎相關 |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | 前臨床 | Adv Pharmacol Pharm Sci | 植物萃取物於大鼠長春新鹼神經病變的作用（與 pregabalin 及肌腱炎無直接關係） |

## 香港上市資訊

香港共有 57 張含本藥成分的許可證（全部有效；皆為單一成分），以下列出 5 張。資料中未提供劑型與核准適應症文字。

<!-- review:begin hk-lic-20261117-pregabalin-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有至少 20 張 pregabalin 單方許可證（清單可能不完整），以下列出 5 張。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 57 張含本藥成分的許可證（全部有效；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-pregabalin-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53029 | LYRICA CAP 25MG | 膠囊 | 未提供 |
| HK-53026 | LYRICA CAP 300MG | 膠囊 | 未提供 |
| HK-66282 | PRELYNCA CAPSULES 75MG | 膠囊 | 未提供 |
| HK-68026 | PREGABALIN TEVA CAPSULES 25MG | 膠囊 | 未提供 |
| HK-62124 | BRILLIOR CAPSULES 50MG | 膠囊 | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：焦慮症、神經官能症、情緒低落性疾患、血小板低下、血管性水腫（含遺傳性、後天性及 RAAS 阻斷劑誘發）、肌病變、橫紋肌溶解、腎功能不全、房室傳導阻滯等。
- **藥物交互作用**：共查得 100 筆，主要包括：
  - 重大：Morphine、Morphine (liposomal)
  - 中度：Pioglitazone、Rosiglitazone、Troglitazone、Difenoxin、Diphenoxylate、Dronabinol、Nabilone、Opium、Metoclopramide、Sibutramine
- 仿單警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何直接研究 pregabalin 治療肌腱炎的試驗或文獻，證據僅為模型預測（L5）。
- 即使有效，也僅可能是症狀性止痛，且肌病變等風險在知識圖譜中被列為禁忌關聯，需謹慎。

**若要推進需要：**
- 取得 pregabalin 的作用機轉資料與香港仿單（警語、禁忌、核准適應症）
- 設計針對肌腱炎疼痛的小型概念驗證試驗
- 評估肌病變相關風險，以及與鴉片類藥物併用的安全性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有至少 20 張 pregabalin 單方許可證（清單可能不完整），以下」→「香港共有 57 張含本藥成分的許可證（全部有效；皆為單一成分」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Lyrica Cr (pregabalin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f280bbd8-2af2-444a-bd96-e409337ca6dd) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

