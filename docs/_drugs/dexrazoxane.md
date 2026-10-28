---
layout: default
title: Dexrazoxane
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Dexrazoxane：預測新適應症為硬化性膽管炎 (Sclerosing Cholangitis)（證據等級 L5）。原適應症：資料中未提供"
monitor_inn: "DEXRAZOXANE"
predicted_indications: ["sclerosing cholangitis", "bronchitis", "paratyphoid fever", "conjunctivitis", "epiglottitis", "peritonitis", "laryngitis", "urinary tract infection (disease)", "pyelonephritis", "cystitis"]
---

# Dexrazoxane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Dexrazoxane：從心臟毒性防護到硬化性膽管炎
{: .text-alpha }

## 一句話總結

Dexrazoxane 是一種化療輔助用藥，在香港已有上市許可，但資料中沒有核准適應症文字可供引用。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，預測分數很高（0.9999）。
不過目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬於模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未提供 |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Dexrazoxane 為單方注射劑，一般被歸類為化療輔助用藥（chemoprotectant），文獻中也將其列於化療保護劑之列。就藥理特性而言，它具有鐵螯合及拓樸異構酶 II 抑制的作用，但這些屬於一般藥理知識，並非本次資料所確認的機轉。

針對硬化性膽管炎，理論上可推測：鐵螯合可能減輕膽管上皮的氧化與發炎損傷。但這純屬推測，目前沒有任何資料支持。分數雖高，仍只是計算模型的輸出。

其他排名較前的預測（支氣管炎、副傷寒、結膜炎、會厭炎、泌尿道感染等）多為感染或發炎性疾病，與 dexrazoxane 沒有明顯的機轉關聯，分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

**補充說明（其他預測適應症）：**
- **膀胱炎（排名 10，證據等級 L4）**：有間接的前臨床與綜述文獻。例如鐵死亡（ferroptosis）參與環磷醯胺引起的出血性膀胱炎（[PMID 37690746](https://pubmed.ncbi.nlm.nih.gov/37690746/)，2023）以及間質性膀胱炎（[PMID 41999537](https://pubmed.ncbi.nlm.nih.gov/41999537/)，2026）。Dexrazoxane 的鐵螯合特性理論上可能有關，但沒有研究直接證明其對膀胱炎有效，且出血性膀胱炎已有 mesna 作為標準用藥。僅屬值得做前臨床測試的假說。
- **腹膜炎（排名 6）**：檢索到的兩篇文獻（[PMID 39394070](https://pubmed.ncbi.nlm.nih.gov/39394070/)、[PMID 18566684](https://pubmed.ncbi.nlm.nih.gov/18566684/)）與 dexrazoxane 治療腹膜炎無關，應屬關鍵字巧合。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-54927 | CARDIOXANE FOR INJ 500MG | 未提供 | 未提供 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 化療輔助用藥，具拓樸異構酶 II 抑制作用 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容）：腎功能不全、非感染性腦膜炎。
- **藥物交互作用**：共查得 19 項，其中重大（Major）交互作用主要為活性減毒疫苗與相關生物製劑：
  - 活性疫苗：卡介苗（BCG）、麻疹、腮腺炎、德國麻疹、輪狀病毒、天花（痘苗）、傷寒（活）、黃熱病疫苗、水痘帶狀疱疹疫苗
  - 溶瘤病毒：Talimogene laherparepvec
- 中度（Moderate）交互作用包括：doxorubicin 與脂質體 doxorubicin、dimethyl fumarate 及其相關化合物（diroximel fumarate、monomethyl fumarate）、腺病毒疫苗、霍亂活疫苗，以及益生菌（Bifidobacterium longum infantis、Lactobacillus acidophilus）。

仿單的警語與禁忌資料尚未取得，其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 硬化性膽管炎的預測僅來自模型，沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 作用機轉與香港仿單的警語、禁忌資料均缺漏，目前無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌、核准適應症）
- 補充 DrugBank 的作用機轉資料
- 針對硬化性膽管炎進行系統性文獻回顧與前臨床（如鐵螯合／氧化損傷模型）驗證
- 若有興趣，可另將膀胱炎（鐵死亡假說）列為前臨床研究題目
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

