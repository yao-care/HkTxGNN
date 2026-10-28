---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Degarelix：預測新適應症為多毛症 (Hypertrichosis)（證據等級 L5）。原適應症：許可證資料未載明（依藥理類別推測為前列腺癌，需確認）"
monitor_inn: "DEGARELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
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

## Degarelix：從前列腺癌（GnRH 拮抗劑）到毛髮過多症的預測評估
{: .text-alpha }

> 註：許可證資料中未提供原適應症文字，上述「前列腺癌」依預測依據中的描述（degarelix 僅上市用於前列腺癌）推得，需以原廠仿單確認。

## 一句話總結

Degarelix 是 GnRH 受體拮抗劑，在香港已有上市許可證。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測，機轉上的關聯也偏弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（依藥理類別推測為前列腺癌，需確認） |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。根據已知資訊，degarelix 是 GnRH 受體拮抗劑，會抑制 LH/FSH 分泌，進而降低睪固酮及下游雄性素。

然而，多毛症 (hypertrichosis) 一般**不是雄性素驅動**的疾病（與 hirsutism 不同），因此雄性素抑制的機轉關聯薄弱。高達 0.9999 的分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，並非生物學證據，亦無實際研究佐證。

前 10 名預測中，其他項目（Ambras 症候群、Dandy-Walker 相關症候群、遺傳性毛幹異常、蕁麻疹等）同樣缺乏合理機轉。相對而言，**中樞性早熟 (central precocious puberty)**（預測分數 0.9967）的機轉最合理：GnRH 軸抑制本就是此病的治療原則（目前使用 GnRH 促效劑），GnRH 拮抗劑在理論上可行，但缺乏兒童資料，也沒有試驗或文獻，仍屬研究假說。家族性男性限定早熟（testotoxicosis）則因 LHCGR 活化突變不受上游 GnRH 控制，機轉上不匹配。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61179 | FIRMAGON POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 120MG | 注射劑（粉劑加溶劑；許可證未載明） | 許可證未載明 |
| HK-61178 | FIRMAGON POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 80MG | 注射劑（粉劑加溶劑；許可證未載明） | 許可證未載明 |

製造商：FERRING PHARMACEUTICALS LTD

## 細胞毒性

Degarelix 屬荷爾蒙治療（GnRH 拮抗劑），並非傳統細胞毒性藥物，本章節不適用。

## 安全性考量

- **知識圖譜標示的相關疾病風險**（來自藥物－疾病關聯，非仿單內容）：long QT 症候群（含家族性）、torsades de pointes、肝臟疾病、膽囊疾病、鉀缺乏。使用前需謹慎評估心律與電解質狀態。
- **藥物交互作用**：共查得 100 筆，以下為部分重點：
  - **嚴重 (Major)**：Cisapride、Dolasetron（可能與 QT 延長風險相關）
  - **中度 (Moderate)**：Clarithromycin、Levofloxacin、Ondansetron、Granisetron、Palonosetron、Famotidine、Loperamide，以及多種瀉劑（Bisacodyl、Picosulfuric acid、Polyethylene glycol、Lactulose、Lactitol、Magnesium citrate、Magnesium hydroxide、Castor oil、Glycerin、Mineral oil）
  - **輕微 (Minor)**：Metronidazole

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測均為 L5（僅模型預測），沒有任何臨床試驗或文獻；排名第一的多毛症在機轉上也缺乏合理性。
- 相對值得追蹤的是中樞性早熟，可列為研究問題，但目前尚無支持證據。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症），並補齊作用機轉資料
- 針對中樞性早熟進行系統性文獻回顧，評估 GnRH 拮抗劑的既有研究與兒童安全性
- 若仍考慮多毛症，需先釐清其病因是否與雄性素相關，否則不建議推進
- 在 QT 風險與藥物交互作用方面建立監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

