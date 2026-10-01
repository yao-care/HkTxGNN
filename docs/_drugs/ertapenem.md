---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ertapenem：從廣效碳青黴烯類抗生素到細菌性關節炎

## 一句話總結

Ertapenem 是一種廣效碳青黴烯類（carbapenem）注射抗生素，在香港已有 4 張許可證。
TxGNN 模型預測它可能對**細菌性關節炎 (Bacterial Arthritis)** 有效。
目前**沒有直接相關的臨床試驗**，文獻有 **10 篇**，多為單一病例報告與間接資料，證據偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 細菌性關節炎 (Bacterial Arthritis) |
| TxGNN 預測分數 | 99.72% |
| 證據等級 | L3（僅有觀察性研究與病例報告，且多為間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ertapenem 是廣效碳青黴烯類抗生素，對多種腸內菌科細菌（Enterobacterales，包含產 ESBL 菌株）與厭氧菌有活性。

細菌性關節炎屬於細菌感染，致病菌常包含上述細菌。從抗菌譜來看，Ertapenem 用於這類關節感染有合理的藥理基礎。文獻中的個案也支持這個方向，例如肺炎克雷伯氏菌（*Klebsiella pneumoniae*）與 *Prevotella bivia* 引起的化膿性關節炎。

不過 TxGNN 分數只是知識圖譜的預測，不是臨床證據。現有文獻多為個案報告與回溯性資料，尚未證明 Ertapenem 對細菌性關節炎的療效與最佳用法。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | 世代研究 | Antimicrob Agents Chemother | 回溯分析 306 名門診接受 Ertapenem 治療的成人，適應症以腹腔內感染最多，也包含骨與關節感染，探討長期門診治療的安全性與療效 |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | 世代研究 | J Antimicrob Chemother | 10 名骨與關節感染患者以皮下注射 β-lactam 作長期抑制性治療，評估安全性與結果（非專指 Ertapenem） |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | 世代研究 | J Antimicrob Chemother | 評估 Temocillin 對第三代頭孢菌素抗藥腸內菌科所致骨關節感染的體外活性，作為碳青黴烯類的可能替代（非 Ertapenem 研究） |
| [29183082](https://pubmed.ncbi.nlm.nih.gov/29183082/) | 2017 | 回顧 | JAMA | 化膿性汗腺炎的診斷與治療進展，與細菌性關節炎關聯低 |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | 病例報告 | J Chemother | 肺炎克雷伯氏菌所致腕關節化膿性關節炎，以 Ertapenem 加 Levofloxacin 治療成功 |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | 病例報告 | BMJ Case Rep | 糖尿病足合併 *Citrobacter koseri* 骨髓炎與化膿性關節炎，以 Ertapenem 治療成功 |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | 病例報告 | J Investig Med High Impact Case Rep | 免疫功能正常成人的 *Prevotella bivia* 化膿性關節炎，附文獻回顧 |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | 病例報告 | Anaerobe | 首例 *Clostridium paraputrificum* 肩關節化膿性關節炎合併骨髓炎，附文獻回顧 |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | 體外研究 | Diagn Microbiol Infect Dis | Auranofin 可恢復 Ertapenem 對碳青黴烯抗藥大腸桿菌的敏感性（非關節感染） |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | 流行病學 | Clin Lab | 分析 4 歲以下兒童骨關節感染的病原菌分布與抗藥性 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51101 | INVANZ FOR INJ 1G | MERCK SHARP & DOHME (ASIA) LTD |
| HK-64357 | CSPC-ETA ERTAPENEM POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION OR INJECTION 1G | JINDUN PHARMA (H.K.) LIMITED |
| HK-68079 | ERTAPENEM KABI POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1G | FRESENIUS KABI HONG KONG LIMITED |
| HK-68815 | ERTEMILL POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION/INJECTION 1G | CHEMILL PHARMA LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 細菌性關節炎沒有任何臨床試驗，文獻僅有個案報告與間接資料，無法支持推進。
- 香港衛生署仿單的警語與禁忌資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症。
- 補充作用機轉資料（例如查詢 DrugBank）。
- 系統性搜尋 Ertapenem 治療骨關節感染的回溯性研究，並確認關節腔穿透性與劑量。
- 評估是否有前瞻性研究或試驗可以進一步驗證。

**補充：** 同一份資料中，第二順位預測「金黃色葡萄球菌感染」的證據較強。該項有多篇 Cefazolin 加 Ertapenem 治療持續性 MSSA 菌血症的病例系列與世代研究，另有 1 項進行中的 Phase 2 試驗（NCT04886284）。若要優先評估，可考慮改以該適應症作為切入點。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

