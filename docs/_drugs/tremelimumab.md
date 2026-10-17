---
layout: default
title: Tremelimumab
parent: 僅模型預測 (L5)
nav_order: 901
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tremelimumab：預測新適應症為糖尿病性白內障 (Diabetic Cataract)（證據等級 L5）。原適應症：香港許可證未載明核准適應症"
monitor_inn: "Tremelimumab"
predicted_indications: ["diabetic cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "craniostenosis cataract", "mature cataract", "tetanic cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic retinopathy"]
---

# Tremelimumab
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

# Tremelimumab：從（原適應症資料未提供）到糖尿病性白內障

## 一句話總結

Tremelimumab（商品名 IMJUDO）是一種抗 CTLA-4 單株抗體，屬於免疫檢查點抑制劑，用於腫瘤治療。
TxGNN 模型預測它可能對**糖尿病性白內障 (Diabetic Cataract)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症 |
| 預測新適應症 | 糖尿病性白內障 (Diabetic Cataract) |
| TxGNN 預測分數 | 98.49% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tremelimumab 是抗 CTLA-4 的單株抗體，透過阻斷 CTLA-4 與 CD80/CD86 的結合來增強 T 細胞活性。它已與 durvalumab 合併，獲 FDA 核准用於不可切除的肝細胞癌（2022 年 10 月）。

然而，**這個預測的合理性很低**。白內障（包含糖尿病性白內障）的成因主要是氧化壓力、多元醇路徑與蛋白質糖化，與 T 細胞檢查點路徑沒有已知的關聯。0.985 的高分可能來自知識圖譜中白內障各亞型彼此相近的網路結構，而非真實的生物學機轉。

此外，檢查點抑制劑可能引發免疫相關眼部不良反應（如葡萄膜炎），也可能惡化免疫相關的代謝問題，這在安全性上是疑慮而非助益。

同一批預測中，排名前 10 的適應症幾乎都是各型白內障（第二型糖尿病相關、未成熟、成熟、老年性、核性、皮質性等）以及糖尿病視網膜病變，皆同樣只有模型預測，沒有試驗或文獻。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68211 | IMJUDO CONCENTRATE FOR SOLUTION FOR INFUSION 300MG/15ML | 濃縮輸注液 | 資料未載明 |
| HK-68210 | IMJUDO CONCENTRATE FOR SOLUTION FOR INFUSION 25MG/1.25ML | 濃縮輸注液 | 資料未載明 |

兩張許可證皆為有效，持有廠商為 AstraZeneca Hong Kong Limited。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 CTLA-4 單株抗體，非傳統細胞毒性藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：本次查詢僅得到 1 筆藥理學層面的紀錄，即其標靶 CTLA-4 (CD152)，並非與其他藥物的臨床交互作用。

其餘警語與禁忌症資料，請參考原廠仿單。

從藥理角度需特別留意：檢查點抑制劑可能引起免疫相關不良反應，包括眼部炎症與免疫相關內分泌或代謝異常。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測僅來自知識圖譜模型（證據等級 L5），沒有任何試驗、文獻或機轉資料支持。
- 全身性免疫檢查點抑制劑用於以手術即可有效處理的白內障，風險與效益明顯失衡，且可能加重眼部免疫毒性。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症資料
- 補齊詳細的作用機轉資料，並釐清 CTLA-4 與晶體病變之間是否存在任何機轉關聯
- 進行前臨床研究，驗證是否有生物學上的合理性
- 在此之前，建議不投入資源推進此適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

