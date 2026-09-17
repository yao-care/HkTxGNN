---
layout: default
title: Sulfadiazine
parent: 中證據等級 (L3-L4)
nav_order: 710
evidence_level: L3
indication_count: 2
---

# Sulfadiazine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sulfadiazine：原適應症未載明，預測新適應症為肺囊蟲病 (Pneumocystosis)

## 一句話總結

Sulfadiazine（DB00359）目前在香港未上市，Evidence Pack 中亦未提供其原始核准適應症資料。
TxGNN 模型預測它可能對**肺囊蟲病 (Pneumocystosis)** 有效，
目前**無相關臨床試驗登記**，但有 **20 篇文獻**（多為 AIDS 患者合併 toxoplasmosis 與 PCP 治療情境）提供機轉層面的間接支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症資料（香港未上市，Evidence Pack 未收錄） |
| 預測新適應症 | 肺囊蟲病 (Pneumocystosis) |
| TxGNN 預測分數 | 99.39% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 Sulfadiazine 詳細的作用機轉資料（Data Gap: DG002）。不過根據文獻整理出的機轉推論：**Sulfadiazine 抑制二氫蝶酸合成酶 (DHPS)，阻斷病原體的葉酸合成路徑**，這與 sulfamethoxazole（TMP-SMX 複方主成分之一，臨床上為 PCP 治療與預防的標準用藥）機轉相同，理論上對 *Pneumocystis jirovecii* 具有潛在活性。

從文獻證據來看，Sulfadiazine 的相關研究幾乎都出現在 AIDS 患者**同時併發 toxoplasmosis 腦炎與 PCP** 的臨床情境中，常以 pyrimethamine-sulfadiazine 方案治療 toxoplasmosis，並在少數個案中觀察到對合併的 PCP 亦有反應（如 PMID 2645082、5315969、12645193）。換言之，現有證據**並非直接證實 Sulfadiazine 為 PCP 的首選或單一治療藥物**，而是來自於與 TMP-SMX 同機轉類推，以及併治個案的間接觀察。

由於原適應症資料本身缺失，無法進一步比對原適應症與肺囊蟲病之間的臨床關聯性，這也是此預測需要在 Guardrails 下推進、而非直接 Go 的主要原因。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Cohort/Comparative | Clinical Pharmacy | AIDS 患者以 Pyrimethamine-sulfadiazine 治療 Pneumocystis carinii pneumonia 與 toxoplasmosis 之合併方案 |
| [5315969](https://pubmed.ncbi.nlm.nih.gov/5315969/) | 1971 | Case report | Annals of Internal Medicine | 以 Pyrimethamine 併 Sulfadiazine 治療 Pneumocystis carinii pneumonia 之個案報告 |
| [4580723](https://pubmed.ncbi.nlm.nih.gov/4580723/) | 1973 | Review | Transplantation Proceedings | 免疫抑制宿主之肺囊蟲病與弓形蟲病診斷與治療回顧 |
| [9097375](https://pubmed.ncbi.nlm.nih.gov/9097375/) | 1997 | Review | Seminars in Respiratory Infections | Toxoplasma 肺炎回顧，涉及免疫低下患者伺機性感染治療 |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | 系統性原蟲感染（含 Pneumocystis carinii）之治療與預防藥物總覽，含機轉、劑量與毒性資料 |
| [12645193](https://pubmed.ncbi.nlm.nih.gov/12645193/) | 2002 | Case report | J Formos Med Assoc | 台灣 AIDS 個案：以 clindamycin 併 sulfadiazine 治療 Toxoplasma 腦膿瘍，同時併發不典型 PCP |
| [2969023](https://pubmed.ncbi.nlm.nih.gov/2969023/) | 1988 | Review | J Infect Dis | Pneumocystis carinii pneumonia 治療與預防策略回顧 |
| [3897099](https://pubmed.ncbi.nlm.nih.gov/3897099/) | 1985 | Case report/Review | Der Internist | Pneumocystis carinii pneumonia 病例討論 |
| [2011633](https://pubmed.ncbi.nlm.nih.gov/2011633/) | 1991 | Review | Primary Care | AIDS 相關寄生蟲疾病回顧，含 PCP 為最常見伺機性感染（逾 80% 個案） |
| [1344647](https://pubmed.ncbi.nlm.nih.gov/1344647/) | 1992 | Review | Bailliere's Clinical Neurology | HIV 中樞神經系統伺機性感染臨床回顧，涵蓋 CD4 低下與相關治療 |

---

## 香港上市資訊

目前 Sulfadiazine 未在香港上市，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 注意：TFDA 仿單警語/禁忌資料缺失（DG001，Blocking），此為進入 S1 安全性初評的阻斷項目，須優先補齊。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉上具合理性（與 TMP-SMX 同屬 DHPS 抑制劑），且有多篇文獻在 AIDS 併發 toxoplasmosis + PCP 情境中觀察到相關治療反應，證據等級達 L3。
- 但目前**無直接針對 Pneumocystosis 的臨床試驗**，且原適應症與 MOA 資料完全缺失，安全性初評（S1）因仿單資料缺失而無法進行，故不建議直接 Go。

**若要推進需要：**
- 補齊 TFDA／原廠仿單警語與禁忌資料（DG001，Blocking，優先處理）
- 透過 DrugBank API 查詢完整作用機轉（MOA）資料（DG002）
- 針對文獻進行 relevance／study_type 分類確認（目前多筆標記為 pending）
- 評估是否有專門針對 Sulfadiazine（非複方 TMP-SMX）用於 PCP 的前瞻性或觀察性研究可補強證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

