---
layout: default
title: Gemfibrozil
parent: 中證據等級 (L3-L4)
nav_order: 404
evidence_level: L4
indication_count: 5
---

# Gemfibrozil
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

# Gemfibrozil：從血脂異常到類風濕性關節炎

## 一句話總結

Gemfibrozil 是一種 PPARα 促效劑，屬降血脂藥（fibrate 類）。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效。
目前**沒有臨床試驗**，僅有 **4 篇文獻**，其中直接相關的是 1 篇大鼠實驗，證據仍停留在前臨床階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血脂異常（依藥物類別判斷；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Gemfibrozil 是 PPARα 促效劑，PPAR 促效劑具有抗發炎與免疫調節作用，例如影響 T 細胞與細胞激素路徑。這些作用在機轉上可能與類風濕性關節炎的發炎病理相關。

支持這個方向的間接證據有兩項：
- 2026 年一項前臨床研究顯示，同屬 fibrate 類的 pan-PPAR 促效劑 Bezafibrate 可減輕實驗性關節炎。
- 2019 年一項大鼠佐劑性關節炎模型研究，測試 Gemfibrozil 合併減量類固醇，結果與全劑量類固醇的控制效果相近。

Bezafibrate 是不同的藥物，只能支持 PPAR 這條機轉，不能直接代表 Gemfibrozil。Gemfibrozil 本身的證據只有一項動物實驗，尚無人體試驗。TxGNN 分數雖然很高，但只是知識圖譜的預測。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | 動物實驗（大鼠） | Modern Rheumatology | 在佐劑性關節炎大鼠模型中，Gemfibrozil 合併減量類固醇，效果與全劑量類固醇相近 |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | 前臨床（動物，不同 PPAR 促效劑） | International Immunopharmacology | Bezafibrate 透過 PPAR 路徑減輕實驗性類風濕性關節炎，尤其與 PPARγ 活性有關 |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | 前臨床（機轉研究） | Journal of Immunology | 探討一氧化氮與調節性 T 細胞 (Foxp3) 的交互作用，屬自體免疫機轉背景資料 |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | 病例報告／綜述 | American Journal of Clinical Dermatology | 掌紅斑的成因與相關系統性疾病，與 Gemfibrozil 的直接關聯低 |

## 香港上市資訊

香港共有 15 張許可證，以下列出 5 張。資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68047 | APT-GEMFIBROZIL TABLETS 600MG | APT PHARMA LIMITED |
| HK-50486 | POLI-FIBROZIL CAP 300MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-50342 | LIPOFOR 600 TAB 600MG | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-43457 | LIPOFOR 300 CAP | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-47676 | SCANTIPID CAP 300MG | HANG LUNG TRADING (H.K.) CO |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測與前臨床線索，沒有任何臨床試驗，也沒有 Gemfibrozil 本身的人體證據。
- 唯一直接相關的 Gemfibrozil 研究是大鼠實驗，其餘證據來自其他 PPAR 促效劑或機轉背景資料。
- 香港仿單的警語與禁忌症資料缺漏，尚無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料（阻擋性缺口）。
- 補齊 DrugBank 的作用機轉資料。
- 重現並擴大 Gemfibrozil 在類風濕性關節炎的動物或體外實驗，包括單獨用藥與合併類固醇。
- 若前臨床結果一致，再評估探索性人體研究，並確認與類風濕性關節炎常用藥物的交互作用。

另一個預測適應症「HIV 相關血脂異常」的證據較多（L3，含 RCT），但屬降血脂用途而非抗病毒，可另案評估。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

