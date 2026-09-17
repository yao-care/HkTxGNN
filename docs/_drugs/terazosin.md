---
layout: default
title: Terazosin
parent: 僅模型預測 (L5)
nav_order: 733
evidence_level: L5
indication_count: 5
---

# Terazosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Terazosin：原適應症資料缺失，TxGNN 預測多項脱髮／偏頭痛適應症

## 一句話總結

Terazosin（DB01162）在本 Evidence Pack 中**缺乏正式原適應症與 MOA 記錄**，香港亦**未上市**。根據預測理由文字，此藥為 α1 腎上腺素受體拮抗劑／血管擴張劑。TxGNN 模型針對此藥產生 **5 項預測適應症**，其中 3 項（先天性稀毛症、先天性稀毛伴粟粒疹、瀰漫性圓形禿）**完全無文獻或試驗佐證**（L5），另 2 項——**脱髮 (alopecia)** 與**偏頭痛 (migraine disorder)**——各有 1-2 篇文獻支持，證據等級分別為 L4 與 L3。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供，香港無許可證記錄） |
| TxGNN 分數最高的預測適應症 | Hypotrichosis simplex of the scalp（先天性頭皮稀毛症） |
| TxGNN 預測分數 | 99.97% |
| 證據等級（最高分候選） | L5（純模型預測，無任何試驗/文獻） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold**（因 TFDA 仿單警語資料為 Blocking 缺口） |

### 五項預測候選比較

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Hypotrichosis simplex of the scalp | 99.97% | L5 | S0 | Hold |
| 2 | Congenital hypotrichosis milia | 99.97% | L5 | S0 | Hold |
| 3 | Diffuse alopecia areata | 99.96% | L5 | S0 | Hold |
| 4 | Alopecia | 99.95% | L4 | S1 | Research Question |
| 5 | Migraine disorder | 99.92% | L3 | S1 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉（MOA）資料。根據 Evidence Pack 中各候選的 `repurposing_rationale`，Terazosin 被描述為 **α1 腎上腺素受體拮抗劑**，具**血管擴張**作用。

**脱髮相關候選（排名 1-4）**：其中排名 1、2、3 三項（先天性稀毛症、先天性稀毛伴粟粒疹、瀰漫性圓形禿）皆屬**遺傳性或自體免疫性**病因（如 APCDD1、LPAR6 基因突變，或 T 細胞介導的毛囊發炎），與血管擴張機轉**無直接病理生理對應**，僅為模型基於嵌入相似性的推論，無任何實證支持。相對地，排名 4 的一般性「Alopecia」則有間接的藥理類比證據——已知同為血管擴張劑的 minoxidil 具誘發毛髮生長的 class effect，2022 年一篇綜述文獻即以此類比說明心血管用藥的「跨適應症」效果，但該文獻並非針對 terazosin 的直接研究。

**偏頭痛（排名 5）**：證據強度相對最高。偏頭痛的血管理論認為顱內外血管異常擴張/收縮參與致病機轉，α1 拮抗劑理論上可調節血管張力達到預防效果。更重要的是，1994 年已有一項小型臨床研究**直接測試** terazosin 於無預兆偏頭痛患者，1997 年另有綜述文獻討論 α1 阻斷劑於偏頭痛預防的角色——顯示這並非單純模型幻想，而是曾被實際探索過的研究方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記（5 項預測適應症皆無 ClinicalTrials.gov 或 ICTRP 資料）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 對應預測適應症 | 主要發現 |
|------|-----|------|------|----------------|---------|
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | 小型臨床試驗（原始研究） | La Clinica terapeutica | Migraine disorder | 46 名無預兆偏頭痛患者分組使用 terazosin/buflomedil，評估預防性療效 |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review | Headache | Migraine disorder | 10 名偏頭痛患者使用 terazosin 或 doxazosin，多數頻率/嚴重度下降，但 5 人因副作用停藥 |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Review | Current Cardiology Reviews | Alopecia | 綜述心血管用藥的心臟外效應，以 minoxidil 誘發多毛症為例說明「附加治療效果」的概念 |

其餘 3 項預測適應症（先天性稀毛症、先天性稀毛伴粟粒疹、瀰漫性圓形禿）目前無相關文獻。

---

## 香港上市資訊

Terazosin 目前**未在香港上市**，無任何許可證記錄（`total_licenses: 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 需特別注意：本案 TFDA／香港仿單警語與禁忌症資料為 **Blocking 級別缺口**，在補齊前無法進行 S1 安全性初評，這也是本報告整體決策為 Hold 的主要原因。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名前 3 的預測適應症（脱髮相關遺傳性疾病）機轉上與 terazosin 的血管擴張作用無合理對應，僅為 L5 模型預測，不建議進一步投入。
- 「Alopecia」與「Migraine disorder」雖有文獻支持且達到 S1 研究問題階段，具備後續探索價值，但**仿單安全性資料（DG001，Blocking）與 MOA 資料（DG002，High）雙重缺口**，使整體案件在藥師/法規層面尚無法推進至下一階段。

**若要推進需要：**
- 補齊 TFDA／原廠仿單警語與禁忌症資料（DG001，來源：TFDA 官網，解析仿單 PDF）
- 補齊 DrugBank 作用機轉資料以支持機轉關聯性分析（DG002）
- 若聚焦 Migraine 或 Alopecia 方向，建議進一步檢索是否有更新、更大規模的隨機對照試驗（現有文獻均為 1990 年代小型研究或綜述）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

