---
layout: default
title: Etodolac
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "ETODOLAC"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
description: "Etodolac：預測新適應症為Acromesomelic dysplasia, Hunter-Thompson type（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Etodolac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Etodolac: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## 一句話總結

Etodolac 是一種偏向抑制 COX-2 的非類固醇抗發炎藥（NSAID），原本用於類風濕性關節炎、退化性關節炎等關節疾病。
TxGNN 模型預測分數最高的是 Hunter-Thompson 型肢中發育不良，但這項預測缺乏機轉與實證支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | 僵直性脊椎炎：L5；排名第 1 之預測：L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold（排名第 1 之預測）；僵直性脊椎炎為 Research Question，建議以 Proceed with Guardrails 的方式審慎評估 |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Etodolac 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「Etodolac 緩釋錠的作用機轉與其他 NSAIDs 一樣尚未完全明瞭，但可能與抑制前列腺素合成酶有關。」英文原文："The mechanism of action of etodolac extended-release tablets, like that of other NSAIDs, is not completely understood, but may be related to prostaglandin synthetase inhibition."（[DailyMed: Etodolac Er (etodolac) prescribing information, Advanced Rx Pharmacy of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=baebdfb2-17f6-9081-e053-2a95a90ab331)，版本日期 2024-12-31；查閱日期 2026-11-19）。根據文獻，etodolac 是偏向抑制環氧合酶-2 (COX-2) 的 NSAID，透過降低前列腺素合成來減輕發炎與疼痛。

**排名第 1 的預測（Hunter-Thompson 型肢中發育不良）**是由 CDMP1/GDF5 基因突變引起的罕見骨骼發育異常。Etodolac 對 GDF5 訊號或骨骼發育沒有已知作用，分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。其他高分預測（短椎體症相關疾病、假性軟骨發育不全等）同樣僅有模型預測，無任何試驗或文獻。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

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

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-44856 | ETOLAC CAP 200MG | 單一成分 | APT PHARMA LIMITED | 有效 |
| HK-45895 | ETONOX CAP 200MG | 單一成分 | DELTAPHARM LIMITED | 有效 |

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示之相關疾病禁忌（非仿單原文）**：高血壓、腎臟疾病、肝臟疾病、膽囊疾病、活動性消化性潰瘍、凝血疾病、心肌梗塞與冠狀動脈血栓、血紅素病變、心血管疾病與心臟疾病等。這與 NSAID 類別的心血管、胃腸道、腎臟風險一致。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：阿斯匹靈、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide（類固醇類）、Metformin、Glimepiride、Repaglinide、Chlorpropamide（降血糖藥）、Mesalazine、Balsalazide、Potassium citrate、Potassium bicarbonate
  - 輕度：Famotidine、Ranitidine、Cimetidine、Linaclotide
- 香港仿單的警語與禁忌資料尚未取得，正式使用前請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（高分罕見骨骼疾病預測）**

**理由：**
- TxGNN 分數最高的預測（Hunter-Thompson 型肢中部發育不良等）缺乏機轉依據、試驗與文獻，不建議推進。
- 僵直性脊椎炎在機轉上合理且 NSAID 為標準症狀治療，但證據多為回顧與觀察性研究，且與 etodolac 既有的脊椎關節病變適應症高度重疊，較屬於標示範圍的延伸，並非全新機會。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字
- 補齊 etodolac 詳細作用機轉資料
- 針對 AS 的 etodolac 對照試驗，或與其他 NSAID 的直接比較證據
- 針對高血壓、腎臟、肝臟、消化性潰瘍及心血管高風險族群制定安全性監測計畫
- 釐清「脊椎關節病變易感性」與「發炎性脊椎病變」是否僅為與原適應症重疊的標籤

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Etodolac Er (etodolac) prescribing information, Advanced Rx Pharmacy of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=baebdfb2-17f6-9081-e053-2a95a90ab331) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

