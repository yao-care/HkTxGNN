---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 5
---

# Felodipine
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

以下是根據 Evidence Pack 產生的藥物再利用評估報告：

---

# Felodipine：從高血壓到肺高壓（多因性不明）

## 一句話總結

Felodipine 是一種二氫吡啶類（DHP）鈣離子通道阻斷劑，臨床上用於高血壓治療。
TxGNN 模型預測它可能對**多因性不明肺高壓（pulmonary hypertension with unclear multifactorial mechanism）**有效，
然而目前**無臨床試驗、無直接相關文獻**支持此預測，5 項預測適應症全數停留於模型推論層級（L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（DHP-CCB 類；香港無登記許可） |
| 預測新適應症 | 多因性不明肺高壓 (pulmonary hypertension with unclear multifactorial mechanism) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Felodipine 詳細的作用機轉資料。根據已知資訊，Felodipine 屬於 DHP 類 L 型鈣離子通道阻斷劑，透過阻斷血管平滑肌細胞的電壓敏感性鈣離子通道、抑制鈣離子內流，達到血管擴張與降壓效果，機轉上可能適用於肺高壓的血管阻力調控。

DHP-CCB 理論上可擴張肺動脈平滑肌、降低肺血管阻力（PVR）——這是 TxGNN 推論的核心機轉基礎。在 WHO Group 1 PAH（特發性肺動脈高壓）中，部分 CCB（nifedipine、diltiazem、amlodipine）已在急性血管反應試驗（AVT）陽性患者中取得核准，提供了同類藥物的概念驗證。

然而，預測的適應症「多因性不明肺高壓」本身異質性極高，CCB 的療效難以一概而論，且 Felodipine 迄今**無針對此族群的獨立 RCT**。更值得注意的是，Rank 2 預測（肺疾病/缺氧性 PH，WHO Group 3）在現行指引中被明確**不建議**使用 CCB——CCB 造成的肺血管舒張可能加重通氣/灌流（V/Q）失配，導致動脈血氧飽和度進一步下降，安全疑慮不可迴避。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對 Felodipine + 多因性不明肺高壓的組合搜尋，結果為零，目前無直接相關文獻。

> **備註（Rank 2 適應症）**：針對「肺疾病/缺氧性 PH」的 PubMed 搜尋返回 20 篇結果，但內容均為缺氧生理學的通論文獻（腦老化、腫瘤缺氧、免疫缺氧等），**不含** Felodipine 與肺高壓的直接研究，不構成支持性證據。

---

## 所有預測適應症總覽

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 | 主要問題 |
|-----|------|-----------|---------|------|---------|
| 1 | 多因性不明肺高壓 | 99.91% | L5 | Hold | 異質性高，無 felodipine 個別 RCT |
| 2 | 肺疾病/缺氧性肺高壓（WHO Group 3） | 99.91% | L5 | Hold | 指引明確不推薦 CCB；可能惡化 V/Q 失配 |
| 3 | 惡性腎血管性高血壓 | 99.90% | L5 | Hold | 首選 RAAS 阻斷劑；CCB 僅為輔助，無獨立資料 |
| 4 | 惡性高血壓腎病 | 99.90% | L5 | Hold | 急性期需靜脈製劑精確控壓；口服製劑藥動學控制力不足 |
| 5 | Braddock 症候群 | 99.88% | L5 | Hold | 遺傳轉錄調控缺陷（MED13L），與 CCB 機轉無合理連結 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（所有 5 項預測適應症）**

**理由：**
所有預測適應症均為 L5 層級，完全缺乏臨床試驗與直接文獻支持。Rank 2（WHO Group 3 PH）更存在現行指引明確的安全疑慮，主動推進的風險明確高於潛在獲益；其餘適應症則缺乏機轉假說或藥物特異性資料。

**若要推進需要：**
- 補充 Felodipine 詳細 MOA 資料（查詢 DrugBank API）
- 補充香港衛生署核准仿單的安全警語與禁忌症（下載 PDF 並解析）
- 若評估 Group 1 PAH 方向：需設計以 Felodipine 為主角的 AVT 試驗方案，不能直接沿用同類 CCB 資料
- **排除** Rank 2（Group 3 PH）方向：有明確安全顧慮，不建議進入後續評估
- **排除** Rank 5（Braddock 症候群）方向：需先建立機轉假說才有評估前提
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

