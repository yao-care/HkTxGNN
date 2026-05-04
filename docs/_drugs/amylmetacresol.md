---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol：從抗菌防腐劑到馬尾症候群

## 一句話總結

Amylmetacresol（AMC）是一種酚類廣譜抗菌化合物，常見於局部抗菌製劑（如咽喉含片），其作用以破壞細菌細胞膜為主。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，預測分數高達 99.99%，
但目前本批次 10 個預測適應症**均無任何臨床試驗或文獻**支持，全部為純模型預測結果（L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部抗菌（台灣未上市，無許可證適應症紀錄） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據已知資訊，Amylmetacresol 屬酚類抗菌化合物，透過破壞細菌細胞膜發揮廣譜抗菌作用，並具輕度抗病毒活性，現有應用主要為局部給藥的抗感染治療。

馬尾症候群（Cauda Equina Syndrome）是由腰椎管壓迫（常見原因：椎間盤突出、腫瘤、外傷）引起的多發性神經根損傷，其核心病生理為物理性壓迫與局部缺血，**與酚類抗菌機轉無已知直接關聯**。目前亦缺乏 AMC 具抗炎或神經保護活性的分子層次證據，機轉合理性極低。

值得特別說明的是，在本次 TxGNN 輸出的 10 個預測適應症中，**感染性前葡萄膜炎（Infectious Anterior Uveitis，排名第 7，分數 99.57%）**的機轉合理性最高：細菌性或病毒性前葡萄膜炎的感染病因與 AMC 的抗菌/抗病毒特性具有直接對應，若後續評估，可優先考慮以此適應症作為研究切入點，並評估眼部局部給藥的可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

Amylmetacresol 目前在台灣**尚未上市**，無任何藥品許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高，但最高排名適應症（馬尾症候群）與 AMC 的抗菌機轉缺乏合理的藥理連結；本批次所有 10 個適應症均無臨床試驗或文獻佐證，目前僅停留在模型預測階段（L5），尚未達到可推進評估的最低證據門檻。

**若要推進需要：**
- 補充 AMC 完整的作用機轉資料（DrugBank MOA、藥理分類）
- 針對機轉合理性最高的適應症（**感染性前葡萄膜炎**）進行深度文獻搜尋，擴大關鍵字範圍（如「phenol antiseptic + uveitis」「AMC + ocular infection」）
- 取得台灣或主要市場（英國、歐盟）的藥品仿單，補充禁忌症與警語資訊
- 評估眼部局部給藥途徑的藥物動力學可行性及眼毒性數據

> ⚠️ 本報告僅供研究參考，不構成醫療建議。所有老藥新用候選需經臨床驗證後方可應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

