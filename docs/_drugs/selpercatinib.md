---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 679
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Selpercatinib：從 RET 突變腫瘤到肺動脈高壓

## 一句話總結

Selpercatinib 是高選擇性 RET 酪氨酸激酶抑制劑，用於 RET 突變/融合陽性的甲狀腺癌與非小細胞肺癌。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，
但目前**無相關臨床試驗**，僅有 **2 篇文獻**（且皆非直接支持此適應症的療效研究），機轉關聯性薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | RET fusion-positive 非小細胞肺癌／RET-mutant 甲狀腺癌（境外核准，未在香港上市） |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Selpercatinib 正式的作用機轉資料庫紀錄（DrugBank MOA 欄位為資料缺口）。根據既有藥理學認知，Selpercatinib 為高選擇性 RET 酪氨酸激酶抑制劑，核准用於 RET 融合陽性非小細胞肺癌及 RET 突變甲狀腺癌。

RET 訊號路徑與肺血管平滑肌細胞增生/重塑之間存在理論上的 VEGFR/RET crosstalk 假說，這可能是 TxGNN 知識圖譜產生高分關聯的來源。然而，**目前沒有任何直接分子機轉文獻證實 Selpercatinib 對肺動脈高壓具有治療效果**，此預測應視為知識圖譜嵌入相似性的推論結果，而非機轉已驗證的候選適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective analysis | Therapeutic Advances in Medical Oncology | Selpercatinib 於 RET 融合陽性 NSCLC 真實世界治療通道之回溯性分析（與肺動脈高壓無直接關聯） |
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world safety study | Frontiers in Pharmacology | 比較 Pralsetinib 與 Selpercatinib 之不良事件差異（FDA 不良事件通報系統分析） |

> 註：上述兩篇文獻均未直接研究 Selpercatinib 對肺動脈高壓的療效，僅與原適應症（NSCLC）安全性相關。

---

## 香港上市資訊

Selpercatinib 目前未在香港取得任何藥物許可證，無上市紀錄。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（RET 選擇性酪氨酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Selpercatinib 未在香港上市，且 TFDA 仿單警語/禁忌資料為 **Blocking** 等級缺口，無法進行 S1 安全性初評。
- 肺動脈高壓此適應症（TxGNN 評分最高）僅有 2 篇間接文獻、無臨床試驗支持，機轉關聯為理論推測，證據等級 L5。
- 其餘兩項預測適應症（migraine disorder、migraine with brainstem aura）完全無臨床試驗或文獻支持，機轉上與 RET 訊號路徑無已知關聯，亦判定 Hold。

**若要推進需要：**
- 補齊 Selpercatinib 作用機轉（MOA）完整資料（DrugBank API 查詢）
- 取得 TFDA／原廠仿單警語與禁忌資料，以解除 Blocking 缺口
- 尋找 RET 訊號路徑與肺血管重塑的直接臨床前證據，驗證機轉合理性
- 若無新增證據，建議暫緩此候選案並定期監測新文獻/試驗登記
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

