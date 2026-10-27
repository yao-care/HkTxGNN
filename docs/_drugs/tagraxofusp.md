---
layout: default
title: Tagraxofusp
parent: 僅模型預測 (L5)
nav_order: 847
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tagraxofusp：預測新適應症為斜視 (Esotropia)（證據等級 L5）。原適應症：CD4+/CD56+ 血液皮膚腫瘤（CD4+/CD56+ hematodermic neoplasm）"
monitor_inn: "Tagraxofusp"
predicted_indications: ["esotropia", "pre-malignant neoplasm", "inner ear neoplasm", "benign neoplasm of tongue", "bronchial adenomas/carcinoids childhood", "ductal or ductular proliferation", "chondroid hamartoma", "non-seminomatous lesion", "cystic neoplasm", "thyroglossal duct cyst"]
---

# Tagraxofusp
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Tagraxofusp：從 CD4+/CD56+ 血液皮膚腫瘤到斜視（Esotropia）
{: .text-alpha }

## 一句話總結

Tagraxofusp 是一種針對 CD123 的細胞毒性融合蛋白，原本用於 CD4+/CD56+ 血液皮膚腫瘤（母細胞性漿細胞樣樹突細胞腫瘤）。
TxGNN 模型預測它可能對**斜視 (Esotropia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，且機轉上找不到合理關聯，這個高分較可能是圖譜預測的假象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | CD4+/CD56+ 血液皮膚腫瘤（CD4+/CD56+ hematodermic neoplasm） |
| 預測新適應症 | 斜視 (Esotropia) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tagraxofusp 是一種 CD123 導向的細胞毒素（IL-3 與截短型白喉毒素融合），可殺死表現 CD123 的細胞，這與其在 CD123 高表現的血液惡性腫瘤中的療效相符。

斜視是眼球運動異常的疾病，已知病理中沒有 CD123 驅動的機制。原適應症為血液腫瘤，兩者在疾病生物學上幾乎沒有交集，因此這個預測缺乏機轉上的支持。

整體而言，99.73% 的分數更像是知識圖譜的預測假象，而非有生物學依據的訊號。此外，本藥具有毛細血管滲漏症候群、肝毒性等已知毒性，用於斜視這類非致命疾病，風險效益並不理想。

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
| HK-68070 | ELZONRIS CONCENTRATE FOR SOLUTION FOR INFUSION 1000MCG/1ML（廠商：A. MENARINI HONG KONG LIMITED） | 輸注用濃縮液（資料未標示） | 資料未提供 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶細胞毒素（CD123 導向的 IL-3 白喉毒素融合蛋白） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單；已知毒性提示應關注肝功能與毛細血管滲漏相關表現 |
| 處置防護 | 請參考原廠仿單 |

請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：已查得 66 筆交互作用，以下為其中的主要項目，嚴重度皆為中度 (Moderate)，且集中在降血糖藥物：
  - 雙胍類／其他口服降血糖藥：Metformin、Pioglitazone、Glimepiride、Chlorpropamide、Acarbose
  - DPP-4 抑制劑：Alogliptin、Saxagliptin、Linagliptin
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin
  - GLP-1 受體促效劑：Albiglutide、Dulaglutide、Semaglutide
  - 胰島素類：Insulin aspart、degludec、detemir、glargine、glulisine、human (isophane)

  若病人同時使用降血糖藥物，需留意血糖變化。

其他警語與禁忌症資料目前缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有臨床試驗或文獻佐證，且斜視與 CD123 驅動的病理之間找不到機轉關聯。
- 藥物毒性顯著，用於非致命的眼科疾病風險效益不佳。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並確認斜視是否存在任何 CD123 相關的生物學依據
- 取得香港衛生署的仿單，完成警語與禁忌症的安全性審查（目前為阻斷性資料缺口）
- 若仍想探索 TxGNN 的高分預測，建議優先檢視與 CD123 較相關的血液腫瘤類（例如預測清單中的「pre-malignant neoplasm」，需先界定具體疾病如骨髓增生異常症候群），而非斜視
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

