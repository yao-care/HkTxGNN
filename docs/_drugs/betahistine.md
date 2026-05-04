---
layout: default
title: Betahistine
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Betahistine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Betahistine：從梅尼爾氏病到不寧腿症候群

## 一句話總結

Betahistine 是組織胺衍生物，在歐洲及亞洲多國廣泛核准用於梅尼爾氏病與前庭性眩暈的治療，但目前在香港尚未取得上市許可。
TxGNN 模型預測它可能對**不寧腿症候群 (Restless Legs Syndrome)** 有效，
然而目前**無任何臨床試驗或文獻**支持此方向，屬純模型預測（L5），建議暫緩推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港未上市（全球主要核准用途：梅尼爾氏病、前庭性眩暈） |
| 預測新適應症 | 不寧腿症候群 (Restless Legs Syndrome) |
| TxGNN 預測分數 | 98.51% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Betahistine 的詳細作用機轉資料。根據已知資訊，Betahistine 是組織胺類似物，同時作為 H1 受體弱激動劑及 H3 受體強拮抗劑（反向激動劑），透過改善內耳微循環及調節前庭核組織胺能回路，在梅尼爾氏病與前庭性眩暈的治療中已有充分的全球藥理依據。

TxGNN 預測 Betahistine 用於不寧腿症候群（RLS）的理論基礎為：H3 受體拮抗可能間接調節黑質紋狀體多巴胺能突觸傳遞——H3 異質受體存在於多巴胺能末梢，而多巴胺功能不足正是 RLS 核心病理機轉之一。若 H3 拮抗能促進多巴胺釋放，理論上可緩解 RLS 症狀。

然而，此推論屬**多級間接連結**，目前無任何基礎研究、臨床前研究或臨床研究驗證 Betahistine 對 RLS 的療效。98.51% 的高預測分數可能反映知識圖譜中「組織胺—多巴胺—睡眠障礙」相關節點間的拓樸接近性，而非直接藥理作用。相比之下，Betahistine 在同一次預測中針對梅尼爾氏病（各亞型評分 98.34%）及周邊性眩暈（98.07%）均有豐富的臨床試驗與文獻支持，對照之下更突顯 RLS 預測需謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Betahistine 目前在香港**未上市**，衛生署無核准許可證紀錄。

> 備注：Betahistine（商品名 Serc®）在歐洲、俄羅斯及亞洲多國已核准上市，主要適應症為梅尼爾氏病及前庭性眩暈。若未來考慮在香港引進，需向衛生署申請藥品登記。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 對 Betahistine 用於不寧腿症候群的預測分數雖高（98.51%），但機轉連結屬多級間接推論，目前完全缺乏支持此適應症的基礎、臨床前或臨床研究，證據等級僅為 L5。此外，Betahistine 在香港尚未上市，整體風險效益比不支持現階段推進 RLS 適應症開發。

**若要推進需要：**
- 取得 Betahistine 完整作用機轉資料，尤其釐清 H3 受體拮抗對黑質紋狀體多巴胺能路徑的直接效應
- 執行基礎研究：評估 Betahistine 在 RLS 動物模型中的行為學及神經化學效應
- 取得完整安全性資料（仿單警語、禁忌症、藥物交互作用）
- 評估 Betahistine 在香港的引進可行性（衛生署藥品登記途徑）
- 若基礎研究結果支持，方可規劃概念驗證（Proof-of-Concept）臨床試驗
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

