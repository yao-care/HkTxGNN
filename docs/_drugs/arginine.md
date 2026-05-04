---
layout: default
title: Arginine
parent: 中證據等級 (L3-L4)
nav_order: 59
evidence_level: L4
indication_count: 1
---

# Arginine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Arginine：從胺基酸補充劑到胃輕癱

## 一句話總結

L-Arginine（L-精胺酸）是人體必需胺基酸之一，為一氧化氮（NO）生成的唯一前驅物，目前主要作為營養補充劑使用，在香港尚無正式核准藥品上市。TxGNN 模型預測它可能對**胃輕癱 (Gastroparesis)** 有效，其核心機轉在於補充 L-Arginine 可恢復腸神經系統的 NO 生成，進而改善胃平滑肌舒張與排空功能。目前有 **10 篇文獻**支持此方向，但所有證據均來自動物模型，尚無直接的人體臨床試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胺基酸補充（無正式核准適應症記錄） |
| 預測新適應症 | 胃輕癱 (Gastroparesis) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

L-Arginine 是一氧化氮合酶（NOS）的唯一底物，腸神經系統中的抑制性運動神經元（nitrergic neurons）依賴 **Arginine → nNOS → NO** 路徑產生一氧化氮，使胃平滑肌舒張，促進胃容納（accommodation）與幽門括約肌鬆弛——這是正常胃排空的關鍵生理步驟。

胃輕癱的病理機制中常見 nitrergic 神經傳導缺損，包括 nNOS 活性下降、BH4 輔因子不足、以及 L-Arginine 耗竭。補充 L-Arginine 理論上可直接恢復 NO 生成底物供應，修復受損的胃運動調控。PMID 25057793（Reichardt et al., 2014, *Endocrinology*）最直接示範：糖皮質激素誘發的胃輕癱係透過 **L-Arginine 耗竭**介導，且補充後可改善症狀，為此再利用方向提供最強的機轉支持。

整體而言，L-Arginine 用於胃輕癱的機轉路徑清晰且具生物合理性，但目前所有支持證據仍停留於動物模型層次，包括糖尿病、帕金森病及糖皮質激素誘發的胃輕癱動物模型。由 L4 等級晉升至 L2/L3 需要人體臨床試驗的直接驗證。

---

## 臨床試驗證據

目前無直接相關的臨床試驗登記。

> 資料庫查詢中，[NCT01702051](https://clinicaltrials.gov/study/NCT01702051) 因糖尿病—胃輕癱共同關鍵字被召回，但其研究主題為「自體胰島細胞移植改善全胰切除後血糖控制」，介入措施為外科細胞移植，與 L-Arginine 藥物治療胃輕癱無直接關聯（相關性評級 C），不具實質參考價值。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Animal Model (mechanistic) | *Endocrinology* | **最直接支持**：糖皮質激素誘發胃輕癱係透過 L-Arginine 耗竭介導，GR(dim) 突變小鼠不受影響，補充 Arginine 可改善胃排空 |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Animal Model (mechanistic) | *Am J Physiol Gastrointest* | BH4（NOS 必需輔因子）缺乏誘發新生小鼠胃輕癱，強化 Arginine→NOS→NO 路徑在胃運動中的核心地位 |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Animal Model | *Am J Physiol Gastrointest* | 帕金森病 6-OHDA 大鼠幽門括約肌 nitrergic 舒張受損，nNOS 功能異常是胃輕癱的重要機轉 |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Animal Model | *Neurogastroenterol Motility* | 糖尿病 BB 大鼠空腸 nNOS 表現顯著下降，確認 NO 路徑在糖尿病胃腸神經病變中的作用 |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Animal Model | *Am J Physiol Gastrointest* | 同步胃電刺激透過 nitrergic 路徑改善迷走神經切斷後的胃容納功能障礙 |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Animal Model | *World J Gastroenterol* | Ghrelin 及 GHRP-6 改善糖尿病胃輕癱小鼠的胃運動，提供治療對照背景 |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Animal Model | *Am J Physiol Gastrointest* | 高血糖透過迷走神經傳入纖維 KATP 通道介導胃運動抑制，提供糖尿病胃輕癱神經機轉背景 |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Animal Model | *Am J Physiol Gastrointest* | 薦椎神經刺激透過脊髓傳入/迷走神經傳出路徑增強大鼠胃容納功能 |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Animal Model | *Gastroenterology* | 食物蛋白過敏誘發大鼠胃排空延遲，早期確認免疫介導胃輕癱模型 |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case Report | *Am J Case Reports* | MELAS 患者使用 Arginine 後乳酸正常化之個案，間接支持 Arginine 補充對粒線體疾病相關胃腸症狀的潛在效益 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數高（99.42%），機轉路徑（L-Arginine→nNOS→NO→胃平滑肌舒張）具清晰生物合理性，且 PMID 25057793 提供直接的動物機轉支持；然而，所有現有證據均停留於 L4 動物模型層次，缺乏人體臨床試驗驗證，目前不具備直接進入臨床應用的依據。

**若要推進需要：**
- 補齊 L-Arginine 完整的 MOA 資料（DrugBank API 查詢）
- 設計人體 Pilot 研究（Phase 1/2），確認 L-Arginine 口服/靜脈給藥對胃輕癱患者的安全性與療效
- 確認在胃輕癱適應症中的最適劑量與給藥途徑（口服 vs. 靜脈注射）
- 評估與現有胃輕癱標準治療（metoclopramide、domperidone）的藥物交互作用
- 查核 L-Arginine 在香港的法規狀態（是否以食品補充品形式流通，是否需另行申請藥品許可證）
- 補充 TFDA/衛生署仿單警語與禁忌症資料，完成正式安全性初評（S1 評估）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

