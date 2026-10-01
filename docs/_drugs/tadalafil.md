---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 831
evidence_level: L5
indication_count: 5
---

# Tadalafil
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

# Tadalafil：從（原適應症資料缺漏）到 Ambras 型全身性多毛症

## 一句話總結

Tadalafil 在香港已有多張上市許可證，但本次輸入資料沒有載明原適應症。
TxGNN 模型預測它可能對 **Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅為模型預測（L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Tadalafil 屬於 PDE5 抑制劑，一般認為會提高 cGMP 濃度，但輸入資料未提供原適應症和完整機轉，因此無法評估與新適應症的關聯。

Ambras 症候群是罕見的先天性疾患，通常認為與 8q 染色體上 TRPS1 附近的結構重排有關。從 PDE5 抑制到這個遺傳成因之間，目前找不到合理的作用路徑。

這個高分較可能是知識圖譜的人為關聯（例如與多毛症、毛髮表型相關疾病叢集的圖譜距離接近），不能視為機轉上的支持。排名前五的其他預測也有類似問題：

- 多毛症（泛稱）：只能推測 cGMP／血管擴張與毛髮生長有關，且無法判斷是有益還是反而加重毛髮過多。
- 牙齒／牙周異常相關畸形症候群：檢索到的文獻是一般牙周炎資料，標題都未提及 tadalafil 或 PDE5 抑制劑，屬關鍵字比對。
- Dandy-Walker 畸形相關症候群：這是胚胎期的結構性神經發育缺陷，PDE5 抑制劑沒有可辨識的矯正機轉。
- 遺傳性毛幹異常：屬角蛋白或結構蛋白基因變異，PDE5 抑制對毛幹結構沒有已知作用。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

共 20 張許可證，以下列出 5 張。許可證資料未提供核准適應症，劑型欄位也是空白，品名皆為錠劑（Tablets）。

| 許可證號 | 品名 | 持證廠商 |
|---------|------|---------|
| HK-68929 | CIATUFF 10 TABLETS 10MG | AUROBINDO PHARMA LIMITED |
| HK-65022 | ERETAF-20 TABLETS 20MG | HOVID LIMITED |
| HK-68281 | TADALAFIL AZEVEDOS TABLETS 20MG | WA MAN (HK) LIMITED |
| HK-66745 | DURACOR TABLETS 20MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-66950 | FIP TADALAFIL TABLETS 20MG | WILSON TRADING COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數，沒有試驗或文獻佐證，也找不到可信的機轉路徑。
- 預測疾病多為先天性結構或遺傳異常，與 PDE5 抑制劑的作用方式明顯不符，高分很可能是圖譜人為關聯。

**若要推進需要：**
- 取得 DrugBank 的完整作用機轉資料，並確認 tadalafil 的原適應症。
- 取得香港衛生署仿單，補齊警語與禁忌症，才能進入安全性篩選。
- 針對 Ambras 症候群與 PDE5/cGMP 通路做專門的文獻檢索，確認是否有前臨床或病例報告。
- 若沒有任何直接證據，建議改看排名較後、機轉較合理的預測，或停止追蹤此候選。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

