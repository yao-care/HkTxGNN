---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 567
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Mesalazine：預測新適應症為類風濕性關節炎 (Rheumatoid Arthritis)（證據等級 L5）。原適應症：潰瘍性結腸炎、發炎性腸道疾病、潰瘍性直腸乙狀結腸炎"
monitor_inn: "MESALAZINE"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "osteoarthritis susceptibility"]
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Mesalazine：從潰瘍性結腸炎到類風濕性關節炎（研究性假說）

## 一句話總結

Mesalazine（美沙拉嗪，5-ASA）原本用於治療潰瘍性結腸炎、發炎性腸道疾病與潰瘍性直腸乙狀結腸炎。
TxGNN 模型預測分數最高的是罕見遺傳疾病，但這些預測缺乏任何支持；其中**類風濕性關節炎 (Rheumatoid Arthritis)** 是唯一有間接文獻線索的候選。
目前**沒有任何臨床試驗**，且文獻多為 sulfasalazine 相關回顧或不良反應個案報告，**沒有直接證明 mesalazine 對該適應症有效**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 潰瘍性結腸炎、發炎性腸道疾病、潰瘍性直腸乙狀結腸炎 |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis)（TxGNN 排名第 3，但為證據最多的候選） |
| TxGNN 預測分數 | 99.57%（排名第 1 的「先天性少毛症合併青少年黃斑部失養症」為 99.65%，但完全沒有證據） |
| 證據等級 | L4（類風濕性關節炎）；其餘候選為 L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（類風濕性關節炎列為研究性問題） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為 mesalazine 具有抗發炎活性（抑制前列腺素與白三烯合成、調節 NF-κB、活化 PPAR-γ），主要在腸道局部作用，全身吸收低。

**類風濕性關節炎**：mesalazine 是 sulfasalazine 的活性成分之一，而 sulfasalazine 是確立的抗風濕藥 (DMARD)。但一般認為 sulfasalazine 的抗風濕效果主要來自 sulfapyridine 部分，而非 5-ASA，單用 mesalazine 並未顯示明確療效。因此這個關聯屬於間接推論（藥物類別效應），不足以支持直接推進。

**其他預測**：
- **骨關節炎**：滑膜有低度發炎，理論上與抗發炎作用有關，但唯一一篇文獻是轉錄體學的靶點篩選研究，僅能產生假說。且口服 mesalazine 設計為腸道局部釋放，到達關節的全身暴露是疑慮。
- **先天性少毛症合併青少年黃斑部失養症**（CDH3 突變的罕見遺傳病）、**脂漏性角化症**、**骨關節炎易感性**：找不到合理的機轉連結，高分很可能是知識圖譜的預測假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為類風濕性關節炎候選的文獻（依類型與相關性挑選）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | 回顧 sulfasalazine 治療類風濕性關節炎的藥理與療效；sulfasalazine 在腸道分解為 sulfapyridine 與 mesalazine，何者為活性成分尚不確定 |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clin Pharmacokinet | 慢作用抗風濕藥的藥動學，療效常需數月才顯現 |
| [7781502](https://pubmed.ncbi.nlm.nih.gov/7781502/) | 1995 | Review | Dtsch Med Wochenschr | Mesalazine 一般性介紹 |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | 藥物警戒分析 | Gut | 重新評估 sulfasalazine 與 mesalazine 向英國藥安委員會通報的嚴重不良反應 |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2026 | Case report | Internal Medicine | 一名類風濕性關節炎患者發生 5-ASA 誘發的結腸炎 |
| [31830393](https://pubmed.ncbi.nlm.nih.gov/31830393/) | 2019 | Case report | G Ital Nefrol | 類風濕性關節炎患者使用 salazopyrin 後，再接觸 mesalazine 引發 DRESS 症候群與急性腎衰竭 |
| [42565551](https://pubmed.ncbi.nlm.nih.gov/42565551/) | 2026 | Cohort | Rheumatology (Oxford) | 免疫媒介發炎疾病女性孕期用藥與妊娠結果 |

另有骨關節炎候選的一篇文獻：[38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/)（2024，J Transl Med，轉錄體學／計算分析，僅為假說產生）。

**小結**：這些文獻以 sulfasalazine 的間接證據和安全性訊號為主，沒有一篇證明 mesalazine 單藥對類風濕性關節炎有效。

---

## 香港上市資訊

本藥在香港共有 20 張有效許可證（皆為單方，無已註銷）。主要許可證如下，資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63749 | SYN-MESALAZINE ENTERIC-COATED TABLETS 250MG | 腸溶錠 | 請參考原廠仿單 |
| HK-37044 | PENTASA SUPP 1G | 栓劑 | 請參考原廠仿單 |
| HK-65052 | SALOFALK GASTRO-RESISTANT PROLONGED-RELEASE GRANULES 1.5G | 緩釋顆粒 | 請參考原廠仿單 |
| HK-51119 | ASACOL ENEMA 4G/100ML | 灌腸劑 | 請參考原廠仿單 |
| HK-59673 | SALOFALK 250 SUPP 250MG | 栓劑 | 請參考原廠仿單 |

---

## 安全性考量

- **知識圖譜中的疾病禁忌訊號**（非仿單文字）：腎臟疾病、肝臟疾病、膽囊疾病、嗜中性白血球低下、顆粒球缺乏症、貧血（含巨球性貧血）、幽門狹窄、類脂性腎病變、間質性腎炎、膿尿輸尿管。
- **藥物交互作用**：共查得 100 筆。
  - **重大 (Major)**：Cidofovir、人類肉毒桿菌神經毒素 A/B 免疫球蛋白。
  - **中度 (Moderate)**：Ketorolac、Ibuprofen、Celecoxib 等 NSAID；Acyclovir、Amphotericin B、Amikacin、Cisplatin 等具腎毒性藥物；Azathioprine 等。合併使用需留意腎功能與血球變化。
- **文獻中的安全性訊號**：5-ASA 誘發結腸炎、DRESS 症候群併急性腎衰竭，在類風濕性關節炎患者中曾有報告。

仿單的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（類風濕性關節炎可列為研究性問題，其餘預測不建議推進）

**理由：**
- 所有預測皆無臨床試驗，最高分的候選缺乏任何機轉或文獻支持，應視為知識圖譜的預測假象。類風濕性關節炎僅有 sulfasalazine 的間接證據，且 mesalazine 單藥未顯示明確療效，並有不良反應的警訊。
- 資料中也缺少仿單的警語與禁忌症，無法完成安全性初篩。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症。
- 補充 mesalazine 的作用機轉資料（如 DrugBank）。
- 針對類風濕性關節炎，系統性檢索 mesalazine 單藥與 sulfapyridine 的比較研究，釐清 5-ASA 的實際貢獻。
- 評估全身暴露是否足以作用於關節，並釐清腎臟與血液學安全性監測計畫。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

