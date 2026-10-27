---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Folic Acid：預測新適應症為生物素代謝疾病 (Biotin Metabolic Disease)（證據等級 L5）。原適應症：維生素缺乏症、葉酸缺乏性貧血、缺鐵性貧血"
monitor_inn: "FOLIC ACID"
predicted_indications: ["biotin metabolic disease"]
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Folic Acid：從葉酸缺乏性貧血到生物素代謝疾病
{: .text-alpha }

## 一句話總結

Folic Acid（葉酸）是維生素 B9，原本用於治療維生素缺乏症及各類貧血（如葉酸缺乏性貧血、缺鐵性貧血）。
TxGNN 模型預測它可能對**生物素代謝疾病 (Biotin Metabolic Disease)** 有效，
但目前**沒有臨床試驗**，僅有 **20 篇文獻**（多為維生素相關的綜述，並非直接驗證此用途），證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素缺乏症、葉酸缺乏性貧血、缺鐵性貧血（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 生物素代謝疾病 (Biotin Metabolic Disease) |
| TxGNN 預測分數 | 99.49% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知葉酸是 B 族維生素，在體內作為一碳單位的載體，參與甲基化反應與核苷酸合成，因此可用於治療葉酸缺乏及相關貧血。

生物素（維生素 B7）是另一種獨立的 B 族維生素，作為羧化酶的輔因子。兩者的關聯主要在於同屬 B 族維生素代謝，以及「維生素反應性疾病」的概念層次。目前沒有已知的直接機轉路徑，顯示葉酸可以矯正生物素代謝缺陷（例如生物素酶缺乏症或全羧化酶合成酶缺乏症）。

TxGNN 的高分（99.49%）較可能反映知識圖譜中維生素與代謝疾病節點之間的接近性，而非經過驗證的治療機轉。因此這項預測應視為假說，而非有實證支持的結論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表列出較相關的文獻（均為綜述、世代研究或其他類型，無針對此預測的 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | 回顧維生素反應性疾病，包括鈷胺素、葉酸、生物素等的缺乏與先天代謝異常 |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | International Journal of Molecular Sciences | 探討維生素 B12 缺乏與神經系統，提及 B12、生物素與葉酸相關的代謝反應 |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | B 族維生素在皮膚科的角色，及其於細胞代謝與紅血球生成的功能 |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | 維生素與第 2 型糖尿病的關係，糖尿病患者的硫胺素、吡哆醇、生物素濃度較低 |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine, Metabolic & Immune Disorders Drug Targets | 評估個別或合併維生素與第 2 型糖尿病的關係 |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | 回顧維生素與代謝疾病的關聯，包括吸收不良、代謝錯誤及維生素依賴症候群 |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Archives of Biochemistry and Biophysics | 微量營養素缺乏（含葉酸、B12、B6）可能造成 DNA 損傷，主張補充以優化代謝 |
| [38350491](https://pubmed.ncbi.nlm.nih.gov/38350491/) | 2025 | Cohort | Nutrition Reviews | 嚴重消瘦或營養性水腫兒童的微量營養素狀態 |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | 動物研究 | Biologica Latina | 大鼠實驗中誘發維生素 H（生物素）缺乏及生物素合併葉酸缺乏 |
| [16183151](https://pubmed.ncbi.nlm.nih.gov/16183151/) | 2006 | 動物研究 | International Journal of Cardiology | 葉酸可降低高同半胱胺酸血症大鼠主動脈的 VCAM-1 表現 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61899 | FILICIN TABLETS 5MG | 未載明 | 未載明 |
| HK-25293 | FOLIC ACID TAB 5MG | 未載明 | 未載明 |
| HK-11525 | FOLIC ACID TAB 5MG | 未載明 | 未載明 |
| HK-67727 | FOLDA TABLETS 5MG | 未載明 | 未載明 |
| HK-51107 | FOLICIL TAB 5MG | 未載明 | 未載明 |

另有 6 張單方許可證（共 11 張，皆為有效）：HK-43342（FOLIFER TAB）、HK-36207（SOLUVIT N INJ）、HK-51439（FEROFORT TAB）、HK-56452（CERNEVIT FOR INJ）、HK-52479（AMINOLEBAN EN POWDER）、HK-54177（AMINOLEBAN ORAL POWDER）。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容，僅供參考）：腎臟病、糖尿病、糖尿病酮酸中毒、消化性潰瘍、發炎性腸道疾病、潰瘍性結腸炎、鐮刀型貧血、溶血性貧血、遺傳性血色素沉著症、威爾森氏症、腎結石、高鈣血症、副甲狀腺機能亢進、結節病、雙相情緒障礙等，共 30 項。這些資料來自圖譜推論，臨床意義需對照正式仿單確認。
- **藥物交互作用**：資料庫共記載 100 筆。其中被列為中度的有 Pancrelipase；輕度的有 Sulfasalazine。其餘多數（如 Metformin、Omeprazole、Pantoprazole、Prednisone、Simvastatin 等）等級為未知。

其餘警語與禁忌的仿單資料目前缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型推論（L5），沒有任何臨床試驗，文獻也未直接支持葉酸治療生物素代謝疾病，機轉上亦無明確連結。
- 高分較可能反映維生素節點在知識圖譜中的鄰近關係，不宜視為療效證據。

**若要推進需要：**
- 釐清葉酸與生物素代謝缺陷（如生物素酶缺乏症、全羧化酶合成酶缺乏症）之間是否存在可驗證的機轉路徑
- 補充葉酸的作用機轉資料
- 取得香港衛生署核准的仿單，確認適應症、警語與禁忌
- 進行針對性的文獻回顧或前臨床研究，再評估是否值得啟動臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

