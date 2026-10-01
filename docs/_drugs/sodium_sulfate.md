---
layout: default
title: Sodium Sulfate
parent: 僅模型預測 (L5)
nav_order: 807
evidence_level: L5
indication_count: 1
---

# Sodium Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sodium Sulfate：從（原適應症未登載）到消化不良

## 一句話總結

Sodium Sulfate（硫酸鈉）是一種滲透性成分，香港的 5 張許可證品名多屬腸道清潔類的口服散劑，但許可證資料中沒有登載原適應症。
TxGNN 模型預測它可能對**消化不良 (Dyspepsia)** 有效，但 3 個臨床試驗都與此無關，4 篇文獻全是動物或細胞的前臨床研究，**實際上沒有直接證據**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未登載（品名顯示為腸道清潔類製劑，屬推論） |
| 預測新適應症 | 消化不良 (Dyspepsia) |
| TxGNN 預測分數 | 99.09% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，DrugBank 也沒有記錄原適應症。Sodium Sulfate 屬滲透性成分，常見於腸道清潔製劑。現有資料中，沒有任何內容顯示它能治療上腹部症狀（如消化不良）。

滲透性腸道清潔製劑反而可能引起噁心、腹脹和腹部不適。因此在消化不良上，不僅療效缺乏支持，還可能造成不良影響。

TxGNN 的高分（0.99）只是知識圖譜的預測。它可能來自圖譜中「硫酸鹽」或「結腸炎」相關節點的鄰近關係，而不是藥理上的關聯。這個預測目前無法視為有效的新用途線索。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | 未知 | 150 | 比較 Oxycodone 與 Pregabalin 用於術後超前鎮痛，與本藥和消化不良無關，可能是關鍵字誤配 |
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | 招募中 | 140 | Alginate 與 Sucralfate 搭配 PPI 緩解 GERD 症狀，疾病相近，但試驗並未使用硫酸鈉 |
| [NCT06339697](https://clinicaltrials.gov/study/NCT06339697) | Phase 4 | 完成 | 194 | 比較腸道清潔製劑對大腸息肉切除患者腸道菌群的影響，只支持其腸道清潔用途，與消化不良無關 |

三個試驗的相關性評級皆為 C，沒有任何一個直接支持這個預測。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | 動物研究 | Molecules | 豬隻 DSS 誘發腸道損傷模型，探討 Donepezil 的藥動學。DSS 是結腸炎造模試劑，不是本藥 |
| [34207410](https://pubmed.ncbi.nlm.nih.gov/34207410/) | 2021 | 動物研究 | Pharmaceuticals | 豬隻 DSS 腸道損傷模型，探討 Galantamine 對胃肌電活動的影響，與本藥無直接關係 |
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | 前臨床研究 | Int J Mol Sci | Atractylodin 透過 PPARα 促效改善 DSS 結腸炎，與本藥無關 |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | 前臨床研究 | J Inflamm Res | 四逆湯治療潰瘍性結腸炎的網絡藥理學與動物驗證，與本藥無關 |

這四篇都是前臨床研究。所謂「sodium sulfate」其實是 DSS（Dextran Sodium Sulfate，葡聚糖硫酸鈉），一種誘發結腸炎的造模試劑，不是本藥。這些文獻不能當作本藥對消化不良有效的證據。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-35934 | KLEAN-PREP | TREASURE MOUNTAIN DEVELOPMENT CO LTD |
| HK-41626 | FORTRANS POWDER FOR ORAL SOL | DCH AURIGA (HONG KONG) LIMITED - HEALTHCARE DIVISION |
| HK-64391 | GI KLEAN POWDER FOR ORAL SOLUTION | ELIXIRPLUS PHARMA COMPANY LIMITED |
| HK-38577 | PEG-LYTE POWDER FOR ORAL SOLUTION | TRENTON-BOMA LTD |
| HK-68345 | ISOCOLAN POWDER FOR ORAL SOLUTION | TREASURE MOUNTAIN DEVELOPMENT CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5。TxGNN 的高分只是模型預測，臨床試驗與文獻都沒有直接支持，也找不到合理的作用機轉。
- 滲透性腸道清潔製劑可能引起噁心、腹脹與腹部不適，用於消化不良的風險可能大於益處。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症。這是目前阻擋進入安全性篩選的缺口。
- 從 DrugBank 補齊作用機轉，並確認原適應症。
- 找出 TxGNN 預測的圖譜路徑，判斷它是真實的藥理關聯，還是只是節點鄰近。
- 若沒有機轉或臨床訊號支持，建議不要進入後續評估。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

