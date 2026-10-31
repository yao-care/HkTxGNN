---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Diclofenac"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis", "diffuse alopecia areata", "juvenile idiopathic arthritis", "WHIM syndrome"]
description: "Diclofenac：預測新適應症為頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Diclofenac
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

## Diclofenac: 頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp)（排名第 1，無證據）；另列出有文獻支持的幼年特發性關節炎 (hypotrichosis simplex of the scalp)
{: .text-alpha }

## 一句話總結

Diclofenac 是一種非類固醇消炎止痛藥（NSAID），原本用於類風濕性關節炎、僵直性脊椎炎、骨關節炎，以及光線性角化症等皮膚病變。
TxGNN 模型排名第一的預測是**頭皮單純性毛髮稀少症**，但該預測沒有任何證據支持。相對地，唯一有文獻支持的預測是**幼年特發性關節炎 (Juvenile Idiopathic Arthritis, JIA)**，目前有 **0 個臨床試驗**和 **14 篇文獻**，但多為較早期的小規模研究，且屬於既有 NSAID 用途的延伸，並非全新的再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp)（排名第 1，無證據）；另列出有文獻支持的幼年特發性關節炎 (hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 0.9969 |
| 證據等級 | L5（排名第 1 的預測）；JIA 為 L3 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold（排名第 1 的預測）；JIA 列為研究問題 (Research Question) |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Diclofenac 屬於 COX-1/COX-2 抑制劑類的 NSAID，透過抑制前列腺素合成來達到消炎與止痛效果。

**排名第 1 的預測（頭皮單純性毛髮稀少症）**：這是一種遺傳性掉髮疾病（如 CDSN、APCDD1、RPL21 變異），並非由前列腺素路徑驅動。目前找不到可信的機轉連結，高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而非生物學證據。

**其他排名前列的預測**：排名 2 至 8 與 10 的疾病（如 Hunter-Thompson 型肢中發育不良、假性軟骨發育不全、短軀幹症、肌硬化症、瀰漫性圓形禿、WHIM 症候群等）多為遺傳性或自體免疫疾病，同樣沒有合理的機轉連結，也沒有任何臨床試驗或文獻。

**幼年特發性關節炎 (JIA)**：這是唯一機轉上相符的預測。JIA 是發炎性關節炎，前列腺素介導的發炎與疼痛可用 NSAID 治療，與 Diclofenac 在類風濕性關節炎和僵直性脊椎炎的作用機轉相同。不過這屬於 NSAID 類別的症狀控制，並非新穎的再利用。現代 JIA 治療以 DMARD 和生物製劑為主，NSAID 為輔助角色。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為 JIA 預測的文獻（依與 Diclofenac 的相關性及研究類型挑選）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3052965](https://pubmed.ncbi.nlm.nih.gov/3052965/) | 1988 | 交叉試驗 | Clin Exp Rheumatol | 28 名血清陰性幼年慢性關節炎兒童，單盲交叉比較 naproxen、diclofenac、tolmetin，為期 12 週 |
| [6361986](https://pubmed.ncbi.nlm.nih.gov/6361986/) | 1983 | 臨床研究 | Scand J Rheumatol | 以 Diclofenac 治療幼年類風濕性關節炎，並評估 2-7 歲兒童的藥動學 |
| [2235663](https://pubmed.ncbi.nlm.nih.gov/2235663/) | 1990 | 開放性非對照研究 | Pediatr Med Chir | 26 名 2-16 歲多關節型幼年慢性關節炎患者使用 Diclofenac 的臨床療效 |
| [10756785](https://pubmed.ncbi.nlm.nih.gov/10756785/) | 1997 | 比較研究／回顧 | Rev Med Chir Soc Med Nat Iasi | 100 名幼年慢性關節炎兒童，比較 diclofenac、paduden 與 aspirin 的效果 |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | Br J Rheumatol | 控制關節症狀方面，diclofenac、ibuprofen、tolmetin、naproxen 療效與耐受性相當 |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Review | Clin Pharmacokinet | 幼年關節炎用藥的臨床藥動學回顧 |
| [11735667](https://pubmed.ncbi.nlm.nih.gov/11735667/) | 2001 | Review | Paediatr Drugs | 兒童使用 NSAID 與 paracetamol 的風險與效益比較 |
| [723822](https://pubmed.ncbi.nlm.nih.gov/723822/) | 1978 | 未分類 | Minerva Pediatr | 以 Diclofenac 鈉治療兒童類風濕性關節炎（無摘要） |
| [17474954](https://pubmed.ncbi.nlm.nih.gov/17474954/) | 2007 | 調查 | Paediatr Anaesth | 英國與愛爾蘭兒科麻醉醫師使用 NSAID 的調查；指出 Diclofenac 在 1 歲以上兒童獲准用於幼年類風濕性關節炎 |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review | Crit Rev Ther Drug Carrier Syst | NSAID 微膠囊化藥物遞送系統（非 Diclofenac 專屬） |

其餘文獻（如 nabumetone、naproxen 回顧、JIA 肺泡出血病例系列、成人 Still 病例報告）與 Diclofenac 關聯較低，未列入。

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一成分製劑，無已註銷者。資料中未提供劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37120 | VOLTAREN SR 75 TAB | 錠劑（緩釋） | 資料未載明 |
| HK-36029 | VOLTAREN SUPP 50MG (FOR ADULTS) | 栓劑 | 資料未載明 |
| HK-66111 | VOLTAREN SR PROLONGED-RELEASE TABLETS 100MG | 錠劑（緩釋） | 資料未載明 |
| HK-25362 | DICLOFENAC SOD INJ 25MG/ML | 注射劑 | 資料未載明 |
| HK-53619 | VOLTA EMULSION GEL 1% W/W | 外用凝膠 | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來源為知識圖譜的藥物-疾病禁忌關聯，非仿單內容）：
  - 心血管：高血壓、鬱血性心衰竭、心肌梗塞、腦中風、腦梗塞、冠狀動脈血栓、心血管疾病
  - 消化道：消化性潰瘍（含活動性）、發炎性腸道疾病
  - 肝臟：肝衰竭、肝病、藥物性肝損傷、膽囊疾病
  - 呼吸道：氣喘（含內因性、過敏性）
  - 血液：凝血疾病、貧血、血紅素病變
  - 代謝：糖尿病、糖尿病酮酸中毒
  - 其他：物質濫用／依賴、角膜炎
- **藥物交互作用**：共查得 100 筆，以下為部分代表：
  - 中度：Acetylsalicylic acid（阿斯匹靈）、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide 等皮質類固醇；Metformin、Glimepiride、Glipizide、Chlorpropamide 等降血糖藥；Mesalazine、Balsalazide、Aprepitant
  - 輕度：Famotidine、Ranitidine、Cimetidine

仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（排名第 1 的預測：頭皮單純性毛髮稀少症；JIA 列為研究問題）

**理由：**
- 排名前 8 及第 10 的預測皆無臨床試驗、無文獻，且機轉上與 COX 抑制沒有合理連結，分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，而非生物學證據，不建議推進。
- JIA 雖有機轉合理性與少量兒童使用文獻，但證據為 1980–1990 年代的小規模研究，屬 NSAID 既有用途延伸，非真正的新適應症，證據等級僅 L3。

**若要推進需要：**
- 取得 Diclofenac 的作用機轉資料與香港仿單的警語、禁忌
- 若評估 JIA，需確認香港許可證是否涵蓋兒童適應症，並與現行 DMARD／生物製劑治療指引比較 NSAID 的定位
- 兒童劑量與心血管、腸胃、肝臟風險的安全性監測計畫
- 針對任何預測新適應症，需先有前臨床或機轉研究支持，才值得進一步評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

