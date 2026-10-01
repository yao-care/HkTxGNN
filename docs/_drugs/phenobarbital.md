---
layout: default
title: Phenobarbital
parent: 中證據等級 (L3-L4)
nav_order: 673
evidence_level: L4
indication_count: 5
---

# Phenobarbital
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Phenobarbital：從抗癲癇用藥到三叉神經腫瘤

## 一句話總結

Phenobarbital（苯巴比妥）是傳統巴比妥類抗癲癇藥物。
TxGNN 模型預測它可能對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效，但目前沒有相關臨床試驗，僅有 **1 篇**間接相關的文獻，證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗癲癇用藥（香港許可證資料未載明適應症文字） |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Phenobarbital 是巴比妥類抗癲癇藥物，在癲癇發作控制上的療效已被廣泛證實，但這與腫瘤生物學沒有直接關聯。

目前找不到機轉上連結抗癲癇作用與三叉神經腫瘤的證據。唯一的文獻是一篇 Sturge-Weber 症候群病例系列，該病是伴隨三叉神經分布區血管異常的神經皮膚症候群，phenobarbital 在其中用於控制癲癇，並非抗腫瘤。

0.9996 的高分較可能來自知識圖譜中癲癇與神經皮膚疾病等節點的相近性，不代表藥物有抗腫瘤效果。解讀這個分數時請特別保守。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | 回顧 14 例 Sturge-Weber 症候群的臨床特徵、病程與治療反應；與腫瘤無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-43727 | UNI-FENO SYRUP 15MG/5ML | Universal Pharmaceutical Laboratories, Limited |
| HK-45682 | PHENOBARBITONE SOD. INJ 200MG/ML | The International Medical Company Limited |
| HK-04992 | PHENOBARBITONE TAB 60MG | Synco (H.K.) Limited |
| HK-04966 | PHENOBARBITONE TAB 30MG | Synco (H.K.) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
沒有任何臨床試驗，唯一的文獻與腫瘤無直接關聯，機轉上也找不到連結。高預測分數很可能是知識圖譜相近性造成的假象，目前不宜推進。

此藥另有 4 項預測適應症（進食性癲癇、聽源性癲癇、思考性癲癇、性高潮誘發癲癇）。它們都屬反射性癲癇，與 phenobarbital 的抗癲癇類別較吻合，證據多為動物實驗或間接文獻，可列為研究問題，但同樣缺乏直接的人體證據。

**若要推進需要：**
- 補齊作用機轉（MOA）資料（可查詢 DrugBank）
- 取得香港衞生署仿單的警語與禁忌資料
- 找到支持神經腫瘤適應症的機轉或前臨床研究
- 若轉向反射性癲癇方向，需取得人體研究證據

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

