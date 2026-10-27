---
layout: default
title: Etodolac
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etodolac：預測新適應症為模型排名第 1 為 acromesomelic dysplasia, Hunter-Thompson type（證據等級 L5）。原適應症：類風濕性關節炎、退化性關節炎、關節病變、幼年型特發性關節炎、脊椎關節病變"
monitor_inn: "ETODOLAC"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "spondyloarthropathy, susceptibility to", "brachyolmia", "ankylosing spondylitis", "pseudoachondroplasia", "hypermobility of coccyx", "inflammatory spondylopathy"]
---

# Etodolac
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

## Etodolac：從類風濕性關節炎／退化性關節炎到僵直性脊椎炎
{: .text-alpha }

## 一句話總結

Etodolac 是一種偏向抑制 COX-2 的非類固醇抗發炎藥（NSAID），原本用於類風濕性關節炎、退化性關節炎等關節疾病。
TxGNN 模型預測分數最高的是罕見骨骼發育異常疾病，但這些預測缺乏機轉與實證支持。相對合理的方向是**僵直性脊椎炎 (Ankylosing Spondylitis)**，目前有 **8 篇文獻**（多為回顧與上市後安全性研究）支持，但**沒有臨床試驗登記**，且缺乏針對該疾病的 etodolac 專屬隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、退化性關節炎、關節病變、幼年型特發性關節炎、脊椎關節病變（香港許可證未載明核准適應症文字，此為知識圖譜所列適應症） |
| 預測新適應症 | 模型排名第 1 為 acromesomelic dysplasia, Hunter-Thompson type（證據等級 L5）；本報告以證據最多的**僵直性脊椎炎**為主要評估對象 |
| TxGNN 預測分數 | 排名第 1：99.97%；僵直性脊椎炎：99.93% |
| 證據等級 | 僵直性脊椎炎：L4；排名第 1 之預測：L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（排名第 1 之預測）；僵直性脊椎炎為 Research Question，建議以 Proceed with Guardrails 的方式審慎評估 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中的 MOA 欄位為空）。根據文獻，etodolac 是偏向抑制環氧合酶-2 (COX-2) 的 NSAID，透過降低前列腺素合成來減輕發炎與疼痛。

**排名第 1 的預測（Hunter-Thompson 型肢中部發育不良）**是由 CDMP1/GDF5 基因突變引起的罕見骨骼發育異常。Etodolac 對 GDF5 訊號或骨骼發育沒有已知作用，分數高很可能只是知識圖譜中與關節病變、骨骼疾病相近所造成。其他高分預測（brachyolmia 相關疾病、假性軟骨發育不全等）同樣僅有模型預測，無任何試驗或文獻。

**僵直性脊椎炎**則不同：NSAID 是此病的一線症狀治療，與 etodolac 在脊椎關節病變的既有用途一致，機轉上合理。但要注意，現有文獻證據偏向 NSAID 類別效應，並非 etodolac 專屬的 AS 隨機試驗。另外「脊椎關節病變易感性」與「發炎性脊椎病變」兩項預測，與原適應症高度重疊，較像本體論（ontology）重疊，而非真正的新機會。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為僵直性脊椎炎預測相關文獻（「發炎性脊椎病變」預測使用相同文獻組）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | Review | Drugs | 回顧 etodolac 在類風濕性關節炎、退化性關節炎、僵直性脊椎炎及疼痛的療效，整體至少與其他 NSAID 相當 |
| [2146130](https://pubmed.ncbi.nlm.nih.gov/2146130/) | 1990 | Review | Eur J Rheumatol Inflamm | 彙整隨機雙盲試驗：etodolac 在類風濕性與退化性關節炎的療效與 naproxen、piroxicam 等相當 |
| [17694363](https://pubmed.ncbi.nlm.nih.gov/17694363/) | 1997 | Review | Inflammopharmacology | 說明 etodolac 偏向 COX-2 的機轉，並已廣泛用於發炎性關節炎，包括僵直性脊椎炎 |
| [22071858](https://pubmed.ncbi.nlm.nih.gov/22071858/) | 2011 | Review（Cochrane） | Cochrane Database Syst Rev | 評估發炎性關節炎患者在使用 methotrexate 時併用 NSAID、阿斯匹靈或乙醯胺酚的安全性 |
| [20829199](https://pubmed.ncbi.nlm.nih.gov/20829199/) | 2011 | 指引／建議 | Ann Rheum Dis | ASAS 對軸性脊椎關節炎試驗中蒐集與報告 NSAID 使用量的建議 |
| [2525800](https://pubmed.ncbi.nlm.nih.gov/2525800/) | 1989 | 觀察性（開放性臨床實務） | Rev Med Interne | 974 位風濕科醫師、4,947 位患者（含 AS）的開放性研究，評估療效與耐受性 |
| [2150569](https://pubmed.ncbi.nlm.nih.gov/2150569/) | 1990 | 開放性試驗（安全性） | Rheumatol Int | 法國兩項大規模開放性研究，含 4,947 位與 51,355 位患者的安全性評估 |
| [2150568](https://pubmed.ncbi.nlm.nih.gov/2150568/) | 1990 | 上市後監測 | Rheumatol Int | 四項上市後監測研究、共 8,334 位患者，顯示良好的安全性 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44856 | ETOLAC CAP 200MG（APT PHARMA LIMITED） | 膠囊（品名標示） | 資料未載明 |
| HK-45895 | ETONOX CAP 200MG（DELTAPHARM LIMITED） | 膠囊（品名標示） | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示之相關疾病禁忌（非仿單原文）**：高血壓、腎臟疾病、肝臟疾病、膽囊疾病、活動性消化性潰瘍、凝血疾病、心肌梗塞與冠狀動脈血栓、血紅素病變、心血管疾病與心臟疾病等。這與 NSAID 類別的心血管、胃腸道、腎臟風險一致。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：阿斯匹靈、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide（類固醇類）、Metformin、Glimepiride、Repaglinide、Chlorpropamide（降血糖藥）、Mesalazine、Balsalazide、Potassium citrate、Potassium bicarbonate
  - 輕度：Famotidine、Ranitidine、Cimetidine、Linaclotide
- 香港仿單的警語與禁忌資料尚未取得，正式使用前請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（高分罕見骨骼疾病預測）；僵直性脊椎炎為 Research Question**

**理由：**
- TxGNN 分數最高的預測（Hunter-Thompson 型肢中部發育不良等）缺乏機轉依據、試驗與文獻，不建議推進。
- 僵直性脊椎炎在機轉上合理且 NSAID 為標準症狀治療，但證據多為回顧與觀察性研究，且與 etodolac 既有的脊椎關節病變適應症高度重疊，較屬於標示範圍的延伸，並非全新機會。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字
- 補齊 etodolac 詳細作用機轉資料
- 針對 AS 的 etodolac 對照試驗，或與其他 NSAID 的直接比較證據
- 針對高血壓、腎臟、肝臟、消化性潰瘍及心血管高風險族群制定安全性監測計畫
- 釐清「脊椎關節病變易感性」與「發炎性脊椎病變」是否僅為與原適應症重疊的標籤
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

