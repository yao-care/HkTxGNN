---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 815
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept：從原適應症（資料缺漏）到急性淋巴芽細胞白血病

## 一句話總結

Sotatercept 是一種 ActRIIA-Fc 融合蛋白，香港已有 4 張 WINREVAIR 注射劑許可證，但 Evidence Pack 未載明原適應症。
TxGNN 模型預測它可能對**急性淋巴芽細胞白血病 (Acute Lymphoblastic Leukemia)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（許可證未提供適應症文字） |
| 預測新適應症 | 急性淋巴芽細胞白血病 (Acute Lymphoblastic Leukemia) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依預測紀錄的說明，Sotatercept 是 ActRIIA-Fc 配體捕捉劑，會結合 activin、GDF、BMP 等配體。Activin 訊號會影響紅血球生成與造血調控。

不過，目前**沒有找到 activin 訊號與急性淋巴芽細胞白血病生物學之間的確立關聯**。此外，Sotatercept 會提高血紅素，也可能造成血小板低下，用於白血病時情況會更複雜。因此這個預測的合理性偏弱，分數高可能只反映知識圖譜中的關聯訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68795 | WINREVAIR 凍晶注射劑 60mg | Merck Sharp & Dohme (Asia) Ltd |
| HK-68794 | WINREVAIR 凍晶注射劑 45mg | Merck Sharp & Dohme (Asia) Ltd |
| HK-68792 | WINREVAIR 凍晶粉末與溶劑注射劑 45mg | Merck Sharp & Dohme (Asia) Ltd |
| HK-68793 | WINREVAIR 凍晶粉末與溶劑注射劑 60mg | Merck Sharp & Dohme (Asia) Ltd |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，預測紀錄提到本藥有出血與微血管擴張 (telangiectasia) 的警語，並可能造成血小板低下。若用於血液惡性腫瘤，這些風險需要特別評估。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測分數，沒有臨床試驗、文獻或明確的機轉連結，證據等級為 L5。
- 血小板低下與出血風險與白血病治療情境相衝突，且香港仿單的警語與禁忌資料尚未取得。

**若要推進需要：**
- 取得香港衛生署仿單，補齊原適應症、警語與禁忌症。
- 從 DrugBank 補充作用機轉資料。
- 針對 activin／ActRIIA 與急性淋巴芽細胞白血病的關聯做系統性文獻檢索，確認是否有前臨床證據。
- 同批預測中，**藥物誘發骨質疏鬆 (drug-induced osteoporosis)**（分數 99.65%）的機轉最合理：activin A 抑制在前臨床模型中可促進骨形成。建議優先對它做針對性文獻檢索。
- 糖尿病視網膜病變相關的 3 筆預測與泌尿上皮癌相關的 4 筆預測，各自高度重疊，可能出自同一圖譜訊號，不宜視為獨立證據。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

