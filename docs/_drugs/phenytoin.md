---
layout: default
title: Phenytoin
parent: 中證據等級 (L3-L4)
nav_order: 680
evidence_level: L4
indication_count: 5
---

# Phenytoin
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

# Phenytoin：從癲癇到三叉神經腫瘤

## 一句話總結

Phenytoin（苯妥英）是鈉離子通道阻斷型的抗癲癇藥物。
TxGNN 模型預測它可能對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效，但目前**沒有臨床試驗**，只有 **5 篇文獻**，且沒有一篇顯示抗腫瘤活性，證據僅為模型預測等級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 癲癇（香港許可證資料未載明適應症文字） |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Phenytoin 屬於鈉離子通道阻斷型抗癲癇藥，在癲癇與神經痛相關的神經異常放電上有已知療效。機轉上可能適用於與三叉神經相關的症狀。

預測分數偏高，很可能是因為「三叉神經腫瘤」這個節點在知識圖譜中非常接近**三叉神經痛**。三叉神經痛是鈉通道阻斷類抗癲癇藥常見的仿單外用途。

不過，檢索到的文獻涵蓋三叉神經痛、Sturge-Weber 症候群與神經生理學，**沒有任何一篇顯示 Phenytoin 具抗腫瘤活性，或能治療三叉神經腫瘤**。兩者的關聯是間接的，較可能反映症狀控制（神經痛或癲癇發作），而非疾病本身的治療。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | 三叉神經痛的各種藥物與手術治療回顧，常見病因為神經根血管壓迫，與腫瘤無直接關係 |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Review | J Assoc Physicians India | Sturge-Weber 症候群（腦三叉神經血管瘤病）病例報告，特徵為血管畸形與癲癇發作 |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | 14 例 Sturge-Weber 症候群的臨床特徵、病程與治療反應回顧 |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Cross-sectional | Birth Defects Orig Artic Ser | 收容機構智能障礙者的皮膚疾病，含藥物治療引起的皮膚反應 |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Preclinical | Trans Am Neurol Assoc | 三叉神經後根纖維大小與痛覺、觸覺傳導的關係，以及三叉神經痛的治療 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-47301 | PHENYTOIN INJ 250MG/5ML | PFIZER CORPORATION HONG KONG LIMITED |
| HK-65291 | DILANTIN EXTENDED CAPSULES 30MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-07909 | DILANTIN CAP 100MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-19932 | DILANTIN INJ 250MG/5ML | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-07913 | DILANTIN SUSP 125MG/5ML | VIATRIS HEALTHCARE HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測沒有任何臨床試驗，文獻也沒有直接顯示 Phenytoin 對三叉神經腫瘤有抗腫瘤作用。高分很可能來自三叉神經痛的間接關聯。
- 本藥在香港已有 5 張許可證，但這不代表它對此新適應症有證據支持。

**若要推進需要：**
- 取得香港衛生署的藥品仿單，補齊警語與禁忌症，這是目前的阻斷性資料缺口。
- 補充詳細的作用機轉資料（MOA），例如查詢 DrugBank。
- 釐清預測的臨床目標：是治療腫瘤本身，還是控制腫瘤相關的神經痛或癲癇發作。
- 搜尋 Phenytoin 與神經腫瘤（如腦腫瘤相關癲癇預防）的直接研究。

**補充觀察：** 同一份預測清單中的反射性癲癇類適應症（進食誘發、排尿誘發、聽源性癲癇等），在機轉上比腫瘤預測更貼近 Phenytoin 的抗癲癇作用。但目前證據仍多為一般癲癇或動物實驗資料，建議列為研究問題，而非推進項目。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

