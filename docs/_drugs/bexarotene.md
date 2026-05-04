---
layout: default
title: Bexarotene
parent: 中證據等級 (L3-L4)
nav_order: 101
evidence_level: L3
indication_count: 3
---

# Bexarotene
{: .fs-9 }

證據等級: **L3** | 預測適應症: **3** 個
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

# Bexarotene：從皮膚T細胞淋巴瘤到原發性皮膚B細胞淋巴瘤

## 一句話總結

Bexarotene 是一種選擇性 RXR（視黃酸 X 受體）激動劑，已獲 FDA 核准用於皮膚T細胞淋巴瘤（CTCL）的治療，目前香港尚未上市。
TxGNN 模型預測它可能對**原發性皮膚B細胞淋巴瘤（Primary Cutaneous B-cell Lymphoma, PCBCL）** 有效，目前有 **1 個臨床試驗**（間接相關）和 **13 篇文獻**支持這個研究方向。
值得注意的是，本次同批預測中 **Sézary Syndrome**（排名第 2，L1 等級）和**淋巴肉瘤**（排名第 3，L2 等級）的佐證強度更高，機轉關聯更為明確，建議優先納入評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚T細胞淋巴瘤（Cutaneous T-cell Lymphoma, CTCL）— FDA 核准 |
| 預測新適應症 | 原發性皮膚B細胞淋巴瘤（Primary Cutaneous B-cell Lymphoma） |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Bexarotene（品牌名 Targretin）是一種合成類視黃酸，選擇性結合並活化視黃酸 X 受體（RXR-α、RXR-β、RXR-γ）三種亞型。RXR 作為配體依賴性轉錄因子，可與 RAR、PPAR、LXR 等核受體形成異二聚體，進而調控淋巴細胞的增殖、分化與凋亡。在 CTCL 中，bexarotene 透過 RXR 訊號活化誘導惡性 T 細胞週期阻滯，並調節 Th2/Th1 免疫微環境平衡，此機轉已獲大量臨床前與臨床數據支持，為其 FDA 核准依據。

PCBCL 與 CTCL 同屬原發性皮膚淋巴瘤，在解剖位置（皮膚局限性）和腫瘤微環境組成上具有結構相似性。理論上，RXR 訊號通路對 B 淋巴細胞的成熟與增殖亦具一定調控作用，但目前缺乏直接針對 PCBCL 的 bexarotene 臨床試驗或機轉研究。TxGNN 的高分預測（99.44%）可能主要反映兩類疾病在知識圖譜中同歸「皮膚淋巴瘤」大節點的結構相似性，而非 B 細胞特異性的 RXR 依賴性機轉。

綜合評估，對 PCBCL 的再利用可能性需謹慎看待：現有間接證據（廣義皮膚淋巴瘤文獻）支持進一步探索，但在正式推進前，需先確認 B 細胞惡性腫瘤中 RXR 訊號活化的細胞效應。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01134341](https://clinicaltrials.gov/study/NCT01134341) | Phase 1 | 已完成 | 34 | Pralatrexate 聯合口服 Bexarotene 用於復發/難治性 CTCL 患者，探討推薦劑量、安全性與初步療效。主要為 CTCL（T 細胞），對 PCBCL 為間接相關佐證，無法作為 PCBCL 療效直接依據。 |

> **注意**：目前無直接針對 PCBCL 的 Bexarotene 臨床試驗登記。另一筆試驗（NCT05106192）因已撤回且從未招募患者，且介入藥物為 Triamcinolone Acetonide 而非 Bexarotene，不具參考價值，故未列入。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31466585](https://pubmed.ncbi.nlm.nih.gov/31466585/) | 2019 | Review/Guideline | Dermatologic Clinics | PCBCL 診斷與處置綜述；強調初始評估排除系統性侵犯的重要性，局部療法為首選，系統性治療資料有限 |
| [34059248](https://pubmed.ncbi.nlm.nih.gov/34059248/) | 2021 | Review/Guideline | Medical Clinics of North America | 皮膚淋巴瘤（含 T 細胞與 B 細胞亞型）的全面診療指引，涵蓋 PCBCL 分類與治療選擇 |
| [29881891](https://pubmed.ncbi.nlm.nih.gov/29881891/) | 2018 | Retrospective Case Series | Der Hautarzt | 163 例原發性皮膚淋巴瘤病例系列分析，呈現完整疾病譜分佈與臨床特徵 |
| [19786826](https://pubmed.ncbi.nlm.nih.gov/19786826/) | 2009 | Narrative Review | Skin Pharmacol Physiol | 皮膚淋巴瘤（含 CTCL 及 CBCL）新型皮膚導向療法綜述；提及 Retinoid 類（包含 Bexarotene）在廣義皮膚淋巴瘤中的潛在應用 |
| [31932947](https://pubmed.ncbi.nlm.nih.gov/31932947/) | 2020 | Review | Der Pathologe | 皮膚淋巴瘤臨床表現、診斷與治療綜述（2020 版）；Bexarotene 列為晚期 MF/SS 的系統性治療選項之一 |
| [14616487](https://pubmed.ncbi.nlm.nih.gov/14616487/) | 2003 | Review/Guideline | Australasian J Dermatol | 原發性皮膚淋巴瘤（含 T/B 細胞亞型）管理策略；提及 Retinoid 治療選項及 B 細胞亞型的放射治療偏好 |
| [22031653](https://pubmed.ncbi.nlm.nih.gov/22031653/) | 2011 | Case Report | Dermatology Online Journal | 復發性原發性皮膚邊緣區 B 細胞淋巴瘤（PCMZL）病例報告，PET-CT 確認皮膚局限性，探討局部治療策略 |
| [20806174](https://pubmed.ncbi.nlm.nih.gov/20806174/) | 2010 | Review | Therapeutische Umschau | 皮膚淋巴瘤（T/B 細胞）WHO/EORTC 分類、診斷與治療概述，介紹 Bexarotene 在 CTCL 中的核准地位 |
| [23941646](https://pubmed.ncbi.nlm.nih.gov/23941646/) | 2013 | Case Report | J Cutaneous Pathology | 皮膚濾泡輔助 T 細胞淋巴瘤（CTfhCL）誤診為 PCBCL 的案例；Rituximab 治療失敗後改診，強調 PCBCL 鑑別診斷的重要性 |
| [31511903](https://pubmed.ncbi.nlm.nih.gov/31511903/) | 2019 | Review | Der Hautarzt | 皮膚淋巴瘤臨床表現、診斷與治療綜述（2019 版），PCBCL 亞型分類與管理策略 |

---

## 細胞毒性

Bexarotene 為抗腫瘤藥物（核受體靶向 Retinoid 類），適用本章節評估。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（核受體調節劑）— RXR 選擇性激動劑，非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 低至中度（口服膠囊可能引起嗜中性白血球減少，需定期監測） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含白血球分類）、空腹血脂（三酸甘油酯）、甲狀腺功能（TSH、Free T4）、肝腎功能 |
| 處置防護 | 請參考原廠仿單的細胞毒性藥物處置規範；致畸胎性風險高，育齡期患者需嚴格避孕 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前缺乏直接針對 PCBCL 的 Bexarotene 臨床試驗，現有文獻證據僅為廣義皮膚淋巴瘤的間接相關資料（L3），且 Bexarotene 的 RXR 機轉主要在 T 細胞惡性腫瘤中有充分實證，對 B 細胞亞型的適用性尚未獲充分驗證，建議暫緩推進。

**若要推進需要：**
- 補充作用機轉資料（MOA）：確認 RXR 訊號活化對 B 淋巴細胞惡性增殖的細胞效應（建議查詢 DrugBank API 及文獻）
- 補充香港/台灣仿單警語與禁忌資料（TFDA/衞生署官網 PDF 解析）
- 評估是否優先推進 **Sézary Syndrome**（L1，Proceed with Guardrails）或**淋巴肉瘤**（L2，Proceed with Guardrails）等佐證更強的適應症
- 如確認推進 PCBCL，需設計 Phase 2 探索性試驗設計方案，並建立 B 細胞皮膚淋巴瘤的生物標記篩選策略（如 RXR 表現量）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

