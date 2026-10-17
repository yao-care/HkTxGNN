---
layout: default
title: Vitamin A
parent: 僅模型預測 (L5)
nav_order: 939
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vitamin A：預測新適應症為先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)（證據等級 L5）。原適應症：維生素缺乏症、維生素 A 缺乏症"
monitor_inn: "Vitamin A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "segmental odontomaxillary dysplasia", "perinatal disease", "florid cemento-osseous dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
---

# Vitamin A
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

# Vitamin A：從維生素缺乏症到先天性凝血酶原缺乏症

## 一句話總結

Vitamin A（維生素 A）原本用於治療維生素缺乏症與維生素 A 缺乏症。
TxGNN 模型預測分數最高的新適應症是**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)**，但目前**沒有任何臨床試驗或文獻**支持，生物學上也不合理。
本報告另整理證據相對較多的「**圍產期疾病 (Perinatal Disease)**」（極低出生體重早產兒）與「**損傷 (Injury)**」方向，供參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素缺乏症、維生素 A 缺乏症（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知維生素 A 及其代謝物（視黃酸）透過 RAR/RXR 核受體調節細胞分化、增殖與上皮組織維持，並為視覺所必需。

就排名第一的先天性凝血酶原缺乏症而言，這項預測**在生物學上不合理**。凝血酶原的合成依賴維生素 K 的 γ-羧化作用，與維生素 A 無已知關聯；此病是 F2 基因缺陷所致，補充維生素 A 不太可能有效。高分應視為圖譜運算的結果，而非真實的治療訊號。

其他預測中，機轉較具支持的是：
- **圍產期疾病**：維生素 A 對肺上皮發育與修復必要，早產兒體內儲備不足，與支氣管肺發育不良 (BPD) 風險相關。
- **損傷**：視黃醇訊號支持上皮再生、膠原合成與發炎調節（傷口癒合）。

---

## 臨床試驗證據

排名第一的預測（先天性凝血酶原缺乏症）：目前無相關臨床試驗登記。

以下為證據較多的替代方向的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01203488](https://clinicaltrials.gov/study/NCT01203488) | Phase 1/2 | 完成 | 807 | 極低出生體重兒給予較高劑量維生素 A，評估無 BPD 存活率與敗血症風險（損傷方向） |
| [NCT02102711](https://clinicaltrials.gov/study/NCT02102711) | 未分期 | 完成 | 62 | 體重 <1500 g 新生兒口服維生素 A，預防 BPD 與早產兒視網膜病變（損傷方向） |
| [NCT01115478](https://clinicaltrials.gov/study/NCT01115478) | 未分期 | 完成 | 2500 | 鋅和/或維生素 A 補充，降低妊娠期胎盤瘧疾及不良妊娠結果（圍產期方向，僅間接相關） |
| [NCT04000789](https://clinicaltrials.gov/study/NCT04000789) | 未分期 | 未知 | 96 | 維生素 A + E + 玻尿酸滴眼液用於糖尿病視網膜病變患者的乾眼（細胞增生異常方向，相關性低） |

---

## 文獻證據

排名第一的預測：目前無相關文獻。

以下為替代方向中較具代表性的文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27552058](https://pubmed.ncbi.nlm.nih.gov/27552058/) | 2016 | 系統性回顧/Meta 分析 | Cochrane Database Syst Rev | 極低出生體重兒補充維生素 A，預防死亡與短、長期併發症 |
| [21975731](https://pubmed.ncbi.nlm.nih.gov/21975731/) | 2011 | 系統性回顧/Meta 分析 | Cochrane Database Syst Rev | 同上（早期版本），維生素 A 與慢性肺病風險 |
| [17943744](https://pubmed.ncbi.nlm.nih.gov/17943744/) | 2007 | 系統性回顧/Meta 分析 | Cochrane Database Syst Rev | 同上（早期版本） |
| [25222155](https://pubmed.ncbi.nlm.nih.gov/25222155/) | 2014 | Review | JAMA Pediatrics | 維生素 A 不足與支氣管肺發育不良風險 |
| [34105132](https://pubmed.ncbi.nlm.nih.gov/34105132/) | 2021 | Meta 分析 | J Spec Oper Med | 維生素 A 攝取與骨折風險的關聯（安全性訊號） |
| [31697447](https://pubmed.ncbi.nlm.nih.gov/31697447/) | 2019 | Review | Nutr Clin Pract | 維生素 A 與傷口癒合 |
| [34181622](https://pubmed.ncbi.nlm.nih.gov/34181622/) | 2021 | Review | Plast Reconstr Surg | 傷口護理的營養介入；維生素與礦物質證據有限 |
| [40901583](https://pubmed.ncbi.nlm.nih.gov/40901583/) | 2025 | Review | World J Hepatol | 維生素 A 毒性與肝臟病變 |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterol Clin North Am | 發炎性腸道疾病的維生素與礦物質；維生素 A 結果不如預期 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61308 | VITAMIN A&D CAP | 未載明 | 未載明 |
| HK-36206 | VITALIPID N ADULT INJ | 未載明 | 未載明 |
| HK-36205 | VITALIPID N INFANT INJ | 未載明 | 未載明 |
| HK-56452 | CERNEVIT FOR INJ | 未載明 | 未載明 |
| HK-01178 | POLIBABY CREAM | 未載明 | 未載明 |

另有 3 張許可證（共 8 張，皆為有效單方）：獸用注射液 ADECON、AMINOLEBAN EN POWDER 與 AMINOLEBAN ORAL POWDER。

---

## 安全性考量

- **知識圖譜標示的禁忌/慎用疾病**（非仿單內容）：腎臟疾病、肝臟疾病、膽囊疾病、消化性潰瘍、結節病、高鈣血症、腎鈣化症、腎結石、鐵代謝疾病（血色素沉著症等）、威爾森氏症、潰瘍性結腸炎、發炎性腸道疾病、溶血性貧血、鐮刀型貧血、維生素過多症等。
- **藥物交互作用**：共 68 筆，主要包括：
  - 重度：Isotretinoin、Acitretin、Tretinoin（視黃酸類，疊加毒性）；Doxycycline、Tetracycline、Minocycline、Omadacycline、Demeclocycline、Eravacycline、Oxytetracycline、Sarecycline（四環黴素類）
  - 中度：Bexarotene、Cholestyramine、Colesevelam、Colestipol、Sevelamer、Selpercatinib
  - 輕度：Orlistat
- **文獻中的安全訊號**：高劑量與骨折風險（PMID 34105132）及肝毒性（PMID 40901583）；過量維生素 A 亦具致畸性。

仿單的警語與禁忌資料目前缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（先天性凝血酶原缺乏症）無任何研究支持，且機轉上不合理；TxGNN 高分僅反映圖譜關聯。
- 證據較多的是早產兒（圍產期）方向，但屬既有用途的劑量、途徑與族群優化問題，不是真正的新適應症，且效益有限。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字
- 補齊作用機轉 (MOA) 資料
- 若聚焦早產兒 BPD，需比較劑量、給藥途徑（如肌肉注射的可行性）與目標族群
- 針對骨骼、肝臟毒性及與視黃酸類、四環黴素類藥物的交互作用，制定監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

