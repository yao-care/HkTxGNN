---
layout: default
title: Ranolazine
parent: 僅模型預測 (L5)
nav_order: 758
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Ranolazine：預測新適應症為腎因性抗利尿不適當症候群 (NSIAD)（證據等級 L5）。原適應症：香港許可證資料未載明"
monitor_inn: "RANOLAZINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Ranolazine：從慢性心絞痛（原適應症資料缺漏）到腎因性抗利尿不適當症候群

## 一句話總結

Ranolazine 是晚期鈉電流（late sodium current）抑制劑，在香港已有 3 張有效許可證，目前以單方製劑上市。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數，屬於初步假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，Ranolazine 是晚期鈉電流（INa-late）抑制劑，對部分脂肪酸氧化以及部分鉀、鈣電流也有作用。

NSIAD 是由血管加壓素 V2 受體（AVPR2）功能獲得性突變所造成，會導致水分滯留與低血鈉，且與血管加壓素本身無關。Ranolazine 對 V2 受體或腎集合管的 cAMP／水通道蛋白-2（AQP2）路徑**沒有已知的直接作用**，因此兩者之間的機轉關聯目前只是推測。

TxGNN 的高分（0.996）屬於計算預測，不等同於證據。若要驗證，需先做前臨床研究，例如 V2 受體訊號分析或 AQP2 轉運試驗。此外，NSIAD 是罕見疾病，多見於兒童，目前以限水、尿素等方式處理。

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
| HK-63607 | RANEXA PROLONGED-RELEASE TABLETS 375MG | 緩釋錠 | 資料未載明 |
| HK-63608 | RANEXA PROLONGED-RELEASE TABLETS 500MG | 緩釋錠 | 資料未載明 |
| HK-63609 | RANEXA PROLONGED-RELEASE TABLETS 750MG | 緩釋錠 | 資料未載明 |

三張許可證均由 A. MENARINI HONG KONG LIMITED 持有，皆為有效的單方製劑。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物—疾病禁忌關聯，非仿單內容）：長 QT 症候群、家族性長 QT 症候群、尖端扭轉型心室頻脈、腎臟疾病、輸尿管積膿、肝硬化。
- **藥物交互作用**：共記錄 100 筆，以下為資料中列出的部分項目。
  - **嚴重 (Major)**：Aprepitant、Dexamethasone、Clarithromycin、Dolasetron、Eliglustat
  - **中度 (Moderate)**：Famotidine、Metformin、Loperamide、Bisacodyl、Budesonide、Canagliflozin、Dapagliflozin、Empagliflozin 等
  - **輕微 (Minor)**：Bupropion、Lorcaserin、Cimetidine
- 此外，Ranolazine 涉及 CYP3A4 與 P-gp 的交互作用，並會延長 QT 間期。對於罕見且多為兒童的 NSIAD，這些風險需審慎權衡。

仿單的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測，沒有任何臨床或文獻證據（L5）。
- 藥理上缺乏與 V2 受體路徑的已知關聯，且藥物交互作用多、有 QT 延長風險，因此不建議推進。

**若要推進需要：**
- 前臨床機轉驗證（V2 受體訊號、AQP2 轉運試驗）
- 取得完整作用機轉（MOA）資料
- 取得香港原廠仿單的警語與禁忌症，完成安全性篩選
- 補齊香港許可證的核准適應症資料
- 評估在目標族群（多為兒童）使用的風險效益，包含 QT 與藥物交互作用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

