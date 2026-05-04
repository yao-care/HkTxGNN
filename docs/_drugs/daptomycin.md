---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin：從革蘭氏陽性菌感染到退化性關節炎

## 一句話總結

Daptomycin 是一種環狀脂肽類抗生素，國際核准用於皮膚感染、金黃色葡萄球菌菌血症及右側心內膜炎，目前在香港尚未上市。
TxGNN 模型預測它可能與**退化性關節炎 (Osteoarthritis)** 有關，預測分數高達 **99.86%**；
然而，目前**無任何臨床試驗登記**，10 篇相關文獻均為骨科感染治療研究，而非退化性關節炎的直接療效研究，此高分預測極可能源於共病共現偏誤（Comorbidity Co-occurrence Bias），而非真實治療潛力。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚及皮膚結構感染、金黃色葡萄球菌菌血症、右側心內膜炎（革蘭氏陽性菌感染） |
| 預測新適應症 | 退化性關節炎 (Osteoarthritis) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Daptomycin 是環狀脂肽類（Cyclic Lipopeptide）抗生素，其核心機轉為嵌入革蘭氏陽性菌細胞膜磷脂雙層，引發細菌快速去極化，導致 DNA、RNA 及蛋白質合成停止而殺菌。此機轉已充分確立，但詳細完整的 MOA 文件目前缺乏原廠資料佐證。

退化性關節炎（OA）患者因關節退化常需接受人工關節置換術，而人工關節周圍感染（Periprosthetic Joint Infection, PJI）是術後最嚴重的併發症之一。Daptomycin 正是治療 MRSA 及其他革蘭氏陽性菌引起的 PJI 的重要抗生素選項，因此在資料庫中，Daptomycin 使用記錄與 OA 患者的共現頻率極高。

⚠️ **這是共病共現偏誤，而非因果關係。** TxGNN 模型的高分預測來自 OA 患者接受手術後的感染治療場景，並非 Daptomycin 對退化性關節炎本身（軟骨退化、滑膜炎症、軟骨下骨硬化）具有任何直接療效。Daptomycin 無任何已知可干預 OA 病理機轉（如 IL-1β/TNF-α 驅動的軟骨分解、MMP 活化或 GDF5 訊號）的機轉假說。

> **值得關注**：TxGNN 第 2 名預測為**類風濕性關節炎（RA）**，其預測分數同樣高達 99.84%，且有 2025 年動物實驗資料（PMID [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/)）顯示 Daptomycin 可抑制 NF-κB 訊號通路及促炎細胞激素，在 CIA 小鼠模型中緩解關節炎症狀——此為本案更具科學價值的研究方向（見下方概覽）。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

> **注意：以下所有文獻均為 Daptomycin 治療骨科相關感染的研究，並非退化性關節炎的直接療效研究。**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | 回溯性比較研究 | J Antimicrob Chemother | 評估 Daptomycin 對比標準療法治療金黃色葡萄球菌菌血症相關骨關節感染之臨床特性與預後 |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | 回溯性世代研究 | J Antimicrob Chemother | Daptomycin 治療髖、膝人工關節感染（PJI）的臨床療效與安全性分析 |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | 體外藥敏試驗 | J Antibiotics | 人工關節感染分離株（金黃色葡萄球菌、表皮葡萄球菌）的抗菌藥敏感性分析，包括 Daptomycin |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | 問卷調查 | Int J Antimicrob Agents | 556 位傳染病科醫師對 PJI 管理現況調查，Daptomycin 為常用選擇之一 |
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | 回溯性案例系列 | Int Orthop | 高劑量 Daptomycin 合併 Rifampicin 治療革蘭氏陽性骨關節感染的安全性與療效評估 |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | 回溯性微生物研究 | Surg Infect | 骨關節感染中葡萄球菌藥物敏感性的十年演變，含 Daptomycin 敏感率資料 |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | 回溯性世代研究 | Int J Antimicrob Agents | 高劑量 Daptomycin（>6 mg/kg）治療複雜骨關節及植入物相關感染的療效與安全性 |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | 登錄資料庫分析 | Med Clin | EU-CORE 資料庫分析：Daptomycin 在西班牙多中心臨床使用概況，含骨關節感染 |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | 案例報告 | Case Rep Orthop | 確診退化性關節炎患者轉介全膝置換術前發現 Corynebacterium striatum 化膿性關節炎，以 Daptomycin 治療 |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | 案例報告 | ASM Case Reports | 原生關節 Corynebacterium propinquum 化膿性關節炎首例報告，使用 Daptomycin 治療 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

以下為來自文獻記載的**已知重要安全性訊號**，在評估任何再利用方案時需特別考量：

- **橫紋肌溶解症（Rhabdomyolysis）**：Daptomycin 的已知副作用，可能繼發引發高尿酸血症及急性痛風發作（PMID [36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/)），使用期間需監測 CK 值
- **嗜酸性球肺炎（Eosinophilic Pneumonitis）**：需監測呼吸道症狀，尤其長療程使用
- 長期免疫調節使用的風險效益比目前完全未被評估

---

## 其他預測適應症概覽

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 | 重點說明 |
|------|------|-----------|---------|------|---------|
| 1 | 退化性關節炎 (Osteoarthritis) | 99.86% | L5 | Hold | 共病共現偏誤，非治療潛力 |
| **2** | **類風濕性關節炎 (Rheumatoid Arthritis)** | **99.84%** | **L4** | **Research Question** | **2025 年動物實驗顯示 NF-κB 抑制機轉，最具潛力** |
| 3 | 退化性關節炎易感性 (OA Susceptibility) | 99.79% | L5 | Hold | 無影響 OA 遺傳易感性機轉 |
| 4 | 痛風 (Gout) | 99.79% | L5 | Hold | 唯一文獻為 Daptomycin 誘發痛風的不良事件報告，方向相反 |
| 5 | 假性軟骨發育不全 (Pseudoachondroplasia) | 99.75% | L5 | Hold | COMP 基因突變先天異常，無相關機轉 |
| 6 | 肢端中段發育不全 Hunter-Thompson 型 | 99.68% | L5 | Hold | GDF5 基因突變，無相關機轉 |
| 7 | 短軀幹症 (Brachyolmia) | 99.67% | L5 | Hold | TRPV4/PAPSS2 基因相關骨骼異常，無相關機轉 |
| 8 | 短指-並指症候群 | 99.62% | L5 | Hold | 胚胎發育缺陷，非藥物可干預 |
| 9 | 眼缺損-小眼球-根性肢短症候群 | 99.61% | L5 | Hold | 超罕見先天異常，無任何機轉 |
| 10 | 短軀幹症合併牙釉質發育不全 | 99.61% | L5 | Hold | PAPSS2 相關，無機轉 |

### 🔬 類風濕性關節炎：最值得關注的研究方向

雖然 Daptomycin 對 RA 的預測排名第 2，但其科學依據遠優於排名第 1 的退化性關節炎：

- **[PMID 39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/)（2025）**：首次證明 Daptomycin 在 CIA 小鼠模型中可顯著抑制 NF-κB 訊號通路，降低 IL-6、TNF-α、IL-1β 等促炎細胞激素，緩解關節炎症狀
- **[PMID 40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/)（2025）**：基於 Daptomycin 結構設計的新型環狀脂肽衍生物（CLP-d2）在體外與動物實驗中展現更優異的抗 RA 效果，提示結構優化空間

**機轉假說**：Daptomycin 的脂肽結構可能干擾免疫細胞膜上的脂質筏（lipid raft）組成，影響訊號傳遞複合體，進而抑制 NF-κB 活化。此為新穎且值得追蹤的研究方向，但目前仍停留於動物模型階段（L4）。

---

## 結論與下一步

**決策：Hold**

**理由：**
首要預測適應症（退化性關節炎）的高 TxGNN 分數極可能源於共病共現偏誤——OA 患者術後常需 Daptomycin 治療感染，而非 Daptomycin 對 OA 本身有療效。10 篇文獻全數圍繞感染治療，無任何直接療效證據；加上香港目前無 Daptomycin 上市許可，缺乏在地監管基礎，本預測方向不建議推進。

**若要推進需要：**
- 優先評估**類風濕性關節炎**（排名第 2，L4 等級）而非退化性關節炎，因其具備初步動物實驗機轉支持
- 補充完整 MOA 資料（建議查詢 DrugBank API，DrugBank ID: DB00080）
- 補充香港衛生署核准仿單警語與禁忌症資料
- 針對 RA 研究方向，需設計分離抗菌效果與免疫調節效果的實驗設計
- 評估橫紋肌溶解症及嗜酸性球肺炎風險在長期免疫調節使用情境下的可接受性
- 探索 Daptomycin 衍生物（如 CLP-d2）作為降低抗菌副作用、保留免疫調節活性的結構優化路徑

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選均需經過嚴格臨床驗證方可應用於臨床。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

