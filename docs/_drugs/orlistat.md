---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 646
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Orlistat：預測新適應症為高維生素症 (Hypervitaminosis)（證據等級 L5）。原適應症：肥胖症（obesity disorder）、單基因肥胖（monogenic obesity）"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
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

## Orlistat：從肥胖症到高維生素症
{: .text-alpha }

## 一句話總結

Orlistat 是胃腸道脂肪酶抑制劑，原本用於肥胖症（obesity disorder）與單基因肥胖（monogenic obesity）的治療。
TxGNN 模型預測它可能對**高維生素症 (Hypervitaminosis)** 有效，
但目前**沒有臨床試驗與文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肥胖症（obesity disorder）、單基因肥胖（monogenic obesity） |
| 預測新適應症 | 高維生素症 (Hypervitaminosis) |
| TxGNN 預測分數 | 0.9942 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 13 張／共 13 張） |
| 許可證數 | 13 張（有效 13 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Orlistat 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Orlistat為胃腸道脂肪酶的可逆性抑制劑。其透過與胃脂肪酶及胰脂肪酶的活性絲胺酸殘基位點形成共價鍵，於胃及小腸腔內發揮其治療作用。」英文原文："Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases."（[DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e)，版本日期 2026-09-30；查閱日期 2026-11-19）。依一般藥理知識，Orlistat 是胃及胰臟脂肪酶抑制劑，可使膳食脂肪吸收減少約 30%。

脂溶性維生素（A、D、E、K）需隨膳食脂肪一同吸收，因此 Orlistat 會降低它們的吸收。對於脂溶性維生素過量所致的高維生素症，理論上減少腸道吸收可能略微降低體內維生素負荷，這是模型預測在生物學上的可能依據。

但需要注意：
- 這個效果正好是 Orlistat 平常的安全性疑慮（維生素缺乏，需額外補充），方向相反。
- 只影響脂溶性維生素，對水溶性維生素無效。
- 高維生素症的主要處置是停止維生素來源，Orlistat 的實用價值有限。
- 以上機轉為依一般知識推論，並非來自本報告彙整的資料。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67026 | ODISTAD 120 CAPSULES 120MG | 膠囊（品名標示） | 資料未提供 |
| HK-61889 | ZEROTEX CAPSULE 120MG | 膠囊（品名標示） | 資料未提供 |
| HK-44752 | XENICAL CAP 120MG | 膠囊（品名標示） | 資料未提供 |
| HK-67567 | OLILIO CAPSULES 60MG | 膠囊（品名標示） | 資料未提供 |
| HK-61430 | CUVARLIX CAP 120MG | 膠囊（品名標示） | 資料未提供 |

本藥共有 13 張有效單方許可證，上表僅列出 5 張主要許可證。

<!-- review:begin hk-lic-20261117-orlistat-1 -->

> **查核更正（2026-11-17）**：原文為「本藥共有 12 張有效單方許可證」。已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69282 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261117-orlistat-1 -->

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（非仿單內容）：肝衰竭、原發性高草酸尿症、神經性厭食症、神經性暴食症、維生素缺乏症、膽汁淤積（含良性復發性肝內膽汁淤積、家族性肝內膽汁淤積）、藥物性肝損傷。
- **藥物交互作用**：共查得 100 筆交互作用，以下為部分範例：
  - 中度：Abacavir、Lamivudine、Acarbose、Albiglutide、Alogliptin、Metformin、Amiodarone、Atazanavir、Emtricitabine、Canagliflozin 等
  - 輕度：Cholecalciferol、Calcifediol、Calcitriol（皆為維生素 D 類，與本預測適應症相關，需特別留意）

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（分數 0.9942），沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 機轉方向與 Orlistat 常見的維生素缺乏風險相反，且高維生素症的標準處置是移除來源，臨床價值不明確。另有 100 筆藥物交互作用，以及多項潛在禁忌疾病（尤其是肝臟與膽汁淤積相關），需審慎看待。

**若要推進需要：**
- 取得 Orlistat 的詳細作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 進行文獻與臨床試驗檢索，確認是否有脂溶性維生素過量的相關研究
- 以前臨床或小規模研究驗證其降低脂溶性維生素負荷的幅度與臨床意義
- 評估與維生素 D 類藥物等交互作用的臨床影響

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本藥共有 12 張有效單方許可證」→「本藥共有 13 張有效單方許可證」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

