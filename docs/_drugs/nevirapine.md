---
layout: default
title: Nevirapine
parent: 中證據等級 (L3-L4)
nav_order: 615
evidence_level: L4
indication_count: 3
---

# Nevirapine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Nevirapine：從 HIV 感染到貓後天免疫缺乏症候群（獸醫適應症）

## 一句話總結

Nevirapine 是一種非核苷類逆轉錄酶抑制劑（NNRTI），原本用於治療 HIV 感染與愛滋病。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**體外生化與結構研究，且該研究顯示機轉支持度有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、愛滋病（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Nevirapine 是 HIV-1 的非核苷類逆轉錄酶抑制劑，透過結合逆轉錄酶的 NNRTI 結合口袋來抑制病毒複製。貓免疫缺乏病毒 (FIV) 同屬慢病毒，也具有逆轉錄酶，這是模型給出高分的可能原因。

然而，2023 年的生化與結構比較研究（PMID 38031646）顯示，由於 NNRTI 結合口袋存在差異，NNRTI 類藥物對 FIV 逆轉錄酶的活性可能有限。換言之，高預測分數並未獲得機轉資料支持。

此外，這是獸醫適應症，與人類臨床應用無直接關聯。預測分數應視為計算模型的結果，不宜視為療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | 體外生化／結構研究 | Journal of Veterinary Science | 比較 Nevirapine、Efavirenz、Rilpivirine 對貓與人類免疫缺乏病毒的作用；FIV 目前尚無有效治療，該研究探討 NNRTI 的潛力，結果顯示對 FIV 逆轉錄酶的活性有限 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63478 | PMS-NEVIRAPINE TABLETS 200MG | 未載明 | 未載明 |
| HK-65069 | NEVIRAPINE TABLETS USP 200MG | 未載明 | 未載明 |
| HK-66786 | APT-NEVIRAPINE TABLETS 200MG | 未載明 | 未載明 |
| HK-62889 | NEVIRAPINE TABLETS 200MG | 未載明 | 未載明 |
| HK-64848 | NEVIRAPINE TABLETS USP 200MG | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：肝衰竭、肝病、膽囊疾病、皮疹、慢性 C 型肝炎、C 型肝炎病毒感染、慢性 B 型肝炎病毒感染、橫紋肌溶解症、結節性筋膜炎、藥物性肝損傷、史蒂文斯-強生症候群 (Stevens-Johnson syndrome)、毒性表皮壞死症 (Lyell 症候群)。這些來自知識圖譜的關聯，並非仿單原文。
- **藥物交互作用**：共查得 100 筆交互作用，列出的皆為中度，包括 Rabeprazole、Bupropion、Aprepitant、Triamcinolone、Dexamethasone、Betamethasone、Budesonide、Clarithromycin、Saxagliptin、Eliglustat 等。Nevirapine 可誘導 CYP3A4/2B6，用藥時須留意併用藥物。

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.85%），但僅有 1 篇體外研究，且結果顯示 NNRTI 對 FIV 逆轉錄酶活性有限，機轉上不支持。
- 這是獸醫適應症，沒有臨床試驗，且 Nevirapine 具有肝毒性與嚴重皮膚反應等安全性疑慮。

**若要推進需要：**
- 取得 Nevirapine 的作用機轉資料與香港仿單的警語與禁忌資料
- 針對 FIV 逆轉錄酶進行更直接的體外活性驗證
- 若有意在獸醫領域發展，須評估貓的藥動學、劑量與安全性

---

### 補充：其他預測適應症

- **猿猴免疫缺乏病毒感染（TxGNN 分數 99.85%，L4，Hold）**：SIV 與 HIV-2 天然對 NNRTI 具抗藥性（RT 結合口袋的自然多型性），所以 Nevirapine 只作為帶有 HIV-1 RT 的嵌合病毒 (RT-SHIV) 動物模型中的研究工具，不是治療用途。
- **伴隨共濟失調步態、無語言與皮質白質減少的神經發育障礙（TxGNN 分數 99.82%，L5，Hold）**：無機轉關聯，也沒有臨床試驗或文獻，僅為模型預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

