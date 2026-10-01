---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine：從 SNRI 類抗憂鬱藥到嬰兒良性陣發性斜頸

## 一句話總結

Duloxetine 是血清素與正腎上腺素再回收抑制劑（SNRI），香港已有多張許可證上市。
TxGNN 模型預測它可能對**嬰兒良性陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明適應症文字（藥理類別為 SNRI） |
| 預測新適應症 | 嬰兒良性陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Duloxetine 屬於 SNRI，透過抑制血清素與正腎上腺素的再回收發揮作用，但資料庫中沒有記錄更完整的機轉描述。

嬰兒良性陣發性斜頸是嬰幼兒期的陣發性動作疾患，可能與離子通道異常或偏頭痛譜系有關。目前沒有資料顯示 SNRI 的藥理作用與這類疾病的致病機轉有明確關聯。

需要特別注意：TxGNN 對多數候選適應症的分數都落在 0.996–0.998，這個高分並沒有鑑別力。它較可能反映知識圖譜中的鄰近關係，而不是藥物特異性的證據。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-68872 | DULOXETINE DELAYED-RELEASE CAPSULES USP 60MG | Controlled Medications Limited |
| HK-64014 | DULOXETINE SANDOZ DELAYED RELEASE CAPSULES 30MG | Sandoz Hong Kong Limited |
| HK-68039 | DULOXETINE GASTRO-RESISTANT CAPSULES 30MG | I & C (Hong Kong) Limited |
| HK-68871 | DULOXETINE DELAYED-RELEASE CAPSULES USP 30MG | Controlled Medications Limited |
| HK-65544 | SEBATA GASTRO-RESISTANT CAPSULES 30MG | LSB (HK) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
這個預測沒有臨床試驗、文獻或可信的機轉支持，屬於 L5 等級。分數缺乏鑑別力，且疾病族群為嬰幼兒，貿然推進的風險與收益不成比例。

**補充：** 同一份預測清單中，**強迫症 (OCD)**（排名第 3）的證據明顯較多，包括 1 項已完成的 Phase 4 試驗（NCT00464698，n=20）、1 項雙盲增強治療 RCT（PMID 27811556）、開放標籤研究與多篇病例報告，證據等級為 L2。若要投入資源，建議優先評估該適應症，且應定位為 SSRI 之後的後線或增強治療選項。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料（目前為阻斷性缺口，無法進入安全性篩選）
- 取得 duloxetine 的作用機轉資料（例如查詢 DrugBank）
- 針對嬰兒良性陣發性斜頸，先做系統性文獻檢索，確認是否有任何機轉或臨床線索
- 評估嬰幼兒族群使用 duloxetine 的安全性與劑型可行性

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

