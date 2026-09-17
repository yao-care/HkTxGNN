---
layout: default
title: Tretinoin
parent: 僅模型預測 (L5)
nav_order: 768
evidence_level: L5
indication_count: 5
---

# Tretinoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# TRETINOIN：從（無登記適應症資料）到類風濕結節病（Rheumatoid Nodulosis）

## 一句話總結

> TRETINOIN 目前缺乏原適應症、作用機轉與安全性資料，且在香港未上市。
> TxGNN 模型預測它可能對**類風濕結節病 (Rheumatoid Nodulosis)** 有效，
> 但**目前無任何臨床試驗或文獻佐證**，且藥理機轉上存在矛盾之處。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無登記資料（Data Gap） |
| 預測新適應症 | 類風濕結節病 (Rheumatoid Nodulosis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 tretinoin 的原適應症登記資料與詳細作用機轉（MOA 標示為 Data Gap），因此本評估主要依據 TxGNN 知識圖譜的關聯性推論結果，而非機轉層面的合理性分析。

根據證據包中的 rationale 說明，tretinoin（維甲酸類藥物）已知藥理特性為細胞分化誘導與角質代謝調節，其已知副作用包含**關節痛與骨質增生（retinoid hyperostosis）**——這與本次前 5 名預測適應症（多屬類風濕結節病、幼年特發性關節炎等關節相關疾病）所需的抗發炎/免疫調節方向**存在潛在矛盾**，而非支持性連結。

換言之，TxGNN 給出的高分（>99%）反映的是知識圖譜嵌入空間中的相似度，**並非藥理機轉上的合理推論**，也沒有任何臨床試驗或發表文獻可佐證。

### 其他預測候選（Rank 2-5）

| Rank | 疾病 | TxGNN 分數 | 證據等級 | 決策 |
|------|------|-----------|---------|------|
| 2 | RF-positive polyarticular juvenile idiopathic arthritis | 99.82% | L5 | Hold |
| 3 | Juvenile idiopathic arthritis | 99.80% | L5 | Hold |
| 4 | Juvenile chronic polyarthritis | 99.78% | L5 | Hold |
| 5 | Spondyloarthropathy, susceptibility to | 99.71% | L5 | Hold |

五個候選皆無臨床試驗或文獻支持，且均屬於同一機轉矛盾疑慮（維甲酸類藥物已知關節相關不良反應）。第 5 項另有分類問題：「susceptibility to」屬易感性標籤而非疾病本身，預測意義有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前無香港上市許可證資料（未上市，總計 0 張許可證）。

## 安全性考量

安全性資訊請參考原廠仿單。

（本評估缺乏 TFDA 仿單警語、禁忌症及藥物交互作用資料，此為 Blocking 級資料缺口。）

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個預測適應症皆為 L5（純模型預測），無任何臨床試驗或文獻佐證。
- Tretinoin 已知的骨骼/關節相關不良反應與這些候選適應症的治療方向存在潛在矛盾。
- 缺乏原廠 MOA、安全性資料，香港亦未上市，尚不具備進入下一階段安全性初評（S1）的條件。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌症資料（DG001，Blocking，來源：TFDA 官網解析仿單 PDF）
- 補齊作用機轉（MOA）資料（DG002，High，來源：DrugBank API）
- 尋找 tretinoin 與類風濕/幼年特發性關節炎相關的獨立臨床或機轉研究，以釐清是否存在被知識圖譜捕捉到但尚未發表的關聯
- 若上述資料補齊後仍無法解決機轉矛盾，建議終止此候選項目的後續評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

