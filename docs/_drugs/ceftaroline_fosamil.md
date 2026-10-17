---
layout: default
title: Ceftaroline Fosamil
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceftaroline Fosamil：預測新適應症為類風濕性關節炎 (rheumatoid arthritis)（證據等級 L5）。原適應症：目前許可證資料未載明"
monitor_inn: "Ceftaroline fosamil"
predicted_indications: ["rheumatoid arthritis", "osteoarthritis", "osteoarthritis susceptibility", "gout", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "hemoglobinopathy", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis"]
---

# Ceftaroline Fosamil
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

# Ceftaroline fosamil：從細菌感染到類風濕性關節炎（模型預測，證據不足）

## 一句話總結

Ceftaroline fosamil 是第五代注射用 cephalosporin 類抗生素，在香港已取得上市許可。
TxGNN 模型預測它可能對**類風濕性關節炎 (rheumatoid arthritis)** 有效，但目前**沒有任何臨床試驗與文獻**支持，屬於純計算預測，現階段不建議推進。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料未載明 |
| 預測新適應症 | 類風濕性關節炎 (rheumatoid arthritis) |
| TxGNN 預測分數 | 98.20% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理分類，Ceftaroline 是 beta-lactam 類（第五代 cephalosporin），透過結合青黴素結合蛋白 (PBP) 抑制細菌細胞壁合成，對 MRSA 的 PBP2a 也有作用。

這個機轉與類風濕性關節炎（自體免疫性關節疾病）並無已知關聯。Ceftaroline 沒有已知的免疫調節或抗發炎活性。較可能的解釋是：TxGNN 的高分反映知識圖譜中，該藥與關節、骨感染相關適應症距離相近，而非真正的治療機轉。因此，**此預測的合理性低**，應視為模型假說，而非可行動的再利用線索。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（補充：在其他排名較高的預測中，僅有少量間接文獻。骨關節炎項下有一篇 2016 年 *J Antimicrob Chemother* 的配對世代研究（PMID [27530754](https://pubmed.ncbi.nlm.nih.gov/27530754/)），比較 ceftaroline 與 vancomycin 用於「骨關節感染」，屬抗菌用途，並非退化性骨關節炎的治療證據。痛風項下的 PMID [21382815](https://pubmed.ncbi.nlm.nih.gov/21382815/) 是同時介紹多種新藥的綜述，只是同時提及，並非療效證據。）

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62093 | ZINFORO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 600MG（Pfizer Corporation Hong Kong Limited） | 注射用濃縮輸注液粉劑 | 許可證資料未載明 |

## 安全性考量

- **藥物交互作用**：共查得 12 筆中度 (Moderate) 交互作用，主要包括：
  - 胺基糖苷類抗生素：Kanamycin、Neomycin、Streptomycin、Amikacin（含 liposome 劑型）、Gentamicin
  - 抗凝血劑：Warfarin、Dicoumarol
  - 其他：Chloramphenicol、Picosulfuric acid、Ethinylestradiol、Mycophenolic acid
- **其他注意事項**：beta-lactam 類藥物可能引起免疫性溶血性貧血，若用於血紅素病變族群須特別留意。

其餘警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗或直接文獻支持，證據等級為 L5。
- 作用機轉（抑制細菌細胞壁合成）與類風濕性關節炎的免疫發炎病理無明顯關聯，高分很可能是知識圖譜的鄰近效應。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，並確認原適應症與許可證核准適應症
- 取得香港衛生署仿單的警語與禁忌症
- 找出任何支持免疫調節或抗發炎作用的前臨床證據，否則不建議投入資源
- 同時評估其他排名靠前的預測（如骨關節感染相關），確認是否有較合理的抗感染方向
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

