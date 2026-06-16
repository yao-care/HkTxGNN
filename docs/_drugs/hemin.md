---
layout: default
title: Hemin
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Hemin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Hemin：從急性肝性紫質症到血小板減少性紫癜

## 一句話總結

Hemin 是外源性血紅素（heme）製劑，臨床上已知用於急性肝性紫質症（AHP）發作的緊急治療，透過抑制 ALAS1 負回饋機制減少毒性卟啉前驅物蓄積。TxGNN 模型在 10 個血液凝固相關疾病中預測其再利用潛力，信心最高為**血小板減少性紫癜 (Thrombocytopenic Purpura)**（分數 99.79%）；然而所有預測適應症中，**血友病（Rank 2）** 為唯一具有機轉關聯性前驅研究支持者（**1 篇動物研究**），其餘 9 個適應症均僅有模型預測，無實際研究支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性肝性紫質症（急性卟啉症發作，依已知臨床用途推斷） |
| 預測新適應症（Rank 1）| 血小板減少性紫癜 (Thrombocytopenic Purpura) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap）。根據文獻脈絡可知，Hemin 是外源性血紅素鐵卟啉製劑，靜脈注射後可透過負回饋抑制 δ-胺基乙醯丙酸合成酶 1（ALAS1），阻斷卟啉合成路徑；同時，Hemin 亦為血紅素氧合酶-1（HO-1）的已知誘導劑，HO-1 活化後產生一氧化碳（CO）與膽紅素，具有抗炎及免疫調節特性。

血小板減少性紫癜（ITP/TTP）的核心病理為免疫媒介性或微血管病性血小板破壞（IgG 自體抗體攻擊血小板、或 ADAMTS13 缺乏導致 vWF 多聚體積聚）。雖然 HO-1 理論上具有抗炎效果，但其與上述血小板破壞機轉之間並無已知直接分子連結，機轉假說為高度推測性。

TxGNN 對此疾病的高分預測（0.998）推測源於知識圖譜中血液疾病節點的拓撲聚類效應，而非真實的生物學機轉關聯。相比之下，Rank 2 的**血友病**具有更直接的機轉依據：前驅動物研究（PMID 19890094）顯示，HO-1 誘導可在 FVIII 缺乏小鼠中顯著降低抗 FVIII 抑制性抗體的生成，而 Hemin 正是 HO-1 的誘導劑，此假說具有初步生物學支撐。

---

## 臨床試驗證據

目前無相關臨床試驗登記（針對血小板減少性紫癜）。

---

## 文獻證據

目前無相關文獻（針對血小板減少性紫癜）。

> **補充說明（Rank 2：血友病）**
> 在全部 10 個預測適應症中，血友病為唯一具有機轉關聯性研究的適應症。以下 1 篇直接相關的前驅研究已識別（其餘 3 篇文獻為 givosiran/AIP 研究，屬錯誤匹配，不納入計分）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [19890094](https://pubmed.ncbi.nlm.nih.gov/19890094/) | 2010 | 前驅動物研究（小鼠模型）| Blood | HO-1 誘導在 FVIII 缺乏小鼠中顯著降低抗 FVIII 抑制性抗體（inhibitor）生成；Hemin 為已知 HO-1 誘導劑，提供「Hemin → HO-1 → 免疫耐受」假說的初步依據 |

---

## 香港上市資訊

Hemin 目前在香港**未上市**，查無任何藥品許可證登記。如需取得藥品，須透過特殊進口或恩慈使用（compassionate use）管道申請。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 所有預測適應症彙整

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 機轉依據 | 決策 |
|------|------|-----------|---------|---------|------|
| 1 | 血小板減少性紫癜 (Thrombocytopenic Purpura) | 99.79% | L5 | 無直接機轉連結，疑為圖譜拓撲效應 | Hold |
| **2** | **血友病 (Hemophilia)** | **99.72%** | **L4** | **HO-1 誘導降低 FVIII 抑制劑（小鼠模型）** | **Research Question** |
| 3 | C1 抑制劑缺乏 (C1 Inhibitor Deficiency) | 99.70% | L5 | 無生物學依據，疑為 serpin 家族拓撲效應 | Hold |
| 4 | 後天性凝血因子缺乏 (Acquired Coagulation Factor Deficiency) | 99.65% | L5 | 極度間接推論（HO-1 → 肝細胞保護） | Hold |
| 5 | 毒性 Serpin 聚合症 (Serpinopathy) | 99.64% | L5 | 高度推測性，疑為 C1Inh 拓撲關聯 | Hold |
| 6 | C1Inh 缺乏型遺傳性血管水腫 (HAE with C1Inh Deficiency) | 99.48% | L5 | 對激肽系統無已知調節作用 | Hold |
| 7 | 遺傳性血栓症 (Inherited Thrombophilia) | 99.45% | L5 | CO 抗血小板路徑極度間接，無驗證研究 | Hold |
| 8 | 女性帶因者症狀性血友病 (Symptomatic Hemophilia in Female Carriers) | 99.37% | L5 | 無針對此亞型的研究，L5 維持 | Hold |
| 9 | 遺傳性 von Willebrand 病 (Hereditary vWD) | 99.30% | L5 | HO-1 對 vWF 表達的影響無文獻支持 | Hold |
| 10 | 先天性 XI 因子缺乏 (Congenital Factor XI Deficiency) | 99.19% | L5 | 對 FXI 無已知機轉連結，疑為凝血疾病群拓撲聚類 | Hold |

---

## 結論與下一步

**決策：Hold（Rank 1 主要預測適應症）**

**理由：**
血小板減少性紫癜缺乏任何臨床試驗或文獻支持，TxGNN 高分預測可能源於血液疾病知識圖譜的拓撲聚類效應，而非真實的機轉關聯。香港目前未上市、作用機轉資料缺失（MOA Data Gap）、安全性資料全數缺失，無法通過 S1 安全性初評門檻。

**潛力最高方向（建議優先深入評估）：血友病 A（Rank 2）**
- 具有唯一直接機轉連結：HO-1 誘導 → 降低 FVIII 抑制性抗體（PMID 19890094，Blood, 2010）
- 假說清晰：「Hemin 作為 HO-1 誘導劑，可能在血友病 A 患者接受凝血因子替代治療時降低免疫排斥風險」
- 目前僅限小鼠模型，尚無人體資料

**若要推進血友病方向，需要：**
1. 取得 Hemin 完整 MOA 資料（查詢 DrugBank API，修復 DG002）
2. 下載原廠仿單並解析警語/禁忌（修復 DG001，解除 Blocking 狀態）
3. 評估香港或其他地區的 Hemin 藥品可及性（compassionate use / 特殊進口）
4. 設計驗證性前驅研究：人類 PBMC 體外模型或非人靈長類模型中驗證 Hemin 的 HO-1 誘導效應對 FVIII 抑制劑的影響
5. 進行完整的 DDI 評估（與現行血友病治療藥物的交互作用）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

