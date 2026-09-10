---
layout: default
title: Rotigotine
parent: 中證據等級 (L3-L4)
nav_order: 664
evidence_level: L4
indication_count: 5
---

# Rotigotine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Rotigotine：從帕金森氏症到注意力不足過動症 (ADHD)

## 一句話總結

Rotigotine 是一種泛多巴胺受體促效劑（作用於 D1–D5 受體），國際上用於帕金森氏症與不寧腿症候群治療，目前**未在香港上市**。TxGNN 模型預測其可能對**注意力不足過動症 (ADHD)** 有效，但目前**無臨床試驗**支持，僅有 3 篇文獻且機轉上存在矛盾，證據等級為 L4，建議 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 帕金森氏症、不寧腿症候群（依國際文獻記載；香港無核准適應症資料） |
| 預測新適應症 | 注意力不足過動症 (Attention Deficit-Hyperactivity Disorder) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 提供的詳細作用機轉資料。根據文獻（PMID 37221270, *Cell Research* 2023）記載，Rotigotine 是一種**泛多巴胺受體促效劑（pan-agonist）**，可同時活化 D1 至 D5 五種多巴胺受體亞型，臨床上核准用於帕金森氏症與不寧腿症候群。

然而，ADHD 的傳統藥理機轉是**抑制多巴胺再回收或促進其釋放**（如中樞興奮劑），而非直接的受體促效作用。作為全促效劑，Rotigotine 長期刺激受體反而可能導致**受體去敏感化**，這與 ADHD 治療所需的機轉方向並不一致。

現有的 3 篇支持文獻（PMID 18656214, 21476956, 34182128）主要聚焦於**兒童不寧腿症候群（RLS）**，而非直接針對 ADHD 進行研究；其關聯性僅來自「RLS 與 ADHD 在兒童族群中症狀重疊、常見共病」的間接推論，**並未提供 Rotigotine 治療 ADHD 的直接機轉或臨床證據**。此為此預測目前僅停留在 S0（假說產生階段）的主要原因。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Basic Science/Mechanistic | Pharmacological Research | α2A腎上腺素受體與 D4 多巴胺受體變異體異二聚體化，與 ADHD 之神經藥理連結探討 |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current Pharmaceutical Design | 兒童不寧腿症候群之藥物治療選項回顧，提及與 ADHD 症狀重疊 |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | 不寧腿症候群（RLS）綜述，描述 RLS 之臨床特徵 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **注意**：Evidence Pack 標示 TFDA 仿單警語/禁忌為 **Blocking 等級資料缺口 (DG001)**，在此缺口補齊前，本候選**無法進入 S1 安全性初評**。

---

## 其他候選適應症總覽

本次 Evidence Pack 共產生 5 個預測候選，除上述 ADHD 外，其餘皆判定為 Hold：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 主要考量 |
|-----|------|-----------|---------|---------|---------|
| 2 | Schizophrenia（精神分裂症） | 99.996% | L3 | S1 | 機轉矛盾：Rotigotine 為全促效劑，可能誘發/惡化精神病症狀（帕金森病人上市後已知安全性訊號），與陰性症狀假說所需的部分促效劑性質不符 |
| 3 | Polymicrogyria, perisylvian（罕見神經發育畸形症候群） | 99.995% | L5 | S0 | 無已知機轉關聯，零文獻/試驗支持，判定為運算假陽性 |
| 4 | Faciodigitogenital syndrome（Aarskog 症候群） | 99.995% | L5 | S0 | 病因為 FGD1/Rho GTPase 路徑，與多巴胺系統無關，判定為運算假陽性 |
| 5 | 先天性醣化異常（缺陷型岩藻糖基化） | 99.995% | L5 | S0 | 病因為醣基化酵素缺陷，與藥物機轉無關，判定為運算假陽性 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的 ADHD 候選缺乏直接臨床試驗與機轉證據，且全促效劑性質與 ADHD 傳統治療機轉方向相悖；排名第二的精神分裂症候選存在潛在安全性風險（可能誘發精神病症狀）；排名 3–5 為明顯的運算假陽性。
- TFDA/相關仿單安全性資料為 **Blocking 缺口**，在補齊前任一候選皆無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 Rotigotine 完整 MOA 資料（DrugBank API 查詢，DG002）
- 取得官方仿單警語與禁忌症資料（DG001，Blocking，須優先處理）
- 若欲推進 ADHD 方向，需針對 Rotigotine 是否引發受體去敏感化進行機轉研究，並釐清與傳統興奮劑機轉的相容性
- 若欲推進精神分裂症方向，需先排除全促效劑誘發精神病惡化的風險，並限定特殊族群（如僅陰性症狀且合併適當抗精神病藥物）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

