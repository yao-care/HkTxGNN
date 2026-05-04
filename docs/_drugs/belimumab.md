---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Belimumab：從系統性紅斑狼瘡 (SLE) 到血小板原發性釋放障礙

## 一句話總結

Belimumab 是一種人類化單株抗體，透過抑制 BLyS/BAFF 信號調節 B 細胞活性，已於多國核准用於系統性紅斑狼瘡（SLE）治療，但香港目前尚無上市許可。
TxGNN 模型預測它可能對**血小板原發性釋放障礙 (Primary Release Disorder of Platelets)** 有效（預測分數 99.96%），
然而唯一登記的臨床試驗與本適應症完全無關，且無任何文獻支持，機轉連結缺乏直接依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 系統性紅斑狼瘡（SLE）（香港未上市，依藥理背景知識填入） |
| 預測新適應症 | 血小板原發性釋放障礙 (Primary Release Disorder of Platelets) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Belimumab 是一種人類化 IgG1λ 單株抗體，透過結合可溶性 BLyS（B 淋巴細胞刺激因子，又稱 BAFF），阻斷其與 B 細胞表面受體（BAFF-R、BCMA、TACI）的結合，從而減少自體反應性 B 細胞的存活與分化，最終降低致病性自體抗體（如 anti-dsDNA）的產生。需注意：本 Evidence Pack 中作用機轉欄位標記為資料缺失，以上說明來自藥理學背景知識，尚待 DrugBank API 查詢補充確認。

就血小板原發性釋放障礙而言，此類疾病涉及血小板 α 顆粒或 dense 顆粒的分泌缺陷（如 Gray platelet syndrome、Delta storage pool disease），**病理基礎主要為功能性或遺傳性缺陷，並非自體免疫機制所主導**。Belimumab 的 B 細胞靶向機轉對此類缺陷無直接靶向理論基礎。Evidence Pack 的機轉評估亦明確指出：TxGNN 知識圖譜的高預測分數（99.96%），極可能源於圖譜中血小板相關疾病節點的群聚效應（node clustering），而非真實的藥物–疾病因果關係。

值得一提的是，本批次六個預測中，機轉最具合理性者為第 4 名的**胎兒及新生兒同種免疫性血小板減少症（FNAIT）**：其病理為母體 B 細胞產生抗胎兒血小板抗原（主要為 anti-HPA-1a）之 IgG 同種抗體，屬 alloimmune 機制，與 BLyS 抑制降低自體抗體的藥理機制最為相近。然而，Belimumab 在妊娠期間的安全性顧慮（FDA 妊娠分類 C，臨床試驗明確排除孕婦）使其臨床可行性受到嚴重限制，且目前完全無 FNAIT 相關臨床或前臨床資料。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | 已完成 | 14 | ⚠️ **適應症不符**：此試驗研究 Belimumab 用於抗 PLA2R 自體抗體陽性之特發性膜性腎小球腎病變（IMGN），評估療效、安全性與作用機轉，與血小板釋放障礙完全無關。此試驗屬資料收集誤匹配，不應計入本適應症之支持性證據。 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Belimumab 在香港目前尚無上市許可，無任何許可證記錄。如需進一步評估，需先取得香港衞生署藥物辦公室的相關審查資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充注意：本 Evidence Pack 安全性欄位（主要警語、禁忌症、藥物交互作用）均為資料缺失狀態，需另行查詢 TFDA 仿單 PDF 或 DrugBank API 補充。Belimumab 為生物製劑，一般已知安全考量包含感染風險升高（尤其是機會性感染）、過敏反應、抑鬱/自殺意念風險，以及妊娠安全性限制，但上述資訊尚未由本 Evidence Pack 核實。

---

## 結論與下一步

**決策：Hold**

**理由：**
血小板原發性釋放障礙為功能性/遺傳性疾病，非自體免疫機制主導，Belimumab 的 BLyS 抑制機轉缺乏直接靶向依據；唯一登記的臨床試驗與本適應症完全不相關（腎臟病適應症），無任何文獻支持，整體證據等級僅 L5，不具推進條件。

**若要推進需要：**
- 補全藥物基本資料：查詢 DrugBank API 取得完整 MOA 及安全性分類
- 補全安全性資料：下載原廠仿單 PDF，解析警語與禁忌
- 重新評估本批次預測：優先探索機轉較合理的 FNAIT（第 4 名）適應症，需先解決妊娠期安全性問題或改以非孕期預防性治療策略為研究框架
- 執行 FNAIT 前臨床驗證：設計 BLyS 抑制對母體同種抗體滴度影響的動物模型實驗，再考慮是否進入臨床研究階段
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

