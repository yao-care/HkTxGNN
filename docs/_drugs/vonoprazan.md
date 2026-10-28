---
layout: default
title: Vonoprazan
parent: 僅模型預測 (L5)
nav_order: 941
evidence_level: L5
indication_count: 8
monitor_inn: "VONOPRAZAN"
predicted_indications: ["peptic ulcer perforation", "hiatus hernia (disease)", "achlorhydria", "pylorospasm", "Dieulafoy lesion", "cascade stomach", "gastric dilatation", "hemorrhagic duodenitis"]
last_modified_at: 2026-10-28
description: "Vonoprazan：預測新適應症為消化性潰瘍穿孔 (Peptic Ulcer Perforation)（證據等級 L5）。原適應症：香港許可證未載明適應症文字"
---

# Vonoprazan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Vonoprazan：從消化性潰瘍到消化性潰瘍穿孔
{: .text-alpha }

## 一句話總結

Vonoprazan 是一種鉀競爭型酸阻斷劑（P-CAB），知識圖譜中記錄其原本用於胃潰瘍、十二指腸潰瘍、食道炎與胃食道逆流症。
TxGNN 模型預測它可能對**消化性潰瘍穿孔 (Peptic Ulcer Perforation)** 有效，但目前**沒有臨床試驗**，僅有 **3 篇文獻**（皆為潰瘍一般性的指引或統合分析，並未直接研究穿孔）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症文字；知識圖譜記錄的關聯為胃潰瘍、十二指腸潰瘍、食道炎、胃食道逆流症 |
| 預測新適應症 | 消化性潰瘍穿孔 (Peptic Ulcer Perforation) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Vonoprazan 屬於鉀競爭型酸阻斷劑，透過抑制胃壁細胞的 H+/K+-ATP 酶來抑制胃酸分泌。知識圖譜記錄其與胃潰瘍、十二指腸潰瘍、食道炎及胃食道逆流症相關，日本、美國已有相關核准（香港許可證未載明適應症文字）。

消化性潰瘍穿孔是潰瘍的嚴重併發症。抑酸治療可能作為輔助手段，但主要處置是手術或內視鏡修補。現有文獻支持的是潰瘍的治療與預防，並未顯示對穿孔結局有幫助，因此這項關聯屬於透過「母疾病」的間接推論。

由於沒有研究直接探討 Vonoprazan 用於消化性潰瘍穿孔，證據等級依規則只能評為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39294424](https://pubmed.ncbi.nlm.nih.gov/39294424/) | 2024 | 統合分析 | Digestive Diseases and Sciences | 比較 Vonoprazan 與 PPI 治療及預防胃/十二指腸潰瘍的療效與安全性（僅涉及潰瘍，非穿孔） |
| [33620586](https://pubmed.ncbi.nlm.nih.gov/33620586/) | 2021 | 指引 | Journal of Gastroenterology | 日本消化器病學會 2020 年消化性潰瘍實證臨床指引 |
| [42635735](https://pubmed.ncbi.nlm.nih.gov/42635735/) | 2026 | 指引 | Journal of Gastroenterology | 2026 年第四版指引，涵蓋穿孔與狹窄的保守治療 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68731 | VOCINTI TABLETS 10MG | 未載明 | 未載明 |
| HK-68732 | VOCINTI TABLETS 20MG | 未載明 | 未載明 |

兩張許可證皆為單一成分製劑，持有者為 Takeda Pharmaceuticals (Hong Kong) Limited。

## 安全性考量

- **藥物交互作用**：資料中僅有藥理標靶紀錄（胃質子幫浦 ATP4A），未列出具體藥物間交互作用。
- **其他安全性觀察**：文獻中有個案報告提到長期使用 Vonoprazan 後出現胃黏膜變化與停藥後的反彈性胃酸分泌過多，屬於需留意的長期使用議題。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何研究直接探討 Vonoprazan 用於消化性潰瘍穿孔，證據僅為模型預測（L5）。
- 穿孔的主要處置是手術或內視鏡修補，抑酸藥最多是輔助角色，機轉上的連結間接。

**若要推進需要：**
- 取得 Vonoprazan 完整的作用機轉資料。
- 取得香港仿單的核准適應症、警語與禁忌。
- 針對穿孔術後或保守治療情境，設計或搜尋直接比較抑酸策略的研究。

### 其他預測適應症備註

- **裂孔疝**與**出血性十二指腸炎**有間接的觀察性研究或潰瘍試驗，但並非直接研究該疾病。
- **胃酸缺乏症**：Vonoprazan 會抑制胃酸，機轉上不支持使用，高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。
- **幽門痙攣、Dieulafoy 病灶、瀑布胃、胃擴張**：缺乏支持證據，不建議進一步投入。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

