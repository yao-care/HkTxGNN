---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 5
---

# Gefitinib
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

# Gefitinib：從非小細胞肺癌到齦纖維瘤病

## 一句話總結

Gefitinib 是第一代 **EGFR 酪胺酸激酶抑制劑（TKI）**，全球已核准用於 EGFR 突變型非小細胞肺癌（NSCLC）一線治療，惟香港藥監系統目前無許可證登記資料。
TxGNN 模型在本次多適應症評估中，預測分數最高者為**齦纖維瘤病（Fibromatosis, Gingival）**（99.89%），
然而此適應症**無任何臨床試驗或文獻支持**；5 個預測適應症中，最具臨床潛力者為**肺門癌（Lung Hilum Carcinoma，L3）**，有個案報告佐證。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | EGFR 突變型非小細胞肺癌（依全球核准適應症；香港藥監系統資料缺乏） |
| 預測新適應症（排名第 1） | 齦纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市（依現有資料） |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉（MOA）資料。根據已知資訊，Gefitinib 是 EGFR 酪胺酸激酶的選擇性抑制劑，透過競爭性佔據 EGFR 胞內區 ATP 結合位點，阻斷下游 RAS-RAF-MEK 及 PI3K-AKT 腫瘤增殖訊號通路，在 EGFR 驅動型惡性腫瘤（尤其是 Exon 19 缺失 / Exon 21 L858R 突變型 NSCLC）中有充分的機轉依據。

齦纖維瘤病（Gingival Fibromatosis）為良性遺傳性疾病，病理機轉主要涉及 SOS1、CTNNB1 等基因突變導致的纖維母細胞過度增生，EGFR 訊號軸**並非此病症的主要驅動因素**。由於病變屬良性非惡性增生，與 Gefitinib 的靶向 EGFR 機轉缺乏明確關聯，機轉合理性薄弱。

此預測屬 TxGNN 模型純推導結果，目前缺乏前臨床研究、臨床試驗及直接文獻佐證，暫不建議推進。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 細胞毒性

Gefitinib 屬抗腫瘤標靶藥物（核准適應症為 EGFR 突變型 NSCLC），納入細胞毒性評估。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（第一代 EGFR 酪胺酸激酶抑制劑；非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 低（較傳統化療顯著降低；偶見輕度白血球或血小板變化） |
| 致吐性分級 | 低 |
| 監測項目 | 肝功能（ALT、AST、膽紅素）、間質性肺炎（ILD）早期症狀（呼吸困難、乾咳、發燒）、皮膚毒性（痤瘡樣皮疹、甲溝炎）、腹瀉嚴重度 |
| 處置防護 | 依抗腫瘤藥物處置規範操作；若出現 ILD 症狀應立即停藥並緊急評估 |

---

## 安全性考量

安全性資訊請參考原廠仿單（Iressa® Prescribing Information）。

---

## 全部預測適應症總覽

本次共評估 5 個預測適應症，摘要如下：

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗 | 文獻 | 證據等級 | 建議決策 |
|------|-------|-----------|---------|------|---------|---------|
| 1 | 齦纖維瘤病 (Fibromatosis, Gingival) | 99.89% | 0 | 0 | L5 | Hold |
| 2 | 肺纖維瘤 (Fibroma of Lung) | 99.86% | 0 | 0 | L5 | Hold |
| 3 | IBMPFD／額顳葉失智症 | 99.86% | 0 | 20 † | L5 | Hold |
| 4 | 肺錯構瘤 (Hamartoma of Lung) | 99.86% | 0 | 0 | L5 | Hold |
| **5** | **肺門癌 (Lung Hilum Carcinoma)** | **99.86%** | **0** | **1** | **L3** | **Proceed with Guardrails** |

† 20 篇文獻均為 FTD 一般性綜述，無一直接涉及 Gefitinib 於 IBMPFD 的應用。

### 最具臨床潛力：肺門癌（Rank 5）

肺門癌（Lung Hilum Carcinoma）為 NSCLC 的中央型解剖亞型，本質屬非小細胞肺癌，與 Gefitinib 的 EGFR 機轉**完全對應**。現有個案報告（[PMID 22688581](https://pubmed.ncbi.nlm.nih.gov/22688581/)，2012，General Thoracic and Cardiovascular Surgery）描述一名 EGFR 突變型肺腺癌患者（cT4N1M1a，含大量肺門淋巴結轉移、肋膜播散）接受 Gefitinib 治療後達到部分緩解，並成功進行補救性手術，直接支持此適應症的可行性。

> **說明**：此適應症本質上屬 Gefitinib 已建立用途的解剖位置延伸應用，而非嚴格意義的藥物再利用（drug repurposing）。證據等級 L3 反映搜尋詞使用特定解剖術語所致，並非真實臨床證據不足。建議以「EGFR mutant NSCLC」或「non-small cell lung cancer gefitinib」重新搜尋，可取得多項 Phase 3 RCT 支持（如 IPASS、WJTOG3405、NEJ002 等）。

### 值得關注的假說：IBMPFD／額顳葉失智症（Rank 3）

IBMPFD（VCP 基因突變）導致蛋白酶體／自噬通路障礙。文獻（[PMID 35039149](https://pubmed.ncbi.nlm.nih.gov/35039149/)，Trends in Pharmacological Sciences, 2022）顯示 progranulin（GRN 基因）與 EGFR 配體（EGF、HB-EGF）存在交互調控關係，progranulin 缺乏（FTD-GRN 型）可能影響 EGFR 訊號平衡，EGFR TKI 是否能透過調控自噬流改善 IBMPFD 病程屬潛在假說。目前 20 篇文獻均為 FTD 一般性綜述，此路徑需細胞及動物實驗驗證方可進入 S1 評估。

---

## 結論與下一步

**主要預測適應症（齦纖維瘤病）決策：Hold**

**理由：**
TxGNN 分數最高的預測適應症在機轉上缺乏合理性（非 EGFR 驅動良性疾病），且完全無任何臨床試驗或文獻佐證。5 個預測中有 4 個評為 L5/Hold，整體再利用潛力偏低。

**例外：肺門癌（Rank 5）建議 Proceed with Guardrails**，機轉明確對應 EGFR 突變型 NSCLC，有個案報告支持，可作為評估延伸適應症的起點。

**若要推進需要：**
- 確認香港衞生署藥物辦公室（Pharmacy and Poisons Board）Gefitinib 許可證登記狀態（目前資料顯示 0 筆，疑為資料管道未能取得）
- 查詢 DrugBank API（DB00317）補充完整 MOA 及分類資料
- 下載並解析 Gefitinib 原廠仿單（Iressa® 250 mg），取得警語、禁忌及藥物交互作用資料
- 肺門癌路徑：以「EGFR mutant NSCLC」或「non-small cell lung cancer gefitinib」重新搜尋 ClinicalTrials.gov，取得完整 Phase 3 RCT 證據基礎
- IBMPFD/FTD 路徑（探索性）：設計 progranulin-EGFR 軸的基礎研究實驗方案；前臨床結果正面後，再評估進入 S1 評估的可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

