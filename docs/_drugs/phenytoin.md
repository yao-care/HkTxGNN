---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 583
evidence_level: L5
indication_count: 5
---

# Phenytoin
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

# Phenytoin：從癲癇/疼痛控制到三叉神經腫瘤（Trigeminal Nerve Neoplasm）

## 一句話總結

Phenytoin 是鈉通道阻斷劑，臨床上用於癲癇控制及三叉神經痛等疼痛管理。
TxGNN 模型將其預測為對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效（預測分數 99.99%），
但經機轉與文獻檢視後，判定此關聯很可能是模型因「trigeminal」關鍵字重疊產生的偽陽性，目前**無臨床試驗**佐證，僅 5 篇文獻且皆與腫瘤治療無關。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未提供完整清單；證據包文字說明 phenytoin 為鈉通道阻斷劑，用於癲癇及三叉神經痛等疼痛控制 |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.99%（模型排名第 378） |
| 證據等級 | L5（僅模型預測，無支持性研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**這個預測目前判定為不合理，很可能是偽陽性。**

Phenytoin 的作用機轉是鈉通道阻斷，用於抑制異常神經放電，臨床應用集中在癲癇（各型反射性/誘發性癲癇）及三叉神經痛等神經疼痛控制。這類機轉與**抑制腫瘤生長或增殖**之間並無已知的藥理關聯。

檢視 TxGNN 排名第 1 的預測適應症「三叉神經腫瘤」，相關文獻檢索到的 5 篇文章實際內容分別是三叉神經痛治療、Sturge-Weber 症候群、機構化智能障礙者皮膚病、三叉神經根纖維與疼痛傳導機轉研究——**沒有一篇涉及腫瘤治療或抗腫瘤機轉**。合理推測，模型是因「trigeminal」（三叉神經）這個關鍵字同時出現在「trigeminal neuralgia（三叉神經痛，phenytoin 已知適應症）」與「trigeminal nerve neoplasm（三叉神經腫瘤）」兩個疾病實體中，導致知識圖譜產生錯誤的高分關聯，而非真實的藥理學信號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | 三叉神經痛的多種內外科治療方式回顧，與腫瘤無關 |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Review | J Assoc Physicians India | Sturge-Weber 症候群（神經皮膚血管病變）個案討論 |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Cohort | Birth Defects Orig Artic Ser | 機構化智能障礙者皮膚病回顧 |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | An Esp Pediatr | Sturge-Weber 症候群 14 例經驗 |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Preclinical (basic science) | Trans Am Neurol Assoc | 三叉神經後根纖維大小與疼痛/觸覺傳導關聯研究 |

以上文獻與「腫瘤」治療或抑制機轉均無直接關聯，僅因主題涉及「三叉神經」而被檢索納入。

---

## 香港上市資訊

Phenytoin 目前**未在香港上市**，查無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本評估的 TFDA 仿單警語/禁忌資料為 **Blocking 等級缺口**，在此資料補齊前無法進入 S1 安全性初評階段。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉分析顯示 phenytoin（鈉通道阻斷劑）與抑制腫瘤生長無已知藥理關聯，此預測疑似為 TxGNN 因關鍵字重疊（trigeminal）產生的偽陽性。
- 無任何臨床試驗，5 篇文獻皆與腫瘤治療無關，證據等級僅 L5。
- 該藥物在香港未上市，且缺乏 MOA 與仿單安全性資料（Blocking 缺口），不具備進一步臨床評估的資料基礎。

**若要推進需要：**
- 若仍要驗證此適應症，需先由藥理專家確認是否存在尚未被知識圖譜捕捉的機轉路徑，而非僅依賴 TxGNN 分數。
- 補齊 TFDA/香港仿單警語與禁忌資料，以及完整 MOA 資料（DG001、DG002）。
- 建議將研究資源轉向本藥物的其他候選適應症——**audiogenic seizures（音源性癲癇）** 排名第 5，證據等級達 L4／決策階段 S1（Research Question），有多篇齧齒類動物實驗直接支持 phenytoin 的抗驚厥效果，機轉一致性遠高於本候選。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

