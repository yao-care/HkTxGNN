---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atezolizumab：預測新適應症為前列腺尿道上皮癌 (Prostatic Urethra Urothelial Carcinoma)（證據等級 L5）。原適應症：移行細胞癌／泌尿道上皮癌"
monitor_inn: "Atezolizumab"
predicted_indications: ["prostatic urethra urothelial carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Atezolizumab
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

## Atezolizumab：從泌尿道上皮癌（移行細胞癌）到前列腺尿道上皮癌
{: .text-alpha }

## 一句話總結

Atezolizumab 是一種 PD-L1 抑制劑，原本用於泌尿道上皮癌（移行細胞癌）的治療。
TxGNN 模型預測它可能對**前列腺尿道上皮癌 (Prostatic Urethra Urothelial Carcinoma)** 有效，
目前有 **1 個臨床試驗**（Phase 1b，間接證據），尚無直接相關文獻。這個預測多半是原適應症向相近部位的延伸，而非真正的新疾病。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 移行細胞癌／泌尿道上皮癌（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 前列腺尿道上皮癌 (Prostatic Urethra Urothelial Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L3（排名第 1 的預測；僅有 Phase 1b 間接證據，保守判定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold（列為研究問題，待補充資料） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Atezolizumab 是 PD-L1 抑制劑，已核准用於泌尿道上皮癌（移行細胞癌），機轉上可能適用於組織學與解剖位置相近的前列腺尿道上皮癌。

前列腺尿道上皮癌同屬泌尿道上皮腫瘤，PD-L1 路徑的理論基礎可以延伸。TxGNN 的高分（99.98%）與這種重疊相符。

需要注意：這比較像是把既有適應症擴展到次部位，而不是全新的藥物再利用。目前也沒有針對此次部位的專屬資料。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 | 進行中（不再招募） | 914 | Cabozantinib 單用或併用 Atezolizumab，用於局部晚期或轉移性實體瘤（含泌尿道上皮癌）的安全性、耐受性與初步療效；未單獨報告前列腺尿道部位，結果尚不完整 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66613 | TECENTRIQ CONCENTRATE FOR SOLUTION FOR INFUSION 840MG/14ML | 未提供 | 未提供 |
| HK-66341 | TECENTRIQ CONCENTRATE FOR SOLUTION FOR INFUSION 1200MG/20ML | 未提供 | 未提供 |
| HK-65567 | TECENTRIQ CONCENTRATE FOR SOLUTION FOR INFUSION 1200MG/20ML | 未提供 | 未提供 |

三張許可證皆由 Roche Hong Kong Limited 持有，狀態皆為有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（PD-L1 免疫檢查點抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：資料共收錄 75 筆交互作用，以下列出部分主要項目：
  - **重度（Major）**：Adalimumab、Baricitinib、卡介苗（BCG，Tice 株活菌）
  - **中度（Moderate）**：多種皮質類固醇（Hydrocortisone、Prednisone、Prednisolone、Dexamethasone、Methylprednisolone、Budesonide、Betamethasone、Triamcinolone、Deflazacort）、Roflumilast、Azathioprine、Alemtuzumab、Anakinra、Alefacept、破傷風類毒素疫苗、炭疽疫苗等

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 前列腺尿道上皮癌目前只有一個 Phase 1b 的間接證據，且試驗仍在進行中，沒有針對該次部位的結果，也沒有文獻支持。
- 此預測主要是原適應症（泌尿道上皮癌）的部位延伸，機轉合理，但缺乏專屬證據。藥物在香港已上市，若有進一步證據，推進的門檻不高。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌症（目前缺漏，屬阻擋性資料缺口）
- 補充詳細的作用機轉資料（MOA）
- 檢索針對前列腺尿道或尿路上皮癌次部位的臨床資料與文獻
- 確認原核准適應症是否已涵蓋此次部位（可能不需要再利用）

## 其他預測適應症（供參考）

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|---------|-----------|---------|------|
| 2 | 腎盂肉瘤樣移行細胞癌 | 99.98% | L5 | Hold |
| 3 | 浸潤性膀胱尿路上皮癌肉瘤樣變異型 | 99.98% | L5 | Hold |
| 4 | 腎盂乳突狀尿路上皮癌 | 99.98% | L5 | Hold |
| 6 | 子宮頸內膜癌 (Endocervical Carcinoma) | 99.92% | L2 | Research Question |

其中**子宮頸內膜癌**的證據最完整：有 1 個已完成的 Phase 2 試驗（[NCT02921269](https://clinicaltrials.gov/study/NCT02921269)，Atezolizumab 併用 Bevacizumab，n=11，非隨機）與 1 個已完成的 Phase 1 試驗（[NCT03738228](https://clinicaltrials.gov/study/NCT03738228)，n=40，搭配化放療）。樣本數小、缺乏隨機對照，療效證據仍需謹慎看待，可作為後續優先評估的方向。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

