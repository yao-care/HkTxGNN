---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aztreonam：預測新適應症為多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)（證據等級 L5）。原適應症：泌尿道感染、綠膿桿菌感染、腹膜炎、大腸桿菌感染、子宮內膜炎等"
monitor_inn: "AZTREONAM"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
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

## Aztreonam：從泌尿道感染等革蘭氏陰性菌感染到淋病性尿道炎
{: .text-alpha }

## 一句話總結

Aztreonam 是單環 β-內醯胺（monobactam）類抗生素，原本用於泌尿道感染、綠膿桿菌感染、腹膜炎、大腸桿菌感染等革蘭氏陰性菌感染。
TxGNN 模型排名第一的預測是**多株性高黏滯症候群 (polyclonal hyperviscosity syndrome)**，但此預測缺乏機轉與臨床依據，應視為模型的圖譜假象。
在前 10 名預測中，證據相對最合理的是**淋病性尿道炎 (gonococcal urethritis)**，目前有 **6 篇文獻**，但**無已登記的臨床試驗**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染、綠膿桿菌感染、腹膜炎、大腸桿菌感染、子宮內膜炎等（香港許可證未載明適應症文字） |
| 預測新適應症（排名第一） | 多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5（排名第一的預測僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

> 補充：排名第 4 的淋病性尿道炎（TxGNN 分數 99.59%）證據等級為 L3，屬較值得進一步研究的方向，詳見下文。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Aztreonam 屬於單環 β-內醯胺類抗生素，作用是結合青黴素結合蛋白 3（PBP3），抑制革蘭氏陰性需氧菌的細胞壁合成，對許多 β-內醯胺酶也相對穩定。

**排名第一的預測（多株性高黏滯症候群）：** 這是血液／蛋白質異常疾病，沒有細菌作為治療目標，機轉上找不到合理連結。99.73% 的高分較可能來自知識圖譜的結構性關聯，而非真實生物學。排名第 2 至 3 的高澱粉酶血症（實驗室指標異常）與先天性無白蛋白血症（遺傳性蛋白合成疾病）同樣缺乏機轉依據。

**較合理的預測（淋病性尿道炎）：** 淋病奈瑟菌為革蘭氏陰性菌，Aztreonam 對其有活性，且與其原有的泌尿道感染適應症屬同類型感染，機轉上說得通。不過，目前臨床指引的標準療法與抗藥性問題，限制了臨床優先性。

**其他需注意的預測：**
- **Ureaplasma 尿道炎**：Ureaplasma 沒有細胞壁，β-內醯胺類理論上天生無效，機轉上不可行。
- **會厭炎、黏滯性腎盂腎炎（xanthogranulomatous pyelonephritis）**：僅能間接推論（致病菌多為革蘭氏陰性菌），但既有標準療法已足夠，且後者以手術為主。
- **單株性γ球蛋白病、血型不合、癌前血液疾病**：無直接機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為排名第一的預測以外、證據相對最多的**淋病性尿道炎**之文獻（排名第一的預測無任何文獻）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | 單臂開放標示臨床試驗 | Antimicrob Agents Chemother | 男性單次肌肉注射 2 g Aztreonam 治療淋病的試驗，探討作為替代療法的可能性 |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | 臨床研究 | Antimicrob Agents Chemother | 1 g 肌肉注射 Aztreonam 與 Spectinomycin 比較，無治療失敗，適用於男性單純性尿道淋病 |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | 臨床研究 | Genitourin Med | 單次 1 g 肌肉注射，61 位男性與 26 位女性除一例咽部感染外皆清除感染，對抗藥與敏感菌株皆有效 |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | 臨床／流行病學研究 | Hinyokika Kiyo | 淋病感染的流行病學及 Aztreonam 單次給藥治療研究 |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | 體外／臨床效果研究 | J Infect Dis | Aztreonam 對產青黴素酶淋病菌株有效 |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | 抗藥性／微生物學研究 | J Infect Chemother | 出現對頭孢類與 Aztreonam 高度抗藥、且不產 β-內醯胺酶的淋病菌株 |

其他預測中有少量間接文獻：會厭炎（[3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/)，1986，兒童嚴重革蘭氏陰性菌感染開放試驗，僅間接相關）、單株性γ球蛋白病（[4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/)，1985，血液疾病合併嚴重感染，僅支持其抗感染用途）。血型不合所對應的一篇文獻（PMID 34956120）屬抗藥基因研究，因關鍵字相近而被檢索到，並非支持證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68891 | EMBLAVEO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1.5G/0.5G（Pfizer Corporation Hong Kong Limited） | — | — |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、支氣管疾病（此為圖譜關聯，並非仿單文字）。
- **藥物交互作用**：共查得 27 筆。中度等級包括 Picosulfuric acid、Dicoumarol、Warfarin（與抗凝血劑併用需留意凝血功能）。其餘如 Vancomycin、Amikacin、Amphotericin B、Tacrolimus、Heparin、Acyclovir 等多筆等級未明。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（多株性高黏滯症候群）沒有機轉、臨床試驗或文獻支持，高分可能只是圖譜假象，證據等級為 L5。
- 前 10 名中僅淋病性尿道炎有較具體證據（L3），但多為非隨機且較早期的研究，並有抗藥性報告，且現行指引療法已存在，臨床優先性有限。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA）
- 取得香港仿單的警語、禁忌與核准適應症
- 若要探索淋病性尿道炎，需評估與現行指引療法的比較、當地抗藥性流行情況，以及設計隨機對照試驗
- 對其他預測（尤其是機轉不可行者，如 Ureaplasma 尿道炎）不建議投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

