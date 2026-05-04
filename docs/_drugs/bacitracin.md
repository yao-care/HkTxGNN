---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

# Bacitracin：從外用細菌感染到點狀上皮角結膜炎

## 一句話總結

Bacitracin 是一種外用多胜肽類抗生素，對革蘭氏陽性菌（如金黃色葡萄球菌、A 型鏈球菌）具有殺菌效果，廣泛用於皮膚傷口及眼部、耳部細菌感染的局部治療。TxGNN 模型最高分預測其可能對**點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效（預測分數 99.999%），然而此疾病成因主要為非細菌性因素（病毒、乾眼、毒性），Bacitracin 的抗菌機轉根本不對位，目前亦無任何臨床試驗或文獻支持。在全部 10 個預測適應症中，**外耳道炎 (Otitis Externa)** 具有最充分的佐證（L3 等級，**6 篇文獻**）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外用細菌感染（皮膚傷口、眼部、耳部局部感染） |
| 最高分預測適應症 | 點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.999% |
| 最高分預測證據等級 | L5（僅模型預測，無臨床研究） |
| 最佳證據適應症 | 外耳道炎 (Otitis Externa)，L3，排名第 4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Bacitracin 是由枯草桿菌（*Bacillus subtilis*）衍生的多胜肽類抗生素。其作用機轉為抑制細菌細胞壁合成——透過干擾細胞膜上脂質焦磷酸酯（Undecaprenyl pyrophosphate）的去磷酸化循環，阻斷肽聚糖前驅物的轉運，最終導致細菌死亡。Bacitracin 對革蘭氏陽性菌活性強，但對革蘭氏陰性菌幾乎無效；系統性使用因腎毒性風險高，臨床上僅以外用形式（皮膚膏、眼膏）廣泛應用。

點狀上皮角結膜炎（PEK）的成因主要為：病毒感染（腺病毒、皰疹病毒）、乾眼症、隱形眼鏡毒性、藥物毒性或紫外線損傷，並非細菌性感染。Bacitracin 的抗菌機轉對 PEK 的原發病理毫無對應靶點，即便在眼科場景中，Bacitracin 眼膏的臨床用途也僅限於預防或治療角膜的繼發性細菌感染，而非 PEK 本身。

因此，TxGNN 最高分預測在機轉層面缺乏合理性基礎，無法支持進一步臨床開發投入。

---

## 臨床試驗證據

目前無針對**點狀上皮角結膜炎**的相關臨床試驗登記。

---

## 文獻證據

目前無針對**點狀上皮角結膜炎**的相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 全部預測適應症總覽

本報告為多適應症評估，涵蓋 Bacitracin 的前 10 個 TxGNN 預測適應症，各項評估結果如下：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 機轉評估摘要 |
|------|-----------|-----------|---------|------|------------|
| 1 | 點狀上皮角結膜炎 | 99.999% | L5 | Hold | 成因非細菌性（病毒/乾眼/毒性），機轉不對位 |
| 2 | 暴露性角膜炎 | 99.991% | L5 | Hold | 主要為保護性治療，Bacitracin 僅具輔助潤滑及預防繼發感染效果，非原發機轉治療 |
| 3 | 非人類動物疾病 | 99.970% | L5 | Hold | 不適用於人類藥物再利用評估框架，排除 |
| **4** | **外耳道炎** | **99.969%** | **L3** | **Research Question** | **Nebacetin 複方（Bacitracin＋Neomycin）耳用製劑在歐洲有歷史臨床使用紀錄，機轉具一定合理性** |
| 5 | 感染後血管炎 | 99.968% | L5 | Hold | 免疫複合物媒介機轉，Bacitracin 無抗炎或免疫調節活性 |
| 6 | 細菌感染後症狀 | 99.967% | L5 | Hold | 12 項相關試驗均非 Bacitracin 特異性研究，無直接支持 |
| 7 | 感染性尿道狹窄 | 99.965% | L5 | Hold | 致病菌為革蘭氏陰性（淋菌/衣原體），Bacitracin 無效；纖維化後遺症非抗菌藥適應症 |
| 8 | 感染後症候群 | 99.965% | L5 | Hold | 涉及免疫失調/自主神經功能障礙（如 Long COVID），純抗菌機轉無法處理 |
| 9 | 感染相關溶血性尿毒症候群 | 99.962% | L5 | Hold | STEC（革蘭氏陰性）引發，且 STEC-HUS 中使用抗生素可能促進毒素釋放，屬禁忌 |
| 10 | Chagas 心肌病 | 99.961% | L5 | Hold | 原蟲（*Trypanosoma cruzi*）感染，Bacitracin 無任何抗原蟲活性 |

---

## 外耳道炎（Otitis Externa）— 最佳候選適應症詳細分析

外耳道炎是 10 個預測適應症中唯一達到 **L3 證據等級**、建議進入 **Research Question** 階段的適應症。

**機轉說明**：外耳道炎主要致病菌包含：
- *Pseudomonas aeruginosa*（革蘭氏陰性，Bacitracin **無效**）
- *Staphylococcus aureus*（革蘭氏陽性，Bacitracin **有效**）

歐洲歷史上使用的 Nebacetin 複方（Bacitracin＋Neomycin）耳用製劑，設計上透過 Neomycin 補足革蘭氏陰性菌覆蓋的不足，使複方在組合上具備一定的臨床合理性。

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | 臨床比較研究 | Eur Arch Otorhinolaryngol | Polymyxin-B＋Bacitracin 軟膏（含/不含氫化可體松）治療急性外耳道炎雙盲試驗（n=151），評估類固醇輔助成分的貢獻，為本系列中最具品質的直接研究 |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | 臨床病例系列 | Z Laryngol Rhinol Otol | Nebacetin（含 Bacitracin）外耳道及鼻炎局部治療歷史案例，最早期的直接使用紀錄 |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | 臨床綜述 | Maryland State Med J | 外耳道炎外用抗菌治療實務綜述，涵蓋 Bacitracin 複方的應用 |
| [4306877](https://pubmed.ncbi.nlm.nih.gov/4306877/) | 1969 | 專家綜述 | Z Arztl Fortbild | 耳科抗生素（含 Bacitracin 複方製劑）使用原則的德語專家意見 |
| [165871](https://pubmed.ncbi.nlm.nih.gov/165871/) | 1975 | 臨床研究 | Can Med Assoc J | 外耳道炎抗菌治療方案比較，作為背景對照資料 |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | 體外敏感性測試 | J Vet Med B | 慢性外耳道炎分離菌株（含葡萄球菌）對 Bacitracin 等 20 種抗生素敏感性測試，為動物研究，僅作參考 |

> ⚠️ 注意：現有文獻以 1960–1970 年代歷史文獻及專家意見為主，缺乏現代 RCT 或系統性回顧，整體證據品質偏低。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 最高分預測（點狀上皮角結膜炎）機轉根本不對位且無任何臨床或文獻支持；10 個預測適應症中，僅外耳道炎（排名第 4）具 L3 等級文獻支持，但文獻品質偏低（以歷史文獻為主，缺乏現代 RCT），加上 Bacitracin 在香港未上市、安全性資訊未能確認，整體評估建議維持 Hold，不進行主動開發投入。

**若未來評估外耳道炎適應症，需要：**
- 補充現代 RCT 或 Cochrane 系統性回顧（Bacitracin 複方用於急性外耳道炎的現代臨床證據）
- 確認完整作用機轉資料（查詢 DrugBank API）
- 查閱並確認安全性資訊（原廠仿單、EMA/TFDA 警語及禁忌症）
- 評估 Bacitracin＋Neomycin 複方耳用劑型的製藥可行性及專利狀況
- 評估香港市場的藥品引進申請可行性（向衛生署提出許可申請）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

