---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 8
monitor_inn: "AMOXICILLIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-20
description: "Amoxicillin：預測新適應症為多株性高黏滯症候群 (polyclonal hyperviscosity syndrome)（證據等級 L5）。香港藥劑製品註冊：156 張（有效 153 張）"
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Amoxicillin：β-內醯胺類抗生素（抑制細菌細胞壁合成）→ 多株性高黏滯症候群 (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## 一句話總結

Amoxicillin 是一種 β-內醯胺類抗生素，用於多種細菌感染。
TxGNN 模型預測它可能對**多株性高黏滯症候群 (polyclonal hyperviscosity syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 多株性高黏滯症候群 (polyclonal hyperviscosity syndrome) |
| TxGNN 預測分數 | 0.9963 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 153 張／共 156 張） |
| 許可證數 | 156 張（有效 153 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Amoxicillin 處方資料（Prescribing Information）「Mechanism of Action」與「Microbiology」段（非官方翻譯）：「Amoxicillin 是一種抗菌藥物。[…] Amoxicillin 對處於活躍繁殖期的敏感細菌所具有的殺菌作用與 penicillin 相似。其作用是透過抑制細胞壁生物合成，進而導致細菌死亡。」英文原文："Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria."（[DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77)，版本日期 2026-11-13；查閱日期 2026-11-19）。就已知資訊，Amoxicillin 是 β-內醯胺類抗菌藥，透過抑制細菌細胞壁合成而殺菌。

多株性高黏滯症候群是由血清免疫球蛋白升高所導致的血液黏滯度上升，並非感染性疾病。Amoxicillin 對免疫球蛋白的生成或血液黏滯度沒有已知作用，因此**目前找不到可信的機轉連結**。

這個高分預測較可能反映模型在網路關係上與感染或免疫球蛋白相關節點的鄰近性，而不是實際的治療作用。分數高不代表有臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 156 張含本藥成分的許可證（有效 153 張、已註銷 3 張；單一成分 69 張、複方 87 張）。以下列出 5 張主要許可證，其核准適應症文字在本地資料中均未記錄。

<!-- review:begin hk-lic-20261117-amoxicillin-1 -->

> **查核更正（2026-11-17）**：原文為「資料顯示共有 20 張單一成分許可證皆為有效，但清單可能不完整。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 156 張含本藥成分的許可證（有效 153 張、已註銷 3 張；單一成分 69 張、複方 87 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-amoxicillin-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52757 | PROMOX CAP 500MG | 未記錄 | 未記錄 |
| HK-35653 | AMOXICAP 250 CAP | 未記錄 | 未記錄 |
| HK-39546 | AMOXYCILLIN CAP 250MG (BRIGHT FUTURE) | 未記錄 | 未記錄 |
| HK-55778 | AMOXICILLIN ORAL SUSPENSION BP 125MG/5ML | 未記錄 | 未記錄 |
| HK-56083 | T.V. MOX CAP 500MG | 未記錄 | 未記錄 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共記錄 100 筆交互作用，較需留意的包括：
  - 重大：Methotrexate、霍亂活疫苗（Vibrio cholerae CVD 103-HgR strain live antigen）
  - 中度：Doxycycline、Minocycline、Demeclocycline、Ethinylestradiol、Estradiol、Dicoumarol、Anisindione、Mycophenolate mofetil、Entecavir 等
  - 輕微：Allopurinol、Amiloride、Azithromycin、Clarithromycin、Erythromycin

其他警語與禁忌症，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測沒有任何臨床試驗或文獻佐證，機轉上也缺乏合理連結（抗菌藥不作用於免疫球蛋白過高造成的黏滯），僅為模型預測，證據等級為 L5。

**若要推進需要：**
- 先建立可信的機轉假說（例如感染是否為該症候群的驅動因素）
- 取得針對此疾病的前臨床或臨床研究證據
- 取得香港原廠仿單，補齊警語、禁忌症與核准適應症資料

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「資料顯示共有 20 張單一成分許可證皆為有效，但清單可能不完整。」→「香港共有 156 張含本藥成分的許可證（有效 153 張、已」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

