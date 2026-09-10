---
layout: default
title: Phenoxymethylpenicillin
parent: 僅模型預測 (L5)
nav_order: 578
evidence_level: L5
indication_count: 2
---

# Phenoxymethylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenoxymethylpenicillin（苯氧甲基青黴素）：從細菌感染到會厭炎／喉炎評估

## 一句話總結

Phenoxymethylpenicillin（Penicillin V）是口服窄譜青黴素類抗生素，傳統用於鏈球菌等革蘭氏陽性菌感染。TxGNN 模型分別預測其對**會厭炎 (Epiglottitis)** 和**喉炎 (Laryngitis)** 有高關聯分數，但會厭炎目前**無任何臨床試驗或文獻**支持，喉炎雖有 **1 篇 RCT 和 4 版 Cochrane 系統性回顧**等直接證據，結論卻一致顯示**療效為陰性**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鏈球菌等革蘭氏陽性菌感染（無香港許可證仿單資料可供比對） |
| 預測新適應症 1 | 會厭炎 (Epiglottitis)，TxGNN 分數 99.90%（rank 2660） |
| 預測新適應症 2 | 喉炎 (Laryngitis)，TxGNN 分數 99.85%（rank 3749） |
| 證據等級 | 會厭炎 L5（僅模型預測）／喉炎 L3（有直接臨床證據，但方向為陰性） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold**（兩項適應症皆不建議推進） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。根據文獻中提供的藥理背景，Penicillin V 是口服、對 β-內醯胺酶不穩定的窄譜青黴素，主要涵蓋 *Streptococcus pyogenes* 等革蘭氏陽性菌，這是 TxGNN 判定其與呼吸道感染相關的機轉基礎。

**會厭炎**是上呼吸道急症，成人致病菌以 *S. pneumoniae*、*S. pyogenes*、*S. aureus* 為主，兒童傳統上以 *Haemophilus influenzae* type b 為主——後者對 Penicillin V 天然不敏感或易產 β-內醯胺酶。臨床指引一律要求靜脈注射廣譜抗生素並優先確保呼吸道，口服窄譜 Penicillin V 在藥理與臨床操作面皆不適配。TxGNN 的高分很可能只反映知識圖譜中「抗生素—呼吸道感染」的一般關聯，而非考量菌種覆蓋與給藥途徑。

**喉炎**病因絕大多數為病毒性，僅少數細菌性病例理論上可能對窄譜青黴素敏感，這是 TxGNN 預測的機轉基礎。但實際直接證據方向相反：雙盲 RCT（PMID 3918495）結論為 Penicillin V 對成人急性喉炎「無效」；歷次 Cochrane 系統性回顧（2005/2007/2013/2015 版）持續不建議常規使用抗生素。機轉假說已被實證推翻。

## 臨床試驗證據

目前無相關臨床試驗登記（會厭炎、喉炎皆無）。

## 文獻證據

**會厭炎**：目前無相關文獻。

**喉炎**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3918495](https://pubmed.ncbi.nlm.nih.gov/3918495/) | 1985 | RCT（雙盲） | Ann Otol Rhinol Laryngol | 100 名成人喉炎雙盲試驗，Penicillin V 與安慰劑對聲音症狀恢復率相同，療效無差異 |
| [23543536](https://pubmed.ncbi.nlm.nih.gov/23543536/) | 2013 | Review (Cochrane) | Cochrane Database Syst Rev | 成人急性喉炎抗生素系統性回顧 2013 更新版，不支持常規使用抗生素 |
| [26002823](https://pubmed.ncbi.nlm.nih.gov/26002823/) | 2015 | Review (Cochrane) | Cochrane Database Syst Rev | 同系列回顧 2015 更新版，結論一致：不建議常規抗生素治療 |
| [17443555](https://pubmed.ncbi.nlm.nih.gov/17443555/) | 2007 | Review (Cochrane) | Cochrane Database Syst Rev | 2007 更新版，結論一致 |
| [15674965](https://pubmed.ncbi.nlm.nih.gov/15674965/) | 2005 | Review (Cochrane) | Cochrane Database Syst Rev | 該系統性回顧最初版本 |
| [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/) | 1992 | Cohort/臨床研究 | Acta Otolaryngol Suppl | 106 名成人喉炎患者比較 erythromycin 與安慰劑，文中提及 Penicillin V 對臨床病程「無效」 |
| [4995584](https://pubmed.ncbi.nlm.nih.gov/4995584/) | 1971 | Review | Nordisk Medicin | 年代久遠之喉炎綜述，非結構化，無摘要 |
| [16087016](https://pubmed.ncbi.nlm.nih.gov/16087016/) | 2005 | 臨床研究（適應症不符） | Otolaryngol Head Neck Surg | 探討 penicillin 對中耳炎（非喉炎）咽鼓管腺體變化的影響 |
| [23904305](https://pubmed.ncbi.nlm.nih.gov/23904305/) | 2013 | Case report | Ear Nose Throat J | 免疫抑制病人原發性喉部放線菌病案例，屬非典型病原，非一般喉炎 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 會厭炎：無任何臨床試驗或文獻支持，且口服窄譜 Penicillin V 在給藥途徑與抗菌覆蓋上均不符合此急重症的臨床處置流程。
- 喉炎：雖有 1 篇雙盲 RCT 及 4 版 Cochrane 系統性回顧等直接證據，但結論一致為陰性，機轉假說已被實證推翻。

**若要推進需要：**
- 補齊仿單警語/禁忌資料（DG001，Blocking）與完整 MOA 資料（DG002）
- 會厭炎：需重新評估給藥途徑（口服 vs 靜脈）與菌種覆蓋範圍是否符合臨床指引，目前不建議投入資源
- 喉炎：需有能推翻現有陰性 RCT／系統性回顧結論的新證據，否則不建議繼續推進
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

