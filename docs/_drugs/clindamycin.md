---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Clindamycin：從細菌感染治療到點狀上皮性角結膜炎

## 一句話總結

Clindamycin 是一種廣泛使用的林可醯胺類（Lincosamide）抗生素，原本用於治療細菌性皮膚、軟組織及厭氧菌感染，亦具抗弓形蟲活性。
TxGNN 模型預測它可能對**點狀上皮性角結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效；
然而目前該方向**無任何臨床試驗、無相關文獻**支持，高預測分數很可能源於知識圖譜節點群聚效應而非疾病特異性連結。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（香港未登記，0 張許可證） |
| 預測新適應症 | 點狀上皮性角結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏完整的作用機轉資料。根據公開已知資訊，Clindamycin 屬林可醯胺類抗生素，主要透過結合細菌核醣體 **50S 亞基**抑制蛋白質合成，對需氧革蘭氏陽性菌（如金黃色葡萄球菌）及厭氧菌具廣譜抗菌活性；此外亦對**弓形蟲（Toxoplasma gondii）**有效，在眼科脈絡膜視網膜炎治療中有一定地位。

點狀上皮性角結膜炎（Punctate Epithelial Keratoconjunctivitis, PEK）是角結膜表皮的瀰漫性淺層炎症，病因多元，包括病毒感染、乾眼症、局部藥物毒性及過敏反應等。其核心病理機制**並非細菌感染**，因此 Clindamycin 的抗菌作用機轉在此適應症缺乏直接的理論支撐。

TxGNN 給出 99.97% 的高預測分數，評估認為這最可能反映知識圖譜中「角膜疾病（corneal disease）」節點群的密集連結效應——即模型學習到鄰近節點間的結構關聯，而非 Clindamycin 對 PEK 的疾病特異性療效。此預測目前缺乏任何文獻或臨床試驗的實質支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **重要安全提示**：根據本次 Evidence Pack 其他預測的文獻評估，Clindamycin 是**艱難梭菌相關性腹瀉（Clostridioides difficile-associated diarrhea, CDAD）的頭號誘發抗生素之一**。任何新適應症評估均需將此風險列為核心安全性考量，並確認處方對象、療程長短及監測計畫。

---

## 結論與下一步

**決策：Hold**

**理由：**
點狀上皮性角結膜炎的主要病因為非細菌性（病毒、乾眼、毒性），Clindamycin 的抗菌機轉缺乏直接治療依據；加之目前完全無臨床試驗或文獻支持此方向，L5 證據等級不足以推進評估。

**其他預測亮點補充：**

| 排名 | 適應症 | 決策 | 說明 |
|------|--------|------|------|
| 2 | 暴露性角膜炎 (Exposure Keratitis) | Research Question | 繼發性細菌感染（MRSA/MSSA）有間接文獻支持，具進一步探索價值 |
| 3 | 非人類動物疾病 | ⚠️ Hold（安全警示） | 文獻為 C. difficile 流行病學研究，方向相反——為 Clindamycin **誘發** CDAD 的風險證據 |
| 6 | 停經後萎縮性陰道炎 | Research Question | Clindamycin 陰道凝膠已是 FDA 核准的 BV 治療，存在鄰近適應症延伸潛力，但缺直接證據 |

**若要推進評估（包括 Rank 2 暴露性角膜炎），需要：**
- 補充 Clindamycin 完整 MOA 資料（DrugBank API 查詢）
- 取得香港衛生署仿單警語與禁忌資訊
- 評估眼用局部製劑（如滴眼液）在香港的開發可行性
- 針對繼發性細菌感染角膜炎設計臨床研究假說，聚焦 MSSA/MRSA 亞群
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

