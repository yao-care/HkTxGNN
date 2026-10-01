---
layout: default
title: Trazodone
parent: 僅模型預測 (L5)
nav_order: 885
evidence_level: L5
indication_count: 10
---

# Trazodone
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

# Trazodone：從憂鬱症到強迫症

## 一句話總結

Trazodone 是一種抗憂鬱藥，文獻指出其核准用途為憂鬱症（香港許可證資料未載明適應症）。
TxGNN 模型預測它可能對**強迫症 (Obsessive-Compulsive Disorder)** 有效。
目前**無已登記的臨床試驗**，但有 **20 篇文獻**，其中 1 篇為 1992 年的小型雙盲安慰劑對照研究，其餘多為個案報告與開放標示研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 強迫症 (Obsessive-Compulsive Disorder) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L2（僅 1 篇雙盲 RCT，結果待全文確認） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料集中的 MOA 欄位為空）。以下說明來自一般藥理知識與文獻。Trazodone 屬於血清素拮抗／再吸收抑制劑 (SARI)，主要作用是拮抗 5-HT2A/2C 受體，並有較弱的血清素再吸收抑制作用。文獻（PMID 1365657）也指出，它最強的藥理效應是 5-HT2 受體拮抗，而非再吸收抑制。

強迫症對血清素再吸收抑制劑反應較好，因此血清素系統被認為與其病理有關。Trazodone 作用於血清素系統，在機轉上有合理性。已有多篇 1980 至 1990 年代的個案報告與開放標示研究，嘗試用於對 clomipramine 無效的患者，或與 fluoxetine 併用。

不過文獻結果並不一致。例如 1986 年一項 11 位患者的試驗，併用 trazodone 與色胺酸，療效有限且耐受性不佳。TxGNN 的高分是知識圖譜上的預測，不是臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT | Journal of Clinical Psychopharmacology | 雙盲、安慰劑對照，測試 trazodone 對強迫症的療效（提供的摘要被截斷，結果需查全文） |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgraduate Medicine | 回顧 trazodone 在精神與內科疾病的使用，包含機轉、劑量與不良反應 |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Review | Current Pharmaceutical Design | 整理 trazodone 的仿單外使用，強迫症為其中一項 |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Review | Psychopharmacology Bulletin | 討論強迫症的單一與多重藥物治療，強調血清素再吸收抑制劑的核心地位 |
| [8331098](https://pubmed.ncbi.nlm.nih.gov/8331098/) | 1993 | Review | Journal of Clinical Psychiatry | 回顧難治型強迫症的生物學治療策略，多為 SRI 合併其他藥物 |
| [8134850](https://pubmed.ncbi.nlm.nih.gov/8134850/) | 1994 | Review | Southern Medical Journal | 回顧強迫症的藥物處置 |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | 個案系列 | Clinical Neuropharmacology | 9 位對 clomipramine 無效者，整體有輕度但顯著的改善，3 位反應良好 |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | 世代研究 | Psychopathology | 治療有反應者的尾狀核葡萄糖代謝出現變化 (PET) |
| [3571943](https://pubmed.ncbi.nlm.nih.gov/3571943/) | 1986 | 開放式前導試驗 | International Clinical Psychopharmacology | 11 位患者併用 trazodone 與色胺酸，效益有限且部分耐受不佳 |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | 個案報告 | Journal of Nervous and Mental Disease | 2 位合併憂鬱的重度強迫症患者，使用後明顯改善 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55397 | TRITTICO PROLONGED RELEASE TAB 75MG | LEE'S PHARMACEUTICAL (H.K) LIMITED |
| HK-68897 | JECETRAZO TABLETS 50MG | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-62870 | MESYREL TABLETS 50MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-60457 | APO-TRAZODONE TAB 50MG | HIND WING CO LTD |
| HK-62384 | TRITCOPRESS TABLET 50MG | VICKMANS LABORATORIES LTD |

共 11 張許可證，上表列出 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 強迫症的證據主要是老舊的個案報告與開放標示研究，僅有 1 篇小型雙盲 RCT，且結果尚未核實。已有 clomipramine 及其他 SSRI 等明確的一線藥物可用。
- 香港仿單的警語與禁忌資料缺失（資料缺口 DG001，屬 Blocking），無法進入安全性篩選。

**若要推進需要：**
- 取得 1992 年 Pigott 等人雙盲 RCT（PMID 1629380）的全文，確認主要療效結果。
- 下載並解析香港衛生署的仿單，補齊警語、禁忌與交互作用。
- 補充 DrugBank 的作用機轉資料。
- 評估是否有新的、設計良好的對照試驗（目前無登記試驗），並與一線藥物比較。

**其他預測適應症（簡述）：** 恐慌症／懼曠症證據等級 L2，但研究為 1980 年代的小規模研究，同樣建議列為研究問題。心境惡劣障礙 (Dysthymia) 的證據多為抗憂鬱藥類別層級，等級 L4。人格障礙類、嬰兒良性陣發性斜頸、Ohdo 症候群等，沒有有效證據或機轉連結，應視為圖譜上的假象，建議 Hold。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

