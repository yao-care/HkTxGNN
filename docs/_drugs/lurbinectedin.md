---
layout: default
title: Lurbinectedin
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
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

# Lurbinectedin：原適應症資料缺失，預測新適應症為 Multiple Endocrine Neoplasia（低信度）

## 一句話總結

Lurbinectedin（DrugBank ID: DB12674）目前在台灣**未上市**，原始核准適應症與作用機轉資料均缺失。
TxGNN 模型列出 10 個候選新適應症，分數最高者為 **Multiple Endocrine Neoplasia（多發性內分泌腫瘤）**（99.44%），
但**全部 10 個候選均無臨床試驗、無文獻支持**，證據等級皆為 L5，機轉關聯性分析也判定多數預測可能是知識圖譜拓樸雜訊。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（DrugBank 未提供，屬 High severity data gap） |
| 預測新適應症 | Multiple Endocrine Neoplasia（多發性內分泌腫瘤） |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L5（僅有模型預測，無臨床試驗或文獻） |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 未提供結構化的 `original_moa` 資料（Blocking/High 級資料缺口）。根據 evidence pack 中各候選適應症的機轉分析文字，可還原出以下背景資訊：Lurbinectedin 已知作用機轉為**與 DNA 小溝結合、抑制致癌基因相關的轉錄（RNA Pol II 相關）**，屬於傳統細胞毒性抗腫瘤藥物。

針對排名第一的候選適應症「多發性內分泌腫瘤（MEN，通常由 RET/MEN1 生殖系突變驅動的遺傳性內分泌腫瘤症候群）」，evidence pack 中的機轉關聯分析明確指出：**無資料支持**此連結，該疾病的致病機轉與 lurbinectedin 的轉錄抑制作用之間並無合理藥理連結，推測 TxGNN 的高分很可能反映知識圖譜中基因/腫瘤節點的拓樸鄰近性，而非真實藥理相關性。

其餘 9 個候選適應症（HIV 感染、類風濕性關節炎、肌萎縮性脊髓側索硬化症、CMV 感染，以及數個獸醫/動物疾病如猴免疫缺陷病毒感染、貓後天免疫缺乏症候群、牛傳染性鼻氣管炎、惡性卡他熱、Mills syndrome）皆被 evidence pack 標註為**無機轉支持**，部分甚至非人類臨床適應症（獸醫用途），應視為模型雜訊而非可推進的再利用假說。

## 臨床試驗證據

目前無相關臨床試驗登記（10 個候選適應症的 ClinicalTrials.gov 與 ICTRP 查詢結果皆為 0 筆）。

## 文獻證據

目前無相關文獻（10 個候選適應症的 PubMed 查詢結果皆為 0 筆）。

## 台灣上市資訊

Lurbinectedin 目前在台灣**未上市**，無許可證登記（`total_licenses: 0`）。

## 細胞毒性

Lurbinectedin 屬抗腫瘤藥物（DNA 小溝結合、抑制致癌基因轉錄），故列出本章節：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA 結合型轉錄抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語與禁忌症資料尚未取得，屬 Blocking 級資料缺口，無法進入 S1 安全性初評）

## 其他預測適應症（Rank 2–10，供參考）

| 排名 | 疾病 | TxGNN 分數 | 機轉支持 | 決策 |
|------|------|-----------|---------|------|
| 2 | HIV infectious disease | 99.34% | 無 | Hold |
| 3 | Rheumatoid arthritis | 99.26% | 無 | Hold |
| 4 | Amyotrophic lateral sclerosis | 99.26% | 無 | Hold |
| 5 | Cytomegalovirus infection | 99.14% | 無 | Hold |
| 6 | Simian immunodeficiency virus infection（動物模式，非人類適應症） | 99.09% | 無 | Hold |
| 7 | Feline acquired immunodeficiency syndrome（獸醫適應症） | 99.09% | 無 | Hold |
| 8 | Infectious bovine rhinotracheitis（獸醫適應症） | 99.09% | 無 | Hold |
| 9 | Malignant catarrh（獸醫適應症） | 99.09% | 無 | Hold |
| 10 | Mills syndrome | 99.08% | 無 | Hold |

## 結論與下一步

**決策：Hold**

**理由：**
- 全部 10 個預測適應症皆為 L5（僅模型預測，無臨床試驗或文獻佐證），且機轉關聯性分析多判定為知識圖譜拓樸雜訊而非真實藥理連結。
- TFDA 仿單警語/禁忌症資料缺失（Blocking 級），無法完成 S1 安全性初評；藥物在台灣也尚未上市。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌症資料（解除 Blocking 缺口 DG001）
- 透過 DrugBank API 或原廠資料補齊完整作用機轉（DG002）
- 針對排名第一的候選適應症（Multiple Endocrine Neoplasia）尋找是否有臨床前或病例層級證據，目前為零筆
- 若無法在合理時間內取得任何臨床試驗或文獻支持，建議直接排除此批候選，不進入下一階段評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

