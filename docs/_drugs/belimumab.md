---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Belimumab：預測新適應症為原發性血小板釋放障礙 (primary release disorder of platelets)（證據等級 L5）。原適應症：全身性紅斑性狼瘡、兒童全身性紅斑性狼瘡"
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
---

# Belimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Belimumab：從全身性紅斑性狼瘡到原發性血小板釋放障礙
{: .text-alpha }

## 一句話總結

Belimumab 是一種抑制 BLyS (BAFF) 的單株抗體，原本用於治療全身性紅斑性狼瘡（含兒童型）。
TxGNN 模型預測它可能對**原發性血小板釋放障礙 (primary release disorder of platelets)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 全身性紅斑性狼瘡、兒童全身性紅斑性狼瘡 |
| 預測新適應症 | 原發性血小板釋放障礙 (primary release disorder of platelets) |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Belimumab 是一種單株抗體，抑制可溶性 BLyS (BAFF)，進而減少自體反應性 B 細胞的存活，這是它在紅斑性狼瘡中發揮療效的基礎。

然而，原發性血小板釋放障礙通常是遺傳性的血小板功能缺陷（顆粒分泌或訊號傳遞異常），並非由 B 細胞介導。因此，機轉上看不出合理的關聯。0.9996 的高分僅是模型預測，沒有試驗或文獻佐證，**不宜單憑分數推論有效**。

### 其他預測適應症（同樣僅有模型預測，皆無試驗或文獻）

| 排名 | 預測疾病 | TxGNN 分數 | 機轉關聯評估 |
|------|---------|-----------|-------------|
| 2 | 假性類血友病因子缺乏症 (pseudo-von Willebrand disease) | 0.9996 | 為 GP1BA 功能增強突變，與 BAFF 無關 |
| 3 | 血小板無力症 (Glanzmann thrombasthenia) | 0.9988 | 為 αIIbβ3 缺陷；僅輸血後產生同種抗體這一點有間接、推測性的關聯 |
| 4 | 胎兒及新生兒同種免疫性血小板低下症 (FNAIT) | 0.9959 | 母體同種抗體介導，B 細胞/漿細胞生物學上較有理論關聯，但懷孕期安全性資料有限，且 IgG1 抗體可通過胎盤 |
| 5 | 重度非增殖性糖尿病視網膜病變 | 0.9905 | 以微血管病變、VEGF 和發炎為主，無 BAFF 角色 |
| 6 | 體染色體顯性巨血小板減少症 | 0.9904 | 為巨核細胞/血小板生成的遺傳缺陷，非自體免疫 |

其中 FNAIT 在理論上最合理，但仍只是假說，若要研究，需以研究問題的方式審慎處理，並考量胎兒暴露風險。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66372 | BENLYSTA SOLUTION FOR INJECTION IN PRE-FILLED PEN 200MG/ML | 注射劑（預填充筆） | 資料未載明 |
| HK-61385 | BENLYSTA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 400MG | 輸注濃縮液用粉劑 | 資料未載明 |
| HK-61384 | BENLYSTA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 120MG | 輸注濃縮液用粉劑 | 資料未載明 |

三張許可證皆為單一成分、狀態有效，持證商為 GlaxoSmithKline Limited。

## 安全性考量

- **藥物交互作用**：共查得 69 筆交互作用，以下為部分代表：
  - **Major（嚴重）**：Adalimumab、Baricitinib、Certolizumab pegol、卡介苗（BCG，Tice 株活菌）
  - **Moderate（中度）**：Azathioprine、Alemtuzumab、Anakinra、Canakinumab、Roflumilast、破傷風類毒素、炭疽疫苗、霍亂活疫苗等
  - **Minor（輕微）**：各種鋅鹽（醋酸鋅、葡萄糖酸鋅、硫酸鋅、氯化鋅）

  整體而言，與其他免疫抑制劑/生物製劑併用以及活性減毒疫苗，是需要特別留意的重點。

- **懷孕相關**：Belimumab 為 IgG1 抗體，可通過胎盤，且懷孕期安全性資料有限。若考慮用於 FNAIT 等情境，須特別評估胎兒暴露風險。

警語與禁忌症的詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 六個預測適應症皆只有模型分數，沒有任何臨床試驗或文獻（證據等級 L5），且多數疾病的病理機轉與 BAFF/B 細胞無關。
- 目前也缺乏作用機轉與仿單安全性資料，無法進入安全性篩選階段。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，補足機轉關聯分析
- 下載並解析香港衛生署的仿單，補齊警語、禁忌症與核准適應症
- 若要優先探索，可從 FNAIT 著手，先做系統性文獻回顧與機轉驗證（含胎盤transfer 與懷孕安全性評估）
- 在取得任何前臨床或臨床證據前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

