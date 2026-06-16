---
layout: default
title: Fenfluramine
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 4
---

# Fenfluramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Fenfluramine：從 Dravet 症候群到 16p11.2 近端微缺失症候群

## 一句話總結

Fenfluramine（芬氟拉明）是一種血清素能藥物，近年以 Fintepla 品牌在多個國家獲核准作為 Dravet 症候群（難治性癲癇）的輔助治療。TxGNN 模型預測它可能對 **16p11.2 近端微缺失症候群 (proximal 16p11.2 microdeletion syndrome)** 有效，然而目前**無任何臨床試驗或文獻**直接支持此適應症，屬純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（已知用於 Dravet 症候群癲癇發作輔助治療） |
| 預測新適應症 | 16p11.2 近端微缺失症候群 (proximal 16p11.2 microdeletion syndrome) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前此 Evidence Pack 缺乏完整的作用機轉（MOA）資料。根據 TxGNN 預測理由與已知文獻背景，推論如下：

**機轉連結（二階推論）**：16p11.2 近端微缺失症候群涉及染色體 16p11.2 區段多個基因的單倍劑量不足，包括 SH2B1（瘦素/胰島素訊號調控）、MAPK3/ERK1（MAP 激酶通路）等，臨床表現涵蓋自閉症譜系障礙、癲癇、肥胖及智能障礙等異質性表現型。Fenfluramine 在 Dravet 症候群的核心療效機轉為活化 5-HT2C 受體，進而調節 HCN1 通道功能與 sigma-1 受體，抑制異常神經放電。

**適用性推論**：部分 16p11.2 近端微缺失患者具有癲癇表現型，TxGNN 模型可能透過「Dravet 症候群抗癲癇機轉 → 16p11.2 相關癲癇表現型」的路徑建立連結。在本批預測中，此適應症被評估為間接機轉關聯度最強者。

**重要限制**：此連結屬**二階推論**，尚無直接路徑研究支持。此外，16p11.2 缺失症候群表現型異質性高，並非所有患者均有癲癇，且其神經發育異常的病理機轉與 Dravet 症候群的離子通道病變（SCN1A 功能喪失）並不相同，不能直接類比。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：Fenfluramine 歷史上因與心臟瓣膜病變及肺動脈高壓相關而於 1997 年在多個國家撤市；現以低劑量重新核准用於 Dravet 症候群，附有嚴格的心臟監測要求（REMS 計畫）。申請任何新適應症前，心臟安全性評估為必要前提。

---

## 結論與下一步

**決策：Hold**

**理由：**
預測連結屬二階推論，目前無任何臨床試驗或文獻直接支持 fenfluramine 用於 16p11.2 近端微缺失症候群；加以該藥在香港未上市、MOA 及安全性完整資料缺失，且該藥既有的心臟安全性疑慮尚需在新適應症框架下重新評估，現階段不宜推進。

**若要推進需要：**
- 補充完整作用機轉（MOA）資料（DrugBank API / 原廠技術文件）
- 取得仿單警語與禁忌症資料（解析原廠 Fintepla 仿單 PDF）
- 尋找 fenfluramine 用於 16p11.2 或相關神經發育症候群癲癇亞群的前臨床研究（動物模型、病理機轉研究）
- 確認 16p11.2 近端微缺失患者中癲癇亞群的比例與神經電生理表現型特徵
- 評估心臟瓣膜安全性監測計畫在新適應症患者族群中的可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

