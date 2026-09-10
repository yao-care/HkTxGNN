---
layout: default
title: Perflubutane
parent: 僅模型預測 (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Perflubutane
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

# Perflubutane：從超音波顯影劑到支氣管炎

## 一句話總結

Perflubutane（DrugBank ID: DB12821）目前在台灣未上市，且缺乏完整的原始適應症與作用機轉資料；已知它是聲學顯影用氣體微球（超音波顯影劑）。TxGNN 模型預測其可能對**支氣管炎 (Bronchitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，證據包本身的機轉分析也明確指出此藥缺乏相關藥理活性。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無台灣核准適應症資料（未上市）；已知用途為超音波顯影用氣體微球 |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 97.33% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 台灣上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap）。根據證據包中的已知資訊，Perflubutane 是一種聲學顯影用氣體微球，臨床上用於超音波影像顯影（如腫瘤/肝臟病灶顯影），並非具有全身性藥理活性的治療性藥物。

證據包中對此預測的機轉關聯分析明確指出：Perflubutane「無已知抗發炎/抗感染藥理活性，與支氣管炎治療無可辨識生化路徑」，並研判該預測分數較可能反映知識圖譜中**顯影應用的拓撲鄰近性**（例如與呼吸道影像檢查相關的節點連結），而非真實的藥理機轉關聯。同樣的問題也出現在其餘 9 個預測適應症中——每一項的機轉分析都表示缺乏對應的生化合理性。

換句話說，這批預測目前應被視為**知識圖譜結構訊號**，而非具科學實證支持的老藥新用候選。

## 全部候選適應症總表

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 機轉合理性 |
|------|-----------|-----------|---------|-----------|
| 1 | Bronchitis | 97.33% | L5 | 無已知機轉支持，疑為拓撲鄰近性 |
| 2 | Bronchial neoplasm | 92.51% | L5 | 無細胞毒性/標靶機轉，疑與顯影用途混淆 |
| 3 | Severe nonproliferative diabetic retinopathy | 90.33% | L5 | 無血管新生抑制證據 |
| 4 | Gastroduodenitis | 90.22% | L5 | 無胃黏膜保護機轉 |
| 5 | Peptic ulcer disease | 88.91% | L5 | 無抑酸/黏膜修復證據 |
| 6 | Chagas cardiomyopathy | 88.13% | L5 | 無抗錐蟲或心肌保護機轉 |
| 7 | Infective urethral stricture | 88.08% | L5 | 無抗菌/組織重塑機轉 |
| 8 | Post-infectious syndrome | 87.93% | L5 | 適應症定義模糊，無支持證據 |
| 9 | Diabetic retinopathy | 87.89% | L5 | 同第 3 項問題 |
| 10 | Post-bacterial disorder | 87.89% | L5 | 無抗菌/修復機轉證據 |

10 個候選適應症皆為 L5 等級，且經 ClinicalTrials.gov、ICTRP、PubMed 三方查詢（共 30 筆查詢）均無任何相關結果。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

Perflubutane 於台灣未上市，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單（TFDA 仿單警語/禁忌為 Blocking 等級資料缺口，尚無法取得）。

## 結論與下一步

**決策：Hold**

**理由：**
全部 10 個預測適應症皆僅為 L5 等級（純模型預測），無任何臨床試驗或文獻佐證；證據包自身的機轉分析也一致指出 Perflubutane 缺乏對應藥理活性，預測結果較可能源於知識圖譜拓撲結構而非真實生物學關聯。加上台灣未上市、仿單警語與禁忌屬 Blocking 缺口，目前無法進入安全性初評（S1）。

**若要推進需要：**
- 取得 TFDA（或適用藥政機關）仿單原文，補齊警語/禁忌資料（Blocking 缺口）
- 向 DrugBank 或原廠查證完整作用機轉（MOA）
- 針對排名較高的候選適應症（如 bronchitis）進行獨立文獻/臨床試驗檢索，確認是否存在圖譜資料庫未收錄的證據
- 若後續資料仍支持「顯影劑拓撲鄰近性」假說，建議將此候選標記為低優先級，暫緩投入資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

