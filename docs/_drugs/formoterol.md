---
layout: default
title: Formoterol
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome"]
description: "Formoterol：預測新適應症為呼吸道畸形 (respiratory malformation)（證據等級 L5）。香港藥劑製品註冊：16 張（有效 16 張）"
---

# Formoterol
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

## Formoterol: 呼吸道畸形 (respiratory malformation)
{: .text-alpha }

## 一句話總結

Formoterol 是長效 β2 受體促效劑，作用是放鬆氣道平滑肌。
TxGNN 模型預測它可能對**呼吸道畸形 (respiratory malformation)** 有效，但目前**沒有臨床試驗**，也沒有直接研究此疾病的文獻，證據僅停留在模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 呼吸道畸形 (respiratory malformation) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 16 張／共 16 張） |
| 許可證數 | 16 張（有效 16 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Formoterol 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Formoterol fumarate 是一種長效型 beta 2 -腎上腺素受體致效劑（beta 2 -致效劑）。吸入的 formoterol fumarate 在肺部發揮局部作用，作為支氣管擴張劑。體外研究顯示，formoterol 對 beta 2 -受體的致效活性比對 beta 1 -受體高出 200 倍以上。」英文原文："Formoterol fumarate is a long-acting, beta 2 -adrenergic receptor agonist (beta 2 -agonist). Inhaled formoterol fumarate acts locally in the lung as a bronchodilator. In vitro studies have shown that formoterol has more than 200-fold greater agonist activity at beta 2 -receptors than at beta 1 -receptors."（[DailyMed: Formoterol Fumarate Inhalation Solution (formoterol fumarate dihydrate) prescribing information, Ritedose Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d9bf685-8886-4865-834b-2748af124b79)，版本日期 2025-12-10；查閱日期 2026-11-19）。已知 Formoterol 屬於長效 β2 受體促效劑，藉由放鬆氣道平滑肌產生支氣管擴張作用。

呼吸道畸形是結構性的先天解剖缺陷，支氣管擴張無法矯正這類缺陷，因此看不出可信的機轉連結。分數偏高，較可能是因為模型中此疾病與阻塞性氣道疾病在網絡上相近。檢索到的文獻主要談氣喘與慢性阻塞性肺病，並非呼吸道畸形。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻皆未直接研究呼吸道畸形，僅作為背景參考（涉及氣喘、慢性阻塞性肺病或其他疾病）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | RCT（系統性回顧與統合分析） | J Am Pharm Assoc | 比較含 formoterol 的三合一與二合一吸入劑用於慢性阻塞性肺病的安全性與療效 |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT | Eur Respir J | 比較重複劑量 budesonide/formoterol 與 salbutamol 在成人氣喘的支氣管擴張與心血管作用 |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | budesonide/formoterol 吸入劑在非裔美籍氣喘患者的長期安全性 |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | RCT | Eur Respir J | Formoterol 可減輕氣喘患者由血小板活化因子引起的反應 |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | J Asthma | 回顧 budesonide/formoterol 吸入劑治療持續性氣喘的療效與安全性 |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Review | Prog Neuropsychopharmacol Biol Psychiatry | 唐氏症認知功能障礙的神經傳導物質策略回顧 |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Cohort | Eur J Appl Physiol | 慢性阻塞性肺病患者睡眠期間的呼吸力學代償反應 |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Case report | J Med Case Rep | 長新冠患者的小氣道疾病個案報告 |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Case report | Medicine | 肺癌術後患者的過敏性支氣管肺黴菌症個案與文獻回顧 |

## 香港上市資訊

香港含本藥成分的許可證皆為複方，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表，均為含 formoterol 的吸入劑產品。

<!-- review:begin hk-lic-20261117-formoterol-1 -->

> **查核更正（2026-11-24）**：原文為「本藥在香港有 13 張有效許可證，均為含 formoterol 的吸入劑產品，目前無已取消者。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證皆為複方，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-formoterol-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-61392 | FOSTER PRESSURISED INHALATION SOLUTION 100/6 MICROGRAMS PER ACTUATION | 複方 | ZENFIELDS (H.K.) LIMITED | 有效 |
| HK-62090 | FLUTIFORM 250 MICROGRAM/10 MICROGRAM PER ACTUATION PRESSURISED INHALATION SUSPEN… | 複方 | DKSH HONG KONG LIMITED | 有效 |
| HK-64503 | DUAKLIR GENUAIR INHALATION POWDER 340 MCG/12 MCG | 複方 | ASTRAZENECA HONG KONG LIMITED | 有效 |
| HK-60618 | VANNAIR PRESSURIZED METERED-DOSE INHALER 80/4.5MCG/DOSE | 複方 | ASTRAZENECA HONG KONG LIMITED | 有效 |
| HK-49176 | SYMBICORT TURBUHALER 160/4.5MCG/DOSE | 複方 | ASTRAZENECA HONG KONG LIMITED | 有效 |

上表列出其中 5 張（共 16 張）。

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分例子。
  - 中度：Acarbose、Isometheptene、Famotidine、Albiglutide、Alogliptin、Canagliflozin、Cisapride、Clarithromycin、Dolasetron、Ephedrine 等
  - 輕度：Beclomethasone dipropionate、Betamethasone、Budesonide、Dexamethasone

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 呼吸道畸形是結構性缺陷，β2 促效劑的支氣管擴張作用無法矯正，機轉上沒有可信的連結。
- 沒有任何臨床試驗，也沒有直接研究此疾病的文獻，證據等級僅為 L5，高分很可能只反映模型中的網絡相近性。

**若要推進需要：**
- 先釐清 Formoterol 與呼吸道畸形之間是否存在合理的機轉假說
- 檢索直接針對呼吸道畸形（或其症狀性氣道阻塞）使用 β2 促效劑的研究
- 取得詳細的作用機轉資料，並從原廠仿單取得完整的警語與禁忌資訊

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「本藥在香港有 13 張有效許可證，均為含 formoterol 的吸入劑產品，目」→「香港含本藥成分的許可證皆為複方，張數與有效張數見」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Formoterol Fumarate Inhalation Solution (formoterol fumarate dihydrate) prescribing information, Ritedose Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d9bf685-8886-4865-834b-2748af124b79) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

