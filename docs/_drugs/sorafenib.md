---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 827
evidence_level: L5
indication_count: 6
monitor_inn: "SORAFENIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-11-17
description: "Sorafenib：預測新適應症為脂肪肉瘤 (liposarcoma)（證據等級 L5）。香港藥劑製品註冊：8 張（有效 8 張）"
---

# Sorafenib
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

## Sorafenib: 脂肪肉瘤 (liposarcoma)
{: .text-alpha }

## 一句話總結

Sorafenib 是一種多重激酶抑制劑，知識圖譜中記錄的原適應症包含肝細胞癌、腎細胞癌與甲狀腺癌。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **1 個臨床試驗**（混合軟組織肉瘤，非脂肪肉瘤專屬）和 **8 篇文獻**，但沒有直接以脂肪肉瘤為對象的研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 脂肪肉瘤 (liposarcoma) |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Sorafenib 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Sorafenib 是一種激酶抑制劑，可於體外減少腫瘤細胞增生。Sorafenib 已證實可抑制多種細胞內激酶（c-CRAF、BRAF 及突變型 BRAF）及細胞表面激酶（KIT、FLT- 3、RET、RET/PTC、VEGFR-1、VEGFR- 2、VEGFR- 3 及 PDGFR-ß）。」英文原文："Sorafenib is a kinase inhibitor that decreases tumor cell proliferation in vitro. Sorafenib was shown to inhibit multiple intracellular (c-CRAF, BRAF and mutant BRAF) and cell surface kinases (KIT, FLT- 3, RET, RET/PTC, VEGFR-1, VEGFR- 2, VEGFR- 3, and PDGFR-ß)."（[DailyMed: Nexavar (sorafenib) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b50667e4-5ebc-4968-a646-d605058dbef0)，版本日期 2023-08-28；查閱日期 2026-11-19）。根據已知資訊，Sorafenib 是多重激酶抑制劑，作用標的包括 RAF/MEK/ERK 訊號路徑、VEGFR 與 PDGFR，這些路徑與腫瘤生長及血管新生有關。

這些路徑在軟組織肉瘤中也有參與。前臨床研究顯示，Sorafenib 能抑制惡性周邊神經鞘瘤與去分化脂肪肉瘤細胞株的生長及 MAPK 訊號；去分化脂肪肉瘤異種移植模型則顯示 PTEN 下調與 PI3K 路徑依賴。

不過，現有臨床研究收納的是混合組織型的軟組織肉瘤，並未針對脂肪肉瘤分層報告，因此對脂肪肉瘤的療效尚未確立。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | 完成 | 51 | 單臂試驗，評估 Sorafenib 用於晚期軟組織肉瘤；脂肪肉瘤為其中一種組織型，未單獨分層 |

## 文獻證據

下表以與脂肪肉瘤及 Sorafenib 較相關者為主：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 試驗 (SWOG S0505) | Cancer | Sorafenib 用於晚期軟組織肉瘤的多中心 Phase 2 研究，納入混合組織型 |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 試驗 | Ann Surg Oncol | 術前放射治療併用 Sorafenib 於局部晚期肢體軟組織肉瘤 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 軟組織肉瘤依組織型選擇治療；脂肪肉瘤以 trabectedin 等為主 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | 軟組織肉瘤依組織型的藥物治療概述 |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | 前臨床 | Mol Cancer Ther | Sorafenib 抑制 MPNST 與去分化脂肪肉瘤細胞株的生長及 MAPK 訊號 |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | 前臨床（異種移植） | Am J Pathol | 去分化脂肪肉瘤模型顯示 PTEN 下調及對 PI3K 抑制的反應（非 Sorafenib 研究） |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (PDOX 模型) | Front Oncol | 肉瘤 PDOX 模型與 CDK 抑制劑組合治療（非 Sorafenib 專屬） |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | 病例報告 | Anti-cancer Drugs | Trabectedin 用於滑膜肉瘤（非 Sorafenib） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55409 | NEXAVAR TAB 200MG（拜耳） | 錠劑 | 未提供 |
| HK-67562 | SORAFENIB STADA TABLETS 200MG | 錠劑 | 未提供 |
| HK-66345 | SORAFENAT TABLETS 200MG | 錠劑 | 未提供 |
| HK-68075 | RAFALVO TABLETS 200MG | 錠劑 | 未提供 |
| HK-68600 | SORAFENIB TABLETS USP 200MG | 錠劑 | 未提供 |

另有 HK-68700（SORAFENIB SANDOZ TABLETS 200MG）、HK-69182（REVAMOX FILM-COATED TABLETS 200MG）與 HK-69261（SORAVAR 200 TABLETS 200MG），共 8 張單一成分許可證，均為有效狀態。

<!-- review:begin hk-lic-20261117-sorafenib-1 -->

> **查核更正（2026-11-17）**：原文為「另有 HK-68700（SORAFENIB SANDOZ TABLETS 200MG），共 6 張單一成分許可證」。已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69182、HK-69261 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261117-sorafenib-1 -->

## 細胞毒性

Sorafenib 屬抗腫瘤藥物（標靶藥物，多重激酶抑制劑）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多重激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：高血壓、肝衰竭、血小板低下、嗜中性白血球低下、顆粒球缺乏症、凝血疾病、急性冠心症／心肌梗塞／心肌缺血、貧血、低磷血症、胰臟炎、焦慮及相關精神疾患等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 重大 (Major)：Dolasetron
  - 中度 (Moderate)：Clarithromycin、Dexamethasone、Levofloxacin、Famotidine、Loperamide、Palonosetron、Naltrexone
  - 輕微 (Minor)：Metronidazole、Dapagliflozin、Naloxegol

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何研究直接以脂肪肉瘤為對象。唯一的臨床試驗與 Phase 2 文獻收納的是混合軟組織肉瘤，且未分層，因此證據等級為 L5。
- 香港仿單的安全資料尚缺。

**若要推進需要：**
- 取得 NCT00217620 與 SWOG S0505 中脂肪肉瘤亞群的分層療效資料
- 補齊作用機轉資料與香港仿單的警語、禁忌
- 設計脂肪肉瘤專屬的前瞻性研究，並與 trabectedin 等現行組織型導向療法比較
- 擬定心血管、血壓、血球與肝功能的監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「另有 HK-68700（SORAFENIB SANDOZ TABLETS 200」→「另有 HK-68700（SORAFENIB SANDOZ TABLETS 200」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Nexavar (sorafenib) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b50667e4-5ebc-4968-a646-d605058dbef0) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

