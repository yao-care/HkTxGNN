---
layout: default
title: Dolutegravir
parent: 中證據等級 (L3-L4)
nav_order: 212
evidence_level: L3
indication_count: 3
---

# Dolutegravir
{: .fs-9 }

證據等級: **L3** | 預測適應症: **3** 個
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

# Dolutegravir：從 HIV-1 感染到猴免疫缺陷病毒感染

## 一句話總結

Dolutegravir 是第二代整合酶鏈轉移抑制劑（INSTI），全球廣泛用於 HIV-1 感染治療，但目前香港尚未核准上市。
TxGNN 模型預測它可能對**猴免疫缺陷病毒感染（Simian Immunodeficiency Virus Infection，SIV）** 有效，
目前有 **1 個臨床試驗**和 **15 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（全球已核准；香港未上市） |
| 預測新適應症 | 猴免疫缺陷病毒感染（Simian Immunodeficiency Virus Infection） |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Dolutegravir 是整合酶鏈轉移抑制劑（INSTI）。其作用靶點為病毒整合酶的 D,D-35-E 催化三聯體（DDE motif）——藥物的 DKA 藥效團（diketo acid pharmacophore）與整合酶催化位點的二價金屬離子配位，阻止病毒 cDNA 整合入宿主細胞染色體，從根本上截斷病毒複製週期。

SIV（猴免疫缺陷病毒）與 HIV-1 同屬靈長類慢病毒（Lentivirus），兩者整合酶序列相似度超過 60%，DDE 催化三聯體高度保守。多篇動物研究直接證明 Dolutegravir 可有效抑制 SIV（包括 SIVmac239、SIVcpz、SIVmac251）複製，在非人類靈長類（NHP）模型中達到病毒學抑制，其耐藥突變模式（如 R263K）也與 HIV-1 高度平行，支持分子機轉上的預測合理性。

然而需注意一個重要前提：**SIV 感染是非人類疾病**，主要用於 HIV 研究的動物模型。此預測的臨床轉譯意義在於 Dolutegravir 可作為 SIV NHP 模型中標準 cART 方案的核心藥物，推進 HIV 治癒策略的基礎研究；而非傳統意義上面向人體的藥物再利用。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | 未知 | 12 | Vedolizumab 合併 ART（含 DTG）用於 HIV 感染初治者，探索停藥後持續病毒緩解可能性；主研究藥物為 Vedolizumab，DTG 作為背景 ART 成分；研究對象為 HIV 患者，非直接 SIV 試驗，樣本數極小 |

> **注意**：目前無直接針對 SIV 感染（動物或獸醫）的登記臨床試驗。上列試驗研究對象為 HIV 感染人類，屬間接相關，可信度有限（狀態 UNKNOWN，n=12）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | 動物研究（NHP） | Journal of Virology | DTG 單藥治療 SIV 感染獼猴，選擇性產生 R263K 等多種耐藥突變模式，病毒學結果具多樣性，凸顯單藥治療局限 |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | 體外＋動物研究 | Journal of Virology | 全面表徵 DTG 等 INSTI 在 SIVmac239 的耐藥譜，確認 SIV 對 INSTI 具敏感性，耐藥突變模式與 HIV 高度平行 |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | 縱貫動物研究 | Pharmaceutics | 藥代動力學驗證 SIVmac251 感染 NHP 的長期 ART（含 TDF/FTC/DTG）模型，確認 DTG 在非人靈長類的有效藥效 |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | 動物研究 | AIDS Res Hum Retroviruses | 評估含 DTG 的新型注射 cART 方案在 SIVmac239 感染獼猴的療效，達到臨床相關病毒抑制水平 |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | 結構生物學／回顧 | FEBS Journal | HIV/SIV 整合酶複合體晶體結構闡明 INSTI 結合機制及病毒逃逸路徑，解釋 DTG 高耐藥屏障的分子基礎 |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | 個案報告（動物） | Retrovirology | SIVcpz 誘發圈養黑猩猩 AIDS 樣免疫缺陷，採含 DTG 的 ART 方案成功實現病毒抑制，為首例個案記錄 |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | 動物研究（CNS） | mBio | 即使在含 DTG 的 ART 有效抑制下，HIV/SIV 病毒仍在腦組織持續存在，揭示 CNS 病毒庫清除的瓶頸 |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | 動物研究（CNS） | Frontiers in Immunology | SIV 感染獼猴啟動含 DTG 的 cART 前後腦白質及細胞外自由水分布變化分析，評估早期 CNS 損傷修復 |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | 體外／安全性研究 | Clin Infect Dis | DTG 與 raltegravir 在人類／猿猴脂肪組織引發促脂肪生成、促纖維化效應及胰島素阻抗（安全性警訊） |
| [31619550](https://pubmed.ncbi.nlm.nih.gov/31619550/) | 2019 | 體外研究 | Journal of Virology | ART（含 DTG）抑制的 SIV 感染獼猴中，Wnt/β-catenin 訊號調控長效記憶 CD4+ T 細胞增殖及病毒庫維持 |

---

## 香港上市資訊

Dolutegravir 目前在香港**未取得藥品許可證**，無本地上市資料可查。

> **參考資訊**：在全球主要市場，Dolutegravir 已獲廣泛核准用於 HIV-1 感染治療（品牌：Tivicay®；複方製劑：Triumeq®、Dovato® 等），如需安全性及適應症完整資訊，請查閱美國 FDA 或歐盟 EMA 核准仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **補充提示**：雖然本 Evidence Pack 缺乏本地安全性資料，但根據 Dolutegravir 全球上市後記錄，以下事項值得關注：
> - **孕期暴露風險**：Botswana Tsepamo 研究（2018）報告孕期使用 DTG 與神經管缺陷風險增加的關聯，目前各地指引已更新
> - **體重增加**：INSTI 類藥物（尤其 DTG）與體重增加及代謝影響有關（詳見 PMID 32166319）
> - **藥物交互作用**：與 CYP3A 強效誘導劑（如利福平）合用需調整劑量

---

## 結論與下一步

**決策：Hold**

**理由：**
SIV 感染是非人類疾病，主要應用場景為 HIV 研究的動物模型工具，而非傳統人體新適應症。動物研究（NHP）直接支持 DTG 在 SIV 模型的療效，機轉合理，但臨床轉譯路徑不明確；加之香港無上市基礎，直接推進本地臨床申請不具可行性，應先釐清再利用目標的性質。

**若要推進需要：**
- **明確再利用目標的性質**：
  - 若目標為 **HIV 治癒基礎研究工具**（SIV NHP 模型標準 ART）→ 可直接採購全球核准製劑用於研究用途，無需本地再利用申請
  - 若目標為 **獸醫臨床適應症**（保育靈長類 SIV 治療）→ 需循獸醫用藥申請路徑，與野生動物保育機構合作
- 補充 Dolutegravir 完整 MOA 資料（DrugBank API 查詢，目前為 Data Gap）
- 補充香港/台灣本地藥物相互作用及特殊族群安全性資料
- 若考慮擴展至其他人體適應症，需重新評估排名 1 以外的預測候選（本報告聚焦於 SIV 感染，其餘候選如 FIV 感染及神經發育疾病均建議 Hold）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

