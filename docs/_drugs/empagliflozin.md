---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-17
description: "Empagliflozin：預測新適應症為典型僵人症候群 (Classic Stiff Person Syndrome)（證據等級 L5）。原適應症：第 2 型糖尿病 (Type 2 Diabetes Mellitus)"
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Empagliflozin：從第 2 型糖尿病到僵人症候群（Classic Stiff Person Syndrome）
{: .text-alpha }

## 一句話總結

Empagliflozin 是一種用於第 2 型糖尿病的藥物，在香港已有單方與複方產品上市。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病 (Type 2 Diabetes Mellitus) |
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 0.9906 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 16 張／共 16 張） |
| 許可證數 | 16 張（有效 16 張） |
| 建議決策 | Hold |

註：香港許可證資料中未提供核准適應症文字，上表「原適應症」的來源並非香港許可證資料。

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Empagliflozin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Empagliflozin是SGLT2的抑制劑，SGLT2是負責將葡萄糖從腎絲球濾液再吸收回循環中的主要轉運蛋白。透過抑制SGLT2，empagliflozin可減少腎臟對已過濾葡萄糖的再吸收並降低葡萄糖的腎閾值，從而增加尿液葡萄糖排泄。」英文原文："Empagliflozin is an inhibitor of SGLT2, the predominant transporter responsible for reabsorption of glucose from the glomerular filtrate back into the circulation. By inhibiting SGLT2, empagliflozin reduces renal reabsorption of filtered glucose and lowers the renal threshold for glucose, and thereby increases urinary glucose excretion."（[DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565)，版本日期 2026-11-10；查閱日期 2026-11-19）。Empagliflozin 一般已知為 SGLT2 抑制劑，但本次整理的資料並未提供機轉內容，因此無法從資料中建立與僵人症候群之間的機轉連結。

僵人症候群是一種自體免疫性神經疾病，常與抗 GAD65 抗體及 GABA 神經傳導受損有關。SGLT2 抑制與這類病理之間的關聯並不明確。

較可能的解釋是：GAD65 自體免疫與糖尿病之間存在關聯，模型的高分可能部分反映了這種疾病間的共現關係，而非真正的治療效果。此外，局灶性僵肢症候群（Focal Stiff Limb Syndrome，同屬僵人症候群譜系）取得完全相同的分數 (0.9906)，顯示預測來自 TxGNN 模型（深度學習）中共享的疾病節點特徵，而非獨立證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64095 | JARDIANCE TABLETS 10MG | 錠劑 | 未提供 |
| HK-64096 | JARDIANCE TABLETS 25MG | 錠劑 | 未提供 |
| HK-65353 | GLYXAMBI TABLETS 10MG/5MG | 錠劑 | 未提供 |
| HK-65354 | GLYXAMBI TABLETS 25MG/5MG | 錠劑 | 未提供 |
| HK-64242 | JARDIANCE DUO TABLETS 12.5MG/1000MG | 錠劑 | 未提供 |

以上列出 5 張主要許可證，共 16 張有效許可證（含單方與複方；JARDIANCE、GLYXAMBI、JARDIANCE DUO 由 Boehringer Ingelheim (HK) Ltd 持有，其餘為其他公司的學名藥）。

<!-- review:begin hk-lic-20261117-empagliflozin-1 -->

> **查核更正（2026-11-17）**：原文為「共 10 張有效許可證，均由 Boehringer Ingelheim (HK) Ltd 持有」。已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69040、HK-69041、HK-69189、HK-69190、HK-69229、HK-69230 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261117-empagliflozin-1 -->

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下為部分範例：
  - 中度：Phenylephrine、Acebutolol、Acetazolamide、Formoterol、Pseudoephedrine、Nifedipine、Epinephrine、Ethinylestradiol、Hydrocortisone、Salbutamol、Ethanol、Furosemide
  - 輕度：Hydrocortisone（外用）、Alclometasone（外用）

其他警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 TxGNN 模型預測 (L5)，沒有臨床試驗、文獻或機轉資料支持。
- 預測分數可能受糖尿病與 GAD65 自體免疫的關聯，或相近疾病共享節點特徵影響，不宜視為獨立證據。

**若要推進需要：**
- 補齊作用機轉 (MOA) 資料，評估 SGLT2 抑制與僵人症候群病理的可能連結
- 進行文獻回顧，確認是否有任何前臨床或病例報告
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩選
- 若有前臨床證據，再考慮設計探索性研究

---

### 其他預測適應症（供參考）

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|------|-----------|---------|------|
| 2 | 局灶性僵肢症候群 (Focal Stiff Limb Syndrome) | 0.9906 | L5 | Hold |
| 3 | 眼骨發育不良 (Opsismodysplasia) | 0.9903 | L5 | Hold |

Opsismodysplasia 為由 INPPL1 突變造成的罕見骨骼發育不良，涉及 PI3K／胰島素訊號路徑。雖然與葡萄糖及胰島素訊號有推測性的關聯，但尚未驗證；且對兒童骨骼疾病使用 SGLT2 抑制劑也會引發安全性疑慮。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「共 10 張有效許可證，均由 Boehringer Ingelheim (HK)」→「共 16 張有效許可證（含單方與複方；JARDIANCE、GLYXAMBI、JA」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

