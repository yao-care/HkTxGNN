---
layout: default
title: Methoxy Polyethylene Glycol-Epoetin Beta
parent: 僅模型預測 (L5)
nav_order: 564
evidence_level: L5
indication_count: 5
---

# Methoxy Polyethylene Glycol-Epoetin Beta
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Methoxy Polyethylene Glycol-Epoetin Beta：從紅血球生成刺激劑（ESA）到血小板釋放異常

## 一句話總結

Methoxy Polyethylene Glycol-Epoetin Beta（商品名 Mircera）是一種紅血球生成刺激劑（ESA），原適應症資料未提供。
TxGNN 模型預測它可能對**血小板原發性釋放異常 (Primary Release Disorder of Platelets)** 有效。
目前**沒有臨床試驗和文獻**支持，只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 血小板原發性釋放異常 (Primary Release Disorder of Platelets) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知它是作用於 EPO 受體的 ESA，主要刺激紅血球前驅細胞。

這個預測的可能路徑是尿毒症血小板功能異常。血比容升高，可能改善血小板與血管壁的交互作用。但這是間接的機轉，而且針對的是後天性疾病。先天性的血小板儲存或釋放缺陷並沒有這方面的證據。由於缺乏經整理的 MOA 資料，這條關聯無法驗證。

TxGNN 對其他 4 個疾病也給出高分（99.1%–99.3%）：Glanzmann 血小板無力症、假性血管性血友病、重度非增殖性糖尿病視網膜病變、肝素輔因子 2 缺乏症。這些預測同樣沒有臨床證據。前三者屬遺傳性缺陷，ESA 無法矯正，高分可能來自知識圖譜中血液或出血疾病節點的鄰近關係。糖尿病視網膜病變則有安全疑慮：EPO 的促血管新生作用，可能讓視網膜病變惡化。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-56445 | MIRCERA INJ 150MCG/0.3ML (PRE-FILLED SYRINGE) | ROCHE HONG KONG LIMITED |
| HK-56442 | MIRCERA INJ 50MCG/0.3ML (PRE-FILLED SYRINGE) | ROCHE HONG KONG LIMITED |
| HK-56450 | MIRCERA INJ 75MCG/0.3ML (PRE-FILLED SYRINGE) | ROCHE HONG KONG LIMITED |
| HK-56449 | MIRCERA INJ 200MCG/0.3ML (PRE-FILLED SYRINGE) | ROCHE HONG KONG LIMITED |
| HK-56447 | MIRCERA INJ 100MCG/0.3ML (PRE-FILLED SYRINGE) | ROCHE HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，就預測適應症而言，ESA 有血栓栓塞風險，用於促血栓體質的疾病（如肝素輔因子 2 缺乏症）需審慎評估。對糖尿病視網膜病變，則要先做安全性審查，再考慮療效。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測都只有模型分數，沒有任何臨床試驗或文獻。
- 已知機轉與多數預測疾病並不吻合，部分還有潛在安全疑慮。
- 香港雖已上市，但缺少仿單的警語與禁忌症資料，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署（Department of Health）的仿單，補齊警語與禁忌症
- 補充 DrugBank 的作用機轉（MOA）資料
- 對血小板釋放異常做針對性文獻檢索，特別是 ESA 用於尿毒症血小板功能異常的資料
- 若考慮糖尿病視網膜病變，先評估 ESA 相關視網膜安全性

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

