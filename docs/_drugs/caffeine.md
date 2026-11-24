---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 8
monitor_inn: "CAFFEINE"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
last_modified_at: 2026-11-24
description: "Caffeine：預測新適應症為鼻腔疾病 (nasal cavity disease)（證據等級 L5）。香港藥劑製品註冊：417 張（有效 408 張）"
---

# Caffeine
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

## Caffeine：腺苷受體拮抗型中樞神經興奮劑 → 鼻腔疾病 (nasal cavity disease)
{: .text-alpha }

## 一句話總結

Caffeine（咖啡因）是一種黃嘌呤類中樞神經興奮劑，在香港已有單方許可證上市。
TxGNN 模型預測它可能對**鼻腔疾病 (nasal cavity disease)** 有效，
但目前**沒有臨床試驗**，僅有 **3 篇間接相關文獻**（藥理學回顧、鼻用凝膠的前臨床製劑研究、動物實驗），無法直接支持此預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 鼻腔疾病 (nasal cavity disease) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 408 張／共 417 張） |
| 許可證數 | 417 張（有效 408 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Caffeine 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Caffeine在結構上與其他甲基黃嘌呤類、theophylline及theobromine相關。其為支氣管平滑肌鬆弛劑、中樞神經系統（CNS）興奮劑、心肌興奮劑及利尿劑。雖然caffeine治療早產兒呼吸暫停的作用機轉尚不清楚，但已有數種機轉被提出假說。」英文原文："Caffeine is structurally related to other methylxanthines, theophylline, and theobromine. It is a bronchial smooth muscle relaxant, a CNS stimulant, a cardiac muscle stimulant, and a diuretic. Although the mechanism of action of caffeine in apnea of prematurity is not known, several mechanisms have been hypothesized."（[DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a)，版本日期 2026-07-29；查閱日期 2026-11-19）。已知 Caffeine 為腺苷受體拮抗劑與磷酸二酯酶抑制劑，並可能活化氣道的苦味受體（TAS2R）。這些受體分布於鼻腔與肺部，可能影響黏膜纖毛清除與局部先天免疫，因此在機轉上存在理論上的連結。

另有一項前臨床研究開發了咖啡因鼻用溫感凝膠，顯示經鼻給藥在技術上可行，但該研究針對的是睡眠剝奪後的認知表現，並非鼻腔疾病。

整體而言，這個預測的分數很高，但沒有任何研究直接以鼻腔疾病為對象，因此只能視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | 回顧 | Pharmacology & Therapeutics | 苦味受體表現於鼻腔與肺部等組織，回顧其藥理及在人類氣道的角色 |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | 前臨床製劑研究 | Current Drug Delivery | 咖啡因鼻用溫感凝膠用於改善睡眠剝奪後的認知，未涉及鼻腔疾病 |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | 動物實驗 | Cancer Research | 紅茶與咖啡因抑制大鼠肺部致癌，與鼻腔疾病無直接關聯 |

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-67099 | CAFFEINE CITRATE SOLUTION FOR INJECTION 10MG/1ML | 單一成分 | THE INTERNATIONAL MEDICAL COMPANY LIMITED | 有效 |
| HK-64696 | PEYONA SOLUTION FOR INFUSION AND ORAL SOLUTION 20MG/ML | 單一成分 | ZENFIELDS (H.K.) LIMITED | 有效 |
| HK-50322 | CAFFEINE CITRATE INJ 10MG/ML | 單一成分 | JEAN-MARIE PHARMACAL CO LTD | 有效 |
| HK-01025 | HO CHAI KUNG TJI THUNG SAN | 複方 | KAREN LABORATORIES O/B KAREN PHARMACEUTICAL CO LTD | 有效 |
| HK-50462 | NORMET TAB | 複方 | VICKMANS LABORATORIES LTD | 有效 |

上表列出其中 5 張（共 417 張）。

<!-- licenses:end -->

香港共有 417 張含本藥成分的許可證（有效 408 張、已註銷 9 張；單一成分 3 張、複方 414 張），上表僅列出其中 5 張。

<!-- review:begin hk-lic-20261117-caffeine-1 -->

> **查核更正（2026-11-17）**：原文為「本地資料共列出 20 張有效許可證，此清單可能不完整，上表僅列出其中 5 張。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 417 張含本藥成分的許可證（有效 408 張、已註銷 9 張；單一成分 3 張、複方 414 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-caffeine-1 -->

## 安全性考量

- **藥物交互作用**：已查得 75 筆交互作用，其中較需留意的有：
  - 重大：Cocaine（鼻用）、Cocaine（外用）
  - 中度：Alosetron、Obeticholic acid、Adenosine、Anagrelide、Bendamustine、Capmatinib、Ciprofloxacin、Cycloserine、Dipyridamole、Duloxetine 等
  - 輕度：Acetylsalicylic acid、Cimetidine、Atazanavir、Disulfiram

其他警語與禁忌資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高（0.9991），但目前沒有任何研究直接探討 Caffeine 對鼻腔疾病的作用，僅有機轉推論與製劑可行性研究，證據等級為 L5。

**若要推進需要：**
- 取得詳細的作用機轉資料，特別是苦味受體在鼻黏膜的功能證據
- 以鼻腔疾病（如過敏性或血管運動性鼻炎）為對象的前臨床或探索性臨床研究
- 評估經鼻給藥的局部耐受性與全身暴露風險
- 取得香港原廠仿單的警語、禁忌與核准適應症文字，以完成安全性篩選

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本地資料共列出 20 張有效許可證，此清單可能不完整，上表僅列出其中 5 張。」→「香港共有 417 張含本藥成分的許可證（有效 408 張、已」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

