---
layout: default
title: Piperacillin
parent: 中證據等級 (L3-L4)
nav_order: 590
evidence_level: L4
indication_count: 5
---

# Piperacillin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Piperacillin：從細菌感染到類風濕性關節炎

## 一句話總結

Piperacillin 是一種 β-lactam 類廣效抗生素，原用於治療細菌感染。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
目前有 **18 篇文獻**支持，但經檢視後，文獻內容並未實際證明其對 RA 本身具治療效果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（原適應症詳細資料缺失，香港無許可證登記可查） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Piperacillin 完整的作用機轉資料（DrugBank MOA 欄位為資料缺失）。根據藥物分類與文獻中片段描述，Piperacillin 屬於 β-lactam 類抗生素，透過抑制細菌細胞壁合成達到殺菌效果，本身不具抗發炎或免疫調節機轉。

現有的 18 篇 PubMed 文獻，內容並非「Piperacillin 治療 RA」的直接證據，而是描述 RA 病人在接受免疫抑制治療（如 etanercept、methotrexate、JAK1 抑制劑 upadacitinib）期間，因免疫功能低下併發細菌感染（化膿性心包炎、人工關節感染、蜂窩性組織炎、敗血性休克等），進而使用 piperacillin（多與 tazobactam 併用）治療感染併發症的個案報告。

因此，這個預測反映的較可能是「RA 患者常見感染併發症的共同治療模式」在知識圖譜中的共現關聯，而非 piperacillin 對 RA 疾病本身具有藥理學上的治療潛力。TxGNN 的高分數不應直接解讀為機轉合理性的證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2025 | Cohort | Br J Clin Pharmacol | 建立 ampicillin/sulbactam 或 piperacillin/tazobactam 誘發嗜酸性球增多的風險預測模型（非 RA 相關） |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Ann Transl Med | 抗生素相關藥物性肝損傷之盛行率與臨床特徵 |
| [38169875](https://pubmed.ncbi.nlm.nih.gov/38169875/) | 2023 | Case Series | Clin Nephrol Case Stud | 鈣化防禦症之眼部缺血性表現案例（非 RA） |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case Report | Cureus | RA 緩解 9 年後復發性胸腔積液個案 |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case Report | Orthopadie | RA 病人人工膝關節 H. influenzae 感染，以 piperacillin/tazobactam 治療併發肺炎 |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case Report | Proc (Bayl Univ Med Cent) | RA 病人低劑量 methotrexate 毒性致全血球減少 |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case Report | Cureus | RA 病人低劑量 methotrexate 引發全血球減少 |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case Report | BMJ Case Rep | RA 病人 etanercept 治療併發化膿性心包炎，以 piperacillin-tazobactam 經驗性治療 |
| [29390256](https://pubmed.ncbi.nlm.nih.gov/29390256/) | 2017 | Case Report | Medicine | 修格蘭氏症候群併發全血球減少、腦出血個案 |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Case Report | BMC Infect Dis | 抗藥性 Edwardsiella tarda 引發敗血性休克個案 |

以上文獻多為感染併發症之個案報告，**未提供 piperacillin 直接治療 RA 疾病本身的證據**。

---

## 香港上市資訊

Piperacillin 目前**未於香港上市**，查無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語與禁忌症資料缺失，屬 Blocking 等級資料缺口，無法進行 S1 安全性初評）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 18 篇文獻中無一篇直接證明 piperacillin 對 RA 疾病本身有治療效果，皆為 RA 患者因免疫抑制治療併發細菌感染而使用抗生素之個案，屬共病共現而非機轉證據。
- 無任何臨床試驗登記，且藥物作用機轉（細胞壁合成抑制）與 RA 病理（自體免疫發炎）無生物學合理性。
- 香港未上市、無許可證資料，且 TFDA 仿單安全性資料缺失（Blocking），無法進行安全性初評。
- 其餘四個預測適應症（rank 2-5：coloboma-microphthalmia 症候群、短指併指症候群、硬化性膽管炎、骨關節炎易感性）皆為 L5 等級，無任何文獻或試驗支持，判斷為模型嵌入相似性雜訊。

**若要推進需要：**
- 補齊 DrugBank 作用機轉（MOA）資料
- 取得 TFDA/原廠仿單完整警語與禁忌症資料，解除 Blocking 缺口
- 若仍考慮此方向，需要體外或動物模式的機轉研究，證明 piperacillin 對 RA 發炎路徑的直接作用，而非僅止於感染併發症治療的共現關聯
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

