---
layout: default
title: Atezolizumab
parent: 高證據等級 (L1-L2)
nav_order: 67
evidence_level: L2
indication_count: 10
---

# Atezolizumab
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Atezolizumab：從尿路上皮癌到前列腺尿道尿路上皮癌

## 一句話總結

Atezolizumab（Tecentriq）是一種抗 PD-L1 單株抗體免疫治療藥物，已於全球多國核准用於尿路上皮癌、非小細胞肺癌等適應症，惟目前尚未在香港取得上市許可。TxGNN 模型預測它可能對**前列腺尿道尿路上皮癌 (Prostatic Urethra Urothelial Carcinoma)** 有效，並同時預測另外 9 個相關癌症亞型（含 1 個 L2 等級的子宮頸內口癌）。針對排名第一的適應症，目前有 **2 個臨床試驗**（含 1 個已完成的 Phase 2 試驗，n=172）支持此方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尿路上皮癌（全球核准；香港目前未登記） |
| 預測新適應症（Rank 1） | 前列腺尿道尿路上皮癌 (Prostatic Urethra Urothelial Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 登記數 | 0 張 |
| 建議決策 | **Proceed with Guardrails** |

---

## 為什麼這個預測合理？

目前 Evidence Pack 中缺乏正式的作用機轉（MOA）資料。根據已知資訊，Atezolizumab 是一種人源化 IgG1 抗 PD-L1 單株抗體，透過阻斷 PD-L1 與 T 細胞表面 PD-1 受體及 B7-1 的結合，解除腫瘤微環境對細胞毒性 T 細胞的抑制，從而恢復腫瘤浸潤性淋巴球（TIL）的抗腫瘤功能。其療效已由 IMvigor210（Phase 2）及 IMvigor211（Phase 3）等大型試驗於一般尿路上皮癌中得到驗證。

前列腺尿道尿路上皮癌（Prostatic Urethra Urothelial Carcinoma）與膀胱尿路上皮癌共享相同的組織學起源——均源自尿路上皮（移行上皮），且兩者的腫瘤免疫微環境高度相似：尿路上皮細胞高度表現 PD-L1，腫瘤浸潤性 T 細胞功能受到抑制。因此，在膀胱尿路上皮癌中已獲驗證的 PD-L1 抑制機轉，在機轉上可合理外推至前列腺尿道部位的相同組織學類型。

進一步支持此預測的是，NCT02844816 Phase 2 已完成試驗（n=172）於 BCG 無效的非肌肉侵犯性膀胱癌（NMIBC）中確認了 Atezolizumab 的療效；而大型 Phase 1b 試驗 NCT03170960 的入組族群明確涵蓋「尿路上皮癌（含膀胱、腎盂、輸尿管、尿道）」，提供直接跨解剖位點的安全性及初步療效數據，合計使此預測獲得 L2 等級證據支持。

---

## 臨床試驗證據

（針對 Rank 1 適應症：前列腺尿道尿路上皮癌）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | 已完成 | 172 | Atezolizumab 單藥用於 BCG 無效的復發/難治性 NMIBC；與前列腺尿道尿路上皮癌組織學類型相同，直接支持 PD-L1 抑制在尿路上皮癌的有效性 |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | 進行中（不再招募） | 914 | Cabozantinib 聯合 Atezolizumab 用於多種實體瘤；明確涵蓋尿路上皮癌（含膀胱、腎盂、輸尿管、尿道），提供跨解剖位點的安全性及初步療效資料 |

---

## 文獻證據

（針對 Rank 1 適應症：前列腺尿道尿路上皮癌）

目前無相關文獻登記。

---

## 香港上市資訊

Atezolizumab 目前在香港尚無任何上市許可登記，無相關許可證資料可供列示。如需參考，可查詢 Roche 原廠於歐盟（EMA）或美國（FDA）的核准仿單。

---

## 細胞毒性

Atezolizumab 為抗腫瘤免疫治療藥物（抗 PD-L1 單株抗體），適用細胞毒性評估如下：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療藥物（PD-L1 checkpoint inhibitor，非傳統細胞毒性藥物） |
| 骨髓抑制風險 | 低（主要毒性為免疫相關不良事件 irAE，而非骨髓抑制） |
| 致吐性分級 | 低 |
| 監測項目 | 肝腎功能（irAE 肝炎）、甲狀腺功能（甲狀腺炎）、血糖（免疫相關糖尿病）、CBC（免疫相關血液毒性）、腎上腺功能（免疫相關腎上腺功能不全） |
| 處置防護 | 依單株抗體靜脈輸注標準規範操作，無需細胞毒性藥物特殊防護措施；需備妥輸液反應處理流程 |

---

## 安全性考量

安全性資訊請參考原廠仿單（Roche/Genentech Tecentriq）。

---

## 所有預測適應症摘要（Top 10）

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 | 支持試驗數 | 支持文獻數 |
|------|--------|-----------|---------|---------|-----------|-----------|
| 1 | 前列腺尿道尿路上皮癌 | 99.98% | L2 | **Proceed with Guardrails** | 2 | 0 |
| 2 | 腎盂肉瘤樣移行細胞癌 | 99.98% | L4 | Research Question | 0 | 0 |
| 3 | 浸潤性膀胱尿路上皮癌（肉瘤樣亞型） | 99.98% | L4 | Research Question | 0 | 0 |
| 4 | 腎盂乳頭狀尿路上皮癌 | 99.98% | L3 | Research Question | 1 | 0 |
| 5 | 子宮韌帶腺癌 | 99.93% | L5 | Hold | 0 | 0 |
| 6 | 子宮頸內口癌 | 99.92% | **L2** | **Proceed with Guardrails** | 2 | 1 |
| 7 | 子宮頸腺樣囊性癌 | 99.92% | L5 | Hold | 0 | 0 |
| 8 | 子宮韌帶漿液性腺癌 | 99.92% | L5 | Hold | 0 | 0 |
| 9 | 子宮頸黏液腺癌（印戒細胞亞型） | 99.91% | L5 | Hold | 0 | 0 |
| 10 | 子宮頸黏液腺癌（腸型亞型） | 99.91% | L5 | Hold | 0 | 0 |

> **⚠️ 特別注意**：排名第 6 的**子宮頸內口癌**同樣達到 L2 等級，有 2 個 Phase 1/2 已完成臨床試驗（[NCT02921269](https://clinicaltrials.gov/study/NCT02921269) Phase 2 n=11；[NCT03738228](https://clinicaltrials.gov/study/NCT03738228) Phase 1 n=40），以及 1 篇 2023 年子宮頸小細胞神經內分泌癌綜述文獻（[PMID 37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/)），建議列為次優先跟進目標。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
前列腺尿道尿路上皮癌與膀胱尿路上皮癌具有相同的組織學起源及高度相似的 PD-L1 免疫微環境，已完成的 Phase 2 試驗（NCT02844816，n=172）及 IMvigor210/211 系列數據提供充分的外推依據；同時，大型 Phase 1b（NCT03170960）明確涵蓋尿道在內的泌尿道上皮癌族群，機轉關聯性高且有直接臨床支持。

**若要推進需要：**

- 取得原廠完整仿單（包含 irAE 管理指引、劑量調整標準），補足安全性資料缺口（DG001）
- 查詢 DrugBank API 確認正式 MOA 記錄（DG002）
- 向香港衛生署藥物辦事處評估臨床試驗授權申請（Atezolizumab 目前香港未登記）
- 建立前列腺尿道尿路上皮癌亞型的 PD-L1 免疫組化表現基礎資料（生物標記篩選計畫）
- 設計以此特定部位為主要終點的 Phase 2 研究（或考慮以「泌尿道尿路上皮癌」為 Basket Trial 傘型設計涵蓋此亞型）
- 同步評估 **子宮頸內口癌**（Rank 6，L2）作為次優先適應症，NCT02921269 已完成試驗可提供早期定性參考

---

> **免責聲明**：本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過完整臨床驗證才能應用於實際治療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

