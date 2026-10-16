---
layout: default
title: Alfentanil
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Alfentanil：預測新適應症為腎因性抗利尿不當症候群 (NSIAD)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "ALFENTANIL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Alfentanil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Alfentanil：從（原適應症未載明）到腎因性抗利尿不當症候群

## 一句話總結

Alfentanil 是一種 mu 類鴉片受體促效劑，在香港已有上市許可證，但目前資料未載明其核准適應症。
TxGNN 模型預測它可能對**腎因性抗利尿不當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 腎因性抗利尿不當症候群 (NSIAD) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Alfentanil 屬於鴉片類止痛藥，一般認為是作用於 mu 類鴉片受體。

NSIAD 是由抗利尿激素第二型受體（AVPR2）的活化型突變所引起。受體在沒有血管加壓素的情況下持續活化，導致水分滯留與低血鈉。鴉片類藥物可影響血管加壓素的釋放，也可能經由中樞作用造成類似 SIADH 的抗利尿效果。

不過，NSIAD 的問題出在血管加壓素分泌下游的受體本身，鴉片類藥物理論上無法矯正這種異常，反而可能加重水分滯留與低血鈉。這個預測較可能是知識圖譜的假象（例如與血管加壓素或水分平衡路徑的間接關聯），而不是具生物學合理性的治療機轉。由於原始作用機轉資料缺失，目前無法進一步驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-23819 | RAPIFEN INJ 0.5MG/ML | 未載明（注射劑） | 未載明 |

製造商：DCH Auriga (Hong Kong) Limited – Healthcare Division

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單內容）：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、低血壓疾患、假性腦瘤、顱內高壓。
- **藥物交互作用**：共查詢到 100 筆，以下為部分主要項目。
  - **嚴重 (Major)**：Aprepitant、Bupropion、Clarithromycin、Clotrimazole、Dexfenfluramine、Dolasetron、Fenfluramine、Granisetron、Lorcaserin
  - **中度 (Moderate)**：Atropine、Cimetidine、Clidinium、Dexamethasone、Dicyclomine、Dronabinol、Eluxadoline、Glycopyrronium、Hyoscyamine、Mazindol

仿單的警語與禁忌資料尚未取得，其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數支持，沒有臨床試驗或文獻佐證（證據等級 L5）。
- 機轉上，鴉片類藥物不太可能矯正受體持續活化所致的 NSIAD，反而可能惡化低血鈉，且該藥的知識圖譜禁忌包含腎臟疾病。

**若要推進需要：**
- 取得完整的作用機轉資料（MOA），並重新評估與 AVPR2 路徑的機轉關聯
- 取得香港仿單的警語、禁忌與核准適應症
- 進行系統性文獻與臨床試驗檢索，確認是否有任何支持或反對的證據
- 在釐清生物學合理性之前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

