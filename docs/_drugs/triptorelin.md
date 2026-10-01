---
layout: default
title: Triptorelin
parent: 僅模型預測 (L5)
nav_order: 897
evidence_level: L5
indication_count: 5
---

# Triptorelin
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

# Triptorelin：從原適應症（資料未提供）到多毛症

## 一句話總結

Triptorelin 是 GnRH 促效劑，在香港有 5 張許可證，但本次輸入資料未提供原適應症。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**無臨床試驗**，只有 **1 篇個案報告**，且該報告談的是其他藥物造成的副作用，並未支持 triptorelin 的療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5（僅有模型預測，文獻未支持 triptorelin 與多毛症的關聯） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Triptorelin 屬於 GnRH 促效劑，作用是抑制促性腺激素驅動的性荷爾蒙軸。

多毛症一般不依賴雄性素，與這個機轉的關聯偏弱。因此，這個預測目前只能視為圖譜運算的結果，機轉上的合理性有限。

唯一的文獻是一篇個案報告，描述環孢素（ciclosporin）在一位同時使用雌二醇與 triptorelin 的跨性別女性身上誘發全身性多毛。這是另一種藥物造成的副作用，並非 triptorelin 治療多毛症的證據。

排名第 2 至第 5 的預測（Ambras 型先天性全身多毛症、伴牙齒或牙周異常的畸形症候群、以 Dandy-Walker 畸形為主的症候群、遺傳性毛幹異常）同樣沒有臨床試驗，也沒有 triptorelin 相關文獻，且都缺乏合理的機轉連結。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case report | Cureus | 25 歲跨性別女性因乾癬使用環孢素後出現全身性多毛，同時服用雌二醇與 triptorelin。顯示即使在雄性素被抑制的情況下，環孢素仍可誘發多毛。這是副作用報告，不是 triptorelin 的療效證據 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51941 | DIPHERELINE PR FOR INJ 11.25MG | Beaufour Ipsen International (Hong Kong) Limited |
| HK-47655 | DIPHERELINE PR FOR INJ 3.75MG | Beaufour Ipsen International (Hong Kong) Limited |
| HK-36917 | DECAPEPTYL 0.1MG INJ SC | Ferring Pharmaceuticals Ltd |
| HK-33730 | DECAPEPTYL-CR FOR INJ 3.75MG | Ferring Pharmaceuticals Ltd |
| HK-62788 | DIPHERELINE P.R. POWDER AND SOLVENT FOR SUSPENSION FOR INJECTION 22.5MG | Beaufour Ipsen International (Hong Kong) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗，唯一的文獻是其他藥物誘發多毛的個案報告，機轉上的關聯也偏弱。
- 目前缺少香港衛生署仿單的警語與禁忌症資料，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症），補齊原適應症與安全性資料
- 補充 DrugBank 的作用機轉資料，重新評估與多毛症的機轉連結
- 檢索是否有 GnRH 促效劑直接用於多毛症（例如多囊性卵巢症候群相關多毛）的研究
- 若上述都找不到直接證據，建議不再優先推進此候選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

