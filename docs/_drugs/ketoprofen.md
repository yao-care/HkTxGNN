---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 5
---

# Ketoprofen
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

# Ketoprofen：從非類固醇消炎止痛藥（NSAID）到肢中發育不良 Hunter-Thompson 型

## 一句話總結

Ketoprofen 是一種非選擇性 COX 抑制型的非類固醇消炎止痛藥（NSAID）。
TxGNN 模型預測它可能對**肢中發育不良 Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效。
目前有 **0 個臨床試驗**和 **0 篇文獻**支持，僅有模型預測，機轉上也找不到可信的關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 肢中發育不良 Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5（僅模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。已知 Ketoprofen 屬於 NSAID，透過非選擇性抑制 COX 酵素來減少前列腺素合成，用於消炎止痛。

這個預測在機轉上**難以成立**。此疾病是遺傳性骨骼發育不良，主要與 GDF5/CDMP1 功能喪失有關，會干擾軟骨生成。COX 抑制並不作用於這條路徑。0.9998 的高分較可能反映知識圖譜的拓樸結構，而不是實際的生物學關聯。

模型對本藥的其他預測也是類似情況，證據都停在 L5，建議皆為 Hold：

| 排名 | 預測疾病 | 分數 | 機轉評估 |
|------|---------|------|---------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.98% | 無可信關聯，屬骨骼與牙釉質發育異常 |
| 3 | Myosclerosis | 99.98% | 關聯薄弱，NSAID 至多緩解症狀，無疾病修飾證據 |
| 4 | Brachyolmia | 99.98% | 無可信關聯，屬遺傳性骨骼發育不良 |
| 5 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.98% | 無可信關聯，屬先天性眼部與肢體畸形 |

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68597 | HOHOTAPE MEDICAL PLASTER 30MG | BEST UNITED MARKETING LIMITED |
| HK-57684 | KETO-TDDS PLASTER 30MG | WELL FAVOURED LTD |
| HK-62603 | DERUMA-60 CATAPLASMA PLASTER 60MG | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-18544 | KETOFEN CAP 50MG | WILCOME PHARMACEUTICAL CO LTD |
| HK-58787 | MECOL PATCH 30MG | WELLDONE PHARMACEUTICALS LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有任何臨床試驗或文獻。
- 預測疾病的病理機轉（GDF5 相關的軟骨生成障礙）與 COX 抑制無關，因此不建議推進。

**若要推進需要：**
- 補齊 DrugBank 的 MOA 資料，重新評估機轉關聯。
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選。
- 找到能連結 COX/前列腺素路徑與此疾病的實驗或文獻證據；若找不到，建議放棄此預測。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

