---
layout: default
title: Protamine Sulfate
parent: 僅模型預測 (L5)
nav_order: 728
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Protamine sulfate：從肝素中和到 FGFR1 重排骨髓性腫瘤

## 一句話總結

Protamine sulfate（硫酸魚精蛋白）是一種帶正電的富精胺酸胜肽，藥理上用於中和肝素。
TxGNN 模型預測它可能對**FGFR1 重排相關骨髓性腫瘤 (myeloid neoplasm associated with FGFR1 rearrangement)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數 0.5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（藥理上用於中和肝素） |
| 預測新適應症 | FGFR1 重排相關骨髓性腫瘤 (myeloid neoplasm associated with FGFR1 rearrangement) |
| TxGNN 預測分數 | 50% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Protamine 是一種多陽離子、富含精胺酸的胜肽，已知作用是結合並中和肝素。

唯一可推測的關聯是：protamine 可能也會結合硫酸乙醯肝素 (heparan sulfate)，而它是 FGF/FGFR 訊號的輔助受體。不過，這種腫瘤是由持續活化的 FGFR1 融合激酶驅動，沒有資料顯示 protamine 能抑制這些激酶。這個預測只是推測，並無實證支持。

肝素中和與血液腫瘤在臨床上沒有明顯關聯，且 0.5 的分數代表模型信心很低。

## 其他預測適應症

另外 9 個預測的分數同為 0.5，證據等級皆為 L5，沒有臨床試驗或文獻，決策皆為 Hold，且均未找到合理的機轉關聯：

| 排名 | 預測適應症 | 評估 |
|------|-----------|------|
| 2 | 17q21.31 重複症候群 | 基因體拷貝數異常，與肝素中和無關 |
| 3 | 芳香環轉化酶缺乏症 (aromatase deficiency) | CYP19A1 功能喪失導致雌激素合成受損，protamine 不影響類固醇生成 |
| 4 | 口角顏面裂 (commissural facial cleft) | 先天顱顏結構畸形，全身性肝素中和胜肽無治療角色 |
| 5 | 老花眼 (presbyopia) | 晶狀體調節力隨年齡下降，protamine 對晶狀體或睫狀肌無已知作用 |
| 6 | 6q11-q14 缺失症候群 | 染色體缺失疾病，無藥理關聯 |
| 7 | 4q21 缺失症候群 | 染色體缺失疾病，無藥理關聯 |
| 8 | CBL 相關疾病 | 涉及 RAS/MAPK 訊號失調，protamine 不作用於此路徑 |
| 9 | Reynolds 症候群 | 原發性膽汁性膽管炎合併局限性硬皮症，protamine 無免疫調節或肝膽作用 |
| 10 | 葡萄糖磷酸異構酶缺乏性溶血性貧血 | 先天性糖解酶缺乏，protamine 不影響糖解或紅血球存活 |

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-16886 | PROTAMINE SULPHATE INJ BP 1% | 未載明 | 未載明 |

製造商為 VANTONE MEDICAL SUPPLIES CO LTD。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
所有預測皆為證據等級 L5，只有 0.5 的模型分數，沒有臨床試驗、文獻或可信的機轉支持。排名第 1 的 FGFR1 骨髓性腫瘤僅有推測性的 heparan sulfate 關聯，其餘預測則找不到合理的機轉。

**若要推進需要：**
- 取得香港衛生署仿單，確認原適應症、警語與禁忌症（目前為阻擋性資料缺口）
- 從 DrugBank 補齊作用機轉資料
- 針對 FGFR1 骨髓性腫瘤，進行 protamine 與 heparan sulfate／FGFR 訊號的前臨床機轉驗證
- 確認給藥途徑與劑型是否適用於血液腫瘤治療情境

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

