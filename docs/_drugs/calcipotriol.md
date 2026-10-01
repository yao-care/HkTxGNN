---
layout: default
title: Calcipotriol
parent: 中證據等級 (L3-L4)
nav_order: 143
evidence_level: L3
indication_count: 10
---

# Calcipotriol
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Calcipotriol：從原適應症資料未載明到脂漏性角化症 (Seborrheic Keratosis)

## 一句話總結

Calcipotriol 是外用維生素 D3 類似物，在香港已有 13 張許可證，但本次資料中沒有載明原核准適應症。
TxGNN 模型預測它可能對**脂漏性角化症 (Seborrheic Keratosis)** 有效。
目前**沒有登記的臨床試驗**，只有 **6 篇文獻**，多為病例系列或個案報告，證據等級 L3。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（許可證與藥物資料均無適應症文字） |
| 預測新適應症 | 脂漏性角化症 (Seborrheic Keratosis) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。從預測理由推論，Calcipotriol 是維生素 D 受體 (VDR) 促效劑，可調控角質細胞的增生與分化，也可能誘導細胞凋亡。

脂漏性角化症是良性的表皮過度增生病變，好發於年長者。在機轉上，這與 VDR 調控角質細胞的作用方向一致。外用維生素 D 類似物本來就常用於發炎性角化皮膚病，例如乾癬。

但現有證據結果不一。2005 年的系列報告與 2023 年的病例系列描述有改善，2004 年的比較研究則被認為療效有限。其中 2023 年與 2004 年研究的設計是僅從標題推斷，需要查閱全文確認。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | 病例系列 | Australas J Dermatol | 12 名臉部單發脂漏性角化症患者外用 0.005% calcipotriol 軟膏 3–8 個月，病灶完全消退，追蹤 6–10 年未復發 |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | 比較性臨床研究 | Int J Dermatol | 比較標準冷凍手術與外用 calcipotriene、tazarotene、imiquimod；摘要未載結果，另有評估指出療效有限，需查全文 |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | 小型臨床系列 | J Dermatol | 116 例老年疣（即脂漏性角化症）外用維生素 D3 軟膏（含 calcipotriol）3–12 個月，其中 35 例（30.2%）有反應（摘要截斷），並推測與誘導細胞凋亡有關 |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | 簡短回顧 | Clin Calcium | 以活性維生素 D3 外用治療老年疣的簡短報告（摘要截斷，詳細結果待查全文） |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | 個案報告 | J Dermatol | 相關角化性疾病（苔蘚樣慢性角化症）對 calcipotriol 軟膏有明顯反應 |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | 臨床個案 | JAAPA | 小腿脂漏性角化症的臨床個案介紹，無摘要，與 calcipotriol 療效的關聯有限 |

## 香港上市資訊

共 13 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68704 | BF-CALCIPOTRIOL OINTMENT 0.005% W/W | Bright Future Pharmaceutical Co. Limited |
| HK-55517 | CIPOTRIOL OINTMENT 0.005% | Bright Future Pharmaceuticals Factory |
| HK-35877 | DAIVONEX OINT 50MCG/G | DKSH Hong Kong Limited |
| HK-59632 | XAMIOL GEL | DKSH Hong Kong Limited |
| HK-68653 | BF-CALBETSONE OINTMENT | Bright Future Pharmaceuticals Factory |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有病例系列與個案報告，沒有登記中的臨床試驗，且已有文獻對療效的判斷不一致。
- 香港衛生署仿單的警語與禁忌資料缺失，且被標記為阻擋性缺口，暫時無法進入安全性篩選。
- 本藥是已上市的外用製劑，安全性背景較明確，之後若補齊資料，適合以小型對照試驗驗證。

**若要推進需要：**
- 下載並解析香港衛生署仿單，補齊警語與禁忌症。
- 取得 2023 年病例系列與 2004 年比較研究的全文，確認研究設計與實際結果。
- 補充 DrugBank 的作用機轉資料。
- 設計小型對照試驗，例如與冷凍手術或安慰劑比較，評估療效與局部刺激。

**其他預測適應症：**
排名 2–10 的預測（外陰及乳房相關疾病、骨 Paget 病等）證據等級為 L4–L5，目前均建議 Hold。其中外陰炎（vulvitis）僅有外陰乾癬的間接證據，外陰腫瘤（vulvar neoplasm）僅有個案層級報告。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

