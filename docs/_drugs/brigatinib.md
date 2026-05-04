---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib：從 ALK 陽性非小細胞肺癌 到 牙齦纖維瘤病

## 一句話總結

Brigatinib 是第二代 ALK 激酶抑制劑，原用於 ALK 陽性轉移性非小細胞肺癌（NSCLC）的治療（美國 FDA 已核准，香港尚未上市）。TxGNN 模型預測它可能對**牙齦纖維瘤病 (Fibromatosis, Gingival)** 有效，預測分數達 99.89%，惟目前**無任何臨床試驗或文獻**支持此方向，屬純圖神經網路拓撲推論結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ALK 陽性轉移性非小細胞肺癌（美國已核准；香港未上市） |
| 預測新適應症 | 牙齦纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Brigatinib 是一種次世代小分子 ALK（間變性淋巴瘤激酶）抑制劑，同時具備廣泛多靶點激酶抑制活性（涵蓋 EGFR、ROS1、FLT3 等），以 ATP 競爭方式結合 ALK 激酶結構域並阻斷下游增殖信號。核准適應症針對攜帶 ALK 重排（如 EML4-ALK 融合）的晚期 NSCLC，多個 Phase 3 RCT（ALTA-1L 等）已證明其對 crizotinib 初治及耐藥患者均具優越療效。本資料集中詳細 MOA 資料尚缺正式記錄，建議後續補齊。

牙齦纖維瘤病（Gingival Fibromatosis）是一種罕見遺傳性或特發性疾病，以牙齦組織廣泛纖維增生為特徵，主要致病機轉涉及 **SOS1、PTCH1、MMP2** 基因突變所驅動的纖維母細胞過度增殖。上述路徑與 Brigatinib 的主要靶點 ALK/EGFR 信號軸**無已知直接交集**，目前無前臨床或臨床資料支持。

本次預測的**生物合理性偏低**。TxGNN 高分係源於知識圖譜節點間的拓撲鄰近性推論，而非確立的機轉聯繫。在完全缺乏文獻佐證的情況下，此預測需高度謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 細胞毒性

Brigatinib 為抗腫瘤靶向藥物（ALK 陽性 NSCLC 核准適應症），屬抗腫瘤藥物範疇，適用本章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（次世代 ALK／多靶點酪氨酸激酶抑制劑） |
| 骨髓抑制風險 | 低至中度（相較傳統化療風險較低） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含白血球分類）、肝功能（ALT/AST）、腎功能、血壓、肺功能（間質性肺病風險） |
| 處置防護 | 依細胞毒性藥物處置規範操作；用藥初期（尤其前 7 日）需密切監控早期肺毒性（ILD/pneumonitis）症狀 |

> 請參考原廠仿單的警語與注意事項，以取得完整毒性資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **補充說明**：本資料集缺乏香港衛生署仿單警語及禁忌症正式資料（嚴重度：Blocking），無法完成 S1 安全性初評。根據現有文獻揭示的已知安全性訊號，Brigatinib 具有早期間質性肺病（ILD/pneumonitis）風險（發生率約 3–9%），亦有腫瘤溶解症候群（TLS）罕見個案報告（PMID [34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/)），任何新適應症啟動前需充分評估患者風險。

---

## 結論與下一步

**決策：Hold**

**理由：**
牙齦纖維瘤病的已知致病機轉（SOS1/PTCH1/MMP2 路徑）與 Brigatinib 主要靶點（ALK/EGFR 激酶抑制）無已知交集，生物合理性不足；且目前完全缺乏支持此適應症的臨床試驗或文獻（L5 等級），不符合推進條件。

**若要推進需要：**
- **補齊 MOA 資料（Data Gap DG002）**：確認 Brigatinib 是否對 MMP2/SOS1 相關纖維增生路徑具有任何抑制活性
- **取得香港衛生署核准仿單（Data Gap DG001）**：完成 S1 安全性初評，確認警語、禁忌與藥物交互作用
- **前臨床探索**：若仍欲推進，需進行體外試驗評估 Brigatinib 對牙齦纖維母細胞株（如 ATCC HGF-1）的增殖抑制活性
- **考慮轉向具更強機轉依據的替代預測**：本資料集中 Rank 7（ALK 陽性神經內分泌腫瘤，L4 前臨床證據）及 Rank 10 附帶發現中的 **NF2 相關許旺瘤病**（PMID [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/)，2024 年 Phase 2 前瞻性研究）具備更紮實的 ALK/多靶點機轉連結，建議優先評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

