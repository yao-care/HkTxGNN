---
layout: default
title: Palivizumab
parent: 僅模型預測 (L5)
nav_order: 659
evidence_level: L5
indication_count: 10
monitor_inn: "PALIVIZUMAB"
predicted_indications: ["benign neoplasm of tongue", "epiglottis neoplasm", "cervical neuroblastoma", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "tumor of testis and paratestis", "cystic neoplasm", "schwannoma of jugular foramen", "mesenchymoma", "thyroglossal duct cyst"]
last_modified_at: 2026-10-28
description: "Palivizumab：預測新適應症為良性舌部腫瘤（證據等級 L5）。原適應症：呼吸道融合病毒感染"
---

# Palivizumab
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

## Palivizumab：從呼吸道融合病毒感染到良性舌部腫瘤
{: .text-alpha }

## 一句話總結

Palivizumab 是針對呼吸道融合病毒（RSV）的單株抗體，知識圖譜中記錄的原用途為 RSV 感染。
TxGNN 模型預測它可能對**良性舌部腫瘤 (Benign Neoplasm of Tongue)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 呼吸道融合病毒感染（知識圖譜記錄；香港許可證未載明適應症文字） |
| 預測新適應症 | 良性舌部腫瘤 |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Palivizumab 是一種人源化單株抗體，標靶為 RSV 的 F 蛋白，作用是中和病毒。

這個機轉與良性舌部腫瘤的生物學之間，**找不到合理的關聯**。藥物對腫瘤組織沒有已知的標靶或作用路徑。0.9994 的高分來自 TxGNN 模型（深度學習），較可能反映模型學到的相關疾病之間的相似性，而非生物學上的依據。

同一份預測清單中的其他項目（會厭腫瘤、頸部神經母細胞瘤、下咽良性腫瘤、口底良性腫瘤、睪丸及睪丸旁腫瘤、囊性腫瘤、頸靜脈孔神經鞘瘤、間葉瘤、甲狀舌管囊腫）同樣沒有機轉或臨床證據支持，整體看來像是模型的系統性偏差。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64445 | SYNAGIS SOLUTION FOR INJECTION 100MG/1ML | 未載明 | 未載明 |
| HK-64446 | SYNAGIS SOLUTION FOR INJECTION 50MG/0.5ML | 未載明 | 未載明 |

兩張許可證均為單一成分製劑，持有人為 AstraZeneca Hong Kong Limited，狀態皆為有效。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型運算，沒有任何臨床試驗或文獻直接研究此疾病，證據等級為 L5。
- 抗 RSV F 蛋白抗體與良性舌部腫瘤之間沒有合理的機轉連結，不建議投入資源。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，確認是否有 RSV 以外的標靶。
- 取得香港衛生署的仿單，補齊核准適應症與安全性資訊（警語、禁忌）。
- 若要認真考慮此預測，需先有機轉假說與前臨床數據（如細胞或動物模型）作為依據。
- 優先檢視 TxGNN 預測是否只反映模型學到的相關疾病之間的相似性，再決定是否繼續評估其他腫瘤類預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

