---
layout: default
title: Magnesium Hydroxide
parent: 僅模型預測 (L5)
nav_order: 549
evidence_level: L5
indication_count: 1
monitor_inn: "MAGNESIUM HYDROXIDE"
predicted_indications: ["stomach disease"]
last_modified_at: 2026-10-28
description: "Magnesium Hydroxide：預測新適應症為胃部疾病 (Stomach Disease)（證據等級 L5）。原適應症：知識圖譜記錄：消化性潰瘍、胃食道逆流、食道炎、便秘、消化不良"
---

# Magnesium Hydroxide
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

## 氫氧化鎂：從消化性潰瘍與胃食道逆流到胃部疾病
{: .text-alpha }

## 一句話總結

氫氧化鎂是常見的制酸劑，在知識圖譜中記錄的原有用途包括消化性潰瘍、胃食道逆流、食道炎、便秘與消化不良。
TxGNN 模型預測它可能對**胃部疾病 (Stomach Disease)** 有效，但這是一個涵蓋範圍很廣的上位疾病類別，與原有用途高度重疊。
目前沒有臨床試驗登記，另有 **20 篇文獻**，多為制酸劑在潰瘍與消化不良的間接證據，沒有直接針對「胃部疾病」本身的研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄：消化性潰瘍、胃食道逆流、食道炎、便秘、消化不良（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 胃部疾病 (Stomach Disease) |
| TxGNN 預測分數 | 0.9923 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的制酸劑藥理，氫氧化鎂能中和胃酸、提高胃內 pH 值，因此機轉上可用於與胃酸相關的胃部不適。

「胃部疾病」是範圍很廣的上位分類，涵蓋消化性潰瘍、胃食道逆流、消化不良等知識圖譜中已記錄的用途。因此 0.99 的高分，較可能反映疾病分類架構上的重疊，而不是一個新的藥物再利用訊號。

現有文獻多為制酸劑（常與氫氧化鋁合用）在潰瘍與消化不良的研究，屬於同一機轉的間接證據。沒有任何一篇研究直接以「胃部疾病」作為研究對象，因此證據等級依規則定為 L5。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為與氫氧化鎂或含氫氧化鎂制酸劑相關、且與胃部疾病較貼近的代表性文獻（多數為複方制酸劑，並非單方氫氧化鎂的直接證據）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1763561](https://pubmed.ncbi.nlm.nih.gov/1763561/) | 1991 | 隨機雙盲對照試驗 | Z Gastroenterol | 低劑量制酸劑與 misoprostol 比較，用於十二指腸潰瘍的癒合與症狀緩解（100 名病人） |
| [6992456](https://pubmed.ncbi.nlm.nih.gov/6992456/) | 1980 | 臨床試驗 | Vutreshni Bolesti | 保加利亞複方制酸劑用於 100 名十二指腸潰瘍病人，疼痛緩解 60–68%，氫氧化鎂劑量較高者便秘症狀改善較多 |
| [3903784](https://pubmed.ncbi.nlm.nih.gov/3903784/) | 1985 | 對照臨床研究 | Pharmatherapeutica | 氫氧化鋁加氫氧化鎂制酸劑，與併用 triletide 比較，用於 30 名胃或十二指腸潰瘍門診病人 |
| [3213266](https://pubmed.ncbi.nlm.nih.gov/3213266/) | 1988 | 臨床研究 | Z Rheumatol | 21 名持續使用 NSAID 的病人，以 ranitidine 加制酸劑治療，胃或十二指腸潰瘍仍可癒合 |
| [3604202](https://pubmed.ncbi.nlm.nih.gov/3604202/) | 1987 | 臨床研究 | Vutreshni Bolesti | 含氫氧化鎂的複方製劑 gastralgin 用於 20 名十二指腸潰瘍病人，50–80% 的症狀獲得改善 |
| [236651](https://pubmed.ncbi.nlm.nih.gov/236651/) | 1975 | 回顧 | Am J Hosp Pharm | 說明制酸劑在酸相關消化性疾病的藥理與臨床用法 |
| [6755653](https://pubmed.ncbi.nlm.nih.gov/6755653/) | 1982 | 回顧 | Scand J Gastroenterol Suppl | 制酸劑可促進潰瘍癒合並預防壓力性潰瘍出血，並討論胃泌素釋放與酸反彈 |
| [6293043](https://pubmed.ncbi.nlm.nih.gov/6293043/) | 1982 | 回顧 | Scand J Gastroenterol Suppl | 制酸劑治療對礦物質代謝的影響與副作用 |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | 動物實驗（大鼠） | Scand J Gastroenterol | 含氫氧化鋁與氫氧化鎂的制酸劑對急性胃黏膜損傷具保護作用 |
| [8641951](https://pubmed.ncbi.nlm.nih.gov/8641951/) | 1996 | 臨床藥理（馬） | J Am Vet Med Assoc | 氫氧化鋁/氫氧化鎂制酸劑與 bismuth subsalicylate 對馬胃內 pH 的影響 |

---

## 香港上市資訊

下列為資料中列出的部分許可證（共至少 20 張，清單可能不完整），均為單方製劑。資料中未載明核准適應症與劑型。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43990 | MAGNESIUM HYDROXIDE | 未載明 | 未載明 |
| HK-58779 | PEDIA-LAX CHEWABLE TAB 400MG | 未載明 | 未載明 |
| HK-46908 | LANTACID (S) TAB CHEWABLE | 未載明 | 未載明 |
| HK-30455 | LANTACID TAB (APPLE GREEN) CHEWABLE | 未載明 | 未載明 |
| HK-05470 | SMA SUSPENSION | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜記錄的禁忌疾病（非仿單內容）**：腎臟疾病、腎功能不全、肝病、膽囊疾病、高血鈣、腎結石、腎鈣化、磷代謝異常、低磷血症、腹瀉、闌尾炎、腸道阻塞（糞便嵌塞）、痔瘡、胃癌相關疾病等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 嚴重 (Major)：Dolutegravir
  - 中度：Doxycycline、Alendronic acid、Amiodarone、Hydrochlorothiazide、Tramadol、Acetazolamide
  - 輕微：Famotidine、Ranitidine、Ibuprofen

其他安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 「胃部疾病」是涵蓋範圍很廣的上位分類，高分較可能反映與原有用途的重疊，而非新的再利用訊號。
- 沒有臨床試驗，也沒有直接研究此疾病的文獻，證據等級為 L5。

**若要推進需要：**
- 明確界定「胃部疾病」中具體的新目標族群，且該族群需與現有用途不同。
- 補充作用機轉資料與香港仿單的核准適應症、警語與禁忌。
- 針對該具體疾病，找出或設計單方氫氧化鎂的直接臨床研究。
- 評估腎功能不全等高風險族群與交互作用的用藥管理。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

