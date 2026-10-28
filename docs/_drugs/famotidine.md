---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 4
monitor_inn: "FAMOTIDINE"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
last_modified_at: 2026-10-23
description: "Famotidine：預測新適應症為十二指腸阻塞 (duodenal obstruction)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Famotidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Famotidine: 十二指腸阻塞 (duodenal obstruction)
{: .text-alpha }

## 一句話總結

Famotidine 是 H2 受體拮抗劑，知識圖譜記錄的用途包括胃潰瘍、十二指腸潰瘍、胃食道逆流與 Zollinger-Ellison 症候群等胃酸相關疾病。
TxGNN 模型預測它可能對**十二指腸阻塞 (duodenal obstruction)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇個案報告**，且未直接研究 famotidine 對此疾病的療效，因此證據等級為 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 十二指腸阻塞 (duodenal obstruction) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Famotidine 屬於 H2 受體拮抗劑，一般認為可抑制胃酸分泌。

十二指腸阻塞有時與消化性潰瘍相關，抑制胃酸或許能緩解潰瘍相關症狀。但對固定的機械性阻塞（如狹窄、腫瘤、克隆氏症造成的narrowing），抑酸藥無法解除阻塞本身。

TxGNN 的高分（0.9999）較可能來自此疾病在知識網絡中與十二指腸潰瘍相近，而非直接的臨床證據。這屬於模型推論，不能視為已被證實的療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | Case report | Surgical Endoscopy | 胃空腸吻合術後的巨大邊緣潰瘍，可併發疼痛、出血、阻塞、穿孔與瘻管 |
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | Case report | Surgery Today | 十二指腸克隆氏症造成胃出口阻塞，以手術處理 |

這兩篇皆為個案報告，並未評估 famotidine 對十二指腸阻塞的療效。

## 香港上市資訊

下表僅列出 5 張許可證，清單可能不完整。許可證資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66450 | FAMOSIA TABLETS 40MG | 錠劑（40mg） | 資料未載明 |
| HK-47369 | ULCEDINE 40 TAB 40MG F.C. | 錠劑（40mg） | 資料未載明 |
| HK-48086 | FAMOLTA TAB 20MG | 錠劑（20mg） | 資料未載明 |
| HK-47874 | BALHOA TAB 40MG | 錠劑（40mg） | 資料未載明 |
| HK-48193 | COSODINE TAB 40MG | 錠劑（40mg） | 資料未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：腎臟疾病、腎功能不全、肝臟疾病、膽囊疾病、腎結石、便秘、腹瀉、胃癌（含胃腺癌、胃惡性腫瘤）等。這些來自知識圖譜，需對照原廠仿單確認。
- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分範例：
  - 中度：Abiraterone、Acalabrutinib、Tramadol、Amiodarone、Amitriptyline、Aripiprazole、Salbutamol、Aminophylline
  - 輕度：Alendronic acid、Aluminum hydroxide

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何直接研究 famotidine 用於十二指腸阻塞的臨床試驗或文獻，僅有模型預測與兩篇不相關的個案報告。
- 抑酸藥無法處理機械性阻塞，臨床價值有限。

**若要推進需要：**
- 取得 famotidine 的作用機轉資料
- 取得香港衛生署核准仿單的警語與禁忌
- 界定阻塞類型（潰瘍性水腫或機械性狹窄），評估抑酸治療是否有意義
- 以文獻或前瞻性研究檢驗 H2 阻斷劑對潰瘍相關十二指腸阻塞的輔助作用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

