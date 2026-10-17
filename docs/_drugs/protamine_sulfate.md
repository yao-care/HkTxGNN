---
layout: default
title: Protamine Sulfate
parent: 僅模型預測 (L5)
nav_order: 743
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Protamine Sulfate：預測新適應症為FGFR1 重排相關骨髓腫瘤 (myeloid neoplasm associated with FGFR1 rearrangement)（證據等級 L5）。原適應症：許可證未載明"
monitor_inn: "Protamine sulfate"
predicted_indications: ["myeloid neoplasm associated with FGFR1 rearrangement", "chromosome 17q21.31 duplication syndrome", "aromatase deficiency", "commissural facial cleft", "presbyopia", "chromosome 6q11-q14 deletion syndrome", "chromosome 4q21 deletion syndrome", "CBL-related disorder", "Reynolds syndrome", "hemolytic anemia due to glucophosphate isomerase deficiency"]
---

# Protamine Sulfate
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

# Protamine sulfate：從肝素中和劑到骨髓腫瘤（FGFR1 重排相關）的預測評估

## 一句話總結

Protamine sulfate（硫酸魚精蛋白）是一種帶陽離子、富含精胺酸的胜肽，臨床上常用來中和肝素，目前香港許可證並未載明原適應症文字。
TxGNN 模型預測它可能對 **FGFR1 重排相關骨髓腫瘤 (myeloid neoplasm associated with FGFR1 rearrangement)** 有效，但預測分數僅 50%，目前**沒有任何臨床試驗或文獻**支持，屬於僅有模型預測的階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | FGFR1 重排相關骨髓腫瘤 (myeloid neoplasm associated with FGFR1 rearrangement) |
| TxGNN 預測分數 | 50.0% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 protamine sulfate 是帶正電的精胺酸富集胜肽，透過與肝素結合而中和其抗凝血作用。目前沒有證據顯示它能抑制 FGFR1 訊號傳遞。

理論上，protamine 可能與部分結合肝素的生長因子結合，但這只是推測，對此疾病並無任何研究支持。50% 的預測分數區辨力很低，不足以作為證據。

因此，這個預測在機轉上**無法成立**，應視為模型產生的假說，而非有依據的再利用方向。

其餘九個預測適應症（17q21.31 重複症候群、芳香環轉化酶缺乏症、口角顏面裂、老花眼、6q11-q14 缺失症候群、4q21 缺失症候群、CBL 相關疾患、Reynolds 症候群、GPI 缺乏溶血性貧血）同樣只有 50% 的預測分數，也都沒有試驗、文獻或可信的機轉連結，一律評為 L5、建議 Hold。

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
| HK-16886 | PROTAMINE SULPHATE INJ BP 1% | 未載明 | 未載明 |

廠商：VANTONE MEDICAL SUPPLIES CO LTD（單方，有效）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

另外，在已預測的適應症評估中，曾提及 protamine 本身可能引起不良的血液學與血流動力學作用，若考慮用於任何新適應症，需特別留意。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測僅依據 TxGNN 分數（50%），沒有臨床試驗、文獻或可信的機轉連結，證據等級為 L5。
- 原適應症與作用機轉資料缺漏，仿單的警語與禁忌也尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 從 DrugBank 補充作用機轉（MOA）資料
- 針對 FGFR1 重排相關骨髓腫瘤，進行文獻與前臨床證據檢索，確認是否存在任何機轉連結
- 在沒有上述證據前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

