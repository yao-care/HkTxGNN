---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 770
evidence_level: L5
indication_count: 10
monitor_inn: "RIFABUTIN"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
last_modified_at: 2026-10-28
description: "Rifabutin：預測新適應症為HIV 感染（證據等級 L5）。原適應症：許可證資料未載明"
---

# Rifabutin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Rifabutin：從原適應症（許可證未載明）到 HIV 感染
{: .text-alpha }

## 一句話總結

Rifabutin 是一種利福黴素類抗菌藥，香港有 1 張單一成分許可證，但許可證資料沒有載明核准適應症。
TxGNN 模型預測它可能對 **HIV 感染** 有效，但 Rifabutin 本身沒有抗 HIV 活性。
相關試驗多數是在 HIV 族群中治療或預防分枝桿菌感染，或評估與抗病毒藥物的交互作用，沒有研究直接把 Rifabutin 當作 HIV 感染本身的治療。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | HIV 感染 |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

**證據等級說明：** 本報告所列試驗與文獻研究的是 HIV 族群中的 MAC（鳥分枝桿菌複合群）、結核病，以及藥物交互作用。沒有任何一項研究直接評估 Rifabutin 對 HIV 感染本身的效果，因此依規則判為 L5。

---

## 為什麼這個預測合理？

Rifabutin 是利福黴素類藥物，作用是抑制細菌的 DNA 依賴型 RNA 聚合酶。它沒有直接的抗 HIV 活性，此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

在 HIV 患者身上，Rifabutin 的臨床價值在於治療與預防共病感染，主要是 MAC 與結核病。它對 CYP3A4 的誘導作用比 Rifampin 弱，較容易與蛋白酶抑制劑合併使用，但仍需調整劑量並監測藥物濃度。

因此，把這個預測解讀為「HIV 相關感染的輔助用藥」比解讀為「HIV 感染治療」更合理。目前缺乏詳細的作用機轉資料，上述說明來自已知的藥理特性。

---

## 臨床試驗證據

以下為與 HIV 族群最相關的試驗，主要探討 MAC 與結核病，並非 HIV 感染本身。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | 完成 | 450 | 比較 clarithromycin/ethambutol 搭配兩種劑量 Rifabutin 或安慰劑，治療 AIDS 患者的 MAC 菌血症 |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | 完成 | 400 | 四種治療方案用於 AIDS 患者的瀰漫性 MAC，含 Rifabutin 或 clofazimine 組合 |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | 未分期 | 完成 | 200 | 雙盲隨機試驗，評估含 Rifabutin 方案對 AIDS 患者 MAC 菌血症的療效 |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | 完成 | 1100 | 比較 clarithromycin、Rifabutin 及兩者併用，預防 CD4 ≤100 的 HIV 患者發生 MAC |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | 完成 | 720 | azithromycin 與 Rifabutin 單用及併用，預防 HIV 患者的瀰漫性 MAC |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | 未分期 | 完成 | 750 | 雙盲安慰劑對照，Rifabutin 單藥預防 AIDS 患者 MAC 菌血症 |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2 | 完成 | 246 | 三種含 clarithromycin 方案治療 AIDS 患者的瀰漫性 MAC，其中兩種合併 Rifabutin 或 ethambutol |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | 未分期 | 完成 | 215 | 間歇性含 Rifabutin 方案治療 HIV 相關結核病的失敗與復發率 |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | 完成 | 47 | 越南 TB/HIV 共病患者，Rifabutin 搭配抗病毒治療的藥動學 |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | 完成 | 48 | 南非 TB/HIV 共病患者，Rifabutin 搭配抗病毒治療的藥動學 |

---

## 文獻證據

資料中沒有標示為 RCT 的文獻，以下依世代研究、綜述的順序列出。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | 世代研究 | J Antimicrob Chemother | TB/HIV 共病兒童使用 lopinavir/ritonavir 時的 Rifabutin 藥動學與安全性；先前一項兒童研究曾因嚴重嗜中性白血球減少而提前停止 |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | 世代研究 | J Antimicrob Chemother | HIV/TB 共病兒童使用 Rifabutin 的安全性與療效；既有研究中 6 名兒童有 2 名出現限制治療的嗜中性白血球減少 |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | 綜述 | Microbiol Spectr | HIV 與結核病的雙向交互影響及治療挑戰 |
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | 綜述 | Int J Tuberc Lung Dis | 含蛋白酶抑制劑的抗病毒治療與結核病，探討 Rifabutin 取代 Rifampin 的可行性 |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | 綜述 | Drugs | TB/HIV 共病的實務治療，利福黴素類藥物與抗病毒藥物的交互作用 |
| [8785257](https://pubmed.ncbi.nlm.nih.gov/8785257/) | 1996 | 綜述 | Clin Infect Dis | Rifabutin 在 HIV 感染者、新診斷及多重抗藥結核病中的療效與安全性 |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | 綜述 | Med Clin North Am | 非結核分枝桿菌感染；MAC 是 AIDS 最常見的全身性細菌感染 |
| [10456381](https://pubmed.ncbi.nlm.nih.gov/10456381/) | 1999 | 綜述 | Drug Saf | MAC 感染治療的風險效益評估，含 Rifabutin |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | 藥動學模型 | Br J Clin Pharmacol | Rifabutin 與 dolutegravir 的交互作用族群藥動學模型 |
| [39037240](https://pubmed.ncbi.nlm.nih.gov/39037240/) | 2024 | 族群藥動學研究 | Antimicrob Agents Chemother | HIV/TB 共病兒童的 Rifabutin 藥動學與劑量優化 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-38559 | MYCOBUTIN CAP 150MG | 未載明 | 未載明 |

持有廠商為 PFIZER CORPORATION HONG KONG LIMITED，狀態為有效。

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯：** 知識圖譜記錄了血小板低下、嗜中性白血球低下、顆粒球缺乏症、困難梭狀芽孢桿菌結腸炎、周產期壞死性腸炎。這些是圖譜中的關聯，不是仿單內容。
- **血液學風險：** 兒童 TB/HIV 共病研究曾出現嚴重嗜中性白血球減少，使用時需監測血球計數。
- **藥物交互作用：** 資料共有 100 筆交互作用，以下僅列出前 20 筆中較重要的：
  - 嚴重：Eliglustat
  - 中度：Clarithromycin、Doxycycline、Metronidazole、Dexamethasone、Hydrocortisone、Morphine、Aprepitant、Pioglitazone、Saxagliptin、Linagliptin
  - 輕微：Dolasetron
- **與抗病毒藥物併用：** 多項試驗顯示需調整劑量並監測藥物濃度。

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Rifabutin 沒有抗 HIV 活性，現有試驗研究的是 HIV 族群中的 MAC 與結核病，並非 HIV 感染本身，因此依規則只能判為 L5。
- 把它作為 HIV 感染的新適應症缺乏直接證據。較合理的定位是 HIV 共病分枝桿菌感染的輔助用藥，這需要另行界定。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌。
- 重新界定目標適應症，例如「HIV 患者的 MAC 或結核病」，再重新評估證據等級。
- 補充作用機轉資料。
- 擬定血球監測與藥物交互作用管理計畫，尤其針對併用蛋白酶抑制劑與兒童族群。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

