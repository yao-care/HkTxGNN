---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 656
evidence_level: L5
indication_count: 5
---

# Pazopanib
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

# Pazopanib：從原適應症（資料未提供）到神經母細胞瘤相關腎細胞癌

## 一句話總結

Pazopanib 是一種多標靶激酶抑制劑，已在香港取得 5 張許可證，但本次資料未提供其核准適應症。
TxGNN 模型預測它可能對**神經母細胞瘤相關腎細胞癌 (Renal Cell Carcinoma Associated with Neuroblastoma)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證的適應症欄位皆為空白） |
| 預測新適應症 | 神經母細胞瘤相關腎細胞癌 (Renal Cell Carcinoma Associated with Neuroblastoma) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。Pazopanib 屬於多標靶酪胺酸激酶抑制劑（抑制 VEGFR / PDGFR / c-Kit），透過抗血管新生與抑制腫瘤增殖發揮作用。從這個機轉看，它對腎細胞癌有一般性的合理依據。

不過，這個預測的高分很可能來自「腎細胞癌」層級在知識圖譜上的相近性，而不是這個罕見亞型本身的證據。這個亞型與神經母細胞瘤相關，目前沒有任何專屬的臨床試驗或文獻。因此，現有資料無法建立針對此亞型的機轉連結。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68611 | PAZOPANIB TEVA TABLETS 200MG | Teva Pharmaceutical Hong Kong Limited |
| HK-68625 | PAZOPANIB SANDOZ TABLETS 200MG | Sandoz Hong Kong Limited |
| HK-68006 | TYKIPAZ TABLETS 200MG | Lotus Pharmaceutical HK Limited |
| HK-62096 | VOTRIENT TAB 200MG (SPAIN) | Novartis Pharmaceuticals (HK) Limited |
| HK-67932 | VOTRIENT TABLETS 200MG | Novartis Pharmaceuticals (HK) Limited |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
這個預測只有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。高分很可能反映的是腎細胞癌整體的圖譜相近性，而不是這個罕見亞型的專屬訊號。

**若要推進需要：**
- 取得此亞型的任何臨床或轉譯研究證據（目前為零）
- 補齊 DrugBank 的作用機轉資料，以及香港衛生署仿單的警語與禁忌症
- 確認香港許可證的核准適應症，以釐清原適應症

**補充：**同一份 Evidence Pack 中，另有兩個證據較強的預測值得優先評估：
- **未分類腎細胞癌**：L2，有 1 個已完成的 Phase 3 試驗（NCT01613846，間接證據）、1 項單臂 Phase 2 研究（PMID 28546525）及多項回溯性世代研究，建議 Proceed with Guardrails。
- **脂肪肉瘤**：L2，有多個 pazopanib Phase 2 試驗，包括脂肪肉瘤專屬的 NCT01506596，標為 Research Question。

建議另行產出這兩個適應症的報告。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

