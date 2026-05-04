---
layout: default
title: Amikacin
parent: 中證據等級 (L3-L4)
nav_order: 42
evidence_level: L3
indication_count: 10
---

# Amikacin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Amikacin：從嚴重革蘭氏陰性菌感染到副傷寒

## 一句話總結

Amikacin 是一種氨基糖苷類廣譜抗生素，主要用於治療嚴重革蘭氏陰性菌引起的感染（包括敗血症、肺炎及泌尿道感染等）。
TxGNN 模型預測它可能對**副傷寒 (Paratyphoid Fever)** 有效，
目前有 **0 個臨床試驗**和 **12 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 嚴重革蘭氏陰性菌感染（敗血症、肺炎、泌尿道感染） |
| 預測新適應症 | 副傷寒 (Paratyphoid Fever) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Amikacin 屬於氨基糖苷類（Aminoglycoside）抗生素，其作用機轉為結合細菌 30S 核糖體次單元，造成 mRNA 誤讀並抑制蛋白質合成，對革蘭氏陰性菌具強力殺菌效果。由於此機轉作用於細菌核糖體，而非人類宿主細胞，故對多種革蘭氏陰性菌具廣泛活性。

副傷寒的致病菌 *Salmonella paratyphi* A/B/C 與傷寒桿菌（*S. typhi*）同屬革蘭氏陰性腸桿菌科，具有相同的核糖體結構，因此 amikacin 的 30S 抑制機轉在理論上同樣適用。相較於其他沙門氏菌，*S. paratyphi* 對氨基糖苷類的耐藥率相對較低，使 amikacin 保有一定的治療潛力。

臨床上，amikacin 已被用於多重耐藥（MDR）腸熱症及喹諾酮耐藥 *S. paratyphi* 感染的補救治療方案。PMID 2516600 直接報告了 48 例 paratyphi B 感染、傳統治療失敗患者改用 amikacin 的系列結果；PMID 9459410 描述喹諾酮耐藥 *S. paratyphi* B 腦膜炎新生兒以 amikacin 作為替代治療的案例。這兩篇文獻均提供直接的臨床應用依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Case Series / Retrospective | Mikrobiyoloji Bulteni | 48 例 *S. paratyphi* B 感染耐傳統治療（ampicillin/chloramphenicol/co-trimoxazole）患者改用 amikacin 之治療與抗生素圖結果 |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective Observational | J Indian Medical Association | 145 例 18 歲以下血培養陽性腸熱症兒童，分析 *S. typhi* 及 *S. paratyphi* 現行抗生素敏感性型態 |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case Report | Pediatric Hematology & Oncology | *S. paratyphi* B 感染導致急性無結石膽囊炎之急性白血病兒童，以 cefepime + amikacin + G-CSF 成功治療，生存率優於外科手術 |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case Report | The Journal of Infection | 喹諾酮耐藥 *S. paratyphi* B 腦膜炎新生兒案例，amikacin 作為替代抗生素選項 |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Case Report | Indian Journal of Pediatrics | 40 週足月剖腹產新生兒出生後第 5 天副傷寒敗血症，血培養呈多重藥物敏感型 *S. paratyphi* A |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Microbiological Study | Pakistan Journal of Biological Sciences | 巴基斯坦奎達市各醫院腸熱症患者 *S. paratyphi* 分離鑑定，提供當地流行菌株微生物特性資料 |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Laboratory Surveillance | JNMA (Nepal Medical Association) | 教學醫院血培養分離株菌種分布與抗生素敏感性圖譜，含沙門氏菌對 amikacin 敏感性數據 |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Clinical Study | Medical Journal, Armed Forces India | 45 例腸熱症血培養陽性患者 *S. typhi* 及 *S. paratyphi* A 抗生素敏感性分析，含 amikacin 體外敏感性數據 |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiological Study | The New Microbiologica | 約旦 1988–2000 年 *S. typhi* 及 *S. paratyphi* 流行病學研究，提供地區性發病率及抗藥性背景資料 |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case Series | Journal of Pediatric Surgery | 4 例兒童腸熱症相關脾臟膿瘍以抗生素聯合針吸引流成功治療，免除脾臟切除 |

---

## 香港上市資訊

Amikacin 目前在香港**未有許可證登記**（市場狀態：未上市，登記數：0 張）。如需使用，須透過特殊藥物申請渠道取得。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Amikacin 對 *Salmonella paratyphi* 的殺菌機轉有明確的生物學依據，現有文獻（尤其 PMID 2516600 及 PMID 9459410）直接支持其在多重耐藥或喹諾酮耐藥 *S. paratyphi* 感染中的補救治療角色，整體達 L3 證據等級。
- 然而，目前缺乏正式臨床試驗數據，且 amikacin 在香港未登記，主要定位為耐藥補救方案而非一線治療，推進前需補齊安全性及監管資料。

**若要推進需要：**
- 補充詳細 MOA 資料（建議查詢 DrugBank API，DrugBank ID: DB00479）
- 取得香港衛生署仿單警語及禁忌症資料，以完成 S1 安全性初評
- 確認腎毒性、耳毒性等氨基糖苷類典型副作用的監測計畫（包括血中濃度監測 TDM）
- 設計針對 MDR *S. paratyphi* 的前瞻性觀察研究或小型臨床試驗，以提升證據等級至 L2
- 評估香港本地腸熱症流行病學數據，確認臨床需求規模
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

