---
layout: default
title: Mefenamic Acid
parent: 高證據等級 (L1-L2)
nav_order: 397
evidence_level: L2
indication_count: 5
---

# Mefenamic Acid
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

使用 v5 藥物再利用評估報告 Prompt 格式，根據提供的 Evidence Pack 產出報告如下。

---

# Mefenamic Acid：從（原適應症資料缺口）到類風濕性關節炎

## 一句話總結

> Mefenamic Acid 是 fenamate 類非類固醇消炎止痛藥（NSAID），其官方核准之原始適應症在本次證據包中屬於資料缺口（DG002），故無法直接引述。
> TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
> 目前雖無登記中的臨床試驗，但有 **20 篇文獻**（含 3 篇 RCT）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（DrugBank 未提供，屬 DG002） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L2 |
| 台灣上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Mefenamic Acid 屬於 fenamate 類 NSAID，透過非選擇性抑制 COX-1/COX-2 酵素，減少前列腺素（prostaglandin）合成，產生抗發炎與鎮痛作用。這個機轉本身就是類風濕性關節炎治療的核心藥理路徑之一，因為類風濕性關節炎的關節腫脹、疼痛與晨僵主要由前列腺素介導的滑膜發炎反應所驅動。

雖然本證據包無法提供 Mefenamic Acid 正式核准的原始適應症文字（DrugBank 標註為資料缺口），但這並非代表證據缺口——文獻回顧顯示 Mefenamic Acid 事實上長期被作為 NSAID 用於發炎性關節疾病，且與 ibuprofen、sulindac、flurbiprofen 等同類藥物有多篇直接頭對頭比較試驗，證實其抗發炎/鎮痛效果與其他核准用於類風濕性關節炎的 NSAID 相當。

換句話說，TxGNN 的預測與已知藥理機轉高度一致：COX 抑制 → 前列腺素減少 → 關節發炎與疼痛緩解，這條路徑在類風濕性關節炎中有明確的生物學合理性，也有數十年臨床使用經驗佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov 與 ICTRP 查詢皆為 0 筆）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT | Current Medical Research and Opinion | 雙盲交叉試驗比較 mefenamic acid、sulindac、flurbiprofen，皆顯著優於安慰劑，改善疼痛評分與晨僵 |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | J Int Med Res | 隨機雙盲研究：mefenamic acid 與 ibuprofen 抗發炎鎮痛效果無顯著差異 |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT | The Medical Journal of Australia | 雙盲交叉試驗：mefenamic acid（1500mg/day）與 ibuprofen（1200mg/day）療效相當，副作用輕微且多為腸胃道 |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Cohort/Open-label | Annals of the Rheumatic Diseases | Mefenamic acid 用於類風濕性關節炎之早期臨床觀察 |
| [5333309](https://pubmed.ncbi.nlm.nih.gov/5333309/) | 1966 | Review | British Medical Journal | Mefenamic acid 藥理與臨床應用回顧 |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | 回顧 mefenamic acid 於類風濕性關節炎治療中的角色 |
| [20668](https://pubmed.ncbi.nlm.nih.gov/20668/) | 1977 | Review | Seminars in Arthritis and Rheumatism | 抗發炎藥物綜述，涵蓋 mefenamic acid 等 NSAID 之比較 |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Review | Clinical Pharmacy | NSAID 藥理綜述，說明 COX 抑制與前列腺素合成之關聯（以 diclofenac 為主，間接支持同類藥物機轉） |
| [23611159](https://pubmed.ncbi.nlm.nih.gov/23611159/) | 2014 | Formulation Study | Pharmaceutical Development and Technology | 開發三重同心時控釋放 mefenamic acid 錠劑，針對類風濕性關節炎劑型改良 |
| [16223958](https://pubmed.ncbi.nlm.nih.gov/16223958/) | 2006 | Preclinical | Molecular Pharmacology | Mefenamic acid 於阿茲海默症模型顯示神經保護作用，並提及長期 NSAID 治療類風濕性關節炎患者可降低失智風險之流行病學觀察 |

（本適應症共有 20 篇相關文獻，以上列出證據等級最高之 10 篇）

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本證據包已標記「TFDA 仿單警語/禁忌」為 Blocking 等級資料缺口（DG001），在補齊此資料前，不應進入安全性初評（S1）階段。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 3 篇 1970-80 年代的頭對頭 RCT 支持 mefenamic acid 於類風濕性關節炎的鎮痛/抗發炎效果與其他核准 NSAID 相當，機轉合理性高。
- 但現有證據皆為數十年前的舊研究，缺乏現代臨床試驗驗證，且安全性仿單資料（DG001，Blocking）尚未補齊，暫不宜直接進入安全性初評。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌症資料（DG001，Blocking，需完成才能進入 S1）
- 補充正式作用機轉（MOA）資料，以強化機轉關聯性分析（DG002）
- 評估是否需要現代臨床試驗（現有 RCT 皆為 1970-80 年代研究）
- 若考慮上市，需規劃台灣藥品許可證申請（目前市場狀態為未上市，0 張許可證）

---

## 附錄：其他預測候選適應症一覽

本次 Evidence Pack（TW-DB00784-multi）共預測 5 個候選適應症，除上述類風濕性關節炎外，其餘結果如下：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策 | 說明 |
|------|-----------|-----------|---------|------|------|
| 3 | 頭痛症 (Headache Disorder，含偏頭痛) | 99.64% | L2 | Proceed with Guardrails | 19 篇文獻，含多篇經期偏頭痛預防/急性治療 RCT，機轉與前列腺素介導之腦血管發炎相關，證據品質與 RA 相近 |
| 2 | 骨關節炎易感性 (Osteoarthritis Susceptibility) | 99.72% | L5 | Hold | "易感性" 為基因風險標籤而非可治療表型，無文獻或試驗支持，機轉連結薄弱 |
| 4 | 三叉神經自律神經頭痛 (Trigeminal Autonomic Cephalalgia) | 99.55% | L5 | Hold | 病理機轉以 CGRP 為主，與 NSAID 之 COX 抑制機轉關聯薄弱，臨床上對傳統 NSAID 反應通常不佳，無文獻支持 |
| 5 | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome | 99.49% | L5 | Hold | 罕見遺傳性發育畸形症候群，與 NSAID 藥理機轉無合理連結，判定為知識圖譜噪聲 |

除類風濕性關節炎外，**頭痛症/偏頭痛**是另一個具有中等證據強度（L2）的候選方向，值得後續一併評估；其餘 3 項證據等級皆為 L5（僅模型預測、無實際研究支持），建議維持 Hold。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

