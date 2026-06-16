---
layout: default
title: Gemcitabine
parent: 高證據等級 (L1-L2)
nav_order: 344
evidence_level: L1
indication_count: 5
---

# Gemcitabine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Gemcitabine：從廣效抗腫瘤化療到女性乳癌

## 一句話總結

Gemcitabine 是核苷類似物（nucleoside analogue）細胞毒性化療藥物，廣泛用於多種實體腫瘤治療。TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，預測分數高達 **99.98%**。本次 Evidence Pack 查詢未直接收集到針對此適應症的臨床試驗或文獻，但依據再利用機轉分析，FDA 已核准 Gemcitabine + paclitaxel 聯合方案用於 HER2 陰性轉移性乳癌，評估等級為 **L1**，此預測實為對已確立療法的再確認。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效抗腫瘤化療（香港未上市，無許可證資料） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Gemcitabine 屬於核苷類似物（antimetabolite），其作用機轉為被細胞誤認為正常核苷（deoxycytidine）而嵌入 DNA，在細胞複製期間抑制 DNA 複製叉的進展，最終觸發細胞凋亡。此機轉不依賴特定驅動基因突變，對快速增殖的多種實體腫瘤均有效。目前 Evidence Pack 中缺乏 DrugBank 完整 MOA 資料，以上描述基於公開文獻資訊。

乳癌細胞（尤其 HER2 陰性亞型）增殖速度快、核苷代謝活躍，對 Gemcitabine 具內在敏感性。當與 paclitaxel 聯用時，paclitaxel 將腫瘤細胞阻滯於 G2/M 期，此時 Gemcitabine 的 DNA 嵌入效率更高，兩者具有明確的細胞動力學協同效應。

臨床層面，Slamon et al. 完成的 Phase 3 RCT 確認了 Gemcitabine + paclitaxel 聯合方案對 HER2 陰性轉移性乳癌具統計顯著的 PFS 與 OS 效益，FDA 已據此核准此聯合方案。TxGNN 以 99.98% 的分數偵測到此關聯，反映知識圖譜對此已確立療法的強烈確認。本次 Evidence Pack 查詢未直接收集到原始試驗資料，建議補充檢索。

---

## 臨床試驗證據

目前無相關臨床試驗登記（本次 Evidence Pack 查詢未收集到針對女性乳癌的 Gemcitabine 臨床試驗）。

> **注意：** 根據機轉分析，Gemcitabine + paclitaxel 已有 FDA 核准的 Phase 3 RCT 支持，但原始試驗資料不在本次查詢範圍內，建議補充查詢 ClinicalTrials.gov（關鍵詞：Gemcitabine, breast cancer, paclitaxel）。

---

## 文獻證據

目前無相關文獻（本次 Evidence Pack 查詢未收集到針對女性乳癌的 Gemcitabine 文獻）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Antimetabolite / Nucleoside Analogue 類） |
| 骨髓抑制風險 | 高（嗜中性白血球減少、血小板減少、貧血為主要劑量限制毒性） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝腎功能、電解質（每療程給藥前後） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈注射劑型，需個人防護裝備（PPE）及密閉系統調配 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TxGNN 預測分數極高（99.98%），且機轉分析顯示 FDA 已核准 Gemcitabine + paclitaxel 用於 HER2 陰性轉移性乳癌，屬已確立療法，非全新再利用場景，故維持「有條件推進」建議。然而 Gemcitabine 在香港尚未取得上市許可，且本次 Evidence Pack 缺乏安全性完整資料，需補充後方可進入正式評估流程。

**若要推進需要：**
- 補查 Slamon et al. Phase 3 RCT 完整資料（ClinicalTrials.gov + PubMed）並納入 Evidence Pack
- 確認 Gemcitabine 在香港的進口/特別用藥許可狀態
- 補充完整警語與禁忌症資料（建議查詢 DrugBank API 及 TFDA/EMA 仿單 PDF）
- 明確 HER2 陰性亞型的患者選擇標準（ER/PR 狀態、療程線別）
- 制定骨髓抑制監測計畫及 Gemcitabine + paclitaxel 聯用的 DDI 評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

