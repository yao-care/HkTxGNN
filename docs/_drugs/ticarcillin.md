---
layout: default
title: Ticarcillin
parent: 僅模型預測 (L5)
nav_order: 877
evidence_level: L5
indication_count: 10
monitor_inn: "TICARCILLIN"
predicted_indications: ["lymph node palisaded myofibroblastoma", "abdominal cystic lymphangioma", "celiac trunk compression syndrome", "abdominal ectopic pregnancy", "sacrum chordoma", "disease of retroperitoneum", "urethral disease", "disease of uterine broad ligament", "disease of peritoneum", "pelvic varices"]
last_modified_at: 2026-10-23
description: "Ticarcillin：預測新適應症為淋巴結柵狀肌纖維母細胞瘤（證據等級 L5）。原適應症：香港許可證未提供核准適應症文字"
---

# Ticarcillin
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

## Ticarcillin：從細菌感染到淋巴結柵狀肌纖維母細胞瘤
{: .text-alpha }

## 一句話總結

Ticarcillin 是一種 β-內醯胺類（青黴素類）抗生素，在知識圖譜中記錄的原適應症以泌尿道感染、細菌性肺炎、葡萄球菌感染等為主。
TxGNN 模型預測分數最高的是**淋巴結柵狀肌纖維母細胞瘤**，但該預測沒有任何研究支持，機轉上也不合理。
本報告因此同時說明排名第 9、唯一有文獻佐證的**腹膜疾病 (Disease of Peritoneum)**：該項有 **0 個臨床試驗**和 **20 篇文獻**，但多為感染性腹膜炎的舊文獻，且大多為間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未提供核准適應症文字；知識圖譜記錄的關聯包括泌尿道感染、細菌性肺炎、葡萄球菌感染、骨盆腔炎、胸膜膿胸等（此為知識圖譜關聯，非核准適應症） |
| 預測新適應症（排名第 1） | 淋巴結柵狀肌纖維母細胞瘤 |
| TxGNN 預測分數（排名第 1） | 0.9982 |
| 證據等級（排名第 1） | L5 |
| 淋巴結柵狀肌纖維母細胞瘤 | 分數 0.9982，證據等級 L5（見下方說明） |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

**關於證據等級：** 排名第 9 的腹膜疾病有一批文獻，但多數為感染性腹膜炎（如 CAPD 腹膜炎、續發性腹膜炎）的研究，且試驗設計與結果未能核實。依規則，需有研究直接針對預測疾病本身才可評為 L1–L4，現有文獻針對的是感染性腹膜炎而非「腹膜疾病」整體，因此保守評為 L5。上述文獻仍是值得追蹤的研究線索。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ticarcillin 屬於青黴素類抗生素，一般認為其作用是抑制細菌細胞壁合成，與克拉維酸合用時可涵蓋產 β-內醯胺酶的菌株。

**排名第 1（淋巴結柵狀肌纖維母細胞瘤）：** 這是良性間質腫瘤，沒有細菌病因，抗生素沒有可作用的標靶。0.9982 的分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，也沒有臨床或文獻支持，機轉上不可信。

**其他高分預測：** 腹部囊性淋巴管瘤、腹腔動脈壓迫症候群、腹部異位妊娠、薦骨脊索瘤、骨盆腔靜脈曲張等，皆缺乏合理機轉，也無試驗或文獻。尿道疾病與子宮闊韌帶疾病的高分，則可能反映 TxGNN 模型（深度學習）學到的、與原有泌尿道感染、骨盆腔炎等疾病之間的相似性，並非生物學證據，也不是獨立的新適應症。

**排名第 9（腹膜疾病）：** 僅在感染性腹膜炎的範圍內具生物學合理性。Ticarcillin（尤其合併克拉維酸）可涵蓋腹腔內感染常見的革蘭氏陰性菌、厭氧菌及部分革蘭氏陽性菌。但原適應症已包含相近感染（骨盆腔炎、胸膜膿胸），這較像既有抗菌用途的延伸，而非真正的新藥再利用；對非感染性腹膜疾病則沒有依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為腹膜疾病（排名第 9）的主要文獻。因為文獻僅有標題與摘要片段，研究設計與結果未能核實，以下摘要為暫定。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2691475](https://pubmed.ncbi.nlm.nih.gov/2691475/) | 1989 | 臨床研究（設計未核實） | J Antimicrob Chemother | 50 例續發性腹膜炎患者以 ticarcillin/clavulanate 作為初始抗生素治療 |
| [1361796](https://pubmed.ncbi.nlm.nih.gov/1361796/) | 1992 | 臨床研究（設計未核實） | Adv Perit Dial | 14 位患者 16 次 CAPD 腹膜炎，腹腔內給予 ticarcillin/clavulanate 治療 10 天 |
| [3302345](https://pubmed.ncbi.nlm.nih.gov/3302345/) | 1987 | 臨床研究（設計未核實） | Jpn J Antibiot | 76 例腹腔內及膽道感染使用 ticarcillin/clavulanate 的臨床研究 |
| [2024225](https://pubmed.ncbi.nlm.nih.gov/2024225/) | 1991 | 文獻回顧／經驗報告 | Surg Gynecol Obstet | 長者腹腔內敗血症以 ticarcillin/clavulanate 取代含胺基糖苷類方案的經驗 |
| [9451930](https://pubmed.ncbi.nlm.nih.gov/9451930/) | 1998 | Review | World J Surg | 腹腔感染的抗生素治療總覽，涵蓋大腸桿菌及擬桿菌屬 |
| [16887592](https://pubmed.ncbi.nlm.nih.gov/16887592/) | 1997 | Review | Anaerobe | 腹腔內手術感染的細菌學與治療，強調手術處置為主、抗生素為輔 |
| [1734854](https://pubmed.ncbi.nlm.nih.gov/1734854/) | 1992 | 指引 | Arch Surg | 外科感染學會的腹腔內感染抗感染藥物指引 |
| [28849402](https://pubmed.ncbi.nlm.nih.gov/28849402/) | 2018 | Review（間接） | Clin Pharmacokinet | Temocillin（ticarcillin 衍生物）的藥動／藥效學 |
| [367159](https://pubmed.ncbi.nlm.nih.gov/367159/) | 1978 | 臨床與實驗室研究 | Am J Med Sci | 11 例厭氧菌相關嚴重感染以 carbenicillin 或 ticarcillin 治療，皆臨床治癒 |
| [2151488](https://pubmed.ncbi.nlm.nih.gov/2151488/) | 1990 | 前臨床（間接） | Scand J Infect Dis Suppl | 小鼠腹膜炎敗血症模型，模擬人類藥動學比較 netilmicin、ticarcillin、ceftazidime |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63780 | TICARCILLIN AND CLAVULANIC ACID POWDER FOR SOLUTION FOR INFUSION 3.2G（Ticarcillin 與克拉維酸複方，輸注用粉劑） | 未提供 | 未提供 |

此許可證為 Ticarcillin 與克拉維酸的複方產品（持證商：JINDUN PHARMA (H.K.) LIMITED），不能用來說明單一成分 Ticarcillin 的核准或上市狀況。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：腎臟疾病、輸尿管積膿、困難梭狀芽孢桿菌結腸炎、周產期壞死性腸炎、傳染性單核球增多症、慢性 EB 病毒感染症候群。
- **藥物交互作用**：共查得 23 筆，以下為主要項目：
  - 中度：四環素類（doxycycline、tetracycline、minocycline、demeclocycline、oxytetracycline）、胺基糖苷類（kanamycin、streptomycin、amikacin、gentamicin）、chloramphenicol、抗凝血藥（warfarin、dicoumarol）、ethinylestradiol、picosulfuric acid、放射性碘（I-123、I-131）
  - 輕度：clarithromycin、erythromycin、heparin

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測（淋巴結柵狀肌纖維母細胞瘤）及多數高分預測缺乏機轉合理性與任何研究證據，其分數來自 TxGNN 模型（深度學習），可能僅反映模型學到的相關疾病之間的相似性，並非生物學證據。
- 腹膜疾病雖有文獻，但僅限感染性腹膜炎，多為舊文獻且無登記試驗，屬於既有抗菌用途的延伸，不是新適應症。

**若要推進需要：**
- 取得香港仿單內容（核准適應症、警語、禁忌）。
- 補充作用機轉資料。
- 核實腹膜炎相關文獻的研究設計與結果，並釐清是否僅限於感染性腹膜炎。
- 評估這是否屬於現有抗菌用途的延伸，而非真正的再利用，再決定是否投入。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

